---
title: "Currency (TransactionCurrency)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Currency (TransactionCurrency)  table/entity."
ms.date: 12/07/2022
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Currency (TransactionCurrency)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Currency in which a financial transaction is carried out.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.2/transactioncurrencies<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.2/transactioncurrencies(*transactioncurrencyid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.2/transactioncurrencies(*transactioncurrencyid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveExchangeRate|<xref href="Microsoft.Dynamics.CRM.RetrieveExchangeRate?text=RetrieveExchangeRate Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveExchangeRateRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.2/transactioncurrencies<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH [*org URI*]/api/data/v9.2/transactioncurrencies(*transactioncurrencyid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.2/transactioncurrencies(*transactioncurrencyid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|TransactionCurrencies|
|DisplayCollectionName|Currencies|
|DisplayName|Currency|
|EntitySetName|transactioncurrencies|
|IsBPFEntity|False|
|LogicalCollectionName|transactioncurrencies|
|LogicalName|transactioncurrency|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|transactioncurrencyid|
|PrimaryNameAttribute|currencyname|
|SchemaName|TransactionCurrency|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Name of the transaction currency.|
|DisplayName|Currency Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|currencyname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CurrencyPrecision"></a> CurrencyPrecision

|Property|Value|
|--------|-----|
|Description|Number of decimal places that can be used for currency.|
|DisplayName|Currency Precision|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|currencyprecision|
|MaxValue|10|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

|Property|Value|
|--------|-----|
|Description|Symbol for the transaction currency.|
|DisplayName|Currency Symbol|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|currencysymbol|
|MaxLength|10|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|--------|-----|
|Description|The default image for the entity.|
|DisplayName|Entity Image|
|IsPrimaryImage|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage|
|MaxHeight|144|
|MaxWidth|144|
|RequiredLevel|None|
|Type|Image|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate between the transaction currency and the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|SystemRequired|
|Type|Decimal|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ISOCurrencyCode"></a> ISOCurrencyCode

|Property|Value|
|--------|-----|
|Description|ISO currency code for the transaction currency.|
|DisplayName|Currency Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|isocurrencycode|
|MaxLength|5|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the transaction currency.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the transaction currency.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the transaction currency.|
|DisplayName|Transaction Currency|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|transactioncurrencyid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the transaction currency.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the transaction currency was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the transactioncurrency.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Entity Image Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the transaction currency.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the transaction currency was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the transactioncurrency.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the transaction currency.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_UniqueDscId"></a> UniqueDscId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|UniqueDscId|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|uniquedscid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the transaction currency.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [TransactionCurrency_Goal](#BKMK_TransactionCurrency_Goal)
- [TransactionCurrency_SharePointSite](#BKMK_TransactionCurrency_SharePointSite)
- [TransactionCurrency_QueueItem](#BKMK_TransactionCurrency_QueueItem)
- [transactioncurrency_actioncard](#BKMK_transactioncurrency_actioncard)
- [TransactionCurrency_officegraphdocument](#BKMK_TransactionCurrency_officegraphdocument)
- [TransactionCurrency_KnowledgeBaseRecord](#BKMK_TransactionCurrency_KnowledgeBaseRecord)
- [TransactionCurrency_ActionCardUserState](#BKMK_TransactionCurrency_ActionCardUserState)
- [TransactionCurrency_SharePointDocumentLocation](#BKMK_TransactionCurrency_SharePointDocumentLocation)
- [TransactionCurrency_SLAItem](#BKMK_TransactionCurrency_SLAItem)
- [transactioncurrency_expiredprocess](#BKMK_transactioncurrency_expiredprocess)
- [TransactionCurrency_ProcessSessions](#BKMK_TransactionCurrency_ProcessSessions)
- [TransactionCurrency_SyncErrors](#BKMK_TransactionCurrency_SyncErrors)
- [transactioncurrency_socialactivity](#BKMK_transactioncurrency_socialactivity)
- [TransactionCurrency_MailMergeTemplate](#BKMK_TransactionCurrency_MailMergeTemplate)
- [TransactionCurrency_UserMapping](#BKMK_TransactionCurrency_UserMapping)
- [transactioncurrency_fixedmonthlyfiscalcalendar](#BKMK_transactioncurrency_fixedmonthlyfiscalcalendar)
- [transactioncurrency_semiannualfiscalcalendar](#BKMK_transactioncurrency_semiannualfiscalcalendar)
- [TransactionCurrency_PhoneCall](#BKMK_TransactionCurrency_PhoneCall)
- [TransactionCurrency_Fax](#BKMK_TransactionCurrency_Fax)
- [transactioncurrency_usersettings](#BKMK_transactioncurrency_usersettings)
- [TransactionCurrency_ActivityPointer](#BKMK_TransactionCurrency_ActivityPointer)
- [transactioncurrency_category](#BKMK_transactioncurrency_category)
- [transactioncurrency_position](#BKMK_transactioncurrency_position)
- [TransactionCurrency_Task](#BKMK_TransactionCurrency_Task)
- [TransactionCurrency_SLA](#BKMK_TransactionCurrency_SLA)
- [basecurrency_organization](#BKMK_basecurrency_organization)
- [TransactionCurrency_Letter](#BKMK_TransactionCurrency_Letter)
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
- [transactioncurrency_feedback](#BKMK_transactioncurrency_feedback)
- [transactioncurrency_contact](#BKMK_transactioncurrency_contact)
- [TransactionCurrency_ReportCategory](#BKMK_TransactionCurrency_ReportCategory)
- [TransactionCurrency_InteractionForEmail](#BKMK_TransactionCurrency_InteractionForEmail)
- [TransactionCurrency_slakpiinstance](#BKMK_TransactionCurrency_slakpiinstance)
- [TransactionCurrency_DuplicateBaseRecord](#BKMK_TransactionCurrency_DuplicateBaseRecord)
- [TransactionCurrency_AsyncOperations](#BKMK_TransactionCurrency_AsyncOperations)
- [transactioncurrency_knowledgearticleviews](#BKMK_transactioncurrency_knowledgearticleviews)
- [TransactionCurrency_Theme](#BKMK_TransactionCurrency_Theme)
- [transactioncurrency_newprocess](#BKMK_transactioncurrency_newprocess)
- [TransactionCurrency_knowledgearticle](#BKMK_TransactionCurrency_knowledgearticle)
- [TransactionCurrency_RecurringAppointmentMaster](#BKMK_TransactionCurrency_RecurringAppointmentMaster)
- [transactioncurrency_account](#BKMK_transactioncurrency_account)
- [TransactionCurrency_recommendeddocument](#BKMK_TransactionCurrency_recommendeddocument)
- [TransactionCurrency_Territory](#BKMK_TransactionCurrency_Territory)
- [chat_transactioncurrency_transactioncurrencyid](#BKMK_chat_transactioncurrency_transactioncurrencyid)


### <a name="BKMK_TransactionCurrency_Goal"></a> TransactionCurrency_Goal

Same as the [TransactionCurrency_Goal](goal.md#BKMK_TransactionCurrency_Goal) many-to-one relationship for the [goal](goal.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Goal|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_SharePointSite"></a> TransactionCurrency_SharePointSite

Same as the [TransactionCurrency_SharePointSite](sharepointsite.md#BKMK_TransactionCurrency_SharePointSite) many-to-one relationship for the [sharepointsite](sharepointsite.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_SharePointSite|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_QueueItem"></a> TransactionCurrency_QueueItem

Same as the [TransactionCurrency_QueueItem](queueitem.md#BKMK_TransactionCurrency_QueueItem) many-to-one relationship for the [queueitem](queueitem.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_QueueItem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_actioncard"></a> transactioncurrency_actioncard

Same as the [transactioncurrency_actioncard](actioncard.md#BKMK_transactioncurrency_actioncard) many-to-one relationship for the [actioncard](actioncard.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_actioncard|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_officegraphdocument"></a> TransactionCurrency_officegraphdocument

Same as the [TransactionCurrency_officegraphdocument](officegraphdocument.md#BKMK_TransactionCurrency_officegraphdocument) many-to-one relationship for the [officegraphdocument](officegraphdocument.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|officegraphdocument|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_officegraphdocument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_KnowledgeBaseRecord"></a> TransactionCurrency_KnowledgeBaseRecord

Same as the [TransactionCurrency_KnowledgeBaseRecord](knowledgebaserecord.md#BKMK_TransactionCurrency_KnowledgeBaseRecord) many-to-one relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgebaserecord|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_KnowledgeBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_ActionCardUserState"></a> TransactionCurrency_ActionCardUserState

Same as the [TransactionCurrency_ActionCardUserState](actioncarduserstate.md#BKMK_TransactionCurrency_ActionCardUserState) many-to-one relationship for the [actioncarduserstate](actioncarduserstate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncarduserstate|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_ActionCardUserState|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_SharePointDocumentLocation"></a> TransactionCurrency_SharePointDocumentLocation

Same as the [TransactionCurrency_SharePointDocumentLocation](sharepointdocumentlocation.md#BKMK_TransactionCurrency_SharePointDocumentLocation) many-to-one relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_SharePointDocumentLocation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_SLAItem"></a> TransactionCurrency_SLAItem

Same as the [TransactionCurrency_SLAItem](slaitem.md#BKMK_TransactionCurrency_SLAItem) many-to-one relationship for the [slaitem](slaitem.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_SLAItem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_expiredprocess"></a> transactioncurrency_expiredprocess

Same as the [transactioncurrency_expiredprocess](expiredprocess.md#BKMK_transactioncurrency_expiredprocess) many-to-one relationship for the [expiredprocess](expiredprocess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_expiredprocess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_ProcessSessions"></a> TransactionCurrency_ProcessSessions

Same as the [TransactionCurrency_ProcessSessions](processsession.md#BKMK_TransactionCurrency_ProcessSessions) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_SyncErrors"></a> TransactionCurrency_SyncErrors

Same as the [TransactionCurrency_SyncErrors](syncerror.md#BKMK_TransactionCurrency_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_transactioncurrency_socialactivity"></a> transactioncurrency_socialactivity

Same as the [transactioncurrency_socialactivity](socialactivity.md#BKMK_transactioncurrency_socialactivity) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_socialactivity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_MailMergeTemplate"></a> TransactionCurrency_MailMergeTemplate

Same as the [TransactionCurrency_MailMergeTemplate](mailmergetemplate.md#BKMK_TransactionCurrency_MailMergeTemplate) many-to-one relationship for the [mailmergetemplate](mailmergetemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailmergetemplate|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_MailMergeTemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_UserMapping"></a> TransactionCurrency_UserMapping

Same as the [TransactionCurrency_UserMapping](usermapping.md#BKMK_TransactionCurrency_UserMapping) many-to-one relationship for the [usermapping](usermapping.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|usermapping|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_UserMapping|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_fixedmonthlyfiscalcalendar"></a> transactioncurrency_fixedmonthlyfiscalcalendar

Same as the [transactioncurrency_fixedmonthlyfiscalcalendar](fixedmonthlyfiscalcalendar.md#BKMK_transactioncurrency_fixedmonthlyfiscalcalendar) many-to-one relationship for the [fixedmonthlyfiscalcalendar](fixedmonthlyfiscalcalendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fixedmonthlyfiscalcalendar|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_fixedmonthlyfiscalcalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_semiannualfiscalcalendar"></a> transactioncurrency_semiannualfiscalcalendar

Same as the [transactioncurrency_semiannualfiscalcalendar](semiannualfiscalcalendar.md#BKMK_transactioncurrency_semiannualfiscalcalendar) many-to-one relationship for the [semiannualfiscalcalendar](semiannualfiscalcalendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|semiannualfiscalcalendar|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_semiannualfiscalcalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_PhoneCall"></a> TransactionCurrency_PhoneCall

Same as the [TransactionCurrency_PhoneCall](phonecall.md#BKMK_TransactionCurrency_PhoneCall) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_PhoneCall|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Fax"></a> TransactionCurrency_Fax

Same as the [TransactionCurrency_Fax](fax.md#BKMK_TransactionCurrency_Fax) many-to-one relationship for the [fax](fax.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Fax|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_usersettings"></a> transactioncurrency_usersettings

Same as the [transactioncurrency_usersettings](usersettings.md#BKMK_transactioncurrency_usersettings) many-to-one relationship for the [usersettings](usersettings.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|usersettings|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_usersettings|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_ActivityPointer"></a> TransactionCurrency_ActivityPointer

Same as the [TransactionCurrency_ActivityPointer](activitypointer.md#BKMK_TransactionCurrency_ActivityPointer) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_ActivityPointer|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_category"></a> transactioncurrency_category

Same as the [transactioncurrency_category](category.md#BKMK_transactioncurrency_category) many-to-one relationship for the [category](category.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|category|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_category|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_position"></a> transactioncurrency_position

Same as the [transactioncurrency_position](position.md#BKMK_transactioncurrency_position) many-to-one relationship for the [position](position.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|position|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_position|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Task"></a> TransactionCurrency_Task

Same as the [TransactionCurrency_Task](task.md#BKMK_TransactionCurrency_Task) many-to-one relationship for the [task](task.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Task|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_SLA"></a> TransactionCurrency_SLA

Same as the [TransactionCurrency_SLA](sla.md#BKMK_TransactionCurrency_SLA) many-to-one relationship for the [sla](sla.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_SLA|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_basecurrency_organization"></a> basecurrency_organization

Same as the [basecurrency_organization](organization.md#BKMK_basecurrency_organization) many-to-one relationship for the [organization](organization.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|basecurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|basecurrency_organization|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Letter"></a> TransactionCurrency_Letter

Same as the [TransactionCurrency_Letter](letter.md#BKMK_TransactionCurrency_Letter) many-to-one relationship for the [letter](letter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Letter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_SystemUser"></a> TransactionCurrency_SystemUser

Same as the [TransactionCurrency_SystemUser](systemuser.md#BKMK_TransactionCurrency_SystemUser) many-to-one relationship for the [systemuser](systemuser.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_SystemUser|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Team"></a> TransactionCurrency_Team

Same as the [TransactionCurrency_Team](team.md#BKMK_TransactionCurrency_Team) many-to-one relationship for the [team](team.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Team|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Email"></a> TransactionCurrency_Email

Same as the [TransactionCurrency_Email](email.md#BKMK_TransactionCurrency_Email) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Email|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_BusinessUnit"></a> TransactionCurrency_BusinessUnit

Same as the [TransactionCurrency_BusinessUnit](businessunit.md#BKMK_TransactionCurrency_BusinessUnit) many-to-one relationship for the [businessunit](businessunit.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunit|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_BusinessUnit|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_SocialProfile"></a> transactioncurrency_SocialProfile

Same as the [transactioncurrency_SocialProfile](socialprofile.md#BKMK_transactioncurrency_SocialProfile) many-to-one relationship for the [socialprofile](socialprofile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialprofile|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_SocialProfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Queue"></a> TransactionCurrency_Queue

Same as the [TransactionCurrency_Queue](queue.md#BKMK_TransactionCurrency_Queue) many-to-one relationship for the [queue](queue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Queue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_DuplicateMatchingRecord"></a> TransactionCurrency_DuplicateMatchingRecord

Same as the [TransactionCurrency_DuplicateMatchingRecord](duplicaterecord.md#BKMK_TransactionCurrency_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Appointment"></a> TransactionCurrency_Appointment

Same as the [TransactionCurrency_Appointment](appointment.md#BKMK_TransactionCurrency_Appointment) many-to-one relationship for the [appointment](appointment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Appointment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_quarterlyfiscalcalendar"></a> transactioncurrency_quarterlyfiscalcalendar

Same as the [transactioncurrency_quarterlyfiscalcalendar](quarterlyfiscalcalendar.md#BKMK_transactioncurrency_quarterlyfiscalcalendar) many-to-one relationship for the [quarterlyfiscalcalendar](quarterlyfiscalcalendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|quarterlyfiscalcalendar|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_quarterlyfiscalcalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_KbArticle"></a> TransactionCurrency_KbArticle

Same as the [TransactionCurrency_KbArticle](kbarticle.md#BKMK_TransactionCurrency_KbArticle) many-to-one relationship for the [kbarticle](kbarticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|kbarticle|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_KbArticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_monthlyfiscalcalendar"></a> transactioncurrency_monthlyfiscalcalendar

Same as the [transactioncurrency_monthlyfiscalcalendar](monthlyfiscalcalendar.md#BKMK_transactioncurrency_monthlyfiscalcalendar) many-to-one relationship for the [monthlyfiscalcalendar](monthlyfiscalcalendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|monthlyfiscalcalendar|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_monthlyfiscalcalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_CustomerAddress"></a> TransactionCurrency_CustomerAddress

Same as the [TransactionCurrency_CustomerAddress](customeraddress.md#BKMK_TransactionCurrency_CustomerAddress) many-to-one relationship for the [customeraddress](customeraddress.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|customeraddress|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_CustomerAddress|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_annualfiscalcalendar"></a> transactioncurrency_annualfiscalcalendar

Same as the [transactioncurrency_annualfiscalcalendar](annualfiscalcalendar.md#BKMK_transactioncurrency_annualfiscalcalendar) many-to-one relationship for the [annualfiscalcalendar](annualfiscalcalendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|annualfiscalcalendar|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_annualfiscalcalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Connection"></a> TransactionCurrency_Connection

Same as the [TransactionCurrency_Connection](connection.md#BKMK_TransactionCurrency_Connection) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Connection|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_translationprocess"></a> transactioncurrency_translationprocess

Same as the [transactioncurrency_translationprocess](translationprocess.md#BKMK_transactioncurrency_translationprocess) many-to-one relationship for the [translationprocess](translationprocess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_translationprocess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_feedback"></a> transactioncurrency_feedback

Same as the [transactioncurrency_feedback](feedback.md#BKMK_transactioncurrency_feedback) many-to-one relationship for the [feedback](feedback.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_feedback|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_contact"></a> transactioncurrency_contact

Same as the [transactioncurrency_contact](contact.md#BKMK_transactioncurrency_contact) many-to-one relationship for the [contact](contact.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_contact|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_ReportCategory"></a> TransactionCurrency_ReportCategory

Same as the [TransactionCurrency_ReportCategory](reportcategory.md#BKMK_TransactionCurrency_ReportCategory) many-to-one relationship for the [reportcategory](reportcategory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|reportcategory|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_ReportCategory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_InteractionForEmail"></a> TransactionCurrency_InteractionForEmail

Same as the [TransactionCurrency_InteractionForEmail](interactionforemail.md#BKMK_TransactionCurrency_InteractionForEmail) many-to-one relationship for the [interactionforemail](interactionforemail.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_InteractionForEmail|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_slakpiinstance"></a> TransactionCurrency_slakpiinstance

Same as the [TransactionCurrency_slakpiinstance](slakpiinstance.md#BKMK_TransactionCurrency_slakpiinstance) many-to-one relationship for the [slakpiinstance](slakpiinstance.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_slakpiinstance|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_DuplicateBaseRecord"></a> TransactionCurrency_DuplicateBaseRecord

Same as the [TransactionCurrency_DuplicateBaseRecord](duplicaterecord.md#BKMK_TransactionCurrency_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_AsyncOperations"></a> TransactionCurrency_AsyncOperations

Same as the [TransactionCurrency_AsyncOperations](asyncoperation.md#BKMK_TransactionCurrency_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_knowledgearticleviews"></a> transactioncurrency_knowledgearticleviews

Same as the [transactioncurrency_knowledgearticleviews](knowledgearticleviews.md#BKMK_transactioncurrency_knowledgearticleviews) many-to-one relationship for the [knowledgearticleviews](knowledgearticleviews.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticleviews|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_knowledgearticleviews|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Theme"></a> TransactionCurrency_Theme

Same as the [TransactionCurrency_Theme](theme.md#BKMK_TransactionCurrency_Theme) many-to-one relationship for the [theme](theme.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|theme|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Theme|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_newprocess"></a> transactioncurrency_newprocess

Same as the [transactioncurrency_newprocess](newprocess.md#BKMK_transactioncurrency_newprocess) many-to-one relationship for the [newprocess](newprocess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_newprocess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_knowledgearticle"></a> TransactionCurrency_knowledgearticle

Same as the [TransactionCurrency_knowledgearticle](knowledgearticle.md#BKMK_TransactionCurrency_knowledgearticle) many-to-one relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_knowledgearticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_RecurringAppointmentMaster"></a> TransactionCurrency_RecurringAppointmentMaster

Same as the [TransactionCurrency_RecurringAppointmentMaster](recurringappointmentmaster.md#BKMK_TransactionCurrency_RecurringAppointmentMaster) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_RecurringAppointmentMaster|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_transactioncurrency_account"></a> transactioncurrency_account

Same as the [transactioncurrency_account](account.md#BKMK_transactioncurrency_account) many-to-one relationship for the [account](account.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|transactioncurrency_account|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_recommendeddocument"></a> TransactionCurrency_recommendeddocument

Same as the [TransactionCurrency_recommendeddocument](recommendeddocument.md#BKMK_TransactionCurrency_recommendeddocument) many-to-one relationship for the [recommendeddocument](recommendeddocument.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recommendeddocument|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_recommendeddocument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_TransactionCurrency_Territory"></a> TransactionCurrency_Territory

**Added by**: Application Common Solution

Same as the [TransactionCurrency_Territory](territory.md#BKMK_TransactionCurrency_Territory) many-to-one relationship for the [territory](territory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|territory|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|TransactionCurrency_Territory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_chat_transactioncurrency_transactioncurrencyid"></a> chat_transactioncurrency_transactioncurrencyid

**Added by**: Activities Patch Solution

Same as the [chat_transactioncurrency_transactioncurrencyid](chat.md#BKMK_chat_transactioncurrency_transactioncurrencyid) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|transactioncurrencyid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|chat_transactioncurrency_transactioncurrencyid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_transactioncurrencybase_createdby](#BKMK_lk_transactioncurrencybase_createdby)
- [lk_transactioncurrencybase_modifiedby](#BKMK_lk_transactioncurrencybase_modifiedby)
- [lk_transactioncurrency_modifiedonbehalfby](#BKMK_lk_transactioncurrency_modifiedonbehalfby)
- [organization_transactioncurrencies](#BKMK_organization_transactioncurrencies)
- [lk_transactioncurrency_createdonbehalfby](#BKMK_lk_transactioncurrency_createdonbehalfby)


### <a name="BKMK_lk_transactioncurrencybase_createdby"></a> lk_transactioncurrencybase_createdby

See the [lk_transactioncurrencybase_createdby](systemuser.md#BKMK_lk_transactioncurrencybase_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_transactioncurrencybase_modifiedby"></a> lk_transactioncurrencybase_modifiedby

See the [lk_transactioncurrencybase_modifiedby](systemuser.md#BKMK_lk_transactioncurrencybase_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_transactioncurrency_modifiedonbehalfby"></a> lk_transactioncurrency_modifiedonbehalfby

See the [lk_transactioncurrency_modifiedonbehalfby](systemuser.md#BKMK_lk_transactioncurrency_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_transactioncurrencies"></a> organization_transactioncurrencies

See the [organization_transactioncurrencies](organization.md#BKMK_organization_transactioncurrencies) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_lk_transactioncurrency_createdonbehalfby"></a> lk_transactioncurrency_createdonbehalfby

See the [lk_transactioncurrency_createdonbehalfby](systemuser.md#BKMK_lk_transactioncurrency_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.transactioncurrency?text=transactioncurrency EntityType" />