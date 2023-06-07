---
title: "msdyn_entitylinkchatconfiguration table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_entitylinkchatconfiguration table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_entitylinkchatconfiguration table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Teams Chat Settings Solution Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msdyn_entitylinkchatconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msdyn_entitylinkchatconfigurations<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_entitylinkchatconfigurations|
|DisplayCollectionName|Entity link chat configurations|
|DisplayName|Entity link chat configuration|
|EntitySetName|msdyn_entitylinkchatconfigurations|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_entitylinkchatconfigurations|
|LogicalName|msdyn_entitylinkchatconfiguration|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_entitylinkchatconfigurationid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_entitylinkchatconfiguration|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_ContextViewId](#BKMK_msdyn_ContextViewId)
- [msdyn_EnableAiIntroductionMessage](#BKMK_msdyn_EnableAiIntroductionMessage)
- [msdyn_EnableAiSuggestion](#BKMK_msdyn_EnableAiSuggestion)
- [msdyn_EnableAutoNameChats](#BKMK_msdyn_EnableAutoNameChats)
- [msdyn_EnableKickoffMessage](#BKMK_msdyn_EnableKickoffMessage)
- [msdyn_EnableLogicBasedSuggestion](#BKMK_msdyn_EnableLogicBasedSuggestion)
- [msdyn_entitylinkchatconfigurationId](#BKMK_msdyn_entitylinkchatconfigurationId)
- [msdyn_EntityType](#BKMK_msdyn_EntityType)
- [msdyn_filteringAttributes](#BKMK_msdyn_filteringAttributes)
- [msdyn_isEnabledForBot](#BKMK_msdyn_isEnabledForBot)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_RecentChatLinkerCanUnlink](#BKMK_msdyn_RecentChatLinkerCanUnlink)
- [msdyn_RecordOwnerCanUnlink](#BKMK_msdyn_RecordOwnerCanUnlink)
- [msdyn_UniqueName](#BKMK_msdyn_UniqueName)
- [msdyn_UserCanJoinChat](#BKMK_msdyn_UserCanJoinChat)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


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


### <a name="BKMK_msdyn_ContextViewId"></a> msdyn_ContextViewId

|Property|Value|
|--------|-----|
|Description|The view id of the selected context view.|
|DisplayName|Context view id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_contextviewid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_EnableAiIntroductionMessage"></a> msdyn_EnableAiIntroductionMessage

|Property|Value|
|--------|-----|
|Description|Value of Enable AI introduction message|
|DisplayName|Enable AI introduction message|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_enableaiintroductionmessage|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_EnableAiIntroductionMessage Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_EnableAiSuggestion"></a> msdyn_EnableAiSuggestion

|Property|Value|
|--------|-----|
|Description|Value of Enable AI suggestion|
|DisplayName|Enable AI suggestion|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_enableaisuggestion|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_EnableAiSuggestion Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_EnableAutoNameChats"></a> msdyn_EnableAutoNameChats

|Property|Value|
|--------|-----|
|Description|Enable auto name chats|
|DisplayName|Enable auto name chats|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_enableautonamechats|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_EnableAutoNameChats Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_EnableKickoffMessage"></a> msdyn_EnableKickoffMessage

|Property|Value|
|--------|-----|
|Description|Enable kickoff message|
|DisplayName|Enable kickoff message|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_enablekickoffmessage|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_EnableKickoffMessage Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_EnableLogicBasedSuggestion"></a> msdyn_EnableLogicBasedSuggestion

|Property|Value|
|--------|-----|
|Description|Enable logic-based suggestion|
|DisplayName|Enable logic-based suggestion|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_enablelogicbasedsuggestion|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_EnableLogicBasedSuggestion Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_entitylinkchatconfigurationId"></a> msdyn_entitylinkchatconfigurationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Entity link chat configuration|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_entitylinkchatconfigurationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_EntityType"></a> msdyn_EntityType

|Property|Value|
|--------|-----|
|Description|The entity setup for link team configuration.|
|DisplayName|Entity type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_entitytype|
|RequiredLevel|ApplicationRequired|
|Targets|entity|
|Type|Lookup|


### <a name="BKMK_msdyn_filteringAttributes"></a> msdyn_filteringAttributes

|Property|Value|
|--------|-----|
|Description|List of attributes that we want bot event updates on|
|DisplayName|Filtering Attributes|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_filteringattributes|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isEnabledForBot"></a> msdyn_isEnabledForBot

|Property|Value|
|--------|-----|
|Description|To indicate whether bot event update is enabled for this record|
|DisplayName|Is Enabled For Bot updates|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isenabledforbot|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isEnabledForBot Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|--------|-----|
|Description|The name of link team configuration.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_name|
|MaxLength|128|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_RecentChatLinkerCanUnlink"></a> msdyn_RecentChatLinkerCanUnlink

|Property|Value|
|--------|-----|
|Description|Value of recent chat linker can unlink|
|DisplayName|Recent chat linker can unlink|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_recentchatlinkercanunlink|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_RecentChatLinkerCanUnlink Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_RecordOwnerCanUnlink"></a> msdyn_RecordOwnerCanUnlink

|Property|Value|
|--------|-----|
|Description|Value of record owner can unlink|
|DisplayName|Record owner can unlink|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_recordownercanunlink|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_RecordOwnerCanUnlink Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_UniqueName"></a> msdyn_UniqueName

|Property|Value|
|--------|-----|
|Description|Unique Name for the entity.|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_uniquename|
|MaxLength|128|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_msdyn_UserCanJoinChat"></a> msdyn_UserCanJoinChat

|Property|Value|
|--------|-----|
|Description|Value of User can join chat|
|DisplayName|User can join chat|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_usercanjoinchat|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_UserCanJoinChat Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Entitylink chat configuration|
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
|Description|Reason for the status of the Entitylink chat configuration|
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
- [msdyn_entitytypeName](#BKMK_msdyn_entitytypeName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
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
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



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


### <a name="BKMK_msdyn_entitytypeName"></a> msdyn_entitytypeName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_entitytypename|
|MaxLength|128|
|RequiredLevel|None|
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
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


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

- [msdyn_entitylinkchatconfiguration_SyncErrors](#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors)
- [msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord](#BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord)
- [msdyn_entitylinkchatconfiguration_DuplicateBaseRecord](#BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord)
- [msdyn_entitylinkchatconfiguration_AsyncOperations](#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations)
- [msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders)
- [msdyn_entitylinkchatconfiguration_ProcessSession](#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession)
- [msdyn_entitylinkchatconfiguration_BulkDeleteFailures](#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures)
- [msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msdyn_entitylinkchatconfiguration_SyncErrors"></a> msdyn_entitylinkchatconfiguration_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_SyncErrors](syncerror.md#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord"></a> msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord"></a> msdyn_entitylinkchatconfiguration_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations"></a> msdyn_entitylinkchatconfiguration_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_AsyncOperations](asyncoperation.md#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders"></a> msdyn_entitylinkchatconfiguration_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_entitylinkchatconfiguration_ProcessSession"></a> msdyn_entitylinkchatconfiguration_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_ProcessSession](processsession.md#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures"></a> msdyn_entitylinkchatconfiguration_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_entitylinkchatconfiguration_createdby](#BKMK_lk_msdyn_entitylinkchatconfiguration_createdby)
- [lk_msdyn_entitylinkchatconfiguration_createdonbehalfby](#BKMK_lk_msdyn_entitylinkchatconfiguration_createdonbehalfby)
- [lk_msdyn_entitylinkchatconfiguration_modifiedby](#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedby)
- [lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby](#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby)
- [user_msdyn_entitylinkchatconfiguration](#BKMK_user_msdyn_entitylinkchatconfiguration)
- [team_msdyn_entitylinkchatconfiguration](#BKMK_team_msdyn_entitylinkchatconfiguration)
- [business_unit_msdyn_entitylinkchatconfiguration](#BKMK_business_unit_msdyn_entitylinkchatconfiguration)
- [msdyn_entity_msdyn_entitylinkchatconfiguration](#BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration)


### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_createdby"></a> lk_msdyn_entitylinkchatconfiguration_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_entitylinkchatconfiguration_createdby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_createdonbehalfby"></a> lk_msdyn_entitylinkchatconfiguration_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_entitylinkchatconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedby"></a> lk_msdyn_entitylinkchatconfiguration_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_entitylinkchatconfiguration_modifiedby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby"></a> lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msdyn_entitylinkchatconfiguration"></a> user_msdyn_entitylinkchatconfiguration

**Added by**: System Solution Solution

See the [user_msdyn_entitylinkchatconfiguration](systemuser.md#BKMK_user_msdyn_entitylinkchatconfiguration) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msdyn_entitylinkchatconfiguration"></a> team_msdyn_entitylinkchatconfiguration

**Added by**: System Solution Solution

See the [team_msdyn_entitylinkchatconfiguration](team.md#BKMK_team_msdyn_entitylinkchatconfiguration) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msdyn_entitylinkchatconfiguration"></a> business_unit_msdyn_entitylinkchatconfiguration

**Added by**: System Solution Solution

See the [business_unit_msdyn_entitylinkchatconfiguration](businessunit.md#BKMK_business_unit_msdyn_entitylinkchatconfiguration) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration"></a> msdyn_entity_msdyn_entitylinkchatconfiguration

**Added by**: System Solution Solution

See the [msdyn_entity_msdyn_entitylinkchatconfiguration](entity.md#BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration) one-to-many relationship for the [entity](entity.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_entitylinkchatconfiguration?text=msdyn_entitylinkchatconfiguration EntityType" />