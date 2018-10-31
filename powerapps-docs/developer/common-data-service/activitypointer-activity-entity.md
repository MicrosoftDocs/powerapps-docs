---
title: "ActivityPointer (activity) entity (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The activity pointer (activity) entity represents any activity or task that is performed, or to be performed by a user. An activity is any action for which an entry can be made on a calendar" 
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" 
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# ActivityPointer (activity) entity

The activity pointer (activity) entity represents any activity or task that is performed, or to be performed by a user. An activity is any action for which an entry can be made on a calendar.  
  
 Whenever you create an activity record in Common Data Service for Apps, a corresponding activity pointer record is created. This indicates that the activity record and the corresponding activity pointer record have the same value for the `ActivityId` attribute. For example, if you create an `Email` record, the attribute values of `Email.ActivityId` and the corresponding `ActivityPointer.ActivityId` will be the same.  
  
 The `ActivityPointer.ActivityTypeCode` attribute defines the type of the activity. The possible values for this attribute are defined in `activitypointer_activitytypecode` global option set.  
  
<a name="bkmk_sortdate"></a>   

## Control how activities are sorted by date  
  
 Whenever you display a list of activity entities and order them by date, you can only use the common date  attributes defined in the activitypointer entity. However, sometimes you want different sorting behaviors depending on the type of activity. For example, with the email entity you might want to sort by the senton attribute value  rather than the modifiedon attribute value.  
  
 Use the sortdate attribute to control how activities are sorted by date. By default, the sortdate attribute value is null. You must include business logic to populate the date value that will be set for this attribute and then use the sortdate attribute within the query defined for the view. You can set the sortdate attribute value using a workflow or a plugin. For consistent results you should set this value for every type of activity and any existing activity data in the system.  
  
### See also  
 [Activity Entities](activity-entities.md)   
 [ActivityPointer Entity](reference/entities/activitypointer.md)