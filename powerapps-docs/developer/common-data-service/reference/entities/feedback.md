---
title: "Feedback Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Feedback entity."

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
---
# Feedback Entity Reference

Container for feedback and ratings for knowledge articles.

## Entity Properties

**DisplayName**: Feedback<br />
**DisplayCollectionName**: Feedback<br />
**SchemaName**: Feedback<br />
**CollectionSchemaName**: Feedback<br />
**LogicalName**: feedback<br />
**LogicalCollectionName**: feedback<br />
**EntitySetName**: feedback<br />
**PrimaryIdAttribute**: feedbackid<br />
**PrimaryNameAttribute**: title<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Comments](#BKMK_Comments)
- [CreatedByContact](#BKMK_CreatedByContact)
- [CreatedOnBehalfByContact](#BKMK_CreatedOnBehalfByContact)
- [FeedbackId](#BKMK_FeedbackId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MaxRating](#BKMK_MaxRating)
- [MinRating](#BKMK_MinRating)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Rating](#BKMK_Rating)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Source](#BKMK_Source)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)


### <a name="BKMK_Comments"></a> Comments

**Description**: Type the feedback comments.<br />
**DisplayName**: Comments<br />
**LogicalName**: comments<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_CreatedByContact"></a> CreatedByContact

**Description**: Shows the contact who created the record.<br />
**DisplayName**: Created By (Contact)<br />
**LogicalName**: createdbycontact<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: contact


### <a name="BKMK_CreatedOnBehalfByContact"></a> CreatedOnBehalfByContact

**Description**: Shows the contact who created the record on behalf of another user.<br />
**DisplayName**: Created OnBelhalfBy (Contact)<br />
**LogicalName**: createdonbehalfbycontact<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: contact


### <a name="BKMK_FeedbackId"></a> FeedbackId

**Description**: FeedbackId<br />
**DisplayName**: Feedback<br />
**LogicalName**: feedbackid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Unique identifier of the data import or data migration that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MaxRating"></a> MaxRating

**Description**: Enter the maximum rating value.<br />
**DisplayName**: Maximum Rating<br />
**LogicalName**: maxrating<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MinRating"></a> MinRating

**Description**: Enter the minimum rating value.<br />
**DisplayName**: Minimum Rating<br />
**LogicalName**: minrating<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the knowledge article views.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_Rating"></a> Rating

**Description**: Specifies how helpful the related record was.<br />
**DisplayName**: Rating<br />
**LogicalName**: rating<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Shows the record that the feedback is associated with.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: contact,feedback,knowledgearticle


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_Source"></a> Source

**Description**: Shows where the feedback was submitted from.<br />
**DisplayName**: Source<br />
**LogicalName**: source<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Internal
- **Value**: 1 **Label**: Portal



### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the feedback is open, rejected or closed.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Open **DefaultStatus**: 1 **InvariantName**: Open
- **Value**: 1 **Label**: Closed **DefaultStatus**: 3 **InvariantName**: Closed



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the feedback's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Proposed **State**: 0
- **Value**: 2 **Label**: Accepted **State**: 0
- **Value**: 3 **Label**: Closed **State**: 1
- **Value**: 4 **Label**: Rejected **State**: 1



### <a name="BKMK_Title"></a> Title

**Description**: Type a title for the feedback.<br />
**DisplayName**: Title<br />
**LogicalName**: title<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 155


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Choose the local currency for the record to make sure budgets are reported in the correct currency.<br />
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

- [ClosedBy](#BKMK_ClosedBy)
- [ClosedByName](#BKMK_ClosedByName)
- [ClosedByYomiName](#BKMK_ClosedByYomiName)
- [ClosedOn](#BKMK_ClosedOn)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByContactName](#BKMK_CreatedByContactName)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByContactName](#BKMK_CreatedOnBehalfByContactName)
- [CreatedOnBehalfByContactYomiName](#BKMK_CreatedOnBehalfByContactYomiName)
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
- [NormalizedRating](#BKMK_NormalizedRating)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ClosedBy"></a> ClosedBy

**Description**: Shows who closed the record.<br />
**DisplayName**: Closed By<br />
**LogicalName**: closedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ClosedByName"></a> ClosedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: closedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ClosedByYomiName"></a> ClosedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: closedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ClosedOn"></a> ClosedOn

**Description**: Shows the date and time when the record was closed. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Closed On<br />
**LogicalName**: closedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByContactName"></a> CreatedByContactName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbycontactname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByContactName"></a> CreatedOnBehalfByContactName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbycontactname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByContactYomiName"></a> CreatedOnBehalfByContactYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbycontactyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
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

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
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


### <a name="BKMK_NormalizedRating"></a> NormalizedRating

**Description**: Shows the rating scaled to a value between 0 and 1 based on minimum and maximum ratings.<br />
**DisplayName**: Normalized Rating<br />
**LogicalName**: normalizedrating<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: -100000000000<br />
**Precision**: 2


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the knowledge article views.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team that owns the feedback.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns this feedback.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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

**Description**: Version number of the feedback.<br />
**DisplayName**: Version Number<br />
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

- [Feedback_SyncErrors](#BKMK_Feedback_SyncErrors)
- [feedback_feedback](#BKMK_feedback_feedback)
- [feedback_principalobjectattributeaccess](#BKMK_feedback_principalobjectattributeaccess)


### <a name="BKMK_Feedback_SyncErrors"></a> Feedback_SyncErrors

Same as syncerror entity [Feedback_SyncErrors](syncerror.md#BKMK_Feedback_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Feedback_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_feedback_feedback"></a> feedback_feedback

Same as feedback entity [feedback_feedback](feedback.md#BKMK_feedback_feedback) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: feedback_feedback<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 150

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_feedback_principalobjectattributeaccess"></a> feedback_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [feedback_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_feedback_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: feedback_principalobjectattributeaccess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_feedback_modifiedby](#BKMK_lk_feedback_modifiedby)
- [Contact_Feedback](#BKMK_Contact_Feedback)
- [lk_feedback_closedby](#BKMK_lk_feedback_closedby)
- [feedback_feedback](#BKMK_feedback_feedback)
- [lk_feedback_createdonbehalfby](#BKMK_lk_feedback_createdonbehalfby)
- [KnowledgeArticle_Feedback](#BKMK_KnowledgeArticle_Feedback)
- [transactioncurrency_feedback](#BKMK_transactioncurrency_feedback)
- [lk_feedback_modifiedonbehalfby](#BKMK_lk_feedback_modifiedonbehalfby)
- [business_unit_feedback](#BKMK_business_unit_feedback)
- [lk_contact_feedback_createdonbehalfby](#BKMK_lk_contact_feedback_createdonbehalfby)
- [lk_contact_feedback_createdby](#BKMK_lk_contact_feedback_createdby)
- [lk_feedback_createdby](#BKMK_lk_feedback_createdby)


### <a name="BKMK_lk_feedback_modifiedby"></a> lk_feedback_modifiedby

See systemuser Entity [lk_feedback_modifiedby](systemuser.md#BKMK_lk_feedback_modifiedby) One-To-Many relationship.

### <a name="BKMK_Contact_Feedback"></a> Contact_Feedback

See contact Entity [Contact_Feedback](contact.md#BKMK_Contact_Feedback) One-To-Many relationship.

### <a name="BKMK_lk_feedback_closedby"></a> lk_feedback_closedby

See systemuser Entity [lk_feedback_closedby](systemuser.md#BKMK_lk_feedback_closedby) One-To-Many relationship.

### <a name="BKMK_feedback_feedback"></a> feedback_feedback

See feedback Entity [feedback_feedback](feedback.md#BKMK_feedback_feedback) One-To-Many relationship.

### <a name="BKMK_lk_feedback_createdonbehalfby"></a> lk_feedback_createdonbehalfby

See systemuser Entity [lk_feedback_createdonbehalfby](systemuser.md#BKMK_lk_feedback_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticle_Feedback"></a> KnowledgeArticle_Feedback

See knowledgearticle Entity [KnowledgeArticle_Feedback](knowledgearticle.md#BKMK_KnowledgeArticle_Feedback) One-To-Many relationship.

### <a name="BKMK_transactioncurrency_feedback"></a> transactioncurrency_feedback

See transactioncurrency Entity [transactioncurrency_feedback](transactioncurrency.md#BKMK_transactioncurrency_feedback) One-To-Many relationship.

### <a name="BKMK_lk_feedback_modifiedonbehalfby"></a> lk_feedback_modifiedonbehalfby

See systemuser Entity [lk_feedback_modifiedonbehalfby](systemuser.md#BKMK_lk_feedback_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_feedback"></a> business_unit_feedback

See businessunit Entity [business_unit_feedback](businessunit.md#BKMK_business_unit_feedback) One-To-Many relationship.

### <a name="BKMK_lk_contact_feedback_createdonbehalfby"></a> lk_contact_feedback_createdonbehalfby

See contact Entity [lk_contact_feedback_createdonbehalfby](contact.md#BKMK_lk_contact_feedback_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_contact_feedback_createdby"></a> lk_contact_feedback_createdby

See contact Entity [lk_contact_feedback_createdby](contact.md#BKMK_lk_contact_feedback_createdby) One-To-Many relationship.

### <a name="BKMK_lk_feedback_createdby"></a> lk_feedback_createdby

See systemuser Entity [lk_feedback_createdby](systemuser.md#BKMK_lk_feedback_createdby) One-To-Many relationship.
feedback

