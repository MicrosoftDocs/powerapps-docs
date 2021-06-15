---
title: "QuarterlyFiscalCalendar table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the QuarterlyFiscalCalendar table/entity."
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

# QuarterlyFiscalCalendar table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Quarterly fiscal calendar of an organization. A span of time during which the financial activities of an organization are calculated.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/quarterlyfiscalcalendars<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/quarterlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/quarterlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/quarterlyfiscalcalendars<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/quarterlyfiscalcalendars(*userfiscalcalendarid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|QuarterlyFiscalCalendars|
|DisplayCollectionName|Quarterly Fiscal Calendars|
|DisplayName|Quarterly Fiscal Calendar|
|EntitySetName|quarterlyfiscalcalendars|
|IsBPFEntity|False|
|LogicalCollectionName|quarterlyfiscalcalendars|
|LogicalName|quarterlyfiscalcalendar|
|OwnershipType|None|
|PrimaryIdAttribute|userfiscalcalendarid|
|PrimaryNameAttribute||
|SchemaName|QuarterlyFiscalCalendar|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the quarterly fiscal calendar sales quota takes effect.|
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
|Description|Sales quota for the first quarter in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|quarter1|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period10"></a> Period10

|Property|Value|
|--------|-----|
|Description|Sales quota for the fourth quarter in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|quarter4|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period4"></a> Period4

|Property|Value|
|--------|-----|
|Description|Sales quota for the second quarter in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|quarter2|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|PrecisionSource|2|
|RequiredLevel|SystemRequired|
|Type|Money|


### <a name="BKMK_Period7"></a> Period7

|Property|Value|
|--------|-----|
|Description|Sales quota for the third quarter in the fiscal year.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|quarter3|
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
|Description|Unique identifier of the currency associated with the quarterly fiscal calendar.|
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
|Description|Unique identifier of the quarterly fiscal calendar.|
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
- [Period4_Base](#BKMK_Period4_Base)
- [Period7_Base](#BKMK_Period7_Base)
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
|Description|Unique identifier of the user who created the quarterly fiscal calendar.|
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
|Description|Date and time when the quota for the quarterly fiscal calendar was created.|
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
|Description|Unique identifier of the delegate user who created the quarterlyfiscalcalendar.|
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
|Description|Exchange rate for the currency associated with the quarterly fiscal calendar with respect to the base currency.|
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
|Description|Unique identifier of the user who last modified the quarterly fiscal calendar.|
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
|Description|Date and time when the quarterly fiscal calendar was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the quarterlyfiscalcalendar.|
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
|Description|Base currency equivalent of the sales quota for the first quarter in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|quarter1_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period10_Base"></a> Period10_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the fourth quarter in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|quarter4_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period4_Base"></a> Period4_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the second quarter in the fiscal year|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|quarter2_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_Period7_Base"></a> Period7_Base

|Property|Value|
|--------|-----|
|Description|Base currency equivalent of the sales quota for the third quarter in the fiscal year.|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|quarter3_base|
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

- [QuarterlyFiscalCalendar_AsyncOperations](#BKMK_QuarterlyFiscalCalendar_AsyncOperations)
- [QuarterlyFiscalCalendar_BulkDeleteFailures](#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures)


### <a name="BKMK_QuarterlyFiscalCalendar_AsyncOperations"></a> QuarterlyFiscalCalendar_AsyncOperations

Same as asyncoperation table [QuarterlyFiscalCalendar_AsyncOperations](asyncoperation.md#BKMK_QuarterlyFiscalCalendar_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|QuarterlyFiscalCalendar_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures"></a> QuarterlyFiscalCalendar_BulkDeleteFailures

Same as bulkdeletefailure table [QuarterlyFiscalCalendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|QuarterlyFiscalCalendar_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_quarterlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby)
- [lk_quarterlyfiscalcalendar_createdby](#BKMK_lk_quarterlyfiscalcalendar_createdby)
- [transactioncurrency_quarterlyfiscalcalendar](#BKMK_transactioncurrency_quarterlyfiscalcalendar)
- [lk_quarterlyfiscalcalendar_createdonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby)
- [lk_quarterlyfiscalcalendar_salespersonid](#BKMK_lk_quarterlyfiscalcalendar_salespersonid)
- [lk_quarterlyfiscalcalendar_modifiedby](#BKMK_lk_quarterlyfiscalcalendar_modifiedby)


### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby"></a> lk_quarterlyfiscalcalendar_modifiedonbehalfby

See systemuser Table [lk_quarterlyfiscalcalendar_modifiedonbehalfby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_createdby"></a> lk_quarterlyfiscalcalendar_createdby

See systemuser Table [lk_quarterlyfiscalcalendar_createdby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_createdby) One-To-Many relationship.

### <a name="BKMK_transactioncurrency_quarterlyfiscalcalendar"></a> transactioncurrency_quarterlyfiscalcalendar

See transactioncurrency Table [transactioncurrency_quarterlyfiscalcalendar](transactioncurrency.md#BKMK_transactioncurrency_quarterlyfiscalcalendar) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby"></a> lk_quarterlyfiscalcalendar_createdonbehalfby

See systemuser Table [lk_quarterlyfiscalcalendar_createdonbehalfby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_salespersonid"></a> lk_quarterlyfiscalcalendar_salespersonid

See systemuser Table [lk_quarterlyfiscalcalendar_salespersonid](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_salespersonid) One-To-Many relationship.

### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedby"></a> lk_quarterlyfiscalcalendar_modifiedby

See systemuser Table [lk_quarterlyfiscalcalendar_modifiedby](systemuser.md#BKMK_lk_quarterlyfiscalcalendar_modifiedby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.quarterlyfiscalcalendar?text=quarterlyfiscalcalendar EntityType" />