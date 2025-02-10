---
title: "organizationdatasyncstate table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the organizationdatasyncstate table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# organizationdatasyncstate table/entity reference (Microsoft Dataverse)

Information regarding data synchronization state

## Messages

The following table lists the messages for the organizationdatasyncstate table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /organizationdatasyncstates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /organizationdatasyncstates(*organizationdatasyncstateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /organizationdatasyncstates(*organizationdatasyncstateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /organizationdatasyncstates<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /organizationdatasyncstates(*organizationdatasyncstateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /organizationdatasyncstates(*organizationdatasyncstateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /organizationdatasyncstates(*organizationdatasyncstateid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the organizationdatasyncstate table.

|Property|Value|
| --- | --- |
| **DisplayName** | **OrganizationDataSyncState** |
| **DisplayCollectionName** | **OrganizationDataSyncStates** |
| **SchemaName** | `organizationdatasyncstate` |
| **CollectionSchemaName** | `organizationdatasyncstates` |
| **EntitySetName** | `organizationdatasyncstates`|
| **LogicalName** | `organizationdatasyncstate` |
| **LogicalCollectionName** | `organizationdatasyncstates` |
| **PrimaryIdAttribute** | `organizationdatasyncstateid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Continue from last delta sync**|
|DisplayName|**continuefromlastdeltasync**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`continuefromlastdeltasync`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncstate_continuefromlastdeltasync`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_currentfullsyncfetchxml"></a> currentfullsyncfetchxml

|Property|Value|
|---|---|
|Description||
|DisplayName|**currentfullsyncfetchxml**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`currentfullsyncfetchxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_currentfullsyncstate"></a> currentfullsyncstate

|Property|Value|
|---|---|
|Description||
|DisplayName|**currentfullsyncstate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`currentfullsyncstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`fullsyncstate`|

#### currentfullsyncstate Choices/Options

|Value|Label|
|---|---|
|0|**NotInitialized**|
|1|**Initiating**|
|2|**InProgress**|
|3|**Completed**|
|4|**Invalid**|
|5|**AcceptMerge**|
|6|**Failed**|

### <a name="BKMK_entityname"></a> entityname

|Property|Value|
|---|---|
|Description||
|DisplayName|**entityname**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityname`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organizationdatasyncsubscriptionentity|

### <a name="BKMK_fullsynconly"></a> fullsynconly

|Property|Value|
|---|---|
|Description||
|DisplayName|**fullsynconly**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fullsynconly`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncstate_fullsynconly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_fullsyncpagesdata"></a> fullsyncpagesdata

|Property|Value|
|---|---|
|Description||
|DisplayName|**fullsyncpagesdata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fullsyncpagesdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_implicitlastdataversion"></a> implicitlastdataversion

|Property|Value|
|---|---|
|Description||
|DisplayName|**implicitlastdataversion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`implicitlastdataversion`|
|RequiredLevel|None|
|Type|String|
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

### <a name="BKMK_lastdataversion"></a> lastdataversion

|Property|Value|
|---|---|
|Description||
|DisplayName|**lastdataversion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastdataversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_lastmetadataversion"></a> lastmetadataversion

|Property|Value|
|---|---|
|Description|**Last Metadata Version**|
|DisplayName|**lastmetadataversion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastmetadataversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_lockexpiretimestamp"></a> lockexpiretimestamp

|Property|Value|
|---|---|
|Description||
|DisplayName|**LockExpireTimestamp**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lockexpiretimestamp`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_lockowner"></a> lockowner

|Property|Value|
|---|---|
|Description||
|DisplayName|**LockOwner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lockowner`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_minactiverowversion"></a> minactiverowversion

|Property|Value|
|---|---|
|Description||
|DisplayName|**minactiverowversion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`minactiverowversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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
|MaxLength|200|

### <a name="BKMK_nullstatedate"></a> nullstatedate

|Property|Value|
|---|---|
|Description||
|DisplayName|**nullstatedate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`nullstatedate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_organizationdatasyncstateId"></a> organizationdatasyncstateId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**OrganizationDataSyncState**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationdatasyncstateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscriptionid

|Property|Value|
|---|---|
|Description|**Organization Data Sync Subscription Id**|
|DisplayName|**organizationdatasyncsubscriptionid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organizationdatasyncsubscriptionid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organizationdatasyncsubscription|

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

### <a name="BKMK_pagenumber"></a> pagenumber

|Property|Value|
|---|---|
|Description|**pagenumber**|
|DisplayName|**pagenumber**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pagenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_paginationcookie"></a> paginationcookie

|Property|Value|
|---|---|
|Description||
|DisplayName|**paginationcookie**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`paginationcookie`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300000|

### <a name="BKMK_pagingcookie"></a> pagingcookie

|Property|Value|
|---|---|
|Description||
|DisplayName|**pagingcookie**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pagingcookie`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_partitionid"></a> partitionid

|Property|Value|
|---|---|
|Description||
|DisplayName|**PartitionId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_partitionssyncstatedata"></a> partitionssyncstatedata

|Property|Value|
|---|---|
|Description|**SyncStatesForPartitions**|
|DisplayName|**partitionssyncstatedata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionssyncstatedata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the OrganizationDataSyncState**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`organizationdatasyncstate_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the OrganizationDataSyncState**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`organizationdatasyncstate_statuscode`|

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

### <a name="BKMK_usepagingcookiemax"></a> usepagingcookiemax

|Property|Value|
|---|---|
|Description||
|DisplayName|**usepagingcookiemax**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usepagingcookiemax`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncstate_usepagingcookiemax`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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

- [lk_organizationdatasyncstate_createdby](#BKMK_lk_organizationdatasyncstate_createdby)
- [lk_organizationdatasyncstate_createdonbehalfby](#BKMK_lk_organizationdatasyncstate_createdonbehalfby)
- [lk_organizationdatasyncstate_modifiedby](#BKMK_lk_organizationdatasyncstate_modifiedby)
- [lk_organizationdatasyncstate_modifiedonbehalfby](#BKMK_lk_organizationdatasyncstate_modifiedonbehalfby)
- [organization_organizationdatasyncstate](#BKMK_organization_organizationdatasyncstate)
- [organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid)
- [organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname](#BKMK_organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname)

### <a name="BKMK_lk_organizationdatasyncstate_createdby"></a> lk_organizationdatasyncstate_createdby

One-To-Many Relationship: [systemuser lk_organizationdatasyncstate_createdby](systemuser.md#BKMK_lk_organizationdatasyncstate_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncstate_createdonbehalfby"></a> lk_organizationdatasyncstate_createdonbehalfby

One-To-Many Relationship: [systemuser lk_organizationdatasyncstate_createdonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncstate_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncstate_modifiedby"></a> lk_organizationdatasyncstate_modifiedby

One-To-Many Relationship: [systemuser lk_organizationdatasyncstate_modifiedby](systemuser.md#BKMK_lk_organizationdatasyncstate_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncstate_modifiedonbehalfby"></a> lk_organizationdatasyncstate_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_organizationdatasyncstate_modifiedonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncstate_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_organizationdatasyncstate"></a> organization_organizationdatasyncstate

One-To-Many Relationship: [organization organization_organizationdatasyncstate](organization.md#BKMK_organization_organizationdatasyncstate)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingEntityNavigationPropertyName|`organizationdatasyncsubscriptionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname"></a> organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_organizationdatasyncstate_entityname)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`entityname`|
|ReferencingEntityNavigationPropertyName|`entityname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [organizationdatasyncstate_AsyncOperations](#BKMK_organizationdatasyncstate_AsyncOperations)
- [organizationdatasyncstate_BulkDeleteFailures](#BKMK_organizationdatasyncstate_BulkDeleteFailures)
- [organizationdatasyncstate_DuplicateBaseRecord](#BKMK_organizationdatasyncstate_DuplicateBaseRecord)
- [organizationdatasyncstate_DuplicateMatchingRecord](#BKMK_organizationdatasyncstate_DuplicateMatchingRecord)
- [organizationdatasyncstate_MailboxTrackingFolders](#BKMK_organizationdatasyncstate_MailboxTrackingFolders)
- [organizationdatasyncstate_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses)
- [organizationdatasyncstate_ProcessSession](#BKMK_organizationdatasyncstate_ProcessSession)
- [organizationdatasyncstate_SyncErrors](#BKMK_organizationdatasyncstate_SyncErrors)

### <a name="BKMK_organizationdatasyncstate_AsyncOperations"></a> organizationdatasyncstate_AsyncOperations

Many-To-One Relationship: [asyncoperation organizationdatasyncstate_AsyncOperations](asyncoperation.md#BKMK_organizationdatasyncstate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncstate_BulkDeleteFailures"></a> organizationdatasyncstate_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure organizationdatasyncstate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_organizationdatasyncstate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncstate_DuplicateBaseRecord"></a> organizationdatasyncstate_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord organizationdatasyncstate_DuplicateBaseRecord](duplicaterecord.md#BKMK_organizationdatasyncstate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncstate_DuplicateMatchingRecord"></a> organizationdatasyncstate_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord organizationdatasyncstate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_organizationdatasyncstate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncstate_MailboxTrackingFolders"></a> organizationdatasyncstate_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder organizationdatasyncstate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_organizationdatasyncstate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses"></a> organizationdatasyncstate_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess organizationdatasyncstate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncstate_ProcessSession"></a> organizationdatasyncstate_ProcessSession

Many-To-One Relationship: [processsession organizationdatasyncstate_ProcessSession](processsession.md#BKMK_organizationdatasyncstate_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncstate_SyncErrors"></a> organizationdatasyncstate_SyncErrors

Many-To-One Relationship: [syncerror organizationdatasyncstate_SyncErrors](syncerror.md#BKMK_organizationdatasyncstate_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncstate_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.organizationdatasyncstate?displayProperty=fullName>
