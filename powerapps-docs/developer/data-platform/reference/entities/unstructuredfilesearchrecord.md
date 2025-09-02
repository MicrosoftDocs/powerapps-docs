---
title: "unstructuredfilesearchrecord table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the unstructuredfilesearchrecord table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# unstructuredfilesearchrecord table/entity reference (Microsoft Dataverse)

UnstructuredFileSearchRecord

## Messages

The following table lists the messages for the unstructuredfilesearchrecord table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /unstructuredfilesearchrecords(*unstructuredfilesearchrecordid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /unstructuredfilesearchrecords<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /unstructuredfilesearchrecords(*unstructuredfilesearchrecordid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /unstructuredfilesearchrecords(*unstructuredfilesearchrecordid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /unstructuredfilesearchrecords<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /unstructuredfilesearchrecords(*unstructuredfilesearchrecordid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /unstructuredfilesearchrecords(*unstructuredfilesearchrecordid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /unstructuredfilesearchrecords(*unstructuredfilesearchrecordid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the unstructuredfilesearchrecord table.

|Property|Value|
| --- | --- |
| **DisplayName** | **UnstructuredFileSearchRecord** |
| **DisplayCollectionName** | **UnstructuredFileSearchRecord** |
| **SchemaName** | `unstructuredfilesearchrecord` |
| **CollectionSchemaName** | `unstructuredfilesearchrecords` |
| **EntitySetName** | `unstructuredfilesearchrecords`|
| **LogicalName** | `unstructuredfilesearchrecord` |
| **LogicalCollectionName** | `unstructuredfilesearchrecords` |
| **PrimaryIdAttribute** | `unstructuredfilesearchrecordid` |
| **PrimaryNameAttribute** |`columnname` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeType](#BKMK_AttributeType)
- [ColumnName](#BKMK_ColumnName)
- [Content](#BKMK_Content)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [RecordId](#BKMK_RecordId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UnstructuredFileSearchEntityId](#BKMK_UnstructuredFileSearchEntityId)
- [unstructuredfilesearchrecordId](#BKMK_unstructuredfilesearchrecordId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AttributeType"></a> AttributeType

|Property|Value|
|---|---|
|Description||
|DisplayName|**AttributeType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributetype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`unstructuredfilesearchrecord_attributetype`|

#### AttributeType Choices/Options

|Value|Label|
|---|---|
|1|**FileType**|
|2|**Multiline Text**|

### <a name="BKMK_ColumnName"></a> ColumnName

|Property|Value|
|---|---|
|Description|**Column Name in the external system**|
|DisplayName|**ColumnName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`columnname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_Content"></a> Content

|Property|Value|
|---|---|
|Description|**Contains the Rich Text content if AttributeType = RichText, Otherwise blank**|
|DisplayName|**Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

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

### <a name="BKMK_RecordId"></a> RecordId

|Property|Value|
|---|---|
|Description|**Id of the record in the external system**|
|DisplayName|**RecordId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|600|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Table1**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`unstructuredfilesearchrecord_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Table1**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`unstructuredfilesearchrecord_statuscode`|

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

### <a name="BKMK_UnstructuredFileSearchEntityId"></a> UnstructuredFileSearchEntityId

|Property|Value|
|---|---|
|Description|**Lookup to FederatedFileSearchEntity**|
|DisplayName|**UnstructuredFileSearchEntityId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`unstructuredfilesearchentityid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|unstructuredfilesearchentity|

### <a name="BKMK_unstructuredfilesearchrecordId"></a> unstructuredfilesearchrecordId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**UnstructuredFileSearchRecord**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`unstructuredfilesearchrecordid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
- [Filedata](#BKMK_Filedata)
- [Filedata_Name](#BKMK_Filedata_Name)
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

### <a name="BKMK_Filedata"></a> Filedata

|Property|Value|
|---|---|
|Description|**Contains the content of a file if AttributeType = FileType, Otherwise blank**|
|DisplayName|**Filedata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`filedata`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|10485760|

### <a name="BKMK_Filedata_Name"></a> Filedata_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filedata_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

- [business_unit_unstructuredfilesearchrecord](#BKMK_business_unit_unstructuredfilesearchrecord)
- [FileAttachment_unstructuredfilesearchrecord_Filedata](#BKMK_FileAttachment_unstructuredfilesearchrecord_Filedata)
- [lk_unstructuredfilesearchrecord_createdby](#BKMK_lk_unstructuredfilesearchrecord_createdby)
- [lk_unstructuredfilesearchrecord_createdonbehalfby](#BKMK_lk_unstructuredfilesearchrecord_createdonbehalfby)
- [lk_unstructuredfilesearchrecord_modifiedby](#BKMK_lk_unstructuredfilesearchrecord_modifiedby)
- [lk_unstructuredfilesearchrecord_modifiedonbehalfby](#BKMK_lk_unstructuredfilesearchrecord_modifiedonbehalfby)
- [owner_unstructuredfilesearchrecord](#BKMK_owner_unstructuredfilesearchrecord)
- [team_unstructuredfilesearchrecord](#BKMK_team_unstructuredfilesearchrecord)
- [unstructuredfilesearchentity_unstructuredfilesearchrecord_UnstructuredFileSearchEntityId](#BKMK_unstructuredfilesearchentity_unstructuredfilesearchrecord_UnstructuredFileSearchEntityId)
- [user_unstructuredfilesearchrecord](#BKMK_user_unstructuredfilesearchrecord)

### <a name="BKMK_business_unit_unstructuredfilesearchrecord"></a> business_unit_unstructuredfilesearchrecord

One-To-Many Relationship: [businessunit business_unit_unstructuredfilesearchrecord](businessunit.md#BKMK_business_unit_unstructuredfilesearchrecord)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_unstructuredfilesearchrecord_Filedata"></a> FileAttachment_unstructuredfilesearchrecord_Filedata

One-To-Many Relationship: [fileattachment FileAttachment_unstructuredfilesearchrecord_Filedata](fileattachment.md#BKMK_FileAttachment_unstructuredfilesearchrecord_Filedata)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`filedata`|
|ReferencingEntityNavigationPropertyName|`filedata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_unstructuredfilesearchrecord_createdby"></a> lk_unstructuredfilesearchrecord_createdby

One-To-Many Relationship: [systemuser lk_unstructuredfilesearchrecord_createdby](systemuser.md#BKMK_lk_unstructuredfilesearchrecord_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_unstructuredfilesearchrecord_createdonbehalfby"></a> lk_unstructuredfilesearchrecord_createdonbehalfby

One-To-Many Relationship: [systemuser lk_unstructuredfilesearchrecord_createdonbehalfby](systemuser.md#BKMK_lk_unstructuredfilesearchrecord_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_unstructuredfilesearchrecord_modifiedby"></a> lk_unstructuredfilesearchrecord_modifiedby

One-To-Many Relationship: [systemuser lk_unstructuredfilesearchrecord_modifiedby](systemuser.md#BKMK_lk_unstructuredfilesearchrecord_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_unstructuredfilesearchrecord_modifiedonbehalfby"></a> lk_unstructuredfilesearchrecord_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_unstructuredfilesearchrecord_modifiedonbehalfby](systemuser.md#BKMK_lk_unstructuredfilesearchrecord_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_unstructuredfilesearchrecord"></a> owner_unstructuredfilesearchrecord

One-To-Many Relationship: [owner owner_unstructuredfilesearchrecord](owner.md#BKMK_owner_unstructuredfilesearchrecord)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_unstructuredfilesearchrecord"></a> team_unstructuredfilesearchrecord

One-To-Many Relationship: [team team_unstructuredfilesearchrecord](team.md#BKMK_team_unstructuredfilesearchrecord)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_unstructuredfilesearchrecord_UnstructuredFileSearchEntityId"></a> unstructuredfilesearchentity_unstructuredfilesearchrecord_UnstructuredFileSearchEntityId

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_unstructuredfilesearchrecord_UnstructuredFileSearchEntityId](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_unstructuredfilesearchrecord_UnstructuredFileSearchEntityId)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`unstructuredfilesearchentityid`|
|ReferencingEntityNavigationPropertyName|`UnstructuredFileSearchEntityId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_unstructuredfilesearchrecord"></a> user_unstructuredfilesearchrecord

One-To-Many Relationship: [systemuser user_unstructuredfilesearchrecord](systemuser.md#BKMK_user_unstructuredfilesearchrecord)

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

- [unstructuredfilesearchrecord_AsyncOperations](#BKMK_unstructuredfilesearchrecord_AsyncOperations)
- [unstructuredfilesearchrecord_BulkDeleteFailures](#BKMK_unstructuredfilesearchrecord_BulkDeleteFailures)
- [unstructuredfilesearchrecord_DuplicateBaseRecord](#BKMK_unstructuredfilesearchrecord_DuplicateBaseRecord)
- [unstructuredfilesearchrecord_DuplicateMatchingRecord](#BKMK_unstructuredfilesearchrecord_DuplicateMatchingRecord)
- [unstructuredfilesearchrecord_FileAttachments](#BKMK_unstructuredfilesearchrecord_FileAttachments)
- [unstructuredfilesearchrecord_MailboxTrackingFolders](#BKMK_unstructuredfilesearchrecord_MailboxTrackingFolders)
- [unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses](#BKMK_unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses)
- [unstructuredfilesearchrecord_ProcessSession](#BKMK_unstructuredfilesearchrecord_ProcessSession)
- [unstructuredfilesearchrecord_SyncErrors](#BKMK_unstructuredfilesearchrecord_SyncErrors)

### <a name="BKMK_unstructuredfilesearchrecord_AsyncOperations"></a> unstructuredfilesearchrecord_AsyncOperations

Many-To-One Relationship: [asyncoperation unstructuredfilesearchrecord_AsyncOperations](asyncoperation.md#BKMK_unstructuredfilesearchrecord_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_BulkDeleteFailures"></a> unstructuredfilesearchrecord_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure unstructuredfilesearchrecord_BulkDeleteFailures](bulkdeletefailure.md#BKMK_unstructuredfilesearchrecord_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_DuplicateBaseRecord"></a> unstructuredfilesearchrecord_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord unstructuredfilesearchrecord_DuplicateBaseRecord](duplicaterecord.md#BKMK_unstructuredfilesearchrecord_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_DuplicateMatchingRecord"></a> unstructuredfilesearchrecord_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord unstructuredfilesearchrecord_DuplicateMatchingRecord](duplicaterecord.md#BKMK_unstructuredfilesearchrecord_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_FileAttachments"></a> unstructuredfilesearchrecord_FileAttachments

Many-To-One Relationship: [fileattachment unstructuredfilesearchrecord_FileAttachments](fileattachment.md#BKMK_unstructuredfilesearchrecord_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_MailboxTrackingFolders"></a> unstructuredfilesearchrecord_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder unstructuredfilesearchrecord_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_unstructuredfilesearchrecord_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses"></a> unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_ProcessSession"></a> unstructuredfilesearchrecord_ProcessSession

Many-To-One Relationship: [processsession unstructuredfilesearchrecord_ProcessSession](processsession.md#BKMK_unstructuredfilesearchrecord_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_unstructuredfilesearchrecord_SyncErrors"></a> unstructuredfilesearchrecord_SyncErrors

Many-To-One Relationship: [syncerror unstructuredfilesearchrecord_SyncErrors](syncerror.md#BKMK_unstructuredfilesearchrecord_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`unstructuredfilesearchrecord_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.unstructuredfilesearchrecord?displayProperty=fullName>
