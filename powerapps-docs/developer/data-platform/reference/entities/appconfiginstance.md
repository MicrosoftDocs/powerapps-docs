---
title: "App Configuration Instance (AppConfigInstance) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the App Configuration Instance (AppConfigInstance) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# App Configuration Instance (AppConfigInstance) table/entity reference (Microsoft Dataverse)

Contains a property or a list of properties from the app configuration master list that can be customized for any app in Dynamics 365. For internal use only.

## Messages

The following table lists the messages for the App Configuration Instance (AppConfigInstance) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /appconfiginstances<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /appconfiginstances(*appconfiginstanceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /appconfiginstances(*appconfiginstanceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /appconfiginstances<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: True |`PATCH` /appconfiginstances(*appconfiginstanceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /appconfiginstances(*appconfiginstanceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the App Configuration Instance (AppConfigInstance) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **App Configuration Instance** |
| **DisplayCollectionName** | **App Configuration Instance** |
| **SchemaName** | `AppConfigInstance` |
| **CollectionSchemaName** | `AppConfigInstances` |
| **EntitySetName** | `appconfiginstances`|
| **LogicalName** | `appconfiginstance` |
| **LogicalCollectionName** | `appconfiginstances` |
| **PrimaryIdAttribute** | `appconfiginstanceid` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**System-calculated App Configuration unique identifier.**|
|DisplayName|**App Config ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfigid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|appconfig|

### <a name="BKMK_AppConfigIdUnique"></a> AppConfigIdUnique

|Property|Value|
|---|---|
|Description|**Enter the App Configuration unique identifier of AppConfig entity for which this customization belongs.**|
|DisplayName|**App Config ID Unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfigidunique`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_AppConfigInstanceIdUnique"></a> AppConfigInstanceIdUnique

|Property|Value|
|---|---|
|Description|**System-populated App Configuration Instance unique identifier.**|
|DisplayName|**AppConfigInstanceIdUnique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfiginstanceidunique`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_AppConfigMasterId"></a> AppConfigMasterId

|Property|Value|
|---|---|
|Description|**System-calculated App Configuration Master identifier.**|
|DisplayName|**App Config Master ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfigmasterid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|appconfigmaster|

### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|---|---|
|Description|**ComponentType**|
|DisplayName|**Enter the componenet type of the artifact (Form/View etc.) for which customization is to be created.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componenttype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Shows the version in which the App Configuration Instance is introduced.**|
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

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**ObjectId**|
|DisplayName|**Enter the object identifier for the artifact (Form/View etc.) for which customization is to be created.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Value"></a> Value

|Property|Value|
|---|---|
|Description|**Enter a value for the customization property that is valid as per the validator XML specified in the app configuration master record.**|
|DisplayName|**Value**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`value`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AppConfigInstanceId](#BKMK_AppConfigInstanceId)
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
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AppConfigInstanceId"></a> AppConfigInstanceId

|Property|Value|
|---|---|
|Description|**System-Populated App Configuration instance identifier.**|
|DisplayName|**AppConfig Instance ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appconfiginstanceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**System-Populated Published or UnPublished state of App Configuration Instance.**|
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
|Description|**Shows who created the record on behalfÂ of another user.**|
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
|Description|**For internal use only.**|
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
|Description|**Is Managed**|
|DisplayName|**Shows whether the App Configuration Instance is managed or not.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|ApplicationRequired|
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

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**Shows the last overwrite time for the App Configuration Instance.**|
|DisplayName|**Overwrite Time**|
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
|Description|**Set the solution idenfitier for associated solution.**|
|DisplayName|**SolutionId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**Set the supporting solution idenfitier for associated solution.**|
|DisplayName|**SupportingSolutionId**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

- [appconfig_appconfiginstance](#BKMK_appconfig_appconfiginstance)
- [appconfigmaster_appconfiginstance](#BKMK_appconfigmaster_appconfiginstance)
- [lk_appconfiginstance_createdby](#BKMK_lk_appconfiginstance_createdby)
- [lk_appconfiginstance_createdonbehalfby](#BKMK_lk_appconfiginstance_createdonbehalfby)
- [lk_appconfiginstance_modifiedby](#BKMK_lk_appconfiginstance_modifiedby)
- [lk_appconfiginstance_modifiedonbehalfby](#BKMK_lk_appconfiginstance_modifiedonbehalfby)
- [organization_appconfiginstance](#BKMK_organization_appconfiginstance)

### <a name="BKMK_appconfig_appconfiginstance"></a> appconfig_appconfiginstance

One-To-Many Relationship: [appconfig appconfig_appconfiginstance](appconfig.md#BKMK_appconfig_appconfiginstance)

|Property|Value|
|---|---|
|ReferencedEntity|`appconfig`|
|ReferencedAttribute|`appconfigid`|
|ReferencingAttribute|`appconfigid`|
|ReferencingEntityNavigationPropertyName|`appconfiginstance_appconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_appconfigmaster_appconfiginstance"></a> appconfigmaster_appconfiginstance

One-To-Many Relationship: [appconfigmaster appconfigmaster_appconfiginstance](appconfigmaster.md#BKMK_appconfigmaster_appconfiginstance)

|Property|Value|
|---|---|
|ReferencedEntity|`appconfigmaster`|
|ReferencedAttribute|`appconfigmasterid`|
|ReferencingAttribute|`appconfigmasterid`|
|ReferencingEntityNavigationPropertyName|`appconfiginstance_appconfigmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_appconfiginstance_createdby"></a> lk_appconfiginstance_createdby

One-To-Many Relationship: [systemuser lk_appconfiginstance_createdby](systemuser.md#BKMK_lk_appconfiginstance_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`appconfiginstance_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appconfiginstance_createdonbehalfby"></a> lk_appconfiginstance_createdonbehalfby

One-To-Many Relationship: [systemuser lk_appconfiginstance_createdonbehalfby](systemuser.md#BKMK_lk_appconfiginstance_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`appconfiginstance_createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appconfiginstance_modifiedby"></a> lk_appconfiginstance_modifiedby

One-To-Many Relationship: [systemuser lk_appconfiginstance_modifiedby](systemuser.md#BKMK_lk_appconfiginstance_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`appconfiginstance_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appconfiginstance_modifiedonbehalfby"></a> lk_appconfiginstance_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_appconfiginstance_modifiedonbehalfby](systemuser.md#BKMK_lk_appconfiginstance_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`appconfiginstance_modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_appconfiginstance"></a> organization_appconfiginstance

One-To-Many Relationship: [organization organization_appconfiginstance](organization.md#BKMK_organization_appconfiginstance)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organization_appconfiginstance_appconfiginstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.appconfiginstance?displayProperty=fullName>
