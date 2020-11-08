---
title: "Activity tables (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Activities are tasks that you or your teams perform when they contact customers, for example, sending letters or making telephone calls." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 11/08/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Activity tables

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

In Common Data Service, activities are tasks that you or your teams perform when they contact customers, for example, sending letters or making telephone calls. You  can create activities for yourselves, can assign them to someone else, or can share them with other users or teams. An activity is any action which can be entered  on a calendar  and has time dimensions (start time, stop time, due date, and duration) that help determine when the action occurred or is to occur. Activities has some basic properties that help determine what action the activity represents, for example, subject and description. An activity state can be opened, canceled, or completed. The completed status of an activity will have several substatus values associated with it to clarify the way that the activity was completed.  
  
 Activities involve one or more participants, called activity parties in Common Data Service. For a meeting activity, the participants are those contacts or users attending the meeting. For a telephone call or fax activity, the parties are the caller and the person who is called. The following diagram shows the entity relationships for activities.  
  
 ![Activity diagram](media/entity-model-activity.gif "Activity diagram")  
  
 To support the communication needs of the modern-day business, such as instant messaging (IM) and SMS, you can create [custom activities](custom-activities.md) in Common Data Service.  
  
 ## Other activity tables  
  
The scheduling activities enables you to schedule your services and resources, and thus define work schedules. The scheduling activity tables are [Appointment](reference/entities/appointment.md) and [RecurringAppointmentMaster](reference/entities/recurringappointmentmaster.md) 
  
## Related topics  
 [Custom Activities](custom-activities.md)<br/>
 [E-mail Activity tables](email-activity-entities.md)<br/>
 [Task, Fax, Phone Call, and Letter activity tables](task-fax-phone-call-letter-activity-entities.md)<br/>
 [Activity Party table](activityparty-entity.md)<br/>
 [Activity Pointer (Activity) table](activitypointer-activity-entity.md) 
 [Recurring appointments](recurring-appointment-partial-expansion-model.md)
  
### See also  
 
 [Sample Code for Activity tables](/powerapps/developer/common-data-service/org-service/samples/convert-fax-task)
 
 [Server-side synchronization tables](server-side-synchronization-entities.md)  
  
 [Customize table metadata](customize-entity-metadata.md)
