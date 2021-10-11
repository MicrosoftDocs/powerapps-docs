---
title: "Chatbot subcomponent (botcomponent) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Chatbot subcomponent (botcomponent) table/entity."
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

# Chatbot subcomponent (botcomponent) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Holds key authoring components of a Chatbot such a topics, entities, variables, etc.

**Added by**: Power Virtual Agents Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/botcomponents(*botcomponentid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/botcomponents<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/botcomponents(*botcomponentid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/botcomponents(*botcomponentid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/botcomponents<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/botcomponents(*botcomponentid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/botcomponents(*botcomponentid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|botcomponents|
|DisplayCollectionName|Chatbot subcomponents|
|DisplayName|Chatbot subcomponent|
|EntitySetName|botcomponents|
|IsBPFEntity|False|
|LogicalCollectionName|botcomponents|
|LogicalName|botcomponent|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|botcomponentid|
|PrimaryNameAttribute|name|
|SchemaName|botcomponent|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccentColor](#BKMK_AccentColor)
- [botcomponentId](#BKMK_botcomponentId)
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
- [ParentBotComponentId](#BKMK_ParentBotComponentId)
- [ReusePolicy](#BKMK_ReusePolicy)
- [SchemaName](#BKMK_SchemaName)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AccentColor"></a> AccentColor

|Property|Value|
|--------|-----|
|Description|Accent Color for this re-usable subcomponent|
|DisplayName|Accent Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|accentcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_botcomponentId"></a> botcomponentId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|BotComponent|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|botcomponentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Category"></a> Category

|Property|Value|
|--------|-----|
|Description|The category of Chatbot subcomponent.|
|DisplayName|Category|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|category|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|--------|-----|
|Description|The sub type of Chatbot subcomponent.|
|DisplayName|ComponentType|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|componenttype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### ComponentType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Topic|A topic defines a how a bot conversation plays out. A topic has trigger phrases - these are phrases, keywords, or questions - and conversation nodes - these are what you use to define how a bot should respond and what it should do.|
|1|Skill|Power Virtual Agents enables you to extend your bot using Bot Framework Skills. Bot Framework Skills are re-usable conversational skill building-blocks covering conversational use-cases.|
|2|Bot variable|Variables let you save responses from your customers in a conversation with your bot so that you can reuse them later in the conversation.|
|3|Bot entity|An entity can be viewed as an information unit that represents a certain type of a real-world subject, like a phone number, zip code, city, or even a person's name.|
|4|Dialog|Dialogs provide more advanced functionality than topics and integrate with Bot Framework Composer.|
|5|Trigger|Trigger defines how the topic is triggered and/or what actions are executed.|
|6|Language understanding|Language Understanding (LU) is used by a bot to understand language naturally and contextually to determine what next to do in a conversation flow.|
|7|Language generation|Language Generation (LG) lets you define multiple variations of a phrase, execute simple expressions based on context, and refer to conversational memory.|
|8|Dialog schema|Schema of the dialog that specifies dialog's input and output parameters|



### <a name="BKMK_Content"></a> Content

|Property|Value|
|--------|-----|
|Description|The content or metadata of the Bot Component that defines its structure and properties.|
|DisplayName|Content|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|content|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Data"></a> Data

|Property|Value|
|--------|-----|
|Description|The content of the Bot Component in OBI format|
|DisplayName|Obi Data|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|data|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Contains searchable text for the bot component|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_HelpLink"></a> HelpLink

|Property|Value|
|--------|-----|
|Description|Link to learn More about this subcomponent|
|DisplayName|Help Link|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|helplink|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IconUrl"></a> IconUrl

|Property|Value|
|--------|-----|
|Description|Icon Url for this subcomponent|
|DisplayName|Icon Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|iconurl|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_Language"></a> Language

|Property|Value|
|--------|-----|
|Description|Language of the chatbot subcomponent|
|DisplayName|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|language|
|RequiredLevel|None|
|Type|Picklist|

#### Language Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1025|Arabic||
|1028|Chinese (Traditional)||
|1030|Danish||
|1031|German||
|1033|English||
|1034|Spanish||
|1036|French||
|1040|Italian||
|1041|Japanese||
|1042|Korean||
|1043|Dutch||
|1044|Norwegian||
|1045|Polish||
|1046|Portuguese (Brazilian)||
|1049|Russian||
|1053|Swedish||
|1055|Turkish||
|1057|Indonesian||
|1081|Hindi||
|2052|Chinese (Simplified)||



### <a name="BKMK_name"></a> name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|500|
|RequiredLevel|None|
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
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ParentBotComponentId"></a> ParentBotComponentId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Chatbot subcomponent associated with Chatbot subcomponent.|
|DisplayName|Parent chatbot subcomponent|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentbotcomponentid|
|RequiredLevel|None|
|Targets|botcomponent|
|Type|Lookup|


### <a name="BKMK_ReusePolicy"></a> ReusePolicy

|Property|Value|
|--------|-----|
|Description|Reuse Policy for the chatbot subcomponent|
|DisplayName|Reuse Policy|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|reusepolicy|
|RequiredLevel|None|
|Type|Picklist|

#### ReusePolicy Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None|Not Reusable. By default, a chatbot subcomponent is not reusable and Reuse Policy is None|
|1|Private|Is required by one or more Public chatbot subcomponent, but is not directly invokable or visible|
|2|Public|Visible shared / reusable chatbot subcomponent for use in all bots in the environment|



### <a name="BKMK_SchemaName"></a> SchemaName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|SchemaName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|schemaname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the BotComponent|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the BotComponent|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentBotComponentIdName](#BKMK_ParentBotComponentIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Row id unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

**Added by**: Basic Solution Solution

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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

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


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Added by**: Active Solution Solution

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
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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


### <a name="BKMK_IsManaged"></a> IsManaged

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentBotComponentIdName"></a> ParentBotComponentIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentbotcomponentidname|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionId"></a> SolutionId

**Added by**: Basic Solution Solution

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

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
|DisplayName|Version Number|
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

- [botcomponent_SyncErrors](#BKMK_botcomponent_SyncErrors)
- [botcomponent_AsyncOperations](#BKMK_botcomponent_AsyncOperations)
- [botcomponent_MailboxTrackingFolders](#BKMK_botcomponent_MailboxTrackingFolders)
- [botcomponent_ProcessSession](#BKMK_botcomponent_ProcessSession)
- [botcomponent_BulkDeleteFailures](#BKMK_botcomponent_BulkDeleteFailures)
- [botcomponent_PrincipalObjectAttributeAccesses](#BKMK_botcomponent_PrincipalObjectAttributeAccesses)
- [botcomponent_parent_botcomponent](#BKMK_botcomponent_parent_botcomponent)


### <a name="BKMK_botcomponent_SyncErrors"></a> botcomponent_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [botcomponent_SyncErrors](syncerror.md#BKMK_botcomponent_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|botcomponent_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_botcomponent_AsyncOperations"></a> botcomponent_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [botcomponent_AsyncOperations](asyncoperation.md#BKMK_botcomponent_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|botcomponent_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_botcomponent_MailboxTrackingFolders"></a> botcomponent_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [botcomponent_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_botcomponent_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|botcomponent_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_botcomponent_ProcessSession"></a> botcomponent_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [botcomponent_ProcessSession](processsession.md#BKMK_botcomponent_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|botcomponent_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_botcomponent_BulkDeleteFailures"></a> botcomponent_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [botcomponent_BulkDeleteFailures](bulkdeletefailure.md#BKMK_botcomponent_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|botcomponent_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_botcomponent_PrincipalObjectAttributeAccesses"></a> botcomponent_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [botcomponent_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_botcomponent_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|botcomponent_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_botcomponent_parent_botcomponent"></a> botcomponent_parent_botcomponent

Same as botcomponent table [botcomponent_parent_botcomponent](botcomponent.md#BKMK_botcomponent_parent_botcomponent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|parentbotcomponentid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|botcomponent_parent_botcomponent|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_botcomponent_createdby](#BKMK_lk_botcomponent_createdby)
- [lk_botcomponent_createdonbehalfby](#BKMK_lk_botcomponent_createdonbehalfby)
- [lk_botcomponent_modifiedby](#BKMK_lk_botcomponent_modifiedby)
- [lk_botcomponent_modifiedonbehalfby](#BKMK_lk_botcomponent_modifiedonbehalfby)
- [user_botcomponent](#BKMK_user_botcomponent)
- [team_botcomponent](#BKMK_team_botcomponent)
- [business_unit_botcomponent](#BKMK_business_unit_botcomponent)
- [botcomponent_parent_botcomponent](#BKMK_botcomponent_parent_botcomponent)


### <a name="BKMK_lk_botcomponent_createdby"></a> lk_botcomponent_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_botcomponent_createdby](systemuser.md#BKMK_lk_botcomponent_createdby) One-To-Many relationship.

### <a name="BKMK_lk_botcomponent_createdonbehalfby"></a> lk_botcomponent_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_botcomponent_createdonbehalfby](systemuser.md#BKMK_lk_botcomponent_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_botcomponent_modifiedby"></a> lk_botcomponent_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_botcomponent_modifiedby](systemuser.md#BKMK_lk_botcomponent_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_botcomponent_modifiedonbehalfby"></a> lk_botcomponent_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_botcomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_botcomponent_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_botcomponent"></a> user_botcomponent

**Added by**: System Solution Solution

See systemuser Table [user_botcomponent](systemuser.md#BKMK_user_botcomponent) One-To-Many relationship.

### <a name="BKMK_team_botcomponent"></a> team_botcomponent

**Added by**: System Solution Solution

See team Table [team_botcomponent](team.md#BKMK_team_botcomponent) One-To-Many relationship.

### <a name="BKMK_business_unit_botcomponent"></a> business_unit_botcomponent

**Added by**: System Solution Solution

See businessunit Table [business_unit_botcomponent](businessunit.md#BKMK_business_unit_botcomponent) One-To-Many relationship.

### <a name="BKMK_botcomponent_parent_botcomponent"></a> botcomponent_parent_botcomponent

See botcomponent Table [botcomponent_parent_botcomponent](botcomponent.md#BKMK_botcomponent_parent_botcomponent) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the botcomponent table is the first table in the relationship. Listed by **SchemaName**.

- [bot_botcomponent](#BKMK_bot_botcomponent)
- [botcomponent_botcomponent](#BKMK_botcomponent_botcomponent)
- [botcomponent_environmentvariabledefinition](#BKMK_botcomponent_environmentvariabledefinition)
- [botcomponent_workflow](#BKMK_botcomponent_workflow)


### <a name="BKMK_bot_botcomponent"></a> bot_botcomponent

See bot Table [bot_botcomponent](bot.md#BKMK_bot_botcomponent) Many-To-Many Relationship.

### <a name="BKMK_botcomponent_botcomponent"></a> botcomponent_botcomponent

IntersectEntityName: botcomponent_botcomponent<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|botcomponentidone|
|IsCustomizable|False|
|LogicalName|botcomponent|
|NavigationPropertyName|botcomponent_botcomponent|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|botcomponent|
|IntersectAttribute|botcomponentidtwo|
|NavigationPropertyName|botcomponent_botcomponent|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|


### <a name="BKMK_botcomponent_environmentvariabledefinition"></a> botcomponent_environmentvariabledefinition

IntersectEntityName: botcomponent_environmentvariabledefinition<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|botcomponentid|
|IsCustomizable|False|
|LogicalName|botcomponent|
|NavigationPropertyName|botcomponent_environmentvariabledefinition|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|environmentvariabledefinition|
|IntersectAttribute|environmentvariabledefinitionid|
|NavigationPropertyName|botcomponent_environmentvariabledefinition|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|


### <a name="BKMK_botcomponent_workflow"></a> botcomponent_workflow

IntersectEntityName: botcomponent_workflow<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|botcomponentid|
|IsCustomizable|False|
|LogicalName|botcomponent|
|NavigationPropertyName|botcomponent_workflow|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|workflow|
|IntersectAttribute|workflowid|
|NavigationPropertyName|botcomponent_workflow|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|


### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.botcomponent?text=botcomponent EntityType" />