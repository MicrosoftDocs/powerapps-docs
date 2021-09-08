---
title: Configure table relationship cascading behavior (Microsoft Dataverse) | Microsoft Docs
description: Configure cascading behaviors for a one-to-many relationship in Microsoft Dataverse to preserve data integrity and automate business processes.
services: ''
suite: powerapps
documentationcenter: na
author: "mayadumesh" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 08/06/2021
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Configure table relationship cascading behavior  

You can configure cascading behaviors for a one-to-many relationship to preserve data integrity and automate business processes. Both Web API and organization service support configuring cascading behavior.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Using Web API to configure cascading behavior

When working with Web API, you can define a One-to-Many relationship using <xref href="Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType" />. This definition includes the name of the intersect table to be created as well as how the relationship should be displayed in the application by using <xref href="Microsoft.Dynamics.CRM.AssociatedMenuConfiguration?text=AssociatedMenuConfiguration ComplexType" />, <xref href="Microsoft.Dynamics.CRM.Label?text=Label ComplexType" /> and <xref href="Microsoft.Dynamics.CRM.LocalizedLabel?text=LocalizedLabel ComplexType" />. 

More information: [Create a One-to-Many relationship using Web API](webapi/create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship).

## Using Organization Service to configure cascading behavior

When you use <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRelationshipRequest> you include an instance of a <xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata> class in the body of the request. In the <xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.CascadeConfiguration> property of that class you use the <xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration> class.  

The `CascadeConfiguration` (<xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration> class or <xref href="Microsoft.Dynamics.CRM.CascadeConfiguration?text=CascadeConfiguration ComplexType" />) contains the properties representing actions that may be performed on the referenced table in the one-to-many relationship. Each property can be assigned one of the values of the <xref href="Microsoft.Dynamics.CRM.CascadeType?text=CascadeType EnumType" />.  

|Value|Application label|Description|  
|-----------|-----------------------|-----------------|  
|Active|Cascade Active|Perform the action on all active referencing table records associated with the referenced table record.|  
|Cascade|Cascade All|Perform the action on all referencing table records associated with the referenced table record.|  
|NoCascade|Cascade None|Do nothing.|  
|RemoveLink|Remove Link|Remove the value of the referencing column for all referencing table records associated with the referenced table record.|  
|Restrict|Restrict|Prevent the Referenced table record from being deleted when referencing tables exist.|  
|UserOwned|Cascade User Owned|Perform the action on all referencing table records owned by the same user as the referenced table record.|  

**Active Records considered for Cascading action**

Cascading actions on active records will only include records that have a state code of “Active”. The following State Codes for these tables, are considered Active for Cascade actions. Different labels (other than Active) may be used for this state code in different tables. Any custom state or status code with values other than below will not be processed as an active record for cascading purposes.

| Table Name                       |    State Code 0       |    State Code 1       |    State Code 2       |    State Code 3       | 
| :--------------------------------| :----------------:    | :----------------:    | :----------------:    | :-----------------:    |
|  Account                         |          x            | 	                     | 	                     | 	                     |
|  BulkOperation                   |          x            | 	                     | 	                     | 	                     |
|  BulkOperation                   |          x            | 	                     | 	                     | 	                     |
|  CampaignResponse                |          x            | 	                     | 	                     | 	                     |
|  Contact	                       |          x            | 	                     | 	                     | 	                     |
|  Email	                         |          x            | 	                     | 	                     | 	                     |
|  Fax		                         |          x            | 	                     | 	                     | 	                     |
|  Incident	                       |          x            | 	                     | 	                     | 	                     |
|  IncidentResolution              |          x            | 	                     | 	                     | 	                     |
|  Invoice	                       |          x            | 	                     | 	                     | 	                     |
|  Lead		                         |          x            | 	                     | 	                     | 	                     |
|  Letter	                         |          x            | 	                     | 	                     | 	                     |
|  Opportunity	                   |          x            | 	                     | 	                     | 	                     |
|  OpportunityClose   	           |          x            | 	                     | 	                     | 	                     |
|  OrderClose	                     |          x            | 	                     | 	                     | 	                     |
|  PhoneCall	                     |          x            | 	                     | 	                     | 	                     |
|  SalesOrder	                     |          x            | 	                     | 	                     | 	                     |
|  Task		                         |          x            | 	                     | 	                     | 	                     |
|  All Custom Tables and Custom Activities |          x            | 	                     | 	                     | 	                     |
|  Quotes                          |                       |          x            | 	                     |      	               |
|  Contract                        |                       |                       |          x            | 	                     |
|  Appointment                     |                       | 	                     | 	                     |          x            |
|  ServiceAppointment              |                       | 	                     | 	                     |          x            |
|  RecurringAppointmentMaster      |                       | 	                     | 	                     |          x            |



The `CascadeConfiguration` (<xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration> class or <xref:Microsoft.Dynamics.CRM.CascadeConfiguration?displayProperty=nameWithType>) contains the following properties representing actions that may be performed on the referenced table in the one-to-many relationship.  
  
|Action|Description|Valid options|  
|------------|-----------------|-------------------|  
|Assign|The referenced table record owner is changed.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Delete|The referenced table record is deleted. **Note:**  The options for this action are limited.|Cascade<br />RemoveLink<br />Restrict|  
|Merge|The record is merged with another record. **Note:**  For referenced tables that can be merged, Cascade is the only valid option. In other cases use NoCascade.|Cascade<br />NoCascade|  
|Reparent|See [About the reparent action](#about-the-reparent-action) later.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Share|When the referenced table record is shared with another user.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Unshare|When sharing is removed for the referenced table record.|Active<br />Cascade<br />NoCascade<br />UserOwned|  

> [!NOTE]
> Assign, Delete, Merge, and Reparent actions will not execute in the following situations:
> - If the original parent record and requested action contain the same values. Example: Attempting to trigger an Assign and 
>   choosing a contact that is already the owner of the record
> - Attempting to perform an action on a parent record that is already running a cascading action


> [!NOTE]
> When executing an assign, any workflows or business rules that are currently active on the records will automatically be 
> deactivated when the reassignment occurs. The new owner of the record will need to reactivate the workflow or business rule 
> if they want to continue using it.



<a name="BKMK_ReparentAction"></a>   
### About the reparent action  
 The reparent action is very similar to the share action except that it deals with the inherited access rights instead of explicit access rights. The reparent action is when you change the value of the referencing column in a parental relationship. When a reparent action occurs, the desired scope of the inherited  access rights for related tables might change for ReadAccess, WriteAccess, DeleteAccess, AssignAccess, ShareAccess, AppendAccess and AppendToAccess. It will not change for CreateAccess. The cascade actions related to the reparent action refer to changes to access rights indicated above for the table record and any table records related to it.  

<a name="BKMK_MergeAction"></a>  
### About the merge action  
 The merge action can sometimes have problems completing if a record that is part of the operation set is deleted while the merge system job is running. Often this will result in an error indicating that the record will be "differently parented" or the child record "might lose its parenting". If this occurs, and you would prefer the merge continue forward even if the record is missing, you can choose to disable the parent check when you select the columns to merge.


> [!NOTE]
> When performing a merge between two custom tables, DateTime values will not merge. The DateTime of the target record will remain unchanged.

### See also

[Table relationship definitions](entity-relationship-metadata.md)  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
