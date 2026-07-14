---
title: "Entity table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Entity table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Entity table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Entity table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: False |`GET` /entities<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Entity table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Entity** |
| **DisplayCollectionName** | **Entities** |
| **SchemaName** | `Entity` |
| **CollectionSchemaName** | `Entities` |
| **EntitySetName** | `entities`|
| **LogicalName** | `entity` |
| **LogicalCollectionName** | `entities` |
| **PrimaryIdAttribute** | `entityid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddressTableName](#BKMK_AddressTableName)
- [BaseTableName](#BKMK_BaseTableName)
- [CollectionName](#BKMK_CollectionName)
- [EntityId](#BKMK_EntityId)
- [EntitySetName](#BKMK_EntitySetName)
- [ExtensionTableName](#BKMK_ExtensionTableName)
- [ExternalCollectionName](#BKMK_ExternalCollectionName)
- [ExternalName](#BKMK_ExternalName)
- [LogicalCollectionName](#BKMK_LogicalCollectionName)
- [LogicalName](#BKMK_LogicalName)
- [Name](#BKMK_Name)
- [OriginalLocalizedCollectionName](#BKMK_OriginalLocalizedCollectionName)
- [OriginalLocalizedName](#BKMK_OriginalLocalizedName)
- [ParentControllingAttributeName](#BKMK_ParentControllingAttributeName)
- [PhysicalName](#BKMK_PhysicalName)
- [ReportViewName](#BKMK_ReportViewName)

### <a name="BKMK_AddressTableName"></a> AddressTableName

|Property|Value|
|---|---|
|Description|**The address table name of this entity.**|
|DisplayName|**Address Table Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`addresstablename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_BaseTableName"></a> BaseTableName

|Property|Value|
|---|---|
|Description|**The base table name of this entity.**|
|DisplayName|**Base Table Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`basetablename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_CollectionName"></a> CollectionName

|Property|Value|
|---|---|
|Description|**The collection name of this entity.**|
|DisplayName|**Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`collectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_EntityId"></a> EntityId

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity.**|
|DisplayName|**Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_EntitySetName"></a> EntitySetName

|Property|Value|
|---|---|
|Description|**The entity set name of this entity.**|
|DisplayName|**Entity Set Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitysetname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ExtensionTableName"></a> ExtensionTableName

|Property|Value|
|---|---|
|Description|**The extension table name of this entity.**|
|DisplayName|**Extension Table Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`extensiontablename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ExternalCollectionName"></a> ExternalCollectionName

|Property|Value|
|---|---|
|Description|**The external collection name of this entity.**|
|DisplayName|**External Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`externalcollectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ExternalName"></a> ExternalName

|Property|Value|
|---|---|
|Description|**The external name of this entity.**|
|DisplayName|**External Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`externalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_LogicalCollectionName"></a> LogicalCollectionName

|Property|Value|
|---|---|
|Description|**The logical collection name of this entity.**|
|DisplayName|**Logical Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logicalcollectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|---|---|
|Description|**The logical name of this entity.**|
|DisplayName|**Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of this Entity.**|
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
|MaxLength|128|

### <a name="BKMK_OriginalLocalizedCollectionName"></a> OriginalLocalizedCollectionName

|Property|Value|
|---|---|
|Description|**The original localized collection name of this entity.**|
|DisplayName|**Original Localized Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originallocalizedcollectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_OriginalLocalizedName"></a> OriginalLocalizedName

|Property|Value|
|---|---|
|Description|**The original localized name of this entity.**|
|DisplayName|**Original Localized Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originallocalizedname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ParentControllingAttributeName"></a> ParentControllingAttributeName

|Property|Value|
|---|---|
|Description|**The parent controlling attribute name of this entity.**|
|DisplayName|**Parent Controlling Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentcontrollingattributename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_PhysicalName"></a> PhysicalName

|Property|Value|
|---|---|
|Description|**The physical name of this entity.**|
|DisplayName|**Physical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`physicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ReportViewName"></a> ReportViewName

|Property|Value|
|---|---|
|Description|**The Report view name of this entity.**|
|DisplayName|**Report View Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reportviewname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [IsActivity](#BKMK_IsActivity)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [VersionNumber](#BKMK_VersionNumber)

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

### <a name="BKMK_IsActivity"></a> IsActivity

|Property|Value|
|---|---|
|Description|**Whether this entity is of type activity.**|
|DisplayName|**Is Activity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isactivity`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_entity_isactivity`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**The object type code of this entity.**|
|DisplayName|**Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**The version number of this entity.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [AIPluginOperation_Entity_Entity](#BKMK_AIPluginOperation_Entity_Entity)
- [catalogassignment_entity](#BKMK_catalogassignment_entity)
- [DVFileSearchEntity_Entity_Entity](#BKMK_DVFileSearchEntity_Entity_Entity)
- [DVTableSearchEntity_Entity_Entity](#BKMK_DVTableSearchEntity_Entity_Entity)
- [emailaddressconfiguration_entity_EntityId](#BKMK_emailaddressconfiguration_entity_EntityId)
- [entity_appaction_ContextEntity](#BKMK_entity_appaction_ContextEntity)
- [entity_appactionrule_ContextEntity](#BKMK_entity_appactionrule_ContextEntity)
- [entity_entityanalyticsconfig](#BKMK_entity_entityanalyticsconfig)
- [entity_sensitivitylabelattributemapping_EntityId](#BKMK_entity_sensitivitylabelattributemapping_EntityId)
- [entity_serviceplanmapping](#BKMK_entity_serviceplanmapping)
- [entity_solutioncomponentbatchconfiguration_PrimaryEntity](#BKMK_entity_solutioncomponentbatchconfiguration_PrimaryEntity)
- [entity_solutioncomponentbatchconfiguration_RelatedEntity](#BKMK_entity_solutioncomponentbatchconfiguration_RelatedEntity)
- [entity_solutioncomponentconfiguration](#BKMK_entity_solutioncomponentconfiguration)
- [entityclusterconfig_extensionofrecordid](#BKMK_entityclusterconfig_extensionofrecordid)
- [metadataforarchival_extensionofrecordid](#BKMK_metadataforarchival_extensionofrecordid)
- [msdyn_entity_msdyn_entitylinkchatconfiguration](#BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration)
- [msdyn_insightsstorevirtualentity_extensionofrecordid](#BKMK_msdyn_insightsstorevirtualentity_extensionofrecordid)
- [privilegesremovalsetting_extensionofrecordid](#BKMK_privilegesremovalsetting_extensionofrecordid)
- [recyclebinconfig_extensionofrecordid](#BKMK_recyclebinconfig_extensionofrecordid)
- [sharedlinksetting_extensionofrecordid](#BKMK_sharedlinksetting_extensionofrecordid)
- [virtualentitymetadata_extensionofrecordid](#BKMK_virtualentitymetadata_extensionofrecordid)

### <a name="BKMK_AIPluginOperation_Entity_Entity"></a> AIPluginOperation_Entity_Entity

Many-To-One Relationship: [aipluginoperation AIPluginOperation_Entity_Entity](aipluginoperation.md#BKMK_AIPluginOperation_Entity_Entity)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`entity`|
|ReferencedEntityNavigationPropertyName|`AIPluginOperation_Entity_Entity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_catalogassignment_entity"></a> catalogassignment_entity

Many-To-One Relationship: [catalogassignment catalogassignment_entity](catalogassignment.md#BKMK_catalogassignment_entity)

|Property|Value|
|---|---|
|ReferencingEntity|`catalogassignment`|
|ReferencingAttribute|`object`|
|ReferencedEntityNavigationPropertyName|`CatalogAssignments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_DVFileSearchEntity_Entity_Entity"></a> DVFileSearchEntity_Entity_Entity

Many-To-One Relationship: [dvfilesearchentity DVFileSearchEntity_Entity_Entity](dvfilesearchentity.md#BKMK_DVFileSearchEntity_Entity_Entity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchentity`|
|ReferencingAttribute|`entity`|
|ReferencedEntityNavigationPropertyName|`DVFileSearchEntity_Entity_Entity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_DVTableSearchEntity_Entity_Entity"></a> DVTableSearchEntity_Entity_Entity

Many-To-One Relationship: [dvtablesearchentity DVTableSearchEntity_Entity_Entity](dvtablesearchentity.md#BKMK_DVTableSearchEntity_Entity_Entity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchentity`|
|ReferencingAttribute|`entity`|
|ReferencedEntityNavigationPropertyName|`DVTableSearchEntity_Entity_Entity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_emailaddressconfiguration_entity_EntityId"></a> emailaddressconfiguration_entity_EntityId

Many-To-One Relationship: [emailaddressconfiguration emailaddressconfiguration_entity_EntityId](emailaddressconfiguration.md#BKMK_emailaddressconfiguration_entity_EntityId)

|Property|Value|
|---|---|
|ReferencingEntity|`emailaddressconfiguration`|
|ReferencingAttribute|`entityid`|
|ReferencedEntityNavigationPropertyName|`emailaddressconfiguration_entity_EntityId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_appaction_ContextEntity"></a> entity_appaction_ContextEntity

Many-To-One Relationship: [appaction entity_appaction_ContextEntity](appaction.md#BKMK_entity_appaction_ContextEntity)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`contextentity`|
|ReferencedEntityNavigationPropertyName|`entity_appaction_ContextEntity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_appactionrule_ContextEntity"></a> entity_appactionrule_ContextEntity

Many-To-One Relationship: [appactionrule entity_appactionrule_ContextEntity](appactionrule.md#BKMK_entity_appactionrule_ContextEntity)

|Property|Value|
|---|---|
|ReferencingEntity|`appactionrule`|
|ReferencingAttribute|`contextentity`|
|ReferencedEntityNavigationPropertyName|`entity_appactionrule_ContextEntity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_entityanalyticsconfig"></a> entity_entityanalyticsconfig

Many-To-One Relationship: [entityanalyticsconfig entity_entityanalyticsconfig](entityanalyticsconfig.md#BKMK_entity_entityanalyticsconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`entityanalyticsconfig`|
|ReferencingAttribute|`parententityid`|
|ReferencedEntityNavigationPropertyName|`entity_entityanalyticsconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_sensitivitylabelattributemapping_EntityId"></a> entity_sensitivitylabelattributemapping_EntityId

Many-To-One Relationship: [sensitivitylabelattributemapping entity_sensitivitylabelattributemapping_EntityId](sensitivitylabelattributemapping.md#BKMK_entity_sensitivitylabelattributemapping_EntityId)

|Property|Value|
|---|---|
|ReferencingEntity|`sensitivitylabelattributemapping`|
|ReferencingAttribute|`entityid`|
|ReferencedEntityNavigationPropertyName|`entity_sensitivitylabelattributemapping_EntityId`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_serviceplanmapping"></a> entity_serviceplanmapping

Many-To-One Relationship: [serviceplanmapping entity_serviceplanmapping](serviceplanmapping.md#BKMK_entity_serviceplanmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`serviceplanmapping`|
|ReferencingAttribute|`entity`|
|ReferencedEntityNavigationPropertyName|`entity_serviceplanmapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_solutioncomponentbatchconfiguration_PrimaryEntity"></a> entity_solutioncomponentbatchconfiguration_PrimaryEntity

Many-To-One Relationship: [solutioncomponentbatchconfiguration entity_solutioncomponentbatchconfiguration_PrimaryEntity](solutioncomponentbatchconfiguration.md#BKMK_entity_solutioncomponentbatchconfiguration_PrimaryEntity)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentbatchconfiguration`|
|ReferencingAttribute|`primaryentity`|
|ReferencedEntityNavigationPropertyName|`entity_solutioncomponentbatchconfiguration_PrimaryEntity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_solutioncomponentbatchconfiguration_RelatedEntity"></a> entity_solutioncomponentbatchconfiguration_RelatedEntity

Many-To-One Relationship: [solutioncomponentbatchconfiguration entity_solutioncomponentbatchconfiguration_RelatedEntity](solutioncomponentbatchconfiguration.md#BKMK_entity_solutioncomponentbatchconfiguration_RelatedEntity)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentbatchconfiguration`|
|ReferencingAttribute|`relatedentity`|
|ReferencedEntityNavigationPropertyName|`entity_solutioncomponentbatchconfiguration_RelatedEntity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entity_solutioncomponentconfiguration"></a> entity_solutioncomponentconfiguration

Many-To-One Relationship: [solutioncomponentconfiguration entity_solutioncomponentconfiguration](solutioncomponentconfiguration.md#BKMK_entity_solutioncomponentconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentconfiguration`|
|ReferencingAttribute|`entityid`|
|ReferencedEntityNavigationPropertyName|`entity_solutioncomponentconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityclusterconfig_extensionofrecordid"></a> entityclusterconfig_extensionofrecordid

Many-To-One Relationship: [entityclusterconfig entityclusterconfig_extensionofrecordid](entityclusterconfig.md#BKMK_entityclusterconfig_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencingEntity|`entityclusterconfig`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`entityclusterconfig_extensionofrecordid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_metadataforarchival_extensionofrecordid"></a> metadataforarchival_extensionofrecordid

Many-To-One Relationship: [metadataforarchival metadataforarchival_extensionofrecordid](metadataforarchival.md#BKMK_metadataforarchival_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencingEntity|`metadataforarchival`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`metadataforarchival_extensionofrecordid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration"></a> msdyn_entity_msdyn_entitylinkchatconfiguration

Many-To-One Relationship: [msdyn_entitylinkchatconfiguration msdyn_entity_msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencingAttribute|`msdyn_entitytype`|
|ReferencedEntityNavigationPropertyName|`msdyn_entity_msdyn_entitylinkchatconfiguration_entitytype`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_insightsstorevirtualentity_extensionofrecordid"></a> msdyn_insightsstorevirtualentity_extensionofrecordid

Many-To-One Relationship: [msdyn_insightsstorevirtualentity msdyn_insightsstorevirtualentity_extensionofrecordid](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_insightsstorevirtualentity`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_insightsstorevirtualentity_extensionofrecordid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_extensionofrecordid"></a> privilegesremovalsetting_extensionofrecordid

Many-To-One Relationship: [privilegesremovalsetting privilegesremovalsetting_extensionofrecordid](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencingEntity|`privilegesremovalsetting`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_extensionofrecordid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recyclebinconfig_extensionofrecordid"></a> recyclebinconfig_extensionofrecordid

Many-To-One Relationship: [recyclebinconfig recyclebinconfig_extensionofrecordid](recyclebinconfig.md#BKMK_recyclebinconfig_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencingEntity|`recyclebinconfig`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`recyclebinconfig_extensionofrecordid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sharedlinksetting_extensionofrecordid"></a> sharedlinksetting_extensionofrecordid

Many-To-One Relationship: [sharedlinksetting sharedlinksetting_extensionofrecordid](sharedlinksetting.md#BKMK_sharedlinksetting_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencingEntity|`sharedlinksetting`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`sharedlinksetting_extensionofrecordid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_virtualentitymetadata_extensionofrecordid"></a> virtualentitymetadata_extensionofrecordid

Many-To-One Relationship: [virtualentitymetadata virtualentitymetadata_extensionofrecordid](virtualentitymetadata.md#BKMK_virtualentitymetadata_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencingEntity|`virtualentitymetadata`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`virtualentitymetadata_extensionofrecordid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_card_entity_connections"></a> card_entity_connections

See [card card_entity_connections Many-To-Many Relationship](card.md#BKMK_card_entity_connections)

|Property|Value|
|---|---|
|IntersectEntityName|`cardentityconnections`|
|IsCustomizable|False|
|SchemaName|`card_entity_connections`|
|IntersectAttribute|`entityid`|
|NavigationPropertyName|`card_entity_connections`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.entity?displayProperty=fullName>
