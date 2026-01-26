---
title: "msdyn_historicalcaseharvestrun table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the msdyn_historicalcaseharvestrun table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# msdyn_historicalcaseharvestrun table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the msdyn_historicalcaseharvestrun table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestruns(*msdyn_historicalcaseharvestrunid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_historicalcaseharvestruns<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_historicalcaseharvestruns(*msdyn_historicalcaseharvestrunid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_historicalcaseharvestruns(*msdyn_historicalcaseharvestrunid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_historicalcaseharvestruns<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestruns(*msdyn_historicalcaseharvestrunid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestruns(*msdyn_historicalcaseharvestrunid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_historicalcaseharvestruns(*msdyn_historicalcaseharvestrunid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the msdyn_historicalcaseharvestrun table.

|Property|Value|
| --- | --- |
| **DisplayName** | **msdyn_historicalcaseharvestrun** |
| **DisplayCollectionName** | **msdyn_historicalcaseharvestruns** |
| **SchemaName** | `msdyn_historicalcaseharvestrun` |
| **CollectionSchemaName** | `msdyn_historicalcaseharvestruns` |
| **EntitySetName** | `msdyn_historicalcaseharvestruns`|
| **LogicalName** | `msdyn_historicalcaseharvestrun` |
| **LogicalCollectionName** | `msdyn_historicalcaseharvestruns` |
| **PrimaryIdAttribute** | `msdyn_historicalcaseharvestrunid` |
| **PrimaryNameAttribute** |`msdyn_paginationmarker` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_additionaldetails](#BKMK_msdyn_additionaldetails)
- [msdyn_caseidentificationcompletedon](#BKMK_msdyn_caseidentificationcompletedon)
- [msdyn_conditions](#BKMK_msdyn_conditions)
- [msdyn_fieldmapping](#BKMK_msdyn_fieldmapping)
- [msdyn_harvestingdatatype](#BKMK_msdyn_harvestingdatatype)
- [msdyn_harvestsourceentity](#BKMK_msdyn_harvestsourceentity)
- [msdyn_historicalcaseharvestrunId](#BKMK_msdyn_historicalcaseharvestrunId)
- [msdyn_pageIndex](#BKMK_msdyn_pageIndex)
- [msdyn_paginationmarker](#BKMK_msdyn_paginationmarker)
- [msdyn_totalarticlescreated](#BKMK_msdyn_totalarticlescreated)
- [msdyn_totalcasesdiscovered](#BKMK_msdyn_totalcasesdiscovered)
- [msdyn_totalcasesprocessed](#BKMK_msdyn_totalcasesprocessed)
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

### <a name="BKMK_msdyn_additionaldetails"></a> msdyn_additionaldetails

|Property|Value|
|---|---|
|Description||
|DisplayName|**Additional details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_additionaldetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_caseidentificationcompletedon"></a> msdyn_caseidentificationcompletedon

|Property|Value|
|---|---|
|Description|**Timestamp when all cases were identified for the run.**|
|DisplayName|**Case Identification Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_caseidentificationcompletedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_conditions"></a> msdyn_conditions

|Property|Value|
|---|---|
|Description||
|DisplayName|**Conditions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_conditions`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_fieldmapping"></a> msdyn_fieldmapping

|Property|Value|
|---|---|
|Description||
|DisplayName|**Field Mapping**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_fieldmapping`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_harvestingdatatype"></a> msdyn_harvestingdatatype

|Property|Value|
|---|---|
|Description|**Indicates what type of entity this harvest run is happening for**|
|DisplayName|**harvestingdatatype**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvestingdatatype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_historicalcaseharvestrun_msdyn_harvestingdatatype`|

#### msdyn_harvestingdatatype Choices/Options

|Value|Label|
|---|---|
|0|**Case**|
|1|**Conversation**|
|2|**Custom Entity**|

### <a name="BKMK_msdyn_harvestsourceentity"></a> msdyn_harvestsourceentity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Knowledge Harvest Source Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvestsourceentity`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_historicalcaseharvestrunId"></a> msdyn_historicalcaseharvestrunId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Historical Case Harvest Run ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_historicalcaseharvestrunid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_pageIndex"></a> msdyn_pageIndex

|Property|Value|
|---|---|
|Description||
|DisplayName|**Page Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_pageIndex`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_paginationmarker"></a> msdyn_paginationmarker

|Property|Value|
|---|---|
|Description||
|DisplayName|**Pagination Marker**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_paginationmarker`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_totalarticlescreated"></a> msdyn_totalarticlescreated

|Property|Value|
|---|---|
|Description||
|DisplayName|**Total Articles Created**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_totalarticlescreated`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_totalcasesdiscovered"></a> msdyn_totalcasesdiscovered

|Property|Value|
|---|---|
|Description||
|DisplayName|**Total Cases Discovered**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_totalcasesdiscovered`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_totalcasesprocessed"></a> msdyn_totalcasesprocessed

|Property|Value|
|---|---|
|Description||
|DisplayName|**Total Cases Processed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_totalcasesprocessed`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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
|Description|**Status of the historical case harvest runs**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_historicalcaseharvestrun_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **InProgress**<br />DefaultStatus: 1<br />InvariantName: `InProgress`|
|1|Label: **Completed**<br />DefaultStatus: 4<br />InvariantName: `Completed`|
|2|Label: **Failed**<br />DefaultStatus: 5<br />InvariantName: `Failed`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the historical case harvest run**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_historicalcaseharvestrun_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Ready**<br />State:0<br />TransitionData: None|
|2|Label: **CaseIndentificationInProgress**<br />State:0<br />TransitionData: None|
|3|Label: **CaseIdentificationCompleted**<br />State:0<br />TransitionData: None|
|4|Label: **Completed**<br />State:1<br />TransitionData: None|
|5|Label: **CaseIdentificationFailed**<br />State:2<br />TransitionData: None|
|6|Label: **CTandEACcheckFailed**<br />State:2<br />TransitionData: None|

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
|RequiredLevel|SystemRequired|
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

- [business_unit_msdyn_historicalcaseharvestrun](#BKMK_business_unit_msdyn_historicalcaseharvestrun)
- [lk_msdyn_historicalcaseharvestrun_createdby](#BKMK_lk_msdyn_historicalcaseharvestrun_createdby)
- [lk_msdyn_historicalcaseharvestrun_createdonbehalfby](#BKMK_lk_msdyn_historicalcaseharvestrun_createdonbehalfby)
- [lk_msdyn_historicalcaseharvestrun_modifiedby](#BKMK_lk_msdyn_historicalcaseharvestrun_modifiedby)
- [lk_msdyn_historicalcaseharvestrun_modifiedonbehalfby](#BKMK_lk_msdyn_historicalcaseharvestrun_modifiedonbehalfby)
- [owner_msdyn_historicalcaseharvestrun](#BKMK_owner_msdyn_historicalcaseharvestrun)
- [team_msdyn_historicalcaseharvestrun](#BKMK_team_msdyn_historicalcaseharvestrun)
- [user_msdyn_historicalcaseharvestrun](#BKMK_user_msdyn_historicalcaseharvestrun)

### <a name="BKMK_business_unit_msdyn_historicalcaseharvestrun"></a> business_unit_msdyn_historicalcaseharvestrun

One-To-Many Relationship: [businessunit business_unit_msdyn_historicalcaseharvestrun](businessunit.md#BKMK_business_unit_msdyn_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrun_createdby"></a> lk_msdyn_historicalcaseharvestrun_createdby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrun_createdby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrun_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrun_createdonbehalfby"></a> lk_msdyn_historicalcaseharvestrun_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrun_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrun_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrun_modifiedby"></a> lk_msdyn_historicalcaseharvestrun_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrun_modifiedby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrun_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrun_modifiedonbehalfby"></a> lk_msdyn_historicalcaseharvestrun_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrun_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrun_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_historicalcaseharvestrun"></a> owner_msdyn_historicalcaseharvestrun

One-To-Many Relationship: [owner owner_msdyn_historicalcaseharvestrun](owner.md#BKMK_owner_msdyn_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_historicalcaseharvestrun"></a> team_msdyn_historicalcaseharvestrun

One-To-Many Relationship: [team team_msdyn_historicalcaseharvestrun](team.md#BKMK_team_msdyn_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_historicalcaseharvestrun"></a> user_msdyn_historicalcaseharvestrun

One-To-Many Relationship: [systemuser user_msdyn_historicalcaseharvestrun](systemuser.md#BKMK_user_msdyn_historicalcaseharvestrun)

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

- [msdyn_historicalcaseharvestbatch_historicalcaseharvestrun](#BKMK_msdyn_historicalcaseharvestbatch_historicalcaseharvestrun)
- [msdyn_historicalcaseharvestrun_AsyncOperations](#BKMK_msdyn_historicalcaseharvestrun_AsyncOperations)
- [msdyn_historicalcaseharvestrun_BulkDeleteFailures](#BKMK_msdyn_historicalcaseharvestrun_BulkDeleteFailures)
- [msdyn_historicalcaseharvestrun_MailboxTrackingFolders](#BKMK_msdyn_historicalcaseharvestrun_MailboxTrackingFolders)
- [msdyn_historicalcaseharvestrun_PrincipalObjectAttributeAccesses](#BKMK_msdyn_historicalcaseharvestrun_PrincipalObjectAttributeAccesses)
- [msdyn_historicalcaseharvestrun_ProcessSession](#BKMK_msdyn_historicalcaseharvestrun_ProcessSession)
- [msdyn_historicalcaseharvestrun_SyncErrors](#BKMK_msdyn_historicalcaseharvestrun_SyncErrors)

### <a name="BKMK_msdyn_historicalcaseharvestbatch_historicalcaseharvestrun"></a> msdyn_historicalcaseharvestbatch_historicalcaseharvestrun

Many-To-One Relationship: [msdyn_historicalcaseharvestbatch msdyn_historicalcaseharvestbatch_historicalcaseharvestrun](msdyn_historicalcaseharvestbatch.md#BKMK_msdyn_historicalcaseharvestbatch_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_historicalcaseharvestbatch`|
|ReferencingAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestbatch_historicalcaseharvestrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_AsyncOperations"></a> msdyn_historicalcaseharvestrun_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_historicalcaseharvestrun_AsyncOperations](asyncoperation.md#BKMK_msdyn_historicalcaseharvestrun_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrun_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_BulkDeleteFailures"></a> msdyn_historicalcaseharvestrun_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_historicalcaseharvestrun_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_historicalcaseharvestrun_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrun_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_MailboxTrackingFolders"></a> msdyn_historicalcaseharvestrun_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_historicalcaseharvestrun_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_historicalcaseharvestrun_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrun_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_PrincipalObjectAttributeAccesses"></a> msdyn_historicalcaseharvestrun_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_historicalcaseharvestrun_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_historicalcaseharvestrun_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrun_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_ProcessSession"></a> msdyn_historicalcaseharvestrun_ProcessSession

Many-To-One Relationship: [processsession msdyn_historicalcaseharvestrun_ProcessSession](processsession.md#BKMK_msdyn_historicalcaseharvestrun_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrun_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_SyncErrors"></a> msdyn_historicalcaseharvestrun_SyncErrors

Many-To-One Relationship: [syncerror msdyn_historicalcaseharvestrun_SyncErrors](syncerror.md#BKMK_msdyn_historicalcaseharvestrun_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrun_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_historicalcaseharvestrun?displayProperty=fullName>
