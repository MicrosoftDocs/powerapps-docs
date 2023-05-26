---
title: "msdyn_customcontrolextendedsettings table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_customcontrolextendedsettings table/entity."
ms.date: 05/23/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_customcontrolextendedsettings table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: User Experiences Extended Settings Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.2/msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.2/msdyn_customcontrolextendedsettingses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE [*org URI*]/api/data/v9.2/msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.2/msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.2/msdyn_customcontrolextendedsettingses<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.2/msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.2/msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_customcontrolextendedsettingses|
|DisplayCollectionName|CustomControl Extended Settings|
|DisplayName|Custom Control Extended Setting|
|EntitySetName|msdyn_customcontrolextendedsettingses|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_customcontrolextendedsettingses|
|LogicalName|msdyn_customcontrolextendedsettings|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_customcontrolextendedsettingsid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_customcontrolextendedsettings|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_customcontrolextendedsettingsId](#BKMK_msdyn_customcontrolextendedsettingsId)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_rte_userpersonalizationsettings](#BKMK_msdyn_rte_userpersonalizationsettings)
- [msdyn_timeline_displaylayoutoption](#BKMK_msdyn_timeline_displaylayoutoption)
- [msdyn_timelineWall_isAutoExpanded](#BKMK_msdyn_timelineWall_isAutoExpanded)
- [msdyn_timelineWall_isFilterPaneOpen](#BKMK_msdyn_timelineWall_isFilterPaneOpen)
- [msdyn_timelineWall_isSortOrderNewerToOlder](#BKMK_msdyn_timelineWall_isSortOrderNewerToOlder)
- [msdyn_timelineWall_searchTermApplied](#BKMK_msdyn_timelineWall_searchTermApplied)
- [msdyn_timelineWall_userFilters](#BKMK_msdyn_timelineWall_userFilters)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

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


### <a name="BKMK_msdyn_customcontrolextendedsettingsId"></a> msdyn_customcontrolextendedsettingsId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Custom Control Extended Setting|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_customcontrolextendedsettingsid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_rte_userpersonalizationsettings"></a> msdyn_rte_userpersonalizationsettings

|Property|Value|
|--------|-----|
|Description|User configured personal settings for Rich Text Editor|
|DisplayName|RTE User Personalization Settings|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_rte_userpersonalizationsettings|
|MaxLength|65536|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_timeline_displaylayoutoption"></a> msdyn_timeline_displaylayoutoption

|Property|Value|
|--------|-----|
|Description|User configured display layout option for the Timeline control|
|DisplayName|Timeline display layout options|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_timeline_displaylayoutoption|
|MaxLength|65536|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_timelineWall_isAutoExpanded"></a> msdyn_timelineWall_isAutoExpanded

|Property|Value|
|--------|-----|
|Description|User configured expand state for TimelineWall|
|DisplayName|IsAutoExpanded|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_timelineWall_isAutoExpanded|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_timelineWall_isAutoExpanded Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_timelineWall_isFilterPaneOpen"></a> msdyn_timelineWall_isFilterPaneOpen

|Property|Value|
|--------|-----|
|Description|Will the filter pane open by default on TimelineWall load|
|DisplayName|Is Filter Pane Open|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_timelineWall_isFilterPaneOpen|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_timelineWall_isFilterPaneOpen Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_timelineWall_isSortOrderNewerToOlder"></a> msdyn_timelineWall_isSortOrderNewerToOlder

|Property|Value|
|--------|-----|
|Description|Is TimelineWall set to sort by newer to older records|
|DisplayName|Is Sort Order Newer To Older for TimelineWall|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_timelineWall_isSortOrderNewerToOlder|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_timelineWall_isSortOrderNewerToOlder Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_msdyn_timelineWall_searchTermApplied"></a> msdyn_timelineWall_searchTermApplied

|Property|Value|
|--------|-----|
|Description|Search term to be applied on TimelineWall load|
|DisplayName|Search Term Applied|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_timelineWall_searchTermApplied|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_timelineWall_userFilters"></a> msdyn_timelineWall_userFilters

|Property|Value|
|--------|-----|
|Description|User configured filter settings for TimelineWall|
|DisplayName|User Filters|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_timelineWall_userFilters|
|MaxLength|65536|
|RequiredLevel|None|
|Type|Memo|


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
|Description|Status of the Timeline Wall Extended Setting|
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
|Description|Reason for the status of the Timeline Wall Extended Setting|
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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


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

- [msdyn_customcontrolextendedsettings_SyncErrors](#BKMK_msdyn_customcontrolextendedsettings_SyncErrors)
- [msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord)
- [msdyn_customcontrolextendedsettings_DuplicateBaseRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord)
- [msdyn_customcontrolextendedsettings_AsyncOperations](#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations)
- [msdyn_customcontrolextendedsettings_MailboxTrackingFolders](#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders)
- [msdyn_customcontrolextendedsettings_ProcessSession](#BKMK_msdyn_customcontrolextendedsettings_ProcessSession)
- [msdyn_customcontrolextendedsettings_BulkDeleteFailures](#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures)
- [msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msdyn_customcontrolextendedsettings_SyncErrors"></a> msdyn_customcontrolextendedsettings_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_SyncErrors](syncerror.md#BKMK_msdyn_customcontrolextendedsettings_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord"></a> msdyn_customcontrolextendedsettings_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord"></a> msdyn_customcontrolextendedsettings_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_customcontrolextendedsettings_AsyncOperations"></a> msdyn_customcontrolextendedsettings_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_AsyncOperations](asyncoperation.md#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders"></a> msdyn_customcontrolextendedsettings_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_customcontrolextendedsettings_ProcessSession"></a> msdyn_customcontrolextendedsettings_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_ProcessSession](processsession.md#BKMK_msdyn_customcontrolextendedsettings_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures"></a> msdyn_customcontrolextendedsettings_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses"></a> msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_customcontrolextendedsettings_createdby](#BKMK_lk_msdyn_customcontrolextendedsettings_createdby)
- [lk_msdyn_customcontrolextendedsettings_createdonbehalfby](#BKMK_lk_msdyn_customcontrolextendedsettings_createdonbehalfby)
- [lk_msdyn_customcontrolextendedsettings_modifiedby](#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedby)
- [lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby](#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby)
- [user_msdyn_customcontrolextendedsettings](#BKMK_user_msdyn_customcontrolextendedsettings)
- [team_msdyn_customcontrolextendedsettings](#BKMK_team_msdyn_customcontrolextendedsettings)
- [business_unit_msdyn_customcontrolextendedsettings](#BKMK_business_unit_msdyn_customcontrolextendedsettings)


### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_createdby"></a> lk_msdyn_customcontrolextendedsettings_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_customcontrolextendedsettings_createdby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_createdonbehalfby"></a> lk_msdyn_customcontrolextendedsettings_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_customcontrolextendedsettings_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_modifiedby"></a> lk_msdyn_customcontrolextendedsettings_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_customcontrolextendedsettings_modifiedby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby"></a> lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msdyn_customcontrolextendedsettings"></a> user_msdyn_customcontrolextendedsettings

**Added by**: System Solution Solution

See the [user_msdyn_customcontrolextendedsettings](systemuser.md#BKMK_user_msdyn_customcontrolextendedsettings) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msdyn_customcontrolextendedsettings"></a> team_msdyn_customcontrolextendedsettings

**Added by**: System Solution Solution

See the [team_msdyn_customcontrolextendedsettings](team.md#BKMK_team_msdyn_customcontrolextendedsettings) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msdyn_customcontrolextendedsettings"></a> business_unit_msdyn_customcontrolextendedsettings

**Added by**: System Solution Solution

See the [business_unit_msdyn_customcontrolextendedsettings](businessunit.md#BKMK_business_unit_msdyn_customcontrolextendedsettings) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_customcontrolextendedsettings?text=msdyn_customcontrolextendedsettings EntityType" />