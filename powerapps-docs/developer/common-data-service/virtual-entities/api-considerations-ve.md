---
title: "API considerations of virtual entities (Developer Guide for Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: d329dade-16c5-46e9-8dec-4b8efb996dea
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---

# API considerations of virtual entities

[!INCLUDE[](../../includes/cc_applies_to_update_9_0_0.md)]

There are two broad categories of changes to the metadata system that are associated with the introduction of virtual entities in [!INCLUDE[pn-crm-9-0-0-online](../../includes/pn-crm-9-0-0-online.md)]:

* Addition of a new assembly, namespaces, classes and other types to support development of custom virtual entity data providers
* Changes to the core platform, including a few additional properties to support external data source mapping, and modification of behaviors of existing entity and attribute properties that reflect the limitations of the initial implementation of this feature

## New Dynamics 365 Data SDK assembly

The Dynamics 365 Data SDK assembly, `Microsoft.Xrm.Sdk.Data.dll`, contains types to aid in the creation of custom virtual entity data providers. It is comprised of the following namespaces:

|Namespace|Description|
|---------|---------|
|Microsoft.Xrm.Sdk.Data|Base namespace that contains a few common types, such as the **AllowedQueryOptions** enumeration|
|Microsoft.Xrm.Sdk.Data.CodeGen|Contains classes and interfaces that support dynamic reflection, type matching, and code generation.  Mainly used by the internal provider engine.|
|Microsoft.Xrm.Sdk.Data.Converters|A set of classes to convert standard XRM types to their corresponding .NET fundamental types|
|Microsoft.Xrm.Sdk.Data.Exceptions|A set of exception classes that represent errors that can occur during runtime value resolution.  All are derived from Microsoft.Xrm.Sdk.SdkExceptionBase.|
|Microsoft.Xrm.Sdk.Data.Expressions|Classes to assist in implementing the supported query transformations, such as FILTER, JOIN, and ORDER.|
|Microsoft.Xrm.Sdk.Data.Infra|A few miscellaneous classes that support the central query processing.|
|Microsoft.Xrm.Sdk.Data.Mappings|Classes and interfaces that build the mapping from virtual entity metadata types to external types.|
|Microsoft.Xrm.Sdk.Data.Visitors|Classes that implement the [visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern) to perform specific operations on the **QueryExpression** parameter passed to the data provider during **RetrieveMultiple** requests. Provides specific support for both generic query and LINQ-baseed processing. These classes are derived from Microsoft.Xrm.Sdk.Query.QueryExpressionVisitorBase.|
| | |
 
<!-- TODO: Need to put in links to reference sections for these namespaces after TOC is completed. -->

This assembly is distributed with the Dynamics 365 Data SDK, which is also available as a NuGet package.
<!-- TODO: Will the SDK be downloadable separately? When the final package is ready, put in proper name and link. -->

## Changes to the core platform

The following changes to the standard [!INCLUDE[pn-dynamics365](../../includes/pn-dynamics-365.md)] reference types were introduced to support virtual entities.

### New Web API types

The Dynamics 365 Web API exposes virtual entity data providers and sources as the following new entity types: [EntityDataProvider](../entities/entitydataprovider.md) and [EntityDataSource](../entities/entitydatasource.md). 

### New metadata properties

Four new properties were added to the **Microsoft.Xrm.Sdk.Metadata.EntityMetadata** class:

* **DataProviderId** - GUID that identifies the associated virtual entity data provider
* **DataSourceId** - GUID that identifies the associated virtual entity data source
* **ExternalName** - Name for this type in the external data source
* **ExternalCollectionName** - Plural name for this type, used in the UI and to support OData access

Two new properties were added to the **Microsoft.Xrm.Sdk.Metadata.AttributeMetadata** class:

* **ExternalName** - Name of the type in the external data source
* **IsDataSourceSecret** - Indicates whether the field contains sensitive information

The **ExternalName** property was also added to the **Option** and **OptionSetMetadata** classes. These external names assist in the external data source mapping, by specifiying the name of the associated type in the external data source. These properties are only used for virtual entities; for a builtin or standard custom entity type, these external names must be `null`.


### Virtual entity creation

The approach to programmatically creating a virtual entity type differs slightly from a standard custom entity type creation in that:

* If the associated data provider (and optionally data source) is known at creation time, then these are specified.
* If the data provider for this type is not known, then at minimum, `EntityMetadata.DataProviderId` is set to `7015A531-CC0D-4537-B5F2-C882A1EB65AD`, and the `EntityMetadata.DataSourceId` is set to `null`. Before instances of this type are used at runtime, these properties must be assigned appropriate values.

Two new entity types, [EntityDataProvider](../entities/entitydataprovider.md) and optionally [EntityDataSource](../entities/entitydatasource.md), will be created when you register a plugin, and their respective ID's, **entitydataproviderid** and **entitydatasourceid**, represent these required GUIDs. (Otherwise, developers rarely need to access these custom types directly.) Note that DataSource contains the property **entitydataproviderid** that must match the corresponding DataProvider type or a runtime exception will be thrown.

> [!WARNING]
> Standard (non-virtual) entities must have the values of their associated **EntityMetadata.DataProviderId** and **EntityMetadata.DataSourceId** set to their default values (`null`), otherwise a runtime exception will be thrown.  Once created, you cannot convert from a non-virtual type to a virtual type, or the reverse. 

### Entity metadata property behavior changes

The following table details how the behavior of standard [EntityMetadata properties](https://msdn.microsoft.com/library/microsoft.xrm.sdk.metadata.entitymetadata_properties.aspx) are modified when applied to virtual entities. Some properties are not valid for virtual entities, whereas others are limited in scope or value.

<!-- TODO: Above link URL needs to be changed to docs.microsoft.com -->

|**Metadata Property**|**Applies?**|**Notes**|
|---------------------|------------|---------|
|ActivityTypeMask|_invalid_|Always 0|
|Attributes|valid||
|AutoCreateAccessTeams|_invalid_|Always false|
|AutoRouteToOwnerQueue|_invalid_|Always false, queues are not supported.|
|CanBeInManyToMany|valid||
|CanBePrimaryEntityInRelationship|valid||
|CanBeRelatedEntityInRelationship|valid||
|CanChangeHierarchicalRelationship|_invalid_|Always false, hierarchical relationships are not supported.|
|CanChangeTrackingBeEnabled|_invalid_|Always false, change tracking and auditing values are not supported.|
|CanCreateAttributes|valid||
|CanCreateCharts|_invalid_|Always false|
|CanCreateForms|valid||
|CanCreateViews|valid||
|CanEnableSyncToExternalSearchIndex|_invalid_|Always false|
|CanModifyAdditionalSettings|valid||
|CanTriggerWorkflow|_invalid_|Always false, workflows cannot be triggered.
|ChangeTrackingEnabled|_invalid_|Always false|
|CollectionSchemaName|valid||
|DaysSinceRecordLastModified|_invalid_|Always null or 0|
|Description|valid||
|DisplayCollectionName|valid||
|DisplayName|valid||
|EnforceStateTransitions|_invalid_|StateCode and Status are not supported.|
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
|IsActivity|_invalid_|Always false, activities are not supported.|
|IsActivityParty|_invalid_|Always false|
|IsAIRUpdated|_invalid_|Deprecated|
|IsAuditEnabled|_invalid_|Always false, auditing is not supported.|
|IsAvailableOffline|_invalid_|Always false, offline use is not supported.|
|IsBusinessProcessEnabled|_invalid_|Always false, business processes are not supported.|
|IsChildEntity|_invalid_|Always false, all virtual entity are organizationally owned.|
|IsConnectionsEnabled|valid|<!-- TODO: Connection support is still TBD for Potassium -->|
|IsCustomEntity|valid||
|IsCustomizable|valid||
|IsDocumentManagementEnabled|valid||
|IsDocumentRecommendationsEnabled|_invalid_|Always false, this new feature is not supported.|
|IsDuplicateDetectionEnabled|_invalid_|Always false, but duplicate detection can be performed at the data source.|
|IsEnabledForCharts|_limited_|Only for supported Fetch clauses.|
|IsEnabledForTrace|valid||
|IsImportable|valid|<!--TODO: May have limitations. -->|
|IsInteractionCentricEnabled|valid||
|IsIntersect|valid||
|IsKnowledgeManagementEnabled|_invalid_|Always false, knowledge management integration is not supported.|
|IsMailMergeEnabled|valid||
|IsManaged|valid||
|IsMappable|valid||
|IsOfflineInMobileClient|_invalid_|Always false, virtual entity values are not cached for offline use.|
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
|Keys|_invalid_|Alternate keys are not supported|
|LogicalCollectionName|valid||
|LogicalName|valid||
|ManyToManyRelationships|valid||
|ManyToOneRelationships|valid| Not supported between two virtual entities. |
|MetadataId|valid||
|MobileOfflineFilters|_invalid_|Always false, offline use is not supported.|
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
||||

<!-- TODO: Add links to reference properties in first column. -->


### Attribute metadata property behavior changes

The following table explains how the behavior of standard [AttributeMetadata properties]( https://msdn.microsoft.com/en-us/library/microsoft.xrm.sdk.metadata.attributemetadata_properties.aspx) are modified when applied to virtual entities. Some properties are not valid for virtual entities, whereas others are limited in scope or value.

<!-- TODO: Above link URL needs to be changed to docs.microsoft.com -->

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
|IsAuditEnabled|_invalid_|Always false, auditing is not supported.|
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
|IsSecured|_invalid_|Always false, field-level security is not supported.|
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
|SourceType|_invalid_|Always 0, calculated or rollup values not supported.|
||||

