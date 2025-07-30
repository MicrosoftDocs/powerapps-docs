---
title: "App Module Component (AppModuleComponent) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the App Module Component (AppModuleComponent) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# App Module Component (AppModuleComponent) table/entity reference (Microsoft Dataverse)

A component available in a business app such as entity, dashboard, form, view, chart, and business process.

## Messages

The following table lists the messages for the App Module Component (AppModuleComponent) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /appmodulecomponents(*appmodulecomponentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /appmodulecomponents<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the App Module Component (AppModuleComponent) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **App Module Component** |
| **DisplayCollectionName** | **App Module Components** |
| **SchemaName** | `AppModuleComponent` |
| **CollectionSchemaName** | `App Module Components` |
| **EntitySetName** | `appmodulecomponents`|
| **LogicalName** | `appmodulecomponent` |
| **LogicalCollectionName** | `appmodulecomponents` |
| **PrimaryIdAttribute** | `appmodulecomponentid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppModuleComponentId](#BKMK_AppModuleComponentId)
- [AppModuleComponentIdUnique](#BKMK_AppModuleComponentIdUnique)
- [AppModuleIdUnique](#BKMK_AppModuleIdUnique)
- [ComponentType](#BKMK_ComponentType)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsDefault](#BKMK_IsDefault)
- [IsMetadata](#BKMK_IsMetadata)
- [ObjectId](#BKMK_ObjectId)
- [RootAppModuleComponentId](#BKMK_RootAppModuleComponentId)
- [RootComponentBehavior](#BKMK_RootComponentBehavior)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AppModuleComponentId"></a> AppModuleComponentId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**App Module Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmodulecomponentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AppModuleComponentIdUnique"></a> AppModuleComponentIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the Application Component used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook**|
|DisplayName|**Application Component Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmodulecomponentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AppModuleIdUnique"></a> AppModuleIdUnique

|Property|Value|
|---|---|
|Description|**The App Module Id Unique**|
|DisplayName|**AppModule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmoduleidunique`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|appmodule|

### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|---|---|
|Description|**The object type code of the component.**|
|DisplayName|**Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componenttype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`appmodulecomponent_componenttype`|

#### ComponentType Choices/Options

|Value|Label|
|---|---|
|1|**Entities**|
|26|**Views**|
|29|**Business Process Flows**|
|48|**Command (Ribbon) for Forms, Grids, sub grids**|
|59|**Charts**|
|60|**Forms**|
|62|**Sitemap**|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the application component record is introduced.**|
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

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Is Default**|
|DisplayName|**Is Default**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`appmodulecomponent_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMetadata"></a> IsMetadata

|Property|Value|
|---|---|
|Description|**Is Metadata**|
|DisplayName|**Is Metadata**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismetadata`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appmodulecomponent_ismetadata`|
|DefaultValue|False|
|True Label|Metadata|
|False Label|Data|

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Object Id**|
|DisplayName|**Object**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RootAppModuleComponentId"></a> RootAppModuleComponentId

|Property|Value|
|---|---|
|Description|**The parent ID of the subcomponent, which will be a root**|
|DisplayName|**Root App Module Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rootappmodulecomponentid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RootComponentBehavior"></a> RootComponentBehavior

|Property|Value|
|---|---|
|Description|**Indicates the include behavior of the root component.**|
|DisplayName|**Root Component Behavior**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rootcomponentbehavior`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`appmodulecomponent_rootcomponentbehavior`|

#### RootComponentBehavior Choices/Options

|Value|Label|
|---|---|
|0|**Include Subcomponents**|
|1|**Do not include subcomponents**|
|2|**Include As Shell Only**|

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
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
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
|IsValidForForm|False|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the Application Component with respect to the base currency.**|
|DisplayName|**ExchangeRate**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
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
|Description|**Date and time when the record was modified.**|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
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

- [appmodule_appmodulecomponent](#BKMK_appmodule_appmodulecomponent)
- [lk_appmodulecomponent_createdby](#BKMK_lk_appmodulecomponent_createdby)
- [lk_appmodulecomponent_createdonbehalfby](#BKMK_lk_appmodulecomponent_createdonbehalfby)
- [lk_appmodulecomponent_modifiedby](#BKMK_lk_appmodulecomponent_modifiedby)
- [lk_appmodulecomponent_modifiedonbehalfby](#BKMK_lk_appmodulecomponent_modifiedonbehalfby)

### <a name="BKMK_appmodule_appmodulecomponent"></a> appmodule_appmodulecomponent

One-To-Many Relationship: [appmodule appmodule_appmodulecomponent](appmodule.md#BKMK_appmodule_appmodulecomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`appmodule`|
|ReferencedAttribute|`appmoduleidunique`|
|ReferencingAttribute|`appmoduleidunique`|
|ReferencingEntityNavigationPropertyName|`appmoduleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_appmodulecomponent_createdby"></a> lk_appmodulecomponent_createdby

One-To-Many Relationship: [systemuser lk_appmodulecomponent_createdby](systemuser.md#BKMK_lk_appmodulecomponent_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`appmodulecomponent_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appmodulecomponent_createdonbehalfby"></a> lk_appmodulecomponent_createdonbehalfby

One-To-Many Relationship: [systemuser lk_appmodulecomponent_createdonbehalfby](systemuser.md#BKMK_lk_appmodulecomponent_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appmodulecomponent_modifiedby"></a> lk_appmodulecomponent_modifiedby

One-To-Many Relationship: [systemuser lk_appmodulecomponent_modifiedby](systemuser.md#BKMK_lk_appmodulecomponent_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`appmodulecomponent_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appmodulecomponent_modifiedonbehalfby"></a> lk_appmodulecomponent_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_appmodulecomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_appmodulecomponent_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.appmodulecomponent?displayProperty=fullName>
