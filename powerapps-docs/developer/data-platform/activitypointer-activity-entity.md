---
title: "ActivityPointer (activity) table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The activity pointer (activity) table represents any activity or task a user performs. An activity is any action where you would make an entry on a calendar." 
ms.date: 03/25/2023
ms.reviewer: pehecke
ms.topic: article
author: DanaMartens
ms.subservice: dataverse-developer
ms.author: dmartens 
search.audienceType: 
  - developer
---
# ActivityPointer (activity) table

The [Activity (ActivityPointer)  table](reference/entities/activitypointer.md) represents any activity or task a user performs. An activity is any action where you would make an entry on a calendar.  
  
Whenever you create an activity record in Dataverse, a corresponding activity pointer record is created. The activity record and the corresponding activity pointer record have the same value for the `ActivityId` column. For example, when you create an `Email` record, the column values of `Email.ActivityId` and the corresponding `ActivityPointer.ActivityId` are the same.  
  
The [ActivityPointer.ActivityTypeCode](/power-apps/developer/data-platform/reference/entities/activitypointer#BKMK_ActivityTypeCode) column defines the type of the activity. The possible values for this column are defined in `activitypointer_activitytypecode` global option set.

## Inherited statecode and statuscode options

When you  interact with activities with code, it's important to keep in mind that the `statecode` and `statuscode` columns of the types that are derived from `ActivityPointer` can have differences from the `ActivityPointer` `statecode` and `statuscode` column definitions.

### StateCode option differences

[ActivityPointer.StateCode](/power-apps/developer/data-platform/reference/entities/activitypointer#statecode-choicesoptions) defines four options:

|Label|Value|
|---------|---------|
|**Open**|0|
|**Completed**|1|
|**Canceled**|2|
|**Scheduled**|3|

- [Appointment](/power-apps/developer/data-platform/reference/entities/appointment#statecode-choicesoptions), [Chat](/power-apps/developer/data-platform/reference/entities/chat#statecode-choicesoptions), [RecurringAppointmentMaster](/power-apps/developer/data-platform/reference/entities/recurringappointmentmaster#statecode-choicesoptions), and any custom activities have all four `statecode` options.
- [Email](/power-apps/developer/data-platform/reference/entities/email#statecode-choicesoptions), [Fax](/power-apps/developer/data-platform/reference/entities/fax#statecode-choicesoptions), [Letter](/power-apps/developer/data-platform/reference/entities/letter#statecode-choicesoptions), [PhoneCall](/power-apps/developer/data-platform/reference/entities/phonecall#statecode-choicesoptions), [Task](/power-apps/developer/data-platform/reference/entities/task#statecode-choicesoptions), and [SocialActivity](/power-apps/developer/data-platform/reference/entities/socialactivity#statecode-choicesoptions) only have the first three `statecode` options. There's no valid option to set the state of these activity types as **Scheduled**.

### StatusCode label differences

The `statuscode` options provide reasons for the `statecode` of the record. These option sets can be customized by adding new options, so each table can have a different set of options. Some of the options have the same value as the [ActivityPointer](reference/entities/activitypointer.md) `statuscode` option values, but the labels can be different.

Labels for `statuscode` options vary based on whether you're retrieving rows as an [ActivityPointer](reference/entities/activitypointer.md) or a specific activity type such as an [Appointment](reference/entities/appointment.md), [Email](reference/entities/email.md), or [Task](reference/entities/task.md).

For example, if you retrieve an `ActivityPointer` row that represents an `Appointment`, the label for `statuscode` value `1` shows up as **Open** rather than **Free**.

You can find the labels in the definition of the default `statuscode` options for each table here:

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
  
 Whenever you display a list of activity entities and order them by date, you can only use the common date columns defined in the [ActivityPointer](reference/entities/activitypointer.md) table. However, sometimes you want different sorting behaviors depending on the type of activity. For example, with the email table you might want to sort by the `senton` column value  rather than the `modifiedon` column value.  
  
 Use the `sortdate` column to control how activities are sorted by date. By default, the `sortdate` column value is null. You must include business logic to populate the date value that set for this column and then use the `sortdate` column within the query defined for the view. You can set the `sortdate` column value using a workflow or a plugin. For consistent results, you should set this value for every type of activity and any existing activity data in the system.  
  
### See also

 [Activity tables](activity-entities.md)<br />
 [ActivityPointer table](reference/entities/activitypointer.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
