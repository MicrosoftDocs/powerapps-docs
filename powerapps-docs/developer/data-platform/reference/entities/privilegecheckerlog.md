---
title: "Privilege Checker Log (PrivilegeCheckerLog) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Privilege Checker Log (PrivilegeCheckerLog) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Privilege Checker Log (PrivilegeCheckerLog) table/entity reference (Microsoft Dataverse)

Holds information about privilege checks for the user who started (created) a privilege checker tool run (Privilege Checker Run's child entity)

## Messages

The following table lists the messages for the Privilege Checker Log (PrivilegeCheckerLog) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /privilegecheckerlogs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /privilegecheckerlogs(*privilegecheckerlogid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /privilegecheckerlogs(*privilegecheckerlogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /privilegecheckerlogs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /privilegecheckerlogs(*privilegecheckerlogid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /privilegecheckerlogs(*privilegecheckerlogid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Privilege Checker Log (PrivilegeCheckerLog) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Privilege Checker Log** |
| **DisplayCollectionName** | **Privilege Checker Logs** |
| **SchemaName** | `PrivilegeCheckerLog` |
| **CollectionSchemaName** | `PrivilegeCheckerLogs` |
| **EntitySetName** | `privilegecheckerlogs`|
| **LogicalName** | `privilegecheckerlog` |
| **LogicalCollectionName** | `privilegecheckerlogs` |
| **PrimaryIdAttribute** | `privilegecheckerlogid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_PrivilegeCheckerRunId"></a> PrivilegeCheckerRunId

|Property|Value|
|---|---|
|Description|**Privilege Checker Run for this log**|
|DisplayName|**Privilege Checker Run**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`privilegecheckerrunid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|privilegecheckerrun|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CheckedPrivilege](#BKMK_CheckedPrivilege)
- [CheckedUser](#BKMK_CheckedUser)
- [CheckType](#BKMK_CheckType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ImpersonatingUser](#BKMK_ImpersonatingUser)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [PrivilegeCheckerLogId](#BKMK_PrivilegeCheckerLogId)
- [PrivilegeDepth](#BKMK_PrivilegeDepth)
- [Request](#BKMK_Request)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SupportingCaller](#BKMK_SupportingCaller)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CheckedPrivilege"></a> CheckedPrivilege

|Property|Value|
|---|---|
|Description|**The checked privilege.**|
|DisplayName|**Checked Privilege**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`checkedprivilege`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|privilege|

### <a name="BKMK_CheckedUser"></a> CheckedUser

|Property|Value|
|---|---|
|Description|**The user whose privilege was checked.**|
|DisplayName|**Checked User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`checkeduser`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CheckType"></a> CheckType

|Property|Value|
|---|---|
|Description|**The type of authorization check that was done.**|
|DisplayName|**Check Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`checktype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|5|
|GlobalChoiceName|`privilegecheckerlog_checktype`|

#### CheckType Choices/Options

|Value|Label|
|---|---|
|1|**Privilege Check**|
|2|**Access check**|

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

### <a name="BKMK_ImpersonatingUser"></a> ImpersonatingUser

|Property|Value|
|---|---|
|Description|**If this was an impersonation, this will give who was impersonating -- in this case, their privilege was also checked.**|
|DisplayName|**Impersonating User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`impersonatinguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the log.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
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
|DisplayName|**Owner Id Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_PrivilegeCheckerLogId"></a> PrivilegeCheckerLogId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Privilege Checker Log**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegecheckerlogid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PrivilegeDepth"></a> PrivilegeDepth

|Property|Value|
|---|---|
|Description|**Depth that was checked for the privilege.**|
|DisplayName|**Privilege Depth**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`privilegedepth`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|5|
|GlobalChoiceName|`privilegecheckerlog_privilegedepth`|

#### PrivilegeDepth Choices/Options

|Value|Label|
|---|---|
|0|**Basic**|
|1|**Local**|
|2|**Deep**|
|3|**Global**|
|4|**Record Filter**|
|5|**N/A**|

### <a name="BKMK_Request"></a> Request

|Property|Value|
|---|---|
|Description|**A brief description of the web request.**|
|DisplayName|**Request**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`request`|
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
|Description|**Status of the Privilege checker log**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`privilegecheckerlog_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Privilege checker log**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`privilegecheckerlog_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SupportingCaller"></a> SupportingCaller

|Property|Value|
|---|---|
|Description|**If this was a flow execution, this will give who was the owner of the flow -- in this case, their privilege was also checked.**|
|DisplayName|**Supporting Caller**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`supportingcaller`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

- [lk_privilegecheckerlog_createdby](#BKMK_lk_privilegecheckerlog_createdby)
- [lk_privilegecheckerlog_createdonbehalfby](#BKMK_lk_privilegecheckerlog_createdonbehalfby)
- [lk_privilegecheckerlog_modifiedby](#BKMK_lk_privilegecheckerlog_modifiedby)
- [lk_privilegecheckerlog_modifiedonbehalfby](#BKMK_lk_privilegecheckerlog_modifiedonbehalfby)
- [privilegecheckerlog_CheckedPrivilege](#BKMK_privilegecheckerlog_CheckedPrivilege)
- [privilegecheckerlog_CheckedUser_systemuser](#BKMK_privilegecheckerlog_CheckedUser_systemuser)
- [privilegecheckerlog_ImpersonatingUser_systemuser](#BKMK_privilegecheckerlog_ImpersonatingUser_systemuser)
- [privilegecheckerlog_SupportingCaller_systemuser](#BKMK_privilegecheckerlog_SupportingCaller_systemuser)
- [privilegecheckerrun_privilegecheckerlog](#BKMK_privilegecheckerrun_privilegecheckerlog)

### <a name="BKMK_lk_privilegecheckerlog_createdby"></a> lk_privilegecheckerlog_createdby

One-To-Many Relationship: [systemuser lk_privilegecheckerlog_createdby](systemuser.md#BKMK_lk_privilegecheckerlog_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_privilegecheckerlog_createdonbehalfby"></a> lk_privilegecheckerlog_createdonbehalfby

One-To-Many Relationship: [systemuser lk_privilegecheckerlog_createdonbehalfby](systemuser.md#BKMK_lk_privilegecheckerlog_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_privilegecheckerlog_modifiedby"></a> lk_privilegecheckerlog_modifiedby

One-To-Many Relationship: [systemuser lk_privilegecheckerlog_modifiedby](systemuser.md#BKMK_lk_privilegecheckerlog_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_privilegecheckerlog_modifiedonbehalfby"></a> lk_privilegecheckerlog_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_privilegecheckerlog_modifiedonbehalfby](systemuser.md#BKMK_lk_privilegecheckerlog_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_CheckedPrivilege"></a> privilegecheckerlog_CheckedPrivilege

One-To-Many Relationship: [privilege privilegecheckerlog_CheckedPrivilege](privilege.md#BKMK_privilegecheckerlog_CheckedPrivilege)

|Property|Value|
|---|---|
|ReferencedEntity|`privilege`|
|ReferencedAttribute|`privilegeid`|
|ReferencingAttribute|`checkedprivilege`|
|ReferencingEntityNavigationPropertyName|`CheckedPrivilege`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_CheckedUser_systemuser"></a> privilegecheckerlog_CheckedUser_systemuser

One-To-Many Relationship: [systemuser privilegecheckerlog_CheckedUser_systemuser](systemuser.md#BKMK_privilegecheckerlog_CheckedUser_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`checkeduser`|
|ReferencingEntityNavigationPropertyName|`CheckedUser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_ImpersonatingUser_systemuser"></a> privilegecheckerlog_ImpersonatingUser_systemuser

One-To-Many Relationship: [systemuser privilegecheckerlog_ImpersonatingUser_systemuser](systemuser.md#BKMK_privilegecheckerlog_ImpersonatingUser_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`impersonatinguser`|
|ReferencingEntityNavigationPropertyName|`ImpersonatingUser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_SupportingCaller_systemuser"></a> privilegecheckerlog_SupportingCaller_systemuser

One-To-Many Relationship: [systemuser privilegecheckerlog_SupportingCaller_systemuser](systemuser.md#BKMK_privilegecheckerlog_SupportingCaller_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`supportingcaller`|
|ReferencingEntityNavigationPropertyName|`SupportingCaller`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_privilegecheckerlog"></a> privilegecheckerrun_privilegecheckerlog

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_privilegecheckerlog](privilegecheckerrun.md#BKMK_privilegecheckerrun_privilegecheckerlog)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`privilegecheckerrunid`|
|ReferencingEntityNavigationPropertyName|`PrivilegeCheckerRunId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [privilegecheckerlog_AsyncOperations](#BKMK_privilegecheckerlog_AsyncOperations)
- [privilegecheckerlog_BulkDeleteFailures](#BKMK_privilegecheckerlog_BulkDeleteFailures)
- [privilegecheckerlog_MailboxTrackingFolders](#BKMK_privilegecheckerlog_MailboxTrackingFolders)
- [privilegecheckerlog_PrincipalObjectAttributeAccesses](#BKMK_privilegecheckerlog_PrincipalObjectAttributeAccesses)
- [privilegecheckerlog_ProcessSession](#BKMK_privilegecheckerlog_ProcessSession)
- [privilegecheckerlog_SyncErrors](#BKMK_privilegecheckerlog_SyncErrors)

### <a name="BKMK_privilegecheckerlog_AsyncOperations"></a> privilegecheckerlog_AsyncOperations

Many-To-One Relationship: [asyncoperation privilegecheckerlog_AsyncOperations](asyncoperation.md#BKMK_privilegecheckerlog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegecheckerlog_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegecheckerlog_BulkDeleteFailures"></a> privilegecheckerlog_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure privilegecheckerlog_BulkDeleteFailures](bulkdeletefailure.md#BKMK_privilegecheckerlog_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegecheckerlog_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegecheckerlog_MailboxTrackingFolders"></a> privilegecheckerlog_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder privilegecheckerlog_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_privilegecheckerlog_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegecheckerlog_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegecheckerlog_PrincipalObjectAttributeAccesses"></a> privilegecheckerlog_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess privilegecheckerlog_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_privilegecheckerlog_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`privilegecheckerlog_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegecheckerlog_ProcessSession"></a> privilegecheckerlog_ProcessSession

Many-To-One Relationship: [processsession privilegecheckerlog_ProcessSession](processsession.md#BKMK_privilegecheckerlog_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegecheckerlog_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegecheckerlog_SyncErrors"></a> privilegecheckerlog_SyncErrors

Many-To-One Relationship: [syncerror privilegecheckerlog_SyncErrors](syncerror.md#BKMK_privilegecheckerlog_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegecheckerlog_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.privilegecheckerlog?displayProperty=fullName>
