---
title: "AppConfigMaster table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the AppConfigMaster table/entity."
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

# AppConfigMaster table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Contains the master list of all properties that can be customized for apps in Dynamics 365. For internal use only.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/appconfigmasters(*appconfigmasterid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/appconfigmasters<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|AppConfigMasters|
|DisplayCollectionName|App Config Master|
|DisplayName|App Config Master|
|EntitySetName|appconfigmasters|
|IsBPFEntity|False|
|LogicalCollectionName|appconfigmasters|
|LogicalName|appconfigmaster|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|appconfigmasterid|
|PrimaryNameAttribute|name|
|SchemaName|AppConfigMaster|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Enter the name of the App Configuration and Setting property with which this customization will be identified.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AppConfigMasterId](#BKMK_AppConfigMasterId)
- [ConfigType](#BKMK_ConfigType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DefaultValue](#BKMK_DefaultValue)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsNavigationSetting](#BKMK_IsNavigationSetting)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentAppConfigMasterId](#BKMK_ParentAppConfigMasterId)
- [Validator](#BKMK_Validator)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AppConfigMasterId"></a> AppConfigMasterId

|Property|Value|
|--------|-----|
|Description|System-Populated App Configuration instance identifier.|
|DisplayName|AppConfigMasterId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appconfigmasterid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ConfigType"></a> ConfigType

|Property|Value|
|--------|-----|
|Description|Enter the App Configuration and Setting property data type.|
|DisplayName|ConfigType|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|configtype|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.|
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
|Description|Shows who created the record on behalfÂ of another user.|
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


### <a name="BKMK_DefaultValue"></a> DefaultValue

|Property|Value|
|--------|-----|
|Description|Enter the default value of the App Configuration and Setting property.|
|DisplayName|DefaultValue|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultvalue|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsNavigationSetting"></a> IsNavigationSetting

|Property|Value|
|--------|-----|
|Description|Enter whether this App Configuration and Setting is Navigation Setting.|
|DisplayName|Is Nagivation Setting|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isnavigationsetting|
|MaxValue|1|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.|
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
|Description|Shows who last updated the record on behalf of another user.|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|System-calculated field for Organization identifier.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

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


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was migrated. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ParentAppConfigMasterId"></a> ParentAppConfigMasterId

|Property|Value|
|--------|-----|
|Description|ParentAppConfigMasterId|
|DisplayName|Enter the parent of App Configuration customization property.|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentappconfigmasterid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Validator"></a> Validator

|Property|Value|
|--------|-----|
|Description|Validator|
|DisplayName|Enter the validator configuration xml which will validate against its value when creating AppConfigInstance.|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|validator|
|MaxLength|4000|
|RequiredLevel|SystemRequired|
|Type|String|


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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_appconfigmaster_appconfiginstance"></a> appconfigmaster_appconfiginstance

Same as appconfiginstance table [appconfigmaster_appconfiginstance](appconfiginstance.md#BKMK_appconfigmaster_appconfiginstance) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfiginstance|
|ReferencingAttribute|appconfigmasterid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appconfigmaster_appconfiginstance|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_appconfigmaster_modifiedby](#BKMK_lk_appconfigmaster_modifiedby)
- [lk_appconfigmaster_createdonbehalfby](#BKMK_lk_appconfigmaster_createdonbehalfby)
- [lk_appconfigmaster_createdby](#BKMK_lk_appconfigmaster_createdby)
- [lk_appconfigmaster_modifiedonbehalfby](#BKMK_lk_appconfigmaster_modifiedonbehalfby)
- [organization_appconfigmaster](#BKMK_organization_appconfigmaster)


### <a name="BKMK_lk_appconfigmaster_modifiedby"></a> lk_appconfigmaster_modifiedby

See systemuser Table [lk_appconfigmaster_modifiedby](systemuser.md#BKMK_lk_appconfigmaster_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_appconfigmaster_createdonbehalfby"></a> lk_appconfigmaster_createdonbehalfby

See systemuser Table [lk_appconfigmaster_createdonbehalfby](systemuser.md#BKMK_lk_appconfigmaster_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appconfigmaster_createdby"></a> lk_appconfigmaster_createdby

See systemuser Table [lk_appconfigmaster_createdby](systemuser.md#BKMK_lk_appconfigmaster_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appconfigmaster_modifiedonbehalfby"></a> lk_appconfigmaster_modifiedonbehalfby

See systemuser Table [lk_appconfigmaster_modifiedonbehalfby](systemuser.md#BKMK_lk_appconfigmaster_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_appconfigmaster"></a> organization_appconfigmaster

See organization Table [organization_appconfigmaster](organization.md#BKMK_organization_appconfigmaster) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.appconfigmaster?text=appconfigmaster EntityType" />