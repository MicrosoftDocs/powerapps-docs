---
title: "Auditing (Audit) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Auditing (Audit) table/entity."
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

# Auditing (Audit) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Track changes to records for analysis, record keeping, and compliance.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|DeleteAuditData|<xref href="Microsoft.Dynamics.CRM.DeleteAuditData?text=DeleteAuditData Action" />|<xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest>|
|DeleteRecordChangeHistory|<xref href="Microsoft.Dynamics.CRM.DeleteRecordChangeHistory?text=DeleteRecordChangeHistory Action" />|<xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/audits(*auditid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveAttributeChangeHistory|<xref href="Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistory?text=RetrieveAttributeChangeHistory Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest>|
|RetrieveAuditDetails|<xref href="Microsoft.Dynamics.CRM.RetrieveAuditDetails?text=RetrieveAuditDetails Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest>|
|RetrieveAuditPartitionList|<xref href="Microsoft.Dynamics.CRM.RetrieveAuditPartitionList?text=RetrieveAuditPartitionList Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditPartitionListRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/audits<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveRecordChangeHistory|<xref href="Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=RetrieveRecordChangeHistory Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Audit|
|DisplayCollectionName|Audits|
|DisplayName|Auditing|
|EntitySetName|audits|
|IsBPFEntity|False|
|LogicalCollectionName|audits|
|LogicalName|audit|
|OwnershipType|None|
|PrimaryIdAttribute|auditid|
|PrimaryNameAttribute||
|SchemaName|Audit|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [UserAdditionalInfo](#BKMK_UserAdditionalInfo)


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the record is associated.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UserAdditionalInfo"></a> UserAdditionalInfo

|Property|Value|
|--------|-----|
|Description|Additional information associated to the user who caused the change.|
|DisplayName|User Info|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|useradditionalinfo|
|MaxLength|350|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [Action](#BKMK_Action)
- [AttributeMask](#BKMK_AttributeMask)
- [AuditId](#BKMK_AuditId)
- [CallingUserId](#BKMK_CallingUserId)
- [CallingUserIdName](#BKMK_CallingUserIdName)
- [ChangeData](#BKMK_ChangeData)
- [CreatedOn](#BKMK_CreatedOn)
- [ObjectId](#BKMK_ObjectId)
- [ObjectIdName](#BKMK_ObjectIdName)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [Operation](#BKMK_Operation)
- [TransactionId](#BKMK_TransactionId)
- [UserId](#BKMK_UserId)
- [UserIdName](#BKMK_UserIdName)


### <a name="BKMK_Action"></a> Action

|Property|Value|
|--------|-----|
|Description|Actions the user can perform that cause a change|
|DisplayName|Event|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|action|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### Action Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Unknown||
|1|Create||
|2|Update||
|3|Delete||
|4|Activate||
|5|Deactivate||
|11|Cascade||
|12|Merge||
|13|Assign||
|14|Share||
|15|Retrieve||
|16|Close||
|17|Cancel||
|18|Complete||
|20|Resolve||
|21|Reopen||
|22|Fulfill||
|23|Paid||
|24|Qualify||
|25|Disqualify||
|26|Submit||
|27|Reject||
|28|Approve||
|29|Invoice||
|30|Hold||
|31|Add Member||
|32|Remove Member||
|33|Associate Entities||
|34|Disassociate Entities||
|35|Add Members||
|36|Remove Members||
|37|Add Item||
|38|Remove Item||
|39|Add Substitute||
|40|Remove Substitute||
|41|Set State||
|42|Renew||
|43|Revise||
|44|Win||
|45|Lose||
|46|Internal Processing||
|47|Reschedule||
|48|Modify Share||
|49|Unshare||
|50|Book||
|51|Generate Quote From Opportunity||
|52|Add To Queue||
|53|Assign Role To Team||
|54|Remove Role From Team||
|55|Assign Role To User||
|56|Remove Role From User||
|57|Add Privileges to Role||
|58|Remove Privileges From Role||
|59|Replace Privileges In Role||
|60|Import Mappings||
|61|Clone||
|62|Send Direct Email||
|63|Enabled for organization||
|64|User Access via Web||
|65|User Access via Web Services||
|100|Delete Entity||
|101|Delete Attribute||
|102|Audit Change at Entity Level||
|103|Audit Change at Attribute Level||
|104|Audit Change at Org Level||
|105|Entity Audit Started||
|106|Attribute Audit Started||
|107|Audit Enabled||
|108|Entity Audit Stopped||
|109|Attribute Audit Stopped||
|110|Audit Disabled||
|111|Audit Log Deletion||
|112|User Access Audit Started||
|113|User Access Audit Stopped||



### <a name="BKMK_AttributeMask"></a> AttributeMask

|Property|Value|
|--------|-----|
|Description|Contains a CSV of the ColumnNumber metadata property of attributes|
|DisplayName|Changed Field|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attributemask|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_AuditId"></a> AuditId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the auditing instance|
|DisplayName|Record Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|auditid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CallingUserId"></a> CallingUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the calling user in case of an impersonated call|
|DisplayName|Calling User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|callinguserid|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CallingUserIdName"></a> CallingUserIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|callinguseridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ChangeData"></a> ChangeData

|Property|Value|
|--------|-----|
|Description|Contains a CSV of old values of all the attributes whose IsAuditEnabled property is True and are being changed|
|DisplayName|Change Data|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|changedata|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the audit record was created.|
|DisplayName|Changed Date|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the record that is being audited|
|DisplayName|Record|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|SystemRequired|
|Targets||
|Type|Lookup|


### <a name="BKMK_ObjectIdName"></a> ObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectidname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Unique identifier of the entity that is being audited|
|DisplayName|Entity|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|--------|-----|
|Description|The action that causes the audit--it will be create, delete, or update|
|DisplayName|Operation|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|operation|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Operation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Create||
|2|Update||
|3|Delete||
|4|Access||



### <a name="BKMK_TransactionId"></a> TransactionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for multiple changes that are part of a single operation; this field contains the same GUID for all the audit rows generated in a single transaction|
|DisplayName|Transaction Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_UserId"></a> UserId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who caused a change|
|DisplayName|Changed By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|userid|
|RequiredLevel|SystemRequired|
|Targets|externalparty,systemuser|
|Type|Lookup|


### <a name="BKMK_UserIdName"></a> UserIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|useridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_audit_userid](#BKMK_lk_audit_userid)
- [lk_audit_callinguserid](#BKMK_lk_audit_callinguserid)


### <a name="BKMK_lk_audit_userid"></a> lk_audit_userid

See systemuser Table [lk_audit_userid](systemuser.md#BKMK_lk_audit_userid) One-To-Many relationship.

### <a name="BKMK_lk_audit_callinguserid"></a> lk_audit_callinguserid

See systemuser Table [lk_audit_callinguserid](systemuser.md#BKMK_lk_audit_callinguserid) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.audit?text=audit EntityType" />