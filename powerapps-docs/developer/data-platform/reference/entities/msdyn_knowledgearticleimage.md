---
title: "Knowledge Article Image (msdyn_knowledgearticleimage) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Knowledge Article Image (msdyn_knowledgearticleimage) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Knowledge Article Image (msdyn_knowledgearticleimage) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Knowledge Article Image (msdyn_knowledgearticleimage) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_knowledgearticleimages(*msdyn_knowledgearticleimageid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_knowledgearticleimages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_knowledgearticleimages(*msdyn_knowledgearticleimageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_knowledgearticleimages(*msdyn_knowledgearticleimageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_knowledgearticleimages<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_knowledgearticleimages(*msdyn_knowledgearticleimageid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_knowledgearticleimages(*msdyn_knowledgearticleimageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_knowledgearticleimages(*msdyn_knowledgearticleimageid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Knowledge Article Image (msdyn_knowledgearticleimage) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Knowledge Article Image** |
| **DisplayCollectionName** | **Knowledge Article Images** |
| **SchemaName** | `msdyn_knowledgearticleimage` |
| **CollectionSchemaName** | `msdyn_knowledgearticleimages` |
| **EntitySetName** | `msdyn_knowledgearticleimages`|
| **LogicalName** | `msdyn_knowledgearticleimage` |
| **LogicalCollectionName** | `msdyn_knowledgearticleimages` |
| **PrimaryIdAttribute** | `msdyn_knowledgearticleimageid` |
| **PrimaryNameAttribute** |`msdyn_filename` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_FileName](#BKMK_msdyn_FileName)
- [msdyn_knowledgearticleimageId](#BKMK_msdyn_knowledgearticleimageId)
- [msdyn_ParentEntityRecordID](#BKMK_msdyn_ParentEntityRecordID)
- [msdyn_ParentKnowledgeArticleID](#BKMK_msdyn_ParentKnowledgeArticleID)
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

### <a name="BKMK_msdyn_FileName"></a> msdyn_FileName

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**FileName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_filename`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_knowledgearticleimageId"></a> msdyn_knowledgearticleimageId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**KnowledgeArticleImage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_knowledgearticleimageid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_ParentEntityRecordID"></a> msdyn_ParentEntityRecordID

|Property|Value|
|---|---|
|Description|**Parent entity record ID**|
|DisplayName|**msdyn\_ParentEntityRecordID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parententityrecordid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_msdyn_ParentKnowledgeArticleID"></a> msdyn_ParentKnowledgeArticleID

|Property|Value|
|---|---|
|Description|**Parent Knowledge Article ID**|
|DisplayName|**ParentKnowledgeArticleID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parentknowledgearticleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|knowledgearticle|

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
|Description|**Status of the KnowledgeArticleImage**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_knowledgearticleimage_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the KnowledgeArticleImage**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_knowledgearticleimage_statuscode`|

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
- [msdyn_BlobFile](#BKMK_msdyn_BlobFile)
- [msdyn_BlobFile_Name](#BKMK_msdyn_BlobFile_Name)
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

### <a name="BKMK_msdyn_BlobFile"></a> msdyn_BlobFile

|Property|Value|
|---|---|
|Description|**Blob Image Attribute**|
|DisplayName|**BlobFile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_blobfile`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_BlobFile_Name"></a> msdyn_BlobFile_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_blobfile_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

- [business_unit_msdyn_knowledgearticleimage](#BKMK_business_unit_msdyn_knowledgearticleimage)
- [FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile](#BKMK_FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile)
- [lk_msdyn_knowledgearticleimage_createdby](#BKMK_lk_msdyn_knowledgearticleimage_createdby)
- [lk_msdyn_knowledgearticleimage_createdonbehalfby](#BKMK_lk_msdyn_knowledgearticleimage_createdonbehalfby)
- [lk_msdyn_knowledgearticleimage_modifiedby](#BKMK_lk_msdyn_knowledgearticleimage_modifiedby)
- [lk_msdyn_knowledgearticleimage_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgearticleimage_modifiedonbehalfby)
- [msdyn_knowledgearticleimage_parentknowledgearticleid](#BKMK_msdyn_knowledgearticleimage_parentknowledgearticleid)
- [owner_msdyn_knowledgearticleimage](#BKMK_owner_msdyn_knowledgearticleimage)
- [team_msdyn_knowledgearticleimage](#BKMK_team_msdyn_knowledgearticleimage)
- [user_msdyn_knowledgearticleimage](#BKMK_user_msdyn_knowledgearticleimage)

### <a name="BKMK_business_unit_msdyn_knowledgearticleimage"></a> business_unit_msdyn_knowledgearticleimage

One-To-Many Relationship: [businessunit business_unit_msdyn_knowledgearticleimage](businessunit.md#BKMK_business_unit_msdyn_knowledgearticleimage)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile"></a> FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile](fileattachment.md#BKMK_FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_blobfile`|
|ReferencingEntityNavigationPropertyName|`msdyn_blobfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticleimage_createdby"></a> lk_msdyn_knowledgearticleimage_createdby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticleimage_createdby](systemuser.md#BKMK_lk_msdyn_knowledgearticleimage_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticleimage_createdonbehalfby"></a> lk_msdyn_knowledgearticleimage_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticleimage_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgearticleimage_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticleimage_modifiedby"></a> lk_msdyn_knowledgearticleimage_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticleimage_modifiedby](systemuser.md#BKMK_lk_msdyn_knowledgearticleimage_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticleimage_modifiedonbehalfby"></a> lk_msdyn_knowledgearticleimage_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticleimage_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgearticleimage_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_parentknowledgearticleid"></a> msdyn_knowledgearticleimage_parentknowledgearticleid

One-To-Many Relationship: [knowledgearticle msdyn_knowledgearticleimage_parentknowledgearticleid](knowledgearticle.md#BKMK_msdyn_knowledgearticleimage_parentknowledgearticleid)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`msdyn_parentknowledgearticleid`|
|ReferencingEntityNavigationPropertyName|`msdyn_parentknowledgearticleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_knowledgearticleimage"></a> owner_msdyn_knowledgearticleimage

One-To-Many Relationship: [owner owner_msdyn_knowledgearticleimage](owner.md#BKMK_owner_msdyn_knowledgearticleimage)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_knowledgearticleimage"></a> team_msdyn_knowledgearticleimage

One-To-Many Relationship: [team team_msdyn_knowledgearticleimage](team.md#BKMK_team_msdyn_knowledgearticleimage)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_knowledgearticleimage"></a> user_msdyn_knowledgearticleimage

One-To-Many Relationship: [systemuser user_msdyn_knowledgearticleimage](systemuser.md#BKMK_user_msdyn_knowledgearticleimage)

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

- [msdyn_knowledgearticleimage_AsyncOperations](#BKMK_msdyn_knowledgearticleimage_AsyncOperations)
- [msdyn_knowledgearticleimage_BulkDeleteFailures](#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures)
- [msdyn_knowledgearticleimage_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord)
- [msdyn_knowledgearticleimage_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord)
- [msdyn_knowledgearticleimage_FileAttachments](#BKMK_msdyn_knowledgearticleimage_FileAttachments)
- [msdyn_knowledgearticleimage_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders)
- [msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticleimage_ProcessSession](#BKMK_msdyn_knowledgearticleimage_ProcessSession)
- [msdyn_knowledgearticleimage_SyncErrors](#BKMK_msdyn_knowledgearticleimage_SyncErrors)

### <a name="BKMK_msdyn_knowledgearticleimage_AsyncOperations"></a> msdyn_knowledgearticleimage_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_knowledgearticleimage_AsyncOperations](asyncoperation.md#BKMK_msdyn_knowledgearticleimage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures"></a> msdyn_knowledgearticleimage_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_knowledgearticleimage_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord"></a> msdyn_knowledgearticleimage_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_knowledgearticleimage_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord"></a> msdyn_knowledgearticleimage_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_knowledgearticleimage_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_FileAttachments"></a> msdyn_knowledgearticleimage_FileAttachments

Many-To-One Relationship: [fileattachment msdyn_knowledgearticleimage_FileAttachments](fileattachment.md#BKMK_msdyn_knowledgearticleimage_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders"></a> msdyn_knowledgearticleimage_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_knowledgearticleimage_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_ProcessSession"></a> msdyn_knowledgearticleimage_ProcessSession

Many-To-One Relationship: [processsession msdyn_knowledgearticleimage_ProcessSession](processsession.md#BKMK_msdyn_knowledgearticleimage_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_SyncErrors"></a> msdyn_knowledgearticleimage_SyncErrors

Many-To-One Relationship: [syncerror msdyn_knowledgearticleimage_SyncErrors](syncerror.md#BKMK_msdyn_knowledgearticleimage_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_knowledgearticleimage?displayProperty=fullName>
