---
title: "Goal table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Goal table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Goal table/entity reference (Microsoft Dataverse)

Target objective for a user or a team for a specified time period.

## Messages

The following table lists the messages for the Goal table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /goals(*goalid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /goals<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /goals(*goalid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Recalculate`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Recalculate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RecalculateRequest>|
| `Retrieve`<br />Event: True |`GET` /goals(*goalid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /goals<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /goals(*goalid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /goals(*goalid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /goals(*goalid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Goal table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Goal** |
| **DisplayCollectionName** | **Goals** |
| **SchemaName** | `Goal` |
| **CollectionSchemaName** | `Goals` |
| **EntitySetName** | `goals`|
| **LogicalName** | `goal` |
| **LogicalCollectionName** | `goals` |
| **PrimaryIdAttribute** | `goalid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActualDecimal](#BKMK_ActualDecimal)
- [ActualInteger](#BKMK_ActualInteger)
- [ActualMoney](#BKMK_ActualMoney)
- [AmountDataType](#BKMK_AmountDataType)
- [ConsiderOnlyGoalOwnersRecords](#BKMK_ConsiderOnlyGoalOwnersRecords)
- [CustomRollupFieldDecimal](#BKMK_CustomRollupFieldDecimal)
- [CustomRollupFieldInteger](#BKMK_CustomRollupFieldInteger)
- [CustomRollupFieldMoney](#BKMK_CustomRollupFieldMoney)
- [EntityImage](#BKMK_EntityImage)
- [FiscalPeriod](#BKMK_FiscalPeriod)
- [FiscalYear](#BKMK_FiscalYear)
- [GoalEndDate](#BKMK_GoalEndDate)
- [GoalId](#BKMK_GoalId)
- [GoalOwnerId](#BKMK_GoalOwnerId)
- [GoalOwnerIdType](#BKMK_GoalOwnerIdType)
- [GoalStartDate](#BKMK_GoalStartDate)
- [GoalWithErrorId](#BKMK_GoalWithErrorId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InProgressDecimal](#BKMK_InProgressDecimal)
- [InProgressInteger](#BKMK_InProgressInteger)
- [InProgressMoney](#BKMK_InProgressMoney)
- [IsAmount](#BKMK_IsAmount)
- [IsFiscalPeriodGoal](#BKMK_IsFiscalPeriodGoal)
- [IsOverridden](#BKMK_IsOverridden)
- [IsOverride](#BKMK_IsOverride)
- [LastRolledupDate](#BKMK_LastRolledupDate)
- [MetricId](#BKMK_MetricId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentGoalId](#BKMK_ParentGoalId)
- [Percentage](#BKMK_Percentage)
- [RollupErrorCode](#BKMK_RollupErrorCode)
- [RollupOnlyFromChildGoals](#BKMK_RollupOnlyFromChildGoals)
- [RollUpQueryActualDecimalId](#BKMK_RollUpQueryActualDecimalId)
- [RollupQueryActualIntegerId](#BKMK_RollupQueryActualIntegerId)
- [RollUpQueryActualMoneyId](#BKMK_RollUpQueryActualMoneyId)
- [RollUpQueryCustomDecimalId](#BKMK_RollUpQueryCustomDecimalId)
- [RollUpQueryCustomIntegerId](#BKMK_RollUpQueryCustomIntegerId)
- [RollUpQueryCustomMoneyId](#BKMK_RollUpQueryCustomMoneyId)
- [RollUpQueryInprogressDecimalId](#BKMK_RollUpQueryInprogressDecimalId)
- [RollUpQueryInprogressIntegerId](#BKMK_RollUpQueryInprogressIntegerId)
- [RollUpQueryInprogressMoneyId](#BKMK_RollUpQueryInprogressMoneyId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [StretchTargetDecimal](#BKMK_StretchTargetDecimal)
- [StretchTargetInteger](#BKMK_StretchTargetInteger)
- [StretchTargetMoney](#BKMK_StretchTargetMoney)
- [TargetDecimal](#BKMK_TargetDecimal)
- [TargetInteger](#BKMK_TargetInteger)
- [TargetMoney](#BKMK_TargetMoney)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ActualDecimal"></a> ActualDecimal

|Property|Value|
|---|---|
|Description|**Shows the actual value (Decimal type) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount and the amount data type is Decimal.**|
|DisplayName|**Actual (Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualdecimal`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|10|
|SourceTypeMask|0|

### <a name="BKMK_ActualInteger"></a> ActualInteger

|Property|Value|
|---|---|
|Description|**Shows the actual value (integer) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount or Count and the amount data type is Integer.**|
|DisplayName|**Actual (Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualinteger`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ActualMoney"></a> ActualMoney

|Property|Value|
|---|---|
|Description|**Shows the actual value (Money type) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount and the amount data type is Money.**|
|DisplayName|**Actual (Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualmoney`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_AmountDataType"></a> AmountDataType

|Property|Value|
|---|---|
|Description|**Data type of the amount.**|
|DisplayName|**Amount Data Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`amountdatatype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`metric_goaltype`|

#### AmountDataType Choices/Options

|Value|Label|
|---|---|
|0|**Money**|
|1|**Decimal**|
|2|**Integer**|

### <a name="BKMK_ConsiderOnlyGoalOwnersRecords"></a> ConsiderOnlyGoalOwnersRecords

|Property|Value|
|---|---|
|Description|**Select whether only the goal owner's records, or all records, should be rolled up for goal results.**|
|DisplayName|**Record Set for Rollup**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`consideronlygoalownersrecords`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`goal_consideronlygoalownersrecords`|
|DefaultValue|True|
|True Label|Owned by goal owner|
|False Label|All|

### <a name="BKMK_CustomRollupFieldDecimal"></a> CustomRollupFieldDecimal

|Property|Value|
|---|---|
|Description|**Indicates a placeholder rollup field for a decimal value to track a third category of results other than actuals and in-progress results.**|
|DisplayName|**Custom Rollup Field (Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customrollupfielddecimal`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|10|
|SourceTypeMask|0|

### <a name="BKMK_CustomRollupFieldInteger"></a> CustomRollupFieldInteger

|Property|Value|
|---|---|
|Description|**Indicates a placeholder rollup field for an integer value to track a third category of results other than actuals and in-progress results.**|
|DisplayName|**Custom Rollup Field (Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customrollupfieldinteger`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CustomRollupFieldMoney"></a> CustomRollupFieldMoney

|Property|Value|
|---|---|
|Description|**Indicates a placeholder rollup field for a money value to track a third category of results other than actuals and in-progress results.**|
|DisplayName|**Custom Rollup Field (Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customrollupfieldmoney`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

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

### <a name="BKMK_FiscalPeriod"></a> FiscalPeriod

|Property|Value|
|---|---|
|Description|**Select the fiscal period for the goal.**|
|DisplayName|**Fiscal Period**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fiscalperiod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`goal_fiscalperiod`|

#### FiscalPeriod Choices/Options

|Value|Label|
|---|---|
|1|**Quarter 1**|
|2|**Quarter 2**|
|3|**Quarter 3**|
|4|**Quarter 4**|
|101|**January**|
|102|**February**|
|103|**March**|
|104|**April**|
|105|**May**|
|106|**June**|
|107|**July**|
|108|**August**|
|109|**September**|
|110|**October**|
|111|**November**|
|112|**December**|
|201|**Semester 1**|
|202|**Semester 2**|
|301|**Annual**|
|401|**P1**|
|402|**P2**|
|403|**P3**|
|404|**P4**|
|405|**P5**|
|406|**P6**|
|407|**P7**|
|408|**P8**|
|409|**P9**|
|410|**P10**|
|411|**P11**|
|412|**P12**|
|413|**P13**|

### <a name="BKMK_FiscalYear"></a> FiscalYear

|Property|Value|
|---|---|
|Description|**Select the fiscal year for the goal that's being tracked.**|
|DisplayName|**Fiscal Year**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fiscalyear`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`goal_fiscalyear`|

#### FiscalYear Choices/Options

|Value|Label|
|---|---|
|1970|**FY1970**|
|1971|**FY1971**|
|1972|**FY1972**|
|1973|**FY1973**|
|1974|**FY1974**|
|1975|**FY1975**|
|1976|**FY1976**|
|1977|**FY1977**|
|1978|**FY1978**|
|1979|**FY1979**|
|1980|**FY1980**|
|1981|**FY1981**|
|1982|**FY1982**|
|1983|**FY1983**|
|1984|**FY1984**|
|1985|**FY1985**|
|1986|**FY1986**|
|1987|**FY1987**|
|1988|**FY1988**|
|1989|**FY1989**|
|1990|**FY1990**|
|1991|**FY1991**|
|1992|**FY1992**|
|1993|**FY1993**|
|1994|**FY1994**|
|1995|**FY1995**|
|1996|**FY1996**|
|1997|**FY1997**|
|1998|**FY1998**|
|1999|**FY1999**|
|2000|**FY2000**|
|2001|**FY2001**|
|2002|**FY2002**|
|2003|**FY2003**|
|2004|**FY2004**|
|2005|**FY2005**|
|2006|**FY2006**|
|2007|**FY2007**|
|2008|**FY2008**|
|2009|**FY2009**|
|2010|**FY2010**|
|2011|**FY2011**|
|2012|**FY2012**|
|2013|**FY2013**|
|2014|**FY2014**|
|2015|**FY2015**|
|2016|**FY2016**|
|2017|**FY2017**|
|2018|**FY2018**|
|2019|**FY2019**|
|2020|**FY2020**|
|2021|**FY2021**|
|2022|**FY2022**|
|2023|**FY2023**|
|2024|**FY2024**|
|2025|**FY2025**|
|2026|**FY2026**|
|2027|**FY2027**|
|2028|**FY2028**|
|2029|**FY2029**|
|2030|**FY2030**|
|2031|**FY2031**|
|2032|**FY2032**|
|2033|**FY2033**|
|2034|**FY2034**|
|2035|**FY2035**|
|2036|**FY2036**|
|2037|**FY2037**|
|2038|**FY2038**|

### <a name="BKMK_GoalEndDate"></a> GoalEndDate

|Property|Value|
|---|---|
|Description|**Enter the date when the goal ends.**|
|DisplayName|**To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`goalenddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_GoalId"></a> GoalId

|Property|Value|
|---|---|
|Description|**Unique identifier of the goal.**|
|DisplayName|**Goal**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`goalid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_GoalOwnerId"></a> GoalOwnerId

|Property|Value|
|---|---|
|Description|**Choose the user or team responsible for meeting the goal.**|
|DisplayName|**Goal Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`goalownerid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|systemuser, team|

### <a name="BKMK_GoalOwnerIdType"></a> GoalOwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Goal Owner Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`goalowneridtype`|
|RequiredLevel|ApplicationRequired|
|Type|EntityName|

### <a name="BKMK_GoalStartDate"></a> GoalStartDate

|Property|Value|
|---|---|
|Description|**Enter the date and time when the period for tracking the goal begins.**|
|DisplayName|**From**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`goalstartdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_GoalWithErrorId"></a> GoalWithErrorId

|Property|Value|
|---|---|
|Description|**Unique identifier of the goal that caused an error in the rollup of the goal hierarchy.**|
|DisplayName|**Goal With Error**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`goalwitherrorid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goal|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_InProgressDecimal"></a> InProgressDecimal

|Property|Value|
|---|---|
|Description|**Shows the in-progress value (decimal) against the target. This value could contribute to a goal, but is not counted yet as actual.**|
|DisplayName|**In-progress (Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inprogressdecimal`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|10|
|SourceTypeMask|0|

### <a name="BKMK_InProgressInteger"></a> InProgressInteger

|Property|Value|
|---|---|
|Description|**Shows the in-progress value (integer) against the target. This value could contribute to a goal, but is not counted yet as actual.**|
|DisplayName|**In-progress (Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inprogressinteger`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_InProgressMoney"></a> InProgressMoney

|Property|Value|
|---|---|
|Description|**Shows the in-progress value (money) against the target. This value could contribute to a goal, but is not counted yet as actual.**|
|DisplayName|**In-progress (Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inprogressmoney`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_IsAmount"></a> IsAmount

|Property|Value|
|---|---|
|Description|**Indicates whether the metric type is Count or Amount.**|
|DisplayName|**Metric Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isamount`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`metric_type`|
|DefaultValue|True|
|True Label|Amount|
|False Label|Count|

### <a name="BKMK_IsFiscalPeriodGoal"></a> IsFiscalPeriodGoal

|Property|Value|
|---|---|
|Description|**Select whether the goal period is a fiscal period or custom period.**|
|DisplayName|**Goal Period Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isfiscalperiodgoal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`goal_isfiscalperiodgoal`|
|DefaultValue|True|
|True Label|Fiscal Period|
|False Label|Custom Period|

### <a name="BKMK_IsOverridden"></a> IsOverridden

|Property|Value|
|---|---|
|Description|**Select whether the system rollup fields are updated. If set to Yes, the next system rollup will not update the values of the rollup fields with the system calculated values.**|
|DisplayName|**Overridden**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isoverridden`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`goal_isoverridden`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOverride"></a> IsOverride

|Property|Value|
|---|---|
|Description|**Indicates whether the values of system rollup fields can be updated.**|
|DisplayName|**Override**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isoverride`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`goal_isoverride`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LastRolledupDate"></a> LastRolledupDate

|Property|Value|
|---|---|
|Description|**Shows the date and time when the goal was last rolled up. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Last Rolled Up Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastrolledupdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_MetricId"></a> MetricId

|Property|Value|
|---|---|
|Description|**Choose the metric for the goal. This metric determines how the goal is tracked.**|
|DisplayName|**Goal Metric**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`metricid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|metric|

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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Manager**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ParentGoalId"></a> ParentGoalId

|Property|Value|
|---|---|
|Description|**Choose a parent goal if the current goal is a child goal. This sets up a parent-child relationship for reporting and analytics.**|
|DisplayName|**Parent Goal**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentgoalid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goal|

### <a name="BKMK_Percentage"></a> Percentage

|Property|Value|
|---|---|
|Description|**Shows the percentage achieved against the target goal.**|
|DisplayName|**Percentage Achieved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`percentage`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|0|
|SourceTypeMask|0|

### <a name="BKMK_RollupErrorCode"></a> RollupErrorCode

|Property|Value|
|---|---|
|Description|**Error code associated with rollup.**|
|DisplayName|**Rollup Error Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rolluperrorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_RollupOnlyFromChildGoals"></a> RollupOnlyFromChildGoals

|Property|Value|
|---|---|
|Description|**Select whether the data should be rolled up only from the child goals.**|
|DisplayName|**Roll Up Only from Child Goals**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rolluponlyfromchildgoals`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`goal_rolluponlyfromchildgoals`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RollUpQueryActualDecimalId"></a> RollUpQueryActualDecimalId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate the actual data for the goal (decimal).**|
|DisplayName|**Rollup Query - Actual(Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupqueryactualdecimalid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollupQueryActualIntegerId"></a> RollupQueryActualIntegerId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate the actual data for the goal (integer).**|
|DisplayName|**Rollup Query - Actual(Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupqueryactualintegerid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollUpQueryActualMoneyId"></a> RollUpQueryActualMoneyId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate the actual data for the goal (money).**|
|DisplayName|**Rollup Query - Actual(Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupqueryactualmoneyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollUpQueryCustomDecimalId"></a> RollUpQueryCustomDecimalId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate data for the custom rollup field (decimal).**|
|DisplayName|**Rollup Query - Custom Rollup Field (Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupquerycustomdecimalid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollUpQueryCustomIntegerId"></a> RollUpQueryCustomIntegerId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate data for the custom rollup field (integer).**|
|DisplayName|**Rollup Query - Custom Rollup Field (Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupquerycustomintegerid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollUpQueryCustomMoneyId"></a> RollUpQueryCustomMoneyId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate data for the custom rollup field (money).**|
|DisplayName|**Rollup Query - Custom Rollup Field (Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupquerycustommoneyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollUpQueryInprogressDecimalId"></a> RollUpQueryInprogressDecimalId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate data for the in-progress rollup field (decimal).**|
|DisplayName|**Rollup Query - In-progress(Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupqueryinprogressdecimalid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollUpQueryInprogressIntegerId"></a> RollUpQueryInprogressIntegerId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate data for the in-progress rollup field (integer).**|
|DisplayName|**Rollup Query - In-progress(Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupqueryinprogressintegerid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_RollUpQueryInprogressMoneyId"></a> RollUpQueryInprogressMoneyId

|Property|Value|
|---|---|
|Description|**Choose the query that will be used to calculate data for the in-progress rollup field (money).**|
|DisplayName|**Rollup Query - In-progress(Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rollupqueryinprogressmoneyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|goalrollupquery|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the goal is open, completed, or canceled. Completed and canceled goals are read-only and can't be edited.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`goal_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 0<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 1<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the goal's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`goal_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Open**<br />State:0<br />TransitionData: None|
|1|Label: **Closed**<br />State:1<br />TransitionData: None|
|2|Label: **Discarded**<br />State:1<br />TransitionData: None|

### <a name="BKMK_StretchTargetDecimal"></a> StretchTargetDecimal

|Property|Value|
|---|---|
|Description|**Select a stretch target (decimal) of the goal to define a higher or difficult level of goal than the usual ones.**|
|DisplayName|**Stretch Target (Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stretchtargetdecimal`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_StretchTargetInteger"></a> StretchTargetInteger

|Property|Value|
|---|---|
|Description|**Select the stretch target (integer) of the goal to define a higher or difficult level of goal than the usual ones.**|
|DisplayName|**Stretch Target (Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stretchtargetinteger`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_StretchTargetMoney"></a> StretchTargetMoney

|Property|Value|
|---|---|
|Description|**Select stretch target (money) of the goal to define a higher or difficult level of goal than the usual ones.**|
|DisplayName|**Stretch Target (Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stretchtargetmoney`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|922337203685477|
|MinValue|0|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_TargetDecimal"></a> TargetDecimal

|Property|Value|
|---|---|
|Description|**Select a goal target of the decimal type to use for tracking data that include partial numbers, such as pounds sold of a product sold by weight.**|
|DisplayName|**Target (Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetdecimal`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_TargetInteger"></a> TargetInteger

|Property|Value|
|---|---|
|Description|**Select a goal target of the integer type to use for tracking anything countable in whole numbers, such as units sold.**|
|DisplayName|**Target (Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetinteger`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_TargetMoney"></a> TargetMoney

|Property|Value|
|---|---|
|Description|**Select a goal target (money) to track a monetary amount such as revenue from a product.**|
|DisplayName|**Target (Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetmoney`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|False|
|MaxValue|922337203685477|
|MinValue|0|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**Type a title or name that describes the goal.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ActualMoney_Base](#BKMK_ActualMoney_Base)
- [ActualString](#BKMK_ActualString)
- [ComputedTargetAsOfTodayDecimal](#BKMK_ComputedTargetAsOfTodayDecimal)
- [ComputedTargetAsOfTodayInteger](#BKMK_ComputedTargetAsOfTodayInteger)
- [ComputedTargetAsOfTodayMoney](#BKMK_ComputedTargetAsOfTodayMoney)
- [ComputedTargetAsOfTodayMoney_Base](#BKMK_ComputedTargetAsOfTodayMoney_Base)
- [ComputedTargetAsOfTodayPercentageAchieved](#BKMK_ComputedTargetAsOfTodayPercentageAchieved)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomRollupFieldMoney_Base](#BKMK_CustomRollupFieldMoney_Base)
- [CustomRollupFieldString](#BKMK_CustomRollupFieldString)
- [Depth](#BKMK_Depth)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [InProgressMoney_Base](#BKMK_InProgressMoney_Base)
- [InProgressString](#BKMK_InProgressString)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [StretchTargetMoney_Base](#BKMK_StretchTargetMoney_Base)
- [StretchTargetString](#BKMK_StretchTargetString)
- [TargetMoney_Base](#BKMK_TargetMoney_Base)
- [TargetString](#BKMK_TargetString)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TreeId](#BKMK_TreeId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ActualMoney_Base"></a> ActualMoney_Base

|Property|Value|
|---|---|
|Description|**Shows the actual value (money type) in base currency to track goal results against the target.**|
|DisplayName|**Actual (Money) (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualmoney_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_ActualString"></a> ActualString

|Property|Value|
|---|---|
|Description|**Actual Value of the goal.**|
|DisplayName|**Actual**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`actualstring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ComputedTargetAsOfTodayDecimal"></a> ComputedTargetAsOfTodayDecimal

|Property|Value|
|---|---|
|Description|**Shows the expected amount for actual value (decimal type) against the target goal.**|
|DisplayName|**Today's Target (Decimal)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedtargetasoftodaydecimal`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_ComputedTargetAsOfTodayInteger"></a> ComputedTargetAsOfTodayInteger

|Property|Value|
|---|---|
|Description|**Shows the expected amount for actual value (integer type) against the target goal as of the current date.**|
|DisplayName|**Today's Target (Integer)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedtargetasoftodayinteger`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ComputedTargetAsOfTodayMoney"></a> ComputedTargetAsOfTodayMoney

|Property|Value|
|---|---|
|Description|**Shows the expected amount for actual value (money type) against the target goal as of the current date.**|
|DisplayName|**Today's Target (Money)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedtargetasoftodaymoney`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Auto|
|IsBaseCurrency|False|
|MaxValue|922337203685477|
|MinValue|0|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_ComputedTargetAsOfTodayMoney_Base"></a> ComputedTargetAsOfTodayMoney_Base

|Property|Value|
|---|---|
|Description|**Shows the expected amount in base currency for actual value (money type) against the target goal as of the current date.**|
|DisplayName|**Today's Target (Money) (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedtargetasoftodaymoney_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_ComputedTargetAsOfTodayPercentageAchieved"></a> ComputedTargetAsOfTodayPercentageAchieved

|Property|Value|
|---|---|
|Description|**Shows the expected value for percentage achieved against the target goal as of the current date.**|
|DisplayName|**Today's Target (Percentage Achieved)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedtargetasoftodaypercentageachieved`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|0|
|Precision|0|
|SourceTypeMask|0|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CustomRollupFieldMoney_Base"></a> CustomRollupFieldMoney_Base

|Property|Value|
|---|---|
|Description|**Indicates a placeholder rollup field for a money value in base currency to track a third category of results other than actuals and in-progress results.**|
|DisplayName|**Custom Rollup Field (Money) (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customrollupfieldmoney_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_CustomRollupFieldString"></a> CustomRollupFieldString

|Property|Value|
|---|---|
|Description|**Placeholder rollup field for the goal.**|
|DisplayName|**Custom Rollup Field**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customrollupfieldstring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Depth"></a> Depth

|Property|Value|
|---|---|
|Description|**Depth of the goal in the tree.**|
|DisplayName|**Depth**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`depth`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.**|
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

### <a name="BKMK_InProgressMoney_Base"></a> InProgressMoney_Base

|Property|Value|
|---|---|
|Description|**Shows the in-progress value (money) in base currency to track goal results against the target.**|
|DisplayName|**In-progress (Money) (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inprogressmoney_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_InProgressString"></a> InProgressString

|Property|Value|
|---|---|
|Description|**In-progress value of the goal.**|
|DisplayName|**In-Progress**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inprogressstring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the manager**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier of the team who owns the goal.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user who owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_StretchTargetMoney_Base"></a> StretchTargetMoney_Base

|Property|Value|
|---|---|
|Description|**Shows the stretch target (money) in base currency to indicate a higher or difficult level of goal than the usual ones.**|
|DisplayName|**Stretch Target (Money) (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stretchtargetmoney_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_StretchTargetString"></a> StretchTargetString

|Property|Value|
|---|---|
|Description|**Stretch target value for all data types.**|
|DisplayName|**Stretched Target**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stretchtargetstring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TargetMoney_Base"></a> TargetMoney_Base

|Property|Value|
|---|---|
|Description|**Shows the goal target of the money type in base currency.**|
|DisplayName|**Target (Money) (Base)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetmoney_base`|
|RequiredLevel|None|
|Type|Money|
|ImeMode|Disabled|
|IsBaseCurrency|True|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2 (TransactionCurrency.CurrencyPrecision)|

### <a name="BKMK_TargetString"></a> TargetString

|Property|Value|
|---|---|
|Description|**Target value of the goal.**|
|DisplayName|**Target**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`targetstring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Choose the local currency for the record to make sure budgets are reported in the correct currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_TreeId"></a> TreeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the goal tree.**|
|DisplayName|**Tree ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`treeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the goal.**|
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

- [business_unit_goal](#BKMK_business_unit_goal)
- [goal_parent_goal](#BKMK_goal_parent_goal-many-to-one)
- [Goal_RollupError_Goal](#BKMK_Goal_RollupError_Goal-many-to-one)
- [goal_rollupquery_actualdecimal](#BKMK_goal_rollupquery_actualdecimal)
- [goal_rollupquery_actualmoney](#BKMK_goal_rollupquery_actualmoney)
- [goal_rollupquery_customdecimal](#BKMK_goal_rollupquery_customdecimal)
- [goal_rollupquery_customint](#BKMK_goal_rollupquery_customint)
- [goal_rollupquery_custommoney](#BKMK_goal_rollupquery_custommoney)
- [goal_rollupquery_inprogressdecimal](#BKMK_goal_rollupquery_inprogressdecimal)
- [goal_rollupquery_inprogressint](#BKMK_goal_rollupquery_inprogressint)
- [goal_rollupquery_inprogressmoney](#BKMK_goal_rollupquery_inprogressmoney)
- [goalrollupquery_actualint](#BKMK_goalrollupquery_actualint)
- [lk_goal_createdby](#BKMK_lk_goal_createdby)
- [lk_goal_createdonbehalfby](#BKMK_lk_goal_createdonbehalfby)
- [lk_goal_modifiedby](#BKMK_lk_goal_modifiedby)
- [lk_goal_modifiedonbehalfby](#BKMK_lk_goal_modifiedonbehalfby)
- [metric_goal](#BKMK_metric_goal)
- [owner_goal](#BKMK_owner_goal)
- [team_goal](#BKMK_team_goal)
- [team_goal_goalowner](#BKMK_team_goal_goalowner)
- [TransactionCurrency_Goal](#BKMK_TransactionCurrency_Goal)
- [user_goal](#BKMK_user_goal)
- [user_goal_goalowner](#BKMK_user_goal_goalowner)

### <a name="BKMK_business_unit_goal"></a> business_unit_goal

One-To-Many Relationship: [businessunit business_unit_goal](businessunit.md#BKMK_business_unit_goal)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_parent_goal-many-to-one"></a> goal_parent_goal

One-To-Many Relationship: [goal goal_parent_goal](#BKMK_goal_parent_goal-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`parentgoalid`|
|ReferencingEntityNavigationPropertyName|`parentgoalid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Goal_RollupError_Goal-many-to-one"></a> Goal_RollupError_Goal

One-To-Many Relationship: [goal Goal_RollupError_Goal](#BKMK_Goal_RollupError_Goal-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`goalwitherrorid`|
|ReferencingEntityNavigationPropertyName|`goalwitherrorid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_actualdecimal"></a> goal_rollupquery_actualdecimal

One-To-Many Relationship: [goalrollupquery goal_rollupquery_actualdecimal](goalrollupquery.md#BKMK_goal_rollupquery_actualdecimal)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupqueryactualdecimalid`|
|ReferencingEntityNavigationPropertyName|`rollupqueryactualdecimalid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_actualmoney"></a> goal_rollupquery_actualmoney

One-To-Many Relationship: [goalrollupquery goal_rollupquery_actualmoney](goalrollupquery.md#BKMK_goal_rollupquery_actualmoney)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupqueryactualmoneyid`|
|ReferencingEntityNavigationPropertyName|`rollupqueryactualmoneyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_customdecimal"></a> goal_rollupquery_customdecimal

One-To-Many Relationship: [goalrollupquery goal_rollupquery_customdecimal](goalrollupquery.md#BKMK_goal_rollupquery_customdecimal)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupquerycustomdecimalid`|
|ReferencingEntityNavigationPropertyName|`rollupquerycustomdecimalid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_customint"></a> goal_rollupquery_customint

One-To-Many Relationship: [goalrollupquery goal_rollupquery_customint](goalrollupquery.md#BKMK_goal_rollupquery_customint)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupquerycustomintegerid`|
|ReferencingEntityNavigationPropertyName|`rollupquerycustomintegerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_custommoney"></a> goal_rollupquery_custommoney

One-To-Many Relationship: [goalrollupquery goal_rollupquery_custommoney](goalrollupquery.md#BKMK_goal_rollupquery_custommoney)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupquerycustommoneyid`|
|ReferencingEntityNavigationPropertyName|`rollupquerycustommoneyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_inprogressdecimal"></a> goal_rollupquery_inprogressdecimal

One-To-Many Relationship: [goalrollupquery goal_rollupquery_inprogressdecimal](goalrollupquery.md#BKMK_goal_rollupquery_inprogressdecimal)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupqueryinprogressdecimalid`|
|ReferencingEntityNavigationPropertyName|`rollupqueryinprogressdecimalid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_inprogressint"></a> goal_rollupquery_inprogressint

One-To-Many Relationship: [goalrollupquery goal_rollupquery_inprogressint](goalrollupquery.md#BKMK_goal_rollupquery_inprogressint)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupqueryinprogressintegerid`|
|ReferencingEntityNavigationPropertyName|`rollupqueryinprogressintegerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_rollupquery_inprogressmoney"></a> goal_rollupquery_inprogressmoney

One-To-Many Relationship: [goalrollupquery goal_rollupquery_inprogressmoney](goalrollupquery.md#BKMK_goal_rollupquery_inprogressmoney)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupqueryinprogressmoneyid`|
|ReferencingEntityNavigationPropertyName|`rollupqueryinprogressmoneyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goalrollupquery_actualint"></a> goalrollupquery_actualint

One-To-Many Relationship: [goalrollupquery goalrollupquery_actualint](goalrollupquery.md#BKMK_goalrollupquery_actualint)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`rollupqueryactualintegerid`|
|ReferencingEntityNavigationPropertyName|`rollupqueryactualintegerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goal_createdby"></a> lk_goal_createdby

One-To-Many Relationship: [systemuser lk_goal_createdby](systemuser.md#BKMK_lk_goal_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goal_createdonbehalfby"></a> lk_goal_createdonbehalfby

One-To-Many Relationship: [systemuser lk_goal_createdonbehalfby](systemuser.md#BKMK_lk_goal_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goal_modifiedby"></a> lk_goal_modifiedby

One-To-Many Relationship: [systemuser lk_goal_modifiedby](systemuser.md#BKMK_lk_goal_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goal_modifiedonbehalfby"></a> lk_goal_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_goal_modifiedonbehalfby](systemuser.md#BKMK_lk_goal_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metric_goal"></a> metric_goal

One-To-Many Relationship: [metric metric_goal](metric.md#BKMK_metric_goal)

|Property|Value|
|---|---|
|ReferencedEntity|`metric`|
|ReferencedAttribute|`metricid`|
|ReferencingAttribute|`metricid`|
|ReferencingEntityNavigationPropertyName|`metricid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_goal"></a> owner_goal

One-To-Many Relationship: [owner owner_goal](owner.md#BKMK_owner_goal)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_goal"></a> team_goal

One-To-Many Relationship: [team team_goal](team.md#BKMK_team_goal)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_goal_goalowner"></a> team_goal_goalowner

One-To-Many Relationship: [team team_goal_goalowner](team.md#BKMK_team_goal_goalowner)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`goalownerid`|
|ReferencingEntityNavigationPropertyName|`goalownerid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_Goal"></a> TransactionCurrency_Goal

One-To-Many Relationship: [transactioncurrency TransactionCurrency_Goal](transactioncurrency.md#BKMK_TransactionCurrency_Goal)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_goal"></a> user_goal

One-To-Many Relationship: [systemuser user_goal](systemuser.md#BKMK_user_goal)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_goal_goalowner"></a> user_goal_goalowner

One-To-Many Relationship: [systemuser user_goal_goalowner](systemuser.md#BKMK_user_goal_goalowner)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`goalownerid`|
|ReferencingEntityNavigationPropertyName|`goalownerid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [Goal_Annotation](#BKMK_Goal_Annotation)
- [Goal_AsyncOperations](#BKMK_Goal_AsyncOperations)
- [goal_connections1](#BKMK_goal_connections1)
- [goal_connections2](#BKMK_goal_connections2)
- [Goal_DuplicateBaseRecord](#BKMK_Goal_DuplicateBaseRecord)
- [Goal_DuplicateMatchingRecord](#BKMK_Goal_DuplicateMatchingRecord)
- [goal_parent_goal](#BKMK_goal_parent_goal-one-to-many)
- [goal_principalobjectattributeaccess](#BKMK_goal_principalobjectattributeaccess)
- [Goal_ProcessSessions](#BKMK_Goal_ProcessSessions)
- [Goal_RollupError_Goal](#BKMK_Goal_RollupError_Goal-one-to-many)
- [Goal_SyncErrors](#BKMK_Goal_SyncErrors)

### <a name="BKMK_Goal_Annotation"></a> Goal_Annotation

Many-To-One Relationship: [annotation Goal_Annotation](annotation.md#BKMK_Goal_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Goal_Annotation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Goal_AsyncOperations"></a> Goal_AsyncOperations

Many-To-One Relationship: [asyncoperation Goal_AsyncOperations](asyncoperation.md#BKMK_Goal_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Goal_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_connections1"></a> goal_connections1

Many-To-One Relationship: [connection goal_connections1](connection.md#BKMK_goal_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`goal_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_connections2"></a> goal_connections2

Many-To-One Relationship: [connection goal_connections2](connection.md#BKMK_goal_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`goal_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Goal_DuplicateBaseRecord"></a> Goal_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Goal_DuplicateBaseRecord](duplicaterecord.md#BKMK_Goal_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Goal_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Goal_DuplicateMatchingRecord"></a> Goal_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Goal_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Goal_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Goal_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_parent_goal-one-to-many"></a> goal_parent_goal

Many-To-One Relationship: [goal goal_parent_goal](#BKMK_goal_parent_goal-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`parentgoalid`|
|ReferencedEntityNavigationPropertyName|`goal_parent_goal`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 140<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_principalobjectattributeaccess"></a> goal_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess goal_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_goal_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`goal_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Goal_ProcessSessions"></a> Goal_ProcessSessions

Many-To-One Relationship: [processsession Goal_ProcessSessions](processsession.md#BKMK_Goal_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Goal_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Goal_RollupError_Goal-one-to-many"></a> Goal_RollupError_Goal

Many-To-One Relationship: [goal Goal_RollupError_Goal](#BKMK_Goal_RollupError_Goal-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`goalwitherrorid`|
|ReferencedEntityNavigationPropertyName|`Goal_RollupError_Goal`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Goal_SyncErrors"></a> Goal_SyncErrors

Many-To-One Relationship: [syncerror Goal_SyncErrors](syncerror.md#BKMK_Goal_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Goal_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.goal?displayProperty=fullName>
