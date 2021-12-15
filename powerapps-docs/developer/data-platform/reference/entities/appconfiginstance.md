---
title: "App Configuration Instance (AppConfigInstance) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the App Configuration Instance (AppConfigInstance) table/entity."
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

# App Configuration Instance (AppConfigInstance) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Contains a property or a list of properties from the app configuration master list that can be customized for any app in Dynamics 365. For internal use only.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/appconfiginstances<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/appconfiginstances(*appconfiginstanceid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/appconfiginstances(*appconfiginstanceid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/appconfiginstances<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveUnpublishedMultiple|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?text=RetrieveUnpublishedMultiple Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/appconfiginstances(*appconfiginstanceid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|AppConfigInstances|
|DisplayCollectionName|App Configuration Instance|
|DisplayName|App Configuration Instance|
|EntitySetName|appconfiginstances|
|IsBPFEntity|False|
|LogicalCollectionName|appconfiginstances|
|LogicalName|appconfiginstance|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|appconfiginstanceid|
|PrimaryNameAttribute||
|SchemaName|AppConfigInstance|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppConfigId](#BKMK_AppConfigId)
- [AppConfigIdUnique](#BKMK_AppConfigIdUnique)
- [AppConfigInstanceIdUnique](#BKMK_AppConfigInstanceIdUnique)
- [AppConfigMasterId](#BKMK_AppConfigMasterId)
- [ComponentType](#BKMK_ComponentType)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [ObjectId](#BKMK_ObjectId)
- [Value](#BKMK_Value)


### <a name="BKMK_AppConfigId"></a> AppConfigId

|Property|Value|
|--------|-----|
|Description|System-calculated App Configuration unique identifier.|
|DisplayName|App Config ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appconfigid|
|RequiredLevel|ApplicationRequired|
|Targets|appconfig|
|Type|Lookup|


### <a name="BKMK_AppConfigIdUnique"></a> AppConfigIdUnique

|Property|Value|
|--------|-----|
|Description|Enter the App Configuration unique identifier of AppConfig entity for which this customization belongs.|
|DisplayName|App Config ID Unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appconfigidunique|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_AppConfigInstanceIdUnique"></a> AppConfigInstanceIdUnique

|Property|Value|
|--------|-----|
|Description|System-populated App Configuration Instance unique identifier.|
|DisplayName|AppConfigInstanceIdUnique|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|appconfiginstanceidunique|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_AppConfigMasterId"></a> AppConfigMasterId

|Property|Value|
|--------|-----|
|Description|System-calculated App Configuration Master identifier.|
|DisplayName|App Config Master ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appconfigmasterid|
|RequiredLevel|ApplicationRequired|
|Targets|appconfigmaster|
|Type|Lookup|


### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|--------|-----|
|Description|ComponentType|
|DisplayName|Enter the componenet type of the artifact (Form/View etc.) for which customization is to be created.|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componenttype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Shows the version in which the App Configuration Instance is introduced.|
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


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|ObjectId|
|DisplayName|Enter the object identifier for the artifact (Form/View etc.) for which customization is to be created.|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Value"></a> Value

|Property|Value|
|--------|-----|
|Description|Enter a value for the customization property that is valid as per the validator XML specified in the app configuration master record.|
|DisplayName|Value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|value|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AppConfigInstanceId](#BKMK_AppConfigInstanceId)
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
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AppConfigInstanceId"></a> AppConfigInstanceId

|Property|Value|
|--------|-----|
|Description|System-Populated App Configuration instance identifier.|
|DisplayName|AppConfig Instance ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appconfiginstanceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|System-Populated Published or UnPublished state of App Configuration Instance.|
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


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Is Managed|
|DisplayName|Shows whether the App Configuration Instance is managed or not.|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|ApplicationRequired|
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


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the last overwrite time for the App Configuration Instance.|
|DisplayName|Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Set the solution idenfitier for associated solution.|
|DisplayName|SolutionId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|Set the supporting solution idenfitier for associated solution.|
|DisplayName|SupportingSolutionId|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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

- [appconfig_appconfiginstance](#BKMK_appconfig_appconfiginstance)
- [lk_appconfiginstance_modifiedby](#BKMK_lk_appconfiginstance_modifiedby)
- [lk_appconfiginstance_createdby](#BKMK_lk_appconfiginstance_createdby)
- [lk_appconfiginstance_createdonbehalfby](#BKMK_lk_appconfiginstance_createdonbehalfby)
- [lk_appconfiginstance_modifiedonbehalfby](#BKMK_lk_appconfiginstance_modifiedonbehalfby)
- [organization_appconfiginstance](#BKMK_organization_appconfiginstance)
- [appconfigmaster_appconfiginstance](#BKMK_appconfigmaster_appconfiginstance)


### <a name="BKMK_appconfig_appconfiginstance"></a> appconfig_appconfiginstance

See appconfig Table [appconfig_appconfiginstance](appconfig.md#BKMK_appconfig_appconfiginstance) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_modifiedby"></a> lk_appconfiginstance_modifiedby

See systemuser Table [lk_appconfiginstance_modifiedby](systemuser.md#BKMK_lk_appconfiginstance_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_createdby"></a> lk_appconfiginstance_createdby

See systemuser Table [lk_appconfiginstance_createdby](systemuser.md#BKMK_lk_appconfiginstance_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_createdonbehalfby"></a> lk_appconfiginstance_createdonbehalfby

See systemuser Table [lk_appconfiginstance_createdonbehalfby](systemuser.md#BKMK_lk_appconfiginstance_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_modifiedonbehalfby"></a> lk_appconfiginstance_modifiedonbehalfby

See systemuser Table [lk_appconfiginstance_modifiedonbehalfby](systemuser.md#BKMK_lk_appconfiginstance_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_appconfiginstance"></a> organization_appconfiginstance

See organization Table [organization_appconfiginstance](organization.md#BKMK_organization_appconfiginstance) One-To-Many relationship.

### <a name="BKMK_appconfigmaster_appconfiginstance"></a> appconfigmaster_appconfiginstance

See appconfigmaster Table [appconfigmaster_appconfiginstance](appconfigmaster.md#BKMK_appconfigmaster_appconfiginstance) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.appconfiginstance?text=appconfiginstance EntityType" />