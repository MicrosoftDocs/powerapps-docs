---
title: "MonthlyFiscalCalendar Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the MonthlyFiscalCalendar entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
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
# MonthlyFiscalCalendar Entity Reference

Monthly fiscal calendar of an organization. A span of time during which the financial activities of an organization are calculated.

## Entity Properties

**DisplayName**: Monthly Fiscal Calendar<br />
**DisplayCollectionName**: Monthly Fiscal Calendars<br />
**SchemaName**: MonthlyFiscalCalendar<br />
**CollectionSchemaName**: MonthlyFiscalCalendars<br />
**LogicalName**: monthlyfiscalcalendar<br />
**LogicalCollectionName**: monthlyfiscalcalendars<br />
**EntitySetName**: monthlyfiscalcalendars<br />
**PrimaryIdAttribute**: userfiscalcalendarid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Date and time when the monthly fiscal calendar sales quota takes effect.<br />
**DisplayName**: <br />
**LogicalName**: effectiveon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_Period1"></a> Period1

**Description**: Sales quota for the first month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month1<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period10"></a> Period10

**Description**: Sales quota for the tenth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month10<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period11"></a> Period11

**Description**: Sales quota for the eleventh month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month11<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period12"></a> Period12

**Description**: Sales quota for the twelfth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month12<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period2"></a> Period2

**Description**: Sales quota for the second month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month2<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period3"></a> Period3

**Description**: Sales quota for the third month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month3<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period4"></a> Period4

**Description**: Sales quota for the fourth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month4<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period5"></a> Period5

**Description**: Sales quota for the fifth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month5<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period6"></a> Period6

**Description**: Sales quota for the sixth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month6<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period7"></a> Period7

**Description**: Sales quota for the seventh month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month7<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period8"></a> Period8

**Description**: Sales quota for the eighth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month8<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period9"></a> Period9

**Description**: Sales quota for the ninth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month9<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_SalesPersonId"></a> SalesPersonId

**Description**: Unique identifier of the associated salesperson.<br />
**DisplayName**: <br />
**LogicalName**: salespersonid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the monthly fiscal calendar.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_UserFiscalCalendarId"></a> UserFiscalCalendarId

**Description**: Unique identifier of the monthly fiscal calendar.<br />
**DisplayName**: <br />
**LogicalName**: userfiscalcalendarid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: <br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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
- [SalesPersonIdName](#BKMK_SalesPersonIdName)
- [SalesPersonIdYomiName](#BKMK_SalesPersonIdYomiName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: businessunitid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: businessunitidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the fiscal calendar.<br />
**DisplayName**: <br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
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

**Description**: Date and time when the quota for the monthly fiscal calendar was modified.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the monthlyfiscalcalendar.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the monthly fiscal calendar with respect to the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_FiscalPeriodType"></a> FiscalPeriodType

**Description**: Type of fiscal period used in the sales quota.<br />
**DisplayName**: <br />
**LogicalName**: fiscalperiodtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the quota for the monthly fiscal calendar.<br />
**DisplayName**: <br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
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

**Description**: Date and time when the quota for the monthly fiscal calendar was last modified.<br />
**DisplayName**: <br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the monthlyfiscalcalendar.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_Period1_Base"></a> Period1_Base

**Description**: Base currency equivalent of the sales quota for the first month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month1_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period10_Base"></a> Period10_Base

**Description**: Base currency equivalent of the sales quota for the tenth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month10_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period11_Base"></a> Period11_Base

**Description**: Base currency equivalent of the sales quota for the eleventh month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month11_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period12_Base"></a> Period12_Base

**Description**: Base currency equivalent of the sales quota for the twelfth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month12_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period2_Base"></a> Period2_Base

**Description**: Base currency equivalent of the sales quota for the second month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month2_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period3_Base"></a> Period3_Base

**Description**: Base currency equivalent of the sales quota for the third month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month3_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period4_Base"></a> Period4_Base

**Description**: Base currency equivalent of the sales quota for the fourth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month4_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period5_Base"></a> Period5_Base

**Description**: Base currency equivalent of the sales quota for the fifth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month5_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period6_Base"></a> Period6_Base

**Description**: Base currency equivalent of the sales quota for the sixth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month6_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period7_Base"></a> Period7_Base

**Description**: Base currency equivalent of the sales quota for the seventh month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month7_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period8_Base"></a> Period8_Base

**Description**: Base currency equivalent of the sales quota for the eighth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month8_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period9_Base"></a> Period9_Base

**Description**: Base currency equivalent of the sales quota for the ninth month in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: month9_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_SalesPersonIdName"></a> SalesPersonIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: salespersonidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SalesPersonIdYomiName"></a> SalesPersonIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: salespersonidyominame<br />
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [MonthlyFiscalCalendar_AsyncOperations](#BKMK_MonthlyFiscalCalendar_AsyncOperations)
- [MonthlyFiscalCalendar_BulkDeleteFailures](#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures)


### <a name="BKMK_MonthlyFiscalCalendar_AsyncOperations"></a> MonthlyFiscalCalendar_AsyncOperations

Same as asyncoperation entity [MonthlyFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_MonthlyFiscalCalendar_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: MonthlyFiscalCalendar_AsyncOperations<br />
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


### <a name="BKMK_MonthlyFiscalCalendar_BulkDeleteFailures"></a> MonthlyFiscalCalendar_BulkDeleteFailures

Same as bulkdeletefailure entity [MonthlyFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: MonthlyFiscalCalendar_BulkDeleteFailures<br />
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

- [lk_monthlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby)
- [lk_monthlyfiscalcalendar_modifiedby](#BKMK_lk_monthlyfiscalcalendar_modifiedby)
- [lk_monthlyfiscalcalendar_createdonbehalfby](#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby)
- [transactioncurrency_monthlyfiscalcalendar](#BKMK_transactioncurrency_monthlyfiscalcalendar)
- [lk_monthlyfiscalcalendar_salespersonid](#BKMK_lk_monthlyfiscalcalendar_salespersonid)
- [lk_monthlyfiscalcalendar_createdby](#BKMK_lk_monthlyfiscalcalendar_createdby)


### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby"></a> lk_monthlyfiscalcalendar_modifiedonbehalfby

See systemuser Entity [lk_monthlyfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedby"></a> lk_monthlyfiscalcalendar_modifiedby

See systemuser Entity [lk_monthlyfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_createdonbehalfby"></a> lk_monthlyfiscalcalendar_createdonbehalfby

See systemuser Entity [lk_monthlyfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_transactioncurrency_monthlyfiscalcalendar"></a> transactioncurrency_monthlyfiscalcalendar

See transactioncurrency Entity [transactioncurrency_monthlyfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_monthlyfiscalcalendar) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_salespersonid"></a> lk_monthlyfiscalcalendar_salespersonid

See systemuser Entity [lk_monthlyfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_monthlyfiscalcalendar_salespersonid) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_createdby"></a> lk_monthlyfiscalcalendar_createdby

See systemuser Entity [lk_monthlyfiscalcalendar_createdby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_createdby) One-To-Many relationship.
monthlyfiscalcalendar

