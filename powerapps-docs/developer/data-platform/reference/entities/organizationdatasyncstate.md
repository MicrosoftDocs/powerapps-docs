---
title: "organizationdatasyncstate table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the organizationdatasyncstate table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# organizationdatasyncstate table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Information regarding data synchronization state

**Added by**: DataSyncState Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /organizationdatasyncstates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /organizationdatasyncstates(*organizationdatasyncstateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET /organizationdatasyncstates(*organizationdatasyncstateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /organizationdatasyncstates<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH /organizationdatasyncstates(*organizationdatasyncstateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /organizationdatasyncstates(*organizationdatasyncstateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|organizationdatasyncstates|
|DisplayCollectionName|OrganizationDataSyncStates|
|DisplayName|OrganizationDataSyncState|
|EntitySetName|organizationdatasyncstates|
|IsBPFEntity|False|
|LogicalCollectionName|organizationdatasyncstates|
|LogicalName|organizationdatasyncstate|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|organizationdatasyncstateid|
|PrimaryNameAttribute|name|
|SchemaName|organizationdatasyncstate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [continuefromlastdeltasync](#BKMK_continuefromlastdeltasync)
- [currentfullsyncfetchxml](#BKMK_currentfullsyncfetchxml)
- [currentfullsyncstate](#BKMK_currentfullsyncstate)
- [entityname](#BKMK_entityname)
- [fullsynconly](#BKMK_fullsynconly)
- [fullsyncpagesdata](#BKMK_fullsyncpagesdata)
- [implicitlastdataversion](#BKMK_implicitlastdataversion)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [lastdataversion](#BKMK_lastdataversion)
- [lastmetadataversion](#BKMK_lastmetadataversion)
- [lockexpiretimestamp](#BKMK_lockexpiretimestamp)
- [lockowner](#BKMK_lockowner)
- [minactiverowversion](#BKMK_minactiverowversion)
- [name](#BKMK_name)
- [nullstatedate](#BKMK_nullstatedate)
- [organizationdatasyncstateId](#BKMK_organizationdatasyncstateId)
- [organizationdatasyncsubscriptionid](#BKMK_organizationdatasyncsubscriptionid)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [pagenumber](#BKMK_pagenumber)
- [paginationcookie](#BKMK_paginationcookie)
- [pagingcookie](#BKMK_pagingcookie)
- [partitionid](#BKMK_partitionid)
- [partitionssyncstatedata](#BKMK_partitionssyncstatedata)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [usepagingcookiemax](#BKMK_usepagingcookiemax)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_continuefromlastdeltasync"></a> continuefromlastdeltasync

|Property|Value|
|--------|-----|
|Description|Continue from last delta sync|
|DisplayName|continuefromlastdeltasync|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|continuefromlastdeltasync|
|RequiredLevel|None|
|Type|Boolean|

#### continuefromlastdeltasync Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_currentfullsyncfetchxml"></a> currentfullsyncfetchxml

|Property|Value|
|--------|-----|
|Description||
|DisplayName|currentfullsyncfetchxml|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|currentfullsyncfetchxml|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_currentfullsyncstate"></a> currentfullsyncstate

|Property|Value|
|--------|-----|
|Description||
|DisplayName|currentfullsyncstate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|currentfullsyncstate|
|RequiredLevel|None|
|Type|Picklist|

#### currentfullsyncstate Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|NotInitialized||
|1|Initiating||
|2|InProgress||
|3|Completed||
|4|Invalid||
|5|AcceptMerge||
|6|Failed||



### <a name="BKMK_entityname"></a> entityname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|entityname|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entityname|
|RequiredLevel|SystemRequired|
|Targets|organizationdatasyncsubscriptionentity|
|Type|Lookup|


### <a name="BKMK_fullsynconly"></a> fullsynconly

|Property|Value|
|--------|-----|
|Description||
|DisplayName|fullsynconly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fullsynconly|
|RequiredLevel|None|
|Type|Boolean|

#### fullsynconly Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_fullsyncpagesdata"></a> fullsyncpagesdata

|Property|Value|
|--------|-----|
|Description||
|DisplayName|fullsyncpagesdata|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fullsyncpagesdata|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_implicitlastdataversion"></a> implicitlastdataversion

|Property|Value|
|--------|-----|
|Description||
|DisplayName|implicitlastdataversion|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|implicitlastdataversion|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_lastdataversion"></a> lastdataversion

|Property|Value|
|--------|-----|
|Description||
|DisplayName|lastdataversion|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastdataversion|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_lastmetadataversion"></a> lastmetadataversion

|Property|Value|
|--------|-----|
|Description|Last Metadata Version|
|DisplayName|lastmetadataversion|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastmetadataversion|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_lockexpiretimestamp"></a> lockexpiretimestamp

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|LockExpireTimestamp|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lockexpiretimestamp|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_lockowner"></a> lockowner

|Property|Value|
|--------|-----|
|Description||
|DisplayName|LockOwner|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lockowner|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_minactiverowversion"></a> minactiverowversion

|Property|Value|
|--------|-----|
|Description||
|DisplayName|minactiverowversion|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|minactiverowversion|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


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
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_nullstatedate"></a> nullstatedate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|nullstatedate|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|nullstatedate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_organizationdatasyncstateId"></a> organizationdatasyncstateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|OrganizationDataSyncState|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|organizationdatasyncstateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscriptionid

|Property|Value|
|--------|-----|
|Description|Organization Data Sync Subscription Id|
|DisplayName|organizationdatasyncsubscriptionid|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|organizationdatasyncsubscriptionid|
|RequiredLevel|SystemRequired|
|Targets|organizationdatasyncsubscription|
|Type|Lookup|


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


### <a name="BKMK_pagenumber"></a> pagenumber

|Property|Value|
|--------|-----|
|Description|pagenumber|
|DisplayName|pagenumber|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|pagenumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_paginationcookie"></a> paginationcookie

|Property|Value|
|--------|-----|
|Description||
|DisplayName|paginationcookie|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|paginationcookie|
|MaxLength|300000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_pagingcookie"></a> pagingcookie

|Property|Value|
|--------|-----|
|Description||
|DisplayName|pagingcookie|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|pagingcookie|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_partitionid"></a> partitionid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|PartitionId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|partitionid|
|MaxLength|300|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_partitionssyncstatedata"></a> partitionssyncstatedata

|Property|Value|
|--------|-----|
|Description|SyncStatesForPartitions|
|DisplayName|partitionssyncstatedata|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partitionssyncstatedata|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the OrganizationDataSyncState|
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
|Description|Reason for the status of the OrganizationDataSyncState|
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


### <a name="BKMK_usepagingcookiemax"></a> usepagingcookiemax

|Property|Value|
|--------|-----|
|Description||
|DisplayName|usepagingcookiemax|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|usepagingcookiemax|
|RequiredLevel|None|
|Type|Boolean|

#### usepagingcookiemax Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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
- [entitynameName](#BKMK_entitynameName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [organizationdatasyncsubscriptionidName](#BKMK_organizationdatasyncsubscriptionidName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
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


### <a name="BKMK_entitynameName"></a> entitynameName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entitynamename|
|MaxLength|200|
|RequiredLevel|None|
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


### <a name="BKMK_organizationdatasyncsubscriptionidName"></a> organizationdatasyncsubscriptionidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationdatasyncsubscriptionidname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Added by**: Active Solution Solution

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

- [organizationdatasyncstate_SyncErrors](#BKMK_organizationdatasyncstate_SyncErrors)
- [organizationdatasyncstate_DuplicateMatchingRecord](#BKMK_organizationdatasyncstate_DuplicateMatchingRecord)
- [organizationdatasyncstate_DuplicateBaseRecord](#BKMK_organizationdatasyncstate_DuplicateBaseRecord)
- [organizationdatasyncstate_AsyncOperations](#BKMK_organizationdatasyncstate_AsyncOperations)
- [organizationdatasyncstate_MailboxTrackingFolders](#BKMK_organizationdatasyncstate_MailboxTrackingFolders)
- [organizationdatasyncstate_ProcessSession](#BKMK_organizationdatasyncstate_ProcessSession)
- [organizationdatasyncstate_BulkDeleteFailures](#BKMK_organizationdatasyncstate_BulkDeleteFailures)
- [organizationdatasyncstate_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses)


### <a name="BKMK_organizationdatasyncstate_SyncErrors"></a> organizationdatasyncstate_SyncErrors

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_SyncErrors](syncerror.md#BKMK_organizationdatasyncstate_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncstate_DuplicateMatchingRecord"></a> organizationdatasyncstate_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_organizationdatasyncstate_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncstate_DuplicateBaseRecord"></a> organizationdatasyncstate_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_DuplicateBaseRecord](duplicaterecord.md#BKMK_organizationdatasyncstate_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncstate_AsyncOperations"></a> organizationdatasyncstate_AsyncOperations

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_AsyncOperations](asyncoperation.md#BKMK_organizationdatasyncstate_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncstate_MailboxTrackingFolders"></a> organizationdatasyncstate_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_organizationdatasyncstate_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncstate_ProcessSession"></a> organizationdatasyncstate_ProcessSession

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_ProcessSession](processsession.md#BKMK_organizationdatasyncstate_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncstate_BulkDeleteFailures"></a> organizationdatasyncstate_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_organizationdatasyncstate_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses"></a> organizationdatasyncstate_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [organizationdatasyncstate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncstate_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_organizationdatasyncstate_createdby](#BKMK_lk_organizationdatasyncstate_createdby)
- [lk_organizationdatasyncstate_createdonbehalfby](#BKMK_lk_organizationdatasyncstate_createdonbehalfby)
- [lk_organizationdatasyncstate_modifiedby](#BKMK_lk_organizationdatasyncstate_modifiedby)
- [lk_organizationdatasyncstate_modifiedonbehalfby](#BKMK_lk_organizationdatasyncstate_modifiedonbehalfby)
- [organization_organizationdatasyncstate](#BKMK_organization_organizationdatasyncstate)
- [organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid)
- [organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname](#BKMK_organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname)


### <a name="BKMK_lk_organizationdatasyncstate_createdby"></a> lk_organizationdatasyncstate_createdby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncstate_createdby](systemuser.md#BKMK_lk_organizationdatasyncstate_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_organizationdatasyncstate_createdonbehalfby"></a> lk_organizationdatasyncstate_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncstate_createdonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncstate_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_organizationdatasyncstate_modifiedby"></a> lk_organizationdatasyncstate_modifiedby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncstate_modifiedby](systemuser.md#BKMK_lk_organizationdatasyncstate_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_organizationdatasyncstate_modifiedonbehalfby"></a> lk_organizationdatasyncstate_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncstate_modifiedonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncstate_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_organizationdatasyncstate"></a> organization_organizationdatasyncstate

**Added by**: System Solution Solution

See the [organization_organizationdatasyncstate](organization.md#BKMK_organization_organizationdatasyncstate) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname"></a> organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.organizationdatasyncstate?text=organizationdatasyncstate EntityType" />