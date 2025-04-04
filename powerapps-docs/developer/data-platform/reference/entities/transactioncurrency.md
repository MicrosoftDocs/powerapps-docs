---
title: "Currency (TransactionCurrency) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Currency (TransactionCurrency) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Currency (TransactionCurrency) table/entity reference (Microsoft Dataverse)

Currency in which a financial transaction is carried out.

## Messages

The following table lists the messages for the Currency (TransactionCurrency) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /transactioncurrencies<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /transactioncurrencies(*transactioncurrencyid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /transactioncurrencies(*transactioncurrencyid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveExchangeRate`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveExchangeRate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveExchangeRateRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /transactioncurrencies<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /transactioncurrencies(*transactioncurrencyid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /transactioncurrencies(*transactioncurrencyid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /transactioncurrencies(*transactioncurrencyid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Currency (TransactionCurrency) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Currency** |
| **DisplayCollectionName** | **Currencies** |
| **SchemaName** | `TransactionCurrency` |
| **CollectionSchemaName** | `TransactionCurrencies` |
| **EntitySetName** | `transactioncurrencies`|
| **LogicalName** | `transactioncurrency` |
| **LogicalCollectionName** | `transactioncurrencies` |
| **PrimaryIdAttribute** | `transactioncurrencyid` |
| **PrimaryNameAttribute** |`currencyname` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CurrencyName](#BKMK_CurrencyName)
- [CurrencyPrecision](#BKMK_CurrencyPrecision)
- [CurrencySymbol](#BKMK_CurrencySymbol)
- [CurrencyType](#BKMK_CurrencyType)
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
|---|---|
|Description|**Name of the transaction currency.**|
|DisplayName|**Currency Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`currencyname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CurrencyPrecision"></a> CurrencyPrecision

|Property|Value|
|---|---|
|Description|**Number of decimal places that can be used for currency.**|
|DisplayName|**Currency Precision**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`currencyprecision`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|10|
|MinValue|0|

### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

|Property|Value|
|---|---|
|Description|**Symbol for the transaction currency.**|
|DisplayName|**Currency Symbol**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`currencysymbol`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

### <a name="BKMK_CurrencyType"></a> CurrencyType

|Property|Value|
|---|---|
|Description|**Currency type that can be used for new currency.**|
|DisplayName|**Currency Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`currencytype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`transactioncurrency_currencytype`|

#### CurrencyType Choices/Options

|Value|Label|
|---|---|
|0|**System**|
|1|**Custom**|

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

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate between the transaction currency and the base currency.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|SystemRequired|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

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

### <a name="BKMK_ISOCurrencyCode"></a> ISOCurrencyCode

|Property|Value|
|---|---|
|Description|**ISO currency code for the transaction currency.**|
|DisplayName|**Currency Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isocurrencycode`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

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

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the transaction currency.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`transactioncurrency_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the transaction currency.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`transactioncurrency_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the transaction currency.**|
|DisplayName|**Transaction Currency**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [UniqueDscId](#BKMK_UniqueDscId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the transaction currency.**|
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
|Description|**Date and time when the transaction currency was created.**|
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
|Description|**Unique identifier of the delegate user who created the transactioncurrency.**|
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

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the transaction currency.**|
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
|Description|**Date and time when the transaction currency was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the transactioncurrency.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the transaction currency.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_UniqueDscId"></a> UniqueDscId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**UniqueDscId**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`uniquedscid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the transaction currency.**|
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

- [lk_transactioncurrency_createdonbehalfby](#BKMK_lk_transactioncurrency_createdonbehalfby)
- [lk_transactioncurrency_modifiedonbehalfby](#BKMK_lk_transactioncurrency_modifiedonbehalfby)
- [lk_transactioncurrencybase_createdby](#BKMK_lk_transactioncurrencybase_createdby)
- [lk_transactioncurrencybase_modifiedby](#BKMK_lk_transactioncurrencybase_modifiedby)
- [organization_transactioncurrencies](#BKMK_organization_transactioncurrencies)

### <a name="BKMK_lk_transactioncurrency_createdonbehalfby"></a> lk_transactioncurrency_createdonbehalfby

One-To-Many Relationship: [systemuser lk_transactioncurrency_createdonbehalfby](systemuser.md#BKMK_lk_transactioncurrency_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_transactioncurrency_modifiedonbehalfby"></a> lk_transactioncurrency_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_transactioncurrency_modifiedonbehalfby](systemuser.md#BKMK_lk_transactioncurrency_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_transactioncurrencybase_createdby"></a> lk_transactioncurrencybase_createdby

One-To-Many Relationship: [systemuser lk_transactioncurrencybase_createdby](systemuser.md#BKMK_lk_transactioncurrencybase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_transactioncurrencybase_modifiedby"></a> lk_transactioncurrencybase_modifiedby

One-To-Many Relationship: [systemuser lk_transactioncurrencybase_modifiedby](systemuser.md#BKMK_lk_transactioncurrencybase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_transactioncurrencies"></a> organization_transactioncurrencies

One-To-Many Relationship: [organization organization_transactioncurrencies](organization.md#BKMK_organization_transactioncurrencies)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [adx_inviteredemption_transactioncurrency_transactioncurrencyid](#BKMK_adx_inviteredemption_transactioncurrency_transactioncurrencyid)
- [adx_portalcomment_transactioncurrency_transactioncurrencyid](#BKMK_adx_portalcomment_transactioncurrency_transactioncurrencyid)
- [basecurrency_organization](#BKMK_basecurrency_organization)
- [chat_transactioncurrency_transactioncurrencyid](#BKMK_chat_transactioncurrency_transactioncurrencyid)
- [transactioncurrency_account](#BKMK_transactioncurrency_account)
- [transactioncurrency_actioncard](#BKMK_transactioncurrency_actioncard)
- [TransactionCurrency_ActionCardUserState](#BKMK_TransactionCurrency_ActionCardUserState)
- [TransactionCurrency_ActivityPointer](#BKMK_TransactionCurrency_ActivityPointer)
- [transactioncurrency_annualfiscalcalendar](#BKMK_transactioncurrency_annualfiscalcalendar)
- [TransactionCurrency_Appointment](#BKMK_TransactionCurrency_Appointment)
- [TransactionCurrency_AsyncOperations](#BKMK_TransactionCurrency_AsyncOperations)
- [TransactionCurrency_BusinessUnit](#BKMK_TransactionCurrency_BusinessUnit)
- [transactioncurrency_category](#BKMK_transactioncurrency_category)
- [TransactionCurrency_Connection](#BKMK_TransactionCurrency_Connection)
- [transactioncurrency_contact](#BKMK_transactioncurrency_contact)
- [TransactionCurrency_CustomerAddress](#BKMK_TransactionCurrency_CustomerAddress)
- [TransactionCurrency_DuplicateBaseRecord](#BKMK_TransactionCurrency_DuplicateBaseRecord)
- [TransactionCurrency_DuplicateMatchingRecord](#BKMK_TransactionCurrency_DuplicateMatchingRecord)
- [TransactionCurrency_Email](#BKMK_TransactionCurrency_Email)
- [transactioncurrency_expiredprocess](#BKMK_transactioncurrency_expiredprocess)
- [TransactionCurrency_Fax](#BKMK_TransactionCurrency_Fax)
- [transactioncurrency_feedback](#BKMK_transactioncurrency_feedback)
- [transactioncurrency_fixedmonthlyfiscalcalendar](#BKMK_transactioncurrency_fixedmonthlyfiscalcalendar)
- [TransactionCurrency_Goal](#BKMK_TransactionCurrency_Goal)
- [TransactionCurrency_InteractionForEmail](#BKMK_TransactionCurrency_InteractionForEmail)
- [TransactionCurrency_KbArticle](#BKMK_TransactionCurrency_KbArticle)
- [TransactionCurrency_knowledgearticle](#BKMK_TransactionCurrency_knowledgearticle)
- [transactioncurrency_knowledgearticleviews](#BKMK_transactioncurrency_knowledgearticleviews)
- [TransactionCurrency_KnowledgeBaseRecord](#BKMK_TransactionCurrency_KnowledgeBaseRecord)
- [TransactionCurrency_Letter](#BKMK_TransactionCurrency_Letter)
- [TransactionCurrency_MailMergeTemplate](#BKMK_TransactionCurrency_MailMergeTemplate)
- [transactioncurrency_monthlyfiscalcalendar](#BKMK_transactioncurrency_monthlyfiscalcalendar)
- [transactioncurrency_newprocess](#BKMK_transactioncurrency_newprocess)
- [TransactionCurrency_officegraphdocument](#BKMK_TransactionCurrency_officegraphdocument)
- [TransactionCurrency_PhoneCall](#BKMK_TransactionCurrency_PhoneCall)
- [transactioncurrency_position](#BKMK_transactioncurrency_position)
- [TransactionCurrency_ProcessSessions](#BKMK_TransactionCurrency_ProcessSessions)
- [transactioncurrency_quarterlyfiscalcalendar](#BKMK_transactioncurrency_quarterlyfiscalcalendar)
- [TransactionCurrency_Queue](#BKMK_TransactionCurrency_Queue)
- [TransactionCurrency_QueueItem](#BKMK_TransactionCurrency_QueueItem)
- [TransactionCurrency_recommendeddocument](#BKMK_TransactionCurrency_recommendeddocument)
- [TransactionCurrency_RecurringAppointmentMaster](#BKMK_TransactionCurrency_RecurringAppointmentMaster)
- [TransactionCurrency_ReportCategory](#BKMK_TransactionCurrency_ReportCategory)
- [transactioncurrency_semiannualfiscalcalendar](#BKMK_transactioncurrency_semiannualfiscalcalendar)
- [TransactionCurrency_SharePointDocumentLocation](#BKMK_TransactionCurrency_SharePointDocumentLocation)
- [TransactionCurrency_SharePointSite](#BKMK_TransactionCurrency_SharePointSite)
- [TransactionCurrency_SimilarityRule](#BKMK_TransactionCurrency_SimilarityRule)
- [TransactionCurrency_SLA](#BKMK_TransactionCurrency_SLA)
- [TransactionCurrency_SLAItem](#BKMK_TransactionCurrency_SLAItem)
- [TransactionCurrency_slakpiinstance](#BKMK_TransactionCurrency_slakpiinstance)
- [transactioncurrency_socialactivity](#BKMK_transactioncurrency_socialactivity)
- [transactioncurrency_SocialProfile](#BKMK_transactioncurrency_SocialProfile)
- [TransactionCurrency_SyncErrors](#BKMK_TransactionCurrency_SyncErrors)
- [TransactionCurrency_SystemUser](#BKMK_TransactionCurrency_SystemUser)
- [TransactionCurrency_Task](#BKMK_TransactionCurrency_Task)
- [TransactionCurrency_Team](#BKMK_TransactionCurrency_Team)
- [TransactionCurrency_Territory](#BKMK_TransactionCurrency_Territory)
- [TransactionCurrency_Theme](#BKMK_TransactionCurrency_Theme)
- [transactioncurrency_translationprocess](#BKMK_transactioncurrency_translationprocess)
- [TransactionCurrency_UserMapping](#BKMK_TransactionCurrency_UserMapping)
- [transactioncurrency_usersettings](#BKMK_transactioncurrency_usersettings)

### <a name="BKMK_adx_inviteredemption_transactioncurrency_transactioncurrencyid"></a> adx_inviteredemption_transactioncurrency_transactioncurrencyid

Many-To-One Relationship: [adx_inviteredemption adx_inviteredemption_transactioncurrency_transactioncurrencyid](adx_inviteredemption.md#BKMK_adx_inviteredemption_transactioncurrency_transactioncurrencyid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`adx_inviteredemption_transactioncurrency_transactioncurrencyid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_portalcomment_transactioncurrency_transactioncurrencyid"></a> adx_portalcomment_transactioncurrency_transactioncurrencyid

Many-To-One Relationship: [adx_portalcomment adx_portalcomment_transactioncurrency_transactioncurrencyid](adx_portalcomment.md#BKMK_adx_portalcomment_transactioncurrency_transactioncurrencyid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`adx_portalcomment_transactioncurrency_transactioncurrencyid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_basecurrency_organization"></a> basecurrency_organization

Many-To-One Relationship: [organization basecurrency_organization](organization.md#BKMK_basecurrency_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`organization`|
|ReferencingAttribute|`basecurrencyid`|
|ReferencedEntityNavigationPropertyName|`basecurrency_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_chat_transactioncurrency_transactioncurrencyid"></a> chat_transactioncurrency_transactioncurrencyid

Many-To-One Relationship: [chat chat_transactioncurrency_transactioncurrencyid](chat.md#BKMK_chat_transactioncurrency_transactioncurrencyid)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`chat_transactioncurrency_transactioncurrencyid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_account"></a> transactioncurrency_account

Many-To-One Relationship: [account transactioncurrency_account](account.md#BKMK_transactioncurrency_account)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_account`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_actioncard"></a> transactioncurrency_actioncard

Many-To-One Relationship: [actioncard transactioncurrency_actioncard](actioncard.md#BKMK_transactioncurrency_actioncard)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_actioncard`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_ActionCardUserState"></a> TransactionCurrency_ActionCardUserState

Many-To-One Relationship: [actioncarduserstate TransactionCurrency_ActionCardUserState](actioncarduserstate.md#BKMK_TransactionCurrency_ActionCardUserState)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncarduserstate`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_ActionCardUserState`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_ActivityPointer"></a> TransactionCurrency_ActivityPointer

Many-To-One Relationship: [activitypointer TransactionCurrency_ActivityPointer](activitypointer.md#BKMK_TransactionCurrency_ActivityPointer)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_ActivityPointer`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_annualfiscalcalendar"></a> transactioncurrency_annualfiscalcalendar

Many-To-One Relationship: [annualfiscalcalendar transactioncurrency_annualfiscalcalendar](annualfiscalcalendar.md#BKMK_transactioncurrency_annualfiscalcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`annualfiscalcalendar`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_annualfiscalcalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Appointment"></a> TransactionCurrency_Appointment

Many-To-One Relationship: [appointment TransactionCurrency_Appointment](appointment.md#BKMK_TransactionCurrency_Appointment)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Appointment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_AsyncOperations"></a> TransactionCurrency_AsyncOperations

Many-To-One Relationship: [asyncoperation TransactionCurrency_AsyncOperations](asyncoperation.md#BKMK_TransactionCurrency_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_BusinessUnit"></a> TransactionCurrency_BusinessUnit

Many-To-One Relationship: [businessunit TransactionCurrency_BusinessUnit](businessunit.md#BKMK_TransactionCurrency_BusinessUnit)

|Property|Value|
|---|---|
|ReferencingEntity|`businessunit`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_BusinessUnit`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_category"></a> transactioncurrency_category

Many-To-One Relationship: [category transactioncurrency_category](category.md#BKMK_transactioncurrency_category)

|Property|Value|
|---|---|
|ReferencingEntity|`category`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_category`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Connection"></a> TransactionCurrency_Connection

Many-To-One Relationship: [connection TransactionCurrency_Connection](connection.md#BKMK_TransactionCurrency_Connection)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Connection`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_contact"></a> transactioncurrency_contact

Many-To-One Relationship: [contact transactioncurrency_contact](contact.md#BKMK_transactioncurrency_contact)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_contact`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_CustomerAddress"></a> TransactionCurrency_CustomerAddress

Many-To-One Relationship: [customeraddress TransactionCurrency_CustomerAddress](customeraddress.md#BKMK_TransactionCurrency_CustomerAddress)

|Property|Value|
|---|---|
|ReferencingEntity|`customeraddress`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_CustomerAddress`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_DuplicateBaseRecord"></a> TransactionCurrency_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord TransactionCurrency_DuplicateBaseRecord](duplicaterecord.md#BKMK_TransactionCurrency_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_DuplicateMatchingRecord"></a> TransactionCurrency_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord TransactionCurrency_DuplicateMatchingRecord](duplicaterecord.md#BKMK_TransactionCurrency_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Email"></a> TransactionCurrency_Email

Many-To-One Relationship: [email TransactionCurrency_Email](email.md#BKMK_TransactionCurrency_Email)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Email`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_expiredprocess"></a> transactioncurrency_expiredprocess

Many-To-One Relationship: [expiredprocess transactioncurrency_expiredprocess](expiredprocess.md#BKMK_transactioncurrency_expiredprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`expiredprocess`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_expiredprocess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Fax"></a> TransactionCurrency_Fax

Many-To-One Relationship: [fax TransactionCurrency_Fax](fax.md#BKMK_TransactionCurrency_Fax)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Fax`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_feedback"></a> transactioncurrency_feedback

Many-To-One Relationship: [feedback transactioncurrency_feedback](feedback.md#BKMK_transactioncurrency_feedback)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_feedback`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_fixedmonthlyfiscalcalendar"></a> transactioncurrency_fixedmonthlyfiscalcalendar

Many-To-One Relationship: [fixedmonthlyfiscalcalendar transactioncurrency_fixedmonthlyfiscalcalendar](fixedmonthlyfiscalcalendar.md#BKMK_transactioncurrency_fixedmonthlyfiscalcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`fixedmonthlyfiscalcalendar`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_fixedmonthlyfiscalcalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Goal"></a> TransactionCurrency_Goal

Many-To-One Relationship: [goal TransactionCurrency_Goal](goal.md#BKMK_TransactionCurrency_Goal)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Goal`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_InteractionForEmail"></a> TransactionCurrency_InteractionForEmail

Many-To-One Relationship: [interactionforemail TransactionCurrency_InteractionForEmail](interactionforemail.md#BKMK_TransactionCurrency_InteractionForEmail)

|Property|Value|
|---|---|
|ReferencingEntity|`interactionforemail`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_InteractionForEmail`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_KbArticle"></a> TransactionCurrency_KbArticle

Many-To-One Relationship: [kbarticle TransactionCurrency_KbArticle](kbarticle.md#BKMK_TransactionCurrency_KbArticle)

|Property|Value|
|---|---|
|ReferencingEntity|`kbarticle`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_KbArticle`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_knowledgearticle"></a> TransactionCurrency_knowledgearticle

Many-To-One Relationship: [knowledgearticle TransactionCurrency_knowledgearticle](knowledgearticle.md#BKMK_TransactionCurrency_knowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_knowledgearticle`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_knowledgearticleviews"></a> transactioncurrency_knowledgearticleviews

Many-To-One Relationship: [knowledgearticleviews transactioncurrency_knowledgearticleviews](knowledgearticleviews.md#BKMK_transactioncurrency_knowledgearticleviews)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticleviews`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_knowledgearticleviews`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_KnowledgeBaseRecord"></a> TransactionCurrency_KnowledgeBaseRecord

Many-To-One Relationship: [knowledgebaserecord TransactionCurrency_KnowledgeBaseRecord](knowledgebaserecord.md#BKMK_TransactionCurrency_KnowledgeBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgebaserecord`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_KnowledgeBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Letter"></a> TransactionCurrency_Letter

Many-To-One Relationship: [letter TransactionCurrency_Letter](letter.md#BKMK_TransactionCurrency_Letter)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Letter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_MailMergeTemplate"></a> TransactionCurrency_MailMergeTemplate

Many-To-One Relationship: [mailmergetemplate TransactionCurrency_MailMergeTemplate](mailmergetemplate.md#BKMK_TransactionCurrency_MailMergeTemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`mailmergetemplate`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_MailMergeTemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_monthlyfiscalcalendar"></a> transactioncurrency_monthlyfiscalcalendar

Many-To-One Relationship: [monthlyfiscalcalendar transactioncurrency_monthlyfiscalcalendar](monthlyfiscalcalendar.md#BKMK_transactioncurrency_monthlyfiscalcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`monthlyfiscalcalendar`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_monthlyfiscalcalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_newprocess"></a> transactioncurrency_newprocess

Many-To-One Relationship: [newprocess transactioncurrency_newprocess](newprocess.md#BKMK_transactioncurrency_newprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`newprocess`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_newprocess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_officegraphdocument"></a> TransactionCurrency_officegraphdocument

Many-To-One Relationship: [officegraphdocument TransactionCurrency_officegraphdocument](officegraphdocument.md#BKMK_TransactionCurrency_officegraphdocument)

|Property|Value|
|---|---|
|ReferencingEntity|`officegraphdocument`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_officegraphdocument`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_PhoneCall"></a> TransactionCurrency_PhoneCall

Many-To-One Relationship: [phonecall TransactionCurrency_PhoneCall](phonecall.md#BKMK_TransactionCurrency_PhoneCall)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_PhoneCall`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_position"></a> transactioncurrency_position

Many-To-One Relationship: [position transactioncurrency_position](position.md#BKMK_transactioncurrency_position)

|Property|Value|
|---|---|
|ReferencingEntity|`position`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_position`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_ProcessSessions"></a> TransactionCurrency_ProcessSessions

Many-To-One Relationship: [processsession TransactionCurrency_ProcessSessions](processsession.md#BKMK_TransactionCurrency_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_quarterlyfiscalcalendar"></a> transactioncurrency_quarterlyfiscalcalendar

Many-To-One Relationship: [quarterlyfiscalcalendar transactioncurrency_quarterlyfiscalcalendar](quarterlyfiscalcalendar.md#BKMK_transactioncurrency_quarterlyfiscalcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`quarterlyfiscalcalendar`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_quarterlyfiscalcalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Queue"></a> TransactionCurrency_Queue

Many-To-One Relationship: [queue TransactionCurrency_Queue](queue.md#BKMK_TransactionCurrency_Queue)

|Property|Value|
|---|---|
|ReferencingEntity|`queue`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Queue`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_QueueItem"></a> TransactionCurrency_QueueItem

Many-To-One Relationship: [queueitem TransactionCurrency_QueueItem](queueitem.md#BKMK_TransactionCurrency_QueueItem)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_QueueItem`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_recommendeddocument"></a> TransactionCurrency_recommendeddocument

Many-To-One Relationship: [recommendeddocument TransactionCurrency_recommendeddocument](recommendeddocument.md#BKMK_TransactionCurrency_recommendeddocument)

|Property|Value|
|---|---|
|ReferencingEntity|`recommendeddocument`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_recommendeddocument`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_RecurringAppointmentMaster"></a> TransactionCurrency_RecurringAppointmentMaster

Many-To-One Relationship: [recurringappointmentmaster TransactionCurrency_RecurringAppointmentMaster](recurringappointmentmaster.md#BKMK_TransactionCurrency_RecurringAppointmentMaster)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_RecurringAppointmentMaster`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_ReportCategory"></a> TransactionCurrency_ReportCategory

Many-To-One Relationship: [reportcategory TransactionCurrency_ReportCategory](reportcategory.md#BKMK_TransactionCurrency_ReportCategory)

|Property|Value|
|---|---|
|ReferencingEntity|`reportcategory`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_ReportCategory`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_semiannualfiscalcalendar"></a> transactioncurrency_semiannualfiscalcalendar

Many-To-One Relationship: [semiannualfiscalcalendar transactioncurrency_semiannualfiscalcalendar](semiannualfiscalcalendar.md#BKMK_transactioncurrency_semiannualfiscalcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`semiannualfiscalcalendar`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_semiannualfiscalcalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_SharePointDocumentLocation"></a> TransactionCurrency_SharePointDocumentLocation

Many-To-One Relationship: [sharepointdocumentlocation TransactionCurrency_SharePointDocumentLocation](sharepointdocumentlocation.md#BKMK_TransactionCurrency_SharePointDocumentLocation)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_SharePointDocumentLocation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_SharePointSite"></a> TransactionCurrency_SharePointSite

Many-To-One Relationship: [sharepointsite TransactionCurrency_SharePointSite](sharepointsite.md#BKMK_TransactionCurrency_SharePointSite)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointsite`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_SharePointSite`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_SimilarityRule"></a> TransactionCurrency_SimilarityRule

Many-To-One Relationship: [similarityrule TransactionCurrency_SimilarityRule](similarityrule.md#BKMK_TransactionCurrency_SimilarityRule)

|Property|Value|
|---|---|
|ReferencingEntity|`similarityrule`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_SimilarityRule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_SLA"></a> TransactionCurrency_SLA

Many-To-One Relationship: [sla TransactionCurrency_SLA](sla.md#BKMK_TransactionCurrency_SLA)

|Property|Value|
|---|---|
|ReferencingEntity|`sla`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_SLA`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_SLAItem"></a> TransactionCurrency_SLAItem

Many-To-One Relationship: [slaitem TransactionCurrency_SLAItem](slaitem.md#BKMK_TransactionCurrency_SLAItem)

|Property|Value|
|---|---|
|ReferencingEntity|`slaitem`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_SLAItem`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_slakpiinstance"></a> TransactionCurrency_slakpiinstance

Many-To-One Relationship: [slakpiinstance TransactionCurrency_slakpiinstance](slakpiinstance.md#BKMK_TransactionCurrency_slakpiinstance)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_slakpiinstance`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_socialactivity"></a> transactioncurrency_socialactivity

Many-To-One Relationship: [socialactivity transactioncurrency_socialactivity](socialactivity.md#BKMK_transactioncurrency_socialactivity)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_socialactivity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_SocialProfile"></a> transactioncurrency_SocialProfile

Many-To-One Relationship: [socialprofile transactioncurrency_SocialProfile](socialprofile.md#BKMK_transactioncurrency_SocialProfile)

|Property|Value|
|---|---|
|ReferencingEntity|`socialprofile`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_SocialProfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_SyncErrors"></a> TransactionCurrency_SyncErrors

Many-To-One Relationship: [syncerror TransactionCurrency_SyncErrors](syncerror.md#BKMK_TransactionCurrency_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_SystemUser"></a> TransactionCurrency_SystemUser

Many-To-One Relationship: [systemuser TransactionCurrency_SystemUser](systemuser.md#BKMK_TransactionCurrency_SystemUser)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_SystemUser`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Task"></a> TransactionCurrency_Task

Many-To-One Relationship: [task TransactionCurrency_Task](task.md#BKMK_TransactionCurrency_Task)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Task`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Team"></a> TransactionCurrency_Team

Many-To-One Relationship: [team TransactionCurrency_Team](team.md#BKMK_TransactionCurrency_Team)

|Property|Value|
|---|---|
|ReferencingEntity|`team`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Team`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Territory"></a> TransactionCurrency_Territory

Many-To-One Relationship: [territory TransactionCurrency_Territory](territory.md#BKMK_TransactionCurrency_Territory)

|Property|Value|
|---|---|
|ReferencingEntity|`territory`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Territory`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_Theme"></a> TransactionCurrency_Theme

Many-To-One Relationship: [theme TransactionCurrency_Theme](theme.md#BKMK_TransactionCurrency_Theme)

|Property|Value|
|---|---|
|ReferencingEntity|`theme`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_Theme`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_translationprocess"></a> transactioncurrency_translationprocess

Many-To-One Relationship: [translationprocess transactioncurrency_translationprocess](translationprocess.md#BKMK_transactioncurrency_translationprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`translationprocess`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_translationprocess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TransactionCurrency_UserMapping"></a> TransactionCurrency_UserMapping

Many-To-One Relationship: [usermapping TransactionCurrency_UserMapping](usermapping.md#BKMK_TransactionCurrency_UserMapping)

|Property|Value|
|---|---|
|ReferencingEntity|`usermapping`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`TransactionCurrency_UserMapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_transactioncurrency_usersettings"></a> transactioncurrency_usersettings

Many-To-One Relationship: [usersettings transactioncurrency_usersettings](usersettings.md#BKMK_transactioncurrency_usersettings)

|Property|Value|
|---|---|
|ReferencingEntity|`usersettings`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencedEntityNavigationPropertyName|`transactioncurrency_usersettings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.transactioncurrency?displayProperty=fullName>
