---
title: "Catalog Submission Files (mspcat_CatalogSubmissionFiles) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Catalog Submission Files (mspcat_CatalogSubmissionFiles) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Catalog Submission Files (mspcat_CatalogSubmissionFiles) table/entity reference (Microsoft Dataverse)

Files associated with the package that will be used as part of the submission to the catalog system.

## Messages

The following table lists the messages for the Catalog Submission Files (mspcat_CatalogSubmissionFiles) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspcat_catalogsubmissionfileses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /mspcat_catalogsubmissionfileses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Catalog Submission Files (mspcat_CatalogSubmissionFiles) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Catalog Submission Files (mspcat_CatalogSubmissionFiles) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Catalog Submission Files** |
| **DisplayCollectionName** | **Catalog Submission Files** |
| **SchemaName** | `mspcat_CatalogSubmissionFiles` |
| **CollectionSchemaName** | `mspcat_CatalogSubmissionFileses` |
| **EntitySetName** | `mspcat_catalogsubmissionfileses`|
| **LogicalName** | `mspcat_catalogsubmissionfiles` |
| **LogicalCollectionName** | `mspcat_catalogsubmissionfileses` |
| **PrimaryIdAttribute** | `mspcat_catalogsubmissionfilesid` |
| **PrimaryNameAttribute** |`mspcat_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [mspcat_CatalogSubmissionFilesId](#BKMK_mspcat_CatalogSubmissionFilesId)
- [mspcat_Description](#BKMK_mspcat_Description)
- [mspcat_FileType](#BKMK_mspcat_FileType)
- [mspcat_ImageSize](#BKMK_mspcat_ImageSize)
- [mspcat_Name](#BKMK_mspcat_Name)
- [mspcat_PackageStore](#BKMK_mspcat_PackageStore)
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

### <a name="BKMK_mspcat_CatalogSubmissionFilesId"></a> mspcat_CatalogSubmissionFilesId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Catalog Submission Files**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspcat_catalogsubmissionfilesid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspcat_Description"></a> mspcat_Description

|Property|Value|
|---|---|
|Description|**File Item description**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspcat_description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspcat_FileType"></a> mspcat_FileType

|Property|Value|
|---|---|
|Description|**Type of File Described**|
|DisplayName|**File Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspcat_filetype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspcat_catalogsubmissionfiles_mspcat_filetype`|

#### mspcat_FileType Choices/Options

|Value|Label|
|---|---|
|526430000|**Image**|
|526430001|**Document**|
|526430002|**Video**|

### <a name="BKMK_mspcat_ImageSize"></a> mspcat_ImageSize

|Property|Value|
|---|---|
|Description|**Size of Image Described**|
|DisplayName|**Image Size**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspcat_imagesize`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspcat_catalogsubmissionfiles_mspcat_imagesize`|

#### mspcat_ImageSize Choices/Options

|Value|Label|
|---|---|
|526430000|**48 x 48**|
|526430001|**216 x 216**|
|526430002|**Screen Shot**|

### <a name="BKMK_mspcat_Name"></a> mspcat_Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspcat_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspcat_PackageStore"></a> mspcat_PackageStore

|Property|Value|
|---|---|
|Description|**Related Package Store Item.**|
|DisplayName|**Package Store**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspcat_packagestore`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspcat_packagestore|

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
|Description|**Status of the Catalog Submission Files**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspcat_catalogsubmissionfiles_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Catalog Submission Files**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspcat_catalogsubmissionfiles_statuscode`|

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
- [mspcat_File](#BKMK_mspcat_File)
- [mspcat_File_Name](#BKMK_mspcat_File_Name)
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

### <a name="BKMK_mspcat_File"></a> mspcat_File

|Property|Value|
|---|---|
|Description|**File asset**|
|DisplayName|**File**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspcat_file`|
|RequiredLevel|ApplicationRequired|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_mspcat_File_Name"></a> mspcat_File_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspcat_file_name`|
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

- [business_unit_mspcat_catalogsubmissionfiles](#BKMK_business_unit_mspcat_catalogsubmissionfiles)
- [FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File](#BKMK_FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File)
- [lk_mspcat_catalogsubmissionfiles_createdby](#BKMK_lk_mspcat_catalogsubmissionfiles_createdby)
- [lk_mspcat_catalogsubmissionfiles_createdonbehalfby](#BKMK_lk_mspcat_catalogsubmissionfiles_createdonbehalfby)
- [lk_mspcat_catalogsubmissionfiles_modifiedby](#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedby)
- [lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby](#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby)
- [mspcat_mspcat_catalogsubmissionfiles_PackageStor](#BKMK_mspcat_mspcat_catalogsubmissionfiles_PackageStor)
- [owner_mspcat_catalogsubmissionfiles](#BKMK_owner_mspcat_catalogsubmissionfiles)
- [team_mspcat_catalogsubmissionfiles](#BKMK_team_mspcat_catalogsubmissionfiles)
- [user_mspcat_catalogsubmissionfiles](#BKMK_user_mspcat_catalogsubmissionfiles)

### <a name="BKMK_business_unit_mspcat_catalogsubmissionfiles"></a> business_unit_mspcat_catalogsubmissionfiles

One-To-Many Relationship: [businessunit business_unit_mspcat_catalogsubmissionfiles](businessunit.md#BKMK_business_unit_mspcat_catalogsubmissionfiles)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File"></a> FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File

One-To-Many Relationship: [fileattachment FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File](fileattachment.md#BKMK_FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`mspcat_file`|
|ReferencingEntityNavigationPropertyName|`mspcat_file`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_createdby"></a> lk_mspcat_catalogsubmissionfiles_createdby

One-To-Many Relationship: [systemuser lk_mspcat_catalogsubmissionfiles_createdby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_createdonbehalfby"></a> lk_mspcat_catalogsubmissionfiles_createdonbehalfby

One-To-Many Relationship: [systemuser lk_mspcat_catalogsubmissionfiles_createdonbehalfby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_modifiedby"></a> lk_mspcat_catalogsubmissionfiles_modifiedby

One-To-Many Relationship: [systemuser lk_mspcat_catalogsubmissionfiles_modifiedby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby"></a> lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_mspcat_catalogsubmissionfiles_PackageStor"></a> mspcat_mspcat_catalogsubmissionfiles_PackageStor

One-To-Many Relationship: [mspcat_packagestore mspcat_mspcat_catalogsubmissionfiles_PackageStor](mspcat_packagestore.md#BKMK_mspcat_mspcat_catalogsubmissionfiles_PackageStor)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`mspcat_packagestore`|
|ReferencingEntityNavigationPropertyName|`mspcat_PackageStore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_mspcat_catalogsubmissionfiles"></a> owner_mspcat_catalogsubmissionfiles

One-To-Many Relationship: [owner owner_mspcat_catalogsubmissionfiles](owner.md#BKMK_owner_mspcat_catalogsubmissionfiles)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_mspcat_catalogsubmissionfiles"></a> team_mspcat_catalogsubmissionfiles

One-To-Many Relationship: [team team_mspcat_catalogsubmissionfiles](team.md#BKMK_team_mspcat_catalogsubmissionfiles)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_mspcat_catalogsubmissionfiles"></a> user_mspcat_catalogsubmissionfiles

One-To-Many Relationship: [systemuser user_mspcat_catalogsubmissionfiles](systemuser.md#BKMK_user_mspcat_catalogsubmissionfiles)

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

- [mspcat_catalogsubmissionfiles_Annotations](#BKMK_mspcat_catalogsubmissionfiles_Annotations)
- [mspcat_catalogsubmissionfiles_AsyncOperations](#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations)
- [mspcat_catalogsubmissionfiles_BulkDeleteFailures](#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures)
- [mspcat_catalogsubmissionfiles_DuplicateBaseRecord](#BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord)
- [mspcat_catalogsubmissionfiles_DuplicateMatchingRecord](#BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord)
- [mspcat_catalogsubmissionfiles_FileAttachments](#BKMK_mspcat_catalogsubmissionfiles_FileAttachments)
- [mspcat_catalogsubmissionfiles_MailboxTrackingFolders](#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders)
- [mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses)
- [mspcat_catalogsubmissionfiles_ProcessSession](#BKMK_mspcat_catalogsubmissionfiles_ProcessSession)
- [mspcat_catalogsubmissionfiles_SyncErrors](#BKMK_mspcat_catalogsubmissionfiles_SyncErrors)

### <a name="BKMK_mspcat_catalogsubmissionfiles_Annotations"></a> mspcat_catalogsubmissionfiles_Annotations

Many-To-One Relationship: [annotation mspcat_catalogsubmissionfiles_Annotations](annotation.md#BKMK_mspcat_catalogsubmissionfiles_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_AsyncOperations"></a> mspcat_catalogsubmissionfiles_AsyncOperations

Many-To-One Relationship: [asyncoperation mspcat_catalogsubmissionfiles_AsyncOperations](asyncoperation.md#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures"></a> mspcat_catalogsubmissionfiles_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure mspcat_catalogsubmissionfiles_BulkDeleteFailures](bulkdeletefailure.md#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord"></a> mspcat_catalogsubmissionfiles_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord mspcat_catalogsubmissionfiles_DuplicateBaseRecord](duplicaterecord.md#BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord"></a> mspcat_catalogsubmissionfiles_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord mspcat_catalogsubmissionfiles_DuplicateMatchingRecord](duplicaterecord.md#BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_FileAttachments"></a> mspcat_catalogsubmissionfiles_FileAttachments

Many-To-One Relationship: [fileattachment mspcat_catalogsubmissionfiles_FileAttachments](fileattachment.md#BKMK_mspcat_catalogsubmissionfiles_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders"></a> mspcat_catalogsubmissionfiles_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder mspcat_catalogsubmissionfiles_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses"></a> mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_ProcessSession"></a> mspcat_catalogsubmissionfiles_ProcessSession

Many-To-One Relationship: [processsession mspcat_catalogsubmissionfiles_ProcessSession](processsession.md#BKMK_mspcat_catalogsubmissionfiles_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_SyncErrors"></a> mspcat_catalogsubmissionfiles_SyncErrors

Many-To-One Relationship: [syncerror mspcat_catalogsubmissionfiles_SyncErrors](syncerror.md#BKMK_mspcat_catalogsubmissionfiles_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspcat_catalogsubmissionfiles_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspcat_catalogsubmissionfiles?displayProperty=fullName>
