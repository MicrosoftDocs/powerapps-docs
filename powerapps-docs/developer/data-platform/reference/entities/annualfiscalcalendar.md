---
title: "AnnualFiscalCalendar table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the AnnualFiscalCalendar table/entity."
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

# AnnualFiscalCalendar table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Year long fiscal calendar of an organization. A span of time during which the financial activities of an organization are calculated.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/annualfiscalcalendars<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/annualfiscalcalendars(*userfiscalcalendarid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/annualfiscalcalendars(*userfiscalcalendarid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/annualfiscalcalendars<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/annualfiscalcalendars(*userfiscalcalendarid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|AnnualFiscalCalendars|
|DisplayCollectionName|Annual Fiscal Calendars|
|DisplayName|Annual Fiscal Calendar|
|EntitySetName|annualfiscalcalendars|
|IsBPFEntity|False|
|LogicalCollectionName|annualfiscalcalendars|
|LogicalName|annualfiscalcalendar|
|OwnershipType|None|
|PrimaryIdAttribute|userfiscalcalendarid|
|PrimaryNameAttribute||
|SchemaName|AnnualFiscalCalendar|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EffectiveOn](#BKMK_EffectiveOn)
- [Period1](#BKMK_Period1)
- [SalesPersonId](#BKMK_SalesPersonId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UserFiscalCalendarId](#BKMK_UserFiscalCalendarId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_EffectiveOn"></a> EffectiveOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the fiscal calendar sales quota takes effect.|
|DisplayName||
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|effectiveon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_Period1"></a> Period1

|Property|Value|
|--------|-----|
|Description|Sales quota for the first period in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|annual|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_SalesPersonId"></a> SalesPersonId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the sales person associated with the sales quota.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|salespersonid|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the annual fiscal calendar.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|transactioncurrencyid|
|RequiredLevel|ApplicationRequired|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_UserFiscalCalendarId"></a> UserFiscalCalendarId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user associated with the annual fiscal calendar.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|userfiscalcalendarid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FiscalPeriodType](#BKMK_FiscalPeriodType)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [Period1_Base](#BKMK_Period1_Base)
- [SalesPersonIdName](#BKMK_SalesPersonIdName)
- [SalesPersonIdYomiName](#BKMK_SalesPersonIdYomiName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitid|
|RequiredLevel|ApplicationRequired|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the quota for the annual fiscal calendar.|
|DisplayName||
|IsValidForForm|False|
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
|Description|Date and time when the quota for the annual fiscal calendar was created.|
|DisplayName||
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the annualfiscalcalendar.|
|DisplayName||
|IsValidForForm|False|
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the annual fiscal calendar with respect to the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_FiscalPeriodType"></a> FiscalPeriodType

|Property|Value|
|--------|-----|
|Description|Type of fiscal period used in the sales quota.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|fiscalperiodtype|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the quota for the annual fiscal calendar.|
|DisplayName||
|IsValidForForm|False|
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
|Description|Date and time when the annual fiscal calendar was last modified.|
|DisplayName||
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the annualfiscalcalendar.|
|DisplayName||
|IsValidForForm|False|
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


### <a name="BKMK_Period1_Base"></a> Period1_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the first period in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|annual_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_SalesPersonIdName"></a> SalesPersonIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|salespersonidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_SalesPersonIdYomiName"></a> SalesPersonIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|salespersonidyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [AnnualFiscalCalendar_AsyncOperations](#BKMK_AnnualFiscalCalendar_AsyncOperations)
- [AnnualFiscalCalendar_BulkDeleteFailures](#BKMK_AnnualFiscalCalendar_BulkDeleteFailures)


### <a name="BKMK_AnnualFiscalCalendar_AsyncOperations"></a> AnnualFiscalCalendar_AsyncOperations

Same as asyncoperation table [AnnualFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_AnnualFiscalCalendar_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AnnualFiscalCalendar_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_AnnualFiscalCalendar_BulkDeleteFailures"></a> AnnualFiscalCalendar_BulkDeleteFailures

Same as bulkdeletefailure table [AnnualFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_AnnualFiscalCalendar_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AnnualFiscalCalendar_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [transactioncurrency_annualfiscalcalendar](#BKMK_transactioncurrency_annualfiscalcalendar)
- [lk_annualfiscalcalendar_salespersonid](#BKMK_lk_annualfiscalcalendar_salespersonid)
- [lk_annualfiscalcalendar_modifiedonbehalfby](#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby)
- [lk_annualfiscalcalendar_modifiedby](#BKMK_lk_annualfiscalcalendar_modifiedby)
- [lk_annualfiscalcalendar_createdonbehalfby](#BKMK_lk_annualfiscalcalendar_createdonbehalfby)
- [lk_annualfiscalcalendar_createdby](#BKMK_lk_annualfiscalcalendar_createdby)


### <a name="BKMK_transactioncurrency_annualfiscalcalendar"></a> transactioncurrency_annualfiscalcalendar

See transactioncurrency Table [transactioncurrency_annualfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_annualfiscalcalendar) One-To-Many relationship.

### <a name="BKMK_lk_annualfiscalcalendar_salespersonid"></a> lk_annualfiscalcalendar_salespersonid

See systemuser Table [lk_annualfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_annualfiscalcalendar_salespersonid) One-To-Many relationship.

### <a name="BKMK_lk_annualfiscalcalendar_modifiedonbehalfby"></a> lk_annualfiscalcalendar_modifiedonbehalfby

See systemuser Table [lk_annualfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_annualfiscalcalendar_modifiedby"></a> lk_annualfiscalcalendar_modifiedby

See systemuser Table [lk_annualfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_annualfiscalcalendar_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_annualfiscalcalendar_createdonbehalfby"></a> lk_annualfiscalcalendar_createdonbehalfby

See systemuser Table [lk_annualfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_annualfiscalcalendar_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_annualfiscalcalendar_createdby"></a> lk_annualfiscalcalendar_createdby

See systemuser Table [lk_annualfiscalcalendar_createdby](systemuser.md#BKMK_lk_annualfiscalcalendar_createdby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.annualfiscalcalendar?text=annualfiscalcalendar EntityType" />