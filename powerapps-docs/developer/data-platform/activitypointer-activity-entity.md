---
title: "ActivityPointer (activity) table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The activity pointer (activity) table represents any activity or task that is performed, or to be performed by a user. An activity is any action for which an entry can be made on a calendar" 
ms.date: 03/25/2023
ms.reviewer: pehecke
ms.topic: article
author: DataMartens
ms.subservice: dataverse-developer
ms.author: dmartens 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# ActivityPointer (activity) table

The activity pointer (activity) table represents any activity or task that is performed, or to be performed by a user. An activity is any action for which an entry can be made on a calendar.  
  
 Whenever you create an activity record in Microsoft Dataverse, a corresponding activity pointer record is created. This indicates that the activity record and the corresponding activity pointer record have the same value for the `ActivityId` column. For example, if you create an `Email` record, the column values of `Email.ActivityId` and the corresponding `ActivityPointer.ActivityId` will be the same.  
  
 The `ActivityPointer.ActivityTypeCode` column defines the type of the activity. The possible values for this column are defined in `activitypointer_activitytypecode` global option set.  
 

## Inherited statecode and statuscode options

When you  interact with activities with code, it's important to keep in mind that the labels for `statecode` and `statuscode` options will vary based on whether you are retrieving rows as an [ActivityPointer](reference/entities/activitypointer.md) or a specific activity type such as an [Appointment](reference/entities/appointment.md), [Email](reference/entities/email.md), or [Task](reference/entities/task.md).

For example, if you retrieve an `ActivityPointer` row that represents an `Appointment`, the name value for `statuscode` of 1 will show up as ["Open"](/powerapps-docs/developer/data-platform/reference/entities/activitypointer#statuscode-choicesoptions) rather than ["Free"](/powerapps-docs/developer/data-platform/reference/entities/appointment#statuscode-choicesoptions).

  
<a name="bkmk_sortdate"></a>

## Control how activities are sorted by date  
  
 Whenever you display a list of activity entities and order them by date, you can only use the common date columns defined in the [ActivityPointer](reference/entities/activitypointer.md) table. However, sometimes you want different sorting behaviors depending on the type of activity. For example, with the email table you might want to sort by the `senton` column value  rather than the `modifiedon` column value.  
  
 Use the `sortdate` column to control how activities are sorted by date. By default, the `sortdate` column value is null. You must include business logic to populate the date value that will be set for this column and then use the `sortdate` column within the query defined for the view. You can set the `sortdate` column value using a workflow or a plugin. For consistent results you should set this value for every type of activity and any existing activity data in the system.  
  
### See also  
 [Activity tables](activity-entities.md)   
 [ActivityPointer table](reference/entities/activitypointer.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
