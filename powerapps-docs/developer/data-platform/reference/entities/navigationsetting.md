---
title: "NavigationSetting table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the NavigationSetting table/entity."
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

# NavigationSetting table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Navigation Setting: A setting page or group of pages available for configuration within an app. A record representing a group of pages is regarded as the parent navigation setting of one or more other records. For internal use only.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/navigationsettings<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/navigationsettings(*navigationsettingid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/navigationsettings(*navigationsettingid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/navigationsettings<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveUnpublishedMultiple|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?text=RetrieveUnpublishedMultiple Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/navigationsettings(*navigationsettingid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|NavigationSettings|
|DisplayCollectionName|Navigation Settings|
|DisplayName|Navigation Setting|
|EntitySetName|navigationsettings|
|IsBPFEntity|False|
|LogicalCollectionName|navigationsettings|
|LogicalName|navigationsetting|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|navigationsettingid|
|PrimaryNameAttribute|name|
|SchemaName|NavigationSetting|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Enter the position of this NavigationSetting as it should appear within its group in the Advanced Setup menu.|
|DisplayName|AdvancedOrder|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|advancedsettingorder|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_AppConfigId"></a> AppConfigId

|Property|Value|
|--------|-----|
|Description|Enter the App Config record that this Navigation Setting is associated with.|
|DisplayName|AppConfigId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appconfigid|
|RequiredLevel|ApplicationRequired|
|Targets|appmodule|
|Type|Lookup|


### <a name="BKMK_AppConfigIdUnique"></a> AppConfigIdUnique

|Property|Value|
|--------|-----|
|Description|For system use only.|
|DisplayName|AppConfigIdUnique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appconfigidunique|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type a description that describes that Navigation Setting in detail.|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_GroupName"></a> GroupName

|Property|Value|
|--------|-----|
|Description|Type the name of the group represented by this Navigation Setting record.|
|DisplayName|Group Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|groupname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IconResourceId"></a> IconResourceId

|Property|Value|
|--------|-----|
|Description|The web resource identifier of the icon to be used for a navigation setting area or sub area.|
|DisplayName|IconResourceId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iconresourceid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the similarity rule is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Type a title or name that describes the Navigation Setting so it can be identified in Dynamics CRM views.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_NavigationSettingId"></a> NavigationSettingId

|Property|Value|
|--------|-----|
|Description|Identifies a single setting page or group of pages configured for use in a single app.|
|DisplayName|NavigationSettingId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|navigationsettingid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_NavigationSettingIdUnique"></a> NavigationSettingIdUnique

|Property|Value|
|--------|-----|
|Description|For system use only.|
|DisplayName|NavigationSettingIdUnique|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|navigationsettingidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Enter the Object Type Code of the entity associated whose page this Navigation Setting record represents.|
|DisplayName|EntityObjectTypeCode|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_PageUrl"></a> PageUrl

|Property|Value|
|--------|-----|
|Description|Type the URL which locates the page associated with this Navigation Setting record.|
|DisplayName|Page Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|pageurl|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParentNavigationSettingId"></a> ParentNavigationSettingId

|Property|Value|
|--------|-----|
|Description|The Navigation Setting record that represents the group that this record belongs to.|
|DisplayName|Parent Navigation Setting Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentnavigationsettingid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Privileges"></a> Privileges

|Property|Value|
|--------|-----|
|Description|Enter the Privilege Mask for the entity associated with this navigation setting page that will be the minimum requirement for the page to be made available to a user.|
|DisplayName|Privileges|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|privileges|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ProgressState"></a> ProgressState

|Property|Value|
|--------|-----|
|Description|Select the setup completion level for this Navigation Setting page.|
|DisplayName|Progress State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|progressstate|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### ProgressState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Visited|
|0|Not Visited|

**DefaultValue**: False



### <a name="BKMK_QuickSettingOrder"></a> QuickSettingOrder

|Property|Value|
|--------|-----|
|Description|Enter the position of this NavigationSetting as it should appear in the Quick Setup menu.|
|DisplayName|QuickOrder|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|quicksettingorder|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ResourceId"></a> ResourceId

|Property|Value|
|--------|-----|
|Description|The Web Resource that will be associated with this Navigation Setting record.|
|DisplayName|Resource Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|resourceid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_SettingType"></a> SettingType

|Property|Value|
|--------|-----|
|Description|Select the type of group this Navigation Setting record represents. This determines which of the three in-app customization menus will contain this group.|
|DisplayName|Group Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|settingtype|
|RequiredLevel|None|
|Type|Picklist|

#### SettingType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Advanced Setup||
|1|Basic Setup||
|2|Advanced Setup Summary||
|3|Basic Setup Summary||


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
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
|Description|Shows who created the record on behalf of another user.|
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


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



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
|Description|System-populated field that identifies the organization that owns this Navigation Setting record.|
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
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


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

- [lk_navigationsetting_modifiedonbehalfby](#BKMK_lk_navigationsetting_modifiedonbehalfby)
- [navigationsetting_appconfig](#BKMK_navigationsetting_appconfig)
- [lk_navigationsetting_createdonbehalfby](#BKMK_lk_navigationsetting_createdonbehalfby)
- [lk_navigationsetting_createdby](#BKMK_lk_navigationsetting_createdby)
- [lk_navigationsetting_modifiedby](#BKMK_lk_navigationsetting_modifiedby)
- [organization_navigationsetting](#BKMK_organization_navigationsetting)


### <a name="BKMK_lk_navigationsetting_modifiedonbehalfby"></a> lk_navigationsetting_modifiedonbehalfby

See systemuser Table [lk_navigationsetting_modifiedonbehalfby](systemuser.md#BKMK_lk_navigationsetting_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_navigationsetting_appconfig"></a> navigationsetting_appconfig

See appconfig Table [navigationsetting_appconfig](appconfig.md#BKMK_navigationsetting_appconfig) One-To-Many relationship.

### <a name="BKMK_lk_navigationsetting_createdonbehalfby"></a> lk_navigationsetting_createdonbehalfby

See systemuser Table [lk_navigationsetting_createdonbehalfby](systemuser.md#BKMK_lk_navigationsetting_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_navigationsetting_createdby"></a> lk_navigationsetting_createdby

See systemuser Table [lk_navigationsetting_createdby](systemuser.md#BKMK_lk_navigationsetting_createdby) One-To-Many relationship.

### <a name="BKMK_lk_navigationsetting_modifiedby"></a> lk_navigationsetting_modifiedby

See systemuser Table [lk_navigationsetting_modifiedby](systemuser.md#BKMK_lk_navigationsetting_modifiedby) One-To-Many relationship.

### <a name="BKMK_organization_navigationsetting"></a> organization_navigationsetting

See organization Table [organization_navigationsetting](organization.md#BKMK_organization_navigationsetting) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.navigationsetting?text=navigationsetting EntityType" />