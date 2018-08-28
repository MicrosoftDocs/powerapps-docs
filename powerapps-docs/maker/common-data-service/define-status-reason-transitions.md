---
title: "Define status reason transitions with PowerApps | MicrosoftDocs"
description: "Learn how to define status reason transitions"
ms.custom: ""
ms.date: 05/25/2018
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
ms.assetid: dbc4f436-0b23-42f9-8079-b0de482aaebe
caps.latest.revision: 11
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Define status reason transitions for the Case or custom entities

You can specify status reason transitions for the Incident (**Case**) entity or a custom entity.

> [!NOTE]
> Although the Incident (Case) entity isn't included in a default Common Data Service for Apps environment, it is used by [Dynamics 365 for Customer Service](https://dynamics.microsoft.com/customer-service/) and defined within the [Common Data Model](https://github.com/Microsoft/CDM/blob/master/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/service/Incident.cdm.json)
  
Status reason transitions are an optional additional level of filtering to define what the status reason value can be changed to for each status reason. Defining a limited list of valid options can make it easier for people to choose the correct next status reason for a record when you have a large number of combinations for valid status reason values.  
  
<a name="BKMK_StatusAndStatusReasons"></a>

## What is the connection between Status and Status Reason fields?  

Entities that can have different status values have two fields that capture this data:  
  
|Display Name|Description|  
|------------------|-----------------|  
|**Status**|Represents the state of the record. Typically **Active** or **Inactive**. You cannot add new status options.|  
|**Status Reason**|Represents a reason that is linked to a specific status. Each status must have at least one possible status reason. You can add additional status reason options.|  
  
The metadata for the field defines what status values are valid for a given state. For example, for the Incident (**Case**) entity, the default status and status reason options are:  
  
|Status|Status Reason|  
|------------|-------------------|  
|**Active**|<li>**In Progress**</li><li>**On Hold**</li><li>**Waiting for Details**</li><li>**Researching**</li>| 
|**Resolved**|<li>**Problem Solved**</li><li>**Information Provided**</li>|
|**Canceled**|<li>**Canceled**</li><li>**Merged**</li>|
  
  
<a name="BKMK_EditStatusReasonTransitions"></a>   

## Edit status reason transitions
 
You can modify the status reason field options for the Case entity and custom entities to define which other status reason options people can choose. The only restriction is that each status reason option for an active status must allow at least one path to an inactive status. Otherwise you could create a condition where it would not be possible to resolve or cancel the case.  

> [!NOTE]
> Editing the status reason transitions requires using solution explorer. See [Create and edit fields for Common Data Service for Apps using PowerApps solution explorer](create-edit-field-solution-explorer.md) for information about how to edit fields.
  
 When you edit a status reason field the **Edit Status Reason Transitions** button is in the menu. 

![Edit Status Reason Transitions command](media/status-reason-transitions-command.png)

When you click this button the **Status Reason Transitions** dialog provides the option to choose **Enable Status Reason Transitions**. When this option is selected you must define which *other* status reason values are allowed for each status reason. To remove the filtering applied, remove the **Enable Status Reason Transitions** selection. The transitions you have defined will be kept but not applied.  
  
The screenshot below provides an example that meets the following requirements: 
 
- A case can be merged at any time. You will not be able to merge cases if a status reason transition does not allow for it.  
- An active case can be canceled at any time.  
- A resolved or canceled case cannot be reactivated.  
- All cases must pass through the following stages: **In Progress** > **On Hold** > **Waiting for Details** > **Researching** before they can be resolved. With this configuration, a case could not be set to an earlier status.  
  > [!NOTE]
  >  This is not a good example for real work, but it demonstrates how stages of status can be enforced through status reason transitions.  
  
 ![Example of status reason transitions for case](media/status-reason-transitions-example.PNG)  
  
### See Also  

[Create and edit fields for Common Data Service for Apps using PowerApps solution explorer](create-edit-field-solution-explorer.md)<br />
[Entity metadata > Entity states](/powerapps/developer/common-data-service/entity-metadata#entity-states)<br />
[Define custom state model transitions](/dynamics365/customer-engagement/developer/define-custom-state-model-transitions)

