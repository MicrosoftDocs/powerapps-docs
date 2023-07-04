---
title: Activity (ActivityPointer) table
description: Learn how to work with the Activity (ActivityPointer) table in Microsoft Dataverse.
ms.date: 07/03/2023
ms.reviewer: pehecke
ms.topic: conceptual
author: DanaMartens
ms.author: dmartens 
ms.subservice: dataverse-developer
search.audienceType: 
- developer
ms.custom: bap-template
---

# Activity (ActivityPointer) table

The [Activity (ActivityPointer) table](reference/entities/activitypointer.md) stores data about activities or tasks a user performs. An activity is any action that can be entered on a calendar and has time dimensions (start time, stop time, due date, and duration).

When you create an activity record in Dataverse, it creates a corresponding activity pointer record. The activity record and its associated activity pointer record have the same value for the `ActivityId` column.

The [`ActivityPointer.ActivityTypeCode`](/power-apps/developer/data-platform/reference/entities/activitypointer#BKMK_ActivityTypeCode) column defines the type of the activity. The possible values for this column are defined in the `activitypointer_activitytypecode` global option set.

## Inherited statecode and statuscode options

When you write code that sets or modifies activity columns, it's important to keep in mind that the `statecode` and `statuscode` columns of`ActivityPointer` derived types can have a somewhat different purpose from the base `ActivityPointer` `statecode` and `statuscode` column definitions. The following sections describe these differences.

### StateCode option differences

In this section, let's review state code option differences between `ActivityPointer` and derived types.

[ActivityPointer.StateCode](/power-apps/developer/data-platform/reference/entities/activitypointer#statecode-choicesoptions) defines four options:

| Label | Value |
| --------- | ---------|
| **Open** | 0 |
| **Completed** | 1 |
| **Canceled** | 2 |
| **Scheduled** | 3 |

- [Appointment](/power-apps/developer/data-platform/reference/entities/appointment#statecode-choicesoptions), [Chat](/power-apps/developer/data-platform/reference/entities/chat#statecode-choicesoptions), [RecurringAppointmentMaster](/power-apps/developer/data-platform/reference/entities/recurringappointmentmaster#statecode-choicesoptions), and custom activities have all four `statecode` options.
- [Email](/power-apps/developer/data-platform/reference/entities/email#statecode-choicesoptions), [Fax](/power-apps/developer/data-platform/reference/entities/fax#statecode-choicesoptions), [Letter](/power-apps/developer/data-platform/reference/entities/letter#statecode-choicesoptions), [PhoneCall](/power-apps/developer/data-platform/reference/entities/phonecall#statecode-choicesoptions), [Task](/power-apps/developer/data-platform/reference/entities/task#statecode-choicesoptions), and [SocialActivity](/power-apps/developer/data-platform/reference/entities/socialactivity#statecode-choicesoptions) have the first three `statecode` options. There's no valid option to set the state of these activity types as **Scheduled**.

### StatusCode label differences

The `statuscode` options provide reasons for the `statecode` of the record. You can add new `statuscode` options so that each table has a different set. Some of the options have the same value as the [ActivityPointer](reference/entities/activitypointer.md) `statuscode`, but the labels can be different.

Labels for `statuscode` options vary based on whether you're retrieving rows as an [ActivityPointer](reference/entities/activitypointer.md) or as a specific activity type such as an [Appointment](reference/entities/appointment.md), [Email](reference/entities/email.md), or [Task](reference/entities/task.md).

For example, if you retrieve an `ActivityPointer` row that represents an `Appointment`, the label for `statuscode` value `1` is **Open** rather than **Free**.

Labels are listed in the definition of the default `statuscode` options for each table:

- [ActivityPointer.StatusCode Options](/power-apps/developer/data-platform/reference/entities/activitypointer#statuscode-choicesoptions)
- [Appointment.StatusCode Options](/power-apps/developer/data-platform/reference/entities/appointment#statuscode-choicesoptions)
- [Chat.StatusCode Options](/power-apps/developer/data-platform/reference/entities/chat#statuscode-choicesoptions)
- [Email.StatusCode Options](/power-apps/developer/data-platform/reference/entities/email#statuscode-choicesoptions)
- [Fax.StatusCode Options](/power-apps/developer/data-platform/reference/entities/fax#statuscode-choicesoptions)
- [Letter.StatusCode Options](/power-apps/developer/data-platform/reference/entities/letter#statuscode-choicesoptions)
- [PhoneCall.StatusCode Options](/power-apps/developer/data-platform/reference/entities/phonecall#statuscode-choicesoptions)
- [RecurringAppointmentMaster.StatusCode Options](/power-apps/developer/data-platform/reference/entities/recurringappointmentmaster#statuscode-choicesoptions)
- [Task.StatusCode Options](/power-apps/developer/data-platform/reference/entities/task#statuscode-choicesoptions)
- [SocialActivity.StatusCode Options](/power-apps/developer/data-platform/reference/entities/socialactivity#statuscode-choicesoptions)

<a name="bkmk_sortdate"></a>

## Control how activities are sorted by date

 When you display a list of activity entities in date order, you can only sort on the common date columns defined in the [ActivityPointer](reference/entities/activitypointer.md) table. However, sometimes you want different sorting behaviors depending on the type of activity. For example, you might want to sort email activities by the "sent on" date rather than the "modified on" date. Use the `sortdate` column to control how activities are sorted by date.

By default, the value of the `sortdate` column is null. Include logic to set a value for the column and then use the `sortdate` column in the query you define for the view.

You can set the `sortdate` column value using a workflow or a plugin. For consistent results, you should set this value for every type of activity and any existing activity data in the system.

### See also

 [Activity tables](activity-entities.md)  
 [ActivityPointer table](reference/entities/activitypointer.md)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
