---
title: "Action Card (ActionCard) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Action Card (ActionCard) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Action Card (ActionCard) table/entity reference (Microsoft Dataverse)

Action card entity to show action cards.

## Messages

The following table lists the messages for the Action Card (ActionCard) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /actioncards<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /actioncards(*actioncardid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /actioncards(*actioncardid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /actioncards<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /actioncards(*actioncardid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /actioncards(*actioncardid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Action Card (ActionCard) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Action Card** |
| **DisplayCollectionName** | **Action Cards** |
| **SchemaName** | `ActionCard` |
| **CollectionSchemaName** | `ActionCards` |
| **EntitySetName** | `actioncards`|
| **LogicalName** | `actioncard` |
| **LogicalCollectionName** | `actioncard` |
| **PrimaryIdAttribute** | `actioncardid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActionCardId](#BKMK_ActionCardId)
- [CardType](#BKMK_CardType)
- [CardTypeId](#BKMK_CardTypeId)
- [Data](#BKMK_Data)
- [Description](#BKMK_Description)
- [ExpiryDate](#BKMK_ExpiryDate)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentRegardingObjectId](#BKMK_ParentRegardingObjectId)
- [ParentRegardingObjectIdData](#BKMK_ParentRegardingObjectIdData)
- [ParentRegardingObjectTypeCode](#BKMK_ParentRegardingObjectTypeCode)
- [Priority](#BKMK_Priority)
- [RecordId](#BKMK_RecordId)
- [RecordIdObjectTypeCode](#BKMK_RecordIdObjectTypeCode)
- [RecordIdObjectTypeCode2](#BKMK_RecordIdObjectTypeCode2)
- [ReferenceTokens](#BKMK_ReferenceTokens)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Source](#BKMK_Source)
- [StartDate](#BKMK_StartDate)
- [State](#BKMK_State)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [Visibility](#BKMK_Visibility)

### <a name="BKMK_ActionCardId"></a> ActionCardId

|Property|Value|
|---|---|
|Description|**Unique identifier of the action card.**|
|DisplayName|**Action Card**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`actioncardid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CardType"></a> CardType

|Property|Value|
|---|---|
|Description|**The CardType ENUM value.**|
|DisplayName|**CardType ENUM**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cardtype`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_CardTypeId"></a> CardTypeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the card type.**|
|DisplayName|**Card Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cardtypeid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|cardtype|

### <a name="BKMK_Data"></a> Data

|Property|Value|
|---|---|
|Description|**Json formatted string for generic purpose.**|
|DisplayName|**Data Associated with Card Commandbar Actions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`data`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8192|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Card Description**|
|DisplayName|**Card Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8192|

### <a name="BKMK_ExpiryDate"></a> ExpiryDate

|Property|Value|
|---|---|
|Description|**Shows the Expiry Date**|
|DisplayName|**Expiry Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`expirydate`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|Description|**Unique identifier of the user or team who owns the action card.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ParentRegardingObjectId"></a> ParentRegardingObjectId

|Property|Value|
|---|---|
|Description|**ParentRegardingObjectId of the ActionCard**|
|DisplayName|**ParentRegardingObjectId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentregardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_ParentRegardingObjectIdData"></a> ParentRegardingObjectIdData

|Property|Value|
|---|---|
|Description|**Json formatted string for parent regarding object.**|
|DisplayName|**ParentRegardingObjectIdData**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentregardingobjectiddata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8192|

### <a name="BKMK_ParentRegardingObjectTypeCode"></a> ParentRegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**ParentRegardingObjectTypeCode of the ActionCard**|
|DisplayName|**ParentRegardingObjectTypeCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentregardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Priority"></a> Priority

|Property|Value|
|---|---|
|Description|**Priority of the ActionCard**|
|DisplayName|**Priority**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`priority`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_RecordId"></a> RecordId

|Property|Value|
|---|---|
|Description|**Shows the record ID.**|
|DisplayName|**RecordId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_RecordIdObjectTypeCode"></a> RecordIdObjectTypeCode

|Property|Value|
|---|---|
|Description|**Shows the Object Type Code.**|
|DisplayName|**RecordIdObjectTypeCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recordidobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RecordIdObjectTypeCode2"></a> RecordIdObjectTypeCode2

|Property|Value|
|---|---|
|Description|**RecordIdObjectTypeCode2 of the ActionCard**|
|DisplayName|**RecordIdObjectTypeCode2**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recordidobjecttypecode2`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ReferenceTokens"></a> ReferenceTokens

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Data Associated constructing title and body**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`referencetokens`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8192|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the record that the card relates to.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, adx_inviteredemption, adx_portalcomment, appointment, chat, contact, email, fax, letter, phonecall, recurringappointmentmaster, task|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Source"></a> Source

|Property|Value|
|---|---|
|Description|**Source for the Action Card**|
|DisplayName|**Action Card Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`source`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`actioncard_source`|

#### Source Choices/Options

|Value|Label|
|---|---|
|1|**CRM**|
|2|**Exchange**|

### <a name="BKMK_StartDate"></a> StartDate

|Property|Value|
|---|---|
|Description|**Shows the Start Date**|
|DisplayName|**Start Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`startdate`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_State"></a> State

|Property|Value|
|---|---|
|Description|**State of the Action Card**|
|DisplayName|**Action Card State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`state`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`actioncard_state`|

#### State Choices/Options

|Value|Label|
|---|---|
|0|**Active**|
|1|**Dismissed**|
|2|**Completed**|

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**Title of the ActionCard**|
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the action card.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_Visibility"></a> Visibility

|Property|Value|
|---|---|
|Description|**Select whether the visibility should be set to public/private.**|
|DisplayName|**Visibiliy Status of ActionCard**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`visibility`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`actioncard_visibility`|
|DefaultValue|False|
|True Label|Private|
|False Label|Public|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
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
|Description|**Unique identifier of the user who created the action card.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when action card was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the action card.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the action card with respect to the base currency.**|
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

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the action card.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when action card was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who last modified action card.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
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
|Description|**Unique identifier of the business unit that owns the action card.**|
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
|Description|**Unique identifier of the team who owns the action card.**|
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
|Description|**Unique identifier of the user who owns the action card.**|
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
|Description|**Version number of the action card.**|
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

- [account_actioncard](#BKMK_account_actioncard)
- [adx_inviteredemption_ActionCards](#BKMK_adx_inviteredemption_ActionCards)
- [adx_portalcomment_ActionCards](#BKMK_adx_portalcomment_ActionCards)
- [appointment_actioncard](#BKMK_appointment_actioncard)
- [business_unit_actioncards](#BKMK_business_unit_actioncards)
- [chat_ActionCards](#BKMK_chat_ActionCards)
- [contact_actioncard](#BKMK_contact_actioncard)
- [email_actioncard](#BKMK_email_actioncard)
- [fax_actioncard](#BKMK_fax_actioncard)
- [letter_actioncard](#BKMK_letter_actioncard)
- [lk_actioncardbase_createdby](#BKMK_lk_actioncardbase_createdby)
- [lk_actioncardbase_createdonbehalfby](#BKMK_lk_actioncardbase_createdonbehalfby)
- [lk_actioncardbase_modifiedby](#BKMK_lk_actioncardbase_modifiedby)
- [lk_actioncardbase_modifiedonbehalfby](#BKMK_lk_actioncardbase_modifiedonbehalfby)
- [owner_actioncards](#BKMK_owner_actioncards)
- [phonecall_actioncard](#BKMK_phonecall_actioncard)
- [recurringappointmentmaster_actioncard](#BKMK_recurringappointmentmaster_actioncard)
- [task_actioncard](#BKMK_task_actioncard)
- [transactioncurrency_actioncard](#BKMK_transactioncurrency_actioncard)

### <a name="BKMK_account_actioncard"></a> account_actioncard

One-To-Many Relationship: [account account_actioncard](account.md#BKMK_account_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_ActionCards"></a> adx_inviteredemption_ActionCards

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_ActionCards](adx_inviteredemption.md#BKMK_adx_inviteredemption_ActionCards)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_ActionCards"></a> adx_portalcomment_ActionCards

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_ActionCards](adx_portalcomment.md#BKMK_adx_portalcomment_ActionCards)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appointment_actioncard"></a> appointment_actioncard

One-To-Many Relationship: [appointment appointment_actioncard](appointment.md#BKMK_appointment_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`regardingobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appointment_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_actioncards"></a> business_unit_actioncards

One-To-Many Relationship: [businessunit business_unit_actioncards](businessunit.md#BKMK_business_unit_actioncards)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_ActionCards"></a> chat_ActionCards

One-To-Many Relationship: [chat chat_ActionCards](chat.md#BKMK_chat_ActionCards)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_actioncard"></a> contact_actioncard

One-To-Many Relationship: [contact contact_actioncard](contact.md#BKMK_contact_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_actioncard"></a> email_actioncard

One-To-Many Relationship: [email email_actioncard](email.md#BKMK_email_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`regardingobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_email_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fax_actioncard"></a> fax_actioncard

One-To-Many Relationship: [fax fax_actioncard](fax.md#BKMK_fax_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`regardingobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fax_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_letter_actioncard"></a> letter_actioncard

One-To-Many Relationship: [letter letter_actioncard](letter.md#BKMK_letter_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`regardingobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_letter_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_actioncardbase_createdby"></a> lk_actioncardbase_createdby

One-To-Many Relationship: [systemuser lk_actioncardbase_createdby](systemuser.md#BKMK_lk_actioncardbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_actioncardbase_createdonbehalfby"></a> lk_actioncardbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_actioncardbase_createdonbehalfby](systemuser.md#BKMK_lk_actioncardbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_actioncardbase_modifiedby"></a> lk_actioncardbase_modifiedby

One-To-Many Relationship: [systemuser lk_actioncardbase_modifiedby](systemuser.md#BKMK_lk_actioncardbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_actioncardbase_modifiedonbehalfby"></a> lk_actioncardbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_actioncardbase_modifiedonbehalfby](systemuser.md#BKMK_lk_actioncardbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_actioncards"></a> owner_actioncards

One-To-Many Relationship: [owner owner_actioncards](owner.md#BKMK_owner_actioncards)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_phonecall_actioncard"></a> phonecall_actioncard

One-To-Many Relationship: [phonecall phonecall_actioncard](phonecall.md#BKMK_phonecall_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`regardingobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_phonecall_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurringappointmentmaster_actioncard"></a> recurringappointmentmaster_actioncard

One-To-Many Relationship: [recurringappointmentmaster recurringappointmentmaster_actioncard](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`regardingobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recurringappointmentmaster_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_task_actioncard"></a> task_actioncard

One-To-Many Relationship: [task task_actioncard](task.md#BKMK_task_actioncard)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`regardingobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_task_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_actioncard"></a> transactioncurrency_actioncard

One-To-Many Relationship: [transactioncurrency transactioncurrency_actioncard](transactioncurrency.md#BKMK_transactioncurrency_actioncard)

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

### <a name="BKMK_ActionCardUserState_ActionCard"></a> ActionCardUserState_ActionCard

Many-To-One Relationship: [actioncarduserstate ActionCardUserState_ActionCard](actioncarduserstate.md#BKMK_ActionCardUserState_ActionCard)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncarduserstate`|
|ReferencingAttribute|`actioncardid`|
|ReferencedEntityNavigationPropertyName|`ActionCardUserState_ActionCard`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.actioncard?displayProperty=fullName>
