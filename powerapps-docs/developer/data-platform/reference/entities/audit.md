---
title: "Auditing (Audit) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Auditing (Audit) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Auditing (Audit) table/entity reference (Microsoft Dataverse)

Track changes to records for analysis, record keeping, and compliance.

## Messages

The following table lists the messages for the Auditing (Audit) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `DeleteAuditData`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteAuditData?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest>|
| `DeleteRecordChangeHistory`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteRecordChangeHistory?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryRequest>|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /audits(*auditid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveAttributeChangeHistory`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistory?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest>|
| `RetrieveAuditDetails`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest>|
| `RetrieveAuditPartitionList`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveAuditPartitionList?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditPartitionListRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /audits<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveRecordChangeHistory`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest>|

## Properties

The following table lists selected properties for the Auditing (Audit) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Auditing** |
| **DisplayCollectionName** | **Audits** |
| **SchemaName** | `Audit` |
| **CollectionSchemaName** | `Audit` |
| **EntitySetName** | `audits`|
| **LogicalName** | `audit` |
| **LogicalCollectionName** | `audits` |
| **PrimaryIdAttribute** | `auditid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdditionalInfo](#BKMK_AdditionalInfo)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [UserAdditionalInfo](#BKMK_UserAdditionalInfo)

### <a name="BKMK_AdditionalInfo"></a> AdditionalInfo

|Property|Value|
|---|---|
|Description|**Additional Info for Audit**|
|DisplayName|**Additional Info**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`additionalinfo`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the record is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_UserAdditionalInfo"></a> UserAdditionalInfo

|Property|Value|
|---|---|
|Description|**Additional information associated to the user who caused the change.**|
|DisplayName|**User Info**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`useradditionalinfo`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|350|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Action](#BKMK_Action)
- [AttributeMask](#BKMK_AttributeMask)
- [AuditId](#BKMK_AuditId)
- [CallingUserId](#BKMK_CallingUserId)
- [ChangeData](#BKMK_ChangeData)
- [CreatedOn](#BKMK_CreatedOn)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [Operation](#BKMK_Operation)
- [TimeToLiveInSeconds](#BKMK_TimeToLiveInSeconds)
- [TransactionId](#BKMK_TransactionId)
- [UserId](#BKMK_UserId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_Action"></a> Action

|Property|Value|
|---|---|
|Description|**Actions the user can perform that cause a change**|
|DisplayName|**Event**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`action`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`audit_action`|

#### Action Choices/Options

|Value|Label|
|---|---|
|0|**Unknown**|
|1|**Create**|
|2|**Update**|
|3|**Delete**|
|4|**Activate**|
|5|**Deactivate**|
|6|**Upsert**|
|11|**Cascade**|
|12|**Merge**|
|13|**Assign**|
|14|**Share**|
|15|**Retrieve**|
|16|**Close**|
|17|**Cancel**|
|18|**Complete**|
|20|**Resolve**|
|21|**Reopen**|
|22|**Fulfill**|
|23|**Paid**|
|24|**Qualify**|
|25|**Disqualify**|
|26|**Submit**|
|27|**Reject**|
|28|**Approve**|
|29|**Invoice**|
|30|**Hold**|
|31|**Add Member**|
|32|**Remove Member**|
|33|**Associate Entities**|
|34|**Disassociate Entities**|
|35|**Add Members**|
|36|**Remove Members**|
|37|**Add Item**|
|38|**Remove Item**|
|39|**Add Substitute**|
|40|**Remove Substitute**|
|41|**Set State**|
|42|**Renew**|
|43|**Revise**|
|44|**Win**|
|45|**Lose**|
|46|**Internal Processing**|
|47|**Reschedule**|
|48|**Modify Share**|
|49|**Unshare**|
|50|**Book**|
|51|**Generate Quote From Opportunity**|
|52|**Add To Queue**|
|53|**Assign Role To Team**|
|54|**Remove Role From Team**|
|55|**Assign Role To User**|
|56|**Remove Role From User**|
|57|**Add Privileges to Role**|
|58|**Remove Privileges From Role**|
|59|**Replace Privileges In Role**|
|60|**Import Mappings**|
|61|**Clone**|
|62|**Send Direct Email**|
|63|**Enabled for organization**|
|64|**User Access via Web**|
|65|**User Access via Web Services**|
|100|**Delete Entity**|
|101|**Delete Attribute**|
|102|**Audit Change at Entity Level**|
|103|**Audit Change at Attribute Level**|
|104|**Audit Change at Org Level**|
|105|**Entity Audit Started**|
|106|**Attribute Audit Started**|
|107|**Audit Enabled**|
|108|**Entity Audit Stopped**|
|109|**Attribute Audit Stopped**|
|110|**Audit Disabled**|
|111|**Audit Log Deletion**|
|112|**User Access Audit Started**|
|113|**User Access Audit Stopped**|
|115|**Archive**|
|116|**Retain**|
|117|**RollbackRetain**|
|118|**IPFirewallAcccesDenied**|
|119|**IPFirewallAcccesAllowed**|
|120|**Restore**|
|121|**ApplicationBasedAccessDenied**|
|122|**ApplicationBasedAccessAllowed**|
|123|**Create - AI assisted**|
|124|**Update - AI assisted**|
|125|**Read Unmasked**|

### <a name="BKMK_AttributeMask"></a> AttributeMask

|Property|Value|
|---|---|
|Description|**Contains a CSV of the ColumnNumber metadata property of attributes**|
|DisplayName|**Changed Field**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributemask`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_AuditId"></a> AuditId

|Property|Value|
|---|---|
|Description|**Unique identifier of the auditing instance**|
|DisplayName|**Record Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`auditid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CallingUserId"></a> CallingUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the calling user in case of an impersonated call**|
|DisplayName|**Calling User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`callinguserid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ChangeData"></a> ChangeData

|Property|Value|
|---|---|
|Description|**For given audit action, contains a string value describing the change details when corresponding IsAuditEnabled property is True**|
|DisplayName|**Change Data**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`changedata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the audit record was created.**|
|DisplayName|**Changed Date**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the record that is being audited**|
|DisplayName|**Record**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets||

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity that is being audited**|
|DisplayName|**Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|---|---|
|Description|**The action that causes the audit--it will be create, delete, update, upsert or archive**|
|DisplayName|**Operation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`operation`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`audit_operation`|

#### Operation Choices/Options

|Value|Label|
|---|---|
|1|**Create**|
|2|**Update**|
|3|**Delete**|
|4|**Access**|
|5|**Upsert**|
|115|**Archive**|
|116|**Retain**|
|117|**RollbackRetain**|
|118|**Restore**|
|200|**CustomOperation**|

### <a name="BKMK_TimeToLiveInSeconds"></a> TimeToLiveInSeconds

|Property|Value|
|---|---|
|Description|**Time to live in seconds for audit record**|
|DisplayName|**Time To Live In Seconds**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timetoliveinseconds`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_TransactionId"></a> TransactionId

|Property|Value|
|---|---|
|Description|**Unique identifier for multiple changes that are part of a single operation; this field contains the same GUID for all the audit rows generated in a single transaction**|
|DisplayName|**Transaction Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`transactionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_UserId"></a> UserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who caused a change**|
|DisplayName|**Changed By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`userid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|externalparty, systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the audit.**|
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

- [lk_audit_callinguserid](#BKMK_lk_audit_callinguserid)
- [lk_audit_userid](#BKMK_lk_audit_userid)

### <a name="BKMK_lk_audit_callinguserid"></a> lk_audit_callinguserid

One-To-Many Relationship: [systemuser lk_audit_callinguserid](systemuser.md#BKMK_lk_audit_callinguserid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`callinguserid`|
|ReferencingEntityNavigationPropertyName|`callinguserid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_audit_userid"></a> lk_audit_userid

One-To-Many Relationship: [systemuser lk_audit_userid](systemuser.md#BKMK_lk_audit_userid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`userid`|
|ReferencingEntityNavigationPropertyName|`userid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.audit?displayProperty=fullName>
