---
title: "TransactionCurrency Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the TransactionCurrency entity."
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
# TransactionCurrency Entity Reference

Currency in which a financial transaction is carried out.

## Entity Properties

**DisplayName**: Currency<br />
**DisplayCollectionName**: Currencies<br />
**SchemaName**: TransactionCurrency<br />
**CollectionSchemaName**: TransactionCurrencies<br />
**LogicalName**: transactioncurrency<br />
**LogicalCollectionName**: transactioncurrencies<br />
**EntitySetName**: transactioncurrencies<br />
**PrimaryIdAttribute**: transactioncurrencyid<br />
**PrimaryNameAttribute**: currencyname<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CurrencyName](#BKMK_CurrencyName)
- [CurrencyPrecision](#BKMK_CurrencyPrecision)
- [CurrencySymbol](#BKMK_CurrencySymbol)
- [EntityImage](#BKMK_EntityImage)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [ISOCurrencyCode](#BKMK_ISOCurrencyCode)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)


### <a name="BKMK_CurrencyName"></a> CurrencyName

**Description**: Name of the transaction currency.<br />
**DisplayName**: Currency Name<br />
**LogicalName**: currencyname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CurrencyPrecision"></a> CurrencyPrecision

**Description**: Number of decimal places that can be used for currency.<br />
**DisplayName**: Currency Precision<br />
**LogicalName**: currencyprecision<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 4<br />
**MinValue**: 0


### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

**Description**: Symbol for the transaction currency.<br />
**DisplayName**: Currency Symbol<br />
**LogicalName**: currencysymbol<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 10


### <a name="BKMK_EntityImage"></a> EntityImage

**Description**: The default image for the entity.<br />
**DisplayName**: Entity Image<br />
**LogicalName**: entityimage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Image<br />
**IsPrimaryImage**: False<br />
**MaxHeight**: 144<br />
**MaxWidth**: 144


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate between the transaction currency and the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


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


### <a name="BKMK_ISOCurrencyCode"></a> ISOCurrencyCode

**Description**: ISO currency code for the transaction currency.<br />
**DisplayName**: Currency Code<br />
**LogicalName**: isocurrencycode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


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


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the transaction currency.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the transaction currency.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the transaction currency.<br />
**DisplayName**: Transaction Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

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
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [UniqueDscId](#BKMK_UniqueDscId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the transaction currency.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the transaction currency was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the transactioncurrency.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_timestamp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_url<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_EntityImageId"></a> EntityImageId

**Description**: For internal use only.<br />
**DisplayName**: Entity Image Id<br />
**LogicalName**: entityimageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the transaction currency.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the transaction currency was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the transactioncurrency.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the transaction currency.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_UniqueDscId"></a> UniqueDscId

**Description**: For internal use only.<br />
**DisplayName**: UniqueDscId<br />
**LogicalName**: uniquedscid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the transaction currency.<br />
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

- [TransactionCurrency_Territory](#BKMK_TransactionCurrency_Territory)
- [TransactionCurrency_Goal](#BKMK_TransactionCurrency_Goal)
- [TransactionCurrency_SharePointSite](#BKMK_TransactionCurrency_SharePointSite)
- [TransactionCurrency_QueueItem](#BKMK_TransactionCurrency_QueueItem)
- [transactioncurrency_actioncard](#BKMK_transactioncurrency_actioncard)
- [TransactionCurrency_officegraphdocument](#BKMK_TransactionCurrency_officegraphdocument)
- [TransactionCurrency_KnowledgeBaseRecord](#BKMK_TransactionCurrency_KnowledgeBaseRecord)
- [TransactionCurrency_SharePointDocument](#BKMK_TransactionCurrency_SharePointDocument)
- [TransactionCurrency_delveactionhub](#BKMK_TransactionCurrency_delveactionhub)
- [TransactionCurrency_ActionCardUserState](#BKMK_TransactionCurrency_ActionCardUserState)
- [TransactionCurrency_SharePointDocumentLocation](#BKMK_TransactionCurrency_SharePointDocumentLocation)
- [TransactionCurrency_SLAItem](#BKMK_TransactionCurrency_SLAItem)
- [transactioncurrency_expiredprocess](#BKMK_transactioncurrency_expiredprocess)
- [TransactionCurrency_externalpartyitem](#BKMK_TransactionCurrency_externalpartyitem)
- [TransactionCurrency_profileruleitem](#BKMK_TransactionCurrency_profileruleitem)
- [TransactionCurrency_ProcessSessions](#BKMK_TransactionCurrency_ProcessSessions)
- [TransactionCurrency_profilerule](#BKMK_TransactionCurrency_profilerule)
- [TransactionCurrency_SyncErrors](#BKMK_TransactionCurrency_SyncErrors)
- [transactioncurrency_socialactivity](#BKMK_transactioncurrency_socialactivity)
- [TransactionCurrency_MailMergeTemplate](#BKMK_TransactionCurrency_MailMergeTemplate)
- [TransactionCurrency_UserMapping](#BKMK_TransactionCurrency_UserMapping)
- [transactioncurrency_fixedmonthlyfiscalcalendar](#BKMK_transactioncurrency_fixedmonthlyfiscalcalendar)
- [transactioncurrency_semiannualfiscalcalendar](#BKMK_transactioncurrency_semiannualfiscalcalendar)
- [TransactionCurrency_PhoneCall](#BKMK_TransactionCurrency_PhoneCall)
- [TransactionCurrency_Fax](#BKMK_TransactionCurrency_Fax)
- [transactioncurrency_usersettings](#BKMK_transactioncurrency_usersettings)
- [userentityinstancedata_transactioncurrency](#BKMK_userentityinstancedata_transactioncurrency)
- [TransactionCurrency_ActivityPointer](#BKMK_TransactionCurrency_ActivityPointer)
- [transactioncurrency_category](#BKMK_transactioncurrency_category)
- [TransactionCurrency_ConvertRule](#BKMK_TransactionCurrency_ConvertRule)
- [transactioncurrency_position](#BKMK_transactioncurrency_position)
- [TransactionCurrency_Task](#BKMK_TransactionCurrency_Task)
- [TransactionCurrency_SLA](#BKMK_TransactionCurrency_SLA)
- [basecurrency_organization](#BKMK_basecurrency_organization)
- [TransactionCurrency_Letter](#BKMK_TransactionCurrency_Letter)
- [transactioncurrency_convertruleitem](#BKMK_transactioncurrency_convertruleitem)
- [TransactionCurrency_routingruleitem](#BKMK_TransactionCurrency_routingruleitem)
- [transactioncurrency_cardtype](#BKMK_transactioncurrency_cardtype)
- [TransactionCurrency_SystemUser](#BKMK_TransactionCurrency_SystemUser)
- [TransactionCurrency_Team](#BKMK_TransactionCurrency_Team)
- [TransactionCurrency_Email](#BKMK_TransactionCurrency_Email)
- [TransactionCurrency_BusinessUnit](#BKMK_TransactionCurrency_BusinessUnit)
- [transactioncurrency_SocialProfile](#BKMK_transactioncurrency_SocialProfile)
- [TransactionCurrency_Queue](#BKMK_TransactionCurrency_Queue)
- [TransactionCurrency_DuplicateMatchingRecord](#BKMK_TransactionCurrency_DuplicateMatchingRecord)
- [TransactionCurrency_Appointment](#BKMK_TransactionCurrency_Appointment)
- [transactioncurrency_quarterlyfiscalcalendar](#BKMK_transactioncurrency_quarterlyfiscalcalendar)
- [TransactionCurrency_KbArticle](#BKMK_TransactionCurrency_KbArticle)
- [transactioncurrency_monthlyfiscalcalendar](#BKMK_transactioncurrency_monthlyfiscalcalendar)
- [TransactionCurrency_CustomerAddress](#BKMK_TransactionCurrency_CustomerAddress)
- [transactioncurrency_annualfiscalcalendar](#BKMK_transactioncurrency_annualfiscalcalendar)
- [TransactionCurrency_Connection](#BKMK_TransactionCurrency_Connection)
- [transactioncurrency_translationprocess](#BKMK_transactioncurrency_translationprocess)
- [TransactionCurrency_ExternalParty](#BKMK_TransactionCurrency_ExternalParty)
- [transactioncurrency_feedback](#BKMK_transactioncurrency_feedback)
- [transactioncurrency_contact](#BKMK_transactioncurrency_contact)
- [TransactionCurrency_ReportCategory](#BKMK_TransactionCurrency_ReportCategory)
- [TransactionCurrency_InteractionForEmail](#BKMK_TransactionCurrency_InteractionForEmail)
- [TransactionCurrency_suggestioncardtemplate](#BKMK_TransactionCurrency_suggestioncardtemplate)
- [TransactionCurrency_slakpiinstance](#BKMK_TransactionCurrency_slakpiinstance)
- [TransactionCurrency_DuplicateBaseRecord](#BKMK_TransactionCurrency_DuplicateBaseRecord)
- [TransactionCurrency_AsyncOperations](#BKMK_TransactionCurrency_AsyncOperations)
- [transactioncurrency_knowledgearticleviews](#BKMK_transactioncurrency_knowledgearticleviews)
- [TransactionCurrency_Theme](#BKMK_TransactionCurrency_Theme)
- [TransactionCurrency_ChannelAccessProfile](#BKMK_TransactionCurrency_ChannelAccessProfile)
- [transactioncurrency_newprocess](#BKMK_transactioncurrency_newprocess)
- [TransactionCurrency_knowledgearticle](#BKMK_TransactionCurrency_knowledgearticle)
- [TransactionCurrency_RecurringAppointmentMaster](#BKMK_TransactionCurrency_RecurringAppointmentMaster)
- [transactioncurrency_account](#BKMK_transactioncurrency_account)
- [TransactionCurrency_recommendeddocument](#BKMK_TransactionCurrency_recommendeddocument)
- [TransactionCurrency_Routingrule](#BKMK_TransactionCurrency_Routingrule)


### <a name="BKMK_TransactionCurrency_Territory"></a> TransactionCurrency_Territory

Same as territory entity [TransactionCurrency_Territory](territory.md#BKMK_TransactionCurrency_Territory) Many-To-One relationship.

**ReferencingEntity**: territory<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Territory<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Goal"></a> TransactionCurrency_Goal

Same as goal entity [TransactionCurrency_Goal](goal.md#BKMK_TransactionCurrency_Goal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Goal<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_SharePointSite"></a> TransactionCurrency_SharePointSite

Same as sharepointsite entity [TransactionCurrency_SharePointSite](sharepointsite.md#BKMK_TransactionCurrency_SharePointSite) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_SharePointSite<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_QueueItem"></a> TransactionCurrency_QueueItem

Same as queueitem entity [TransactionCurrency_QueueItem](queueitem.md#BKMK_TransactionCurrency_QueueItem) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_QueueItem<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_actioncard"></a> transactioncurrency_actioncard

Same as actioncard entity [transactioncurrency_actioncard](actioncard.md#BKMK_transactioncurrency_actioncard) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_actioncard<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_officegraphdocument"></a> TransactionCurrency_officegraphdocument

Same as officegraphdocument entity [TransactionCurrency_officegraphdocument](officegraphdocument.md#BKMK_TransactionCurrency_officegraphdocument) Many-To-One relationship.

**ReferencingEntity**: officegraphdocument<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_officegraphdocument<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_KnowledgeBaseRecord"></a> TransactionCurrency_KnowledgeBaseRecord

Same as knowledgebaserecord entity [TransactionCurrency_KnowledgeBaseRecord](knowledgebaserecord.md#BKMK_TransactionCurrency_KnowledgeBaseRecord) Many-To-One relationship.

**ReferencingEntity**: knowledgebaserecord<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_KnowledgeBaseRecord<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_SharePointDocument"></a> TransactionCurrency_SharePointDocument

Same as sharepointdocument entity [TransactionCurrency_SharePointDocument](sharepointdocument.md#BKMK_TransactionCurrency_SharePointDocument) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_SharePointDocument<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_delveactionhub"></a> TransactionCurrency_delveactionhub

Same as delveactionhub entity [TransactionCurrency_delveactionhub](delveactionhub.md#BKMK_TransactionCurrency_delveactionhub) Many-To-One relationship.

**ReferencingEntity**: delveactionhub<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_delveactionhub<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_ActionCardUserState"></a> TransactionCurrency_ActionCardUserState

Same as actioncarduserstate entity [TransactionCurrency_ActionCardUserState](actioncarduserstate.md#BKMK_TransactionCurrency_ActionCardUserState) Many-To-One relationship.

**ReferencingEntity**: actioncarduserstate<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_ActionCardUserState<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_SharePointDocumentLocation"></a> TransactionCurrency_SharePointDocumentLocation

Same as sharepointdocumentlocation entity [TransactionCurrency_SharePointDocumentLocation](sharepointdocumentlocation.md#BKMK_TransactionCurrency_SharePointDocumentLocation) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_SharePointDocumentLocation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_SLAItem"></a> TransactionCurrency_SLAItem

Same as slaitem entity [TransactionCurrency_SLAItem](slaitem.md#BKMK_TransactionCurrency_SLAItem) Many-To-One relationship.

**ReferencingEntity**: slaitem<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_SLAItem<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_expiredprocess"></a> transactioncurrency_expiredprocess

Same as expiredprocess entity [transactioncurrency_expiredprocess](expiredprocess.md#BKMK_transactioncurrency_expiredprocess) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_expiredprocess<br />
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


### <a name="BKMK_TransactionCurrency_externalpartyitem"></a> TransactionCurrency_externalpartyitem

Same as externalpartyitem entity [TransactionCurrency_externalpartyitem](externalpartyitem.md#BKMK_TransactionCurrency_externalpartyitem) Many-To-One relationship.

**ReferencingEntity**: externalpartyitem<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_externalpartyitem<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_profileruleitem"></a> TransactionCurrency_profileruleitem

Same as channelaccessprofileruleitem entity [TransactionCurrency_profileruleitem](channelaccessprofileruleitem.md#BKMK_TransactionCurrency_profileruleitem) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofileruleitem<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_profileruleitem<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_ProcessSessions"></a> TransactionCurrency_ProcessSessions

Same as processsession entity [TransactionCurrency_ProcessSessions](processsession.md#BKMK_TransactionCurrency_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_profilerule"></a> TransactionCurrency_profilerule

Same as channelaccessprofilerule entity [TransactionCurrency_profilerule](channelaccessprofilerule.md#BKMK_TransactionCurrency_profilerule) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_profilerule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_SyncErrors"></a> TransactionCurrency_SyncErrors

Same as syncerror entity [TransactionCurrency_SyncErrors](syncerror.md#BKMK_TransactionCurrency_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_SyncErrors<br />
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


### <a name="BKMK_transactioncurrency_socialactivity"></a> transactioncurrency_socialactivity

Same as socialactivity entity [transactioncurrency_socialactivity](socialactivity.md#BKMK_transactioncurrency_socialactivity) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_socialactivity<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_MailMergeTemplate"></a> TransactionCurrency_MailMergeTemplate

Same as mailmergetemplate entity [TransactionCurrency_MailMergeTemplate](mailmergetemplate.md#BKMK_TransactionCurrency_MailMergeTemplate) Many-To-One relationship.

**ReferencingEntity**: mailmergetemplate<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_MailMergeTemplate<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_UserMapping"></a> TransactionCurrency_UserMapping

Same as usermapping entity [TransactionCurrency_UserMapping](usermapping.md#BKMK_TransactionCurrency_UserMapping) Many-To-One relationship.

**ReferencingEntity**: usermapping<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_UserMapping<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_fixedmonthlyfiscalcalendar"></a> transactioncurrency_fixedmonthlyfiscalcalendar

Same as fixedmonthlyfiscalcalendar entity [transactioncurrency_fixedmonthlyfiscalcalendar](fixedmonthlyfiscalcalendar.md#BKMK_transactioncurrency_fixedmonthlyfiscalcalendar) Many-To-One relationship.

**ReferencingEntity**: fixedmonthlyfiscalcalendar<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_fixedmonthlyfiscalcalendar<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_semiannualfiscalcalendar"></a> transactioncurrency_semiannualfiscalcalendar

Same as semiannualfiscalcalendar entity [transactioncurrency_semiannualfiscalcalendar](semiannualfiscalcalendar.md#BKMK_transactioncurrency_semiannualfiscalcalendar) Many-To-One relationship.

**ReferencingEntity**: semiannualfiscalcalendar<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_semiannualfiscalcalendar<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_PhoneCall"></a> TransactionCurrency_PhoneCall

Same as phonecall entity [TransactionCurrency_PhoneCall](phonecall.md#BKMK_TransactionCurrency_PhoneCall) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_PhoneCall<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Fax"></a> TransactionCurrency_Fax

Same as fax entity [TransactionCurrency_Fax](fax.md#BKMK_TransactionCurrency_Fax) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Fax<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_usersettings"></a> transactioncurrency_usersettings

Same as usersettings entity [transactioncurrency_usersettings](usersettings.md#BKMK_transactioncurrency_usersettings) Many-To-One relationship.

**ReferencingEntity**: usersettings<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_usersettings<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_userentityinstancedata_transactioncurrency"></a> userentityinstancedata_transactioncurrency

Same as userentityinstancedata entity [userentityinstancedata_transactioncurrency](userentityinstancedata.md#BKMK_userentityinstancedata_transactioncurrency) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_transactioncurrency<br />
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


### <a name="BKMK_TransactionCurrency_ActivityPointer"></a> TransactionCurrency_ActivityPointer

Same as activitypointer entity [TransactionCurrency_ActivityPointer](activitypointer.md#BKMK_TransactionCurrency_ActivityPointer) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_ActivityPointer<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_category"></a> transactioncurrency_category

Same as category entity [transactioncurrency_category](category.md#BKMK_transactioncurrency_category) Many-To-One relationship.

**ReferencingEntity**: category<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_category<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_ConvertRule"></a> TransactionCurrency_ConvertRule

Same as convertrule entity [TransactionCurrency_ConvertRule](convertrule.md#BKMK_TransactionCurrency_ConvertRule) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_ConvertRule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_position"></a> transactioncurrency_position

Same as position entity [transactioncurrency_position](position.md#BKMK_transactioncurrency_position) Many-To-One relationship.

**ReferencingEntity**: position<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_position<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Task"></a> TransactionCurrency_Task

Same as task entity [TransactionCurrency_Task](task.md#BKMK_TransactionCurrency_Task) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Task<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_SLA"></a> TransactionCurrency_SLA

Same as sla entity [TransactionCurrency_SLA](sla.md#BKMK_TransactionCurrency_SLA) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_SLA<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_basecurrency_organization"></a> basecurrency_organization

Same as organization entity [basecurrency_organization](organization.md#BKMK_basecurrency_organization) Many-To-One relationship.

**ReferencingEntity**: organization<br />
**ReferencingAttribute**: basecurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: basecurrency_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Letter"></a> TransactionCurrency_Letter

Same as letter entity [TransactionCurrency_Letter](letter.md#BKMK_TransactionCurrency_Letter) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Letter<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_convertruleitem"></a> transactioncurrency_convertruleitem

Same as convertruleitem entity [transactioncurrency_convertruleitem](convertruleitem.md#BKMK_transactioncurrency_convertruleitem) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_convertruleitem<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_routingruleitem"></a> TransactionCurrency_routingruleitem

Same as routingruleitem entity [TransactionCurrency_routingruleitem](routingruleitem.md#BKMK_TransactionCurrency_routingruleitem) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_routingruleitem<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_cardtype"></a> transactioncurrency_cardtype

Same as cardtype entity [transactioncurrency_cardtype](cardtype.md#BKMK_transactioncurrency_cardtype) Many-To-One relationship.

**ReferencingEntity**: cardtype<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_cardtype<br />
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


### <a name="BKMK_TransactionCurrency_SystemUser"></a> TransactionCurrency_SystemUser

Same as systemuser entity [TransactionCurrency_SystemUser](systemuser.md#BKMK_TransactionCurrency_SystemUser) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_SystemUser<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Team"></a> TransactionCurrency_Team

Same as team entity [TransactionCurrency_Team](team.md#BKMK_TransactionCurrency_Team) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Team<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Email"></a> TransactionCurrency_Email

Same as email entity [TransactionCurrency_Email](email.md#BKMK_TransactionCurrency_Email) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Email<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_BusinessUnit"></a> TransactionCurrency_BusinessUnit

Same as businessunit entity [TransactionCurrency_BusinessUnit](businessunit.md#BKMK_TransactionCurrency_BusinessUnit) Many-To-One relationship.

**ReferencingEntity**: businessunit<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_BusinessUnit<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_SocialProfile"></a> transactioncurrency_SocialProfile

Same as socialprofile entity [transactioncurrency_SocialProfile](socialprofile.md#BKMK_transactioncurrency_SocialProfile) Many-To-One relationship.

**ReferencingEntity**: socialprofile<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_SocialProfile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Queue"></a> TransactionCurrency_Queue

Same as queue entity [TransactionCurrency_Queue](queue.md#BKMK_TransactionCurrency_Queue) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Queue<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_DuplicateMatchingRecord"></a> TransactionCurrency_DuplicateMatchingRecord

Same as duplicaterecord entity [TransactionCurrency_DuplicateMatchingRecord](duplicaterecord.md#BKMK_TransactionCurrency_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_DuplicateMatchingRecord<br />
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


### <a name="BKMK_TransactionCurrency_Appointment"></a> TransactionCurrency_Appointment

Same as appointment entity [TransactionCurrency_Appointment](appointment.md#BKMK_TransactionCurrency_Appointment) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Appointment<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_quarterlyfiscalcalendar"></a> transactioncurrency_quarterlyfiscalcalendar

Same as quarterlyfiscalcalendar entity [transactioncurrency_quarterlyfiscalcalendar](quarterlyfiscalcalendar.md#BKMK_transactioncurrency_quarterlyfiscalcalendar) Many-To-One relationship.

**ReferencingEntity**: quarterlyfiscalcalendar<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_quarterlyfiscalcalendar<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_KbArticle"></a> TransactionCurrency_KbArticle

Same as kbarticle entity [TransactionCurrency_KbArticle](kbarticle.md#BKMK_TransactionCurrency_KbArticle) Many-To-One relationship.

**ReferencingEntity**: kbarticle<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_KbArticle<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_monthlyfiscalcalendar"></a> transactioncurrency_monthlyfiscalcalendar

Same as monthlyfiscalcalendar entity [transactioncurrency_monthlyfiscalcalendar](monthlyfiscalcalendar.md#BKMK_transactioncurrency_monthlyfiscalcalendar) Many-To-One relationship.

**ReferencingEntity**: monthlyfiscalcalendar<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_monthlyfiscalcalendar<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_CustomerAddress"></a> TransactionCurrency_CustomerAddress

Same as customeraddress entity [TransactionCurrency_CustomerAddress](customeraddress.md#BKMK_TransactionCurrency_CustomerAddress) Many-To-One relationship.

**ReferencingEntity**: customeraddress<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_CustomerAddress<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_annualfiscalcalendar"></a> transactioncurrency_annualfiscalcalendar

Same as annualfiscalcalendar entity [transactioncurrency_annualfiscalcalendar](annualfiscalcalendar.md#BKMK_transactioncurrency_annualfiscalcalendar) Many-To-One relationship.

**ReferencingEntity**: annualfiscalcalendar<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_annualfiscalcalendar<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Connection"></a> TransactionCurrency_Connection

Same as connection entity [TransactionCurrency_Connection](connection.md#BKMK_TransactionCurrency_Connection) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Connection<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_translationprocess"></a> transactioncurrency_translationprocess

Same as translationprocess entity [transactioncurrency_translationprocess](translationprocess.md#BKMK_transactioncurrency_translationprocess) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_translationprocess<br />
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


### <a name="BKMK_TransactionCurrency_ExternalParty"></a> TransactionCurrency_ExternalParty

Same as externalparty entity [TransactionCurrency_ExternalParty](externalparty.md#BKMK_TransactionCurrency_ExternalParty) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_externalparty<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_feedback"></a> transactioncurrency_feedback

Same as feedback entity [transactioncurrency_feedback](feedback.md#BKMK_transactioncurrency_feedback) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_feedback<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_contact"></a> transactioncurrency_contact

Same as contact entity [transactioncurrency_contact](contact.md#BKMK_transactioncurrency_contact) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_contact<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_ReportCategory"></a> TransactionCurrency_ReportCategory

Same as reportcategory entity [TransactionCurrency_ReportCategory](reportcategory.md#BKMK_TransactionCurrency_ReportCategory) Many-To-One relationship.

**ReferencingEntity**: reportcategory<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_ReportCategory<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_InteractionForEmail"></a> TransactionCurrency_InteractionForEmail

Same as interactionforemail entity [TransactionCurrency_InteractionForEmail](interactionforemail.md#BKMK_TransactionCurrency_InteractionForEmail) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_InteractionForEmail<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_suggestioncardtemplate"></a> TransactionCurrency_suggestioncardtemplate

Same as suggestioncardtemplate entity [TransactionCurrency_suggestioncardtemplate](suggestioncardtemplate.md#BKMK_TransactionCurrency_suggestioncardtemplate) Many-To-One relationship.

**ReferencingEntity**: suggestioncardtemplate<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_suggestioncardtemplate<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_slakpiinstance"></a> TransactionCurrency_slakpiinstance

Same as slakpiinstance entity [TransactionCurrency_slakpiinstance](slakpiinstance.md#BKMK_TransactionCurrency_slakpiinstance) Many-To-One relationship.

**ReferencingEntity**: slakpiinstance<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_slakpiinstance<br />
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


### <a name="BKMK_TransactionCurrency_DuplicateBaseRecord"></a> TransactionCurrency_DuplicateBaseRecord

Same as duplicaterecord entity [TransactionCurrency_DuplicateBaseRecord](duplicaterecord.md#BKMK_TransactionCurrency_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_DuplicateBaseRecord<br />
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


### <a name="BKMK_TransactionCurrency_AsyncOperations"></a> TransactionCurrency_AsyncOperations

Same as asyncoperation entity [TransactionCurrency_AsyncOperations](asyncoperation.md#BKMK_TransactionCurrency_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_AsyncOperations<br />
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


### <a name="BKMK_transactioncurrency_knowledgearticleviews"></a> transactioncurrency_knowledgearticleviews

Same as knowledgearticleviews entity [transactioncurrency_knowledgearticleviews](knowledgearticleviews.md#BKMK_transactioncurrency_knowledgearticleviews) Many-To-One relationship.

**ReferencingEntity**: knowledgearticleviews<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_knowledgearticleviews<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Theme"></a> TransactionCurrency_Theme

Same as theme entity [TransactionCurrency_Theme](theme.md#BKMK_TransactionCurrency_Theme) Many-To-One relationship.

**ReferencingEntity**: theme<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Theme<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_ChannelAccessProfile"></a> TransactionCurrency_ChannelAccessProfile

Same as channelaccessprofile entity [TransactionCurrency_ChannelAccessProfile](channelaccessprofile.md#BKMK_TransactionCurrency_ChannelAccessProfile) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_channelaccessprofile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_newprocess"></a> transactioncurrency_newprocess

Same as newprocess entity [transactioncurrency_newprocess](newprocess.md#BKMK_transactioncurrency_newprocess) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_newprocess<br />
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


### <a name="BKMK_TransactionCurrency_knowledgearticle"></a> TransactionCurrency_knowledgearticle

Same as knowledgearticle entity [TransactionCurrency_knowledgearticle](knowledgearticle.md#BKMK_TransactionCurrency_knowledgearticle) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_knowledgearticle<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_RecurringAppointmentMaster"></a> TransactionCurrency_RecurringAppointmentMaster

Same as recurringappointmentmaster entity [TransactionCurrency_RecurringAppointmentMaster](recurringappointmentmaster.md#BKMK_TransactionCurrency_RecurringAppointmentMaster) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_RecurringAppointmentMaster<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_transactioncurrency_account"></a> transactioncurrency_account

Same as account entity [transactioncurrency_account](account.md#BKMK_transactioncurrency_account) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: transactioncurrency_account<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_recommendeddocument"></a> TransactionCurrency_recommendeddocument

Same as recommendeddocument entity [TransactionCurrency_recommendeddocument](recommendeddocument.md#BKMK_TransactionCurrency_recommendeddocument) Many-To-One relationship.

**ReferencingEntity**: recommendeddocument<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_recommendeddocument<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_TransactionCurrency_Routingrule"></a> TransactionCurrency_Routingrule

Same as routingrule entity [TransactionCurrency_Routingrule](routingrule.md#BKMK_TransactionCurrency_Routingrule) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: transactioncurrencyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransactionCurrency_Routingrule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_transactioncurrencybase_createdby](#BKMK_lk_transactioncurrencybase_createdby)
- [lk_transactioncurrencybase_modifiedby](#BKMK_lk_transactioncurrencybase_modifiedby)
- [lk_transactioncurrency_modifiedonbehalfby](#BKMK_lk_transactioncurrency_modifiedonbehalfby)
- [organization_transactioncurrencies](#BKMK_organization_transactioncurrencies)
- [lk_transactioncurrency_createdonbehalfby](#BKMK_lk_transactioncurrency_createdonbehalfby)


### <a name="BKMK_lk_transactioncurrencybase_createdby"></a> lk_transactioncurrencybase_createdby

See systemuser Entity [lk_transactioncurrencybase_createdby](systemuser.md#BKMK_lk_transactioncurrencybase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_transactioncurrencybase_modifiedby"></a> lk_transactioncurrencybase_modifiedby

See systemuser Entity [lk_transactioncurrencybase_modifiedby](systemuser.md#BKMK_lk_transactioncurrencybase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_transactioncurrency_modifiedonbehalfby"></a> lk_transactioncurrency_modifiedonbehalfby

See systemuser Entity [lk_transactioncurrency_modifiedonbehalfby](systemuser.md#BKMK_lk_transactioncurrency_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_transactioncurrencies"></a> organization_transactioncurrencies

See organization Entity [organization_transactioncurrencies](organization.md#BKMK_organization_transactioncurrencies) One-To-Many relationship.

### <a name="BKMK_lk_transactioncurrency_createdonbehalfby"></a> lk_transactioncurrency_createdonbehalfby

See systemuser Entity [lk_transactioncurrency_createdonbehalfby](systemuser.md#BKMK_lk_transactioncurrency_createdonbehalfby) One-To-Many relationship.
transactioncurrency

