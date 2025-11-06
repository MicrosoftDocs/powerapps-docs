---
title: "Interim Update Knowledge Article (msdyn_interimupdateknowledgearticle) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Interim Update Knowledge Article (msdyn_interimupdateknowledgearticle) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Interim Update Knowledge Article (msdyn_interimupdateknowledgearticle) table/entity reference (Microsoft Dataverse)

Interim table to facilitate the update of knowledge articles from knowledge harvesting.

## Messages

The following table lists the messages for the Interim Update Knowledge Article (msdyn_interimupdateknowledgearticle) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_interimupdateknowledgearticles(*msdyn_interimupdateknowledgearticleid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_interimupdateknowledgearticles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_interimupdateknowledgearticles(*msdyn_interimupdateknowledgearticleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_interimupdateknowledgearticles(*msdyn_interimupdateknowledgearticleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_interimupdateknowledgearticles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_interimupdateknowledgearticles(*msdyn_interimupdateknowledgearticleid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_interimupdateknowledgearticles(*msdyn_interimupdateknowledgearticleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_interimupdateknowledgearticles(*msdyn_interimupdateknowledgearticleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Interim Update Knowledge Article (msdyn_interimupdateknowledgearticle) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Interim Update Knowledge Article** |
| **DisplayCollectionName** | **Interim Update Knowledge Articles** |
| **SchemaName** | `msdyn_interimupdateknowledgearticle` |
| **CollectionSchemaName** | `msdyn_interimupdateknowledgearticles` |
| **EntitySetName** | `msdyn_interimupdateknowledgearticles`|
| **LogicalName** | `msdyn_interimupdateknowledgearticle` |
| **LogicalCollectionName** | `msdyn_interimupdateknowledgearticles` |
| **PrimaryIdAttribute** | `msdyn_interimupdateknowledgearticleid` |
| **PrimaryNameAttribute** |`msdyn_title` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_compliancestatecode](#BKMK_msdyn_compliancestatecode)
- [msdyn_content](#BKMK_msdyn_content)
- [msdyn_creationmode](#BKMK_msdyn_creationmode)
- [msdyn_interimupdateknowledgearticleId](#BKMK_msdyn_interimupdateknowledgearticleId)
- [msdyn_relatedrecord](#BKMK_msdyn_relatedrecord)
- [msdyn_sourceofcreation](#BKMK_msdyn_sourceofcreation)
- [msdyn_statecode](#BKMK_msdyn_statecode)
- [msdyn_statuscode](#BKMK_msdyn_statuscode)
- [msdyn_targetknowledgearticleid](#BKMK_msdyn_targetknowledgearticleid)
- [msdyn_title](#BKMK_msdyn_title)
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

### <a name="BKMK_msdyn_compliancestatecode"></a> msdyn_compliancestatecode

|Property|Value|
|---|---|
|Description|**field to indicate the compliance state of an article**|
|DisplayName|**Compliance State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_compliancestatecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_content"></a> msdyn_content

|Property|Value|
|---|---|
|Description|**Shows the body of the article stored in HTML format.**|
|DisplayName|**Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_content`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_creationmode"></a> msdyn_creationmode

|Property|Value|
|---|---|
|Description|**Opiton set to hold details about article if it is generated by AI or manually created**|
|DisplayName|**Creation Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_creationmode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_interimupdateknowledgearticleId"></a> msdyn_interimupdateknowledgearticleId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Interim Update Knowledge Article**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_interimupdateknowledgearticleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_relatedrecord"></a> msdyn_relatedrecord

|Property|Value|
|---|---|
|Description|**Json list of records related to the knowledge article update.**|
|DisplayName|**Related Record**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_relatedrecord`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_sourceofcreation"></a> msdyn_sourceofcreation

|Property|Value|
|---|---|
|Description|**Option set to hold details about article origin, if it is generated from Real Time Harvesting/ Bulk Harvesting/ knowledge draft assist/ Manual**|
|DisplayName|**Source of Creation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sourceofcreation`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_statecode"></a> msdyn_statecode

|Property|Value|
|---|---|
|Description|**Shows whether the article is a draft or is published, archived, or discarded. Draft articles aren't available externally and can be edited. Published articles are available externally, based on applicable permissions, but can't be edited. All metadata changes are reflected in the published version. Archived and discarded articles aren't available externally and can't be edited.**|
|DisplayName|**Knowledge Article Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_statecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_statuscode"></a> msdyn_statuscode

|Property|Value|
|---|---|
|Description|**Select the article's status.**|
|DisplayName|**Knowledge Article Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_statuscode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_targetknowledgearticleid"></a> msdyn_targetknowledgearticleid

|Property|Value|
|---|---|
|Description|**Knowledge article to create a new version of with provided data.**|
|DisplayName|**Target Knowledge Article**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_targetknowledgearticleid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|knowledgearticle|

### <a name="BKMK_msdyn_title"></a> msdyn_title

|Property|Value|
|---|---|
|Description|**Type a title for the article.**|
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_title`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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
|Description|**Status of the Interim Update Knowledge Article**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_interimupdateknowledgearticle_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Interim Update Knowledge Article**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_interimupdateknowledgearticle_statuscode`|

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

- [business_unit_msdyn_interimupdateknowledgearticle](#BKMK_business_unit_msdyn_interimupdateknowledgearticle)
- [lk_msdyn_interimupdateknowledgearticle_createdby](#BKMK_lk_msdyn_interimupdateknowledgearticle_createdby)
- [lk_msdyn_interimupdateknowledgearticle_createdonbehalfby](#BKMK_lk_msdyn_interimupdateknowledgearticle_createdonbehalfby)
- [lk_msdyn_interimupdateknowledgearticle_modifiedby](#BKMK_lk_msdyn_interimupdateknowledgearticle_modifiedby)
- [lk_msdyn_interimupdateknowledgearticle_modifiedonbehalfby](#BKMK_lk_msdyn_interimupdateknowledgearticle_modifiedonbehalfby)
- [msdyn_interimupdateknowledgearticle_knowledgearticle](#BKMK_msdyn_interimupdateknowledgearticle_knowledgearticle)
- [owner_msdyn_interimupdateknowledgearticle](#BKMK_owner_msdyn_interimupdateknowledgearticle)
- [team_msdyn_interimupdateknowledgearticle](#BKMK_team_msdyn_interimupdateknowledgearticle)
- [user_msdyn_interimupdateknowledgearticle](#BKMK_user_msdyn_interimupdateknowledgearticle)

### <a name="BKMK_business_unit_msdyn_interimupdateknowledgearticle"></a> business_unit_msdyn_interimupdateknowledgearticle

One-To-Many Relationship: [businessunit business_unit_msdyn_interimupdateknowledgearticle](businessunit.md#BKMK_business_unit_msdyn_interimupdateknowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_interimupdateknowledgearticle_createdby"></a> lk_msdyn_interimupdateknowledgearticle_createdby

One-To-Many Relationship: [systemuser lk_msdyn_interimupdateknowledgearticle_createdby](systemuser.md#BKMK_lk_msdyn_interimupdateknowledgearticle_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_interimupdateknowledgearticle_createdonbehalfby"></a> lk_msdyn_interimupdateknowledgearticle_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_interimupdateknowledgearticle_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_interimupdateknowledgearticle_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_interimupdateknowledgearticle_modifiedby"></a> lk_msdyn_interimupdateknowledgearticle_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_interimupdateknowledgearticle_modifiedby](systemuser.md#BKMK_lk_msdyn_interimupdateknowledgearticle_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_interimupdateknowledgearticle_modifiedonbehalfby"></a> lk_msdyn_interimupdateknowledgearticle_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_interimupdateknowledgearticle_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_interimupdateknowledgearticle_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_interimupdateknowledgearticle_knowledgearticle"></a> msdyn_interimupdateknowledgearticle_knowledgearticle

One-To-Many Relationship: [knowledgearticle msdyn_interimupdateknowledgearticle_knowledgearticle](knowledgearticle.md#BKMK_msdyn_interimupdateknowledgearticle_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`msdyn_targetknowledgearticleid`|
|ReferencingEntityNavigationPropertyName|`msdyn_targetknowledgearticleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_interimupdateknowledgearticle"></a> owner_msdyn_interimupdateknowledgearticle

One-To-Many Relationship: [owner owner_msdyn_interimupdateknowledgearticle](owner.md#BKMK_owner_msdyn_interimupdateknowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_interimupdateknowledgearticle"></a> team_msdyn_interimupdateknowledgearticle

One-To-Many Relationship: [team team_msdyn_interimupdateknowledgearticle](team.md#BKMK_team_msdyn_interimupdateknowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_interimupdateknowledgearticle"></a> user_msdyn_interimupdateknowledgearticle

One-To-Many Relationship: [systemuser user_msdyn_interimupdateknowledgearticle](systemuser.md#BKMK_user_msdyn_interimupdateknowledgearticle)

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

- [msdyn_interimupdateknowledgearticle_AsyncOperations](#BKMK_msdyn_interimupdateknowledgearticle_AsyncOperations)
- [msdyn_interimupdateknowledgearticle_BulkDeleteFailures](#BKMK_msdyn_interimupdateknowledgearticle_BulkDeleteFailures)
- [msdyn_interimupdateknowledgearticle_MailboxTrackingFolders](#BKMK_msdyn_interimupdateknowledgearticle_MailboxTrackingFolders)
- [msdyn_interimupdateknowledgearticle_PrincipalObjectAttributeAccesses](#BKMK_msdyn_interimupdateknowledgearticle_PrincipalObjectAttributeAccesses)
- [msdyn_interimupdateknowledgearticle_ProcessSession](#BKMK_msdyn_interimupdateknowledgearticle_ProcessSession)
- [msdyn_interimupdateknowledgearticle_SyncErrors](#BKMK_msdyn_interimupdateknowledgearticle_SyncErrors)

### <a name="BKMK_msdyn_interimupdateknowledgearticle_AsyncOperations"></a> msdyn_interimupdateknowledgearticle_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_interimupdateknowledgearticle_AsyncOperations](asyncoperation.md#BKMK_msdyn_interimupdateknowledgearticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_interimupdateknowledgearticle_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_interimupdateknowledgearticle_BulkDeleteFailures"></a> msdyn_interimupdateknowledgearticle_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_interimupdateknowledgearticle_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_interimupdateknowledgearticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_interimupdateknowledgearticle_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_interimupdateknowledgearticle_MailboxTrackingFolders"></a> msdyn_interimupdateknowledgearticle_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_interimupdateknowledgearticle_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_interimupdateknowledgearticle_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_interimupdateknowledgearticle_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_interimupdateknowledgearticle_PrincipalObjectAttributeAccesses"></a> msdyn_interimupdateknowledgearticle_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_interimupdateknowledgearticle_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_interimupdateknowledgearticle_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_interimupdateknowledgearticle_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_interimupdateknowledgearticle_ProcessSession"></a> msdyn_interimupdateknowledgearticle_ProcessSession

Many-To-One Relationship: [processsession msdyn_interimupdateknowledgearticle_ProcessSession](processsession.md#BKMK_msdyn_interimupdateknowledgearticle_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_interimupdateknowledgearticle_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_interimupdateknowledgearticle_SyncErrors"></a> msdyn_interimupdateknowledgearticle_SyncErrors

Many-To-One Relationship: [syncerror msdyn_interimupdateknowledgearticle_SyncErrors](syncerror.md#BKMK_msdyn_interimupdateknowledgearticle_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_interimupdateknowledgearticle_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

