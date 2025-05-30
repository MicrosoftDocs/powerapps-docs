---
title: "Virtual Entity Data Provider (EntityDataProvider) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Virtual Entity Data Provider (EntityDataProvider) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Virtual Entity Data Provider (EntityDataProvider) table/entity reference (Microsoft Dataverse)

Developers can register plug-ins on a data provider to enable data access for virtual entities in the system.

## Messages

The following table lists the messages for the Virtual Entity Data Provider (EntityDataProvider) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /entitydataproviders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /entitydataproviders(*entitydataproviderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /entitydataproviders(*entitydataproviderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /entitydataproviders<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /entitydataproviders(*entitydataproviderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /entitydataproviders(*entitydataproviderid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Virtual Entity Data Provider (EntityDataProvider) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Virtual Entity Data Provider** |
| **DisplayCollectionName** | **Virtual Entity Data Providers** |
| **SchemaName** | `EntityDataProvider` |
| **CollectionSchemaName** | `EntityDataProviders` |
| **EntitySetName** | `entitydataproviders`|
| **LogicalName** | `entitydataprovider` |
| **LogicalCollectionName** | `entitydataproviders` |
| **PrimaryIdAttribute** | `entitydataproviderid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ArchivePlugin](#BKMK_ArchivePlugin)
- [BulkArchivePlugin](#BKMK_BulkArchivePlugin)
- [BulkRetainPlugin](#BKMK_BulkRetainPlugin)
- [CreateMultiplePlugin](#BKMK_CreateMultiplePlugin)
- [CreatePlugin](#BKMK_CreatePlugin)
- [DataSourceLogicalName](#BKMK_DataSourceLogicalName)
- [DeleteMultiplePlugin](#BKMK_DeleteMultiplePlugin)
- [DeletePlugin](#BKMK_DeletePlugin)
- [Description](#BKMK_Description)
- [EntityDataProviderId](#BKMK_EntityDataProviderId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [LookupExpansionEnabled](#BKMK_LookupExpansionEnabled)
- [Name](#BKMK_Name)
- [PurgeArchivedContentPlugin](#BKMK_PurgeArchivedContentPlugin)
- [PurgeRetainedContentPlugin](#BKMK_PurgeRetainedContentPlugin)
- [RetainPlugin](#BKMK_RetainPlugin)
- [RetrieveEntityChangesPlugin](#BKMK_RetrieveEntityChangesPlugin)
- [RetrieveMultiplePlugin](#BKMK_RetrieveMultiplePlugin)
- [RetrievePlugin](#BKMK_RetrievePlugin)
- [RollbackRetainPlugin](#BKMK_RollbackRetainPlugin)
- [UpdateMultiplePlugin](#BKMK_UpdateMultiplePlugin)
- [UpdatePlugin](#BKMK_UpdatePlugin)
- [UpsertMultiplePlugin](#BKMK_UpsertMultiplePlugin)
- [UpsertPlugin](#BKMK_UpsertPlugin)
- [ValidateArchiveConfigPlugin](#BKMK_ValidateArchiveConfigPlugin)
- [ValidateRetentionConfigPlugin](#BKMK_ValidateRetentionConfigPlugin)

### <a name="BKMK_ArchivePlugin"></a> ArchivePlugin

|Property|Value|
|---|---|
|Description|**Contains the archiveplugin id that should be run when Archive is invoked**|
|DisplayName|**Contains the archiveplugin id that should be run when Archive is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`archiveplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_BulkArchivePlugin"></a> BulkArchivePlugin

|Property|Value|
|---|---|
|Description|**Contains the bulkarchiveplugin id that should be run when BulkArchive is invoked**|
|DisplayName|**Contains the bulkarchiveplugin id that should be run when BulkArchive is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bulkarchiveplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_BulkRetainPlugin"></a> BulkRetainPlugin

|Property|Value|
|---|---|
|Description|**Contains the bulkretainplugin id that should be run when BulkRetain is invoked**|
|DisplayName|**Contains the bulkretainplugin id that should be run when BulkRetain is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bulkretainplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_CreateMultiplePlugin"></a> CreateMultiplePlugin

|Property|Value|
|---|---|
|Description|**Contains the createmultipleplugin id that should be run when CreateMultiple is invoked**|
|DisplayName|**Contains the createmultipleplugin id that should be run when CreateMultiple is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createmultipleplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_CreatePlugin"></a> CreatePlugin

|Property|Value|
|---|---|
|Description|**Create Plugin**|
|DisplayName|**Create Plugin**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DataSourceLogicalName"></a> DataSourceLogicalName

|Property|Value|
|---|---|
|Description|**When creating a Data Provider, the end user must select the name of the Data Source entity that will be created for the provider.**|
|DisplayName|**Data Source Entity Logical Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`datasourcelogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_DeleteMultiplePlugin"></a> DeleteMultiplePlugin

|Property|Value|
|---|---|
|Description|**Contains the deletemultipleplugin id that should be run when DeleteMultiple is invoked**|
|DisplayName|**Contains the deletemultipleplugin id that should be run when DeleteMultiple is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deletemultipleplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DeletePlugin"></a> DeletePlugin

|Property|Value|
|---|---|
|Description|**Delete Plugin**|
|DisplayName|**Delete Plugin**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deleteplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**What is this Data Provider used for and data store technologies does it target?**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_EntityDataProviderId"></a> EntityDataProviderId

|Property|Value|
|---|---|
|Description|**Unique identifier of the data provider.**|
|DisplayName|**Data Provider**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entitydataproviderid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the form is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_LookupExpansionEnabled"></a> LookupExpansionEnabled

|Property|Value|
|---|---|
|Description|**Enables expansion support for lookups columns. Only applicable to RetrieveMultiple plugin. Enabling this might modify the filter expression supplied to RetrieveMultiple plugin. Default value is false.**|
|DisplayName|**LookupExpansionEnabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lookupexpansionenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_lookupexpansionenabled_entitydataprovider`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of this Data Provider. This is the name that appears in the dropdown when creating a new entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_PurgeArchivedContentPlugin"></a> PurgeArchivedContentPlugin

|Property|Value|
|---|---|
|Description|**Contains the purgearchivedcontentplugin id that should be run when PurgeArchivedContent is invoked**|
|DisplayName|**Contains the purgearchivedcontentplugin id that should be run when PurgeArchivedContent is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`purgearchivedcontentplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PurgeRetainedContentPlugin"></a> PurgeRetainedContentPlugin

|Property|Value|
|---|---|
|Description|**Contains the purgeretainedcontentplugin id that should be run when PurgeRetainedContent is invoked**|
|DisplayName|**Contains the purgeretainedcontentplugin id that should be run when PurgeRetainedContent is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`purgeretainedcontentplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RetainPlugin"></a> RetainPlugin

|Property|Value|
|---|---|
|Description|**Contains the retainplugin id that should be run when Retain is invoked**|
|DisplayName|**Contains the retainplugin id that should be run when Retain is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`retainplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RetrieveEntityChangesPlugin"></a> RetrieveEntityChangesPlugin

|Property|Value|
|---|---|
|Description|**Contains the retrieveentitychangesplugin id that should be run when RetrieveEntityChanges is invoked**|
|DisplayName|**Contains the retrieveentitychangesplugin id that should be run when RetrieveEntityChanges is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`retrieveentitychangesplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RetrieveMultiplePlugin"></a> RetrieveMultiplePlugin

|Property|Value|
|---|---|
|Description|**MultipleRetrieve Plugin**|
|DisplayName|**MultipleRetrieve Plugin**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`retrievemultipleplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RetrievePlugin"></a> RetrievePlugin

|Property|Value|
|---|---|
|Description|**Retrieve Plugin**|
|DisplayName|**Retrieve Plugin**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`retrieveplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RollbackRetainPlugin"></a> RollbackRetainPlugin

|Property|Value|
|---|---|
|Description|**Contains the rollbackretainplugin id that should be run when Rollback Retain is invoked**|
|DisplayName|**Contains the rollbackretainplugin id that should be run when Rollback Retain is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollbackretainplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_UpdateMultiplePlugin"></a> UpdateMultiplePlugin

|Property|Value|
|---|---|
|Description|**Contains the updatemultipleplugin id that should be run when UpdateMultiple is invoked**|
|DisplayName|**Contains the updatemultipleplugin id that should be run when UpdateMultiple is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`updatemultipleplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_UpdatePlugin"></a> UpdatePlugin

|Property|Value|
|---|---|
|Description|**Update Plugin**|
|DisplayName|**Update Plugin**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`updateplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_UpsertMultiplePlugin"></a> UpsertMultiplePlugin

|Property|Value|
|---|---|
|Description|**Contains the upsertmultipleplugin id that should be run when UpsertMultiple is invoked**|
|DisplayName|**Contains the upsertmultipleplugin id that should be run when UpsertMultiple is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upsertmultipleplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_UpsertPlugin"></a> UpsertPlugin

|Property|Value|
|---|---|
|Description|**Contains the upsertplugin id that should be run when Upsert is invoked**|
|DisplayName|**Contains the upsertplugin id that should be run when Upsert is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upsertplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ValidateArchiveConfigPlugin"></a> ValidateArchiveConfigPlugin

|Property|Value|
|---|---|
|Description|**Contains the validatearchiveconfigplugin id that should be run when ValidateArchiveConfig is invoked**|
|DisplayName|**Contains the validatearchiveconfigplugin id that should be run when ValidateArchiveConfig is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`validatearchiveconfigplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ValidateRetentionConfigPlugin"></a> ValidateRetentionConfigPlugin

|Property|Value|
|---|---|
|Description|**Contains the validateretentionconfigplugin id that should be run when ValidateRetentionConfig is invoked**|
|DisplayName|**Contains the validateretentionconfigplugin id that should be run when ValidateRetentionConfig is invoked**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`validateretentionconfigplugin`|
|RequiredLevel|None|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [EntityDataProviderIdUnique](#BKMK_EntityDataProviderIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_EntityDataProviderIdUnique"></a> EntityDataProviderIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entitydataprovideridunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization.**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

### <a name="BKMK_organization_entitydataprovider"></a> organization_entitydataprovider

One-To-Many Relationship: [organization organization_entitydataprovider](organization.md#BKMK_organization_entitydataprovider)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.entitydataprovider?displayProperty=fullName>
