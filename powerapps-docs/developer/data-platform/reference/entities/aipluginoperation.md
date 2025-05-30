---
title: "AIPluginOperation table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AIPluginOperation table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AIPluginOperation table/entity reference (Microsoft Dataverse)

AIPluginOperations component

## Messages

The following table lists the messages for the AIPluginOperation table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /aipluginoperations(*aipluginoperationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /aipluginoperations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /aipluginoperations(*aipluginoperationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /aipluginoperations(*aipluginoperationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /aipluginoperations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RetrieveUnpublished`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /aipluginoperations(*aipluginoperationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /aipluginoperations(*aipluginoperationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /aipluginoperations(*aipluginoperationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AIPluginOperation table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AIPluginOperation** |
| **DisplayCollectionName** | **AIPluginOperations** |
| **SchemaName** | `AIPluginOperation` |
| **CollectionSchemaName** | `AIPluginOperations` |
| **EntitySetName** | `aipluginoperations`|
| **LogicalName** | `aipluginoperation` |
| **LogicalCollectionName** | `aipluginoperations` |
| **PrimaryIdAttribute** | `aipluginoperationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AIPlugin](#BKMK_AIPlugin)
- [AIPluginOperationExportKey](#BKMK_AIPluginOperationExportKey)
- [AIPluginOperationId](#BKMK_AIPluginOperationId)
- [AIPluginOperationResponseTemplate](#BKMK_AIPluginOperationResponseTemplate)
- [CustomAPI](#BKMK_CustomAPI)
- [Description](#BKMK_Description)
- [DVFileSearch](#BKMK_DVFileSearch)
- [DVTableSearch](#BKMK_DVTableSearch)
- [Entity](#BKMK_Entity)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsConsequential](#BKMK_IsConsequential)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_AIModel](#BKMK_msdyn_AIModel)
- [Name](#BKMK_Name)
- [OperationId](#BKMK_OperationId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ReferencedOperationId](#BKMK_ReferencedOperationId)
- [ResponseSemantics](#BKMK_ResponseSemantics)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [Workflow](#BKMK_Workflow)

### <a name="BKMK_AIPlugin"></a> AIPlugin

|Property|Value|
|---|---|
|Description||
|DisplayName|**AIPlugin**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aiplugin`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|aiplugin|

### <a name="BKMK_AIPluginOperationExportKey"></a> AIPluginOperationExportKey

|Property|Value|
|---|---|
|Description||
|DisplayName|**AI Plugin Operation Export Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aipluginoperationexportkey`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

### <a name="BKMK_AIPluginOperationId"></a> AIPluginOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AIPluginOperation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`aipluginoperationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AIPluginOperationResponseTemplate"></a> AIPluginOperationResponseTemplate

|Property|Value|
|---|---|
|Description||
|DisplayName|**AIPluginOperationResponseTemplate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aipluginoperationresponsetemplate`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|aipluginoperationresponsetemplate|

### <a name="BKMK_CustomAPI"></a> CustomAPI

|Property|Value|
|---|---|
|Description||
|DisplayName|**Custom API**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customapi`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|customapi|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Operation Description**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_DVFileSearch"></a> DVFileSearch

|Property|Value|
|---|---|
|Description||
|DisplayName|**DVFileSearch**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dvfilesearch`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|dvfilesearch|

### <a name="BKMK_DVTableSearch"></a> DVTableSearch

|Property|Value|
|---|---|
|Description||
|DisplayName|**DVTableSearch**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dvtablesearch`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|dvtablesearch|

### <a name="BKMK_Entity"></a> Entity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entity`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|entity|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsConsequential"></a> IsConsequential

|Property|Value|
|---|---|
|Description|**Defines if the AIPluginOperation is consequential.**|
|DisplayName|**Is Consequential**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isconsequential`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`aipluginoperation_isconsequential`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_msdyn_AIModel"></a> msdyn_AIModel

|Property|Value|
|---|---|
|Description|**Lookup to AI Model**|
|DisplayName|**AIModel**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aimodel`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_aimodel|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OperationId"></a> OperationId

|Property|Value|
|---|---|
|Description|**OperationId on the swagger file**|
|DisplayName|**OperationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ReferencedOperationId"></a> ReferencedOperationId

|Property|Value|
|---|---|
|Description|**ReferencedOperationId Description**|
|DisplayName|**ReferencedOperationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`referencedoperationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ResponseSemantics"></a> ResponseSemantics

|Property|Value|
|---|---|
|Description|**ResponseSemantics for the AI Plugin Operation**|
|DisplayName|**ResponseSemantics**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`responsesemantics`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the AIPluginOperation**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`aipluginoperation_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the AIPluginOperation**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`aipluginoperation_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_Workflow"></a> Workflow

|Property|Value|
|---|---|
|Description||
|DisplayName|**Process**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`workflow`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [AIPluginOperation_AIPlugin_AIPlugin](#BKMK_AIPluginOperation_AIPlugin_AIPlugin)
- [AIPluginOperation_CustomAPI_CustomAPI](#BKMK_AIPluginOperation_CustomAPI_CustomAPI)
- [AIPluginOperation_DVFileSearch_DVFileSear](#BKMK_AIPluginOperation_DVFileSearch_DVFileSear)
- [AIPluginOperation_DVTableSearch_DVTableSe](#BKMK_AIPluginOperation_DVTableSearch_DVTableSe)
- [AIPluginOperation_Entity_Entity](#BKMK_AIPluginOperation_Entity_Entity)
- [AIPluginOperation_Workflow_Workflow](#BKMK_AIPluginOperation_Workflow_Workflow)
- [business_unit_aipluginoperation](#BKMK_business_unit_aipluginoperation)
- [lk_aipluginoperation_createdby](#BKMK_lk_aipluginoperation_createdby)
- [lk_aipluginoperation_createdonbehalfby](#BKMK_lk_aipluginoperation_createdonbehalfby)
- [lk_aipluginoperation_modifiedby](#BKMK_lk_aipluginoperation_modifiedby)
- [lk_aipluginoperation_modifiedonbehalfby](#BKMK_lk_aipluginoperation_modifiedonbehalfby)
- [msdyn_AIPluginOperation_AIModel](#BKMK_msdyn_AIPluginOperation_AIModel)
- [operationresponsetemplate_aipluginoperation](#BKMK_operationresponsetemplate_aipluginoperation)
- [owner_aipluginoperation](#BKMK_owner_aipluginoperation)
- [team_aipluginoperation](#BKMK_team_aipluginoperation)
- [user_aipluginoperation](#BKMK_user_aipluginoperation)

### <a name="BKMK_AIPluginOperation_AIPlugin_AIPlugin"></a> AIPluginOperation_AIPlugin_AIPlugin

One-To-Many Relationship: [aiplugin AIPluginOperation_AIPlugin_AIPlugin](aiplugin.md#BKMK_AIPluginOperation_AIPlugin_AIPlugin)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugin`|
|ReferencedAttribute|`aipluginid`|
|ReferencingAttribute|`aiplugin`|
|ReferencingEntityNavigationPropertyName|`AIPlugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_AIPluginOperation_CustomAPI_CustomAPI"></a> AIPluginOperation_CustomAPI_CustomAPI

One-To-Many Relationship: [customapi AIPluginOperation_CustomAPI_CustomAPI](customapi.md#BKMK_AIPluginOperation_CustomAPI_CustomAPI)

|Property|Value|
|---|---|
|ReferencedEntity|`customapi`|
|ReferencedAttribute|`customapiid`|
|ReferencingAttribute|`customapi`|
|ReferencingEntityNavigationPropertyName|`CustomAPI`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AIPluginOperation_DVFileSearch_DVFileSear"></a> AIPluginOperation_DVFileSearch_DVFileSear

One-To-Many Relationship: [dvfilesearch AIPluginOperation_DVFileSearch_DVFileSear](dvfilesearch.md#BKMK_AIPluginOperation_DVFileSearch_DVFileSear)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearch`|
|ReferencedAttribute|`dvfilesearchid`|
|ReferencingAttribute|`dvfilesearch`|
|ReferencingEntityNavigationPropertyName|`DVFileSearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AIPluginOperation_DVTableSearch_DVTableSe"></a> AIPluginOperation_DVTableSearch_DVTableSe

One-To-Many Relationship: [dvtablesearch AIPluginOperation_DVTableSearch_DVTableSe](dvtablesearch.md#BKMK_AIPluginOperation_DVTableSearch_DVTableSe)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`dvtablesearch`|
|ReferencingEntityNavigationPropertyName|`DVTableSearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AIPluginOperation_Entity_Entity"></a> AIPluginOperation_Entity_Entity

One-To-Many Relationship: [entity AIPluginOperation_Entity_Entity](entity.md#BKMK_AIPluginOperation_Entity_Entity)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`entity`|
|ReferencingEntityNavigationPropertyName|`Entity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AIPluginOperation_Workflow_Workflow"></a> AIPluginOperation_Workflow_Workflow

One-To-Many Relationship: [workflow AIPluginOperation_Workflow_Workflow](workflow.md#BKMK_AIPluginOperation_Workflow_Workflow)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`workflow`|
|ReferencingEntityNavigationPropertyName|`Workflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_aipluginoperation"></a> business_unit_aipluginoperation

One-To-Many Relationship: [businessunit business_unit_aipluginoperation](businessunit.md#BKMK_business_unit_aipluginoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aipluginoperation_createdby"></a> lk_aipluginoperation_createdby

One-To-Many Relationship: [systemuser lk_aipluginoperation_createdby](systemuser.md#BKMK_lk_aipluginoperation_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aipluginoperation_createdonbehalfby"></a> lk_aipluginoperation_createdonbehalfby

One-To-Many Relationship: [systemuser lk_aipluginoperation_createdonbehalfby](systemuser.md#BKMK_lk_aipluginoperation_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aipluginoperation_modifiedby"></a> lk_aipluginoperation_modifiedby

One-To-Many Relationship: [systemuser lk_aipluginoperation_modifiedby](systemuser.md#BKMK_lk_aipluginoperation_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aipluginoperation_modifiedonbehalfby"></a> lk_aipluginoperation_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_aipluginoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_aipluginoperation_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_AIPluginOperation_AIModel"></a> msdyn_AIPluginOperation_AIModel

One-To-Many Relationship: [msdyn_aimodel msdyn_AIPluginOperation_AIModel](msdyn_aimodel.md#BKMK_msdyn_AIPluginOperation_AIModel)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`msdyn_aimodel`|
|ReferencingEntityNavigationPropertyName|`msdyn_AIModel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_operationresponsetemplate_aipluginoperation"></a> operationresponsetemplate_aipluginoperation

One-To-Many Relationship: [aipluginoperationresponsetemplate operationresponsetemplate_aipluginoperation](aipluginoperationresponsetemplate.md#BKMK_operationresponsetemplate_aipluginoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`aipluginoperationresponsetemplate`|
|ReferencingEntityNavigationPropertyName|`AIPluginOperationResponseTemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_aipluginoperation"></a> owner_aipluginoperation

One-To-Many Relationship: [owner owner_aipluginoperation](owner.md#BKMK_owner_aipluginoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_aipluginoperation"></a> team_aipluginoperation

One-To-Many Relationship: [team team_aipluginoperation](team.md#BKMK_team_aipluginoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_aipluginoperation"></a> user_aipluginoperation

One-To-Many Relationship: [systemuser user_aipluginoperation](systemuser.md#BKMK_user_aipluginoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [aipluginoperation_AsyncOperations](#BKMK_aipluginoperation_AsyncOperations)
- [aipluginoperation_BulkDeleteFailures](#BKMK_aipluginoperation_BulkDeleteFailures)
- [aipluginoperation_MailboxTrackingFolders](#BKMK_aipluginoperation_MailboxTrackingFolders)
- [aipluginoperation_PrincipalObjectAttributeAccesses](#BKMK_aipluginoperation_PrincipalObjectAttributeAccesses)
- [aipluginoperation_ProcessSession](#BKMK_aipluginoperation_ProcessSession)
- [aipluginoperation_SyncErrors](#BKMK_aipluginoperation_SyncErrors)
- [AIPluginOperationParameter_AIPluginO](#BKMK_AIPluginOperationParameter_AIPluginO)
- [fabricaiskill_aipluginoperationid](#BKMK_fabricaiskill_aipluginoperationid)
- [msdyn_knowledgeassetconfiguration_aipluginoperationid](#BKMK_msdyn_knowledgeassetconfiguration_aipluginoperationid)

### <a name="BKMK_aipluginoperation_AsyncOperations"></a> aipluginoperation_AsyncOperations

Many-To-One Relationship: [asyncoperation aipluginoperation_AsyncOperations](asyncoperation.md#BKMK_aipluginoperation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aipluginoperation_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aipluginoperation_BulkDeleteFailures"></a> aipluginoperation_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure aipluginoperation_BulkDeleteFailures](bulkdeletefailure.md#BKMK_aipluginoperation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aipluginoperation_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aipluginoperation_MailboxTrackingFolders"></a> aipluginoperation_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder aipluginoperation_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_aipluginoperation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aipluginoperation_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aipluginoperation_PrincipalObjectAttributeAccesses"></a> aipluginoperation_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess aipluginoperation_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_aipluginoperation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`aipluginoperation_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aipluginoperation_ProcessSession"></a> aipluginoperation_ProcessSession

Many-To-One Relationship: [processsession aipluginoperation_ProcessSession](processsession.md#BKMK_aipluginoperation_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aipluginoperation_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aipluginoperation_SyncErrors"></a> aipluginoperation_SyncErrors

Many-To-One Relationship: [syncerror aipluginoperation_SyncErrors](syncerror.md#BKMK_aipluginoperation_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aipluginoperation_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AIPluginOperationParameter_AIPluginO"></a> AIPluginOperationParameter_AIPluginO

Many-To-One Relationship: [aipluginoperationparameter AIPluginOperationParameter_AIPluginO](aipluginoperationparameter.md#BKMK_AIPluginOperationParameter_AIPluginO)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperationparameter`|
|ReferencingAttribute|`aipluginoperation`|
|ReferencedEntityNavigationPropertyName|`AIPluginOperationParameter_AIPluginO`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_fabricaiskill_aipluginoperationid"></a> fabricaiskill_aipluginoperationid

Many-To-One Relationship: [fabricaiskill fabricaiskill_aipluginoperationid](fabricaiskill.md#BKMK_fabricaiskill_aipluginoperationid)

|Property|Value|
|---|---|
|ReferencingEntity|`fabricaiskill`|
|ReferencingAttribute|`aipluginoperationid`|
|ReferencedEntityNavigationPropertyName|`fabricaiskill_aipluginoperationid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_aipluginoperationid"></a> msdyn_knowledgeassetconfiguration_aipluginoperationid

Many-To-One Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_aipluginoperationid](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_aipluginoperationid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencingAttribute|`msdyn_aipluginoperationid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeassetconfiguration_aipluginoperationid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_botcomponent_aipluginoperation"></a> botcomponent_aipluginoperation

See [botcomponent botcomponent_aipluginoperation Many-To-Many Relationship](botcomponent.md#BKMK_botcomponent_aipluginoperation)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_aipluginoperation`|
|IsCustomizable|False|
|SchemaName|`botcomponent_aipluginoperation`|
|IntersectAttribute|`aipluginoperationid`|
|NavigationPropertyName|`botcomponent_aipluginoperation`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.aipluginoperation?displayProperty=fullName>
