---
title: Customize the behavior and format of the fields in portals
description: Learn how to customize the behavior and format of the Microsoft Dataverse fields in portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
---

# Customize the behavior and format of the fields in portals

In this article, you'll learn about working with Microsoft Dataverse fields, and the field data types that can be customized in Power Apps portals.

## Date and time

In Microsoft Dataverse, the Date and Time data type is used in many system table fields. For example, you can show when an account was last used in a marketing campaign, or show the date and time when a case was escalated. You can also create custom tables that include the date and time fields. Depending on what the field represents, you can choose one of the following field behaviors for portal forms and grids: 
- **User Local**: The field values are displayed in the user’s local time and formatted as per their current portal language/locale. The values are stored in UTC time zone format in Dataverse. When a user in Dataverse (or another portal user) in a different time zone views that value, they see it converted to their own time zone.
- **Date Only**: The field values only contain the date and are displayed with no time zone conversion. The time portion of the value is always 12:00 AM. The value entered by one user is seen the same by other users in different time zones (for example, birth dates).
  
  > [!Note]
  > The behavior of this field can’t be changed after it’s saved.
  
- **Time-Zone Independent**: The field values contain date and time, and are displayed with no time zone conversion. The value entered by one user is seen the same by other users in different time zones.
  
  > [!Note]
  > The behavior of this field can’t be changed after it’s saved.

You can also override the default date/time format to be used on portals by creating the following site settings:
- DateTime/DateFormat: The date format used on the portal. 
- DateTime/TimeFormat: The time format used on the portal. 
- DateTime/DateTimeFormat: The format for full date and time used on the portal.

By default, the portal uses the standard date/time formats specified by the website language settings. For a complete list of the accepted date/time formats, read [Custom date and time format strings](/dotnet/standard/base-types/custom-date-and-time-format-strings).

## Duration

Dataverse forms allow you to add, or edit fields having [duration](../../data-platform/create-edit-field-portal.md) data type with custom values. For example, instead of the default `7 hours`, or `2 days`, you can enter `7.5 hours`, or `2.5 days`. You can't add, or edit this field with such custom values using portals. However, portals will display such custom values when defined for the records from Dataverse.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]