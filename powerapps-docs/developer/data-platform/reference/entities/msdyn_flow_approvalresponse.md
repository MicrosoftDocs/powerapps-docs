---
title: "Approval Response (msdyn_flow_approvalresponse) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Approval Response (msdyn_flow_approvalresponse) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Approval Response (msdyn_flow_approvalresponse) table/entity reference (Microsoft Dataverse)

An individual response to an approval.

## Messages

The following table lists the messages for the Approval Response (msdyn_flow_approvalresponse) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_flow_approvalresponses(*msdyn_flow_approvalresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_flow_approvalresponses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_flow_approvalresponses(*msdyn_flow_approvalresponseid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_flow_approvalresponses(*msdyn_flow_approvalresponseid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_flow_approvalresponses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_flow_approvalresponses(*msdyn_flow_approvalresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_flow_approvalresponses(*msdyn_flow_approvalresponseid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_flow_approvalresponses(*msdyn_flow_approvalresponseid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Approval Response (msdyn_flow_approvalresponse) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Approval Response** |
| **DisplayCollectionName** | **Approval Responses** |
| **SchemaName** | `msdyn_flow_approvalresponse` |
| **CollectionSchemaName** | `msdyn_flow_approvalresponses` |
| **EntitySetName** | `msdyn_flow_approvalresponses`|
| **LogicalName** | `msdyn_flow_approvalresponse` |
| **LogicalCollectionName** | `msdyn_flow_approvalresponses` |
| **PrimaryIdAttribute** | `msdyn_flow_approvalresponseid` |
| **PrimaryNameAttribute** |`msdyn_flow_approvalresponse_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_flow_approvalresponse_additionalfields](#BKMK_msdyn_flow_approvalresponse_additionalfields)
- [msdyn_flow_approvalresponse_approval](#BKMK_msdyn_flow_approvalresponse_approval)
- [msdyn_flow_approvalresponse_approvalstagekey](#BKMK_msdyn_flow_approvalresponse_approvalstagekey)
- [msdyn_flow_approvalresponse_comments](#BKMK_msdyn_flow_approvalresponse_comments)
- [msdyn_flow_approvalresponse_name](#BKMK_msdyn_flow_approvalresponse_name)
- [msdyn_flow_approvalresponse_response](#BKMK_msdyn_flow_approvalresponse_response)
- [msdyn_flow_approvalresponse_stage](#BKMK_msdyn_flow_approvalresponse_stage)
- [msdyn_flow_approvalresponse_stepnumber](#BKMK_msdyn_flow_approvalresponse_stepnumber)
- [msdyn_flow_approvalresponseId](#BKMK_msdyn_flow_approvalresponseId)
- [msdyn_flow_approvalresponseidx_approvalid](#BKMK_msdyn_flow_approvalresponseidx_approvalid)
- [msdyn_flow_approvalresponseidx_owninguserid](#BKMK_msdyn_flow_approvalresponseidx_owninguserid)
- [msdyn_flow_approvalresponseidx_stage](#BKMK_msdyn_flow_approvalresponseidx_stage)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [StageNumber](#BKMK_StageNumber)
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

### <a name="BKMK_msdyn_flow_approvalresponse_additionalfields"></a> msdyn_flow_approvalresponse_additionalfields

|Property|Value|
|---|---|
|Description||
|DisplayName|**Additional Fields**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_additionalfields`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_flow_approvalresponse_approval"></a> msdyn_flow_approvalresponse_approval

|Property|Value|
|---|---|
|Description|**The linked approval.**|
|DisplayName|**Approval**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_approval`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msdyn_flow_approval|

### <a name="BKMK_msdyn_flow_approvalresponse_approvalstagekey"></a> msdyn_flow_approvalresponse_approvalstagekey

|Property|Value|
|---|---|
|Description|**Lookup key to match approval id and stage in fetch xml.**|
|DisplayName|**Approval Stage Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_approvalstagekey`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalresponse_comments"></a> msdyn_flow_approvalresponse_comments

|Property|Value|
|---|---|
|Description|**The owner's comments.**|
|DisplayName|**Comments**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_comments`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_flow_approvalresponse_name"></a> msdyn_flow_approvalresponse_name

|Property|Value|
|---|---|
|Description|**The name of the approval response.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalresponse_response"></a> msdyn_flow_approvalresponse_response

|Property|Value|
|---|---|
|Description|**The owner's response.**|
|DisplayName|**Response**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_response`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalresponse_stage"></a> msdyn_flow_approvalresponse_stage

|Property|Value|
|---|---|
|Description|**The assigned stage of the associated approval.**|
|DisplayName|**Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_stage`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_flow_approvalstage`|

#### msdyn_flow_approvalresponse_stage Choices/Options

|Value|Label|
|---|---|
|192350000|**Not Specified**|
|192350001|**Basic**|
|192351000|**Complete**|

### <a name="BKMK_msdyn_flow_approvalresponse_stepnumber"></a> msdyn_flow_approvalresponse_stepnumber

|Property|Value|
|---|---|
|Description||
|DisplayName|**Step Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponse_stepnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_flow_approvalresponseId"></a> msdyn_flow_approvalresponseId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Approval Response**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponseid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_flow_approvalresponseidx_approvalid"></a> msdyn_flow_approvalresponseidx_approvalid

|Property|Value|
|---|---|
|Description|**Field mirroring the linked approval for the constraint index.**|
|DisplayName|**Approval Id Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponseidx_approvalid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalresponseidx_owninguserid"></a> msdyn_flow_approvalresponseidx_owninguserid

|Property|Value|
|---|---|
|Description|**Field mirroring the owning user id for the constraint index.**|
|DisplayName|**Owning User Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponseidx_owninguserid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalresponseidx_stage"></a> msdyn_flow_approvalresponseidx_stage

|Property|Value|
|---|---|
|Description|**Field mirroring the stage for the constraint index.**|
|DisplayName|**Stage Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalresponseidx_stage`|
|RequiredLevel|None|
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

### <a name="BKMK_StageNumber"></a> StageNumber

|Property|Value|
|---|---|
|Description|**The stage number to which this approval response belongs.**|
|DisplayName|**Stage Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Approval Response**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approvalresponse_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 192350000<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 192350002<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**The reason for the status of the response.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|ApplicationRequired|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approvalresponse_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|192350000|Label: **Reviewing**<br />State:0<br />TransitionData: None|
|192350001|Label: **Saved**<br />State:0<br />TransitionData: None|
|192350002|Label: **Committed**<br />State:1<br />TransitionData: None|

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

- [business_unit_msdyn_flow_approvalresponse](#BKMK_business_unit_msdyn_flow_approvalresponse)
- [lk_msdyn_flow_approvalresponse_createdby](#BKMK_lk_msdyn_flow_approvalresponse_createdby)
- [lk_msdyn_flow_approvalresponse_createdonbehalfby](#BKMK_lk_msdyn_flow_approvalresponse_createdonbehalfby)
- [lk_msdyn_flow_approvalresponse_modifiedby](#BKMK_lk_msdyn_flow_approvalresponse_modifiedby)
- [lk_msdyn_flow_approvalresponse_modifiedonbehalfby](#BKMK_lk_msdyn_flow_approvalresponse_modifiedonbehalfby)
- [msdyn_flow_approvalrelationship_approvalresponses](#BKMK_msdyn_flow_approvalrelationship_approvalresponses)
- [owner_msdyn_flow_approvalresponse](#BKMK_owner_msdyn_flow_approvalresponse)
- [team_msdyn_flow_approvalresponse](#BKMK_team_msdyn_flow_approvalresponse)
- [user_msdyn_flow_approvalresponse](#BKMK_user_msdyn_flow_approvalresponse)

### <a name="BKMK_business_unit_msdyn_flow_approvalresponse"></a> business_unit_msdyn_flow_approvalresponse

One-To-Many Relationship: [businessunit business_unit_msdyn_flow_approvalresponse](businessunit.md#BKMK_business_unit_msdyn_flow_approvalresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalresponse_createdby"></a> lk_msdyn_flow_approvalresponse_createdby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalresponse_createdby](systemuser.md#BKMK_lk_msdyn_flow_approvalresponse_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalresponse_createdonbehalfby"></a> lk_msdyn_flow_approvalresponse_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalresponse_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approvalresponse_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalresponse_modifiedby"></a> lk_msdyn_flow_approvalresponse_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalresponse_modifiedby](systemuser.md#BKMK_lk_msdyn_flow_approvalresponse_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalresponse_modifiedonbehalfby"></a> lk_msdyn_flow_approvalresponse_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalresponse_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approvalresponse_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrelationship_approvalresponses"></a> msdyn_flow_approvalrelationship_approvalresponses

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approvalrelationship_approvalresponses](msdyn_flow_approval.md#BKMK_msdyn_flow_approvalrelationship_approvalresponses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`msdyn_flow_approvalresponse_approval`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalresponse_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_flow_approvalresponse"></a> owner_msdyn_flow_approvalresponse

One-To-Many Relationship: [owner owner_msdyn_flow_approvalresponse](owner.md#BKMK_owner_msdyn_flow_approvalresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_flow_approvalresponse"></a> team_msdyn_flow_approvalresponse

One-To-Many Relationship: [team team_msdyn_flow_approvalresponse](team.md#BKMK_team_msdyn_flow_approvalresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_flow_approvalresponse"></a> user_msdyn_flow_approvalresponse

One-To-Many Relationship: [systemuser user_msdyn_flow_approvalresponse](systemuser.md#BKMK_user_msdyn_flow_approvalresponse)

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

- [msdyn_flow_approvalresponse_AsyncOperations](#BKMK_msdyn_flow_approvalresponse_AsyncOperations)
- [msdyn_flow_approvalresponse_BulkDeleteFailures](#BKMK_msdyn_flow_approvalresponse_BulkDeleteFailures)
- [msdyn_flow_approvalresponse_DuplicateBaseRecord](#BKMK_msdyn_flow_approvalresponse_DuplicateBaseRecord)
- [msdyn_flow_approvalresponse_DuplicateMatchingRecord](#BKMK_msdyn_flow_approvalresponse_DuplicateMatchingRecord)
- [msdyn_flow_approvalresponse_MailboxTrackingFolders](#BKMK_msdyn_flow_approvalresponse_MailboxTrackingFolders)
- [msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approvalresponse_ProcessSession](#BKMK_msdyn_flow_approvalresponse_ProcessSession)
- [msdyn_flow_approvalresponse_SyncErrors](#BKMK_msdyn_flow_approvalresponse_SyncErrors)

### <a name="BKMK_msdyn_flow_approvalresponse_AsyncOperations"></a> msdyn_flow_approvalresponse_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_flow_approvalresponse_AsyncOperations](asyncoperation.md#BKMK_msdyn_flow_approvalresponse_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalresponse_BulkDeleteFailures"></a> msdyn_flow_approvalresponse_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_flow_approvalresponse_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_flow_approvalresponse_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalresponse_DuplicateBaseRecord"></a> msdyn_flow_approvalresponse_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approvalresponse_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_flow_approvalresponse_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalresponse_DuplicateMatchingRecord"></a> msdyn_flow_approvalresponse_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approvalresponse_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_flow_approvalresponse_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalresponse_MailboxTrackingFolders"></a> msdyn_flow_approvalresponse_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_flow_approvalresponse_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_flow_approvalresponse_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalresponse_ProcessSession"></a> msdyn_flow_approvalresponse_ProcessSession

Many-To-One Relationship: [processsession msdyn_flow_approvalresponse_ProcessSession](processsession.md#BKMK_msdyn_flow_approvalresponse_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalresponse_SyncErrors"></a> msdyn_flow_approvalresponse_SyncErrors

Many-To-One Relationship: [syncerror msdyn_flow_approvalresponse_SyncErrors](syncerror.md#BKMK_msdyn_flow_approvalresponse_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalresponse_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_flow_approvalresponse?displayProperty=fullName>
