---
title: "Approval Request (msdyn_flow_approvalrequest) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Approval Request (msdyn_flow_approvalrequest) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Approval Request (msdyn_flow_approvalrequest) table/entity reference (Microsoft Dataverse)

An individual request for approval.

## Messages

The following table lists the messages for the Approval Request (msdyn_flow_approvalrequest) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_flow_approvalrequests(*msdyn_flow_approvalrequestid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_flow_approvalrequests<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_flow_approvalrequests(*msdyn_flow_approvalrequestid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_flow_approvalrequests(*msdyn_flow_approvalrequestid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_flow_approvalrequests<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_flow_approvalrequests(*msdyn_flow_approvalrequestid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_flow_approvalrequests(*msdyn_flow_approvalrequestid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_flow_approvalrequests(*msdyn_flow_approvalrequestid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Approval Request (msdyn_flow_approvalrequest) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Approval Request** |
| **DisplayCollectionName** | **Approval Requests** |
| **SchemaName** | `msdyn_flow_approvalrequest` |
| **CollectionSchemaName** | `msdyn_flow_approvalrequests` |
| **EntitySetName** | `msdyn_flow_approvalrequests`|
| **LogicalName** | `msdyn_flow_approvalrequest` |
| **LogicalCollectionName** | `msdyn_flow_approvalrequests` |
| **PrimaryIdAttribute** | `msdyn_flow_approvalrequestid` |
| **PrimaryNameAttribute** |`msdyn_flow_approvalrequest_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_flow_approvalrequest_allowreassignment](#BKMK_msdyn_flow_approvalrequest_allowreassignment)
- [msdyn_flow_approvalrequest_approval](#BKMK_msdyn_flow_approvalrequest_approval)
- [msdyn_flow_approvalrequest_approvalstagekey](#BKMK_msdyn_flow_approvalrequest_approvalstagekey)
- [msdyn_flow_approvalrequest_dueon](#BKMK_msdyn_flow_approvalrequest_dueon)
- [msdyn_flow_approvalrequest_expireson](#BKMK_msdyn_flow_approvalrequest_expireson)
- [msdyn_flow_approvalrequest_lastnotifiedon](#BKMK_msdyn_flow_approvalrequest_lastnotifiedon)
- [msdyn_flow_approvalrequest_name](#BKMK_msdyn_flow_approvalrequest_name)
- [msdyn_flow_approvalrequest_notificationfrequency](#BKMK_msdyn_flow_approvalrequest_notificationfrequency)
- [msdyn_flow_approvalrequest_options](#BKMK_msdyn_flow_approvalrequest_options)
- [msdyn_flow_approvalrequest_partnermetadata](#BKMK_msdyn_flow_approvalrequest_partnermetadata)
- [msdyn_flow_approvalrequest_reassignedfrom](#BKMK_msdyn_flow_approvalrequest_reassignedfrom)
- [msdyn_flow_approvalrequest_responseoptions](#BKMK_msdyn_flow_approvalrequest_responseoptions)
- [msdyn_flow_approvalrequest_responseoptionstype](#BKMK_msdyn_flow_approvalrequest_responseoptionstype)
- [msdyn_flow_approvalrequest_stage](#BKMK_msdyn_flow_approvalrequest_stage)
- [msdyn_flow_approvalrequest_stepnumber](#BKMK_msdyn_flow_approvalrequest_stepnumber)
- [msdyn_flow_approvalrequestId](#BKMK_msdyn_flow_approvalrequestId)
- [msdyn_flow_approvalrequestidx_approvalid](#BKMK_msdyn_flow_approvalrequestidx_approvalid)
- [msdyn_flow_approvalrequestidx_owninguserid](#BKMK_msdyn_flow_approvalrequestidx_owninguserid)
- [msdyn_flow_approvalrequestidx_reassignedfromid](#BKMK_msdyn_flow_approvalrequestidx_reassignedfromid)
- [msdyn_flow_approvalrequestidx_stage](#BKMK_msdyn_flow_approvalrequestidx_stage)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [StageNumber](#BKMK_StageNumber)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_msdyn_flow_approvalrequest_allowreassignment"></a> msdyn_flow_approvalrequest_allowreassignment

|Property|Value|
|---|---|
|Description|**Whether the approval request may be reassigned to another user.**|
|DisplayName|**Allow Reassignment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_allowreassignment`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_flow_approvalrequest_msdyn_flow_approvalrequest_allowreassignment`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_flow_approvalrequest_approval"></a> msdyn_flow_approvalrequest_approval

|Property|Value|
|---|---|
|Description|**The linked approval.**|
|DisplayName|**Approval**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_approval`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msdyn_flow_approval|

### <a name="BKMK_msdyn_flow_approvalrequest_approvalstagekey"></a> msdyn_flow_approvalrequest_approvalstagekey

|Property|Value|
|---|---|
|Description|**Lookup key to match approval id and stage in fetch xml.**|
|DisplayName|**Approval Stage Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_approvalstagekey`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalrequest_dueon"></a> msdyn_flow_approvalrequest_dueon

|Property|Value|
|---|---|
|Description|**The due date.**|
|DisplayName|**Due On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_dueon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_flow_approvalrequest_expireson"></a> msdyn_flow_approvalrequest_expireson

|Property|Value|
|---|---|
|Description|**The expiration date.**|
|DisplayName|**Expires On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_expireson`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_flow_approvalrequest_lastnotifiedon"></a> msdyn_flow_approvalrequest_lastnotifiedon

|Property|Value|
|---|---|
|Description|**The last notification date.**|
|DisplayName|**Last Notified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_lastnotifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_flow_approvalrequest_name"></a> msdyn_flow_approvalrequest_name

|Property|Value|
|---|---|
|Description|**The name of the approval request.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalrequest_notificationfrequency"></a> msdyn_flow_approvalrequest_notificationfrequency

|Property|Value|
|---|---|
|Description|**The notification frequency in hours.**|
|DisplayName|**Notification Frequency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_notificationfrequency`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|87600|
|MinValue|-1|

### <a name="BKMK_msdyn_flow_approvalrequest_options"></a> msdyn_flow_approvalrequest_options

|Property|Value|
|---|---|
|Description|**The set of available response options.**|
|DisplayName|**Response Options**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_options`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_flow_approvalrequest_partnermetadata"></a> msdyn_flow_approvalrequest_partnermetadata

|Property|Value|
|---|---|
|Description|**Unstructured space to store extraneous information associated with the approval request for partner services.**|
|DisplayName|**Partner Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_partnermetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_flow_approvalrequest_reassignedfrom"></a> msdyn_flow_approvalrequest_reassignedfrom

|Property|Value|
|---|---|
|Description|**The approval request from which this one was reassigned.**|
|DisplayName|**Reassigned From**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_reassignedfrom`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_flow_approvalrequest|

### <a name="BKMK_msdyn_flow_approvalrequest_responseoptions"></a> msdyn_flow_approvalrequest_responseoptions

|Property|Value|
|---|---|
|Description|**The response options, comma-separated.**|
|DisplayName|**Response Options**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_responseoptions`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_msdyn_flow_approvalrequest_responseoptionstype"></a> msdyn_flow_approvalrequest_responseoptionstype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Response Options Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_responseoptionstype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|192350000|
|GlobalChoiceName|`msdyn_flow_approvalresponseoptionstype`|

#### msdyn_flow_approvalrequest_responseoptionstype Choices/Options

|Value|Label|
|---|---|
|192350000|**NotSpecified**|
|192350001|**BasicApproveReject**|
|192350002|**CustomOptions**|

### <a name="BKMK_msdyn_flow_approvalrequest_stage"></a> msdyn_flow_approvalrequest_stage

|Property|Value|
|---|---|
|Description|**The assigned stage of the associated approval.**|
|DisplayName|**Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_stage`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_flow_approvalstage`|

#### msdyn_flow_approvalrequest_stage Choices/Options

|Value|Label|
|---|---|
|192350000|**Not Specified**|
|192350001|**Basic**|
|192351000|**Complete**|

### <a name="BKMK_msdyn_flow_approvalrequest_stepnumber"></a> msdyn_flow_approvalrequest_stepnumber

|Property|Value|
|---|---|
|Description||
|DisplayName|**Step Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequest_stepnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_flow_approvalrequestId"></a> msdyn_flow_approvalrequestId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Approval Request**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequestid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_flow_approvalrequestidx_approvalid"></a> msdyn_flow_approvalrequestidx_approvalid

|Property|Value|
|---|---|
|Description|**Field mirroring the linked approval for the constraint index.**|
|DisplayName|**Approval Id Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequestidx_approvalid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalrequestidx_owninguserid"></a> msdyn_flow_approvalrequestidx_owninguserid

|Property|Value|
|---|---|
|Description|**Field mirroring the owning user id for the constraint index.**|
|DisplayName|**Owning User Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequestidx_owninguserid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalrequestidx_reassignedfromid"></a> msdyn_flow_approvalrequestidx_reassignedfromid

|Property|Value|
|---|---|
|Description|**Field mirroring the reassigned from id for the constraint index.**|
|DisplayName|**Reassigned From Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequestidx_reassignedfromid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approvalrequestidx_stage"></a> msdyn_flow_approvalrequestidx_stage

|Property|Value|
|---|---|
|Description|**Field mirroring the stage for the constraint index.**|
|DisplayName|**Stage Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalrequestidx_stage`|
|RequiredLevel|None|
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

### <a name="BKMK_StageNumber"></a> StageNumber

|Property|Value|
|---|---|
|Description|**The stage number to which this approval request belongs.**|
|DisplayName|**Stage Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Approval Request**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approvalrequest_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 192350000<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**The reason for the status of the request.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|ApplicationRequired|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approvalrequest_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|192350000|Label: **Reassigned**<br />State:1<br />TransitionData: None|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
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

- [business_unit_msdyn_flow_approvalrequest](#BKMK_business_unit_msdyn_flow_approvalrequest)
- [lk_msdyn_flow_approvalrequest_createdby](#BKMK_lk_msdyn_flow_approvalrequest_createdby)
- [lk_msdyn_flow_approvalrequest_createdonbehalfby](#BKMK_lk_msdyn_flow_approvalrequest_createdonbehalfby)
- [lk_msdyn_flow_approvalrequest_modifiedby](#BKMK_lk_msdyn_flow_approvalrequest_modifiedby)
- [lk_msdyn_flow_approvalrequest_modifiedonbehalfby](#BKMK_lk_msdyn_flow_approvalrequest_modifiedonbehalfby)
- [msdyn_flow_approvalrelationship_approvalrequests](#BKMK_msdyn_flow_approvalrelationship_approvalrequests)
- [msdyn_flow_approvalrequestrelationship_reassignment](#BKMK_msdyn_flow_approvalrequestrelationship_reassignment-many-to-one)
- [owner_msdyn_flow_approvalrequest](#BKMK_owner_msdyn_flow_approvalrequest)
- [team_msdyn_flow_approvalrequest](#BKMK_team_msdyn_flow_approvalrequest)
- [user_msdyn_flow_approvalrequest](#BKMK_user_msdyn_flow_approvalrequest)

### <a name="BKMK_business_unit_msdyn_flow_approvalrequest"></a> business_unit_msdyn_flow_approvalrequest

One-To-Many Relationship: [businessunit business_unit_msdyn_flow_approvalrequest](businessunit.md#BKMK_business_unit_msdyn_flow_approvalrequest)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalrequest_createdby"></a> lk_msdyn_flow_approvalrequest_createdby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalrequest_createdby](systemuser.md#BKMK_lk_msdyn_flow_approvalrequest_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalrequest_createdonbehalfby"></a> lk_msdyn_flow_approvalrequest_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalrequest_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approvalrequest_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalrequest_modifiedby"></a> lk_msdyn_flow_approvalrequest_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalrequest_modifiedby](systemuser.md#BKMK_lk_msdyn_flow_approvalrequest_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approvalrequest_modifiedonbehalfby"></a> lk_msdyn_flow_approvalrequest_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approvalrequest_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approvalrequest_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrelationship_approvalrequests"></a> msdyn_flow_approvalrelationship_approvalrequests

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approvalrelationship_approvalrequests](msdyn_flow_approval.md#BKMK_msdyn_flow_approvalrelationship_approvalrequests)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`msdyn_flow_approvalrequest_approval`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalrequest_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequestrelationship_reassignment-many-to-one"></a> msdyn_flow_approvalrequestrelationship_reassignment

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequestrelationship_reassignment](#BKMK_msdyn_flow_approvalrequestrelationship_reassignment-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`msdyn_flow_approvalrequest_reassignedfrom`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approvalrequest_reassignedfrom`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_flow_approvalrequest"></a> owner_msdyn_flow_approvalrequest

One-To-Many Relationship: [owner owner_msdyn_flow_approvalrequest](owner.md#BKMK_owner_msdyn_flow_approvalrequest)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_flow_approvalrequest"></a> team_msdyn_flow_approvalrequest

One-To-Many Relationship: [team team_msdyn_flow_approvalrequest](team.md#BKMK_team_msdyn_flow_approvalrequest)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_flow_approvalrequest"></a> user_msdyn_flow_approvalrequest

One-To-Many Relationship: [systemuser user_msdyn_flow_approvalrequest](systemuser.md#BKMK_user_msdyn_flow_approvalrequest)

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

- [msdyn_flow_approvalrequest_AsyncOperations](#BKMK_msdyn_flow_approvalrequest_AsyncOperations)
- [msdyn_flow_approvalrequest_BulkDeleteFailures](#BKMK_msdyn_flow_approvalrequest_BulkDeleteFailures)
- [msdyn_flow_approvalrequest_DuplicateBaseRecord](#BKMK_msdyn_flow_approvalrequest_DuplicateBaseRecord)
- [msdyn_flow_approvalrequest_DuplicateMatchingRecord](#BKMK_msdyn_flow_approvalrequest_DuplicateMatchingRecord)
- [msdyn_flow_approvalrequest_MailboxTrackingFolders](#BKMK_msdyn_flow_approvalrequest_MailboxTrackingFolders)
- [msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approvalrequest_ProcessSession](#BKMK_msdyn_flow_approvalrequest_ProcessSession)
- [msdyn_flow_approvalrequest_SyncErrors](#BKMK_msdyn_flow_approvalrequest_SyncErrors)
- [msdyn_flow_approvalrequestrelationship_reassignment](#BKMK_msdyn_flow_approvalrequestrelationship_reassignment-one-to-many)

### <a name="BKMK_msdyn_flow_approvalrequest_AsyncOperations"></a> msdyn_flow_approvalrequest_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_flow_approvalrequest_AsyncOperations](asyncoperation.md#BKMK_msdyn_flow_approvalrequest_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequest_BulkDeleteFailures"></a> msdyn_flow_approvalrequest_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_flow_approvalrequest_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_flow_approvalrequest_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequest_DuplicateBaseRecord"></a> msdyn_flow_approvalrequest_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approvalrequest_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_flow_approvalrequest_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequest_DuplicateMatchingRecord"></a> msdyn_flow_approvalrequest_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approvalrequest_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_flow_approvalrequest_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequest_MailboxTrackingFolders"></a> msdyn_flow_approvalrequest_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_flow_approvalrequest_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_flow_approvalrequest_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequest_ProcessSession"></a> msdyn_flow_approvalrequest_ProcessSession

Many-To-One Relationship: [processsession msdyn_flow_approvalrequest_ProcessSession](processsession.md#BKMK_msdyn_flow_approvalrequest_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequest_SyncErrors"></a> msdyn_flow_approvalrequest_SyncErrors

Many-To-One Relationship: [syncerror msdyn_flow_approvalrequest_SyncErrors](syncerror.md#BKMK_msdyn_flow_approvalrequest_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequest_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrequestrelationship_reassignment-one-to-many"></a> msdyn_flow_approvalrequestrelationship_reassignment

Many-To-One Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequestrelationship_reassignment](#BKMK_msdyn_flow_approvalrequestrelationship_reassignment-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalrequest`|
|ReferencingAttribute|`msdyn_flow_approvalrequest_reassignedfrom`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrequestrelationship_reassignment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_flow_approvalrequest?displayProperty=fullName>
