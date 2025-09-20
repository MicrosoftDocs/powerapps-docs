---
title: "Connection table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Connection table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Connection table/entity reference (Microsoft Dataverse)

Relationship between two entities.

## Messages

The following table lists the messages for the Connection table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /connections(*connectionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /connections<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /connections(*connectionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /connections(*connectionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /connections<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /connections(*connectionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /connections(*connectionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /connections(*connectionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Connection table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Connection** |
| **DisplayCollectionName** | **Connections** |
| **SchemaName** | `Connection` |
| **CollectionSchemaName** | `Connections` |
| **EntitySetName** | `connections`|
| **LogicalName** | `connection` |
| **LogicalCollectionName** | `connections` |
| **PrimaryIdAttribute** | `connectionid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConnectionId](#BKMK_ConnectionId)
- [Description](#BKMK_Description)
- [EffectiveEnd](#BKMK_EffectiveEnd)
- [EffectiveStart](#BKMK_EffectiveStart)
- [EntityImage](#BKMK_EntityImage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Record1Id](#BKMK_Record1Id)
- [Record1IdObjectTypeCode](#BKMK_Record1IdObjectTypeCode)
- [Record1RoleId](#BKMK_Record1RoleId)
- [Record2Id](#BKMK_Record2Id)
- [Record2IdObjectTypeCode](#BKMK_Record2IdObjectTypeCode)
- [Record2RoleId](#BKMK_Record2RoleId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)

### <a name="BKMK_ConnectionId"></a> ConnectionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the connection.**|
|DisplayName|**Connection**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`connectionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the connection, such as the length or quality of the relationship.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_EffectiveEnd"></a> EffectiveEnd

|Property|Value|
|---|---|
|Description|**Enter the end date of the connection.**|
|DisplayName|**Ending**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`effectiveend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_EffectiveStart"></a> EffectiveStart

|Property|Value|
|---|---|
|Description|**Enter the start date of the connection.**|
|DisplayName|**Starting**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`effectivestart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|---|---|
|Description|**The default image for the entity.**|
|DisplayName|**Entity Image**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|False|
|IsPrimaryImage|True|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
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
|Description|**Type of the owner of the connection, such as user, team, or business unit.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_Record1Id"></a> Record1Id

|Property|Value|
|---|---|
|Description|**Choose the primary account, contact, or other record involved in the connection.**|
|DisplayName|**Connected From**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`record1id`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activitypointer, adx_invitation, adx_inviteredemption, appointment, channelaccessprofilerule, contact, email, fax, goal, knowledgearticle, knowledgebaserecord, letter, mspp_publishingstatetransitionrule, mspp_shortcut, mspp_website, phonecall, position, processsession, recurringappointmentmaster, socialactivity, socialprofile, systemuser, task, team, territory|

### <a name="BKMK_Record1IdObjectTypeCode"></a> Record1IdObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`record1idobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Record1RoleId"></a> Record1RoleId

|Property|Value|
|---|---|
|Description|**Choose the primary party's role or relationship with the second party.**|
|DisplayName|**Role (From)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`record1roleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connectionrole|

### <a name="BKMK_Record2Id"></a> Record2Id

|Property|Value|
|---|---|
|Description|**Select the secondary account, contact, or other record involved in the connection.**|
|DisplayName|**Connected To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`record2id`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activitypointer, adx_invitation, adx_inviteredemption, appointment, channelaccessprofilerule, contact, email, fax, goal, knowledgearticle, knowledgebaserecord, letter, mspp_publishingstatetransitionrule, mspp_shortcut, mspp_website, phonecall, position, processsession, recurringappointmentmaster, socialactivity, socialprofile, systemuser, task, team, territory|

### <a name="BKMK_Record2IdObjectTypeCode"></a> Record2IdObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`record2idobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Record2RoleId"></a> Record2RoleId

|Property|Value|
|---|---|
|Description|**Choose the secondary party's role or relationship with the primary party.**|
|DisplayName|**Role (To)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`record2roleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connectionrole|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the connection is active or inactive. Inactive connections are read-only and can't be edited unless they are reactivated.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`connection_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the connection.**|
|DisplayName|**Status Reason**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`connection_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Choose the local currency for the record to make sure budgets are reported in the correct currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsMaster](#BKMK_IsMaster)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Name](#BKMK_Name)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Record1ObjectTypeCode](#BKMK_Record1ObjectTypeCode)
- [Record2ObjectTypeCode](#BKMK_Record2ObjectTypeCode)
- [RelatedConnectionId](#BKMK_RelatedConnectionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Entity Image Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_IsMaster"></a> IsMaster

|Property|Value|
|---|---|
|Description|**Indicates that this is the master record.**|
|DisplayName|**Is Master**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismaster`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`connection_ismaster`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
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
|Description|**Name of the connection.**|
|DisplayName|**Connection Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner of the connection.**|
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
|Description||
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
|Description|**Shows the business unit that the record owner belongs to.**|
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
|Description|**Unique identifier of the team who owns the connection.**|
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
|Description|**Unique identifier of the user who owns the connection.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Record1ObjectTypeCode"></a> Record1ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Shows the record type of the source record.**|
|DisplayName|**Type (From)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`record1objecttypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`connection_record1objecttypecode`|

#### Record1ObjectTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Account**|
|2|**Contact**|
|8|**User**|
|9|**Team**|
|50|**Position**|
|99|**Social Profile**|
|2013|**Territory**|
|4200|**Activity**|
|4201|**Appointment**|
|4202|**Email**|
|4204|**Fax**|
|4207|**Letter**|
|4210|**Phone Call**|
|4212|**Task**|
|4216|**Social Activity**|
|4251|**Recurring Appointment**|
|4710|**Process Session**|
|9400|**Channel Access Profile Rule**|
|9600|**Goal**|
|9930|**Knowledge Base Record**|
|9953|**Knowledge Article**|
|10377|**Invitation**|
|10378|**Invite Redemption**|
|10397|**Publishing State Transition Rule**|
|10399|**Shortcut**|
|10411|**Website**|

### <a name="BKMK_Record2ObjectTypeCode"></a> Record2ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Shows the record type of the target record.**|
|DisplayName|**Type (To)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`record2objecttypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`connection_record2objecttypecode`|

#### Record2ObjectTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Account**|
|2|**Contact**|
|8|**User**|
|9|**Team**|
|50|**Position**|
|99|**Social Profile**|
|2013|**Territory**|
|4200|**Activity**|
|4201|**Appointment**|
|4202|**Email**|
|4204|**Fax**|
|4207|**Letter**|
|4210|**Phone Call**|
|4212|**Task**|
|4216|**Social Activity**|
|4251|**Recurring Appointment**|
|4710|**Process Session**|
|9400|**Channel Access Profile Rule**|
|9600|**Goal**|
|9930|**Knowledge Base Record**|
|9953|**Knowledge Article**|
|10377|**Invitation**|
|10378|**Invite Redemption**|
|10397|**Publishing State Transition Rule**|
|10399|**Shortcut**|
|10411|**Website**|

### <a name="BKMK_RelatedConnectionId"></a> RelatedConnectionId

|Property|Value|
|---|---|
|Description|**Unique identifier for the reciprocal connection record.**|
|DisplayName|**Reciprocal Connection**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relatedconnectionid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|connection|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the connection.**|
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

- [account_connections1](#BKMK_account_connections1)
- [account_connections2](#BKMK_account_connections2)
- [activitypointer_connections1](#BKMK_activitypointer_connections1)
- [activitypointer_connections2](#BKMK_activitypointer_connections2)
- [adx_invitation_connections1](#BKMK_adx_invitation_connections1)
- [adx_invitation_connections2](#BKMK_adx_invitation_connections2)
- [adx_inviteredemption_connections1](#BKMK_adx_inviteredemption_connections1)
- [adx_inviteredemption_connections2](#BKMK_adx_inviteredemption_connections2)
- [appointment_connections1](#BKMK_appointment_connections1)
- [appointment_connections2](#BKMK_appointment_connections2)
- [business_unit_connections](#BKMK_business_unit_connections)
- [connection_related_connection](#BKMK_connection_related_connection-many-to-one)
- [connection_role_connections1](#BKMK_connection_role_connections1)
- [connection_role_connections2](#BKMK_connection_role_connections2)
- [contact_connections1](#BKMK_contact_connections1)
- [contact_connections2](#BKMK_contact_connections2)
- [createdby_connection](#BKMK_createdby_connection)
- [email_connections1](#BKMK_email_connections1)
- [email_connections2](#BKMK_email_connections2)
- [fax_connections1](#BKMK_fax_connections1)
- [fax_connections2](#BKMK_fax_connections2)
- [goal_connections1](#BKMK_goal_connections1)
- [goal_connections2](#BKMK_goal_connections2)
- [knowledgearticle_connections1](#BKMK_knowledgearticle_connections1)
- [knowledgearticle_connections2](#BKMK_knowledgearticle_connections2)
- [KnowledgeBaseRecord_connections1](#BKMK_KnowledgeBaseRecord_connections1)
- [KnowledgeBaseRecord_connections2](#BKMK_KnowledgeBaseRecord_connections2)
- [letter_connections1](#BKMK_letter_connections1)
- [letter_connections2](#BKMK_letter_connections2)
- [lk_connectionbase_createdonbehalfby](#BKMK_lk_connectionbase_createdonbehalfby)
- [lk_connectionbase_modifiedonbehalfby](#BKMK_lk_connectionbase_modifiedonbehalfby)
- [modifiedby_connection](#BKMK_modifiedby_connection)
- [mspp_publishingstatetransitionrule_connections1](#BKMK_mspp_publishingstatetransitionrule_connections1)
- [mspp_publishingstatetransitionrule_connections2](#BKMK_mspp_publishingstatetransitionrule_connections2)
- [mspp_shortcut_connections1](#BKMK_mspp_shortcut_connections1)
- [mspp_shortcut_connections2](#BKMK_mspp_shortcut_connections2)
- [mspp_website_connections1](#BKMK_mspp_website_connections1)
- [mspp_website_connections2](#BKMK_mspp_website_connections2)
- [owner_connections](#BKMK_owner_connections)
- [phonecall_connections1](#BKMK_phonecall_connections1)
- [phonecall_connections2](#BKMK_phonecall_connections2)
- [position_connection1](#BKMK_position_connection1)
- [position_connection2](#BKMK_position_connection2)
- [processsession_connections1](#BKMK_processsession_connections1)
- [processsession_connections2](#BKMK_processsession_connections2)
- [recurringappointmentmaster_connections1](#BKMK_recurringappointmentmaster_connections1)
- [recurringappointmentmaster_connections2](#BKMK_recurringappointmentmaster_connections2)
- [socialactivity_connections1](#BKMK_socialactivity_connections1)
- [socialactivity_connections2](#BKMK_socialactivity_connections2)
- [socialprofile_connections1](#BKMK_socialprofile_connections1)
- [socialprofile_connections2](#BKMK_socialprofile_connections2)
- [systemuser_connections1](#BKMK_systemuser_connections1)
- [systemuser_connections2](#BKMK_systemuser_connections2)
- [task_connections1](#BKMK_task_connections1)
- [task_connections2](#BKMK_task_connections2)
- [team_connections1](#BKMK_team_connections1)
- [team_connections2](#BKMK_team_connections2)
- [territory_connections1](#BKMK_territory_connections1)
- [territory_connections2](#BKMK_territory_connections2)
- [TransactionCurrency_Connection](#BKMK_TransactionCurrency_Connection)

### <a name="BKMK_account_connections1"></a> account_connections1

One-To-Many Relationship: [account account_connections1](account.md#BKMK_account_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_account_connections2"></a> account_connections2

One-To-Many Relationship: [account account_connections2](account.md#BKMK_account_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activitypointer_connections1"></a> activitypointer_connections1

One-To-Many Relationship: [activitypointer activitypointer_connections1](activitypointer.md#BKMK_activitypointer_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activitypointer_connections2"></a> activitypointer_connections2

One-To-Many Relationship: [activitypointer activitypointer_connections2](activitypointer.md#BKMK_activitypointer_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_connections1"></a> adx_invitation_connections1

One-To-Many Relationship: [adx_invitation adx_invitation_connections1](adx_invitation.md#BKMK_adx_invitation_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_connections2"></a> adx_invitation_connections2

One-To-Many Relationship: [adx_invitation adx_invitation_connections2](adx_invitation.md#BKMK_adx_invitation_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_connections1"></a> adx_inviteredemption_connections1

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_connections1](adx_inviteredemption.md#BKMK_adx_inviteredemption_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_connections2"></a> adx_inviteredemption_connections2

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_connections2](adx_inviteredemption.md#BKMK_adx_inviteredemption_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appointment_connections1"></a> appointment_connections1

One-To-Many Relationship: [appointment appointment_connections1](appointment.md#BKMK_appointment_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appointment_connections2"></a> appointment_connections2

One-To-Many Relationship: [appointment appointment_connections2](appointment.md#BKMK_appointment_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_connections"></a> business_unit_connections

One-To-Many Relationship: [businessunit business_unit_connections](businessunit.md#BKMK_business_unit_connections)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connection_related_connection-many-to-one"></a> connection_related_connection

One-To-Many Relationship: [connection connection_related_connection](#BKMK_connection_related_connection-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`connection`|
|ReferencedAttribute|`connectionid`|
|ReferencingAttribute|`relatedconnectionid`|
|ReferencingEntityNavigationPropertyName|`relatedconnectionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connection_role_connections1"></a> connection_role_connections1

One-To-Many Relationship: [connectionrole connection_role_connections1](connectionrole.md#BKMK_connection_role_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionrole`|
|ReferencedAttribute|`connectionroleid`|
|ReferencingAttribute|`record1roleid`|
|ReferencingEntityNavigationPropertyName|`record1roleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connection_role_connections2"></a> connection_role_connections2

One-To-Many Relationship: [connectionrole connection_role_connections2](connectionrole.md#BKMK_connection_role_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionrole`|
|ReferencedAttribute|`connectionroleid`|
|ReferencingAttribute|`record2roleid`|
|ReferencingEntityNavigationPropertyName|`record2roleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_connections1"></a> contact_connections1

One-To-Many Relationship: [contact contact_connections1](contact.md#BKMK_contact_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_connections2"></a> contact_connections2

One-To-Many Relationship: [contact contact_connections2](contact.md#BKMK_contact_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_createdby_connection"></a> createdby_connection

One-To-Many Relationship: [systemuser createdby_connection](systemuser.md#BKMK_createdby_connection)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_connections1"></a> email_connections1

One-To-Many Relationship: [email email_connections1](email.md#BKMK_email_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_connections2"></a> email_connections2

One-To-Many Relationship: [email email_connections2](email.md#BKMK_email_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fax_connections1"></a> fax_connections1

One-To-Many Relationship: [fax fax_connections1](fax.md#BKMK_fax_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fax_connections2"></a> fax_connections2

One-To-Many Relationship: [fax fax_connections2](fax.md#BKMK_fax_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_connections1"></a> goal_connections1

One-To-Many Relationship: [goal goal_connections1](goal.md#BKMK_goal_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_goal`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_connections2"></a> goal_connections2

One-To-Many Relationship: [goal goal_connections2](goal.md#BKMK_goal_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_goal`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_connections1"></a> knowledgearticle_connections1

One-To-Many Relationship: [knowledgearticle knowledgearticle_connections1](knowledgearticle.md#BKMK_knowledgearticle_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_connections2"></a> knowledgearticle_connections2

One-To-Many Relationship: [knowledgearticle knowledgearticle_connections2](knowledgearticle.md#BKMK_knowledgearticle_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_connections1"></a> KnowledgeBaseRecord_connections1

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_connections1](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_connections2"></a> KnowledgeBaseRecord_connections2

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_connections2](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_letter_connections1"></a> letter_connections1

One-To-Many Relationship: [letter letter_connections1](letter.md#BKMK_letter_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_letter_connections2"></a> letter_connections2

One-To-Many Relationship: [letter letter_connections2](letter.md#BKMK_letter_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_connectionbase_createdonbehalfby"></a> lk_connectionbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_connectionbase_createdonbehalfby](systemuser.md#BKMK_lk_connectionbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_connectionbase_modifiedonbehalfby"></a> lk_connectionbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_connectionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_connectionbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_connection"></a> modifiedby_connection

One-To-Many Relationship: [systemuser modifiedby_connection](systemuser.md#BKMK_modifiedby_connection)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_publishingstatetransitionrule_connections1"></a> mspp_publishingstatetransitionrule_connections1

One-To-Many Relationship: [mspp_publishingstatetransitionrule mspp_publishingstatetransitionrule_connections1](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstatetransitionrule`|
|ReferencedAttribute|`mspp_publishingstatetransitionruleid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_mspp_publishingstatetransitionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_publishingstatetransitionrule_connections2"></a> mspp_publishingstatetransitionrule_connections2

One-To-Many Relationship: [mspp_publishingstatetransitionrule mspp_publishingstatetransitionrule_connections2](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstatetransitionrule`|
|ReferencedAttribute|`mspp_publishingstatetransitionruleid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_mspp_publishingstatetransitionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_shortcut_connections1"></a> mspp_shortcut_connections1

One-To-Many Relationship: [mspp_shortcut mspp_shortcut_connections1](mspp_shortcut.md#BKMK_mspp_shortcut_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_shortcut`|
|ReferencedAttribute|`mspp_shortcutid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_mspp_shortcut`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_shortcut_connections2"></a> mspp_shortcut_connections2

One-To-Many Relationship: [mspp_shortcut mspp_shortcut_connections2](mspp_shortcut.md#BKMK_mspp_shortcut_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_shortcut`|
|ReferencedAttribute|`mspp_shortcutid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_mspp_shortcut`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_connections1"></a> mspp_website_connections1

One-To-Many Relationship: [mspp_website mspp_website_connections1](mspp_website.md#BKMK_mspp_website_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_mspp_website`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_connections2"></a> mspp_website_connections2

One-To-Many Relationship: [mspp_website mspp_website_connections2](mspp_website.md#BKMK_mspp_website_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_mspp_website`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_connections"></a> owner_connections

One-To-Many Relationship: [owner owner_connections](owner.md#BKMK_owner_connections)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_phonecall_connections1"></a> phonecall_connections1

One-To-Many Relationship: [phonecall phonecall_connections1](phonecall.md#BKMK_phonecall_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_phonecall_connections2"></a> phonecall_connections2

One-To-Many Relationship: [phonecall phonecall_connections2](phonecall.md#BKMK_phonecall_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_position_connection1"></a> position_connection1

One-To-Many Relationship: [position position_connection1](position.md#BKMK_position_connection1)

|Property|Value|
|---|---|
|ReferencedEntity|`position`|
|ReferencedAttribute|`positionid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_position`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_position_connection2"></a> position_connection2

One-To-Many Relationship: [position position_connection2](position.md#BKMK_position_connection2)

|Property|Value|
|---|---|
|ReferencedEntity|`position`|
|ReferencedAttribute|`positionid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_position`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processsession_connections1"></a> processsession_connections1

One-To-Many Relationship: [processsession processsession_connections1](processsession.md#BKMK_processsession_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_processsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processsession_connections2"></a> processsession_connections2

One-To-Many Relationship: [processsession processsession_connections2](processsession.md#BKMK_processsession_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_processsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurringappointmentmaster_connections1"></a> recurringappointmentmaster_connections1

One-To-Many Relationship: [recurringappointmentmaster recurringappointmentmaster_connections1](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurringappointmentmaster_connections2"></a> recurringappointmentmaster_connections2

One-To-Many Relationship: [recurringappointmentmaster recurringappointmentmaster_connections2](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialactivity_connections1"></a> socialactivity_connections1

One-To-Many Relationship: [socialactivity socialactivity_connections1](socialactivity.md#BKMK_socialactivity_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialactivity_connections2"></a> socialactivity_connections2

One-To-Many Relationship: [socialactivity socialactivity_connections2](socialactivity.md#BKMK_socialactivity_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialprofile_connections1"></a> socialprofile_connections1

One-To-Many Relationship: [socialprofile socialprofile_connections1](socialprofile.md#BKMK_socialprofile_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialprofile_connections2"></a> socialprofile_connections2

One-To-Many Relationship: [socialprofile socialprofile_connections2](socialprofile.md#BKMK_socialprofile_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_connections1"></a> systemuser_connections1

One-To-Many Relationship: [systemuser systemuser_connections1](systemuser.md#BKMK_systemuser_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_connections2"></a> systemuser_connections2

One-To-Many Relationship: [systemuser systemuser_connections2](systemuser.md#BKMK_systemuser_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_task_connections1"></a> task_connections1

One-To-Many Relationship: [task task_connections1](task.md#BKMK_task_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_task_connections2"></a> task_connections2

One-To-Many Relationship: [task task_connections2](task.md#BKMK_task_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_connections1"></a> team_connections1

One-To-Many Relationship: [team team_connections1](team.md#BKMK_team_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_connections2"></a> team_connections2

One-To-Many Relationship: [team team_connections2](team.md#BKMK_team_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_territory_connections1"></a> territory_connections1

One-To-Many Relationship: [territory territory_connections1](territory.md#BKMK_territory_connections1)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`record1id`|
|ReferencingEntityNavigationPropertyName|`record1id_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_territory_connections2"></a> territory_connections2

One-To-Many Relationship: [territory territory_connections2](territory.md#BKMK_territory_connections2)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`record2id`|
|ReferencingEntityNavigationPropertyName|`record2id_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_Connection"></a> TransactionCurrency_Connection

One-To-Many Relationship: [transactioncurrency TransactionCurrency_Connection](transactioncurrency.md#BKMK_TransactionCurrency_Connection)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [Connection_AsyncOperations](#BKMK_Connection_AsyncOperations)
- [connection_principalobjectattributeaccess](#BKMK_connection_principalobjectattributeaccess)
- [Connection_ProcessSessions](#BKMK_Connection_ProcessSessions)
- [connection_related_connection](#BKMK_connection_related_connection-one-to-many)
- [Connection_SyncErrors](#BKMK_Connection_SyncErrors)

### <a name="BKMK_Connection_AsyncOperations"></a> Connection_AsyncOperations

Many-To-One Relationship: [asyncoperation Connection_AsyncOperations](asyncoperation.md#BKMK_Connection_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Connection_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connection_principalobjectattributeaccess"></a> connection_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess connection_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_connection_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`connection_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Connection_ProcessSessions"></a> Connection_ProcessSessions

Many-To-One Relationship: [processsession Connection_ProcessSessions](processsession.md#BKMK_Connection_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Connection_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_connection_related_connection-one-to-many"></a> connection_related_connection

Many-To-One Relationship: [connection connection_related_connection](#BKMK_connection_related_connection-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`relatedconnectionid`|
|ReferencedEntityNavigationPropertyName|`connection_related_connection`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Connection_SyncErrors"></a> Connection_SyncErrors

Many-To-One Relationship: [syncerror Connection_SyncErrors](syncerror.md#BKMK_Connection_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Connection_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.connection?displayProperty=fullName>
