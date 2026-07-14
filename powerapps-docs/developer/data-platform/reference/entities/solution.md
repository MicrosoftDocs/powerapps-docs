---
title: "Solution table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution table/entity reference (Microsoft Dataverse)

A solution which contains CRM customizations.

## Messages

The following table lists the messages for the Solution table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `CloneAsPatch`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CloneAsPatch?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CloneAsPatchRequest>|
| `CloneAsSolution`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CloneAsSolution?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CloneAsSolutionRequest>|
| `Create`<br />Event: False |`POST` /solutions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /solutions(*solutionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteAndPromote`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteAndPromote?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DeleteAndPromoteRequest>|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /solutions(*solutionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /solutions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /solutions(*solutionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /solutions(*solutionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Solution table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution** |
| **DisplayCollectionName** | **Solutions** |
| **SchemaName** | `Solution` |
| **CollectionSchemaName** | `Solutions` |
| **EntitySetName** | `solutions`|
| **LogicalName** | `solution` |
| **LogicalCollectionName** | `solutions` |
| **PrimaryIdAttribute** | `solutionid` |
| **PrimaryNameAttribute** |`friendlyname` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConfigurationPageId](#BKMK_ConfigurationPageId)
- [Description](#BKMK_Description)
- [EnabledForSourceControlIntegration](#BKMK_EnabledForSourceControlIntegration)
- [FriendlyName](#BKMK_FriendlyName)
- [PublisherId](#BKMK_PublisherId)
- [SolutionId](#BKMK_SolutionId)
- [SolutionPackageVersion](#BKMK_SolutionPackageVersion)
- [SolutionType](#BKMK_SolutionType)
- [SourceControlSyncStatus](#BKMK_SourceControlSyncStatus)
- [TemplateSuffix](#BKMK_TemplateSuffix)
- [Thumbprint](#BKMK_Thumbprint)
- [UniqueName](#BKMK_UniqueName)
- [Version](#BKMK_Version)

### <a name="BKMK_ConfigurationPageId"></a> ConfigurationPageId

|Property|Value|
|---|---|
|Description|**A link to an optional configuration page for this solution.**|
|DisplayName|**Configuration Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`configurationpageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|webresource|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the solution.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_EnabledForSourceControlIntegration"></a> EnabledForSourceControlIntegration

|Property|Value|
|---|---|
|Description|**Indicates if solution is enabled for source control integration**|
|DisplayName|**Enabled for Source Control Integration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enabledforsourcecontrolintegration`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`solution_enabledforsourcecontrolintegration`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_FriendlyName"></a> FriendlyName

|Property|Value|
|---|---|
|Description|**User display name for the solution.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`friendlyname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|256|

### <a name="BKMK_PublisherId"></a> PublisherId

|Property|Value|
|---|---|
|Description|**Unique identifier of the publisher.**|
|DisplayName|**Publisher**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publisherid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|publisher|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the solution.**|
|DisplayName|**Solution Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionPackageVersion"></a> SolutionPackageVersion

|Property|Value|
|---|---|
|Description|**Solution package source organization version**|
|DisplayName|**Solution Package Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionpackageversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SolutionType"></a> SolutionType

|Property|Value|
|---|---|
|Description|**Solution Type**|
|DisplayName|**Solution Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutiontype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`solution_solutiontype`|

#### SolutionType Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Snapshot**|
|2|**Internal**|

### <a name="BKMK_SourceControlSyncStatus"></a> SourceControlSyncStatus

|Property|Value|
|---|---|
|Description|**Indicates the current status of source control integration**|
|DisplayName|**Source Control Sync Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcecontrolsyncstatus`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`solution_sourcecontrolsyncstatus`|

#### SourceControlSyncStatus Choices/Options

|Value|Label|
|---|---|
|0|**Not started**|
|1|**Initial sync in progress**|
|2|**Errors in initial sync**|
|3|**Pending changes to be committed**|
|4|**Committed**|

### <a name="BKMK_TemplateSuffix"></a> TemplateSuffix

|Property|Value|
|---|---|
|Description|**The template suffix of this solution**|
|DisplayName|**Suffix**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`templatesuffix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65|

### <a name="BKMK_Thumbprint"></a> Thumbprint

|Property|Value|
|---|---|
|Description|**thumbprint of the solution signature**|
|DisplayName|**Thumbprint**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`thumbprint`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65|

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**The unique name of this solution**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65|

### <a name="BKMK_Version"></a> Version

|Property|Value|
|---|---|
|Description|**Solution version, used to identify a solution for upgrades and hotfixes.**|
|DisplayName|**Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [FileId](#BKMK_FileId)
- [InstalledOn](#BKMK_InstalledOn)
- [IsApiManaged](#BKMK_IsApiManaged)
- [IsInternal](#BKMK_IsInternal)
- [IsManaged](#BKMK_IsManaged)
- [IsVisible](#BKMK_IsVisible)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [ParentSolutionId](#BKMK_ParentSolutionId)
- [PinpointAssetId](#BKMK_PinpointAssetId)
- [PinpointPublisherId](#BKMK_PinpointPublisherId)
- [PinpointSolutionDefaultLocale](#BKMK_PinpointSolutionDefaultLocale)
- [PinpointSolutionId](#BKMK_PinpointSolutionId)
- [PublisherIdOptionValuePrefix](#BKMK_PublisherIdOptionValuePrefix)
- [PublisherIdPrefix](#BKMK_PublisherIdPrefix)
- [UpdatedOn](#BKMK_UpdatedOn)
- [UpgradeInfo](#BKMK_UpgradeInfo)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the solution.**|
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
|Description|**Date and time when the solution was created.**|
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
|Description|**Unique identifier of the delegate user who created the solution.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_FileId"></a> FileId

|Property|Value|
|---|---|
|Description|**File Id for the blob url used for file storage.**|
|DisplayName|**File Id**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`fileid`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|128000|

### <a name="BKMK_InstalledOn"></a> InstalledOn

|Property|Value|
|---|---|
|Description|**Date and time when the solution was installed/upgraded.**|
|DisplayName|**Installed On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`installedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_IsApiManaged"></a> IsApiManaged

|Property|Value|
|---|---|
|Description|**Information about whether the solution is api managed.**|
|DisplayName|**Is Api Managed Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isapimanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`solution_isapimanaged`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsInternal"></a> IsInternal

|Property|Value|
|---|---|
|Description|**Indicates whether the solution is internal or not.**|
|DisplayName|**Is internal solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`isinternal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solution_isinternal`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution is managed or unmanaged.**|
|DisplayName|**Package Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solution_ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_IsVisible"></a> IsVisible

|Property|Value|
|---|---|
|Description|**Indicates whether the solution is visible outside of the platform.**|
|DisplayName|**Is Visible Outside Platform**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvisible`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solution_isvisible`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the solution.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the solution was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who modified the solution.**|
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
|Description|**Unique identifier of the organization associated with the solution.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_ParentSolutionId"></a> ParentSolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent solution. Should only be non-null if this solution is a patch.**|
|DisplayName|**Parent Solution**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentsolutionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|solution|

### <a name="BKMK_PinpointAssetId"></a> PinpointAssetId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pinpointassetid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_PinpointPublisherId"></a> PinpointPublisherId

|Property|Value|
|---|---|
|Description|**Identifier of the publisher of this solution in Microsoft Pinpoint.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pinpointpublisherid`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_PinpointSolutionDefaultLocale"></a> PinpointSolutionDefaultLocale

|Property|Value|
|---|---|
|Description|**Default locale of the solution in Microsoft Pinpoint.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pinpointsolutiondefaultlocale`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|16|

### <a name="BKMK_PinpointSolutionId"></a> PinpointSolutionId

|Property|Value|
|---|---|
|Description|**Identifier of the solution in Microsoft Pinpoint.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pinpointsolutionid`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_PublisherIdOptionValuePrefix"></a> PublisherIdOptionValuePrefix

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publisheridoptionvalueprefix`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_PublisherIdPrefix"></a> PublisherIdPrefix

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publisheridprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_UpdatedOn"></a> UpdatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the solution was updated.**|
|DisplayName|**Updated On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`updatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_UpgradeInfo"></a> UpgradeInfo

|Property|Value|
|---|---|
|Description|**Contains component info for the solution upgrade operation**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`upgradeinfo`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [fileattachment_solution_fileid](#BKMK_fileattachment_solution_fileid)
- [lk_solution_createdby](#BKMK_lk_solution_createdby)
- [lk_solution_modifiedby](#BKMK_lk_solution_modifiedby)
- [lk_solutionbase_createdonbehalfby](#BKMK_lk_solutionbase_createdonbehalfby)
- [lk_solutionbase_modifiedonbehalfby](#BKMK_lk_solutionbase_modifiedonbehalfby)
- [organization_solution](#BKMK_organization_solution)
- [publisher_solution](#BKMK_publisher_solution)
- [solution_configuration_webresource](#BKMK_solution_configuration_webresource)
- [solution_parent_solution](#BKMK_solution_parent_solution-many-to-one)

### <a name="BKMK_fileattachment_solution_fileid"></a> fileattachment_solution_fileid

One-To-Many Relationship: [fileattachment fileattachment_solution_fileid](fileattachment.md#BKMK_fileattachment_solution_fileid)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`fileid`|
|ReferencingEntityNavigationPropertyName|`fileid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solution_createdby"></a> lk_solution_createdby

One-To-Many Relationship: [systemuser lk_solution_createdby](systemuser.md#BKMK_lk_solution_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solution_modifiedby"></a> lk_solution_modifiedby

One-To-Many Relationship: [systemuser lk_solution_modifiedby](systemuser.md#BKMK_lk_solution_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutionbase_createdonbehalfby"></a> lk_solutionbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_solutionbase_createdonbehalfby](systemuser.md#BKMK_lk_solutionbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutionbase_modifiedonbehalfby"></a> lk_solutionbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_solutionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_solutionbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_solution"></a> organization_solution

One-To-Many Relationship: [organization organization_solution](organization.md#BKMK_organization_solution)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_publisher_solution"></a> publisher_solution

One-To-Many Relationship: [publisher publisher_solution](publisher.md#BKMK_publisher_solution)

|Property|Value|
|---|---|
|ReferencedEntity|`publisher`|
|ReferencedAttribute|`publisherid`|
|ReferencingAttribute|`publisherid`|
|ReferencingEntityNavigationPropertyName|`publisherid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_solution_configuration_webresource"></a> solution_configuration_webresource

One-To-Many Relationship: [webresource solution_configuration_webresource](webresource.md#BKMK_solution_configuration_webresource)

|Property|Value|
|---|---|
|ReferencedEntity|`webresource`|
|ReferencedAttribute|`webresourceid`|
|ReferencingAttribute|`configurationpageid`|
|ReferencingEntityNavigationPropertyName|`configurationpageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solution_parent_solution-many-to-one"></a> solution_parent_solution

One-To-Many Relationship: [solution solution_parent_solution](#BKMK_solution_parent_solution-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`parentsolutionid`|
|ReferencingEntityNavigationPropertyName|`parentsolutionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [FileAttachment_Solution](#BKMK_FileAttachment_Solution)
- [FK_CanvasApp_Solution](#BKMK_FK_CanvasApp_Solution)
- [solution_fieldpermission](#BKMK_solution_fieldpermission)
- [solution_fieldsecurityprofile](#BKMK_solution_fieldsecurityprofile)
- [solution_parent_solution](#BKMK_solution_parent_solution-one-to-many)
- [solution_privilege](#BKMK_solution_privilege)
- [solution_role](#BKMK_solution_role)
- [solution_roleprivileges](#BKMK_solution_roleprivileges)
- [solution_solutioncomponent](#BKMK_solution_solutioncomponent)
- [Solution_SyncErrors](#BKMK_Solution_SyncErrors)
- [user_settings_preferred_solution](#BKMK_user_settings_preferred_solution)

### <a name="BKMK_FileAttachment_Solution"></a> FileAttachment_Solution

Many-To-One Relationship: [fileattachment FileAttachment_Solution](fileattachment.md#BKMK_FileAttachment_Solution)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`regardingobjectid_fileattachment_solution`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FK_CanvasApp_Solution"></a> FK_CanvasApp_Solution

Many-To-One Relationship: [canvasapp FK_CanvasApp_Solution](canvasapp.md#BKMK_FK_CanvasApp_Solution)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`solutionid`|
|ReferencedEntityNavigationPropertyName|`FK_CanvasApp_Solution`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_fieldpermission"></a> solution_fieldpermission

Many-To-One Relationship: [fieldpermission solution_fieldpermission](fieldpermission.md#BKMK_solution_fieldpermission)

|Property|Value|
|---|---|
|ReferencingEntity|`fieldpermission`|
|ReferencingAttribute|`solutionid`|
|ReferencedEntityNavigationPropertyName|`solution_fieldpermission`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_fieldsecurityprofile"></a> solution_fieldsecurityprofile

Many-To-One Relationship: [fieldsecurityprofile solution_fieldsecurityprofile](fieldsecurityprofile.md#BKMK_solution_fieldsecurityprofile)

|Property|Value|
|---|---|
|ReferencingEntity|`fieldsecurityprofile`|
|ReferencingAttribute|`solutionid`|
|ReferencedEntityNavigationPropertyName|`solution_fieldsecurityprofile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_parent_solution-one-to-many"></a> solution_parent_solution

Many-To-One Relationship: [solution solution_parent_solution](#BKMK_solution_parent_solution-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`solution`|
|ReferencingAttribute|`parentsolutionid`|
|ReferencedEntityNavigationPropertyName|`solution_parent_solution`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_privilege"></a> solution_privilege

Many-To-One Relationship: [privilege solution_privilege](privilege.md#BKMK_solution_privilege)

|Property|Value|
|---|---|
|ReferencingEntity|`privilege`|
|ReferencingAttribute|`solutionid`|
|ReferencedEntityNavigationPropertyName|`solution_privilege`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_role"></a> solution_role

Many-To-One Relationship: [role solution_role](role.md#BKMK_solution_role)

|Property|Value|
|---|---|
|ReferencingEntity|`role`|
|ReferencingAttribute|`solutionid`|
|ReferencedEntityNavigationPropertyName|`solution_role`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_roleprivileges"></a> solution_roleprivileges

Many-To-One Relationship: [roleprivileges solution_roleprivileges](roleprivileges.md#BKMK_solution_roleprivileges)

|Property|Value|
|---|---|
|ReferencingEntity|`roleprivileges`|
|ReferencingAttribute|`solutionid`|
|ReferencedEntityNavigationPropertyName|`solution_roleprivileges`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_solutioncomponent"></a> solution_solutioncomponent

Many-To-One Relationship: [solutioncomponent solution_solutioncomponent](solutioncomponent.md#BKMK_solution_solutioncomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponent`|
|ReferencingAttribute|`solutionid`|
|ReferencedEntityNavigationPropertyName|`solution_solutioncomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Solution_SyncErrors"></a> Solution_SyncErrors

Many-To-One Relationship: [syncerror Solution_SyncErrors](syncerror.md#BKMK_Solution_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Solution_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_user_settings_preferred_solution"></a> user_settings_preferred_solution

Many-To-One Relationship: [usersettings user_settings_preferred_solution](usersettings.md#BKMK_user_settings_preferred_solution)

|Property|Value|
|---|---|
|ReferencingEntity|`usersettings`|
|ReferencingAttribute|`preferredsolution`|
|ReferencedEntityNavigationPropertyName|`user_settings_preferred_solution`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_package_solution"></a> package_solution

See [package package_solution Many-To-Many Relationship](package.md#BKMK_package_solution)

|Property|Value|
|---|---|
|IntersectEntityName|`package_solution`|
|IsCustomizable|False|
|SchemaName|`package_solution`|
|IntersectAttribute|`solutionid`|
|NavigationPropertyName|`package_solution`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.solution?displayProperty=fullName>
