---
title: "Approval (msdyn_flow_approval) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Approval (msdyn_flow_approval) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Approval (msdyn_flow_approval) table/entity reference (Microsoft Dataverse)

An approval.

## Messages

The following table lists the messages for the Approval (msdyn_flow_approval) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_flow_approvals(*msdyn_flow_approvalid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_flow_approvals<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_flow_approvals(*msdyn_flow_approvalid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_flow_approvals(*msdyn_flow_approvalid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_flow_approvals<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_flow_approvals(*msdyn_flow_approvalid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_flow_approvals(*msdyn_flow_approvalid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_flow_approvals(*msdyn_flow_approvalid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Approval (msdyn_flow_approval) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Approval** |
| **DisplayCollectionName** | **Approvals** |
| **SchemaName** | `msdyn_flow_approval` |
| **CollectionSchemaName** | `msdyn_flow_approvals` |
| **EntitySetName** | `msdyn_flow_approvals`|
| **LogicalName** | `msdyn_flow_approval` |
| **LogicalCollectionName** | `msdyn_flow_approvals` |
| **PrimaryIdAttribute** | `msdyn_flow_approvalid` |
| **PrimaryNameAttribute** |`msdyn_flow_approval_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CurrentStage](#BKMK_CurrentStage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_flow_approval_additionalfields](#BKMK_msdyn_flow_approval_additionalfields)
- [msdyn_flow_approval_allowreassign](#BKMK_msdyn_flow_approval_allowreassign)
- [msdyn_flow_approval_approvalstagekey](#BKMK_msdyn_flow_approval_approvalstagekey)
- [msdyn_flow_approval_basicapprovalmodel](#BKMK_msdyn_flow_approval_basicapprovalmodel)
- [msdyn_flow_approval_category](#BKMK_msdyn_flow_approval_category)
- [msdyn_flow_approval_completedon](#BKMK_msdyn_flow_approval_completedon)
- [msdyn_flow_approval_currentstepnumber](#BKMK_msdyn_flow_approval_currentstepnumber)
- [msdyn_flow_approval_details](#BKMK_msdyn_flow_approval_details)
- [msdyn_flow_approval_dueon](#BKMK_msdyn_flow_approval_dueon)
- [msdyn_flow_approval_expireson](#BKMK_msdyn_flow_approval_expireson)
- [msdyn_flow_approval_itemlink](#BKMK_msdyn_flow_approval_itemlink)
- [msdyn_flow_approval_itemlinkdescription](#BKMK_msdyn_flow_approval_itemlinkdescription)
- [msdyn_flow_approval_itemlinkhash](#BKMK_msdyn_flow_approval_itemlinkhash)
- [msdyn_flow_approval_modelid](#BKMK_msdyn_flow_approval_modelid)
- [msdyn_flow_approval_modeltype](#BKMK_msdyn_flow_approval_modeltype)
- [msdyn_flow_approval_name](#BKMK_msdyn_flow_approval_name)
- [msdyn_flow_approval_partneridhash](#BKMK_msdyn_flow_approval_partneridhash)
- [msdyn_flow_approval_partnermetadata](#BKMK_msdyn_flow_approval_partnermetadata)
- [msdyn_flow_approval_priority](#BKMK_msdyn_flow_approval_priority)
- [msdyn_flow_approval_requesttype](#BKMK_msdyn_flow_approval_requesttype)
- [msdyn_flow_approval_result](#BKMK_msdyn_flow_approval_result)
- [msdyn_flow_approval_sendemail](#BKMK_msdyn_flow_approval_sendemail)
- [msdyn_flow_approval_source](#BKMK_msdyn_flow_approval_source)
- [msdyn_flow_approval_stage](#BKMK_msdyn_flow_approval_stage)
- [msdyn_flow_approval_tags](#BKMK_msdyn_flow_approval_tags)
- [msdyn_flow_approval_templateformid](#BKMK_msdyn_flow_approval_templateformid)
- [msdyn_flow_approval_templateid](#BKMK_msdyn_flow_approval_templateid)
- [msdyn_flow_approval_templateresponseId](#BKMK_msdyn_flow_approval_templateresponseId)
- [msdyn_flow_approval_title](#BKMK_msdyn_flow_approval_title)
- [msdyn_flow_approvalId](#BKMK_msdyn_flow_approvalId)
- [new_msdyn_flow_approval_allowcancel](#BKMK_new_msdyn_flow_approval_allowcancel)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ProcessId](#BKMK_ProcessId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_CurrentStage"></a> CurrentStage

|Property|Value|
|---|---|
|Description|**The link to the current stage of the multi stage approvals**|
|DisplayName|**Current Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`currentstage`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|approvalstageorder|

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

### <a name="BKMK_msdyn_flow_approval_additionalfields"></a> msdyn_flow_approval_additionalfields

|Property|Value|
|---|---|
|Description||
|DisplayName|**Additional Fields**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_additionalfields`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_flow_approval_allowreassign"></a> msdyn_flow_approval_allowreassign

|Property|Value|
|---|---|
|Description|**Boolean field that allows the approvers to reassign approval requests.**|
|DisplayName|**Allow Reassign**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_allowreassign`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_flow_approval_msdyn_flow_approval_allowreassign`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_flow_approval_approvalstagekey"></a> msdyn_flow_approval_approvalstagekey

|Property|Value|
|---|---|
|Description|**Lookup key to match approval id and stage in fetch xml.**|
|DisplayName|**Approval Stage Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_approvalstagekey`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approval_basicapprovalmodel"></a> msdyn_flow_approval_basicapprovalmodel

|Property|Value|
|---|---|
|Description|**The linked basic approval model data.**|
|DisplayName|**Basic Approval Model**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_basicapprovalmodel`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_flow_basicapprovalmodel|

### <a name="BKMK_msdyn_flow_approval_category"></a> msdyn_flow_approval_category

|Property|Value|
|---|---|
|Description|**User defined string that allows approval creators to categorize an approval.**|
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_category`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_msdyn_flow_approval_completedon"></a> msdyn_flow_approval_completedon

|Property|Value|
|---|---|
|Description|**The completion date.**|
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_flow_approval_currentstepnumber"></a> msdyn_flow_approval_currentstepnumber

|Property|Value|
|---|---|
|Description||
|DisplayName|**Current Step Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_currentstepnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_flow_approval_details"></a> msdyn_flow_approval_details

|Property|Value|
|---|---|
|Description|**The description of the approval.**|
|DisplayName|**Details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_details`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32768|

### <a name="BKMK_msdyn_flow_approval_dueon"></a> msdyn_flow_approval_dueon

|Property|Value|
|---|---|
|Description|**The due date.**|
|DisplayName|**Due On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_dueon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_flow_approval_expireson"></a> msdyn_flow_approval_expireson

|Property|Value|
|---|---|
|Description|**The expiration date.**|
|DisplayName|**Expires On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_expireson`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_flow_approval_itemlink"></a> msdyn_flow_approval_itemlink

|Property|Value|
|---|---|
|Description|**The optional link to the item to approve.**|
|DisplayName|**Item Link**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_itemlink`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_msdyn_flow_approval_itemlinkdescription"></a> msdyn_flow_approval_itemlinkdescription

|Property|Value|
|---|---|
|Description|**The optional description for the item link.**|
|DisplayName|**Item Link Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_itemlinkdescription`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_msdyn_flow_approval_itemlinkhash"></a> msdyn_flow_approval_itemlinkhash

|Property|Value|
|---|---|
|Description|**Item link hash to enable queries.**|
|DisplayName|**Item Link Hash**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_itemlinkhash`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approval_modelid"></a> msdyn_flow_approval_modelid

|Property|Value|
|---|---|
|Description|**Id of the approval model.**|
|DisplayName|**Approval Model Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_modelid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approval_modeltype"></a> msdyn_flow_approval_modeltype

|Property|Value|
|---|---|
|Description|**Table name of the approval model.**|
|DisplayName|**Approval Model Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_modeltype`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approval_name"></a> msdyn_flow_approval_name

|Property|Value|
|---|---|
|Description|**The name of the approval.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approval_partneridhash"></a> msdyn_flow_approval_partneridhash

|Property|Value|
|---|---|
|Description|**The hash of a unique partner id associated with a document. Meant for search scenarios.**|
|DisplayName|**Partner Id Hash**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_partneridhash`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_msdyn_flow_approval_partnermetadata"></a> msdyn_flow_approval_partnermetadata

|Property|Value|
|---|---|
|Description|**Unstructured space to store extraneous information associated with the approval for partner services.**|
|DisplayName|**Partner Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_partnermetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_flow_approval_priority"></a> msdyn_flow_approval_priority

|Property|Value|
|---|---|
|Description|**The priority of the approval.**|
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_priority`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|192350002|
|GlobalChoiceName|`msdyn_flow_approval_priority`|

#### msdyn_flow_approval_priority Choices/Options

|Value|Label|
|---|---|
|192350000|**Urgent**|
|192350001|**Important**|
|192350002|**Medium**|
|192350003|**Low**|

### <a name="BKMK_msdyn_flow_approval_requesttype"></a> msdyn_flow_approval_requesttype

|Property|Value|
|---|---|
|Description|**The type of request that created the approval whether from an approval template, esignature process, etc.**|
|DisplayName|**Request Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_requesttype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|192350001|
|GlobalChoiceName|`msdyn_flow_approval_requesttype`|

#### msdyn_flow_approval_requesttype Choices/Options

|Value|Label|
|---|---|
|192350000|**Other**|
|192350001|**Basic**|
|192350002|**eSign**|
|192350003|**Templates**|

### <a name="BKMK_msdyn_flow_approval_result"></a> msdyn_flow_approval_result

|Property|Value|
|---|---|
|Description|**Final outcome of the approval.**|
|DisplayName|**Result**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_result`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_flow_approval_sendemail"></a> msdyn_flow_approval_sendemail

|Property|Value|
|---|---|
|Description|**Whether to send system-generated email notifications for this approval.**|
|DisplayName|**Send Email Notification**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_sendemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_flow_approval_msdyn_flow_approval_sendemail`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_flow_approval_source"></a> msdyn_flow_approval_source

|Property|Value|
|---|---|
|Description|**Source of the request that created the approval.**|
|DisplayName|**Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_source`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_msdyn_flow_approval_stage"></a> msdyn_flow_approval_stage

|Property|Value|
|---|---|
|Description|**The stage.**|
|DisplayName|**Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_stage`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_flow_approvalstage`|

#### msdyn_flow_approval_stage Choices/Options

|Value|Label|
|---|---|
|192350000|**Not Specified**|
|192350001|**Basic**|
|192351000|**Complete**|

### <a name="BKMK_msdyn_flow_approval_tags"></a> msdyn_flow_approval_tags

|Property|Value|
|---|---|
|Description|**Semicolon delimited list of user defined strings to help filter and search approvals.**|
|DisplayName|**Tags**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_tags`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_flow_approval_templateformid"></a> msdyn_flow_approval_templateformid

|Property|Value|
|---|---|
|Description|**Base64 encoded string id of the template approval form.**|
|DisplayName|**Template Form Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_templateformid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_flow_approval_templateid"></a> msdyn_flow_approval_templateid

|Property|Value|
|---|---|
|Description|**Base64 encoded string id of the template used to create the approval.**|
|DisplayName|**Template Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_templateid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_flow_approval_templateresponseId"></a> msdyn_flow_approval_templateresponseId

|Property|Value|
|---|---|
|Description|**Base64 encoded string id of the unique templated approval response.**|
|DisplayName|**Template Response Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_templateresponseid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|36|

### <a name="BKMK_msdyn_flow_approval_title"></a> msdyn_flow_approval_title

|Property|Value|
|---|---|
|Description|**The title.**|
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_title`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_msdyn_flow_approvalId"></a> msdyn_flow_approvalId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Approval**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approvalid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_new_msdyn_flow_approval_allowcancel"></a> new_msdyn_flow_approval_allowcancel

|Property|Value|
|---|---|
|Description|**Boolean field that allows the approval owner to cancel the approval.**|
|DisplayName|**Allow Cancel**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_flow_approval_allowcancel`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_flow_approval_new_msdyn_flow_approval_allowcancel`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**The id of the approval process from which the approval is created**|
|DisplayName|**Process Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processid`|
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
|Description|**Status of the Approval**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approval_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 192350000<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 192350004<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**The reason for the status of the approval.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|ApplicationRequired|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_flow_approval_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|192350000|Label: **Created**<br />State:0<br />TransitionData: None|
|192350001|Label: **Pending**<br />State:0<br />TransitionData: None|
|192350002|Label: **Suspended**<br />State:0<br />TransitionData: None|
|192350004|Label: **Completed**<br />State:1<br />TransitionData: None|
|192350005|Label: **Expired**<br />State:1<br />TransitionData: None|
|192350006|Label: **Canceled**<br />State:1<br />TransitionData: None|
|192350007|Label: **Abandoned**<br />State:1<br />TransitionData: None|

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

- [business_unit_msdyn_flow_approval](#BKMK_business_unit_msdyn_flow_approval)
- [lk_msdyn_flow_approval_createdby](#BKMK_lk_msdyn_flow_approval_createdby)
- [lk_msdyn_flow_approval_createdonbehalfby](#BKMK_lk_msdyn_flow_approval_createdonbehalfby)
- [lk_msdyn_flow_approval_modifiedby](#BKMK_lk_msdyn_flow_approval_modifiedby)
- [lk_msdyn_flow_approval_modifiedonbehalfby](#BKMK_lk_msdyn_flow_approval_modifiedonbehalfby)
- [msdyn_flow_approval_currentstage_approvalstageorder](#BKMK_msdyn_flow_approval_currentstage_approvalstageorder)
- [msdyn_flow_basicapprovalmodelrelationship_approval](#BKMK_msdyn_flow_basicapprovalmodelrelationship_approval)
- [owner_msdyn_flow_approval](#BKMK_owner_msdyn_flow_approval)
- [team_msdyn_flow_approval](#BKMK_team_msdyn_flow_approval)
- [user_msdyn_flow_approval](#BKMK_user_msdyn_flow_approval)

### <a name="BKMK_business_unit_msdyn_flow_approval"></a> business_unit_msdyn_flow_approval

One-To-Many Relationship: [businessunit business_unit_msdyn_flow_approval](businessunit.md#BKMK_business_unit_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approval_createdby"></a> lk_msdyn_flow_approval_createdby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approval_createdby](systemuser.md#BKMK_lk_msdyn_flow_approval_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approval_createdonbehalfby"></a> lk_msdyn_flow_approval_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approval_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approval_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approval_modifiedby"></a> lk_msdyn_flow_approval_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approval_modifiedby](systemuser.md#BKMK_lk_msdyn_flow_approval_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_flow_approval_modifiedonbehalfby"></a> lk_msdyn_flow_approval_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_flow_approval_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_flow_approval_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_currentstage_approvalstageorder"></a> msdyn_flow_approval_currentstage_approvalstageorder

One-To-Many Relationship: [approvalstageorder msdyn_flow_approval_currentstage_approvalstageorder](approvalstageorder.md#BKMK_msdyn_flow_approval_currentstage_approvalstageorder)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`currentstage`|
|ReferencingEntityNavigationPropertyName|`currentstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodelrelationship_approval"></a> msdyn_flow_basicapprovalmodelrelationship_approval

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodelrelationship_approval](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodelrelationship_approval)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`msdyn_flow_approval_basicapprovalmodel`|
|ReferencingEntityNavigationPropertyName|`msdyn_flow_approval_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_flow_approval"></a> owner_msdyn_flow_approval

One-To-Many Relationship: [owner owner_msdyn_flow_approval](owner.md#BKMK_owner_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_flow_approval"></a> team_msdyn_flow_approval

One-To-Many Relationship: [team team_msdyn_flow_approval](team.md#BKMK_team_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_flow_approval"></a> user_msdyn_flow_approval

One-To-Many Relationship: [systemuser user_msdyn_flow_approval](systemuser.md#BKMK_user_msdyn_flow_approval)

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

- [approvalstageapproval_approval_msdyn_flow_approval](#BKMK_approvalstageapproval_approval_msdyn_flow_approval)
- [approvalstagecondition_approval_msdyn_flow_approval](#BKMK_approvalstagecondition_approval_msdyn_flow_approval)
- [approvalstageintelligent_approval_msdyn_flow_approval](#BKMK_approvalstageintelligent_approval_msdyn_flow_approval)
- [approvalstageorder_approval_msdyn_flow_approval](#BKMK_approvalstageorder_approval_msdyn_flow_approval)
- [msdyn_flow_approval_Annotations](#BKMK_msdyn_flow_approval_Annotations)
- [msdyn_flow_approval_AsyncOperations](#BKMK_msdyn_flow_approval_AsyncOperations)
- [msdyn_flow_approval_BulkDeleteFailures](#BKMK_msdyn_flow_approval_BulkDeleteFailures)
- [msdyn_flow_approval_DuplicateBaseRecord](#BKMK_msdyn_flow_approval_DuplicateBaseRecord)
- [msdyn_flow_approval_DuplicateMatchingRecord](#BKMK_msdyn_flow_approval_DuplicateMatchingRecord)
- [msdyn_flow_approval_MailboxTrackingFolders](#BKMK_msdyn_flow_approval_MailboxTrackingFolders)
- [msdyn_flow_approval_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approval_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approval_ProcessSession](#BKMK_msdyn_flow_approval_ProcessSession)
- [msdyn_flow_approval_SyncErrors](#BKMK_msdyn_flow_approval_SyncErrors)
- [msdyn_flow_approvalrelationship_approvalrequests](#BKMK_msdyn_flow_approvalrelationship_approvalrequests)
- [msdyn_flow_approvalrelationship_approvalresponses](#BKMK_msdyn_flow_approvalrelationship_approvalresponses)
- [msdyn_flow_approvalrelationship_approvalsteps](#BKMK_msdyn_flow_approvalrelationship_approvalsteps)
- [msdyn_flow_approvalrelationship_flowapprovals](#BKMK_msdyn_flow_approvalrelationship_flowapprovals)

### <a name="BKMK_approvalstageapproval_approval_msdyn_flow_approval"></a> approvalstageapproval_approval_msdyn_flow_approval

Many-To-One Relationship: [approvalstageapproval approvalstageapproval_approval_msdyn_flow_approval](approvalstageapproval.md#BKMK_approvalstageapproval_approval_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageapproval`|
|ReferencingAttribute|`approval`|
|ReferencedEntityNavigationPropertyName|`approvalstageapproval_approval_msdyn_flow_approval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstagecondition_approval_msdyn_flow_approval"></a> approvalstagecondition_approval_msdyn_flow_approval

Many-To-One Relationship: [approvalstagecondition approvalstagecondition_approval_msdyn_flow_approval](approvalstagecondition.md#BKMK_approvalstagecondition_approval_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstagecondition`|
|ReferencingAttribute|`approval`|
|ReferencedEntityNavigationPropertyName|`approvalstagecondition_approval_msdyn_flow_approval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageintelligent_approval_msdyn_flow_approval"></a> approvalstageintelligent_approval_msdyn_flow_approval

Many-To-One Relationship: [approvalstageintelligent approvalstageintelligent_approval_msdyn_flow_approval](approvalstageintelligent.md#BKMK_approvalstageintelligent_approval_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageintelligent`|
|ReferencingAttribute|`approval`|
|ReferencedEntityNavigationPropertyName|`approvalstageintelligent_approval_msdyn_flow_approval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_approval_msdyn_flow_approval"></a> approvalstageorder_approval_msdyn_flow_approval

Many-To-One Relationship: [approvalstageorder approvalstageorder_approval_msdyn_flow_approval](approvalstageorder.md#BKMK_approvalstageorder_approval_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageorder`|
|ReferencingAttribute|`approval`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_approval_msdyn_flow_approval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_Annotations"></a> msdyn_flow_approval_Annotations

Many-To-One Relationship: [annotation msdyn_flow_approval_Annotations](annotation.md#BKMK_msdyn_flow_approval_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_AsyncOperations"></a> msdyn_flow_approval_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_flow_approval_AsyncOperations](asyncoperation.md#BKMK_msdyn_flow_approval_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_BulkDeleteFailures"></a> msdyn_flow_approval_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_flow_approval_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_flow_approval_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_DuplicateBaseRecord"></a> msdyn_flow_approval_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approval_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_flow_approval_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_DuplicateMatchingRecord"></a> msdyn_flow_approval_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_flow_approval_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_flow_approval_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_MailboxTrackingFolders"></a> msdyn_flow_approval_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_flow_approval_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_flow_approval_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approval_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_flow_approval_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_flow_approval_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_ProcessSession"></a> msdyn_flow_approval_ProcessSession

Many-To-One Relationship: [processsession msdyn_flow_approval_ProcessSession](processsession.md#BKMK_msdyn_flow_approval_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_SyncErrors"></a> msdyn_flow_approval_SyncErrors

Many-To-One Relationship: [syncerror msdyn_flow_approval_SyncErrors](syncerror.md#BKMK_msdyn_flow_approval_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrelationship_approvalrequests"></a> msdyn_flow_approvalrelationship_approvalrequests

Many-To-One Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrelationship_approvalrequests](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrelationship_approvalrequests)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalrequest`|
|ReferencingAttribute|`msdyn_flow_approvalrequest_approval`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrelationship_approvalrequests`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrelationship_approvalresponses"></a> msdyn_flow_approvalrelationship_approvalresponses

Many-To-One Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalrelationship_approvalresponses](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalrelationship_approvalresponses)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalresponse`|
|ReferencingAttribute|`msdyn_flow_approvalresponse_approval`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrelationship_approvalresponses`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrelationship_approvalsteps"></a> msdyn_flow_approvalrelationship_approvalsteps

Many-To-One Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalrelationship_approvalsteps](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalrelationship_approvalsteps)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalstep`|
|ReferencingAttribute|`msdyn_flow_approvalstep_approval`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrelationship_approvalsteps`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approvalrelationship_flowapprovals"></a> msdyn_flow_approvalrelationship_flowapprovals

Many-To-One Relationship: [msdyn_flow_flowapproval msdyn_flow_approvalrelationship_flowapprovals](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_approvalrelationship_flowapprovals)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_flowapproval`|
|ReferencingAttribute|`msdyn_flow_flowapproval_approval`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approvalrelationship_flowapprovals`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_flow_approval?displayProperty=fullName>
