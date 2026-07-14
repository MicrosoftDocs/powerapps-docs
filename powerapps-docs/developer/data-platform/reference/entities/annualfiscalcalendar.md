---
title: "Annual Fiscal Calendar (AnnualFiscalCalendar) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Annual Fiscal Calendar (AnnualFiscalCalendar) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Annual Fiscal Calendar (AnnualFiscalCalendar) table/entity reference (Microsoft Dataverse)

Year long fiscal calendar of an organization. A span of time during which the financial activities of an organization are calculated.

## Messages

The following table lists the messages for the Annual Fiscal Calendar (AnnualFiscalCalendar) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /annualfiscalcalendars<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /annualfiscalcalendars(*userfiscalcalendarid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /annualfiscalcalendars(*userfiscalcalendarid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /annualfiscalcalendars<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /annualfiscalcalendars(*userfiscalcalendarid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /annualfiscalcalendars(*userfiscalcalendarid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Annual Fiscal Calendar (AnnualFiscalCalendar) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Annual Fiscal Calendar** |
| **DisplayCollectionName** | **Annual Fiscal Calendars** |
| **SchemaName** | `AnnualFiscalCalendar` |
| **CollectionSchemaName** | `AnnualFiscalCalendars` |
| **EntitySetName** | `annualfiscalcalendars`|
| **LogicalName** | `annualfiscalcalendar` |
| **LogicalCollectionName** | `annualfiscalcalendars` |
| **PrimaryIdAttribute** | `userfiscalcalendarid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Date and time when the fiscal calendar sales quota takes effect.**|
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
|Description|**Sales quota for the first period in the fiscal year.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`annual`|
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
|Description|**Unique identifier of the sales person associated with the sales quota.**|
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
|Description|**Unique identifier of the currency associated with the annual fiscal calendar.**|
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
|Description|**Unique identifier of the user associated with the annual fiscal calendar.**|
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
|Description|**Unique identifier of the user who created the quota for the annual fiscal calendar.**|
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
|Description|**Date and time when the quota for the annual fiscal calendar was created.**|
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
|Description|**Unique identifier of the delegate user who created the annualfiscalcalendar.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the annual fiscal calendar with respect to the base currency.**|
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
|Description|**Unique identifier of the user who last modified the quota for the annual fiscal calendar.**|
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
|Description|**Date and time when the annual fiscal calendar was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the annualfiscalcalendar.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Period1_Base"></a> Period1_Base

|Property|Value|
|---|---|
|Description|**Base currency equivalent of the sales quota for the first period in the fiscal year.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`annual_base`|
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

- [lk_annualfiscalcalendar_createdby](#BKMK_lk_annualfiscalcalendar_createdby)
- [lk_annualfiscalcalendar_createdonbehalfby](#BKMK_lk_annualfiscalcalendar_createdonbehalfby)
- [lk_annualfiscalcalendar_modifiedby](#BKMK_lk_annualfiscalcalendar_modifiedby)
- [lk_annualfiscalcalendar_modifiedonbehalfby](#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby)
- [lk_annualfiscalcalendar_salespersonid](#BKMK_lk_annualfiscalcalendar_salespersonid)
- [transactioncurrency_annualfiscalcalendar](#BKMK_transactioncurrency_annualfiscalcalendar)

### <a name="BKMK_lk_annualfiscalcalendar_createdby"></a> lk_annualfiscalcalendar_createdby

One-To-Many Relationship: [systemuser lk_annualfiscalcalendar_createdby](systemuser.md#BKMK_lk_annualfiscalcalendar_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_annualfiscalcalendar_createdonbehalfby"></a> lk_annualfiscalcalendar_createdonbehalfby

One-To-Many Relationship: [systemuser lk_annualfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_annualfiscalcalendar_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_annualfiscalcalendar_modifiedby"></a> lk_annualfiscalcalendar_modifiedby

One-To-Many Relationship: [systemuser lk_annualfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_annualfiscalcalendar_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_annualfiscalcalendar_modifiedonbehalfby"></a> lk_annualfiscalcalendar_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_annualfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_annualfiscalcalendar_salespersonid"></a> lk_annualfiscalcalendar_salespersonid

One-To-Many Relationship: [systemuser lk_annualfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_annualfiscalcalendar_salespersonid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`salespersonid`|
|ReferencingEntityNavigationPropertyName|`salespersonid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_annualfiscalcalendar"></a> transactioncurrency_annualfiscalcalendar

One-To-Many Relationship: [transactioncurrency transactioncurrency_annualfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_annualfiscalcalendar)

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

- [AnnualFiscalCalendar_AsyncOperations](#BKMK_AnnualFiscalCalendar_AsyncOperations)
- [AnnualFiscalCalendar_BulkDeleteFailures](#BKMK_AnnualFiscalCalendar_BulkDeleteFailures)

### <a name="BKMK_AnnualFiscalCalendar_AsyncOperations"></a> AnnualFiscalCalendar_AsyncOperations

Many-To-One Relationship: [asyncoperation AnnualFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_AnnualFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`AnnualFiscalCalendar_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AnnualFiscalCalendar_BulkDeleteFailures"></a> AnnualFiscalCalendar_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure AnnualFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_AnnualFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`AnnualFiscalCalendar_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.annualfiscalcalendar?displayProperty=fullName>
