---
title: "Catalog Submission Files (mspcat_CatalogSubmissionFiles)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Catalog Submission Files (mspcat_CatalogSubmissionFiles)  table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Catalog Submission Files (mspcat_CatalogSubmissionFiles)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Files associated with the package that will be used as part of the submission to the catalog system.

**Added by**: Power Platform Catalog Client Packaging Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspcat_catalogsubmissionfileses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /mspcat_catalogsubmissionfileses<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /mspcat_catalogsubmissionfileses(*mspcat_catalogsubmissionfilesid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspcat_CatalogSubmissionFileses|
|DisplayCollectionName|Catalog Submission Files|
|DisplayName|Catalog Submission Files|
|EntitySetName|mspcat_catalogsubmissionfileses|
|IsBPFEntity|False|
|LogicalCollectionName|mspcat_catalogsubmissionfileses|
|LogicalName|mspcat_catalogsubmissionfiles|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|mspcat_catalogsubmissionfilesid|
|PrimaryNameAttribute|mspcat_name|
|SchemaName|mspcat_CatalogSubmissionFiles|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspcat_CatalogSubmissionFilesId"></a> mspcat_CatalogSubmissionFilesId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Catalog Submission Files|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspcat_catalogsubmissionfilesid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspcat_Description"></a> mspcat_Description

|Property|Value|
|--------|-----|
|Description|File Item description|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspcat_description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspcat_FileType"></a> mspcat_FileType

|Property|Value|
|--------|-----|
|Description|Type of File Described|
|DisplayName|File Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspcat_filetype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspcat_FileType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|526430000|Image||
|526430001|Document||
|526430002|Video||



### <a name="BKMK_mspcat_ImageSize"></a> mspcat_ImageSize

|Property|Value|
|--------|-----|
|Description|Size of Image Described|
|DisplayName|Image Size|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspcat_imagesize|
|RequiredLevel|None|
|Type|Picklist|

#### mspcat_ImageSize Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|526430000|48 x 48||
|526430001|216 x 216||
|526430002|Screen Shot||



### <a name="BKMK_mspcat_Name"></a> mspcat_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspcat_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspcat_PackageStore"></a> mspcat_PackageStore

|Property|Value|
|--------|-----|
|Description|Related Package Store Item.|
|DisplayName|Package Store|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspcat_packagestore|
|RequiredLevel|ApplicationRequired|
|Targets|mspcat_packagestore|
|Type|Lookup|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Catalog Submission Files|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Catalog Submission Files|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [mspcat_File](#BKMK_mspcat_File)
- [mspcat_File_Name](#BKMK_mspcat_File_Name)
- [mspcat_PackageStoreName](#BKMK_mspcat_PackageStoreName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_mspcat_File"></a> mspcat_File

|Property|Value|
|--------|-----|
|Description|File asset|
|DisplayName|File|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspcat_file|
|RequiredLevel|ApplicationRequired|
|Type|File|


### <a name="BKMK_mspcat_File_Name"></a> mspcat_File_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspcat_file_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspcat_PackageStoreName"></a> mspcat_PackageStoreName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspcat_packagestorename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [mspcat_catalogsubmissionfiles_SyncErrors](#BKMK_mspcat_catalogsubmissionfiles_SyncErrors)
- [mspcat_catalogsubmissionfiles_DuplicateMatchingRecord](#BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord)
- [mspcat_catalogsubmissionfiles_DuplicateBaseRecord](#BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord)
- [mspcat_catalogsubmissionfiles_AsyncOperations](#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations)
- [mspcat_catalogsubmissionfiles_MailboxTrackingFolders](#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders)
- [mspcat_catalogsubmissionfiles_ProcessSession](#BKMK_mspcat_catalogsubmissionfiles_ProcessSession)
- [mspcat_catalogsubmissionfiles_BulkDeleteFailures](#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures)
- [mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses)
- [mspcat_catalogsubmissionfiles_Annotations](#BKMK_mspcat_catalogsubmissionfiles_Annotations)


### <a name="BKMK_mspcat_catalogsubmissionfiles_SyncErrors"></a> mspcat_catalogsubmissionfiles_SyncErrors

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_SyncErrors](syncerror.md#BKMK_mspcat_catalogsubmissionfiles_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord"></a> mspcat_catalogsubmissionfiles_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_DuplicateMatchingRecord](duplicaterecord.md#BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord"></a> mspcat_catalogsubmissionfiles_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_DuplicateBaseRecord](duplicaterecord.md#BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_AsyncOperations"></a> mspcat_catalogsubmissionfiles_AsyncOperations

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_AsyncOperations](asyncoperation.md#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders"></a> mspcat_catalogsubmissionfiles_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_ProcessSession"></a> mspcat_catalogsubmissionfiles_ProcessSession

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_ProcessSession](processsession.md#BKMK_mspcat_catalogsubmissionfiles_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures"></a> mspcat_catalogsubmissionfiles_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_BulkDeleteFailures](bulkdeletefailure.md#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses"></a> mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspcat_catalogsubmissionfiles_Annotations"></a> mspcat_catalogsubmissionfiles_Annotations

**Added by**: System Solution Solution

Same as the [mspcat_catalogsubmissionfiles_Annotations](annotation.md#BKMK_mspcat_catalogsubmissionfiles_Annotations) many-to-one relationship for the [annotation](annotation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspcat_catalogsubmissionfiles_Annotations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_mspcat_catalogsubmissionfiles_createdby](#BKMK_lk_mspcat_catalogsubmissionfiles_createdby)
- [lk_mspcat_catalogsubmissionfiles_createdonbehalfby](#BKMK_lk_mspcat_catalogsubmissionfiles_createdonbehalfby)
- [lk_mspcat_catalogsubmissionfiles_modifiedby](#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedby)
- [lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby](#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby)
- [user_mspcat_catalogsubmissionfiles](#BKMK_user_mspcat_catalogsubmissionfiles)
- [team_mspcat_catalogsubmissionfiles](#BKMK_team_mspcat_catalogsubmissionfiles)
- [business_unit_mspcat_catalogsubmissionfiles](#BKMK_business_unit_mspcat_catalogsubmissionfiles)
- [mspcat_mspcat_catalogsubmissionfiles_PackageStor](#BKMK_mspcat_mspcat_catalogsubmissionfiles_PackageStor)


### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_createdby"></a> lk_mspcat_catalogsubmissionfiles_createdby

**Added by**: System Solution Solution

See the [lk_mspcat_catalogsubmissionfiles_createdby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_createdonbehalfby"></a> lk_mspcat_catalogsubmissionfiles_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_mspcat_catalogsubmissionfiles_createdonbehalfby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_modifiedby"></a> lk_mspcat_catalogsubmissionfiles_modifiedby

**Added by**: System Solution Solution

See the [lk_mspcat_catalogsubmissionfiles_modifiedby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby"></a> lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby](systemuser.md#BKMK_lk_mspcat_catalogsubmissionfiles_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_mspcat_catalogsubmissionfiles"></a> user_mspcat_catalogsubmissionfiles

**Added by**: System Solution Solution

See the [user_mspcat_catalogsubmissionfiles](systemuser.md#BKMK_user_mspcat_catalogsubmissionfiles) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_mspcat_catalogsubmissionfiles"></a> team_mspcat_catalogsubmissionfiles

**Added by**: System Solution Solution

See the [team_mspcat_catalogsubmissionfiles](team.md#BKMK_team_mspcat_catalogsubmissionfiles) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_mspcat_catalogsubmissionfiles"></a> business_unit_mspcat_catalogsubmissionfiles

**Added by**: System Solution Solution

See the [business_unit_mspcat_catalogsubmissionfiles](businessunit.md#BKMK_business_unit_mspcat_catalogsubmissionfiles) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_mspcat_mspcat_catalogsubmissionfiles_PackageStor"></a> mspcat_mspcat_catalogsubmissionfiles_PackageStor

See the [mspcat_mspcat_catalogsubmissionfiles_PackageStor](mspcat_packagestore.md#BKMK_mspcat_mspcat_catalogsubmissionfiles_PackageStor) one-to-many relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspcat_catalogsubmissionfiles?text=mspcat_catalogsubmissionfiles EntityType" />