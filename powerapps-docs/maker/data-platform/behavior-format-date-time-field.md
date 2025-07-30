---
title: "Behavior and format of the Date and Time column in Microsoft Dataverse | MicrosoftDocs"
description: Understand the format of date and time columns. 
ms.custom: ""
ms.date: 06/18/2025
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
contributors:
  - tahoon-ms
---
# Behavior and format of the date and time column

In Microsoft Dataverse, you can specify how date and time values are shown to users and how they're adjusted for time zones.

Two options are available for date and time columns.

- **Behavior**: Whether to adjust values for time zones.
- **Format**: Whether to display the time portion of the value.

## Behavior

Dataverse stores all date and time values in UTC time zone. When your app displays values or processing values entered by users, Dataverse and model-driven apps can adjust for the user's time zone with these **Behavior** options.

- **User local**: Adjust values for the user's time zone. This is the default behavior for the **Date and time** format. You can [change this once to another behavior](#change-user-local-behavior).
- **Time zone independent**: No time zone conversion. This is the default behavior for the **Date only** format. 
- **Date only**: No time zone conversion. Unlike **Time zone independent**, the time portion isn't stored.

The user's time zone is set in [personal options](../../user/set-personal-options.md#general-tab-options), not the system time zone in Windows, Android, iOS, or macOS. However, the [system time zone might affect client scripts that work with JavaScript Dates](#get-values-with-client-api).

## Format

All date and time columns have a time portion unless its behavior is **Date Only**. **Format** determines whether to display the time portion of the value.

- **Date and time**: Displays the date and time of the value.
- **Date only**: Displays the date portion of the value only.

> [!NOTE]
> Users can still change the time portion if the **Format** is **Date Only**. For example, with Web API calls or by using a control that has the time portion. This is different from **Date only** **Behavior**, where the time portion is not stored at all.

## Usage guidelines

Use **Time zone independent** behavior when time zone information isn't required, such as hotel check-in times. With this selection, users in all time zones see the same date and time value.

Use **Date only** behavior when information about the time of the day and the time zone isn't required, such as birthdays or anniversaries. With this selection, users in all time zones see the exact same date value.

**Time zone independent** behavior with **Date only** format is practically the same as **Date only** behavior. Use the former if you aren't sure whether you need the time portion in the future.

> [!IMPORTANT]
> Avoid **Date only** format with **User local** behavior. Users in different time zones might see a different date, which is not intended in most scenarios. When a user sets a date in a model-driven app, the time portion will automatically be set to midnight of their time zone. This might cause the date to appear a day earlier or later for other users.

## Examples

### Display values

Dataverse stores `2023-10-15T07:30:00Z` (or `2023-10-15` for **Date only** behavior). Users in the time zone UTC-8 see these in the model-driven app or with a [Web API request for the formatted value](../../developer/data-platform/webapi/query/select-columns.md#formatted-values):

| Behavior | Format | Display value |
| -------- | ------ | ------------- |
| User local | Date and time | October 14th, 2023, 11:30 pm |
| User local | Date only | October 14th, 2023 |
| Time zone Independent | Date and time | October 15th, 2023, 7:30 am |
| Time zone Independent | Date only | October 15th, 2023 |
| Date only | - | October 15th, 2023 |

### Enter values in an app

Users in the time zone UTC-8 enter `October 14th, 2023, 11:30 pm` in a model-driven app. The value is saved in Dataverse as:

| Behavior | Format | Value saved in Dataverse |
| -------- | ------ | ------------------------ |
| User local | Date and time | 2023-10-15T07:30:00Z |
| User local | Date only | 2023-10-15T07:30:00Z |
| Time zone Independent | Date and time | 2023-10-14T23:30:00Z |
| Time zone Independent | Date only | 2023-10-14T23:30:00Z |
| Date only | - | 2023-10-14 |

If the user enters just the date `October 14th, 2023`, the time portion is assumed to be 12:00 AM.

| Behavior | Format | Value saved in Dataverse |
| -------- | ------ | ------------------------ |
| User local | Date only | 2023-10-14T08:00:00Z |
| Time zone Independent | Date only | 2023-10-14T00:00:00Z |
| Date only | - | 2023-10-14 |

### Enter invalid values in an app

Different clients have different ways to handle invalid input. For example, in Pacific time zone, daylight saving started on March 12th, 2023 at 2:00 AM, moving the time forward one hour to 3:00 AM. The time between 2:00 AM and 3:00 AM on that day doesn't exist. When users try to enter a value in that time range, apps might do one of the following:

* Change to the previous or next valid time.
* Revert to the last known value.
* Show an error message.
* Don't show times between 2:00 AM and 3:00 AM in the time picker, so that users can't select them in the first place.

Similarly, different clients have different ways to handle repeated time ranges. For example, in Pacific time zone, daylight saving ended on November 5th, 2023 at 2:00 AM, moving the time backward one hour to 1:00 AM. The time between 1:00 AM and 2:00 AM on that day is repeated twice. A time like 1:30 AM could refer to either time zones. If you need to unambiguously show or enter times in that range, it's best to temporarily switch to a time zone that doesn't use daylight saving.

### Get raw values with Web API

Dataverse stores `2023-10-15T07:30:00Z` (or `2023-10-15` for **Date only** behavior). Users in all time zones get these with a [Web API request for the value](../../developer/data-platform/webapi/query/select-columns.md):

| Behavior | Format | Raw value |
| -------- | ------ | --------- |
| User local | Date and time | 2023-10-15T07:30:00Z |
| User local | Date only | 2023-10-15T07:30:00Z |
| Time zone Independent | Date and time | 2023-10-15T07:30:00Z |
| Time zone Independent | Date only | 2023-10-15T07:30:00Z |
| Date only | - | 2023-10-15 |

### Get values with Client API

Users in the time zone UTC-8 enter `October 14th, 2023, 11:30 pm` in a model-driven app. [Client API](../../developer/model-driven-apps/client-scripting.md) functions like `formContext.getAttribute(<column name>).getValue()` return the value with time zone adjustments applied:

| Behavior | Format | JavaScript `dateValue.toUTCString()` |
| -------- | ------ | ------------------------------------ |
| User local | Date and time | 2023-10-15 07:30 (UTC)|
| User local | Date only | 2023-10-15 07:30 (UTC) |

For **Time zone independent** behavior, the JavaScript Date value is in the browser's time zone:

| Behavior | Format | JavaScript `dateValue.toString()` |
| -------- | ------ | --------------------------------- |
| Time zone Independent | Date and time | 2023-10-14 23:30 (browser time zone) |
| Time zone Independent | Date only | 2023-10-14 23:30 (browser time zone) |

JavaScript date values always have a time component. That's why **Date only** behavior has a time component of 12:00 AM:

| Behavior | Format | JavaScript `dateValue.toString()` |
| -------- | ------ | --------------------------------- |
| Date only | - | 2023-10-15 00:00 (browser time zone) |

> [!NOTE]
> JavaScript date values are affected by the browser's time zone, which comes from the device operating system settings.
>
> For **User local** behavior, the Client API result should be interpreted as a UTC value. Use `Date.getUTCDate()`, `Date.getUTCHours()`, etc. to work with it. To get what the user sees, apply [getTimeZoneOffsetMinutes](../../developer/component-framework/reference/usersettings/gettimezoneoffsetminutes.md). Do not use `Date.getDate()`, `Date.getHours()`, etc. because these will show the value in the browser's time zone.
>
> For **Time zone independent** and **Date only** behavior, the Client API result should be interpreted as a value in the browser's time zone. Use `Date.getDate()`, `Date.getHours()`, etc. to work with it. Don't use `Date.getUTCDate()`, `Date.getUTCHours()`, and so on because you don't have to adjust for any time zones.

## Change user local behavior

Unless the publisher of a managed solution prevents this, you can change the behavior of existing custom date columns from  **User local** to **Date only** or **Time zone independent**. This is a one-time change.

Changing the column behavior affects the column values that are added or modified after the column behavior was changed. The existing column values remain in the database in the UTC time zone format. To change the behavior of the existing column values from UTC to **Date only**, you might need a help of a developer to [convert behavior of existing date and time values in the database](../../developer/data-platform/behavior-format-date-time-attribute.md#convert-behavior-of-existing-date-and-time-values-in-the-database). 

> [!WARNING]
> Before changing the behavior of an existing date and time column, you should review all the dependencies of the column, such as business rules, workflows, calculated columns, or rollup columns, to ensure that there are no issues as a result of changing the behavior. After changing the behavior of a date and time column, open each business rule, workflow, calculated column, and rollup column dependent on the column that you changed, review the information, and save it, to ensure that the latest date and time column's behavior and value are used.

### Change behavior during a solution import

When you import a solution that contains a Date column with **User local** behavior, you can change the behavior to **Date only** or **Time zone independent**.  

> [!NOTE]
> You can only change the behavior of an existing managed **Date only** or **Date and time** column if you are the publisher. In order to make a change to these fields, an upgrade must be made to the solution that added the **Date only** or **Date and time** column. More information: [Upgrade or update a solution](update-solutions.md)

### Prevent changing behavior

If you're distributing a custom date column in a managed solution, prevent people using your solution from changing the behavior by setting the **CanChangeDateTimeBehavior** managed property to **False**. More information: [Set managed properties for columns](set-managed-properties-for-field.md)

## Date and time query operators not supported for Date only behavior

The following date and time related query operators are invalid for the **Date only** behavior. An invalid operator exception error is thrown when one of these operators is used in the query.

- Older Than X Minutes
- Older Than X Hours
- Last X Hours
- Next X Hours

### See also

[Troubleshoot date and time issues in model-driven apps](/troubleshoot/power-platform/power-apps/isolate-and-troubleshoot-common-issues/troubleshoot-model-driven-app-date-time-issues)   
[Create and edit columns](create-edit-fields.md)   
[Define calculated columns to automate manual calculations](define-calculated-fields.md)   
[Column managed properties](/power-platform/alm/managed-properties-alm#view-and-edit-column-managed-properties)   
[Managed properties](/power-platform/alm/managed-properties-alm)   
[Blog: Working with time zones in the Dataverse](https://powerapps.microsoft.com/en-us/blog/working-with-time-zones-in-the-common-data-service/)   
[Configure the behavior and format of the date and time column using code](../../developer/data-platform/behavior-format-date-time-attribute.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
