---
title: "Semiannual Fiscal Calendar (SemiAnnualFiscalCalendar) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Semiannual Fiscal Calendar (SemiAnnualFiscalCalendar) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Semiannual Fiscal Calendar (SemiAnnualFiscalCalendar) table/entity reference (Microsoft Dataverse)

Calendar representing the semi-annual span of time during which the financial activities of an organization are calculated.

## Messages

The following table lists the messages for the Semiannual Fiscal Calendar (SemiAnnualFiscalCalendar) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /semiannualfiscalcalendars<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /semiannualfiscalcalendars(*userfiscalcalendarid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /semiannualfiscalcalendars(*userfiscalcalendarid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /semiannualfiscalcalendars<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /semiannualfiscalcalendars(*userfiscalcalendarid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /semiannualfiscalcalendars(*userfiscalcalendarid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Semiannual Fiscal Calendar (SemiAnnualFiscalCalendar) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Semiannual Fiscal Calendar** |
| **DisplayCollectionName** | **Semiannual Fiscal Calendars** |
| **SchemaName** | `SemiAnnualFiscalCalendar` |
| **CollectionSchemaName** | `SemiAnnualFiscalCalendars` |
| **EntitySetName** | `semiannualfiscalcalendars`|
| **LogicalName** | `semiannualfiscalcalendar` |
| **LogicalCollectionName** | `semiannualfiscalcalendars` |
| **PrimaryIdAttribute** | `userfiscalcalendarid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EffectiveOn](#BKMK_EffectiveOn)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Period1](#BKMK_Period1)
- [Period7](#BKMK_Period7)
- [SalesPersonId](#BKMK_SalesPersonId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UserFiscalCalendarId](#BKMK_UserFiscalCalendarId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_EffectiveOn"></a> EffectiveOn

|Property|Value|
|---|---|
|Description|**Date and time when the semiannual fiscal calendar sales quota takes effect.**|
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

### <a name="BKMK_Period1"></a> Period1

|Property|Value|
|---|---|
|Description|**Sales quota for the first half of the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`firsthalf`|
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
|Description|**Sales quota for the second half of the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`secondhalf`|
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
|Description|**Unique identifier of the currency associated with the semiannual fiscal calendar.**|
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
|Description|**Unique identifier for the user who created the semiannual fiscal calendar.**|
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
- [Period7_Base](#BKMK_Period7_Base)

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit with which the calendar is associated.**|
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
|Description|**Unique identifier of the user who created the semiannual fiscal calendar.**|
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
|Description|**Date and time when the quota for the semiannual fiscal calendar was created.**|
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
|Description|**Unique identifier of the delegate user who created the semiannualfiscalcalendar.**|
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
|Description|**Exchange rate for the currency associated with the semiannual fiscal calendar with respect to the base currency.**|
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
|Description|**Unique identifier of the user who last modified the semiannual fiscal calendar.**|
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
|Description|**Date and time when the semiannual fiscal calendar was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the semiannualfiscalcalendar.**|
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
|Description|**Base currency equivalent for the sales quota for the first half of the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`firsthalf_base`|
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
|Description|**Base currency equivalent of the sales quota for the second half of the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`secondhalf_base`|
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

- [lk_semiannualfiscalcalendar_createdby](#BKMK_lk_semiannualfiscalcalendar_createdby)
- [lk_semiannualfiscalcalendar_createdonbehalfby](#BKMK_lk_semiannualfiscalcalendar_createdonbehalfby)
- [lk_semiannualfiscalcalendar_modifiedby](#BKMK_lk_semiannualfiscalcalendar_modifiedby)
- [lk_semiannualfiscalcalendar_modifiedonbehalfby](#BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby)
- [lk_semiannualfiscalcalendar_salespersonid](#BKMK_lk_semiannualfiscalcalendar_salespersonid)
- [transactioncurrency_semiannualfiscalcalendar](#BKMK_transactioncurrency_semiannualfiscalcalendar)

### <a name="BKMK_lk_semiannualfiscalcalendar_createdby"></a> lk_semiannualfiscalcalendar_createdby

One-To-Many Relationship: [systemuser lk_semiannualfiscalcalendar_createdby](systemuser.md#BKMK_lk_semiannualfiscalcalendar_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_semiannualfiscalcalendar_createdonbehalfby"></a> lk_semiannualfiscalcalendar_createdonbehalfby

One-To-Many Relationship: [systemuser lk_semiannualfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_semiannualfiscalcalendar_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_semiannualfiscalcalendar_modifiedby"></a> lk_semiannualfiscalcalendar_modifiedby

One-To-Many Relationship: [systemuser lk_semiannualfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_semiannualfiscalcalendar_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby"></a> lk_semiannualfiscalcalendar_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_semiannualfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_semiannualfiscalcalendar_salespersonid"></a> lk_semiannualfiscalcalendar_salespersonid

One-To-Many Relationship: [systemuser lk_semiannualfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_semiannualfiscalcalendar_salespersonid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`salespersonid`|
|ReferencingEntityNavigationPropertyName|`salespersonid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_semiannualfiscalcalendar"></a> transactioncurrency_semiannualfiscalcalendar

One-To-Many Relationship: [transactioncurrency transactioncurrency_semiannualfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_semiannualfiscalcalendar)

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

- [SemiAnnualFiscalCalendar_AsyncOperations](#BKMK_SemiAnnualFiscalCalendar_AsyncOperations)
- [SemiAnnualFiscalCalendar_BulkDeleteFailures](#BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures)

### <a name="BKMK_SemiAnnualFiscalCalendar_AsyncOperations"></a> SemiAnnualFiscalCalendar_AsyncOperations

Many-To-One Relationship: [asyncoperation SemiAnnualFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_SemiAnnualFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SemiAnnualFiscalCalendar_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures"></a> SemiAnnualFiscalCalendar_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure SemiAnnualFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SemiAnnualFiscalCalendar_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.semiannualfiscalcalendar?displayProperty=fullName>
