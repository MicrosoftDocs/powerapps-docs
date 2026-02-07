---
title: "Package History (packagehistory) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Package History (packagehistory) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Package History (packagehistory) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Package History (packagehistory) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /packagehistories<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /packagehistories(*packagehistoryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /packagehistories(*packagehistoryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /packagehistories<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /packagehistories(*packagehistoryid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /packagehistories(*packagehistoryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /packagehistories(*packagehistoryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Package History (packagehistory) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Package History** |
| **DisplayCollectionName** | **Package Histories** |
| **SchemaName** | `packagehistory` |
| **CollectionSchemaName** | `packagehistories` |
| **EntitySetName** | `packagehistories`|
| **LogicalName** | `packagehistory` |
| **LogicalCollectionName** | `packagehistories` |
| **PrimaryIdAttribute** | `packagehistoryid` |
| **PrimaryNameAttribute** |`executionname` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApplicationId](#BKMK_ApplicationId)
- [ApplicationName](#BKMK_ApplicationName)
- [CatalogId](#BKMK_CatalogId)
- [CorrelationId](#BKMK_CorrelationId)
- [DeployAsUserId](#BKMK_DeployAsUserId)
- [DeploymentMessageId](#BKMK_DeploymentMessageId)
- [ExecutionName](#BKMK_ExecutionName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsClusterOperation](#BKMK_IsClusterOperation)
- [OperationId](#BKMK_OperationId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [packagehistoryId](#BKMK_packagehistoryId)
- [PackageId](#BKMK_PackageId)
- [PackageInstanceId](#BKMK_PackageInstanceId)
- [PackageType](#BKMK_PackageType)
- [Priority](#BKMK_Priority)
- [PublisherId](#BKMK_PublisherId)
- [PublisherName](#BKMK_PublisherName)
- [Settings](#BKMK_Settings)
- [StageValue](#BKMK_StageValue)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [StatusMessage](#BKMK_StatusMessage)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UniqueName](#BKMK_UniqueName)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [Version](#BKMK_Version)

### <a name="BKMK_ApplicationId"></a> ApplicationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the application installed**|
|DisplayName|**Application Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ApplicationName"></a> ApplicationName

|Property|Value|
|---|---|
|Description|**The application name of the target for installation**|
|DisplayName|**Application Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CatalogId"></a> CatalogId

|Property|Value|
|---|---|
|Description|**The catalog that acted as the source for the artifact**|
|DisplayName|**Catalog Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`catalogid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|---|---|
|Description|**The correlationId for this process**|
|DisplayName|**Correlation Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`correlationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_DeployAsUserId"></a> DeployAsUserId

|Property|Value|
|---|---|
|Description|**deploy package as given user (azureactivedirectoryobjectid)**|
|DisplayName|**Deploy As User Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deployasuserid`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400000|

### <a name="BKMK_DeploymentMessageId"></a> DeploymentMessageId

|Property|Value|
|---|---|
|Description|**Stores Deployment MessageId for the queued package.**|
|DisplayName|**Deployment Message Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deploymentmessageid`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ExecutionName"></a> ExecutionName

|Property|Value|
|---|---|
|Description|**The display name for this operation**|
|DisplayName|**Execution Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_IsClusterOperation"></a> IsClusterOperation

|Property|Value|
|---|---|
|Description|**Indicates whether this package history record represents a cluster operation**|
|DisplayName|**Cluster Operation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isclusteroperation`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`packagehistories_isclusteroperation`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OperationId"></a> OperationId

|Property|Value|
|---|---|
|Description|**OperationId**|
|DisplayName|**OperationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

### <a name="BKMK_packagehistoryId"></a> packagehistoryId

|Property|Value|
|---|---|
|Description|**Unique identifier for a single package history execution**|
|DisplayName|**Package History**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`packagehistoryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PackageId"></a> PackageId

|Property|Value|
|---|---|
|Description|**Unique identifier for the package to install**|
|DisplayName|**Package Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`packageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PackageInstanceId"></a> PackageInstanceId

|Property|Value|
|---|---|
|Description||
|DisplayName|**PackageInstanceId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`packageinstanceid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PackageType"></a> PackageType

|Property|Value|
|---|---|
|Description|**Type of the package**|
|DisplayName|**Package Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`packagetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`packagehistories_packagetype`|

#### PackageType Choices/Options

|Value|Label|
|---|---|
|0|**App**|
|1|**Solution**|
|2|**DatabaseVersionUpdate**|

### <a name="BKMK_Priority"></a> Priority

|Property|Value|
|---|---|
|Description|**Priority level for the package**|
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`priority`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`packagehistories_priority`|

#### Priority Choices/Options

|Value|Label|
|---|---|
|1|**High**|
|2|**Medium**|
|3|**Low**|

### <a name="BKMK_PublisherId"></a> PublisherId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Publisher Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publisherid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PublisherName"></a> PublisherName

|Property|Value|
|---|---|
|Description|**The publisher name of the target for installation**|
|DisplayName|**Publisher Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publishername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Settings"></a> Settings

|Property|Value|
|---|---|
|Description|**Deployment Package settings value.**|
|DisplayName|**Settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`settings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400000|

### <a name="BKMK_StageValue"></a> StageValue

|Property|Value|
|---|---|
|Description|**Stage of the operation**|
|DisplayName|**Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagevalue`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`packagehistories_stagevalue`|

#### StageValue Choices/Options

|Value|Label|
|---|---|
|0|**PackageProcessing**|
|1|**Solutions**|
|2|**Configuration**|
|3|**PackageInit**|
|4|**CustomCode**|
|5|**DataImport**|
|6|**FnO**|
|7|**SchemaDeployed**|
|8|**QueuedForCluster**|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the operation**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`packagehistory_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 526430000<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 526430003<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the operation**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`packagehistory_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|526430000|Label: **Requested**<br />State:0<br />TransitionData: None|
|526430001|Label: **Scheduled**<br />State:0<br />TransitionData: None|
|526430002|Label: **In Process**<br />State:0<br />TransitionData: None|
|526430003|Label: **Completed**<br />State:1<br />TransitionData: None|
|526430004|Label: **Failed**<br />State:1<br />TransitionData: None|
|526430005|Label: **Uninstalled**<br />State:1<br />TransitionData: None|

### <a name="BKMK_StatusMessage"></a> StatusMessage

|Property|Value|
|---|---|
|Description|**Status for the orchestration**|
|DisplayName|**Status Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statusmessage`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**The unique name of the target for installation**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_Version"></a> Version

|Property|Value|
|---|---|
|Description|**The version of the target for installation**|
|DisplayName|**Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DeploymentLog](#BKMK_DeploymentLog)
- [DeploymentLog_Name](#BKMK_DeploymentLog_Name)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [PackageFile](#BKMK_PackageFile)
- [PackageFile_Name](#BKMK_PackageFile_Name)
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

### <a name="BKMK_DeploymentLog"></a> DeploymentLog

|Property|Value|
|---|---|
|Description|**Stores the package deployment logs for an installation**|
|DisplayName|**Deployment Log**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deploymentlog`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|256000|

### <a name="BKMK_DeploymentLog_Name"></a> DeploymentLog_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deploymentlog_name`|
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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_PackageFile"></a> PackageFile

|Property|Value|
|---|---|
|Description|**Stores the package file for installation**|
|DisplayName|**Package File**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`packagefile`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|256000|

### <a name="BKMK_PackageFile_Name"></a> PackageFile_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`packagefile_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

- [FileAttachment_packagehistory_DeploymentLog](#BKMK_FileAttachment_packagehistory_DeploymentLog)
- [FileAttachment_packagehistory_PackageFile](#BKMK_FileAttachment_packagehistory_PackageFile)
- [lk_packagehistory_createdby](#BKMK_lk_packagehistory_createdby)
- [lk_packagehistory_createdonbehalfby](#BKMK_lk_packagehistory_createdonbehalfby)
- [lk_packagehistory_modifiedby](#BKMK_lk_packagehistory_modifiedby)
- [lk_packagehistory_modifiedonbehalfby](#BKMK_lk_packagehistory_modifiedonbehalfby)
- [organization_packagehistory](#BKMK_organization_packagehistory)

### <a name="BKMK_FileAttachment_packagehistory_DeploymentLog"></a> FileAttachment_packagehistory_DeploymentLog

One-To-Many Relationship: [fileattachment FileAttachment_packagehistory_DeploymentLog](fileattachment.md#BKMK_FileAttachment_packagehistory_DeploymentLog)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`deploymentlog`|
|ReferencingEntityNavigationPropertyName|`deploymentlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_packagehistory_PackageFile"></a> FileAttachment_packagehistory_PackageFile

One-To-Many Relationship: [fileattachment FileAttachment_packagehistory_PackageFile](fileattachment.md#BKMK_FileAttachment_packagehistory_PackageFile)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`packagefile`|
|ReferencingEntityNavigationPropertyName|`packagefile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_packagehistory_createdby"></a> lk_packagehistory_createdby

One-To-Many Relationship: [systemuser lk_packagehistory_createdby](systemuser.md#BKMK_lk_packagehistory_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_packagehistory_createdonbehalfby"></a> lk_packagehistory_createdonbehalfby

One-To-Many Relationship: [systemuser lk_packagehistory_createdonbehalfby](systemuser.md#BKMK_lk_packagehistory_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_packagehistory_modifiedby"></a> lk_packagehistory_modifiedby

One-To-Many Relationship: [systemuser lk_packagehistory_modifiedby](systemuser.md#BKMK_lk_packagehistory_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_packagehistory_modifiedonbehalfby"></a> lk_packagehistory_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_packagehistory_modifiedonbehalfby](systemuser.md#BKMK_lk_packagehistory_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_packagehistory"></a> organization_packagehistory

One-To-Many Relationship: [organization organization_packagehistory](organization.md#BKMK_organization_packagehistory)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [packagehistory_AsyncOperations](#BKMK_packagehistory_AsyncOperations)
- [packagehistory_BulkDeleteFailures](#BKMK_packagehistory_BulkDeleteFailures)
- [packagehistory_DuplicateBaseRecord](#BKMK_packagehistory_DuplicateBaseRecord)
- [packagehistory_DuplicateMatchingRecord](#BKMK_packagehistory_DuplicateMatchingRecord)
- [packagehistory_FileAttachments](#BKMK_packagehistory_FileAttachments)
- [packagehistory_MailboxTrackingFolders](#BKMK_packagehistory_MailboxTrackingFolders)
- [packagehistory_PrincipalObjectAttributeAccesses](#BKMK_packagehistory_PrincipalObjectAttributeAccesses)
- [packagehistory_ProcessSession](#BKMK_packagehistory_ProcessSession)
- [packagehistory_SyncErrors](#BKMK_packagehistory_SyncErrors)

### <a name="BKMK_packagehistory_AsyncOperations"></a> packagehistory_AsyncOperations

Many-To-One Relationship: [asyncoperation packagehistory_AsyncOperations](asyncoperation.md#BKMK_packagehistory_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_BulkDeleteFailures"></a> packagehistory_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure packagehistory_BulkDeleteFailures](bulkdeletefailure.md#BKMK_packagehistory_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_DuplicateBaseRecord"></a> packagehistory_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord packagehistory_DuplicateBaseRecord](duplicaterecord.md#BKMK_packagehistory_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_DuplicateMatchingRecord"></a> packagehistory_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord packagehistory_DuplicateMatchingRecord](duplicaterecord.md#BKMK_packagehistory_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_FileAttachments"></a> packagehistory_FileAttachments

Many-To-One Relationship: [fileattachment packagehistory_FileAttachments](fileattachment.md#BKMK_packagehistory_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_MailboxTrackingFolders"></a> packagehistory_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder packagehistory_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_packagehistory_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_PrincipalObjectAttributeAccesses"></a> packagehistory_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess packagehistory_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_packagehistory_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_ProcessSession"></a> packagehistory_ProcessSession

Many-To-One Relationship: [processsession packagehistory_ProcessSession](processsession.md#BKMK_packagehistory_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_packagehistory_SyncErrors"></a> packagehistory_SyncErrors

Many-To-One Relationship: [syncerror packagehistory_SyncErrors](syncerror.md#BKMK_packagehistory_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`packagehistory_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.packagehistory?displayProperty=fullName>
