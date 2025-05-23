---
title: "App Config Master (AppConfigMaster) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the App Config Master (AppConfigMaster) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# App Config Master (AppConfigMaster) table/entity reference (Microsoft Dataverse)

Contains the master list of all properties that can be customized for apps in Dynamics 365. For internal use only.

## Messages

The following table lists the messages for the App Config Master (AppConfigMaster) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /appconfigmasters(*appconfigmasterid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /appconfigmasters<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the App Config Master (AppConfigMaster) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **App Config Master** |
| **DisplayCollectionName** | **App Config Master** |
| **SchemaName** | `AppConfigMaster` |
| **CollectionSchemaName** | `AppConfigMasters` |
| **EntitySetName** | `appconfigmasters`|
| **LogicalName** | `appconfigmaster` |
| **LogicalCollectionName** | `appconfigmasters` |
| **PrimaryIdAttribute** | `appconfigmasterid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Enter the name of the App Configuration and Setting property with which this customization will be identified.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|200|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AppConfigMasterId](#BKMK_AppConfigMasterId)
- [ConfigType](#BKMK_ConfigType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DefaultValue](#BKMK_DefaultValue)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsNavigationSetting](#BKMK_IsNavigationSetting)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentAppConfigMasterId](#BKMK_ParentAppConfigMasterId)
- [Validator](#BKMK_Validator)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AppConfigMasterId"></a> AppConfigMasterId

|Property|Value|
|---|---|
|Description|**System-Populated App Configuration instance identifier.**|
|DisplayName|**AppConfigMasterId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfigmasterid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ConfigType"></a> ConfigType

|Property|Value|
|---|---|
|Description|**Enter the App Configuration and Setting property data type.**|
|DisplayName|**ConfigType**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`configtype`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.**|
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
|Description|**Shows who created the record on behalfÂ of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_DefaultValue"></a> DefaultValue

|Property|Value|
|---|---|
|Description|**Enter the default value of the App Configuration and Setting property.**|
|DisplayName|**DefaultValue**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultvalue`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsNavigationSetting"></a> IsNavigationSetting

|Property|Value|
|---|---|
|Description|**Enter whether this App Configuration and Setting is Navigation Setting.**|
|DisplayName|**Is Nagivation Setting**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnavigationsetting`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1|
|MinValue|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**System-calculated field for Organization identifier.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was migrated. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.**|
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

### <a name="BKMK_ParentAppConfigMasterId"></a> ParentAppConfigMasterId

|Property|Value|
|---|---|
|Description|**ParentAppConfigMasterId**|
|DisplayName|**Enter the parent of App Configuration customization property.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentappconfigmasterid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Validator"></a> Validator

|Property|Value|
|---|---|
|Description|**Validator**|
|DisplayName|**Enter the validator configuration xml which will validate against its value when creating AppConfigInstance.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`validator`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

- [lk_appconfigmaster_createdby](#BKMK_lk_appconfigmaster_createdby)
- [lk_appconfigmaster_createdonbehalfby](#BKMK_lk_appconfigmaster_createdonbehalfby)
- [lk_appconfigmaster_modifiedby](#BKMK_lk_appconfigmaster_modifiedby)
- [lk_appconfigmaster_modifiedonbehalfby](#BKMK_lk_appconfigmaster_modifiedonbehalfby)
- [organization_appconfigmaster](#BKMK_organization_appconfigmaster)

### <a name="BKMK_lk_appconfigmaster_createdby"></a> lk_appconfigmaster_createdby

One-To-Many Relationship: [systemuser lk_appconfigmaster_createdby](systemuser.md#BKMK_lk_appconfigmaster_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`appconfigmaster_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appconfigmaster_createdonbehalfby"></a> lk_appconfigmaster_createdonbehalfby

One-To-Many Relationship: [systemuser lk_appconfigmaster_createdonbehalfby](systemuser.md#BKMK_lk_appconfigmaster_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`appconfigmaster_createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appconfigmaster_modifiedby"></a> lk_appconfigmaster_modifiedby

One-To-Many Relationship: [systemuser lk_appconfigmaster_modifiedby](systemuser.md#BKMK_lk_appconfigmaster_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`appconfigmaster_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appconfigmaster_modifiedonbehalfby"></a> lk_appconfigmaster_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_appconfigmaster_modifiedonbehalfby](systemuser.md#BKMK_lk_appconfigmaster_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`appconfigmaster_modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_appconfigmaster"></a> organization_appconfigmaster

One-To-Many Relationship: [organization organization_appconfigmaster](organization.md#BKMK_organization_appconfigmaster)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organization_appconfigmaster_appconfigmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_appconfigmaster_appconfiginstance"></a> appconfigmaster_appconfiginstance

Many-To-One Relationship: [appconfiginstance appconfigmaster_appconfiginstance](appconfiginstance.md#BKMK_appconfigmaster_appconfiginstance)

|Property|Value|
|---|---|
|ReferencingEntity|`appconfiginstance`|
|ReferencingAttribute|`appconfigmasterid`|
|ReferencedEntityNavigationPropertyName|`appconfigmaster_appconfiginstance`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.appconfigmaster?displayProperty=fullName>
