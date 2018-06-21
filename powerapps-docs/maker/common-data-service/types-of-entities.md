---
title: "Types of entities | MicrosoftDocs"
ms.custom: ""
ms.date: 05/30/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 2f3f6053-0b9e-41e7-bd94-2239351e9f4b
caps.latest.revision: 41
ms.author: "matp"
manager: "kvivek"
---
# Types of entities

Before creating or editing entities in Common Data Service for Apps, you should understand that there are different types of entities. Once a custom entity is created, these types cannot be changed. The two major divisions are based on entity ownership and whether the entities are activity entities.  
  
<a name="BKMK_EntityOwnership"></a>

## Entity ownership  

There are four different types of entity ownership. When you create a custom entity the only options are **user or team owned** or **organization-owned**, but you should be aware that other entities have different ownership types.  
  
|Ownership|Description|  
|---------------|-----------------|  
|**Business-owned**|Data in these entities belongs to the Business unit. Access to the data can be controlled at the business unit level.|  
|**None**|Data not owned by another entity.|  
|**Organization-owned**|Data belongs to the organization. Access to the data is controlled at the organization level.|  
|**User or Team Owned**|Data belongs to a user or a team. Actions that can be performed on these records can be controlled on a user level.|  
  
  
> [!IMPORTANT]
>  After an entity is created, you can’t change the ownership. Before you create an entity, make sure that you choose the correct type of ownership. If you later determine that your custom entity must be of a different type, you have to delete it and create a new one.
  
<a name="BKMK_ActivityEntities"></a>

## Activity entities

An activity can be thought of as any action for which an entry can be made on a calendar. An activity has time dimensions (start time, stop time, due date, and duration) that help determine when the action occurred or will occur. Activities also contain data that helps determine what action the activity represents, for example, subject and description. An activity can be opened, canceled, or completed. The completed status of an activity will have several sub-status values associated with it to clarify the way that the activity was completed.  
  
Activity entities can only be owned by a user or team, they can’t be owned by an organization.  
  
The following table lists activity entities that are available in a default CDS for Apps environment.
  
|Name|Description|Display in activity menus|Reference|
|----------|-----------------|----------------|---------------|  
|**Appointment**|Commitment representing a time interval with start/end times and duration.|Yes|[Appointment](/powerapps/developer/common-data-service/reference/entities/appointment)|
|**Email**|Activity that is delivered using email protocols.|Yes|[Email ](/powerapps/developer/common-data-service/reference/entities/email)|
|**Fax**|Activity that tracks call outcome and number of pages for a fax and optionally stores an electronic copy of the document.|Yes|[Fax](/powerapps/developer/common-data-service/reference/entities/fax)|
|**Letter**|Activity that tracks the delivery of a letter. The activity can contain the electronic copy of the letter.|Yes|[Letter](/powerapps/developer/common-data-service/reference/entities/letter)|
|**Phone Call**|Activity to track a telephone call.|Yes|[PhoneCall ](/powerapps/developer/common-data-service/reference/entities/phonecall)|
|**Recurring Appointment**|The master appointment of a recurring appointment series.|Yes|[RecurringAppointmentMaster](/powerapps/developer/common-data-service/reference/entities/recurringappointmentmaster)|
|**Task**|Generic activity representing work needed to be done.|Yes|[Task](/powerapps/developer/common-data-service/reference/entities/task)|
  
You can create new custom activity entities. For example you might create a custom activity entity to record instant message communications. Creating an activity entity is different from creating a non-activity entity because you don’t specify a primary field. All activity entities have a **Primary Field** set to **Subject** and other common fields that are defined by the Activity entity. This allows all types of activities to be shown in a view where just the common fields are displayed.  

> [!NOTE]
> You cannot create a custom activity using the PowerApps portal. You must open the solution explorer using the **Advanced** button.
  
To create a custom activity entity, select **Define as an activity entity**. After you select this, you’ll see that **Display in Activity Menus** is selected. This setting allows people to create this type of activity in the activity menus. This isn’t selected for activities that are typically associated with specific events and created behind using code or by a workflow. After you save the entity, you can’t change these settings.  

### See also
[Create or edit entities](create-edit-entities.md)
