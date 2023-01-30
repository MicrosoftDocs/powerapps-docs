---
title: "Virtual Entity Data Provider (EntityDataProvider)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Virtual Entity Data Provider (EntityDataProvider)  table/entity."
ms.date: 12/07/2022
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Virtual Entity Data Provider (EntityDataProvider)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Developers can register plug-ins on a data provider to enable data access for virtual entities in the system.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.2/entitydataproviders<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.2/entitydataproviders(*entitydataproviderid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.2/entitydataproviders(*entitydataproviderid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.2/entitydataproviders<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.2/entitydataproviders(*entitydataproviderid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|EntityDataProviders|
|DisplayCollectionName|Virtual Entity Data Providers|
|DisplayName|Virtual Entity Data Provider|
|EntitySetName|entitydataproviders|
|IsBPFEntity|False|
|LogicalCollectionName|entitydataproviders|
|LogicalName|entitydataprovider|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|entitydataproviderid|
|PrimaryNameAttribute|name|
|SchemaName|EntityDataProvider|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ArchivePlugin](#BKMK_ArchivePlugin)
- [BulkArchivePlugin](#BKMK_BulkArchivePlugin)
- [CreateMultiplePlugin](#BKMK_CreateMultiplePlugin)
- [CreatePlugin](#BKMK_CreatePlugin)
- [DataSourceLogicalName](#BKMK_DataSourceLogicalName)
- [DeleteMultiplePlugin](#BKMK_DeleteMultiplePlugin)
- [DeletePlugin](#BKMK_DeletePlugin)
- [Description](#BKMK_Description)
- [EntityDataProviderId](#BKMK_EntityDataProviderId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Name](#BKMK_Name)
- [PurgeArchivedContentPlugin](#BKMK_PurgeArchivedContentPlugin)
- [RetrieveEntityChangesPlugin](#BKMK_RetrieveEntityChangesPlugin)
- [RetrieveMultiplePlugin](#BKMK_RetrieveMultiplePlugin)
- [RetrievePlugin](#BKMK_RetrievePlugin)
- [UpdateMultiplePlugin](#BKMK_UpdateMultiplePlugin)
- [UpdatePlugin](#BKMK_UpdatePlugin)
- [UpsertMultiplePlugin](#BKMK_UpsertMultiplePlugin)
- [UpsertPlugin](#BKMK_UpsertPlugin)
- [ValidateArchiveConfigPlugin](#BKMK_ValidateArchiveConfigPlugin)


### <a name="BKMK_ArchivePlugin"></a> ArchivePlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the archiveplugin id that should be run when Archive is invoked|
|DisplayName|Contains the archiveplugin id that should be run when Archive is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|archiveplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_BulkArchivePlugin"></a> BulkArchivePlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the bulkarchiveplugin id that should be run when BulkArchive is invoked|
|DisplayName|Contains the bulkarchiveplugin id that should be run when BulkArchive is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|bulkarchiveplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_CreateMultiplePlugin"></a> CreateMultiplePlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the createmultipleplugin id that should be run when CreateMultiple is invoked|
|DisplayName|Contains the createmultipleplugin id that should be run when CreateMultiple is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createmultipleplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_CreatePlugin"></a> CreatePlugin

|Property|Value|
|--------|-----|
|Description|Create Plugin|
|DisplayName|Create Plugin|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_DataSourceLogicalName"></a> DataSourceLogicalName

|Property|Value|
|--------|-----|
|Description|When creating a Data Provider, the end user must select the name of the Data Source entity that will be created for the provider.|
|DisplayName|Data Source Entity Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|datasourcelogicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DeleteMultiplePlugin"></a> DeleteMultiplePlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the deletemultipleplugin id that should be run when DeleteMultiple is invoked|
|DisplayName|Contains the deletemultipleplugin id that should be run when DeleteMultiple is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|deletemultipleplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_DeletePlugin"></a> DeletePlugin

|Property|Value|
|--------|-----|
|Description|Delete Plugin|
|DisplayName|Delete Plugin|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|deleteplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|What is this Data Provider used for and data store technologies does it target?|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityDataProviderId"></a> EntityDataProviderId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data provider.|
|DisplayName|Data Provider|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entitydataproviderid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the form is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of this Data Provider. This is the name that appears in the dropdown when creating a new entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PurgeArchivedContentPlugin"></a> PurgeArchivedContentPlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the purgearchivedcontentplugin id that should be run when PurgeArchivedContent is invoked|
|DisplayName|Contains the purgearchivedcontentplugin id that should be run when PurgeArchivedContent is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|purgearchivedcontentplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RetrieveEntityChangesPlugin"></a> RetrieveEntityChangesPlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the retrieveentitychangesplugin id that should be run when RetrieveEntityChanges is invoked|
|DisplayName|Contains the retrieveentitychangesplugin id that should be run when RetrieveEntityChanges is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|retrieveentitychangesplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RetrieveMultiplePlugin"></a> RetrieveMultiplePlugin

|Property|Value|
|--------|-----|
|Description|MultipleRetrieve Plugin|
|DisplayName|MultipleRetrieve Plugin|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|retrievemultipleplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RetrievePlugin"></a> RetrievePlugin

|Property|Value|
|--------|-----|
|Description|Retrieve Plugin|
|DisplayName|Retrieve Plugin|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|retrieveplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_UpdateMultiplePlugin"></a> UpdateMultiplePlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the updatemultipleplugin id that should be run when UpdateMultiple is invoked|
|DisplayName|Contains the updatemultipleplugin id that should be run when UpdateMultiple is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|updatemultipleplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_UpdatePlugin"></a> UpdatePlugin

|Property|Value|
|--------|-----|
|Description|Update Plugin|
|DisplayName|Update Plugin|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|updateplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_UpsertMultiplePlugin"></a> UpsertMultiplePlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the upsertmultipleplugin id that should be run when UpsertMultiple is invoked|
|DisplayName|Contains the upsertmultipleplugin id that should be run when UpsertMultiple is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|upsertmultipleplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_UpsertPlugin"></a> UpsertPlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the upsertplugin id that should be run when Upsert is invoked|
|DisplayName|Contains the upsertplugin id that should be run when Upsert is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|upsertplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ValidateArchiveConfigPlugin"></a> ValidateArchiveConfigPlugin

**Added by**: EntityDataProviderExtensions Solution

|Property|Value|
|--------|-----|
|Description|Contains the validatearchiveconfigplugin id that should be run when ValidateArchiveConfig is invoked|
|DisplayName|Contains the validatearchiveconfigplugin id that should be run when ValidateArchiveConfig is invoked|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|validatearchiveconfigplugin|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [EntityDataProviderIdUnique](#BKMK_EntityDataProviderIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_EntityDataProviderIdUnique"></a> EntityDataProviderIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entitydataprovideridunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization.|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.


### <a name="BKMK_organization_entitydataprovider"></a> organization_entitydataprovider

See the [organization_entitydataprovider](organization.md#BKMK_organization_entitydataprovider) one-to-many relationship for the [organization](organization.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.entitydataprovider?text=entitydataprovider EntityType" />