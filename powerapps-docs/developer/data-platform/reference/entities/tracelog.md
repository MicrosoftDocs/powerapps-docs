---
title: "Trace (TraceLog) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Trace (TraceLog) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Trace (TraceLog) table/entity reference (Microsoft Dataverse)

A trace log.

## Messages

The following table lists the messages for the Trace (TraceLog) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /tracelogs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /tracelogs(*tracelogid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /tracelogs(*tracelogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /tracelogs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Trace (TraceLog) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Trace** |
| **DisplayCollectionName** | **Traces** |
| **SchemaName** | `TraceLog` |
| **CollectionSchemaName** | `TraceLogs` |
| **EntitySetName** | `tracelogs`|
| **LogicalName** | `tracelog` |
| **LogicalCollectionName** | `tracelogs` |
| **PrimaryIdAttribute** | `tracelogid` |
| **PrimaryNameAttribute** |`text` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeDeleted](#BKMK_CanBeDeleted)
- [CollationLevel](#BKMK_CollationLevel)
- [ErrorDetails](#BKMK_ErrorDetails)
- [ErrorTypeDisplay](#BKMK_ErrorTypeDisplay)
- [IsUnique](#BKMK_IsUnique)
- [Level](#BKMK_Level)
- [MachineName](#BKMK_MachineName)
- [ParentTraceLogId](#BKMK_ParentTraceLogId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Text](#BKMK_Text)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TraceActionXml](#BKMK_TraceActionXml)
- [TraceCode](#BKMK_TraceCode)
- [TraceDetailXml](#BKMK_TraceDetailXml)
- [TraceLogId](#BKMK_TraceLogId)
- [TraceParameterXml](#BKMK_TraceParameterXml)
- [TraceStatus](#BKMK_TraceStatus)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|---|---|
|Description|**Indicates if this trace log can be deleted.**|
|DisplayName|**Trace CanBeDeleted Flag**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbedeleted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`tracelog_canbedeleted`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CollationLevel"></a> CollationLevel

|Property|Value|
|---|---|
|Description|**Indicates the collation level**|
|DisplayName|**Collation Level**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`collationlevel`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ErrorDetails"></a> ErrorDetails

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`errordetails`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_ErrorTypeDisplay"></a> ErrorTypeDisplay

|Property|Value|
|---|---|
|Description||
|DisplayName|**Trace Error Details**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`errortypedisplay`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_IsUnique"></a> IsUnique

|Property|Value|
|---|---|
|Description|**Tells if this traceLog is created uniquely(only one) for the associated entity.**|
|DisplayName|**Is Unique Trace**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isunique`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`tracelog_isunique`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Level"></a> Level

|Property|Value|
|---|---|
|Description|**Information about the trace level.**|
|DisplayName|**Level**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`level`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`tracelog_level`|

#### Level Choices/Options

|Value|Label|
|---|---|
|1|**Information**|
|2|**Warning**|
|3|**Error**|

### <a name="BKMK_MachineName"></a> MachineName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`machinename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_ParentTraceLogId"></a> ParentTraceLogId

|Property|Value|
|---|---|
|Description|**Indicates the parent ID of the trace log.**|
|DisplayName|**Parent Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parenttracelogid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|tracelog|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Regarding mailbox or email server profile.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|emailserverprofile, mailbox|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of the regarding object.**|
|DisplayName|**Regarding Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Text"></a> Text

|Property|Value|
|---|---|
|Description|**Text of the trace.**|
|DisplayName|**Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`text`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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

### <a name="BKMK_TraceActionXml"></a> TraceActionXml

|Property|Value|
|---|---|
|Description|**XML representation of the trace actions.**|
|DisplayName|**Trace Actions XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traceactionxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_TraceCode"></a> TraceCode

|Property|Value|
|---|---|
|Description|**Error code.**|
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tracecode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_TraceDetailXml"></a> TraceDetailXml

|Property|Value|
|---|---|
|Description|**XML representation of the trace details.**|
|DisplayName|**Trace Detail XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tracedetailxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_TraceLogId"></a> TraceLogId

|Property|Value|
|---|---|
|Description|**Unique identifier of the trace.**|
|DisplayName|**Trace**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tracelogid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TraceParameterXml"></a> TraceParameterXml

|Property|Value|
|---|---|
|Description|**XML representation of the trace parameters.**|
|DisplayName|**Trace Parameter XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traceparameterxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_TraceStatus"></a> TraceStatus

|Property|Value|
|---|---|
|Description|**Status about the trace.**|
|DisplayName|**Trace Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tracestatus`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`tracelog_tracestatus`|
|DefaultValue|False|
|True Label|Success|
|False Label|Failure|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the trace was created.**|
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
- [RegardingObjectOwnerId](#BKMK_RegardingObjectOwnerId)
- [RegardingObjectOwnerIdType](#BKMK_RegardingObjectOwnerIdType)
- [RegardingObjectOwningBusinessUnit](#BKMK_RegardingObjectOwningBusinessUnit)
- [TraceParameterHash](#BKMK_TraceParameterHash)
- [TraceRegardingId](#BKMK_TraceRegardingId)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the trace.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Time the error is created and logged.**|
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
|Description|**Unique identifier of the delegate user who created the trace.**|
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
|Description|**Unique identifier of the user who modified the trace.**|
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
|Description|**Time the error is updated and logged for the same regarding object.**|
|DisplayName|**Last Update On**|
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
|Description|**Unique identifier of the delegate user who modified the trace.**|
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
|Description|**Unique identifier of the organization associated with the trace.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_RegardingObjectOwnerId"></a> RegardingObjectOwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the regarding object.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_RegardingObjectOwnerIdType"></a> RegardingObjectOwnerIdType

|Property|Value|
|---|---|
|Description|**Owner type of the regarding object.**|
|DisplayName|**Owner Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectowneridtype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RegardingObjectOwningBusinessUnit"></a> RegardingObjectOwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the regarding object.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectowningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_TraceParameterHash"></a> TraceParameterHash

|Property|Value|
|---|---|
|Description|**Stores the hash of the entity object associated with this tracelog. Hash is computed using the object type code and its id.**|
|DisplayName|**Trace Parameter Hash**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traceparameterhash`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TraceRegardingId"></a> TraceRegardingId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Trace Regarding**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`traceregardingid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|traceregarding|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_tracelog_createdby](#BKMK_lk_tracelog_createdby)
- [lk_tracelog_createdonbehalfby](#BKMK_lk_tracelog_createdonbehalfby)
- [lk_tracelog_modifiedby](#BKMK_lk_tracelog_modifiedby)
- [lk_tracelog_modifiedonbehalfby](#BKMK_lk_tracelog_modifiedonbehalfby)
- [organization_tracelog](#BKMK_organization_tracelog)
- [tracelog_EmailServerProfile](#BKMK_tracelog_EmailServerProfile)
- [tracelog_Mailbox](#BKMK_tracelog_Mailbox)
- [tracelog_parent_tracelog](#BKMK_tracelog_parent_tracelog-many-to-one)

### <a name="BKMK_lk_tracelog_createdby"></a> lk_tracelog_createdby

One-To-Many Relationship: [systemuser lk_tracelog_createdby](systemuser.md#BKMK_lk_tracelog_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_tracelog_createdonbehalfby"></a> lk_tracelog_createdonbehalfby

One-To-Many Relationship: [systemuser lk_tracelog_createdonbehalfby](systemuser.md#BKMK_lk_tracelog_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_tracelog_modifiedby"></a> lk_tracelog_modifiedby

One-To-Many Relationship: [systemuser lk_tracelog_modifiedby](systemuser.md#BKMK_lk_tracelog_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_tracelog_modifiedonbehalfby"></a> lk_tracelog_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_tracelog_modifiedonbehalfby](systemuser.md#BKMK_lk_tracelog_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_tracelog"></a> organization_tracelog

One-To-Many Relationship: [organization organization_tracelog](organization.md#BKMK_organization_tracelog)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tracelog_EmailServerProfile"></a> tracelog_EmailServerProfile

One-To-Many Relationship: [emailserverprofile tracelog_EmailServerProfile](emailserverprofile.md#BKMK_tracelog_EmailServerProfile)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailserverprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tracelog_Mailbox"></a> tracelog_Mailbox

One-To-Many Relationship: [mailbox tracelog_Mailbox](mailbox.md#BKMK_tracelog_Mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tracelog_parent_tracelog-many-to-one"></a> tracelog_parent_tracelog

One-To-Many Relationship: [tracelog tracelog_parent_tracelog](#BKMK_tracelog_parent_tracelog-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`tracelog`|
|ReferencedAttribute|`tracelogid`|
|ReferencingAttribute|`parenttracelogid`|
|ReferencingEntityNavigationPropertyName|`parenttracelogid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_tracelog_parent_tracelog-one-to-many"></a> tracelog_parent_tracelog

Many-To-One Relationship: [tracelog tracelog_parent_tracelog](#BKMK_tracelog_parent_tracelog-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`tracelog`|
|ReferencingAttribute|`parenttracelogid`|
|ReferencedEntityNavigationPropertyName|`tracelog_parent_tracelog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.tracelog?displayProperty=fullName>
