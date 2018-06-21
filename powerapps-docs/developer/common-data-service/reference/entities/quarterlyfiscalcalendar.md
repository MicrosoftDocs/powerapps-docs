---
title: "QuarterlyFiscalCalendar Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the QuarterlyFiscalCalendar entity."

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
# QuarterlyFiscalCalendar Entity Reference

Quarterly fiscal calendar of an organization. A span of time during which the financial activities of an organization are calculated.

## Entity Properties

**DisplayName**: Quarterly Fiscal Calendar<br />
**DisplayCollectionName**: Quarterly Fiscal Calendars<br />
**SchemaName**: QuarterlyFiscalCalendar<br />
**CollectionSchemaName**: QuarterlyFiscalCalendars<br />
**LogicalName**: quarterlyfiscalcalendar<br />
**LogicalCollectionName**: quarterlyfiscalcalendars<br />
**EntitySetName**: quarterlyfiscalcalendars<br />
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
- [Period4](#BKMK_Period4)
- [Period7](#BKMK_Period7)
- [SalesPersonId](#BKMK_SalesPersonId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UserFiscalCalendarId](#BKMK_UserFiscalCalendarId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_EffectiveOn"></a> EffectiveOn

**Description**: Date and time when the quarterly fiscal calendar sales quota takes effect.<br />
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

**Description**: Sales quota for the first quarter in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: quarter1<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period10"></a> Period10

**Description**: Sales quota for the fourth quarter in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: quarter4<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period4"></a> Period4

**Description**: Sales quota for the second quarter in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: quarter2<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Money<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2<br />
**PrecisionSource**: 2


### <a name="BKMK_Period7"></a> Period7

**Description**: Sales quota for the third quarter in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: quarter3<br />
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

**Description**: Unique identifier of the currency associated with the quarterly fiscal calendar.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_UserFiscalCalendarId"></a> UserFiscalCalendarId

**Description**: Unique identifier of the quarterly fiscal calendar.<br />
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
- [Period4_Base](#BKMK_Period4_Base)
- [Period7_Base](#BKMK_Period7_Base)
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

**Description**: Unique identifier of the user who created the quarterly fiscal calendar.<br />
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

**Description**: Date and time when the quota for the quarterly fiscal calendar was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the quarterlyfiscalcalendar.<br />
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

**Description**: Exchange rate for the currency associated with the quarterly fiscal calendar with respect to the base currency.<br />
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

**Description**: Unique identifier of the user who last modified the quarterly fiscal calendar.<br />
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

**Description**: Date and time when the quarterly fiscal calendar was last modified.<br />
**DisplayName**: <br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the quarterlyfiscalcalendar.<br />
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

**Description**: Base currency equivalent of the sales quota for the first quarter in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: quarter1_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period10_Base"></a> Period10_Base

**Description**: Base currency equivalent of the sales quota for the fourth quarter in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: quarter4_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period4_Base"></a> Period4_Base

**Description**: Base currency equivalent of the sales quota for the second quarter in the fiscal year<br />
**DisplayName**: <br />
**LogicalName**: quarter2_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_Period7_Base"></a> Period7_Base

**Description**: Base currency equivalent of the sales quota for the third quarter in the fiscal year.<br />
**DisplayName**: <br />
**LogicalName**: quarter3_base<br />
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

- [QuarterlyFiscalCalendar_AsyncOperations](#BKMK_QuarterlyFiscalCalendar_AsyncOperations)
- [QuarterlyFiscalCalendar_BulkDeleteFailures](#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures)


### <a name="BKMK_QuarterlyFiscalCalendar_AsyncOperations"></a> QuarterlyFiscalCalendar_AsyncOperations

Same as asyncoperation entity [QuarterlyFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_QuarterlyFiscalCalendar_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: QuarterlyFiscalCalendar_AsyncOperations<br />
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


### <a name="BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures"></a> QuarterlyFiscalCalendar_BulkDeleteFailures

Same as bulkdeletefailure entity [QuarterlyFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: QuarterlyFiscalCalendar_BulkDeleteFailures<br />
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

- [lk_quarterlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby)
- [lk_quarterlyfiscalcalendar_createdby](#BKMK_lk_quarterlyfiscalcalendar_createdby)
- [transactioncurrency_quarterlyfiscalcalendar](#BKMK_transactioncurrency_quarterlyfiscalcalendar)
- [lk_quarterlyfiscalcalendar_createdonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby)
- [lk_quarterlyfiscalcalendar_salespersonid](#BKMK_lk_quarterlyfiscalcalendar_salespersonid)
- [lk_quarterlyfiscalcalendar_modifiedby](#BKMK_lk_quarterlyfiscalcalendar_modifiedby)


### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby"></a> lk_quarterlyfiscalcalendar_modifiedonbehalfby

See systemuser Entity [lk_quarterlyfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_createdby"></a> lk_quarterlyfiscalcalendar_createdby

See systemuser Entity [lk_quarterlyfiscalcalendar_createdby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_createdby) One-To-Many relationship.

### <a name="BKMK_transactioncurrency_quarterlyfiscalcalendar"></a> transactioncurrency_quarterlyfiscalcalendar

See transactioncurrency Entity [transactioncurrency_quarterlyfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_quarterlyfiscalcalendar) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby"></a> lk_quarterlyfiscalcalendar_createdonbehalfby

See systemuser Entity [lk_quarterlyfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_salespersonid"></a> lk_quarterlyfiscalcalendar_salespersonid

See systemuser Entity [lk_quarterlyfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_salespersonid) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedby"></a> lk_quarterlyfiscalcalendar_modifiedby

See systemuser Entity [lk_quarterlyfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_modifiedby) One-To-Many relationship.
quarterlyfiscalcalendar

