---
title: "API considerations of virtual tables (Microsoft Dataverse) | Microsoft Docs"
description: "Describes API considerations of virtual tables"
ms.date: 02/11/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---

# API considerations for virtual tables

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Two broad categories of changes to the table definition system are associated with the introduction of virtual tables (also known as virtual entities) in Microsoft Dataverse:

- Addition of a new assembly, namespaces, classes, and other types to support development of custom virtual table data providers
- Changes to the core platform, including a few other properties to support external data source mapping, and modification of behaviors of existing table and column properties that reflect the limitations of the initial implementation of this feature

## Dynamics 365 Data SDK assembly

The Dynamics 365 Data SDK assembly, `Microsoft.Xrm.Sdk.Data.dll`, contains types to aid in the creation of custom virtual table data providers. It comprises the following namespaces:

|Namespace|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Data>|Base namespace that contains a few common types, such as the **AllowedQueryOptions** enumeration|
|<xref:Microsoft.Xrm.Sdk.Data.CodeGen>|Contains classes and interfaces that support dynamic reflection, type matching, and code generation.  Mainly used by the internal provider engine.|
|<xref:Microsoft.Xrm.Sdk.Data.Converters>|A set of classes to convert standard XRM types to their corresponding .NET fundamental types|
|<xref:Microsoft.Xrm.Sdk.Data.Exceptions>|A set of exception classes that represent errors that can occur during runtime value resolution.  All are derived from Microsoft.Xrm.Sdk.SdkExceptionBase.|
|<xref:Microsoft.Xrm.Sdk.Data.Expressions>|Classes to help implementing the supported query transformations, such as FILTER, JOIN, and ORDER.|
|<xref:Microsoft.Xrm.Sdk.Data.Mappings>|Classes and interfaces that build the mapping from virtual table definition types to external types.|
|Microsoft.Xrm.Sdk.Data.Visitors|Classes that implement the [visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern) to perform specific operations on the **QueryExpression** parameter passed to the data provider during **RetrieveMultiple** requests. Provides specific support for both generic query and LINQ-baseed processing. These classes are derived from Microsoft.Xrm.Sdk.Query.QueryExpressionVisitorBase.|

Distribute this assembly as a NuGet package: [Microsoft.CrmSdk.Data](https://www.nuget.org/packages/Microsoft.CrmSdk.Data/).

## Changes to the core platform

The following changes to the standard Dataverse reference types support virtual tables.

### New tables

Dataverse exposes virtual table data providers and sources as the following tables: [EntityDataProvider](../reference/entities/entitydataprovider.md) and `EntityDataSource`.

### New table definition properties

Four new properties were added to the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata> class:

|Property|Description|
|--|--|
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DataProviderId>|GUID that identifies the associated virtual table data provider|
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DataSourceId>|GUID that identifies the associated virtual table data source|
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ExternalName>|Name for this type in the external data source|
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ExternalCollectionName>|Plural name for this type, used in the UI and to support OData access|

Two new properties were added to the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> class:

|Property|Description|
|--|--|
|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.ExternalName>|Name of the type in the external data source|
|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsDataSourceSecret>|Indicates whether the field contains sensitive information|

The `ExternalName` property was also added to the <xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata> and <xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata> classes. These external names help the external data source mapping, by specifying the name of the associated type in the external data source. These properties are only used for virtual tables. For a built-in or standard custom entity type, these external names must be `null`.


### Virtual table creation

The approach to programmatically creating a virtual table type differs slightly from a standard custom entity type creation in that:

- If you know the associated data provider (and optionally data source) at creation time, specify these values.
- If you don't know the data provider for this type, set <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DataProviderId> to `7015A531-CC0D-4537-B5F2-C882A1EB65AD` and set <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DataSourceId> to `null`. Before you use instances of this type at runtime, assign these properties appropriate values.

When you register a plugin, you create two new tables, [EntityDataProvider](../reference/entities/entitydataprovider.md) and optionally `EntityDataSource`. Their respective IDs, `entitydataproviderid` and `entitydatasourceid`, represent these required GUIDs. (Otherwise, developers rarely need to access these custom types directly.) Note that DataSource contains the property `entitydataproviderid` that must match the corresponding DataProvider type or a runtime exception is thrown.

> [!WARNING]
> Standard (nonvirtual) tables must have the values of their associated `DataProviderId` and `DataSourceId` set to their default values (`null`), otherwise a runtime exception is thrown.  Once created, you can't convert from a nonvirtual type to a virtual type, or the reverse. 

### Table definition property behavior changes

The following table details how the behavior of standard [EntityMetadata properties](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata#properties) changes when you apply them to virtual tables. Some properties aren't valid for virtual tables, whereas others are limited in scope or value.

|**Metadata Property**|**Applies?**|**Notes**|
|---------------------|------------|---------|
|ActivityTypeMask|_invalid_|Always 0|
|Attributes|valid||
|AutoCreateAccessTeams|_invalid_|Always false|
|AutoRouteToOwnerQueue|_invalid_|Always false, queues aren't supported.|
|CanBeInManyToMany|valid||
|CanBePrimaryEntityInRelationship|valid||
|CanBeRelatedEntityInRelationship|valid||
|CanChangeHierarchicalRelationship|_invalid_|Always false, hierarchical relationships aren't supported.|
|CanChangeTrackingBeEnabled|_invalid_|Always false, change tracking, and auditing values aren't supported.|
|CanCreateAttributes|valid||
|CanCreateCharts|_invalid_|Always false|
|CanCreateForms|valid||
|CanCreateViews|valid||
|CanEnableSyncToExternalSearchIndex|_invalid_|Always false|
|CanModifyAdditionalSettings|valid||
|CanTriggerWorkflow|_invalid_|Always false, workflows can't be triggered.
|ChangeTrackingEnabled|_invalid_|Always false|
|CollectionSchemaName|valid||
|DaysSinceRecordLastModified|_invalid_|Always null or 0|
|Description|valid||
|DisplayCollectionName|valid||
|DisplayName|valid||
|EnforceStateTransitions|_invalid_|StateCode and Status aren't supported.|
|EntityColor|valid||
|EntityHelpUrl|valid||
|EntityHelpUrlEnabled|valid||
|EntitySetName|valid||
|ExtensionData|_invalid_|Deprecated property|
|HasChanged|valid||
|IconLargeName|valid||
|IconMediumName|valid||
|IconSmallName|valid||
|IntroducedVersion|valid||
|IsActivity|_invalid_|Always false, activities aren't supported.|
|IsActivityParty|_invalid_|Always false|
|IsAIRUpdated|_invalid_|Deprecated|
|IsAuditEnabled|_invalid_|Always false, auditing isn't supported.|
|IsAvailableOffline|_invalid_|Always false, offline use isn't supported.|
|IsBusinessProcessEnabled|_invalid_|Always false, business processes aren't supported.|
|IsChildEntity|_invalid_|Always false, all virtual tables are organizationally owned.|
|IsConnectionsEnabled|valid|<!-- TODO: Connection support is still TBD for Potassium -->|
|IsCustomEntity|valid||
|IsCustomizable|valid||
|IsDocumentManagementEnabled|valid||
|IsDocumentRecommendationsEnabled|_invalid_|Always false, this new feature isn't supported.|
|IsDuplicateDetectionEnabled|_invalid_|Always false, but duplicate detection can be performed at the data source.|
|IsEnabledForCharts|_limited_|Only for supported Fetch clauses.|
|IsEnabledForTrace|valid||
|IsImportable|valid|<!--TODO: May have limitations. -->|
|IsInteractionCentricEnabled|valid||
|IsIntersect|valid||
|IsKnowledgeManagementEnabled|_invalid_|Always false, knowledge management integration isn't supported.|
|IsMailMergeEnabled|valid||
|IsManaged|valid||
|IsMappable|valid||
|IsOfflineInMobileClient|_invalid_|Always false, virtual table values aren't cached for offline use.|
|IsOneNoteIntegrationEnabled|valid||
|IsOptimisticConcurrencyEnabled|_invalid_|Always false, concurrency must be implemented in the data source.|
|IsPrivate|valid||
|IsQuickCreateEnabled|valid||
|IsReadOnlyInMobileClient|valid||
|IsRenameable|valid||
|IsSLAEnabled|_invalid_|Always false|
|IsStateModelAware|_invalid_|<!-- TODO: TBD? -->|
|IsValidForAdvancedFind|valid||
|IsValidForQueue|valid||
|IsVisibleInMobile|valid||
|IsVisibleInMobileClient|valid||
|Keys|_invalid_|Alternate keys aren't supported|
|LogicalCollectionName|valid||
|LogicalName|valid||
|ManyToManyRelationships|valid||
|ManyToOneRelationships|valid| Not supported between two virtual tables. |
|MetadataId|valid||
|MobileOfflineFilters|_invalid_|Always false, offline use isn't supported.|
|ObjectTypeCode|valid||
|OneToManyRelationships|valid||
|OwnershipType|_invalid_|Always **OrganizationOwned**|
|PrimaryIdAttribute|valid||
|PrimaryImageAttribute|valid||
|PrimaryNameAttribute|valid||
|Privileges|_invalid_|<!-- TODO: TBD? -->|
|RecurrenceBaseEntityLogicalName|_invalid_||
|ReportViewName|_invalid_||
|SchemaName|valid||
|SyncToExternalSearchIndex|_invalid_||

<!-- TODO: Add links to reference properties in first column. -->


### Column definition property behavior changes

The following table explains how the behavior of standard [AttributeMetadata properties](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata#properties) changes when you apply them to virtual tables. Some properties aren't valid for virtual tables, whereas others have limited scope or value.

|**Metadata Property**|**Applies?**|**Notes**|
|---------------------|------------|---------|
|ColumnNumber|_invalid_||
|DeprecatedVersion|valid||
|Description|valid||
|DisplayName|valid||
|EntityLogicalName|valid||
|ExtensionData|_invalid_|<!-- TODO: TBD? -->|
|HasChanged|valid||
|InheritsFrom|valid||
|IntroducedVersion|valid||
|IsAuditEnabled|_invalid_|Always false, auditing isn't supported.|
|IsCustomAttribute|valid||
|IsCustomizable|valid||
|IsFilterable|valid||
|IsGlobalFilterEnabled|valid||
|IsLogical|valid||
|IsManaged|valid||
|IsPrimaryId|valid||
|IsPrimaryName|valid||
|IsRenameable|valid||
|IsSearchable|valid||
|IsSecured|_invalid_|Always false, field-level security isn't supported.|
|IsSortableEnabled|valid||
|IsValidForAdvancedFind|valid||
|IsValidForCreate|valid||
|IsValidForRead|valid||
|IsValidForUpdate|valid||
|LinkedAttributeId|valid||
|LogicalName|valid||
|MetadataId|valid||
|RequiredLevel|valid||
|SchemaName|valid||
|SourceType|_invalid_|Always 0, calculated or rollup values aren't supported.|

### See also

[Get started with virtual entities](get-started-ve.md)<br />
[Custom virtual table data providers](custom-ve-data-providers.md)<br />
[Sample: Generic virtual table data provider plug-in](sample-generic-ve-plugin.md)



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
