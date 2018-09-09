---
title: "CardType Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the CardType entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# CardType Entity Reference

To provide master data for the card types list. For internal use only

## Entity Properties

**DisplayName**: Action Card Type<br />
**DisplayCollectionName**: Action Card Type<br />
**SchemaName**: CardType<br />
**CollectionSchemaName**: CardTypes<br />
**LogicalName**: cardtype<br />
**LogicalCollectionName**: cardtypes<br />
**EntitySetName**: cardtype<br />
**PrimaryIdAttribute**: cardtypeid<br />
**PrimaryNameAttribute**: cardname<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Actions](#BKMK_Actions)
- [BoolCardOption](#BKMK_BoolCardOption)
- [CardName](#BKMK_CardName)
- [CardType](#BKMK_CardType)
- [CardTypeIcon](#BKMK_CardTypeIcon)
- [CardTypeId](#BKMK_CardTypeId)
- [ClientAvailability](#BKMK_ClientAvailability)
- [GroupType](#BKMK_GroupType)
- [HasSnoozeDismiss](#BKMK_HasSnoozeDismiss)
- [IntCardOption](#BKMK_IntCardOption)
- [IsBaseCard](#BKMK_IsBaseCard)
- [IsEnabled](#BKMK_IsEnabled)
- [IsLiveOnly](#BKMK_IsLiveOnly)
- [IsPreviewCard](#BKMK_IsPreviewCard)
- [LastSyncTime](#BKMK_LastSyncTime)
- [ScheduleTime](#BKMK_ScheduleTime)
- [SoftTitle](#BKMK_SoftTitle)
- [StringCardOption](#BKMK_StringCardOption)
- [SummaryText](#BKMK_SummaryText)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)


### <a name="BKMK_Actions"></a> Actions

**Description**: For internal use only.<br />
**DisplayName**: CommandBar Actions JSON definition<br />
**LogicalName**: actions<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 8192


### <a name="BKMK_BoolCardOption"></a> BoolCardOption

**Description**: Bolean option for a cardtype.<br />
**DisplayName**: Bolean option for a cardtype.<br />
**LogicalName**: boolcardoption<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Check
- **FalseOption Value**: 0 **Label**: Uncheck

**DefaultValue**: False


### <a name="BKMK_CardName"></a> CardName

**Description**: The name of the custom entity.<br />
**DisplayName**: CardName<br />
**LogicalName**: cardname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CardType"></a> CardType

**Description**: The CardType ENUM value.<br />
**DisplayName**: CardType ENUM<br />
**LogicalName**: cardtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: Duration<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_CardTypeIcon"></a> CardTypeIcon

**Description**: The CardTypeIcon of the card.<br />
**DisplayName**: CardTypeIcon<br />
**LogicalName**: cardtypeicon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_CardTypeId"></a> CardTypeId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: CardType<br />
**LogicalName**: cardtypeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ClientAvailability"></a> ClientAvailability

**Description**: Determines on which client is this card available on.<br />
**DisplayName**: Card Client Availability<br />
**LogicalName**: clientavailability<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: WebClientOnly
- **Value**: 2 **Label**: MocaOnly
- **Value**: 3 **Label**: MocaAndWeb



### <a name="BKMK_GroupType"></a> GroupType

**Description**: Specifies the card group type<br />
**DisplayName**: GroupType<br />
**LogicalName**: grouptype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_HasSnoozeDismiss"></a> HasSnoozeDismiss

**Description**: Specifies if the card type has snooze dismiss<br />
**DisplayName**: HasSnoozeDismiss<br />
**LogicalName**: hassnoozedismiss<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IntCardOption"></a> IntCardOption

**Description**: Any int option for a cardtype.<br />
**DisplayName**: Any int option for a cardtype.<br />
**LogicalName**: intcardoption<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IsBaseCard"></a> IsBaseCard

**Description**: IsBaseCard<br />
**DisplayName**: IsBaseCard<br />
**LogicalName**: isbasecard<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsEnabled"></a> IsEnabled

**Description**: IsEnabled<br />
**DisplayName**: IsEnabled<br />
**LogicalName**: isenabled<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsLiveOnly"></a> IsLiveOnly

**Description**: IsLiveOnly<br />
**DisplayName**: IsLiveOnly<br />
**LogicalName**: isliveonly<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsPreviewCard"></a> IsPreviewCard

**Description**: IsPreviewCard<br />
**DisplayName**: IsPreviewCard<br />
**LogicalName**: ispreviewcard<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_LastSyncTime"></a> LastSyncTime

**Description**: This column is updated by the Plugin based on the last fetched data.<br />
**DisplayName**: LastSyncTime<br />
**LogicalName**: lastsynctime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ScheduleTime"></a> ScheduleTime

**Description**: This column is updated by the Plugin based on the last fetched data.<br />
**DisplayName**: ScheduleTime<br />
**LogicalName**: scheduletime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: Recommended<br />
**Type**: DateTime<br />
**DateTimeBehavior**: TimeZoneIndependent<br />
**Format**: DateAndTime


### <a name="BKMK_SoftTitle"></a> SoftTitle

**Description**: The soft title of the card.<br />
**DisplayName**: Soft Title<br />
**LogicalName**: softtitle<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_StringCardOption"></a> StringCardOption

**Description**: Any string option for a cardtype.<br />
**DisplayName**: Any string option for a cardtype.<br />
**LogicalName**: stringcardoption<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 8192


### <a name="BKMK_SummaryText"></a> SummaryText

**Description**: The summary text of the card.<br />
**DisplayName**: Summary Text<br />
**LogicalName**: summarytext<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Exchange rate for the currency associated with the CardType with respect to the base currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the record.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the CardType with respect to the base currency.<br />
**DisplayName**: ExchangeRate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the record was modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [cardtype_actioncard](#BKMK_cardtype_actioncard)
- [cardtype_actioncardusersettings](#BKMK_cardtype_actioncardusersettings)


### <a name="BKMK_cardtype_actioncard"></a> cardtype_actioncard

Same as actioncard entity [cardtype_actioncard](actioncard.md#BKMK_cardtype_actioncard) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: cardtypeid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: cardtype_actioncards<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_cardtype_actioncardusersettings"></a> cardtype_actioncardusersettings

Same as actioncardusersettings entity [cardtype_actioncardusersettings](actioncardusersettings.md#BKMK_cardtype_actioncardusersettings) Many-To-One relationship.

**ReferencingEntity**: actioncardusersettings<br />
**ReferencingAttribute**: cardtypeid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: cardtype_actioncardusersettingss<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_cardtype_createdby](#BKMK_lk_cardtype_createdby)
- [lk_cardtype_createdonbehalfby](#BKMK_lk_cardtype_createdonbehalfby)
- [lk_cardtype_modifiedby](#BKMK_lk_cardtype_modifiedby)
- [lk_cardtype_modifiedonbehalfby](#BKMK_lk_cardtype_modifiedonbehalfby)
- [transactioncurrency_cardtype](#BKMK_transactioncurrency_cardtype)


### <a name="BKMK_lk_cardtype_createdby"></a> lk_cardtype_createdby

See systemuser Entity [lk_cardtype_createdby](systemuser.md#BKMK_lk_cardtype_createdby) One-To-Many relationship.

### <a name="BKMK_lk_cardtype_createdonbehalfby"></a> lk_cardtype_createdonbehalfby

See systemuser Entity [lk_cardtype_createdonbehalfby](systemuser.md#BKMK_lk_cardtype_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_cardtype_modifiedby"></a> lk_cardtype_modifiedby

See systemuser Entity [lk_cardtype_modifiedby](systemuser.md#BKMK_lk_cardtype_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_cardtype_modifiedonbehalfby"></a> lk_cardtype_modifiedonbehalfby

See systemuser Entity [lk_cardtype_modifiedonbehalfby](systemuser.md#BKMK_lk_cardtype_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_transactioncurrency_cardtype"></a> transactioncurrency_cardtype

See transactioncurrency Entity [transactioncurrency_cardtype](transactioncurrency.md#BKMK_transactioncurrency_cardtype) One-To-Many relationship.
cardtype

