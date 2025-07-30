---
title: "Approval Step (msdyn_flow_approvalstep) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Approval Step (msdyn_flow_approvalstep) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Approval Step (msdyn_flow_approvalstep) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Approval Step (msdyn_flow_approvalstep) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_flow_approvalsteps(*msdyn_flow_approvalstepid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_flow_approvalsteps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_flow_approvalsteps(*msdyn_flow_approvalstepid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_flow_approvalsteps(*msdyn_flow_approvalstepid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_flow_approvalsteps<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_flow_approvalsteps(*msdyn_flow_approvalstepid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_flow_approvalsteps(*msdyn_flow_approvalstepid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_flow_approvalsteps(*msdyn_flow_approvalstepid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Approval Step (msdyn_flow_approvalstep) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Approval Step** |
| **DisplayCollectionName** | **Approval Step** |
| **SchemaName** | `msdyn_flow_approvalstep` |
| **CollectionSchemaName** | `msdyn_flow_approvalsteps` |
| **EntitySetName** | `msdyn_flow_approvalsteps`|
| **LogicalName** | `msdyn_flow_approvalstep` |
| **LogicalCollectionName** | `msdyn_flow_approvalsteps` |
| **PrimaryIdAttribute** | `msdyn_flow_approvalstepid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_flow_approvalstep_approval](#BKMK_msdyn_flow_approvalstep_approval)
- [msdyn_flow_approvalstep_approvalid](#BKMK_msdyn_flow_approvalstep_approvalid)
- [msdyn_flow_approvalstep_model](#BKMK_msdyn_flow_approvalstep_model)
- [msdyn_flow_approvalstep_modelIdType](#BKMK_msdyn_flow_approvalstep_modelIdType)
- [msdyn_flow_approvalstep_modeltype](#BKMK_msdyn_flow_approvalstep_modeltype)
- [msdyn_flow_approvalstep_number](#BKMK_msdyn_flow_approvalstep_number)
- [msdyn_flow_approvalstep_result](#BKMK_msdyn_flow_approvalstep_result)
- [msdyn_flow_approvalstep_stage](#BKMK_msdyn_flow_approvalstep_stage)
- [msdyn_flow_approvalstepId](#BKMK_msdyn_flow_approvalstepId)
- [msdyn_Name](#BKMK_msdyn_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_msdyn_flow_approvalstep_approval"></a> msdyn_flow_approvalstep_approval

|Property|Value|
|---|---|
|Description||
|DisplayName|**Approval**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_approval`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_flow_approval|

### <a name="BKMK_msdyn_flow_approvalstep_approvalid"></a> msdyn_flow_approvalstep_approvalid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Approval Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_approvalid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalstep_model"></a> msdyn_flow_approvalstep_model

|Property|Value|
|---|---|
|Description|**Step model Lookup**|
|DisplayName|**Step Model**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_model`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_flow_actionapprovalmodel, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel|

### <a name="BKMK_msdyn_flow_approvalstep_modelIdType"></a> msdyn_flow_approvalstep_modelIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_modelidtype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_msdyn_flow_approvalstep_modeltype"></a> msdyn_flow_approvalstep_modeltype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Model Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_modeltype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalstep_number"></a> msdyn_flow_approvalstep_number

|Property|Value|
|---|---|
|Description||
|DisplayName|**Step Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_number`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_flow_approvalstep_result"></a> msdyn_flow_approvalstep_result

|Property|Value|
|---|---|
|Description||
|DisplayName|**Result**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_result`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalstep_stage"></a> msdyn_flow_approvalstep_stage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstep_stage`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_flow_approvalstage`|

#### msdyn_flow_approvalstep_stage Choices/Options

|Value|Label|
|---|---|
|192350000|**Not Specified**|
|192350001|**Basic**|
|192351000|**Complete**|

### <a name="BKMK_msdyn_flow_approvalstepId"></a> msdyn_flow_approvalstepId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Approval Step**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalstepid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Approval Step**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approvalstep_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Approval Step**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approvalstep_statuscode`|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

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

- [business_unit_msdyn_flow_approvalstep](#BKMK_business_unit_msdyn_flow_approvalstep)
- [lk_msdyn_flow_approvalstep_createdby](#BKMK_lk_msdyn_flow_approvalstep_createdby)
- [lk_msdyn_flow_approvalstep_createdonbehalfby](#BKMK_lk_msdyn_flow_approvalstep_createdonbehalfby)
- [lk_msdyn_flow_approvalstep_modifiedby](#BKMK_lk_msdyn_flow_approvalstep_modifiedby)
- [lk_msdyn_flow_approvalstep_modifiedonbehalfby](#BKMK_lk_msdyn_flow_approvalstep_modifiedonbehalfby)
- [msdyn_flow_actionapprovalmodelrelationship_approvalsteps](#BKMK_msdyn_flow_actionapprovalmodelrelationship_approvalsteps)
- [msdyn_flow_approvalrelationship_approvalsteps](#BKMK_msdyn_flow_approvalrelationship_approvalsteps)
- [msdyn_flow_awaitallactionapprovalmodelrelationship_approvalsteps](#BKMK_msdyn_flow_awaitallactionapprovalmodelrelationship_approvalsteps)
- [msdyn_flow_awaitallapprovalmodelrelationship_approvalsteps](#BKMK_msdyn_flow_awaitallapprovalmodelrelationship_approvalsteps)
- [msdyn_flow_basicapprovalmodelrelationship_approvalsteps](#BKMK_msdyn_flow_basicapprovalmodelrelationship_approvalsteps)
- [owner_msdyn_flow_approvalstep](#BKMK_owner_msdyn_flow_approvalstep)
- [team_msdyn_flow_approvalstep](#BKMK_team_msdyn_flow_approvalstep)
- [user_msdyn_flow_approvalstep](#BKMK_user_msdyn_flow_approvalstep)

### <a name="BKMK_business_unit_msdyn_flow_approvalstep"></a> business_unit_msdyn_flow_approvalstep

One-To-Many Relationship: [businessunit business_unit_msdyn_flow_approvalstep](businessunit.md#BKMK_business_unit_msdyn_flow_approvalstep)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalstep_createdby"></a> lk_msdyn_flow_approvalstep_createdby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalstep_createdby](systemuser.md#BKMK_lk_msdyn_flow_approvalstep_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalstep_createdonbehalfby"></a> lk_msdyn_flow_approvalstep_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalstep_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approvalstep_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalstep_modifiedby"></a> lk_msdyn_flow_approvalstep_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalstep_modifiedby](systemuser.md#BKMK_lk_msdyn_flow_approvalstep_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalstep_modifiedonbehalfby"></a> lk_msdyn_flow_approvalstep_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalstep_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approvalstep_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodelrelationship_approvalsteps"></a> msdyn_flow_actionapprovalmodelrelationship_approvalsteps

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodelrelationship_approvalsteps](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodelrelationship_approvalsteps)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`msdyn_flow_approvalstep_model`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalstep_model_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrelationship_approvalsteps"></a> msdyn_flow_approvalrelationship_approvalsteps

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approvalrelationship_approvalsteps](msdyn_flow_approval.md#BKMK_msdyn_flow_approvalrelationship_approvalsteps)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`msdyn_flow_approvalstep_approval`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalstep_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodelrelationship_approvalsteps"></a> msdyn_flow_awaitallactionapprovalmodelrelationship_approvalsteps

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodelrelationship_approvalsteps](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodelrelationship_approvalsteps)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`msdyn_flow_approvalstep_model`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalstep_model_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodelrelationship_approvalsteps"></a> msdyn_flow_awaitallapprovalmodelrelationship_approvalsteps

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodelrelationship_approvalsteps](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodelrelationship_approvalsteps)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`msdyn_flow_approvalstep_model`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalstep_model_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodelrelationship_approvalsteps"></a> msdyn_flow_basicapprovalmodelrelationship_approvalsteps

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodelrelationship_approvalsteps](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodelrelationship_approvalsteps)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`msdyn_flow_approvalstep_model`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalstep_model_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_flow_approvalstep"></a> owner_msdyn_flow_approvalstep

One-To-Many Relationship: [owner owner_msdyn_flow_approvalstep](owner.md#BKMK_owner_msdyn_flow_approvalstep)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_flow_approvalstep"></a> team_msdyn_flow_approvalstep

One-To-Many Relationship: [team team_msdyn_flow_approvalstep](team.md#BKMK_team_msdyn_flow_approvalstep)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_flow_approvalstep"></a> user_msdyn_flow_approvalstep

One-To-Many Relationship: [systemuser user_msdyn_flow_approvalstep](systemuser.md#BKMK_user_msdyn_flow_approvalstep)

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

- [msdyn_flow_approvalstep_AsyncOperations](#BKMK_msdyn_flow_approvalstep_AsyncOperations)
- [msdyn_flow_approvalstep_BulkDeleteFailures](#BKMK_msdyn_flow_approvalstep_BulkDeleteFailures)
- [msdyn_flow_approvalstep_DuplicateBaseRecord](#BKMK_msdyn_flow_approvalstep_DuplicateBaseRecord)
- [msdyn_flow_approvalstep_DuplicateMatchingRecord](#BKMK_msdyn_flow_approvalstep_DuplicateMatchingRecord)
- [msdyn_flow_approvalstep_MailboxTrackingFolders](#BKMK_msdyn_flow_approvalstep_MailboxTrackingFolders)
- [msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approvalstep_ProcessSession](#BKMK_msdyn_flow_approvalstep_ProcessSession)
- [msdyn_flow_approvalstep_SyncErrors](#BKMK_msdyn_flow_approvalstep_SyncErrors)

### <a name="BKMK_msdyn_flow_approvalstep_AsyncOperations"></a> msdyn_flow_approvalstep_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_flow_approvalstep_AsyncOperations](asyncoperation.md#BKMK_msdyn_flow_approvalstep_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalstep_BulkDeleteFailures"></a> msdyn_flow_approvalstep_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_flow_approvalstep_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_flow_approvalstep_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalstep_DuplicateBaseRecord"></a> msdyn_flow_approvalstep_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approvalstep_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_flow_approvalstep_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalstep_DuplicateMatchingRecord"></a> msdyn_flow_approvalstep_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approvalstep_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_flow_approvalstep_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalstep_MailboxTrackingFolders"></a> msdyn_flow_approvalstep_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_flow_approvalstep_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_flow_approvalstep_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalstep_ProcessSession"></a> msdyn_flow_approvalstep_ProcessSession

Many-To-One Relationship: [processsession msdyn_flow_approvalstep_ProcessSession](processsession.md#BKMK_msdyn_flow_approvalstep_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalstep_SyncErrors"></a> msdyn_flow_approvalstep_SyncErrors

Many-To-One Relationship: [syncerror msdyn_flow_approvalstep_SyncErrors](syncerror.md#BKMK_msdyn_flow_approvalstep_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalstep_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_flow_approvalstep?displayProperty=fullName>
