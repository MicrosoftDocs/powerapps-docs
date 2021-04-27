---
title: "Define custom state model transitions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about defining custom state model transitions for the Incident (Case) table or custom tables." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/11/2021
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
# Define custom state model transitions

You can specify custom state transitions for the `Incident` (**Case**) table or custom tables. The <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsStateModelAware> property is `true` for tables that support state model transitions.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

 Custom state transitions are an optional level of filtering to define which state transitions are valid for a record in a given state. Particularly when you have a large number of combinations for valid states and status values, defining a limited list of options can make it easier for people to choose the correct status for a record.  

<a name="BKMK_StateModel"></a>
   
## What is the state model?  
Tables that support the concept of state have a pair of columns that capture this data, as shown in this table.  
  
|Logical Name|Display Name|Description|  
|------------------|------------------|-----------------|  
|`statecode`|**Status**|Represents the state of the record. For custom tables this is **Active** or **Inactive**. The Incident (case) table uses **Active**, **Resolved**, and **Canceled**. You can’t add more state choices but you can change the choice labels.|  
|`statuscode`|**Status Reason**|Represents a status that is linked to a specific state. Each state must have at least one possible status. You can add additional status choices and change the labels of existing choices.|  
  
 The table definitions for the columns defines what status values are valid for a given state. For example, for the `Incident` (**Case**) table, the default state and status options are shown in the following table.  
  
|State|Status|  
|-----------|------------|  
|`Label`: **Active**<br /><br /> `Value`: 0|`Label`: **In Progress**<br /><br /> `Value`: 1<br /><br /> `State`: 0|  
|`Label`: **Active**<br /><br /> `Value`: 0|`Label`: **On Hold**<br /><br /> `Value`: 2<br /><br /> `State`: 0|  
|`Label`: **Active**<br /><br /> `Value`: 0|`Label`: **Waiting for Details**<br /><br /> `Value`: 3<br /><br /> `State`: 0|  
|`Label`: **Active**<br /><br /> `Value`: 0|Label: **Researching**<br /><br /> `Value`: 4<br /><br /> `State`: 0|  
|`Label`: **Resolved**<br /><br /> `Value`: 1|`Label`: **Problem Solved**<br /><br /> `Value`: 5<br /><br /> `State`: 1|  
|`Label`: **Resolved**<br /><br /> `Value`: 1|Label: **Information Provided**<br /><br /> `Value`: 1000<br /><br /> `State`: 1|  
|Label: **Canceled**<br /><br /> `Value`: 2|`Label`: **Canceled**<br /><br /> `Value`: 6<br /><br /> `State`: 2|  
|Label: **Canceled**<br /><br /> `Value`: 2|`Label`: **Merged**<br /><br /> `Value`: 2000<br /><br /> `State`: 2|  
  
 This data is stored in the <xref:Microsoft.Xrm.Sdk.Metadata.StatusOptionMetadata> class, which represents the options in the <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata> class.  
  
To view table definitions for your organization, install the Metadata Browser solution described in [Browse table definitions for your organization](browse-your-metadata.md). You can also browse the reference documentation for table in the [Table/entity reference](/reference/about-entity-reference.md).
  
<a name="BKMK_DetectValidStatusTransitions"></a>   

## Detect valid status transitions  
 You can modify the `statuscode` column to define which other status options represent valid transitions from the current status. For instructions, see the Customization Guide topic: [Define status reason transitions](https://go.microsoft.com/fwlink/p/?LinkId=393657)  
  
 When custom state transitions are applied to a table, the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EnforceStateTransitions> property will be `true`. Also, each <xref:Microsoft.Xrm.Sdk.Metadata.StatusOptionMetadata> within the <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata.Options> collection will have a new <xref:Microsoft.Xrm.Sdk.Metadata.StatusOptionMetadata.TransitionData> property. This property will contain a String value that represents an XML document. This document contains the definition of the allowed transitions. For example, the default `Incident` (**Case**) `StatusCode` column option may have the following `TransitionData` value.  
  
```xml  
<allowedtransitions xmlns="https://schemas.microsoft.com/crm/2009/WebServices">  
<allowedtransition sourcestatusid="1" tostatusid="6" />  
<allowedtransition sourcestatusid="1" tostatusid="1000" />   
<allowedtransition sourcestatusid="1" tostatusid="2000" />  
<allowedtransition sourcestatusid="1" tostatusid="5" />  
</allowedtransitions>  
```  
  
> [!NOTE]
>  When this data is retrieved in unmanaged code from the web service, for example when using JavaScript, it will be escaped and appear like the following example.  
  
```xml  
<allowedtransitions xmlns="https://schemas.microsoft.com/crm/2009/WebServices">  
<allowedtransition sourcestatusid="1" tostatusid="6">  
<allowedtransition sourcestatusid="1" tostatusid="1000">  
<allowedtransition sourcestatusid="1" tostatusid="2000">  
<allowedtransition sourcestatusid="1" tostatusid="5">  
</allowedtransitions>  
```  
  
 When this data is present and the table `EnforceStateTransitions` property is `true`, any incident instance can only be changed to one of the allowed `statuscode` values. You can use<xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> to set the `statuscode`<xref:Microsoft.Xrm.Sdk.OptionSetValue> to any of the allowed values that don’t represent a change in state. To change the state, use <xref:Microsoft.Crm.Sdk.Messages.SetStateRequest> setting the allowed <xref:Microsoft.Crm.Sdk.Messages.SetStateRequest.State> and <xref:Microsoft.Crm.Sdk.Messages.SetStateRequest.Status> property values or the <xref:Microsoft.Crm.Sdk.Messages.CloseIncidentRequest> setting <xref:Microsoft.Crm.Sdk.Messages.CloseIncidentRequest.Status> property to one of the values allowed for the current `statuscode` value. Attempting to set an invalid value throws an error.  
  
### See also  
 [Sample: Retrieve valid status transitions](org-service/samples/retrieve-valid-status-transitions.md)   
 [Record state and status](/dynamics365/customer-engagement/developer/introduction-entities#bkmk_RecordStateandStatus)   
 [Retrieve and detect changes to table definitions](org-service/metadata-retrieve-detect-changes.md)   
 [Define status reason transitions](/powerapps/maker/data-platform/define-status-reason-transitions)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]