---
title: "AIPlugin table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AIPlugin table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AIPlugin table/entity reference (Microsoft Dataverse)

AIPlugins component

## Messages

The following table lists the messages for the AIPlugin table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /aiplugins(*aipluginid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /aiplugins<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /aiplugins(*aipluginid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /aiplugins(*aipluginid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /aiplugins<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RetrieveUnpublished`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /aiplugins(*aipluginid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /aiplugins(*aipluginid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /aiplugins(*aipluginid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AIPlugin table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AIPlugin** |
| **DisplayCollectionName** | **AIPlugins** |
| **SchemaName** | `AIPlugin` |
| **CollectionSchemaName** | `AIPlugins` |
| **EntitySetName** | `aiplugins`|
| **LogicalName** | `aiplugin` |
| **LogicalCollectionName** | `aiplugins` |
| **PrimaryIdAttribute** | `aipluginid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AIPluginId](#BKMK_AIPluginId)
- [AIPluginTitle](#BKMK_AIPluginTitle)
- [Connector](#BKMK_Connector)
- [ContactEmail](#BKMK_ContactEmail)
- [HumanDescription](#BKMK_HumanDescription)
- [HumanName](#BKMK_HumanName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [LegalInfoUrl](#BKMK_LegalInfoUrl)
- [ModelDescription](#BKMK_ModelDescription)
- [ModelName](#BKMK_ModelName)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PluginAuthId](#BKMK_PluginAuthId)
- [PluginSubType](#BKMK_PluginSubType)
- [PluginType](#BKMK_PluginType)
- [PrivacyPolicyUrl](#BKMK_PrivacyPolicyUrl)
- [SchemaVersion](#BKMK_SchemaVersion)
- [SharedConnector](#BKMK_SharedConnector)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UpsertSwagger](#BKMK_UpsertSwagger)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AIPluginId"></a> AIPluginId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AIPlugin**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`aipluginid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AIPluginTitle"></a> AIPluginTitle

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aiplugintitle`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|aiplugintitle|

### <a name="BKMK_Connector"></a> Connector

|Property|Value|
|---|---|
|Description|**Connector reference for AIPlugin**|
|DisplayName|**Connector**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connector`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connector|

### <a name="BKMK_ContactEmail"></a> ContactEmail

|Property|Value|
|---|---|
|Description|**Contact Email**|
|DisplayName|**ContactEmail**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contactemail`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_HumanDescription"></a> HumanDescription

|Property|Value|
|---|---|
|Description|**Human-readable description of the Plugin**|
|DisplayName|**HumanDescription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`humandescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_HumanName"></a> HumanName

|Property|Value|
|---|---|
|Description|**Human-readable name for the model**|
|DisplayName|**HumanName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`humanname`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_LegalInfoUrl"></a> LegalInfoUrl

|Property|Value|
|---|---|
|Description|**Legal Info Url**|
|DisplayName|**LegalInfoUrl**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`legalinfourl`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ModelDescription"></a> ModelDescription

|Property|Value|
|---|---|
|Description|**Description better tailored to the model, such as token context length considerations or keyword usage for improved plugin prompting.**|
|DisplayName|**ModelDescription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modeldescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ModelName"></a> ModelName

|Property|Value|
|---|---|
|Description|**Model name for the plugin**|
|DisplayName|**ModelName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modelname`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
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
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_PluginAuthId"></a> PluginAuthId

|Property|Value|
|---|---|
|Description|**Auth reference for AIPlugin**|
|DisplayName|**PluginAuthId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pluginauthid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|aipluginauth|

### <a name="BKMK_PluginSubType"></a> PluginSubType

|Property|Value|
|---|---|
|Description||
|DisplayName|**PluginSubType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pluginsubtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`aipluginsubtype`|

#### PluginSubType Choices/Options

|Value|Label|
|---|---|
|0|**Dataverse**|
|1|**Certified Connector**|
|2|**QA**|
|3|**Flow**|
|4|**Prompt**|
|5|**Conversational**|
|6|**Custom Api**|
|7|**Rest Api**|
|8|**Custom Connector**|

### <a name="BKMK_PluginType"></a> PluginType

|Property|Value|
|---|---|
|Description||
|DisplayName|**PluginType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`plugintype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`aiplugintype`|

#### PluginType Choices/Options

|Value|Label|
|---|---|
|0|**Dataverse**|
|1|**CustomConnector**|
|2|**Connector**|
|3|**Flow**|

### <a name="BKMK_PrivacyPolicyUrl"></a> PrivacyPolicyUrl

|Property|Value|
|---|---|
|Description|**Privacy Policy Url**|
|DisplayName|**PrivacyPolicyUrl**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`privacypolicyurl`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_SchemaVersion"></a> SchemaVersion

|Property|Value|
|---|---|
|Description|**SchemaVersion of OpenAI Manifest**|
|DisplayName|**SchemaVersion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`schemaversion`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`openaischemaversion`|

#### SchemaVersion Choices/Options

|Value|Label|
|---|---|
|0|**1.0**|

### <a name="BKMK_SharedConnector"></a> SharedConnector

|Property|Value|
|---|---|
|Description|**SharedConnector Description**|
|DisplayName|**SharedConnector**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sharedconnector`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the AIPlugin**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`aiplugin_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the AIPlugin**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`aiplugin_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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

### <a name="BKMK_UpsertSwagger"></a> UpsertSwagger

|Property|Value|
|---|---|
|Description|**Swagger value that is upserted to generated plugin definition, used to provide override for properties not exposed as table/columns.Example:\{  "info": \{      "x-ms-keywords": \[ "sales", "support" \]   \}\}Adds x-ms-keywords in info property.**|
|DisplayName|**UpsertSwagger**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upsertswagger`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
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
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|DefaultFormValue||
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
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
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
|IsValidForForm|True|
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
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
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
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
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
|IsValidForForm|True|
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
|IsValidForForm|True|
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
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
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
|Description|**Yomi name of the owner**|
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
|Description|**Unique identifier for the business unit that owns the record**|
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
|Description|**Unique identifier for the team that owns the record.**|
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
|Description|**Unique identifier for the user that owns the record.**|
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

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [aiplugin_AIPluginTitle_aiplugintitle](#BKMK_aiplugin_AIPluginTitle_aiplugintitle)
- [AIPlugin_connector_connector](#BKMK_AIPlugin_connector_connector)
- [AIPluginAuth_AIPlugin](#BKMK_AIPluginAuth_AIPlugin)
- [business_unit_aiplugin](#BKMK_business_unit_aiplugin)
- [lk_aiplugin_createdby](#BKMK_lk_aiplugin_createdby)
- [lk_aiplugin_createdonbehalfby](#BKMK_lk_aiplugin_createdonbehalfby)
- [lk_aiplugin_modifiedby](#BKMK_lk_aiplugin_modifiedby)
- [lk_aiplugin_modifiedonbehalfby](#BKMK_lk_aiplugin_modifiedonbehalfby)
- [owner_aiplugin](#BKMK_owner_aiplugin)
- [team_aiplugin](#BKMK_team_aiplugin)
- [user_aiplugin](#BKMK_user_aiplugin)

### <a name="BKMK_aiplugin_AIPluginTitle_aiplugintitle"></a> aiplugin_AIPluginTitle_aiplugintitle

One-To-Many Relationship: [aiplugintitle aiplugin_AIPluginTitle_aiplugintitle](aiplugintitle.md#BKMK_aiplugin_AIPluginTitle_aiplugintitle)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`aiplugintitle`|
|ReferencingEntityNavigationPropertyName|`AIPluginTitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AIPlugin_connector_connector"></a> AIPlugin_connector_connector

One-To-Many Relationship: [connector AIPlugin_connector_connector](connector.md#BKMK_AIPlugin_connector_connector)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`connector`|
|ReferencingEntityNavigationPropertyName|`connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AIPluginAuth_AIPlugin"></a> AIPluginAuth_AIPlugin

One-To-Many Relationship: [aipluginauth AIPluginAuth_AIPlugin](aipluginauth.md#BKMK_AIPluginAuth_AIPlugin)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`pluginauthid`|
|ReferencingEntityNavigationPropertyName|`AIPluginAuth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_business_unit_aiplugin"></a> business_unit_aiplugin

One-To-Many Relationship: [businessunit business_unit_aiplugin](businessunit.md#BKMK_business_unit_aiplugin)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aiplugin_createdby"></a> lk_aiplugin_createdby

One-To-Many Relationship: [systemuser lk_aiplugin_createdby](systemuser.md#BKMK_lk_aiplugin_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aiplugin_createdonbehalfby"></a> lk_aiplugin_createdonbehalfby

One-To-Many Relationship: [systemuser lk_aiplugin_createdonbehalfby](systemuser.md#BKMK_lk_aiplugin_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aiplugin_modifiedby"></a> lk_aiplugin_modifiedby

One-To-Many Relationship: [systemuser lk_aiplugin_modifiedby](systemuser.md#BKMK_lk_aiplugin_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aiplugin_modifiedonbehalfby"></a> lk_aiplugin_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_aiplugin_modifiedonbehalfby](systemuser.md#BKMK_lk_aiplugin_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_aiplugin"></a> owner_aiplugin

One-To-Many Relationship: [owner owner_aiplugin](owner.md#BKMK_owner_aiplugin)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_aiplugin"></a> team_aiplugin

One-To-Many Relationship: [team team_aiplugin](team.md#BKMK_team_aiplugin)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_aiplugin"></a> user_aiplugin

One-To-Many Relationship: [systemuser user_aiplugin](systemuser.md#BKMK_user_aiplugin)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [AIPlugin_AIPluginConversationStarterMapping](#BKMK_AIPlugin_AIPluginConversationStarterMapping)
- [aiplugin_AsyncOperations](#BKMK_aiplugin_AsyncOperations)
- [aiplugin_BulkDeleteFailures](#BKMK_aiplugin_BulkDeleteFailures)
- [aiplugin_MailboxTrackingFolders](#BKMK_aiplugin_MailboxTrackingFolders)
- [aiplugin_PrincipalObjectAttributeAccesses](#BKMK_aiplugin_PrincipalObjectAttributeAccesses)
- [aiplugin_ProcessSession](#BKMK_aiplugin_ProcessSession)
- [aiplugin_SyncErrors](#BKMK_aiplugin_SyncErrors)
- [aiplugingovernance_aiplugin](#BKMK_aiplugingovernance_aiplugin)
- [AIPluginInstance_AIPlugin_AIPlugin](#BKMK_AIPluginInstance_AIPlugin_AIPlugin)
- [AIPluginOperation_AIPlugin_AIPlugin](#BKMK_AIPluginOperation_AIPlugin_AIPlugin)
- [sideloadedaiplugin_AIPlugin_aiplugin](#BKMK_sideloadedaiplugin_AIPlugin_aiplugin)

### <a name="BKMK_AIPlugin_AIPluginConversationStarterMapping"></a> AIPlugin_AIPluginConversationStarterMapping

Many-To-One Relationship: [aipluginconversationstartermapping AIPlugin_AIPluginConversationStarterMapping](aipluginconversationstartermapping.md#BKMK_AIPlugin_AIPluginConversationStarterMapping)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginconversationstartermapping`|
|ReferencingAttribute|`aiplugin`|
|ReferencedEntityNavigationPropertyName|`AIPlugin_AIPluginConversationStarterMapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugin_AsyncOperations"></a> aiplugin_AsyncOperations

Many-To-One Relationship: [asyncoperation aiplugin_AsyncOperations](asyncoperation.md#BKMK_aiplugin_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugin_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugin_BulkDeleteFailures"></a> aiplugin_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure aiplugin_BulkDeleteFailures](bulkdeletefailure.md#BKMK_aiplugin_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugin_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugin_MailboxTrackingFolders"></a> aiplugin_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder aiplugin_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_aiplugin_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugin_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugin_PrincipalObjectAttributeAccesses"></a> aiplugin_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess aiplugin_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_aiplugin_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`aiplugin_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugin_ProcessSession"></a> aiplugin_ProcessSession

Many-To-One Relationship: [processsession aiplugin_ProcessSession](processsession.md#BKMK_aiplugin_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugin_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugin_SyncErrors"></a> aiplugin_SyncErrors

Many-To-One Relationship: [syncerror aiplugin_SyncErrors](syncerror.md#BKMK_aiplugin_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugin_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugingovernance_aiplugin"></a> aiplugingovernance_aiplugin

Many-To-One Relationship: [aiplugingovernance aiplugingovernance_aiplugin](aiplugingovernance.md#BKMK_aiplugingovernance_aiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugingovernance`|
|ReferencingAttribute|`aiplugin`|
|ReferencedEntityNavigationPropertyName|`aiplugingovernance_aiplugin`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AIPluginInstance_AIPlugin_AIPlugin"></a> AIPluginInstance_AIPlugin_AIPlugin

Many-To-One Relationship: [aiplugininstance AIPluginInstance_AIPlugin_AIPlugin](aiplugininstance.md#BKMK_AIPluginInstance_AIPlugin_AIPlugin)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugininstance`|
|ReferencingAttribute|`aiplugin`|
|ReferencedEntityNavigationPropertyName|`AIPluginInstance_AIPlugin_AIPlugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AIPluginOperation_AIPlugin_AIPlugin"></a> AIPluginOperation_AIPlugin_AIPlugin

Many-To-One Relationship: [aipluginoperation AIPluginOperation_AIPlugin_AIPlugin](aipluginoperation.md#BKMK_AIPluginOperation_AIPlugin_AIPlugin)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`aiplugin`|
|ReferencedEntityNavigationPropertyName|`AIPluginOperation_AIPlugin_AIPlugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sideloadedaiplugin_AIPlugin_aiplugin"></a> sideloadedaiplugin_AIPlugin_aiplugin

Many-To-One Relationship: [sideloadedaiplugin sideloadedaiplugin_AIPlugin_aiplugin](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_AIPlugin_aiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`sideloadedaiplugin`|
|ReferencingAttribute|`aiplugin`|
|ReferencedEntityNavigationPropertyName|`sideloadedaiplugin_AIPlugin_aiplugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_AICoPilot_AIPlugin_AIPlugin"></a> AICoPilot_AIPlugin_AIPlugin

See [aicopilot AICoPilot_AIPlugin_AIPlugin Many-To-Many Relationship](aicopilot.md#BKMK_AICoPilot_AIPlugin_AIPlugin)

|Property|Value|
|---|---|
|IntersectEntityName|`aicopilot_aiplugin`|
|IsCustomizable|True|
|SchemaName|`AICoPilot_AIPlugin_AIPlugin`|
|IntersectAttribute|`aipluginid`|
|NavigationPropertyName|`AICopilot_AIPlugin_AIPlugin`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.aiplugin?displayProperty=fullName>
