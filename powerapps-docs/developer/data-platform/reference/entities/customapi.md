---
title: "Custom API (CustomAPI) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Custom API (CustomAPI) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Custom API (CustomAPI) table/entity reference (Microsoft Dataverse)

Entity that defines a custom API

## Messages

The following table lists the messages for the Custom API (CustomAPI) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /customapis(*customapiid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /customapis<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /customapis(*customapiid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /customapis(*customapiid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /customapis<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /customapis(*customapiid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /customapis(*customapiid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /customapis(*customapiid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Custom API (CustomAPI) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Custom API** |
| **DisplayCollectionName** | **Custom APIs** |
| **SchemaName** | `CustomAPI` |
| **CollectionSchemaName** | `CustomAPIs` |
| **EntitySetName** | `customapis`|
| **LogicalName** | `customapi` |
| **LogicalCollectionName** | `customapis` |
| **PrimaryIdAttribute** | `customapiid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AllowedCustomProcessingStepType](#BKMK_AllowedCustomProcessingStepType)
- [BindingType](#BKMK_BindingType)
- [BoundEntityLogicalName](#BKMK_BoundEntityLogicalName)
- [CustomAPIId](#BKMK_CustomAPIId)
- [Description](#BKMK_Description)
- [DisplayName](#BKMK_DisplayName)
- [ExecutePrivilegeName](#BKMK_ExecutePrivilegeName)
- [FxExpressionId](#BKMK_FxExpressionId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsFunction](#BKMK_IsFunction)
- [IsPrivate](#BKMK_IsPrivate)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PluginTypeId](#BKMK_PluginTypeId)
- [PowerfxRuleId](#BKMK_PowerfxRuleId)
- [SdkMessageId](#BKMK_SdkMessageId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UniqueName](#BKMK_UniqueName)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WorkflowSdkStepEnabled](#BKMK_WorkflowSdkStepEnabled)

### <a name="BKMK_AllowedCustomProcessingStepType"></a> AllowedCustomProcessingStepType

|Property|Value|
|---|---|
|Description|**The type of custom processing step allowed**|
|DisplayName|**Allowed Custom Processing Step Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowedcustomprocessingsteptype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`customapi_allowedcustomprocessingsteptype`|

#### AllowedCustomProcessingStepType Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Async Only**|
|2|**Sync and Async**|

### <a name="BKMK_BindingType"></a> BindingType

|Property|Value|
|---|---|
|Description|**The binding type of the custom API**|
|DisplayName|**Binding Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bindingtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`customapi_bindingtype`|

#### BindingType Choices/Options

|Value|Label|
|---|---|
|0|**Global**|
|1|**Entity**|
|2|**Entity Collection**|

### <a name="BKMK_BoundEntityLogicalName"></a> BoundEntityLogicalName

|Property|Value|
|---|---|
|Description|**The logical name of the entity bound to the custom API**|
|DisplayName|**Bound Entity Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`boundentitylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CustomAPIId"></a> CustomAPIId

|Property|Value|
|---|---|
|Description|**Unique identifier for custom API instances**|
|DisplayName|**Custom API**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customapiid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Localized description for custom API instances**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|300|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**Localized display name for custom API instances**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_ExecutePrivilegeName"></a> ExecutePrivilegeName

|Property|Value|
|---|---|
|Description|**Name of the privilege that allows execution of the custom API**|
|DisplayName|**Execute Privilege Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executeprivilegename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_FxExpressionId"></a> FxExpressionId

|Property|Value|
|---|---|
|Description|**Unique identifier for fxexpression associated with Custom API.**|
|DisplayName|**FxExpression**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fxexpressionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|fxexpression|

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

### <a name="BKMK_IsFunction"></a> IsFunction

|Property|Value|
|---|---|
|Description|**Indicates if the custom API is a function (GET is supported) or not (POST is supported)**|
|DisplayName|**Is Function**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isfunction`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`customapi_isfunction`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPrivate"></a> IsPrivate

|Property|Value|
|---|---|
|Description|**Indicates if the custom API is private (hidden from metadata and documentation)**|
|DisplayName|**Is Private**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isprivate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`customapi_isprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The primary name of the custom API**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
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

### <a name="BKMK_PluginTypeId"></a> PluginTypeId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Plugin Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`plugintypeid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|plugintype|

### <a name="BKMK_PowerfxRuleId"></a> PowerfxRuleId

|Property|Value|
|---|---|
|Description|**Unique identifier for powerfxrule associated with Custom API.**|
|DisplayName|**PowerFx Rule**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerfxruleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|powerfxrule|

### <a name="BKMK_SdkMessageId"></a> SdkMessageId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Sdk Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sdkmessageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sdkmessage|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Custom API**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`customapi_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Custom API**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`customapi_statuscode`|

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

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**Unique name for the custom API**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

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

### <a name="BKMK_WorkflowSdkStepEnabled"></a> WorkflowSdkStepEnabled

|Property|Value|
|---|---|
|Description|**Indicates if the custom API is enabled as a workflow action**|
|DisplayName|**Enabled for Workflow**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`workflowsdkstepenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`customapi_workflowsdkstepenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|


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

- [business_unit_customapi](#BKMK_business_unit_customapi)
- [fxexpression_customapi](#BKMK_fxexpression_customapi)
- [lk_customapi_createdby](#BKMK_lk_customapi_createdby)
- [lk_customapi_createdonbehalfby](#BKMK_lk_customapi_createdonbehalfby)
- [lk_customapi_modifiedby](#BKMK_lk_customapi_modifiedby)
- [lk_customapi_modifiedonbehalfby](#BKMK_lk_customapi_modifiedonbehalfby)
- [owner_customapi](#BKMK_owner_customapi)
- [plugintype_customapi](#BKMK_plugintype_customapi)
- [powerfxrule_customapi](#BKMK_powerfxrule_customapi)
- [sdkmessage_customapi](#BKMK_sdkmessage_customapi)
- [team_customapi](#BKMK_team_customapi)
- [user_customapi](#BKMK_user_customapi)

### <a name="BKMK_business_unit_customapi"></a> business_unit_customapi

One-To-Many Relationship: [businessunit business_unit_customapi](businessunit.md#BKMK_business_unit_customapi)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_customapi"></a> fxexpression_customapi

One-To-Many Relationship: [fxexpression fxexpression_customapi](fxexpression.md#BKMK_fxexpression_customapi)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`fxexpressionid`|
|ReferencingEntityNavigationPropertyName|`fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customapi_createdby"></a> lk_customapi_createdby

One-To-Many Relationship: [systemuser lk_customapi_createdby](systemuser.md#BKMK_lk_customapi_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customapi_createdonbehalfby"></a> lk_customapi_createdonbehalfby

One-To-Many Relationship: [systemuser lk_customapi_createdonbehalfby](systemuser.md#BKMK_lk_customapi_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customapi_modifiedby"></a> lk_customapi_modifiedby

One-To-Many Relationship: [systemuser lk_customapi_modifiedby](systemuser.md#BKMK_lk_customapi_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customapi_modifiedonbehalfby"></a> lk_customapi_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_customapi_modifiedonbehalfby](systemuser.md#BKMK_lk_customapi_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_customapi"></a> owner_customapi

One-To-Many Relationship: [owner owner_customapi](owner.md#BKMK_owner_customapi)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugintype_customapi"></a> plugintype_customapi

One-To-Many Relationship: [plugintype plugintype_customapi](plugintype.md#BKMK_plugintype_customapi)

|Property|Value|
|---|---|
|ReferencedEntity|`plugintype`|
|ReferencedAttribute|`plugintypeid`|
|ReferencingAttribute|`plugintypeid`|
|ReferencingEntityNavigationPropertyName|`PluginTypeId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_customapi"></a> powerfxrule_customapi

One-To-Many Relationship: [powerfxrule powerfxrule_customapi](powerfxrule.md#BKMK_powerfxrule_customapi)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`powerfxruleid`|
|ReferencingEntityNavigationPropertyName|`powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sdkmessage_customapi"></a> sdkmessage_customapi

One-To-Many Relationship: [sdkmessage sdkmessage_customapi](sdkmessage.md#BKMK_sdkmessage_customapi)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessage`|
|ReferencedAttribute|`sdkmessageid`|
|ReferencingAttribute|`sdkmessageid`|
|ReferencingEntityNavigationPropertyName|`SdkMessageId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_customapi"></a> team_customapi

One-To-Many Relationship: [team team_customapi](team.md#BKMK_team_customapi)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_customapi"></a> user_customapi

One-To-Many Relationship: [systemuser user_customapi](systemuser.md#BKMK_user_customapi)

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

- [AIPluginOperation_CustomAPI_CustomAPI](#BKMK_AIPluginOperation_CustomAPI_CustomAPI)
- [catalogassignment_customapi](#BKMK_catalogassignment_customapi)
- [customapi_AsyncOperations](#BKMK_customapi_AsyncOperations)
- [customapi_BulkDeleteFailures](#BKMK_customapi_BulkDeleteFailures)
- [customapi_customapirequestparameter](#BKMK_customapi_customapirequestparameter)
- [customapi_customapiresponseproperty](#BKMK_customapi_customapiresponseproperty)
- [customapi_MailboxTrackingFolders](#BKMK_customapi_MailboxTrackingFolders)
- [customapi_msdyn_function_customapi](#BKMK_customapi_msdyn_function_customapi)
- [customapi_plugin_CustomAPI](#BKMK_customapi_plugin_CustomAPI)
- [customapi_PrincipalObjectAttributeAccesses](#BKMK_customapi_PrincipalObjectAttributeAccesses)
- [customapi_ProcessSession](#BKMK_customapi_ProcessSession)
- [customapi_serviceplanmapping](#BKMK_customapi_serviceplanmapping)
- [customapi_SyncErrors](#BKMK_customapi_SyncErrors)
- [fabricaiskill_customapiid](#BKMK_fabricaiskill_customapiid)
- [MCPTool_CustomAPI_CustomAPI](#BKMK_MCPTool_CustomAPI_CustomAPI)
- [msdyn_customapi_msdyn_pmbusinessruleautomationconfig_CustomApiId](#BKMK_msdyn_customapi_msdyn_pmbusinessruleautomationconfig_CustomApiId)
- [msdyn_formmapping_customapiid](#BKMK_msdyn_formmapping_customapiid)
- [msdyn_knowledgeassetconfiguration_customapiid](#BKMK_msdyn_knowledgeassetconfiguration_customapiid)

### <a name="BKMK_AIPluginOperation_CustomAPI_CustomAPI"></a> AIPluginOperation_CustomAPI_CustomAPI

Many-To-One Relationship: [aipluginoperation AIPluginOperation_CustomAPI_CustomAPI](aipluginoperation.md#BKMK_AIPluginOperation_CustomAPI_CustomAPI)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`customapi`|
|ReferencedEntityNavigationPropertyName|`AIPluginOperation_CustomAPI_CustomAPI`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_catalogassignment_customapi"></a> catalogassignment_customapi

Many-To-One Relationship: [catalogassignment catalogassignment_customapi](catalogassignment.md#BKMK_catalogassignment_customapi)

|Property|Value|
|---|---|
|ReferencingEntity|`catalogassignment`|
|ReferencingAttribute|`object`|
|ReferencedEntityNavigationPropertyName|`CatalogAssignments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_AsyncOperations"></a> customapi_AsyncOperations

Many-To-One Relationship: [asyncoperation customapi_AsyncOperations](asyncoperation.md#BKMK_customapi_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`customapi_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_BulkDeleteFailures"></a> customapi_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure customapi_BulkDeleteFailures](bulkdeletefailure.md#BKMK_customapi_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`customapi_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_customapirequestparameter"></a> customapi_customapirequestparameter

Many-To-One Relationship: [customapirequestparameter customapi_customapirequestparameter](customapirequestparameter.md#BKMK_customapi_customapirequestparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`customapirequestparameter`|
|ReferencingAttribute|`customapiid`|
|ReferencedEntityNavigationPropertyName|`CustomAPIRequestParameters`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_customapiresponseproperty"></a> customapi_customapiresponseproperty

Many-To-One Relationship: [customapiresponseproperty customapi_customapiresponseproperty](customapiresponseproperty.md#BKMK_customapi_customapiresponseproperty)

|Property|Value|
|---|---|
|ReferencingEntity|`customapiresponseproperty`|
|ReferencingAttribute|`customapiid`|
|ReferencedEntityNavigationPropertyName|`CustomAPIResponseProperties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_MailboxTrackingFolders"></a> customapi_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder customapi_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_customapi_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`customapi_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_msdyn_function_customapi"></a> customapi_msdyn_function_customapi

Many-To-One Relationship: [msdyn_function customapi_msdyn_function_customapi](msdyn_function.md#BKMK_customapi_msdyn_function_customapi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_function`|
|ReferencingAttribute|`customapi`|
|ReferencedEntityNavigationPropertyName|`customapi_msdyn_function_customapi`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_plugin_CustomAPI"></a> customapi_plugin_CustomAPI

Many-To-One Relationship: [plugin customapi_plugin_CustomAPI](plugin.md#BKMK_customapi_plugin_CustomAPI)

|Property|Value|
|---|---|
|ReferencingEntity|`plugin`|
|ReferencingAttribute|`customapi`|
|ReferencedEntityNavigationPropertyName|`customapi_plugin_CustomAPI`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_PrincipalObjectAttributeAccesses"></a> customapi_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess customapi_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_customapi_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`customapi_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_ProcessSession"></a> customapi_ProcessSession

Many-To-One Relationship: [processsession customapi_ProcessSession](processsession.md#BKMK_customapi_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`customapi_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_serviceplanmapping"></a> customapi_serviceplanmapping

Many-To-One Relationship: [serviceplanmapping customapi_serviceplanmapping](serviceplanmapping.md#BKMK_customapi_serviceplanmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`serviceplanmapping`|
|ReferencingAttribute|`customapi`|
|ReferencedEntityNavigationPropertyName|`customapi_serviceplanmapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customapi_SyncErrors"></a> customapi_SyncErrors

Many-To-One Relationship: [syncerror customapi_SyncErrors](syncerror.md#BKMK_customapi_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`customapi_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_fabricaiskill_customapiid"></a> fabricaiskill_customapiid

Many-To-One Relationship: [fabricaiskill fabricaiskill_customapiid](fabricaiskill.md#BKMK_fabricaiskill_customapiid)

|Property|Value|
|---|---|
|ReferencingEntity|`fabricaiskill`|
|ReferencingAttribute|`customapiid`|
|ReferencedEntityNavigationPropertyName|`fabricaiskill_customapiid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_MCPTool_CustomAPI_CustomAPI"></a> MCPTool_CustomAPI_CustomAPI

Many-To-One Relationship: [mcptool MCPTool_CustomAPI_CustomAPI](mcptool.md#BKMK_MCPTool_CustomAPI_CustomAPI)

|Property|Value|
|---|---|
|ReferencingEntity|`mcptool`|
|ReferencingAttribute|`customapiid`|
|ReferencedEntityNavigationPropertyName|`MCPTool_CustomAPI_CustomAPI`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customapi_msdyn_pmbusinessruleautomationconfig_CustomApiId"></a> msdyn_customapi_msdyn_pmbusinessruleautomationconfig_CustomApiId

Many-To-One Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_customapi_msdyn_pmbusinessruleautomationconfig_CustomApiId](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_customapi_msdyn_pmbusinessruleautomationconfig_CustomApiId)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencingAttribute|`customapiid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customapi_msdyn_pmbusinessruleautomationconfig_CustomApiId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_formmapping_customapiid"></a> msdyn_formmapping_customapiid

Many-To-One Relationship: [msdyn_formmapping msdyn_formmapping_customapiid](msdyn_formmapping.md#BKMK_msdyn_formmapping_customapiid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_formmapping`|
|ReferencingAttribute|`customapiid`|
|ReferencedEntityNavigationPropertyName|`msdyn_formmapping_customapiid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_customapiid"></a> msdyn_knowledgeassetconfiguration_customapiid

Many-To-One Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_customapiid](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_customapiid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencingAttribute|`msdyn_customapiid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeassetconfiguration_customapiid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.customapi?displayProperty=fullName>
