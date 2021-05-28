---
title: "MonthlyFiscalCalendar table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the MonthlyFiscalCalendar table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# MonthlyFiscalCalendar table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Monthly fiscal calendar of an organization. A span of time during which the financial activities of an organization are calculated.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/monthlyfiscalcalendars<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/monthlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/monthlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/monthlyfiscalcalendars<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/monthlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|MonthlyFiscalCalendars|
|DisplayCollectionName|Monthly Fiscal Calendars|
|DisplayName|Monthly Fiscal Calendar|
|EntitySetName|monthlyfiscalcalendars|
|IsBPFEntity|False|
|LogicalCollectionName|monthlyfiscalcalendars|
|LogicalName|monthlyfiscalcalendar|
|OwnershipType|None|
|PrimaryIdAttribute|userfiscalcalendarid|
|PrimaryNameAttribute||
|SchemaName|MonthlyFiscalCalendar|

<a name="writable-attributes"></a>

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
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the monthly fiscal calendar sales quota takes effect.|
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
|Description|Sales quota for the first month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month1|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period10"></a> Period10

|Property|Value|
|--------|-----|
|Description|Sales quota for the tenth month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month10|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period11"></a> Period11

|Property|Value|
|--------|-----|
|Description|Sales quota for the eleventh month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month11|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period12"></a> Period12

|Property|Value|
|--------|-----|
|Description|Sales quota for the twelfth month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month12|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period2"></a> Period2

|Property|Value|
|--------|-----|
|Description|Sales quota for the second month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month2|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period3"></a> Period3

|Property|Value|
|--------|-----|
|Description|Sales quota for the third month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month3|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period4"></a> Period4

|Property|Value|
|--------|-----|
|Description|Sales quota for the fourth month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month4|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period5"></a> Period5

|Property|Value|
|--------|-----|
|Description|Sales quota for the fifth month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month5|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period6"></a> Period6

|Property|Value|
|--------|-----|
|Description|Sales quota for the sixth month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month6|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period7"></a> Period7

|Property|Value|
|--------|-----|
|Description|Sales quota for the seventh month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month7|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period8"></a> Period8

|Property|Value|
|--------|-----|
|Description|Sales quota for the eighth month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month8|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period9"></a> Period9

|Property|Value|
|--------|-----|
|Description|Sales quota for the ninth month in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|month9|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_SalesPersonId"></a> SalesPersonId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated salesperson.|
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
|Description|Unique identifier of the currency associated with the monthly fiscal calendar.|
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
|Description|Unique identifier of the monthly fiscal calendar.|
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
|Description|Unique identifier of the user who created the fiscal calendar.|
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
|Description|Date and time when the quota for the monthly fiscal calendar was modified.|
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
|Description|Unique identifier of the delegate user who created the monthlyfiscalcalendar.|
|DisplayName|Created By (Delegate)|
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
|Description|Exchange rate for the currency associated with the monthly fiscal calendar with respect to the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
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
|Description|Unique identifier of the user who last modified the quota for the monthly fiscal calendar.|
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
|Description|Date and time when the quota for the monthly fiscal calendar was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the monthlyfiscalcalendar.|
|DisplayName|Modified By (Delegate)|
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
|Description|Base currency equivalent of the sales quota for the first month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month1_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period10_Base"></a> Period10_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the tenth month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month10_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period11_Base"></a> Period11_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the eleventh month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month11_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period12_Base"></a> Period12_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the twelfth month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month12_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period2_Base"></a> Period2_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the second month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month2_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period3_Base"></a> Period3_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the third month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month3_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period4_Base"></a> Period4_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the fourth month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month4_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period5_Base"></a> Period5_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the fifth month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month5_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period6_Base"></a> Period6_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the sixth month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month6_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period7_Base"></a> Period7_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the seventh month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month7_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period8_Base"></a> Period8_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the eighth month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month8_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period9_Base"></a> Period9_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the ninth month in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|month9_base|
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

- [MonthlyFiscalCalendar_AsyncOperations](#BKMK_MonthlyFiscalCalendar_AsyncOperations)
- [MonthlyFiscalCalendar_BulkDeleteFailures](#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures)


### <a name="BKMK_MonthlyFiscalCalendar_AsyncOperations"></a> MonthlyFiscalCalendar_AsyncOperations

Same as asyncoperation table [MonthlyFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_MonthlyFiscalCalendar_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|MonthlyFiscalCalendar_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_MonthlyFiscalCalendar_BulkDeleteFailures"></a> MonthlyFiscalCalendar_BulkDeleteFailures

Same as bulkdeletefailure table [MonthlyFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|MonthlyFiscalCalendar_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_monthlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby)
- [lk_monthlyfiscalcalendar_modifiedby](#BKMK_lk_monthlyfiscalcalendar_modifiedby)
- [lk_monthlyfiscalcalendar_createdonbehalfby](#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby)
- [transactioncurrency_monthlyfiscalcalendar](#BKMK_transactioncurrency_monthlyfiscalcalendar)
- [lk_monthlyfiscalcalendar_salespersonid](#BKMK_lk_monthlyfiscalcalendar_salespersonid)
- [lk_monthlyfiscalcalendar_createdby](#BKMK_lk_monthlyfiscalcalendar_createdby)


### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby"></a> lk_monthlyfiscalcalendar_modifiedonbehalfby

See systemuser Table [lk_monthlyfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedby"></a> lk_monthlyfiscalcalendar_modifiedby

See systemuser Table [lk_monthlyfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_createdonbehalfby"></a> lk_monthlyfiscalcalendar_createdonbehalfby

See systemuser Table [lk_monthlyfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_transactioncurrency_monthlyfiscalcalendar"></a> transactioncurrency_monthlyfiscalcalendar

See transactioncurrency Table [transactioncurrency_monthlyfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_monthlyfiscalcalendar) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_salespersonid"></a> lk_monthlyfiscalcalendar_salespersonid

See systemuser Table [lk_monthlyfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_monthlyfiscalcalendar_salespersonid) One-To-Many relationship.

### <a name="BKMK_lk_monthlyfiscalcalendar_createdby"></a> lk_monthlyfiscalcalendar_createdby

See systemuser Table [lk_monthlyfiscalcalendar_createdby](systemuser.md#BKMK_lk_monthlyfiscalcalendar_createdby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.monthlyfiscalcalendar?text=monthlyfiscalcalendar EntityType" />