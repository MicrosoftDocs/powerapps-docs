---
title: "AppModuleComponent table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the AppModuleComponent table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# AppModuleComponent table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

A component available in a business app such as entity, dashboard, form, view, chart, and business process.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/appmodulecomponents(*appmodulecomponentid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/appmodulecomponents<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|App Module Components|
|DisplayCollectionName|App Module Components|
|DisplayName|App Module Component|
|EntitySetName|appmodulecomponents|
|IsBPFEntity|False|
|LogicalCollectionName|appmodulecomponents|
|LogicalName|appmodulecomponent|
|OwnershipType|None|
|PrimaryIdAttribute|appmodulecomponentid|
|PrimaryNameAttribute||
|SchemaName|AppModuleComponent|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|App Module Component|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|appmodulecomponentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AppModuleComponentIdUnique"></a> AppModuleComponentIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Application Component used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook|
|DisplayName|Application Component Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appmodulecomponentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AppModuleIdUnique"></a> AppModuleIdUnique

|Property|Value|
|--------|-----|
|Description|The App Module Id Unique|
|DisplayName|AppModule|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appmoduleidunique|
|RequiredLevel|ApplicationRequired|
|Targets|appmodule|
|Type|Lookup|


### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|--------|-----|
|Description|The object type code of the component.|
|DisplayName|Object Type Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componenttype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### ComponentType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Entities||
|26|Views||
|29|Business Process Flows||
|48|Command (Ribbon) for Forms, Grids, sub grids||
|59|Charts||
|60|Forms||
|62|Sitemap||



### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the application component record is introduced.|
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


### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|--------|-----|
|Description|Is Default|
|DisplayName|Is Default|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdefault|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### IsDefault Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsMetadata"></a> IsMetadata

|Property|Value|
|--------|-----|
|Description|Is Metadata|
|DisplayName|Is Metadata|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismetadata|
|RequiredLevel|None|
|Type|Boolean|

#### IsMetadata Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Metadata|
|0|Data|

**DefaultValue**: False



### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Object Id|
|DisplayName|Object|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RootAppModuleComponentId"></a> RootAppModuleComponentId

|Property|Value|
|--------|-----|
|Description|The parent ID of the subcomponent, which will be a root|
|DisplayName|Root App Module Component|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rootappmodulecomponentid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RootComponentBehavior"></a> RootComponentBehavior

|Property|Value|
|--------|-----|
|Description|Indicates the include behavior of the root component.|
|DisplayName|Root Component Behavior|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rootcomponentbehavior|
|RequiredLevel|None|
|Type|Picklist|

#### RootComponentBehavior Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Include Subcomponents||
|1|Do not include subcomponents||
|2|Include As Shell Only||



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

- [AppModuleIdName](#BKMK_AppModuleIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AppModuleIdName"></a> AppModuleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appmoduleidname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

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
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the Application Component with respect to the base currency.|
|DisplayName|ExchangeRate|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

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


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [appmodule_appmodulecomponent](#BKMK_appmodule_appmodulecomponent)
- [lk_appmodulecomponent_createdonbehalfby](#BKMK_lk_appmodulecomponent_createdonbehalfby)
- [lk_appmodulecomponent_modifiedonbehalfby](#BKMK_lk_appmodulecomponent_modifiedonbehalfby)
- [lk_appmodulecomponent_createdby](#BKMK_lk_appmodulecomponent_createdby)
- [lk_appmodulecomponent_modifiedby](#BKMK_lk_appmodulecomponent_modifiedby)


### <a name="BKMK_appmodule_appmodulecomponent"></a> appmodule_appmodulecomponent

See appmodule Table [appmodule_appmodulecomponent](appmodule.md#BKMK_appmodule_appmodulecomponent) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_createdonbehalfby"></a> lk_appmodulecomponent_createdonbehalfby

See systemuser Table [lk_appmodulecomponent_createdonbehalfby](systemuser.md#BKMK_lk_appmodulecomponent_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_modifiedonbehalfby"></a> lk_appmodulecomponent_modifiedonbehalfby

See systemuser Table [lk_appmodulecomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_appmodulecomponent_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_createdby"></a> lk_appmodulecomponent_createdby

See systemuser Table [lk_appmodulecomponent_createdby](systemuser.md#BKMK_lk_appmodulecomponent_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_modifiedby"></a> lk_appmodulecomponent_modifiedby

See systemuser Table [lk_appmodulecomponent_modifiedby](systemuser.md#BKMK_lk_appmodulecomponent_modifiedby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.appmodulecomponent?text=appmodulecomponent EntityType" />