---
title: "packagehistory table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the packagehistory table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# packagehistory table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: msdyn_SolutionPackageMapping Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /packagehistories<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /packagehistories(*packagehistoryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET /packagehistories(*packagehistoryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /packagehistories<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH /packagehistories(*packagehistoryid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /packagehistories(*packagehistoryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|packagehistories|
|DisplayCollectionName|Package Histories|
|DisplayName|Package History|
|EntitySetName|packagehistories|
|IsBPFEntity|False|
|LogicalCollectionName|packagehistories|
|LogicalName|packagehistory|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|packagehistoryid|
|PrimaryNameAttribute|executionname|
|SchemaName|packagehistory|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApplicationId](#BKMK_ApplicationId)
- [ApplicationName](#BKMK_ApplicationName)
- [CatalogId](#BKMK_CatalogId)
- [CorrelationId](#BKMK_CorrelationId)
- [ExecutionName](#BKMK_ExecutionName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OperationId](#BKMK_OperationId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [packagehistoryId](#BKMK_packagehistoryId)
- [PackageId](#BKMK_PackageId)
- [PublisherId](#BKMK_PublisherId)
- [PublisherName](#BKMK_PublisherName)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [StatusMessage](#BKMK_StatusMessage)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UniqueName](#BKMK_UniqueName)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [Version](#BKMK_Version)


### <a name="BKMK_ApplicationId"></a> ApplicationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the application installed|
|DisplayName|Application Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|applicationid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ApplicationName"></a> ApplicationName

|Property|Value|
|--------|-----|
|Description|The application name of the target for installation|
|DisplayName|Application Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|applicationname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CatalogId"></a> CatalogId

|Property|Value|
|--------|-----|
|Description|The catalog that acted as the source for the artifact|
|DisplayName|Catalog Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|catalogid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|--------|-----|
|Description|The correlationId for this process|
|DisplayName|Correlation Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|correlationid|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExecutionName"></a> ExecutionName

|Property|Value|
|--------|-----|
|Description|The display name for this operation|
|DisplayName|Execution Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|executionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_OperationId"></a> OperationId

|Property|Value|
|--------|-----|
|Description|OperationId|
|DisplayName|OperationId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|operationid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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


### <a name="BKMK_packagehistoryId"></a> packagehistoryId

|Property|Value|
|--------|-----|
|Description|Unique identifier for a single package history execution|
|DisplayName|Package History|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|packagehistoryid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_PackageId"></a> PackageId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the package to install|
|DisplayName|Package Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|packageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_PublisherId"></a> PublisherId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Publisher Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|publisherid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_PublisherName"></a> PublisherName

|Property|Value|
|--------|-----|
|Description|The publisher name of the target for installation|
|DisplayName|Publisher Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|publishername|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the operation|
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
|0|Active|526430000|Active|
|1|Inactive|526430003|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the operation|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|526430000|Requested|0|
|526430001|Scheduled|0|
|526430002|In Process|0|
|526430003|Completed|1|
|526430004|Failed|1|
|526430005|Uninstalled|1|



### <a name="BKMK_StatusMessage"></a> StatusMessage

|Property|Value|
|--------|-----|
|Description|Status for the orchestration|
|DisplayName|Status Message|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statusmessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|--------|-----|
|Description|The unique name of the target for installation|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|uniquename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_Version"></a> Version

|Property|Value|
|--------|-----|
|Description|The version of the target for installation|
|DisplayName|Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|version|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

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
- [DeploymentLog](#BKMK_DeploymentLog)
- [DeploymentLog_Name](#BKMK_DeploymentLog_Name)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
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


### <a name="BKMK_DeploymentLog"></a> DeploymentLog

|Property|Value|
|--------|-----|
|Description|Stores the package deployment logs for an installation|
|DisplayName|Deployment Log|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|deploymentlog|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_DeploymentLog_Name"></a> DeploymentLog_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|deploymentlog_name|
|MaxLength|200|
|RequiredLevel|None|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


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

- [packagehistory_SyncErrors](#BKMK_packagehistory_SyncErrors)
- [packagehistory_DuplicateMatchingRecord](#BKMK_packagehistory_DuplicateMatchingRecord)
- [packagehistory_DuplicateBaseRecord](#BKMK_packagehistory_DuplicateBaseRecord)
- [packagehistory_AsyncOperations](#BKMK_packagehistory_AsyncOperations)
- [packagehistory_MailboxTrackingFolders](#BKMK_packagehistory_MailboxTrackingFolders)
- [packagehistory_ProcessSession](#BKMK_packagehistory_ProcessSession)
- [packagehistory_BulkDeleteFailures](#BKMK_packagehistory_BulkDeleteFailures)
- [packagehistory_PrincipalObjectAttributeAccesses](#BKMK_packagehistory_PrincipalObjectAttributeAccesses)


### <a name="BKMK_packagehistory_SyncErrors"></a> packagehistory_SyncErrors

**Added by**: System Solution Solution

Same as the [packagehistory_SyncErrors](syncerror.md#BKMK_packagehistory_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_packagehistory_DuplicateMatchingRecord"></a> packagehistory_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [packagehistory_DuplicateMatchingRecord](duplicaterecord.md#BKMK_packagehistory_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_packagehistory_DuplicateBaseRecord"></a> packagehistory_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [packagehistory_DuplicateBaseRecord](duplicaterecord.md#BKMK_packagehistory_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_packagehistory_AsyncOperations"></a> packagehistory_AsyncOperations

**Added by**: System Solution Solution

Same as the [packagehistory_AsyncOperations](asyncoperation.md#BKMK_packagehistory_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_packagehistory_MailboxTrackingFolders"></a> packagehistory_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [packagehistory_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_packagehistory_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_packagehistory_ProcessSession"></a> packagehistory_ProcessSession

**Added by**: System Solution Solution

Same as the [packagehistory_ProcessSession](processsession.md#BKMK_packagehistory_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_packagehistory_BulkDeleteFailures"></a> packagehistory_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [packagehistory_BulkDeleteFailures](bulkdeletefailure.md#BKMK_packagehistory_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_packagehistory_PrincipalObjectAttributeAccesses"></a> packagehistory_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [packagehistory_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_packagehistory_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|packagehistory_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_packagehistory_createdby](#BKMK_lk_packagehistory_createdby)
- [lk_packagehistory_createdonbehalfby](#BKMK_lk_packagehistory_createdonbehalfby)
- [lk_packagehistory_modifiedby](#BKMK_lk_packagehistory_modifiedby)
- [lk_packagehistory_modifiedonbehalfby](#BKMK_lk_packagehistory_modifiedonbehalfby)
- [organization_packagehistory](#BKMK_organization_packagehistory)


### <a name="BKMK_lk_packagehistory_createdby"></a> lk_packagehistory_createdby

**Added by**: System Solution Solution

See the [lk_packagehistory_createdby](systemuser.md#BKMK_lk_packagehistory_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_packagehistory_createdonbehalfby"></a> lk_packagehistory_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_packagehistory_createdonbehalfby](systemuser.md#BKMK_lk_packagehistory_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_packagehistory_modifiedby"></a> lk_packagehistory_modifiedby

**Added by**: System Solution Solution

See the [lk_packagehistory_modifiedby](systemuser.md#BKMK_lk_packagehistory_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_packagehistory_modifiedonbehalfby"></a> lk_packagehistory_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_packagehistory_modifiedonbehalfby](systemuser.md#BKMK_lk_packagehistory_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_packagehistory"></a> organization_packagehistory

**Added by**: System Solution Solution

See the [organization_packagehistory](organization.md#BKMK_organization_packagehistory) one-to-many relationship for the [organization](organization.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.packagehistory?text=packagehistory EntityType" />