---
title: "Data Map (ImportMap) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Data Map (ImportMap) table/entity with Microsoft Dataverse."
ms.date: 11/09/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Data Map (ImportMap) table/entity reference

Data map used in import.

## Messages

The following table lists the messages for the Data Map (ImportMap) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: False |`PATCH` /importmaps(*importmapid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Create`<br />Event: False |`POST` /importmaps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /importmaps(*importmapid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `ExportMappingsImportMap`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ExportMappingsImportMap?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ExportMappingsImportMapRequest>|
| `GrantAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ImportMappingsImportMap`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ImportMappingsImportMap?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ImportMappingsImportMapRequest>|
| `ModifyAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /importmaps(*importmapid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /importmaps<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: False |`PATCH` /importmaps(*importmapid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /importmaps(*importmapid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /importmaps(*importmapid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Data Map (ImportMap) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Data Map** |
| **DisplayCollectionName** | **Data Maps** |
| **SchemaName** | `ImportMap` |
| **CollectionSchemaName** | `ImportMaps` |
| **EntitySetName** | `importmaps`|
| **LogicalName** | `importmap` |
| **LogicalCollectionName** | `importmaps` |
| **PrimaryIdAttribute** | `importmapid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [EntitiesPerFile](#BKMK_EntitiesPerFile)
- [ImportMapId](#BKMK_ImportMapId)
- [ImportMapType](#BKMK_ImportMapType)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsWizardCreated](#BKMK_IsWizardCreated)
- [MapCustomizations](#BKMK_MapCustomizations)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Source](#BKMK_Source)
- [SourceType](#BKMK_SourceType)
- [SourceUserIdentifierForSourceCRMUserLink](#BKMK_SourceUserIdentifierForSourceCRMUserLink)
- [SourceUserIdentifierForSourceDataSourceUserLink](#BKMK_SourceUserIdentifierForSourceDataSourceUserLink)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TargetUserIdentifierForSourceCRMUserLink](#BKMK_TargetUserIdentifierForSourceCRMUserLink)

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the data map, such as the intended use or data source.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_EntitiesPerFile"></a> EntitiesPerFile

|Property|Value|
|---|---|
|Description|**Choose whether a data file can contain data for one or more record types.**|
|DisplayName|**Entities Per File**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitiesperfile`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importmap_entitiesperfile`|

#### EntitiesPerFile Choices/Options

|Value|Label|
|---|---|
|1|**Single Entity Per File**|
|2|**Multiple Entities Per File**|

### <a name="BKMK_ImportMapId"></a> ImportMapId

|Property|Value|
|---|---|
|Description|**Unique identifier of the data map.**|
|DisplayName|**Data Map**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importmapid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ImportMapType"></a> ImportMapType

|Property|Value|
|---|---|
|Description|**Select the type of data map to distinguish out-of-the-box data maps from custom maps.**|
|DisplayName|**Map Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`importmaptype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importmap_importmaptype`|

#### ImportMapType Choices/Options

|Value|Label|
|---|---|
|1|**Standard**|
|2|**Out of Box**|
|3|**In Process**|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the component is introduced.**|
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

### <a name="BKMK_IsWizardCreated"></a> IsWizardCreated

|Property|Value|
|---|---|
|Description|**Information about whether this data map was created by the Data Migration Manager.**|
|DisplayName|**Is Wizard-Created**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iswizardcreated`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`importmap_iswizardcreated`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_MapCustomizations"></a> MapCustomizations

|Property|Value|
|---|---|
|Description|**Customizations XML**|
|DisplayName|**Map Customizations**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mapcustomizations`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a descriptive name for the data map.**|
|DisplayName|**Map Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_Source"></a> Source

|Property|Value|
|---|---|
|Description|**Type the name of the migration source that this data map is used for.**|
|DisplayName|**Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`source`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_SourceType"></a> SourceType

|Property|Value|
|---|---|
|Description|**Select the migration source type that this data map is used for.**|
|DisplayName|**Source System Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importmap_sourcetype`|

#### SourceType Choices/Options

|Value|Label|
|---|---|
|1|**Map For SalesForce.com Full Data Export**|
|2|**Map For SalesForce.com Report Export**|
|3|**Map For SalesForce.com Contact and Account Report Export**|
|4|**Microsoft Office Outlook 2010 with Business Contact Manager**|
|5|**Generic Map for Contact and Account**|

### <a name="BKMK_SourceUserIdentifierForSourceCRMUserLink"></a> SourceUserIdentifierForSourceCRMUserLink

|Property|Value|
|---|---|
|Description|**Source user value for source Microsoft Dynamics 365 user link.**|
|DisplayName|**Source User Value**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourceuseridentifierforsourcecrmuserlink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_SourceUserIdentifierForSourceDataSourceUserLink"></a> SourceUserIdentifierForSourceDataSourceUserLink

|Property|Value|
|---|---|
|Description|**Column in the source file that uniquely identifies a user.**|
|DisplayName|**Source User Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourceuseridentifierforsourcedatasourceuserlink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the data map is active or inactive. Inactive data maps are read-only and can't be edited.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`importmap_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the data map's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue|1|
|GlobalChoiceName|`importmap_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TargetUserIdentifierForSourceCRMUserLink"></a> TargetUserIdentifierForSourceCRMUserLink

|Property|Value|
|---|---|
|Description|**Microsoft Dynamics 365 user.**|
|DisplayName|**Target User Value**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`targetuseridentifierforsourcecrmuserlink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ImportMapIdUnique](#BKMK_ImportMapIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [IsValidForImport](#BKMK_IsValidForImport)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TargetEntity](#BKMK_TargetEntity)

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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
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

### <a name="BKMK_ImportMapIdUnique"></a> ImportMapIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the ImortMap.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importmapidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component is managed.**|
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_IsValidForImport"></a> IsValidForImport

|Property|Value|
|---|---|
|Description|**Information about whether the data map is valid for use with data import.**|
|DisplayName|**Is Valid For Import**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvalidforimport`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`importmap_isvalidforimport`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|SystemRequired|
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

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Business unit that owns the data map.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier of the team who owns the data map.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the data map.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_TargetEntity"></a> TargetEntity

|Property|Value|
|---|---|
|Description|**Select the name of the Microsoft Dynamics 365 record type that this data map is defined for.**|
|DisplayName|**Record Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetentity`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`importmap_targetentity`|

#### TargetEntity Choices/Options

|Value|Label|
|---|---|
|1|**Account**|
|2|**Contact**|
|5|**Note**|
|6|**Business Unit Map**|
|7|**Owner**|
|8|**User**|
|9|**Team**|
|10|**Business Unit**|
|14|**System User Principal**|
|29|**Subscription**|
|30|**Filter Template**|
|31|**Privilege Object Type Code**|
|33|**Subscription Synchronization Information**|
|35|**Tracking information for deleted entities**|
|36|**Client update**|
|37|**Subscription Manually Tracked Object**|
|42|**SystemUser BusinessUnit Entity Map**|
|44|**Field Sharing**|
|45|**Subscription Statistic Offline**|
|46|**Subscription Statistic Outlook**|
|47|**Subscription Sync Entry Offline**|
|48|**Subscription Sync Entry Outlook**|
|50|**Position**|
|51|**System User Manager Map**|
|52|**User Search Facet**|
|54|**Global Search Configuration**|
|55|**FileAttachment**|
|60|**SystemUserAuthorizationChangeTracker**|
|61|**PrincipalEntityBusinessUnitMap**|
|72|**Record Filter**|
|73|**EntityRecordFilter**|
|74|**Secured Masking Rule**|
|75|**Privilege Checker Run**|
|76|**Privilege Checker Log**|
|78|**Virtual Entity Data Provider**|
|85|**Virtual Entity Data Source**|
|92|**Team template**|
|99|**Social Profile**|
|101|**Service Plan**|
|103|**Privileges Removal Setting**|
|126|**Indexed Article**|
|127|**Article**|
|129|**Subject**|
|132|**Announcement**|
|135|**Activity Party**|
|150|**User Settings**|
|300|**Canvas App**|
|301|**Callback Registration**|
|372|**Connector**|
|373|**Connection Instance**|
|380|**Environment Variable Definition**|
|381|**Environment Variable Value**|
|400|**AI Template**|
|401|**AI Model**|
|402|**AI Configuration**|
|418|**Dataflow**|
|430|**Entity Analytics Config**|
|431|**Image Attribute Configuration**|
|432|**Entity Image Configuration**|
|950|**New Process**|
|951|**Translation Process**|
|955|**Expired Process**|
|1001|**Attachment**|
|1002|**Attachment**|
|1003|**Internal Address**|
|1007|**Image Descriptor**|
|1016|**Article Template**|
|1019|**Organization**|
|1021|**Organization UI**|
|1023|**Privilege**|
|1030|**System Form**|
|1031|**User Dashboard**|
|1036|**Security Role**|
|1037|**Role Template**|
|1039|**View**|
|1043|**String Map**|
|1071|**Address**|
|1072|**Subscription Clients**|
|1075|**Status Map**|
|1082|**Article Comment**|
|1086|**User Fiscal Calendar**|
|1094|**Authorization Server**|
|1095|**Partner Application**|
|1111|**System Chart**|
|1112|**User Chart**|
|1113|**Ribbon Tab To Command Mapping**|
|1115|**Ribbon Context Group**|
|1116|**Ribbon Command**|
|1117|**Ribbon Rule**|
|1120|**Application Ribbons**|
|1130|**Ribbon Difference**|
|1140|**Replication Backlog**|
|1189|**Document Suggestions**|
|1190|**SuggestionCardTemplate**|
|1200|**Field Security Profile**|
|1201|**Field Permission**|
|1203|**Team Profiles**|
|1204|**Application**|
|1234|**Channel Property Group**|
|1236|**Channel Property**|
|1300|**SocialInsightsConfiguration**|
|1309|**Saved Organization Insights Configuration**|
|1400|**Sync Attribute Mapping Profile**|
|1401|**Sync Attribute Mapping**|
|1403|**Team Sync-Attribute Mapping Profiles**|
|1404|**Principal Sync Attribute Map**|
|2000|**Annual Fiscal Calendar**|
|2001|**Semiannual Fiscal Calendar**|
|2002|**Quarterly Fiscal Calendar**|
|2003|**Monthly Fiscal Calendar**|
|2004|**Fixed Monthly Fiscal Calendar**|
|2010|**Email Template**|
|2012|**Unresolved Address**|
|2013|**Territory**|
|2015|**Theme**|
|2016|**User Mapping**|
|2020|**Queue**|
|2023|**QueueItemCount**|
|2024|**QueueMemberCount**|
|2027|**License**|
|2029|**Queue Item**|
|2500|**User Entity UI Settings**|
|2501|**User Entity Instance Data**|
|3000|**Integration Status**|
|3005|**Channel Access Profile**|
|3008|**External Party**|
|3231|**Connection Role**|
|3233|**Connection Role Object Type Code**|
|3234|**Connection**|
|4003|**Calendar**|
|4004|**Calendar Rule**|
|4011|**Inter Process Lock**|
|4023|**Email Hash**|
|4101|**Display String Map**|
|4102|**Display String**|
|4110|**Notification**|
|4120|**Exchange Sync Id Mapping**|
|4200|**Activity**|
|4201|**Appointment**|
|4202|**Email**|
|4204|**Fax**|
|4207|**Letter**|
|4210|**Phone Call**|
|4212|**Task**|
|4216|**Social Activity**|
|4220|**UntrackedEmail**|
|4230|**Saved View**|
|4231|**Metadata Difference**|
|4232|**Business Data Localized Label**|
|4250|**Recurrence Rule**|
|4251|**Recurring Appointment**|
|4299|**Email Search**|
|4410|**Data Import**|
|4411|**Data Map**|
|4412|**Import Source File**|
|4413|**Import Data**|
|4414|**Duplicate Detection Rule**|
|4415|**Duplicate Record**|
|4416|**Duplicate Rule Condition**|
|4417|**Column Mapping**|
|4418|**List Value Mapping**|
|4419|**Lookup Mapping**|
|4420|**Owner Mapping**|
|4423|**Import Log**|
|4424|**Bulk Delete Operation**|
|4425|**Bulk Delete Failure**|
|4426|**Transformation Mapping**|
|4427|**Transformation Parameter Mapping**|
|4428|**Import Entity Mapping**|
|4450|**Data Performance Dashboard**|
|4490|**Office Document**|
|4500|**Relationship Role**|
|4501|**Relationship Role Map**|
|4502|**Customer Relationship**|
|4567|**Auditing**|
|4579|**Ribbon Client Metadata.**|
|4600|**Entity Map**|
|4601|**Attribute Map**|
|4602|**Plug-in Type**|
|4603|**Plug-in Type Statistic**|
|4605|**Plug-in Assembly**|
|4606|**Sdk Message**|
|4607|**Sdk Message Filter**|
|4608|**Sdk Message Processing Step**|
|4609|**Sdk Message Request**|
|4610|**Sdk Message Response**|
|4611|**Sdk Message Response Field**|
|4613|**Sdk Message Pair**|
|4614|**Sdk Message Request Field**|
|4615|**Sdk Message Processing Step Image**|
|4616|**Sdk Message Processing Step Secure Configuration**|
|4618|**Service Endpoint**|
|4619|**Plug-in Trace Log**|
|4700|**System Job**|
|4702|**Workflow Wait Subscription**|
|4703|**Process**|
|4704|**Process Dependency**|
|4705|**ISV Config**|
|4706|**Process Log**|
|4707|**Application File**|
|4708|**Organization Statistic**|
|4709|**Site Map**|
|4710|**Process Session**|
|4711|**Expander Event**|
|4712|**Process Trigger**|
|4720|**Flow Session**|
|4724|**Process Stage**|
|4725|**Business Process Flow Instance**|
|4800|**Web Wizard**|
|4802|**Wizard Page**|
|4803|**Web Wizard Access Privilege**|
|4810|**Time Zone Definition**|
|4811|**Time Zone Rule**|
|4812|**Time Zone Localized Name**|
|5000|**Recently Used**|
|5004|**NL2SQ Registration Information**|
|7000|**System Application Metadata**|
|7001|**User Application Metadata**|
|7100|**Solution**|
|7101|**Publisher**|
|7102|**Publisher Address**|
|7103|**Solution Component**|
|7104|**Solution Component Definition**|
|7105|**Dependency**|
|7106|**Dependency Node**|
|7107|**Invalid Dependency**|
|7108|**Dependency Feature**|
|7200|**RuntimeDependency**|
|7755|**ElasticFileAttachment**|
|8000|**Post**|
|8001|**Post Role**|
|8002|**Post Regarding**|
|8003|**Follow**|
|8005|**Comment**|
|8006|**Like**|
|8040|**ACIViewMapper**|
|8050|**Trace**|
|8051|**Trace Association**|
|8052|**Trace Regarding**|
|8181|**Routing Rule Set**|
|8199|**Rule Item**|
|8700|**AppModule Metadata**|
|8701|**AppModule Metadata Dependency**|
|8702|**AppModule Metadata Async Operation**|
|8840|**Hierarchy Rule**|
|9006|**Model-driven App**|
|9007|**App Module Component**|
|9009|**App Module Roles**|
|9011|**App Config Master**|
|9012|**App Configuration**|
|9013|**App Configuration Instance**|
|9100|**Report**|
|9101|**Report Related Entity**|
|9102|**Report Related Category**|
|9103|**Report Visibility**|
|9104|**Report Link**|
|9105|**Currency**|
|9106|**Mail Merge Template**|
|9107|**Import Job**|
|9201|**LocalConfigStore**|
|9300|**Record Creation and Update Rule**|
|9301|**Record Creation and Update Rule Item**|
|9333|**Web Resource**|
|9400|**Channel Access Profile Rule**|
|9401|**Channel Access Profile Rule Item**|
|9502|**SharePoint Site**|
|9507|**Sharepoint Document**|
|9508|**Document Location**|
|9509|**SharePoint Data**|
|9510|**Rollup Properties**|
|9511|**Rollup Job**|
|9600|**Goal**|
|9602|**Rollup Query**|
|9603|**Goal Metric**|
|9604|**Rollup Field**|
|9605|**Email Server Profile**|
|9606|**Mailbox**|
|9607|**Mailbox Statistics**|
|9608|**Mailbox Auto Tracking Folder**|
|9609|**Mailbox Tracking Category**|
|9650|**Process Configuration**|
|9690|**Organization Insights Notification**|
|9699|**Organization Insights Metric**|
|9750|**SLA**|
|9751|**SLA Item**|
|9752|**SLA KPI Instance**|
|9753|**Custom Control**|
|9754|**Custom Control Resource**|
|9755|**Custom Control Default Config**|
|9800|**Entity**|
|9808|**Attribute**|
|9809|**OptionSet**|
|9810|**Entity Key**|
|9811|**Entity Relationship**|
|9812|**Managed Property**|
|9813|**Relationship Entity**|
|9814|**Relationship Attribute**|
|9815|**Entity Index**|
|9816|**Index Attribute**|
|9820|**Secured Masking Column**|
|9866|**Mobile Offline Profile**|
|9867|**Mobile Offline Profile Item**|
|9868|**Mobile Offline Profile Item Association**|
|9869|**Sync Error**|
|9870|**Offline Command Definition**|
|9875|**Language Provisioning State**|
|9880|**Ribbon Metadata To Process**|
|9890|**SolutionHistoryData**|
|9900|**Navigation Setting**|
|9910|**MultiEntitySearch**|
|9912|**Multi Select Option Value**|
|9919|**Hierarchy Security Configuration**|
|9930|**Knowledge Base Record**|
|9932|**Time Stamp Date Mapping**|
|9936|**Azure Service Connection**|
|9940|**Document Template**|
|9941|**Personal Document Template**|
|9945|**Text Analytics Entity Mapping**|
|9947|**Knowledge Search Model**|
|9949|**Advanced Similarity Rule**|
|9950|**Office Graph Document**|
|9951|**Similarity Rule**|
|9953|**Knowledge Article**|
|9955|**Knowledge Article Views**|
|9957|**Language**|
|9958|**Feedback**|
|9959|**Category**|
|9960|**Knowledge Article Category**|
|9961|**DelveActionHub**|
|9962|**Action Card**|
|9968|**ActionCardUserState**|
|9973|**Action Card User Settings**|
|9983|**Action Card Type**|
|9986|**Interaction for Email**|
|9987|**External Party Item**|
|9996|**HolidayWrapper**|
|9997|**Email Signature**|
|10000|**Solution Component Attribute Configuration**|
|10001|**Solution Component Batch Configuration**|
|10002|**Solution Component Configuration**|
|10003|**Solution Component Relationship Configuration**|
|10004|**Solution History**|
|10005|**Solution History Data Source**|
|10006|**Component Layer**|
|10007|**Component Layer Data Source**|
|10008|**Package**|
|10009|**Package History**|
|10011|**StageSolutionUpload**|
|10012|**ExportSolutionUpload**|
|10013|**FeatureControlSetting**|
|10014|**Solution Component Summary**|
|10015|**Solution Component Count Summary**|
|10016|**Solution Component Data Source**|
|10017|**Solution Component Count Data Source**|
|10018|**Microsoft Entra ID**|
|10019|**Staged Entity**|
|10020|**Staged Entity Attribute**|
|10021|**Staged Metadata Async Operation**|
|10022|**Key Vault Reference**|
|10023|**Managed Identity**|
|10024|**Catalog**|
|10025|**Catalog Assignment**|
|10026|**Internal Catalog Assignment**|
|10027|**Custom API**|
|10028|**Custom API Request Parameter**|
|10029|**Custom API Response Property**|
|10030|**Plugin Package**|
|10031|**NonRelational Data Source**|
|10032|**ProvisionLanguageForUser**|
|10033|**Shared Object**|
|10034|**Shared Workspace**|
|10035|**Shared Workspace Access Token**|
|10036|**Shared Workspace Pool**|
|10037|**Data Lake Folder**|
|10038|**Data Lake Folder Permission**|
|10039|**Data Lake Workspace**|
|10040|**Data Lake Workspace Permission**|
|10041|**Data Processing configuration**|
|10042|**Exported Excel**|
|10043|**RetainedData Excel**|
|10044|**Synapse Database**|
|10045|**Synapse Link External Table State**|
|10046|**Synapse Link Profile**|
|10047|**Synapse Link Profile Entity**|
|10048|**Synapse Link Profile Entity State**|
|10049|**Synapse Link Schedule**|
|10050|**Component Version**|
|10051|**Component Version Data Source**|
|10052|**Component Version (Internal)**|
|10053|**Git Branch**|
|10054|**Git Configuration Retrieval Data Source**|
|10055|**Git Organization**|
|10056|**Git Project**|
|10057|**Git Repository**|
|10058|**Source Control Branch Configuration**|
|10059|**Source Control Component**|
|10060|**Source Control Component Payload**|
|10061|**Source Control Configuration**|
|10062|**DataflowRefreshHistory**|
|10063|**EntityRefreshHistory**|
|10064|**Shared Link Setting**|
|10065|**DelegatedAuthorization**|
|10067|**CascadeGrantRevokeAccessRecordsTracker**|
|10068|**CascadeGrantRevokeAccessVersionTracker**|
|10069|**RevokeInheritedAccessRecordsTracker**|
|10070|**TdsMetadata**|
|10071|**Model-Driven App Element**|
|10072|**Model-Driven App Component Node's Edge**|
|10073|**Model-Driven App Component Node**|
|10074|**Model-Driven App Setting**|
|10075|**Model-Driven App User Setting**|
|10076|**Organization Setting**|
|10077|**Setting Definition**|
|10078|**CanvasApp Extended Metadata**|
|10079|**Service Plan Mapping**|
|10080|**Service Plan Custom Control**|
|10082|**ApplicationUser**|
|10085|**OData v4 Data Source**|
|10086|**Workflow Binary**|
|10087|**Credential**|
|10088|**Desktop Flow Module**|
|10089|**Flow Capacity Assignment**|
|10090|**Flow Credential Application**|
|10091|**Flow Event**|
|10092|**Flow Machine**|
|10093|**Flow Machine Group**|
|10094|**Flow Machine Image**|
|10095|**Flow Machine Image Version**|
|10096|**Flow Machine Network**|
|10097|**ProcessStageParameter**|
|10098|**Work Queue**|
|10099|**Work Queue Item**|
|10100|**Desktop Flow Binary**|
|10101|**Flow Log**|
|10102|**Flow Run**|
|10103|**Action Approval Model**|
|10104|**Approval**|
|10105|**Approval Request**|
|10106|**Approval Response**|
|10107|**Approval Step**|
|10108|**Await All Action Approval Model**|
|10109|**Await All Approval Model**|
|10110|**Basic Approval Model Data**|
|10111|**Flow Approval**|
|10120|**Connection Reference**|
|10121|**DVFileSearch**|
|10122|**DVFileSearchAttribute**|
|10123|**DVFileSearchEntity**|
|10124|**DVTableSearch**|
|10125|**DVTableSearchAttribute**|
|10126|**DVTableSearchEntity**|
|10127|**AICopilot**|
|10128|**AIPluginAuth**|
|10129|**AI Plugin Conversation Starter**|
|10130|**AI Plugin Conversation Starter Mapping**|
|10131|**AI Plugin Governance**|
|10132|**AI Plugin Governance Extended**|
|10133|**AIPluginOperationResponseTemplate**|
|10134|**AIPluginTitle**|
|10135|**SideloadedAIPlugin**|
|10136|**AIPlugin**|
|10137|**AIPluginExternalSchema**|
|10138|**AIPluginExternalSchemaProperty**|
|10139|**AIPluginInstance**|
|10140|**AIPluginOperation**|
|10141|**AIPluginOperationParameter**|
|10142|**AIPluginUserSetting**|
|10144|**AI Event**|
|10145|**AI Builder Feedback Loop**|
|10146|**AI Form Processing Document**|
|10147|**AI Object Detection Image**|
|10148|**AI Object Detection Label**|
|10149|**AI Object Detection Bounding Box**|
|10150|**AI Object Detection Image Mapping**|
|10152|**AI Builder Dataset**|
|10153|**AI Builder Dataset File**|
|10154|**AI Builder Dataset Record**|
|10155|**AI Builder Datasets Container**|
|10156|**AI Builder File**|
|10157|**AI Builder File Attached Data**|
|10158|**Help Page**|
|10159|**Tour**|
|10160|**BotContent**|
|10161|**ConversationTranscript**|
|10162|**Copilot**|
|10163|**Copilot component**|
|10164|**Copilot component collection**|
|10175|**Comment**|
|10176|**Governance Configuration**|
|10177|**Fabric AISkill**|
|10178|**App Insights Metadata**|
|10179|**Dataflow Connection Reference**|
|10180|**Schedule**|
|10181|**Dataflow Template**|
|10182|**Dataflow DatalakeFolder**|
|10183|**Data Movement Service Request**|
|10184|**Data Movement Service Request Status**|
|10185|**DMS Sync Request**|
|10186|**DMS Sync Status**|
|10187|**Knowledge Asset Configuration**|
|10188|**Module Run Detail**|
|10189|**Salesforce Structured Object**|
|10190|**Salesforce Structured QnA Config**|
|10191|**Workflow Action Status**|
|10192|**FederatedKnowledgeConfiguration**|
|10193|**FederatedKnowledgeEntityConfiguration**|
|10194|**Form Mapping**|
|10195|**PDF Setting**|
|10196|**Activity File Attachment**|
|10197|**Teams chat**|
|10198|**Service Configuration**|
|10199|**SLA KPI**|
|10200|**Integrated search provider**|
|10201|**Knowledge Management Setting**|
|10202|**Knowledge Federated Article**|
|10203|**Knowledge Federated Article Incident**|
|10204|**Search provider**|
|10205|**Knowledge Article Image**|
|10206|**Knowledge Configuration**|
|10207|**Knowledge Interaction Insight**|
|10208|**Knowledge Search Insight**|
|10209|**Favorite knowledge article**|
|10210|**Knowledge article language setting**|
|10211|**Knowledge Article Attachment**|
|10212|**Knowledge personalization**|
|10213|**Knowledge Article Template**|
|10214|**Knowledge search personal filter config**|
|10215|**Knowledge search filter**|
|10217|**msdyn_historicalcaseharvestbatch**|
|10218|**msdyn_historicalcaseharvestrun**|
|10219|**Knowledge Harvest Job Record**|
|10220|**SupportUserTable**|
|10221|**FxExpression**|
|10222|**Plug-in**|
|10223|**PowerfxRule**|
|10224|**Planner Business Scenario**|
|10225|**Planner Sync Action**|
|10226|**Ms Graph Resource To Subscription**|
|10227|**Virtual Entity  Metadata**|
|10228|**Background Operation**|
|10229|**Report Parameter**|
|10230|**MobileOfflineProfileExtension**|
|10231|**MobileOfflineProfileItemFilter**|
|10232|**TeamMobileOfflineProfileMembership**|
|10233|**UserMobileOfflineProfileMembership**|
|10234|**OrganizationDataSyncSubscription**|
|10235|**OrganizationDataSyncSubscriptionEntity**|
|10236|**OrganizationDataSyncSubscriptionFnoTable**|
|10237|**OrganizationDataSyncFnoState**|
|10238|**OrganizationDataSyncState**|
|10239|**ArchiveCleanupInfo**|
|10240|**ArchiveCleanupOperation**|
|10241|**BulkArchiveConfig**|
|10242|**BulkArchiveFailureDetail**|
|10243|**BulkArchiveOperation**|
|10244|**BulkArchiveOperationDetail**|
|10245|**EnableArchivalRequest**|
|10246|**MetadataForArchival**|
|10247|**ReconciliationEntityInfo**|
|10248|**ReconciliationEntityStepInfo**|
|10249|**ReconciliationInfo**|
|10250|**RetentionCleanupInfo**|
|10251|**RetentionCleanupOperation**|
|10252|**RetentionConfig**|
|10253|**RetentionFailureDetail**|
|10254|**RetentionOperation**|
|10255|**RetentionOperationDetail**|
|10256|**RetentionSuccessDetail**|
|10257|**CertificateCredential**|
|10258|**Notification**|
|10259|**User Rating**|
|10260|**Mobile App**|
|10261|**Insights Store Data Source**|
|10262|**Insights Store Virtual Entity**|
|10263|**RoleEditorLayout**|
|10264|**Deleted Record Reference**|
|10265|**Restore Deleted Records Configuration**|
|10266|**App Action**|
|10267|**App Action Migration**|
|10268|**App Action Rule**|
|10271|**Card**|
|10272|**Card State Item**|
|10275|**Entity link chat configuration**|
|10276|**AI Skill Config**|
|10277|**Rich Text Attachment**|
|10278|**Custom Control Extended Setting**|
|10279|**Timeline Pin**|
|10280|**Virtual Connector Data Source**|
|10281|**Virtual Table Column Candidate**|
|10283|**PM Analysis History**|
|10284|**PM Business Rule Automation Config**|
|10285|**PM Calendar**|
|10286|**PM Calendar Version**|
|10287|**PM Inferred Task**|
|10288|**PM Process Extended Metadata Version**|
|10289|**PM Process Template**|
|10290|**PM Process User Settings**|
|10291|**PM Process Version**|
|10292|**PM Recording**|
|10293|**PM Simulation**|
|10294|**PM Template**|
|10295|**PM View**|
|10296|**Analysis Component**|
|10297|**Analysis Job**|
|10298|**Analysis Override**|
|10299|**Analysis Result**|
|10300|**Analysis Result Detail**|
|10301|**Solution Health Rule**|
|10302|**Solution Health Rule Argument**|
|10303|**Solution Health Rule Set**|
|10304|**Power BI Dataset**|
|10305|**powerbidatasetapdx**|
|10306|**Power BI Mashup Parameter**|
|10307|**Power BI Report**|
|10308|**powerbireportapdx**|
|10309|**File Upload**|
|10310|**MainFewShot**|
|10311|**MakerFewShot**|
|10312|**SearchAttributeSettings**|
|10313|**SearchCustomAnalyzer**|
|10314|**SearchRelationshipSettings**|
|10315|**SearchResultsCache**|
|10316|**Search Telemetry**|
|10317|**ViewAsExampleQuestion**|
|10318|**CopilotExampleQuestion**|
|10319|**CopilotGlossaryTerm**|
|10320|**CopilotSynonyms**|
|10321|**API Request Cache**|
|10322|**API Request Folder**|
|10323|**Site Component**|
|10324|**Site**|
|10325|**Site Language**|
|10326|**Power Pages Site Published**|
|10329|**External Identity**|
|10330|**Invitation**|
|10331|**Invite Redemption**|
|10332|**Portal Comment**|
|10333|**Setting**|
|10334|**Multistep Form Session**|
|10338|**Ad Placement**|
|10339|**Column Permission**|
|10340|**Column Permission Profile**|
|10341|**Content Snippet**|
|10342|**Basic Form**|
|10343|**Basic Form Metadata**|
|10344|**List**|
|10345|**Table Permission**|
|10346|**Page Template**|
|10347|**Poll Placement**|
|10348|**Power Pages Core Entity DS**|
|10349|**Publishing State**|
|10350|**Publishing State Transition Rule**|
|10351|**Redirect**|
|10352|**Shortcut**|
|10353|**Site Marker**|
|10354|**Site Setting**|
|10355|**Web File**|
|10356|**Multistep Form**|
|10357|**Multistep Form Metadata**|
|10358|**Form Step**|
|10359|**Web Link**|
|10360|**Web Link Set**|
|10361|**Web Page**|
|10362|**Web Page Access Control Rule**|
|10363|**Web Role**|
|10364|**Website**|
|10365|**Website Access**|
|10366|**Website Language**|
|10367|**Web Template**|
|10374|**Power Pages Scan Report**|
|10375|**Power Pages Log**|
|10376|**PowerPagesManagedIdentity**|
|10377|**Power Pages Site AI Feedback**|
|10382|**Catalog Submission Files**|
|10383|**Package Submission Store**|
|18085|**Event Expander Breadcrumb**|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [BusinessUnit_ImportMaps](#BKMK_BusinessUnit_ImportMaps)
- [lk_importmap_createdonbehalfby](#BKMK_lk_importmap_createdonbehalfby)
- [lk_importmap_modifiedonbehalfby](#BKMK_lk_importmap_modifiedonbehalfby)
- [lk_importmapbase_createdby](#BKMK_lk_importmapbase_createdby)
- [lk_importmapbase_modifiedby](#BKMK_lk_importmapbase_modifiedby)
- [owner_importmaps](#BKMK_owner_importmaps)
- [SystemUser_ImportMaps](#BKMK_SystemUser_ImportMaps)
- [team_ImportMaps](#BKMK_team_ImportMaps)

### <a name="BKMK_BusinessUnit_ImportMaps"></a> BusinessUnit_ImportMaps

One-To-Many Relationship: [businessunit BusinessUnit_ImportMaps](businessunit.md#BKMK_BusinessUnit_ImportMaps)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importmap_createdonbehalfby"></a> lk_importmap_createdonbehalfby

One-To-Many Relationship: [systemuser lk_importmap_createdonbehalfby](systemuser.md#BKMK_lk_importmap_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importmap_modifiedonbehalfby"></a> lk_importmap_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_importmap_modifiedonbehalfby](systemuser.md#BKMK_lk_importmap_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importmapbase_createdby"></a> lk_importmapbase_createdby

One-To-Many Relationship: [systemuser lk_importmapbase_createdby](systemuser.md#BKMK_lk_importmapbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importmapbase_modifiedby"></a> lk_importmapbase_modifiedby

One-To-Many Relationship: [systemuser lk_importmapbase_modifiedby](systemuser.md#BKMK_lk_importmapbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_importmaps"></a> owner_importmaps

One-To-Many Relationship: [owner owner_importmaps](owner.md#BKMK_owner_importmaps)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_ImportMaps"></a> SystemUser_ImportMaps

One-To-Many Relationship: [systemuser SystemUser_ImportMaps](systemuser.md#BKMK_SystemUser_ImportMaps)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_ImportMaps"></a> team_ImportMaps

One-To-Many Relationship: [team team_ImportMaps](team.md#BKMK_team_ImportMaps)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [ColumnMapping_ImportMap](#BKMK_ColumnMapping_ImportMap)
- [ImportEntityMapping_ImportMap](#BKMK_ImportEntityMapping_ImportMap)
- [ImportMap_AsyncOperations](#BKMK_ImportMap_AsyncOperations)
- [ImportMap_BulkDeleteFailures](#BKMK_ImportMap_BulkDeleteFailures)
- [ImportMap_ImportFile](#BKMK_ImportMap_ImportFile)
- [ImportMap_SyncErrors](#BKMK_ImportMap_SyncErrors)
- [OwnerMapping_ImportMap](#BKMK_OwnerMapping_ImportMap)
- [TransformationMapping_ImportMap](#BKMK_TransformationMapping_ImportMap)

### <a name="BKMK_ColumnMapping_ImportMap"></a> ColumnMapping_ImportMap

Many-To-One Relationship: [columnmapping ColumnMapping_ImportMap](columnmapping.md#BKMK_ColumnMapping_ImportMap)

|Property|Value|
|---|---|
|ReferencingEntity|`columnmapping`|
|ReferencingAttribute|`importmapid`|
|ReferencedEntityNavigationPropertyName|`ColumnMapping_ImportMap`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportEntityMapping_ImportMap"></a> ImportEntityMapping_ImportMap

Many-To-One Relationship: [importentitymapping ImportEntityMapping_ImportMap](importentitymapping.md#BKMK_ImportEntityMapping_ImportMap)

|Property|Value|
|---|---|
|ReferencingEntity|`importentitymapping`|
|ReferencingAttribute|`importmapid`|
|ReferencedEntityNavigationPropertyName|`ImportEntityMapping_ImportMap`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportMap_AsyncOperations"></a> ImportMap_AsyncOperations

Many-To-One Relationship: [asyncoperation ImportMap_AsyncOperations](asyncoperation.md#BKMK_ImportMap_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ImportMap_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportMap_BulkDeleteFailures"></a> ImportMap_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure ImportMap_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ImportMap_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ImportMap_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportMap_ImportFile"></a> ImportMap_ImportFile

Many-To-One Relationship: [importfile ImportMap_ImportFile](importfile.md#BKMK_ImportMap_ImportFile)

|Property|Value|
|---|---|
|ReferencingEntity|`importfile`|
|ReferencingAttribute|`importmapid`|
|ReferencedEntityNavigationPropertyName|`ImportMap_ImportFile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportMap_SyncErrors"></a> ImportMap_SyncErrors

Many-To-One Relationship: [syncerror ImportMap_SyncErrors](syncerror.md#BKMK_ImportMap_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ImportMap_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_OwnerMapping_ImportMap"></a> OwnerMapping_ImportMap

Many-To-One Relationship: [ownermapping OwnerMapping_ImportMap](ownermapping.md#BKMK_OwnerMapping_ImportMap)

|Property|Value|
|---|---|
|ReferencingEntity|`ownermapping`|
|ReferencingAttribute|`importmapid`|
|ReferencedEntityNavigationPropertyName|`OwnerMapping_ImportMap`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransformationMapping_ImportMap"></a> TransformationMapping_ImportMap

Many-To-One Relationship: [transformationmapping TransformationMapping_ImportMap](transformationmapping.md#BKMK_TransformationMapping_ImportMap)

|Property|Value|
|---|---|
|ReferencingEntity|`transformationmapping`|
|ReferencingAttribute|`importmapid`|
|ReferencedEntityNavigationPropertyName|`TransformationMapping_ImportMap`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.importmap?displayProperty=fullName>
