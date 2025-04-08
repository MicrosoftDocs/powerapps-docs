---
title: "Monthly Fiscal Calendar (MonthlyFiscalCalendar) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Monthly Fiscal Calendar (MonthlyFiscalCalendar) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Monthly Fiscal Calendar (MonthlyFiscalCalendar) table/entity reference (Microsoft Dataverse)

Monthly fiscal calendar of an organization. A span of time during which the financial activities of an organization are calculated.

## Messages

The following table lists the messages for the Monthly Fiscal Calendar (MonthlyFiscalCalendar) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /monthlyfiscalcalendars<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /monthlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /monthlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /monthlyfiscalcalendars<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /monthlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /monthlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Monthly Fiscal Calendar (MonthlyFiscalCalendar) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Monthly Fiscal Calendar** |
| **DisplayCollectionName** | **Monthly Fiscal Calendars** |
| **SchemaName** | `MonthlyFiscalCalendar` |
| **CollectionSchemaName** | `MonthlyFiscalCalendars` |
| **EntitySetName** | `monthlyfiscalcalendars`|
| **LogicalName** | `monthlyfiscalcalendar` |
| **LogicalCollectionName** | `monthlyfiscalcalendars` |
| **PrimaryIdAttribute** | `userfiscalcalendarid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EffectiveOn](#BKMK_EffectiveOn)
- [Period1](#BKMK_Period1)
- [Period10](#BKMK_Period10)
- [Period11](#BKMK_Period11)
- [Period12](#BKMK_Period12)
- [Period2](#BKMK_Period2)
- [Period3](#BKMK_Period3)
- [Period4](#BKMK_Period4)
- [Period5](#BKMK_Period5)
- [Period6](#BKMK_Period6)
- [Period7](#BKMK_Period7)
- [Period8](#BKMK_Period8)
- [Period9](#BKMK_Period9)
- [SalesPersonId](#BKMK_SalesPersonId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UserFiscalCalendarId](#BKMK_UserFiscalCalendarId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_EffectiveOn"></a> EffectiveOn

|Property|Value|
|---|---|
|Description|**Date and time when the monthly fiscal calendar sales quota takes effect.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`effectiveon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Period1"></a> Period1

|Property|Value|
|---|---|
|Description|**Sales quota for the first month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month1`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period10"></a> Period10

|Property|Value|
|---|---|
|Description|**Sales quota for the tenth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month10`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period11"></a> Period11

|Property|Value|
|---|---|
|Description|**Sales quota for the eleventh month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month11`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period12"></a> Period12

|Property|Value|
|---|---|
|Description|**Sales quota for the twelfth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month12`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period2"></a> Period2

|Property|Value|
|---|---|
|Description|**Sales quota for the second month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month2`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period3"></a> Period3

|Property|Value|
|---|---|
|Description|**Sales quota for the third month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month3`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period4"></a> Period4

|Property|Value|
|---|---|
|Description|**Sales quota for the fourth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month4`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period5"></a> Period5

|Property|Value|
|---|---|
|Description|**Sales quota for the fifth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month5`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period6"></a> Period6

|Property|Value|
|---|---|
|Description|**Sales quota for the sixth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month6`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period7"></a> Period7

|Property|Value|
|---|---|
|Description|**Sales quota for the seventh month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month7`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period8"></a> Period8

|Property|Value|
|---|---|
|Description|**Sales quota for the eighth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month8`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period9"></a> Period9

|Property|Value|
|---|---|
|Description|**Sales quota for the ninth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`month9`|
|RequiredLevel|SystemRequired|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_SalesPersonId"></a> SalesPersonId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated salesperson.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`salespersonid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the monthly fiscal calendar.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_UserFiscalCalendarId"></a> UserFiscalCalendarId

|Property|Value|
|---|---|
|Description|**Unique identifier of the monthly fiscal calendar.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`userfiscalcalendarid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FiscalPeriodType](#BKMK_FiscalPeriodType)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Period1_Base](#BKMK_Period1_Base)
- [Period10_Base](#BKMK_Period10_Base)
- [Period11_Base](#BKMK_Period11_Base)
- [Period12_Base](#BKMK_Period12_Base)
- [Period2_Base](#BKMK_Period2_Base)
- [Period3_Base](#BKMK_Period3_Base)
- [Period4_Base](#BKMK_Period4_Base)
- [Period5_Base](#BKMK_Period5_Base)
- [Period6_Base](#BKMK_Period6_Base)
- [Period7_Base](#BKMK_Period7_Base)
- [Period8_Base](#BKMK_Period8_Base)
- [Period9_Base](#BKMK_Period9_Base)

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the fiscal calendar.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the quota for the monthly fiscal calendar was modified.**|
|DisplayName||
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

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the monthlyfiscalcalendar.**|
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
|Description|**Exchange rate for the currency associated with the monthly fiscal calendar with respect to the base currency.**|
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

### <a name="BKMK_FiscalPeriodType"></a> FiscalPeriodType

|Property|Value|
|---|---|
|Description|**Type of fiscal period used in the sales quota.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalperiodtype`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the quota for the monthly fiscal calendar.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the quota for the monthly fiscal calendar was last modified.**|
|DisplayName||
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
|Description|**Unique identifier of the delegate user who last modified the monthlyfiscalcalendar.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Period1_Base"></a> Period1_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the first month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month1_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period10_Base"></a> Period10_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the tenth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month10_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period11_Base"></a> Period11_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the eleventh month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month11_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period12_Base"></a> Period12_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the twelfth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month12_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period2_Base"></a> Period2_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the second month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month2_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period3_Base"></a> Period3_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the third month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month3_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period4_Base"></a> Period4_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the fourth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month4_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period5_Base"></a> Period5_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the fifth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month5_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period6_Base"></a> Period6_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the sixth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month6_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period7_Base"></a> Period7_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the seventh month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month7_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period8_Base"></a> Period8_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the eighth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month8_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_Period9_Base"></a> Period9_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the ninth month in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`month9_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_monthlyfiscalcalendar_createdby](#BKMK_lk_monthlyfiscalcalendar_createdby)
- [lk_monthlyfiscalcalendar_createdonbehalfby](#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby)
- [lk_monthlyfiscalcalendar_modifiedby](#BKMK_lk_monthlyfiscalcalendar_modifiedby)
- [lk_monthlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby)
- [lk_monthlyfiscalcalendar_salespersonid](#BKMK_lk_monthlyfiscalcalendar_salespersonid)
- [transactioncurrency_monthlyfiscalcalendar](#BKMK_transactioncurrency_monthlyfiscalcalendar)

### <a name="BKMK_lk_monthlyfiscalcalendar_createdby"></a> lk_monthlyfiscalcalendar_createdby

One-To-Many Relationship: [systemuser lk_monthlyfiscalcalendar_createdby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_monthlyfiscalcalendar_createdonbehalfby"></a> lk_monthlyfiscalcalendar_createdonbehalfby

One-To-Many Relationship: [systemuser lk_monthlyfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedby"></a> lk_monthlyfiscalcalendar_modifiedby

One-To-Many Relationship: [systemuser lk_monthlyfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby"></a> lk_monthlyfiscalcalendar_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_monthlyfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_monthlyfiscalcalendar_salespersonid"></a> lk_monthlyfiscalcalendar_salespersonid

One-To-Many Relationship: [systemuser lk_monthlyfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_monthlyfiscalcalendar_salespersonid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`salespersonid`|
|ReferencingEntityNavigationPropertyName|`salespersonid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_monthlyfiscalcalendar"></a> transactioncurrency_monthlyfiscalcalendar

One-To-Many Relationship: [transactioncurrency transactioncurrency_monthlyfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_monthlyfiscalcalendar)

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

- [MonthlyFiscalCalendar_AsyncOperations](#BKMK_MonthlyFiscalCalendar_AsyncOperations)
- [MonthlyFiscalCalendar_BulkDeleteFailures](#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures)

### <a name="BKMK_MonthlyFiscalCalendar_AsyncOperations"></a> MonthlyFiscalCalendar_AsyncOperations

Many-To-One Relationship: [asyncoperation MonthlyFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_MonthlyFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`MonthlyFiscalCalendar_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_MonthlyFiscalCalendar_BulkDeleteFailures"></a> MonthlyFiscalCalendar_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure MonthlyFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`MonthlyFiscalCalendar_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.monthlyfiscalcalendar?displayProperty=fullName>
