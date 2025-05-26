---
title: "Copilot component (botcomponent) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Copilot component (botcomponent) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Copilot component (botcomponent) table/entity reference (Microsoft Dataverse)

Holds key authoring components of a Copilot such a topics, entities, variables, etc.

## Messages

The following table lists the messages for the Copilot component (botcomponent) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /botcomponents(*botcomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /botcomponents<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /botcomponents(*botcomponentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /botcomponents(*botcomponentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /botcomponents<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /botcomponents(*botcomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /botcomponents(*botcomponentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /botcomponents(*botcomponentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Copilot component (botcomponent) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Copilot component** |
| **DisplayCollectionName** | **Copilot components** |
| **SchemaName** | `botcomponent` |
| **CollectionSchemaName** | `botcomponents` |
| **EntitySetName** | `botcomponents`|
| **LogicalName** | `botcomponent` |
| **LogicalCollectionName** | `botcomponents` |
| **PrimaryIdAttribute** | `botcomponentid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccentColor](#BKMK_AccentColor)
- [botcomponentId](#BKMK_botcomponentId)
- [canmodifystate](#BKMK_canmodifystate)
- [Category](#BKMK_Category)
- [ComponentType](#BKMK_ComponentType)
- [Content](#BKMK_Content)
- [Data](#BKMK_Data)
- [Description](#BKMK_Description)
- [HelpLink](#BKMK_HelpLink)
- [IconUrl](#BKMK_IconUrl)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Language](#BKMK_Language)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentBotComponentCollectionId](#BKMK_ParentBotComponentCollectionId)
- [ParentBotComponentId](#BKMK_ParentBotComponentId)
- [ParentBotId](#BKMK_ParentBotId)
- [ReusePolicy](#BKMK_ReusePolicy)
- [SchemaName](#BKMK_SchemaName)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AccentColor"></a> AccentColor

|Property|Value|
|---|---|
|Description|**Accent Color for this re-usable component**|
|DisplayName|**Accent Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accentcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_botcomponentId"></a> botcomponentId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**BotComponent**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`botcomponentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_canmodifystate"></a> canmodifystate

|Property|Value|
|---|---|
|Description||
|DisplayName|**canmodifystate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canmodifystate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`botcomponent_canmodifystate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Category"></a> Category

|Property|Value|
|---|---|
|Description|**The category of Copilot component.**|
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`category`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|---|---|
|Description|**The sub type of Copilot component.**|
|DisplayName|**ComponentType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componenttype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`botcomponent_componenttype`|

#### ComponentType Choices/Options

|Value|Label|
|---|---|
|0|**Topic**|
|1|**Skill**|
|2|**Bot variable**|
|3|**Bot entity**|
|4|**Dialog**|
|5|**Trigger**|
|6|**Language understanding**|
|7|**Language generation**|
|8|**Dialog schema**|
|9|**Topic (V2)**|
|10|**Bot translations (V2)**|
|11|**Bot entity (V2)**|
|12|**Bot variable (V2)**|
|13|**Skill (V2)**|
|14|**Bot File Attachment**|
|15|**Custom GPT**|
|16|**Knowledge Source**|
|17|**External Trigger**|
|18|**Copilot Settings**|
|19|**Test Case**|

### <a name="BKMK_Content"></a> Content

|Property|Value|
|---|---|
|Description|**The content or metadata of the Bot Component that defines its structure and properties.**|
|DisplayName|**Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_Data"></a> Data

|Property|Value|
|---|---|
|Description|**The content of the Bot Component in OBI format**|
|DisplayName|**Obi Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`data`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Contains searchable text for the bot component**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_HelpLink"></a> HelpLink

|Property|Value|
|---|---|
|Description|**Link to learn More about this component**|
|DisplayName|**Help Link**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`helplink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_IconUrl"></a> IconUrl

|Property|Value|
|---|---|
|Description|**Icon Url for this component**|
|DisplayName|**Icon Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iconurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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

### <a name="BKMK_Language"></a> Language

|Property|Value|
|---|---|
|Description|**Language of the copilot component**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`language`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`chatbotlanguage`|

#### Language Choices/Options

|Value|Label|
|---|---|
|1025|**Arabic**|
|1028|**Chinese (Traditional)**|
|1029|**Czech**|
|1030|**Danish**|
|1031|**German**|
|1032|**Greek**|
|1033|**English**|
|1034|**Spanish**|
|1035|**Finnish**|
|1036|**French**|
|1037|**Hebrew**|
|1040|**Italian**|
|1041|**Japanese**|
|1042|**Korean**|
|1043|**Dutch**|
|1044|**Norwegian**|
|1045|**Polish**|
|1046|**Portuguese (Brazilian)**|
|1049|**Russian**|
|1053|**Swedish**|
|1054|**Thai**|
|1055|**Turkish**|
|1057|**Indonesian**|
|1081|**Hindi**|
|2052|**Chinese (Simplified)**|
|2057|**English (United Kingdom)**|
|2070|**Portuguese (Portugal)**|
|3081|**English (Australia)**|
|3084|**French (Canada)**|
|21514|**Spanish (United States)**|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

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

### <a name="BKMK_ParentBotComponentCollectionId"></a> ParentBotComponentCollectionId

|Property|Value|
|---|---|
|Description|**Unique identifier for Copilot component collection associated with Copilot component.**|
|DisplayName|**ParentBotComponentCollection**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentbotcomponentcollectionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|botcomponentcollection|

### <a name="BKMK_ParentBotComponentId"></a> ParentBotComponentId

|Property|Value|
|---|---|
|Description|**Unique identifier for Copilot component associated with Copilot component.**|
|DisplayName|**Parent copilot component**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentbotcomponentid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|botcomponent|

### <a name="BKMK_ParentBotId"></a> ParentBotId

|Property|Value|
|---|---|
|Description|**Unique identifier for Bot associated with the Component.**|
|DisplayName|**parentbotid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentbotid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|bot|

### <a name="BKMK_ReusePolicy"></a> ReusePolicy

|Property|Value|
|---|---|
|Description|**Reuse Policy for the copilot component**|
|DisplayName|**Reuse Policy**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reusepolicy`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`botcomponentreusepolicy`|

#### ReusePolicy Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Private**|
|2|**Public**|

### <a name="BKMK_SchemaName"></a> SchemaName

|Property|Value|
|---|---|
|Description||
|DisplayName|**SchemaName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`schemaname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the BotComponent**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`botcomponent_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the BotComponent**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`botcomponent_statuscode`|

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
- [FileData](#BKMK_FileData)
- [FileData_Name](#BKMK_FileData_Name)
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

### <a name="BKMK_FileData"></a> FileData

|Property|Value|
|---|---|
|Description|**This is a file type attribute to store File attachments.**|
|DisplayName|**filedata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`filedata`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|524288|

### <a name="BKMK_FileData_Name"></a> FileData_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filedata_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

- [botcomponent_parent_bot](#BKMK_botcomponent_parent_bot)
- [botcomponent_parent_botcomponent](#BKMK_botcomponent_parent_botcomponent-many-to-one)
- [botcomponent_parent_botcomponentcollection](#BKMK_botcomponent_parent_botcomponentcollection)
- [business_unit_botcomponent](#BKMK_business_unit_botcomponent)
- [FileAttachment_botcomponent_FileData](#BKMK_FileAttachment_botcomponent_FileData)
- [lk_botcomponent_createdby](#BKMK_lk_botcomponent_createdby)
- [lk_botcomponent_createdonbehalfby](#BKMK_lk_botcomponent_createdonbehalfby)
- [lk_botcomponent_modifiedby](#BKMK_lk_botcomponent_modifiedby)
- [lk_botcomponent_modifiedonbehalfby](#BKMK_lk_botcomponent_modifiedonbehalfby)
- [owner_botcomponent](#BKMK_owner_botcomponent)
- [team_botcomponent](#BKMK_team_botcomponent)
- [user_botcomponent](#BKMK_user_botcomponent)

### <a name="BKMK_botcomponent_parent_bot"></a> botcomponent_parent_bot

One-To-Many Relationship: [bot botcomponent_parent_bot](bot.md#BKMK_botcomponent_parent_bot)

|Property|Value|
|---|---|
|ReferencedEntity|`bot`|
|ReferencedAttribute|`botid`|
|ReferencingAttribute|`parentbotid`|
|ReferencingEntityNavigationPropertyName|`parentbotid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_parent_botcomponent-many-to-one"></a> botcomponent_parent_botcomponent

One-To-Many Relationship: [botcomponent botcomponent_parent_botcomponent](#BKMK_botcomponent_parent_botcomponent-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`parentbotcomponentid`|
|ReferencingEntityNavigationPropertyName|`ParentBotComponentId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_botcomponent_parent_botcomponentcollection"></a> botcomponent_parent_botcomponentcollection

One-To-Many Relationship: [botcomponentcollection botcomponent_parent_botcomponentcollection](botcomponentcollection.md#BKMK_botcomponent_parent_botcomponentcollection)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponentcollection`|
|ReferencedAttribute|`botcomponentcollectionid`|
|ReferencingAttribute|`parentbotcomponentcollectionid`|
|ReferencingEntityNavigationPropertyName|`ParentBotComponentCollectionId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_botcomponent"></a> business_unit_botcomponent

One-To-Many Relationship: [businessunit business_unit_botcomponent](businessunit.md#BKMK_business_unit_botcomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_botcomponent_FileData"></a> FileAttachment_botcomponent_FileData

One-To-Many Relationship: [fileattachment FileAttachment_botcomponent_FileData](fileattachment.md#BKMK_FileAttachment_botcomponent_FileData)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`filedata`|
|ReferencingEntityNavigationPropertyName|`filedata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_botcomponent_createdby"></a> lk_botcomponent_createdby

One-To-Many Relationship: [systemuser lk_botcomponent_createdby](systemuser.md#BKMK_lk_botcomponent_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_botcomponent_createdonbehalfby"></a> lk_botcomponent_createdonbehalfby

One-To-Many Relationship: [systemuser lk_botcomponent_createdonbehalfby](systemuser.md#BKMK_lk_botcomponent_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_botcomponent_modifiedby"></a> lk_botcomponent_modifiedby

One-To-Many Relationship: [systemuser lk_botcomponent_modifiedby](systemuser.md#BKMK_lk_botcomponent_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_botcomponent_modifiedonbehalfby"></a> lk_botcomponent_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_botcomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_botcomponent_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_botcomponent"></a> owner_botcomponent

One-To-Many Relationship: [owner owner_botcomponent](owner.md#BKMK_owner_botcomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_botcomponent"></a> team_botcomponent

One-To-Many Relationship: [team team_botcomponent](team.md#BKMK_team_botcomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_botcomponent"></a> user_botcomponent

One-To-Many Relationship: [systemuser user_botcomponent](systemuser.md#BKMK_user_botcomponent)

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

- [botcomponent_AsyncOperations](#BKMK_botcomponent_AsyncOperations)
- [botcomponent_BulkDeleteFailures](#BKMK_botcomponent_BulkDeleteFailures)
- [botcomponent_FileAttachments](#BKMK_botcomponent_FileAttachments)
- [botcomponent_MailboxTrackingFolders](#BKMK_botcomponent_MailboxTrackingFolders)
- [botcomponent_parent_botcomponent](#BKMK_botcomponent_parent_botcomponent-one-to-many)
- [botcomponent_PrincipalObjectAttributeAccesses](#BKMK_botcomponent_PrincipalObjectAttributeAccesses)
- [botcomponent_ProcessSession](#BKMK_botcomponent_ProcessSession)
- [botcomponent_SyncErrors](#BKMK_botcomponent_SyncErrors)

### <a name="BKMK_botcomponent_AsyncOperations"></a> botcomponent_AsyncOperations

Many-To-One Relationship: [asyncoperation botcomponent_AsyncOperations](asyncoperation.md#BKMK_botcomponent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_BulkDeleteFailures"></a> botcomponent_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure botcomponent_BulkDeleteFailures](bulkdeletefailure.md#BKMK_botcomponent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_FileAttachments"></a> botcomponent_FileAttachments

Many-To-One Relationship: [fileattachment botcomponent_FileAttachments](fileattachment.md#BKMK_botcomponent_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_MailboxTrackingFolders"></a> botcomponent_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder botcomponent_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_botcomponent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_parent_botcomponent-one-to-many"></a> botcomponent_parent_botcomponent

Many-To-One Relationship: [botcomponent botcomponent_parent_botcomponent](#BKMK_botcomponent_parent_botcomponent-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponent`|
|ReferencingAttribute|`parentbotcomponentid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_parent_botcomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_PrincipalObjectAttributeAccesses"></a> botcomponent_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess botcomponent_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_botcomponent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_ProcessSession"></a> botcomponent_ProcessSession

Many-To-One Relationship: [processsession botcomponent_ProcessSession](processsession.md#BKMK_botcomponent_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_SyncErrors"></a> botcomponent_SyncErrors

Many-To-One Relationship: [syncerror botcomponent_SyncErrors](syncerror.md#BKMK_botcomponent_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [bot_botcomponent](#BKMK_bot_botcomponent)
- [botcomponent_aipluginoperation](#BKMK_botcomponent_aipluginoperation)
- [botcomponent_botcomponent](#BKMK_botcomponent_botcomponent)
- [botcomponent_connectionreference](#BKMK_botcomponent_connectionreference)
- [botcomponent_dvtablesearch](#BKMK_botcomponent_dvtablesearch)
- [botcomponent_environmentvariabledefinition](#BKMK_botcomponent_environmentvariabledefinition)
- [botcomponent_msdyn_aimodel](#BKMK_botcomponent_msdyn_aimodel)
- [botcomponent_workflow](#BKMK_botcomponent_workflow)

### <a name="BKMK_bot_botcomponent"></a> bot_botcomponent

See [bot bot_botcomponent Many-To-Many Relationship](bot.md#BKMK_bot_botcomponent)

|Property|Value|
|---|---|
|IntersectEntityName|`bot_botcomponent`|
|IsCustomizable|False|
|SchemaName|`bot_botcomponent`|
|IntersectAttribute|`botcomponentid`|
|NavigationPropertyName|`bot_botcomponent`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_aipluginoperation"></a> botcomponent_aipluginoperation

See [aipluginoperation botcomponent_aipluginoperation Many-To-Many Relationship](aipluginoperation.md#BKMK_botcomponent_aipluginoperation)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_aipluginoperation`|
|IsCustomizable|False|
|SchemaName|`botcomponent_aipluginoperation`|
|IntersectAttribute|`botcomponentid`|
|NavigationPropertyName|`botcomponent_aipluginoperation`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_botcomponent"></a> botcomponent_botcomponent

This is a self-referencing many-to-many relationship.

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_botcomponent`|
|IsCustomizable|False|
|SchemaName|`botcomponent_botcomponent`|
|Entity1IntersectAttribute|`botcomponentidone`|
|Entity2IntersectAttribute|`botcomponentidtwo`|
|Entity1NavigationPropertyName|`botcomponent_botcomponent`|
|Entity2NavigationPropertyName|`botcomponent_botcomponent`|
|Entity1AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|
|Entity2AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_connectionreference"></a> botcomponent_connectionreference

See [connectionreference botcomponent_connectionreference Many-To-Many Relationship](connectionreference.md#BKMK_botcomponent_connectionreference)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_connectionreference`|
|IsCustomizable|False|
|SchemaName|`botcomponent_connectionreference`|
|IntersectAttribute|`botcomponentid`|
|NavigationPropertyName|`botcomponent_connectionreference`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_dvtablesearch"></a> botcomponent_dvtablesearch

See [dvtablesearch botcomponent_dvtablesearch Many-To-Many Relationship](dvtablesearch.md#BKMK_botcomponent_dvtablesearch)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_dvtablesearch`|
|IsCustomizable|False|
|SchemaName|`botcomponent_dvtablesearch`|
|IntersectAttribute|`botcomponentid`|
|NavigationPropertyName|`botcomponent_dvtablesearch`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_environmentvariabledefinition"></a> botcomponent_environmentvariabledefinition

See [environmentvariabledefinition botcomponent_environmentvariabledefinition Many-To-Many Relationship](environmentvariabledefinition.md#BKMK_botcomponent_environmentvariabledefinition)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_environmentvariabledefinition`|
|IsCustomizable|False|
|SchemaName|`botcomponent_environmentvariabledefinition`|
|IntersectAttribute|`botcomponentid`|
|NavigationPropertyName|`botcomponent_environmentvariabledefinition`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_msdyn_aimodel"></a> botcomponent_msdyn_aimodel

See [msdyn_aimodel botcomponent_msdyn_aimodel Many-To-Many Relationship](msdyn_aimodel.md#BKMK_botcomponent_msdyn_aimodel)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_msdyn_aimodel`|
|IsCustomizable|False|
|SchemaName|`botcomponent_msdyn_aimodel`|
|IntersectAttribute|`botcomponentid`|
|NavigationPropertyName|`botcomponent_msdyn_aimodel`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_workflow"></a> botcomponent_workflow

See [workflow botcomponent_workflow Many-To-Many Relationship](workflow.md#BKMK_botcomponent_workflow)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_workflow`|
|IsCustomizable|False|
|SchemaName|`botcomponent_workflow`|
|IntersectAttribute|`botcomponentid`|
|NavigationPropertyName|`botcomponent_workflow`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.botcomponent?displayProperty=fullName>
