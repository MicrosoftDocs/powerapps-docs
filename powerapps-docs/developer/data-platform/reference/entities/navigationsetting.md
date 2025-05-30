---
title: "Navigation Setting (NavigationSetting) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Navigation Setting (NavigationSetting) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Navigation Setting (NavigationSetting) table/entity reference (Microsoft Dataverse)

Navigation Setting: A setting page or group of pages available for configuration within an app. A record representing a group of pages is regarded as the parent navigation setting of one or more other records. For internal use only.

## Messages

The following table lists the messages for the Navigation Setting (NavigationSetting) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /navigationsettings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /navigationsettings(*navigationsettingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /navigationsettings(*navigationsettingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /navigationsettings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: True |`PATCH` /navigationsettings(*navigationsettingid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /navigationsettings(*navigationsettingid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Navigation Setting (NavigationSetting) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Navigation Setting** |
| **DisplayCollectionName** | **Navigation Settings** |
| **SchemaName** | `NavigationSetting` |
| **CollectionSchemaName** | `NavigationSettings` |
| **EntitySetName** | `navigationsettings`|
| **LogicalName** | `navigationsetting` |
| **LogicalCollectionName** | `navigationsettings` |
| **PrimaryIdAttribute** | `navigationsettingid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdvancedSettingOrder](#BKMK_AdvancedSettingOrder)
- [AppConfigId](#BKMK_AppConfigId)
- [AppConfigIdUnique](#BKMK_AppConfigIdUnique)
- [Description](#BKMK_Description)
- [GroupName](#BKMK_GroupName)
- [IconResourceId](#BKMK_IconResourceId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [Name](#BKMK_Name)
- [NavigationSettingId](#BKMK_NavigationSettingId)
- [NavigationSettingIdUnique](#BKMK_NavigationSettingIdUnique)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [PageUrl](#BKMK_PageUrl)
- [ParentNavigationSettingId](#BKMK_ParentNavigationSettingId)
- [Privileges](#BKMK_Privileges)
- [ProgressState](#BKMK_ProgressState)
- [QuickSettingOrder](#BKMK_QuickSettingOrder)
- [ResourceId](#BKMK_ResourceId)
- [SettingType](#BKMK_SettingType)

### <a name="BKMK_AdvancedSettingOrder"></a> AdvancedSettingOrder

|Property|Value|
|---|---|
|Description|**Enter the position of this NavigationSetting as it should appear within its group in the Advanced Setup menu.**|
|DisplayName|**AdvancedOrder**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`advancedsettingorder`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_AppConfigId"></a> AppConfigId

|Property|Value|
|---|---|
|Description|**Enter the App Config record that this Navigation Setting is associated with.**|
|DisplayName|**AppConfigId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfigid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|appmodule|

### <a name="BKMK_AppConfigIdUnique"></a> AppConfigIdUnique

|Property|Value|
|---|---|
|Description|**For system use only.**|
|DisplayName|**AppConfigIdUnique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfigidunique`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type a description that describes that Navigation Setting in detail.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_GroupName"></a> GroupName

|Property|Value|
|---|---|
|Description|**Type the name of the group represented by this Navigation Setting record.**|
|DisplayName|**Group Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`groupname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|400|

### <a name="BKMK_IconResourceId"></a> IconResourceId

|Property|Value|
|---|---|
|Description|**The web resource identifier of the icon to be used for a navigation setting area or sub area.**|
|DisplayName|**IconResourceId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconresourceid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the similarity rule is introduced.**|
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
|MaxLength|100|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a title or name that describes the Navigation Setting so it can be identified in Dynamics CRM views.**|
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
|MaxLength|100|

### <a name="BKMK_NavigationSettingId"></a> NavigationSettingId

|Property|Value|
|---|---|
|Description|**Identifies a single setting page or group of pages configured for use in a single app.**|
|DisplayName|**NavigationSettingId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`navigationsettingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_NavigationSettingIdUnique"></a> NavigationSettingIdUnique

|Property|Value|
|---|---|
|Description|**For system use only.**|
|DisplayName|**NavigationSettingIdUnique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`navigationsettingidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Enter the Object Type Code of the entity associated whose page this Navigation Setting record represents.**|
|DisplayName|**EntityObjectTypeCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_PageUrl"></a> PageUrl

|Property|Value|
|---|---|
|Description|**Type the URL which locates the page associated with this Navigation Setting record.**|
|DisplayName|**Page Url**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pageurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

### <a name="BKMK_ParentNavigationSettingId"></a> ParentNavigationSettingId

|Property|Value|
|---|---|
|Description|**The Navigation Setting record that represents the group that this record belongs to.**|
|DisplayName|**Parent Navigation Setting Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentnavigationsettingid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Privileges"></a> Privileges

|Property|Value|
|---|---|
|Description|**Enter the Privilege Mask for the entity associated with this navigation setting page that will be the minimum requirement for the page to be made available to a user.**|
|DisplayName|**Privileges**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privileges`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ProgressState"></a> ProgressState

|Property|Value|
|---|---|
|Description|**Select the setup completion level for this Navigation Setting page.**|
|DisplayName|**Progress State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`progressstate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`navigationsetting_progressstate`|
|DefaultValue|False|
|True Label|Visited|
|False Label|Not Visited|

### <a name="BKMK_QuickSettingOrder"></a> QuickSettingOrder

|Property|Value|
|---|---|
|Description|**Enter the position of this NavigationSetting as it should appear in the Quick Setup menu.**|
|DisplayName|**QuickOrder**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`quicksettingorder`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ResourceId"></a> ResourceId

|Property|Value|
|---|---|
|Description|**The Web Resource that will be associated with this Navigation Setting record.**|
|DisplayName|**Resource Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`resourceid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SettingType"></a> SettingType

|Property|Value|
|---|---|
|Description|**Select the type of group this Navigation Setting record represents. This determines which of the three in-app customization menus will contain this group.**|
|DisplayName|**Group Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`settingtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`navigationsetting_settingtype`|

#### SettingType Choices/Options

|Value|Label|
|---|---|
|0|**Advanced Setup**|
|1|**Basic Setup**|
|2|**Advanced Setup Summary**|
|3|**Basic Setup Summary**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

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
|Description|**System-populated field that identifies the organization that owns this Navigation Setting record.**|
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
|Description|**Date and time that the record was migrated.**|
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

- [lk_navigationsetting_createdby](#BKMK_lk_navigationsetting_createdby)
- [lk_navigationsetting_createdonbehalfby](#BKMK_lk_navigationsetting_createdonbehalfby)
- [lk_navigationsetting_modifiedby](#BKMK_lk_navigationsetting_modifiedby)
- [lk_navigationsetting_modifiedonbehalfby](#BKMK_lk_navigationsetting_modifiedonbehalfby)
- [navigationsetting_appconfig](#BKMK_navigationsetting_appconfig)
- [organization_navigationsetting](#BKMK_organization_navigationsetting)

### <a name="BKMK_lk_navigationsetting_createdby"></a> lk_navigationsetting_createdby

One-To-Many Relationship: [systemuser lk_navigationsetting_createdby](systemuser.md#BKMK_lk_navigationsetting_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`navigationsetting_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_navigationsetting_createdonbehalfby"></a> lk_navigationsetting_createdonbehalfby

One-To-Many Relationship: [systemuser lk_navigationsetting_createdonbehalfby](systemuser.md#BKMK_lk_navigationsetting_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`navigationsetting_createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_navigationsetting_modifiedby"></a> lk_navigationsetting_modifiedby

One-To-Many Relationship: [systemuser lk_navigationsetting_modifiedby](systemuser.md#BKMK_lk_navigationsetting_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`navigationsetting_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_navigationsetting_modifiedonbehalfby"></a> lk_navigationsetting_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_navigationsetting_modifiedonbehalfby](systemuser.md#BKMK_lk_navigationsetting_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`navigationsetting_modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_navigationsetting_appconfig"></a> navigationsetting_appconfig

One-To-Many Relationship: [appconfig navigationsetting_appconfig](appconfig.md#BKMK_navigationsetting_appconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`appconfig`|
|ReferencedAttribute|`appconfigid`|
|ReferencingAttribute|`appconfigid`|
|ReferencingEntityNavigationPropertyName|`navigationsetting_appconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_organization_navigationsetting"></a> organization_navigationsetting

One-To-Many Relationship: [organization organization_navigationsetting](organization.md#BKMK_organization_navigationsetting)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organization_navigationsetting_navigationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.navigationsetting?displayProperty=fullName>
