---
title: "Connection Reference (connectionreference) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Connection Reference (connectionreference) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Connection Reference (connectionreference) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Connection Reference (connectionreference) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /connectionreferences(*connectionreferenceid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /connectionreferences<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /connectionreferences(*connectionreferenceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `PvaShareConnection`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaShareConnection?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: False |`GET` /connectionreferences(*connectionreferenceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /connectionreferences<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /connectionreferences(*connectionreferenceid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /connectionreferences(*connectionreferenceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /connectionreferences(*connectionreferenceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Connection Reference (connectionreference) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Connection Reference** |
| **DisplayCollectionName** | **Connection References** |
| **SchemaName** | `connectionreference` |
| **CollectionSchemaName** | `connectionreferences` |
| **EntitySetName** | `connectionreferences`|
| **LogicalName** | `connectionreference` |
| **LogicalCollectionName** | `connectionreferences` |
| **PrimaryIdAttribute** | `connectionreferenceid` |
| **PrimaryNameAttribute** |`connectionreferencedisplayname` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConnectionId](#BKMK_ConnectionId)
- [ConnectionParametersConfig](#BKMK_ConnectionParametersConfig)
- [ConnectionParameterSetConfig](#BKMK_ConnectionParameterSetConfig)
- [connectionreferencedisplayname](#BKMK_connectionreferencedisplayname)
- [connectionreferenceId](#BKMK_connectionreferenceId)
- [ConnectionReferenceLogicalName](#BKMK_ConnectionReferenceLogicalName)
- [ConnectorId](#BKMK_ConnectorId)
- [CustomConnectorId](#BKMK_CustomConnectorId)
- [Description](#BKMK_Description)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PromptingBehavior](#BKMK_PromptingBehavior)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ConnectionId"></a> ConnectionId

|Property|Value|
|---|---|
|Description|**Id of the connection in API hub**|
|DisplayName|**Connection Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_ConnectionParametersConfig"></a> ConnectionParametersConfig

|Property|Value|
|---|---|
|Description|**Connection parameters that can be reused when creating connections in Microsoft Copilot Studio**|
|DisplayName|**Connection Parameters Config**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionparametersconfig`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_ConnectionParameterSetConfig"></a> ConnectionParameterSetConfig

|Property|Value|
|---|---|
|Description|**The connection parameters set that can be reused when creating connections in Microsoft Copilot Studio**|
|DisplayName|**Connection Parameters Set Config**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionparametersetconfig`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_connectionreferencedisplayname"></a> connectionreferencedisplayname

|Property|Value|
|---|---|
|Description|**Display name of the connection reference**|
|DisplayName|**Connection Reference Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionreferencedisplayname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_connectionreferenceId"></a> connectionreferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Connection Reference**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`connectionreferenceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ConnectionReferenceLogicalName"></a> ConnectionReferenceLogicalName

|Property|Value|
|---|---|
|Description|**Connection Reference unique name**|
|DisplayName|**Connection Reference Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionreferencelogicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ConnectorId"></a> ConnectorId

|Property|Value|
|---|---|
|Description|**Id of the Public/Shared Connector**|
|DisplayName|**Connector Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectorid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_CustomConnectorId"></a> CustomConnectorId

|Property|Value|
|---|---|
|Description|**Look up to the Connector entity**|
|DisplayName|**Custom Connector Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customconnectorid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connector|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of Connection Reference**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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

### <a name="BKMK_PromptingBehavior"></a> PromptingBehavior

|Property|Value|
|---|---|
|Description|**The Prompting Behavior for this connection reference**|
|DisplayName|**Prompting Behavior**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`promptingbehavior`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`connectionreference_promptingbehavior`|

#### PromptingBehavior Choices/Options

|Value|Label|
|---|---|
|0|**Prompt on import**|
|1|**Skip**|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Connection Reference**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`connectionreference_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Connection Reference**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`connectionreference_statuscode`|

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

- [business_unit_connectionreference](#BKMK_business_unit_connectionreference)
- [connector_connectionreference](#BKMK_connector_connectionreference)
- [lk_connectionreference_createdby](#BKMK_lk_connectionreference_createdby)
- [lk_connectionreference_createdonbehalfby](#BKMK_lk_connectionreference_createdonbehalfby)
- [lk_connectionreference_modifiedby](#BKMK_lk_connectionreference_modifiedby)
- [lk_connectionreference_modifiedonbehalfby](#BKMK_lk_connectionreference_modifiedonbehalfby)
- [owner_connectionreference](#BKMK_owner_connectionreference)
- [team_connectionreference](#BKMK_team_connectionreference)
- [user_connectionreference](#BKMK_user_connectionreference)

### <a name="BKMK_business_unit_connectionreference"></a> business_unit_connectionreference

One-To-Many Relationship: [businessunit business_unit_connectionreference](businessunit.md#BKMK_business_unit_connectionreference)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_connectionreference"></a> connector_connectionreference

One-To-Many Relationship: [connector connector_connectionreference](connector.md#BKMK_connector_connectionreference)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`customconnectorid`|
|ReferencingEntityNavigationPropertyName|`CustomConnectorId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_connectionreference_createdby"></a> lk_connectionreference_createdby

One-To-Many Relationship: [systemuser lk_connectionreference_createdby](systemuser.md#BKMK_lk_connectionreference_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_connectionreference_createdonbehalfby"></a> lk_connectionreference_createdonbehalfby

One-To-Many Relationship: [systemuser lk_connectionreference_createdonbehalfby](systemuser.md#BKMK_lk_connectionreference_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_connectionreference_modifiedby"></a> lk_connectionreference_modifiedby

One-To-Many Relationship: [systemuser lk_connectionreference_modifiedby](systemuser.md#BKMK_lk_connectionreference_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_connectionreference_modifiedonbehalfby"></a> lk_connectionreference_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_connectionreference_modifiedonbehalfby](systemuser.md#BKMK_lk_connectionreference_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_connectionreference"></a> owner_connectionreference

One-To-Many Relationship: [owner owner_connectionreference](owner.md#BKMK_owner_connectionreference)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_connectionreference"></a> team_connectionreference

One-To-Many Relationship: [team team_connectionreference](team.md#BKMK_team_connectionreference)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_connectionreference"></a> user_connectionreference

One-To-Many Relationship: [systemuser user_connectionreference](systemuser.md#BKMK_user_connectionreference)

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

- [bot_connectionreference](#BKMK_bot_connectionreference)
- [connectionreference_AsyncOperations](#BKMK_connectionreference_AsyncOperations)
- [connectionreference_BulkDeleteFailures](#BKMK_connectionreference_BulkDeleteFailures)
- [connectionreference_connectioninstance](#BKMK_connectionreference_connectioninstance)
- [ConnectionReference_DVTableSearch](#BKMK_ConnectionReference_DVTableSearch)
- [connectionreference_federatedknowledgeconfiguration](#BKMK_connectionreference_federatedknowledgeconfiguration)
- [connectionreference_MailboxTrackingFolders](#BKMK_connectionreference_MailboxTrackingFolders)
- [connectionreference_PrincipalObjectAttributeAccesses](#BKMK_connectionreference_PrincipalObjectAttributeAccesses)
- [connectionreference_ProcessSession](#BKMK_connectionreference_ProcessSession)
- [connectionreference_SyncErrors](#BKMK_connectionreference_SyncErrors)
- [msdyn_AIConfiguration_ConnectionReference](#BKMK_msdyn_AIConfiguration_ConnectionReference)
- [msdyn_connectionreference_msdyn_aimodelcatalog_ConnectionReferenceId](#BKMK_msdyn_connectionreference_msdyn_aimodelcatalog_ConnectionReferenceId)
- [msdyn_connreference_msdyn_connectordatasource](#BKMK_msdyn_connreference_msdyn_connectordatasource)
- [msdyn_dfcr_cr_connect](#BKMK_msdyn_dfcr_cr_connect)

### <a name="BKMK_bot_connectionreference"></a> bot_connectionreference

Many-To-One Relationship: [bot bot_connectionreference](bot.md#BKMK_bot_connectionreference)

|Property|Value|
|---|---|
|ReferencingEntity|`bot`|
|ReferencingAttribute|`providerconnectionreferenceid`|
|ReferencedEntityNavigationPropertyName|`bot_connectionreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_AsyncOperations"></a> connectionreference_AsyncOperations

Many-To-One Relationship: [asyncoperation connectionreference_AsyncOperations](asyncoperation.md#BKMK_connectionreference_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`connectionreference_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_BulkDeleteFailures"></a> connectionreference_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure connectionreference_BulkDeleteFailures](bulkdeletefailure.md#BKMK_connectionreference_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`connectionreference_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_connectioninstance"></a> connectionreference_connectioninstance

Many-To-One Relationship: [connectioninstance connectionreference_connectioninstance](connectioninstance.md#BKMK_connectionreference_connectioninstance)

|Property|Value|
|---|---|
|ReferencingEntity|`connectioninstance`|
|ReferencingAttribute|`connectionreferenceid`|
|ReferencedEntityNavigationPropertyName|`connectionreference_connectioninstance`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ConnectionReference_DVTableSearch"></a> ConnectionReference_DVTableSearch

Many-To-One Relationship: [dvtablesearch ConnectionReference_DVTableSearch](dvtablesearch.md#BKMK_ConnectionReference_DVTableSearch)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearch`|
|ReferencingAttribute|`connectionreference`|
|ReferencedEntityNavigationPropertyName|`ConnectionReference_DVTableSearch`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_federatedknowledgeconfiguration"></a> connectionreference_federatedknowledgeconfiguration

Many-To-One Relationship: [federatedknowledgeconfiguration connectionreference_federatedknowledgeconfiguration](federatedknowledgeconfiguration.md#BKMK_connectionreference_federatedknowledgeconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`federatedknowledgeconfiguration`|
|ReferencingAttribute|`connectionreference`|
|ReferencedEntityNavigationPropertyName|`connectionreference_federatedknowledgeconfiguration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_MailboxTrackingFolders"></a> connectionreference_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder connectionreference_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_connectionreference_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`connectionreference_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_PrincipalObjectAttributeAccesses"></a> connectionreference_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess connectionreference_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_connectionreference_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`connectionreference_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_ProcessSession"></a> connectionreference_ProcessSession

Many-To-One Relationship: [processsession connectionreference_ProcessSession](processsession.md#BKMK_connectionreference_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`connectionreference_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connectionreference_SyncErrors"></a> connectionreference_SyncErrors

Many-To-One Relationship: [syncerror connectionreference_SyncErrors](syncerror.md#BKMK_connectionreference_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`connectionreference_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_AIConfiguration_ConnectionReference"></a> msdyn_AIConfiguration_ConnectionReference

Many-To-One Relationship: [msdyn_aiconfiguration msdyn_AIConfiguration_ConnectionReference](msdyn_aiconfiguration.md#BKMK_msdyn_AIConfiguration_ConnectionReference)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiconfiguration`|
|ReferencingAttribute|`msdyn_connectionreferenceid`|
|ReferencedEntityNavigationPropertyName|`msdyn_AIConfiguration_ConnectionReference`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_connectionreference_msdyn_aimodelcatalog_ConnectionReferenceId"></a> msdyn_connectionreference_msdyn_aimodelcatalog_ConnectionReferenceId

Many-To-One Relationship: [msdyn_aimodelcatalog msdyn_connectionreference_msdyn_aimodelcatalog_ConnectionReferenceId](msdyn_aimodelcatalog.md#BKMK_msdyn_connectionreference_msdyn_aimodelcatalog_ConnectionReferenceId)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aimodelcatalog`|
|ReferencingAttribute|`msdyn_connectionreferenceid`|
|ReferencedEntityNavigationPropertyName|`msdyn_connectionreference_msdyn_aimodelcatalog_ConnectionReferenceId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_connreference_msdyn_connectordatasource"></a> msdyn_connreference_msdyn_connectordatasource

Many-To-One Relationship: [msdyn_connectordatasource msdyn_connreference_msdyn_connectordatasource](msdyn_connectordatasource.md#BKMK_msdyn_connreference_msdyn_connectordatasource)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_connectordatasource`|
|ReferencingAttribute|`msdyn_connectionreferenceid`|
|ReferencedEntityNavigationPropertyName|`msdyn_connreference_msdyn_connectordatasource`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_dfcr_cr_connect"></a> msdyn_dfcr_cr_connect

Many-To-One Relationship: [msdyn_dataflowconnectionreference msdyn_dfcr_cr_connect](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dfcr_cr_connect)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowconnectionreference`|
|ReferencingAttribute|`msdyn_connectionreference`|
|ReferencedEntityNavigationPropertyName|`msdyn_msdyn_dataflowconnectionreference_Connect`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_botcomponent_connectionreference"></a> botcomponent_connectionreference

See [botcomponent botcomponent_connectionreference Many-To-Many Relationship](botcomponent.md#BKMK_botcomponent_connectionreference)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_connectionreference`|
|IsCustomizable|False|
|SchemaName|`botcomponent_connectionreference`|
|IntersectAttribute|`connectionreferenceid`|
|NavigationPropertyName|`botcomponent_connectionreference`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.connectionreference?displayProperty=fullName>
