---
title: "Define custom state model transitions (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about defining custom state model transitions for the Incident (Case) table or custom tables."
ms.date: 06/15/2022
ms.reviewer: jdaly
ms.topic: article
author: mkannapiran
ms.author: kamanick
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Define custom state model transitions

You can specify custom state transitions for the `Incident` (Case) table or custom tables. The <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsStateModelAware?text=EntityMetadata.IsStateModelAware> property is `true` for tables that support state model transitions.

> [!NOTE]
> Although the `Incident` (Case) table isn't included in a default Microsoft Dataverse environment, it is used by [Dynamics 365 for Customer Service](https://dynamics.microsoft.com/customer-service/) and defined within the [Common Data Model](https://github.com/Microsoft/CDM/blob/master/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/service/Case.cdm.json)

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Custom state transitions are an optional level of filtering to define which state transitions are valid for a record in a given state. Particularly when you have a large number of combinations for valid states and status values, defining a limited list of options can make it easier for people to choose the correct status for a record.  

<a name="BKMK_StateModel"></a>

## What is the state model?

Tables that support the concept of state have a pair of columns that capture state model data, as shown in the following table.  
  
|Logical Name|Display Name|Description|  
|------------------|------------------|-----------------|  
|`statecode`|**Status**|Represents the state of the record. For custom tables this value is **Active** or **Inactive**. You can't add more state choices but you can change the choice labels.|  
|`statuscode`|**Status Reason**|Represents a status that is linked to a specific state. Each state must have at least one possible status. You can add more status choices and change the labels of existing choices.|  
  
The table definitions for the columns define what status values are valid for a given state. For example, for the `Incident` (**Case**) table, the default state and status options are shown in the following table.  
  
|State|Status|  
|-----------|------------|  
|`Label`: **Active**<br />`Value`: 0<br />&nbsp;|`Label`: **In Progress**<br /> `Value`: 1<br /> `State`: 0|  
|`Label`: **Active**<br />`Value`: 0<br />&nbsp;|`Label`: **On Hold**<br /> `Value`: 2<br /> `State`: 0|  
|`Label`: **Active**<br />`Value`: 0<br />&nbsp;|`Label`: **Waiting for Details**<br /> `Value`: 3<br /> `State`: 0|  
|`Label`: **Active**<br />`Value`: 0<br />&nbsp;|Label: **Researching**<br /> `Value`: 4<br /> `State`: 0|  
|`Label`: **Resolved**<br />`Value`: 1<br />&nbsp;|`Label`: **Problem Solved**<br /> `Value`: 5<br /> `State`: 1|  
|`Label`: **Resolved**<br />`Value`: 1<br />&nbsp;|Label: **Information Provided**<br /> `Value`: 1000<br /> `State`: 1|  
|Label: **Canceled**<br />`Value`: 2<br />&nbsp;|`Label`: **Canceled**<br /> `Value`: 6<br /> `State`: 2|  
|Label: **Canceled**<br />`Value`: 2<br />&nbsp;|`Label`: **Merged**<br /> `Value`: 2000<br /> `State`: 2|  
  
This data is stored in the <xref:Microsoft.Xrm.Sdk.Metadata.StatusOptionMetadata> class, which represents the options in the <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata> class.  
  
To view table definitions for your organization, install the Metadata Browser solution described in [Browse table definitions for your organization](browse-your-metadata.md). You can also browse the reference documentation for table in the [Table/entity reference](reference/about-entity-reference.md).
  
<a name="BKMK_DetectValidStatusTransitions"></a>   

## Detect valid status transitions

You can modify the `statuscode` column to define which other status options represent valid transitions from the current status. For instructions, see the [Define status reason transitions for the Case or custom tables](../../maker/data-platform/define-status-reason-transitions.md)
  
When custom state transitions are applied to a table, the [EntityMetadata.EnforceStateTransitions](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EnforceStateTransitions) property is `true`. Also, each <xref:Microsoft.Xrm.Sdk.Metadata.StatusOptionMetadata> within the <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata.Options> collection has a <xref:Microsoft.Xrm.Sdk.Metadata.StatusOptionMetadata.TransitionData> property. This property contains a string value that represents an XML document. This document contains the definition of the allowed transitions. For example, the default `Incident` (**Case**) `StatusCode` column option might have the following `TransitionData` value.
  
```xml  
<allowedtransitions xmlns="https://schemas.microsoft.com/crm/2009/WebServices">  
<allowedtransition sourcestatusid="1" tostatusid="6" />  
<allowedtransition sourcestatusid="1" tostatusid="1000" />   
<allowedtransition sourcestatusid="1" tostatusid="2000" />  
<allowedtransition sourcestatusid="1" tostatusid="5" />  
</allowedtransitions>  
```  

When this data is present and the table `EnforceStateTransitions` property is `true`, any incident instance can only be changed to one of the allowed `statuscode` values. You can use <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*?text=IOrganizationService.Update> to set the `statuscode` <xref:Microsoft.Xrm.Sdk.OptionSetValue> to any of the allowed values that don't represent a change in state. To change the state, use <xref:Microsoft.Crm.Sdk.Messages.SetStateRequest> setting the allowed <xref:Microsoft.Crm.Sdk.Messages.SetStateRequest.State> and <xref:Microsoft.Crm.Sdk.Messages.SetStateRequest.Status> property values or the <xref:Microsoft.Crm.Sdk.Messages.CloseIncidentRequest> setting <xref:Microsoft.Crm.Sdk.Messages.CloseIncidentRequest.Status> property to one of the values allowed for the current `statuscode` value. Attempting to set an invalid value throws an error.


### See also

[Sample: Retrieve valid status transitions](org-service/samples/retrieve-valid-status-transitions.md)<br />
[Sample: Validate record state and set the state of record](org-service/samples/validate-record-state.md)<br />
[Retrieve and detect changes to table definitions](org-service/metadata-retrieve-detect-changes.md)<br />
[Define status reason transitions](/powerapps/maker/data-platform/define-status-reason-transitions)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
