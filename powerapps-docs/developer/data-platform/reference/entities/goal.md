---
title: "Goal table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Goal table/entity."
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

# Goal table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Target objective for a user or a team for a specified time period.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/goals(*goalid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/goals<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/goals(*goalid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Recalculate|<xref href="Microsoft.Dynamics.CRM.Recalculate?text=Recalculate Action" />|<xref:Microsoft.Crm.Sdk.Messages.RecalculateRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/goals(*goalid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/goals<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/goals(*goalid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/goals(*goalid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Goals|
|DisplayCollectionName|Goals|
|DisplayName|Goal|
|EntitySetName|goals|
|IsBPFEntity|False|
|LogicalCollectionName|goals|
|LogicalName|goal|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|goalid|
|PrimaryNameAttribute|title|
|SchemaName|Goal|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Shows the actual value (Decimal type) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount and the amount data type is Decimal.|
|DisplayName|Actual (Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualdecimal|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ActualInteger"></a> ActualInteger

|Property|Value|
|--------|-----|
|Description|Shows the actual value (integer) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount or Count and the amount data type is Integer.|
|DisplayName|Actual (Integer)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualinteger|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ActualMoney"></a> ActualMoney

|Property|Value|
|--------|-----|
|Description|Shows the actual value (Money type) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount and the amount data type is Money.|
|DisplayName|Actual (Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualmoney|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_AmountDataType"></a> AmountDataType

|Property|Value|
|--------|-----|
|Description|Data type of the amount.|
|DisplayName|Amount Data Type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|amountdatatype|
|RequiredLevel|None|
|Type|Picklist|

#### AmountDataType Choices/Options

|Value|Label|
|-----|-----|
|0|Money|
|1|Decimal|
|2|Integer|



### <a name="BKMK_ConsiderOnlyGoalOwnersRecords"></a> ConsiderOnlyGoalOwnersRecords

|Property|Value|
|--------|-----|
|Description|Select whether only the goal owner's records, or all records, should be rolled up for goal results.|
|DisplayName|Record Set for Rollup|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|consideronlygoalownersrecords|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### ConsiderOnlyGoalOwnersRecords Choices/Options

|Value|Label|
|-----|-----|
|1|Owned by goal owner|
|0|All|

**DefaultValue**: True



### <a name="BKMK_CustomRollupFieldDecimal"></a> CustomRollupFieldDecimal

|Property|Value|
|--------|-----|
|Description|Indicates a placeholder rollup field for a decimal value to track a third category of results other than actuals and in-progress results.|
|DisplayName|Custom Rollup Field (Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customrollupfielddecimal|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_CustomRollupFieldInteger"></a> CustomRollupFieldInteger

|Property|Value|
|--------|-----|
|Description|Indicates a placeholder rollup field for an integer value to track a third category of results other than actuals and in-progress results.|
|DisplayName|Custom Rollup Field (Integer)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customrollupfieldinteger|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_CustomRollupFieldMoney"></a> CustomRollupFieldMoney

|Property|Value|
|--------|-----|
|Description|Indicates a placeholder rollup field for a money value to track a third category of results other than actuals and in-progress results.|
|DisplayName|Custom Rollup Field (Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customrollupfieldmoney|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|--------|-----|
|Description|The default image for the entity.|
|DisplayName|Entity Image|
|IsPrimaryImage|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage|
|MaxHeight|144|
|MaxWidth|144|
|RequiredLevel|None|
|Type|Image|


### <a name="BKMK_FiscalPeriod"></a> FiscalPeriod

|Property|Value|
|--------|-----|
|Description|Select the fiscal period for the goal.|
|DisplayName|Fiscal Period|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fiscalperiod|
|RequiredLevel|None|
|Type|Picklist|

#### FiscalPeriod Choices/Options

|Value|Label|
|-----|-----|
|1|Quarter 1|
|2|Quarter 2|
|3|Quarter 3|
|4|Quarter 4|
|101|January|
|102|February|
|103|March|
|104|April|
|105|May|
|106|June|
|107|July|
|108|August|
|109|September|
|110|October|
|111|November|
|112|December|
|201|Semester 1|
|202|Semester 2|
|301|Annual|
|401|P1|
|402|P2|
|403|P3|
|404|P4|
|405|P5|
|406|P6|
|407|P7|
|408|P8|
|409|P9|
|410|P10|
|411|P11|
|412|P12|
|413|P13|



### <a name="BKMK_FiscalYear"></a> FiscalYear

|Property|Value|
|--------|-----|
|Description|Select the fiscal year for the goal that's being tracked.|
|DisplayName|Fiscal Year|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fiscalyear|
|RequiredLevel|None|
|Type|Picklist|

#### FiscalYear Choices/Options

|Value|Label|
|-----|-----|
|1970|FY1970|
|1971|FY1971|
|1972|FY1972|
|1973|FY1973|
|1974|FY1974|
|1975|FY1975|
|1976|FY1976|
|1977|FY1977|
|1978|FY1978|
|1979|FY1979|
|1980|FY1980|
|1981|FY1981|
|1982|FY1982|
|1983|FY1983|
|1984|FY1984|
|1985|FY1985|
|1986|FY1986|
|1987|FY1987|
|1988|FY1988|
|1989|FY1989|
|1990|FY1990|
|1991|FY1991|
|1992|FY1992|
|1993|FY1993|
|1994|FY1994|
|1995|FY1995|
|1996|FY1996|
|1997|FY1997|
|1998|FY1998|
|1999|FY1999|
|2000|FY2000|
|2001|FY2001|
|2002|FY2002|
|2003|FY2003|
|2004|FY2004|
|2005|FY2005|
|2006|FY2006|
|2007|FY2007|
|2008|FY2008|
|2009|FY2009|
|2010|FY2010|
|2011|FY2011|
|2012|FY2012|
|2013|FY2013|
|2014|FY2014|
|2015|FY2015|
|2016|FY2016|
|2017|FY2017|
|2018|FY2018|
|2019|FY2019|
|2020|FY2020|
|2021|FY2021|
|2022|FY2022|
|2023|FY2023|
|2024|FY2024|
|2025|FY2025|
|2026|FY2026|
|2027|FY2027|
|2028|FY2028|
|2029|FY2029|
|2030|FY2030|
|2031|FY2031|
|2032|FY2032|
|2033|FY2033|
|2034|FY2034|
|2035|FY2035|
|2036|FY2036|
|2037|FY2037|
|2038|FY2038|



### <a name="BKMK_GoalEndDate"></a> GoalEndDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the date when the goal ends.|
|DisplayName|To|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|goalenddate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_GoalId"></a> GoalId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the goal.|
|DisplayName|Goal|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|goalid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_GoalOwnerId"></a> GoalOwnerId

|Property|Value|
|--------|-----|
|Description|Choose the user or team responsible for meeting the goal.|
|DisplayName|Goal Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|goalownerid|
|RequiredLevel|ApplicationRequired|
|Targets|systemuser,team|
|Type|Lookup|


### <a name="BKMK_GoalOwnerIdType"></a> GoalOwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Goal Owner Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|goalowneridtype|
|RequiredLevel|ApplicationRequired|
|Type|EntityName|


### <a name="BKMK_GoalStartDate"></a> GoalStartDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the date and time when the period for tracking the goal begins.|
|DisplayName|From|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|goalstartdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_GoalWithErrorId"></a> GoalWithErrorId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the goal that caused an error in the rollup of the goal hierarchy.|
|DisplayName|Goal With Error|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|goalwitherrorid|
|RequiredLevel|None|
|Targets|goal|
|Type|Lookup|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_InProgressDecimal"></a> InProgressDecimal

|Property|Value|
|--------|-----|
|Description|Shows the in-progress value (decimal) against the target. This value could contribute to a goal, but is not counted yet as actual.|
|DisplayName|In-progress (Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|inprogressdecimal|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_InProgressInteger"></a> InProgressInteger

|Property|Value|
|--------|-----|
|Description|Shows the in-progress value (integer) against the target. This value could contribute to a goal, but is not counted yet as actual.|
|DisplayName|In-progress (Integer)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|inprogressinteger|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_InProgressMoney"></a> InProgressMoney

|Property|Value|
|--------|-----|
|Description|Shows the in-progress value (money) against the target. This value could contribute to a goal, but is not counted yet as actual.|
|DisplayName|In-progress (Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|inprogressmoney|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_IsAmount"></a> IsAmount

|Property|Value|
|--------|-----|
|Description|Indicates whether the metric type is Count or Amount.|
|DisplayName|Metric Type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|isamount|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### IsAmount Choices/Options

|Value|Label|
|-----|-----|
|1|Amount|
|0|Count|

**DefaultValue**: True



### <a name="BKMK_IsFiscalPeriodGoal"></a> IsFiscalPeriodGoal

|Property|Value|
|--------|-----|
|Description|Select whether the goal period is a fiscal period or custom period.|
|DisplayName|Goal Period Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isfiscalperiodgoal|
|RequiredLevel|None|
|Type|Boolean|

#### IsFiscalPeriodGoal Choices/Options

|Value|Label|
|-----|-----|
|1|Fiscal Period|
|0|Custom Period|

**DefaultValue**: True



### <a name="BKMK_IsOverridden"></a> IsOverridden

|Property|Value|
|--------|-----|
|Description|Select whether the system rollup fields are updated. If set to Yes, the next system rollup will not update the values of the rollup fields with the system calculated values.|
|DisplayName|Overridden|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isoverridden|
|RequiredLevel|None|
|Type|Boolean|

#### IsOverridden Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsOverride"></a> IsOverride

|Property|Value|
|--------|-----|
|Description|Indicates whether the values of system rollup fields can be updated.|
|DisplayName|Override|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isoverride|
|RequiredLevel|None|
|Type|Boolean|

#### IsOverride Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_LastRolledupDate"></a> LastRolledupDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the goal was last rolled up. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Last Rolled Up Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastrolledupdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_MetricId"></a> MetricId

|Property|Value|
|--------|-----|
|Description|Choose the metric for the goal. This metric determines how the goal is tracked.|
|DisplayName|Goal Metric|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|metricid|
|RequiredLevel|ApplicationRequired|
|Targets|metric|
|Type|Lookup|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
|DisplayName|Manager|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ParentGoalId"></a> ParentGoalId

|Property|Value|
|--------|-----|
|Description|Choose a parent goal if the current goal is a child goal. This sets up a parent-child relationship for reporting and analytics.|
|DisplayName|Parent Goal|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentgoalid|
|RequiredLevel|None|
|Targets|goal|
|Type|Lookup|


### <a name="BKMK_Percentage"></a> Percentage

|Property|Value|
|--------|-----|
|Description|Shows the percentage achieved against the target goal.|
|DisplayName|Percentage Achieved|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|percentage|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|0|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_RollupErrorCode"></a> RollupErrorCode

|Property|Value|
|--------|-----|
|Description|Error code associated with rollup.|
|DisplayName|Rollup Error Code|
|Format|None|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rolluperrorcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_RollupOnlyFromChildGoals"></a> RollupOnlyFromChildGoals

|Property|Value|
|--------|-----|
|Description|Select whether the data should be rolled up only from the child goals.|
|DisplayName|Roll Up Only from Child Goals|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rolluponlyfromchildgoals|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### RollupOnlyFromChildGoals Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_RollUpQueryActualDecimalId"></a> RollUpQueryActualDecimalId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate the actual data for the goal (decimal).|
|DisplayName|Rollup Query - Actual(Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupqueryactualdecimalid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollupQueryActualIntegerId"></a> RollupQueryActualIntegerId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate the actual data for the goal (integer).|
|DisplayName|Rollup Query - Actual(Integer)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupqueryactualintegerid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollUpQueryActualMoneyId"></a> RollUpQueryActualMoneyId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate the actual data for the goal (money).|
|DisplayName|Rollup Query - Actual(Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupqueryactualmoneyid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollUpQueryCustomDecimalId"></a> RollUpQueryCustomDecimalId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate data for the custom rollup field (decimal).|
|DisplayName|Rollup Query - Custom Rollup Field (Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupquerycustomdecimalid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollUpQueryCustomIntegerId"></a> RollUpQueryCustomIntegerId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate data for the custom rollup field (integer).|
|DisplayName|Rollup Query - Custom Rollup Field (Integer)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupquerycustomintegerid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollUpQueryCustomMoneyId"></a> RollUpQueryCustomMoneyId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate data for the custom rollup field (money).|
|DisplayName|Rollup Query - Custom Rollup Field (Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupquerycustommoneyid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollUpQueryInprogressDecimalId"></a> RollUpQueryInprogressDecimalId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate data for the in-progress rollup field (decimal).|
|DisplayName|Rollup Query - In-progress(Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupqueryinprogressdecimalid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollUpQueryInprogressIntegerId"></a> RollUpQueryInprogressIntegerId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate data for the in-progress rollup field (integer).|
|DisplayName|Rollup Query - In-progress(Integer)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupqueryinprogressintegerid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_RollUpQueryInprogressMoneyId"></a> RollUpQueryInprogressMoneyId

|Property|Value|
|--------|-----|
|Description|Choose the query that will be used to calculate data for the in-progress rollup field (money).|
|DisplayName|Rollup Query - In-progress(Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rollupqueryinprogressmoneyid|
|RequiredLevel|None|
|Targets|goalrollupquery|
|Type|Lookup|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the goal is open, completed, or canceled. Completed and canceled goals are read-only and can't be edited.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|0|Active|
|1|Inactive|1|Inactive|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the goal's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|0|Open|0|
|1|Closed|1|
|2|Discarded|1|



### <a name="BKMK_StretchTargetDecimal"></a> StretchTargetDecimal

|Property|Value|
|--------|-----|
|Description|Select a stretch target (decimal) of the goal to define a higher or difficult level of goal than the usual ones.|
|DisplayName|Stretch Target (Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stretchtargetdecimal|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_StretchTargetInteger"></a> StretchTargetInteger

|Property|Value|
|--------|-----|
|Description|Select the stretch target (integer) of the goal to define a higher or difficult level of goal than the usual ones.|
|DisplayName|Stretch Target (Integer)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stretchtargetinteger|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_StretchTargetMoney"></a> StretchTargetMoney

|Property|Value|
|--------|-----|
|Description|Select stretch target (money) of the goal to define a higher or difficult level of goal than the usual ones.|
|DisplayName|Stretch Target (Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stretchtargetmoney|
|MaxValue|922337203685477|
|MinValue|0|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_TargetDecimal"></a> TargetDecimal

|Property|Value|
|--------|-----|
|Description|Select a goal target of the decimal type to use for tracking data that include partial numbers, such as pounds sold of a product sold by weight.|
|DisplayName|Target (Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|targetdecimal|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_TargetInteger"></a> TargetInteger

|Property|Value|
|--------|-----|
|Description|Select a goal target of the integer type to use for tracking anything countable in whole numbers, such as units sold.|
|DisplayName|Target (Integer)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|targetinteger|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TargetMoney"></a> TargetMoney

|Property|Value|
|--------|-----|
|Description|Select a goal target (money) to track a monetary amount such as revenue from a product.|
|DisplayName|Target (Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|targetmoney|
|MaxValue|922337203685477|
|MinValue|0|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Title"></a> Title

|Property|Value|
|--------|-----|
|Description|Type a title or name that describes the goal.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|title|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
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

- [ActualMoney_Base](#BKMK_ActualMoney_Base)
- [ActualString](#BKMK_ActualString)
- [ComputedTargetAsOfTodayDecimal](#BKMK_ComputedTargetAsOfTodayDecimal)
- [ComputedTargetAsOfTodayInteger](#BKMK_ComputedTargetAsOfTodayInteger)
- [ComputedTargetAsOfTodayMoney](#BKMK_ComputedTargetAsOfTodayMoney)
- [ComputedTargetAsOfTodayMoney_Base](#BKMK_ComputedTargetAsOfTodayMoney_Base)
- [ComputedTargetAsOfTodayPercentageAchieved](#BKMK_ComputedTargetAsOfTodayPercentageAchieved)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomRollupFieldMoney_Base](#BKMK_CustomRollupFieldMoney_Base)
- [CustomRollupFieldString](#BKMK_CustomRollupFieldString)
- [Depth](#BKMK_Depth)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [GoalOwnerIdName](#BKMK_GoalOwnerIdName)
- [GoalOwnerIdYomiName](#BKMK_GoalOwnerIdYomiName)
- [GoalWithErrorIdName](#BKMK_GoalWithErrorIdName)
- [InProgressMoney_Base](#BKMK_InProgressMoney_Base)
- [InProgressString](#BKMK_InProgressString)
- [MetricIdName](#BKMK_MetricIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentGoalIdName](#BKMK_ParentGoalIdName)
- [RollUpQueryActualDecimalIdName](#BKMK_RollUpQueryActualDecimalIdName)
- [RollupQueryActualIntegerIdName](#BKMK_RollupQueryActualIntegerIdName)
- [RollUpQueryActualMoneyIdName](#BKMK_RollUpQueryActualMoneyIdName)
- [RollUpQueryCustomDecimalIdName](#BKMK_RollUpQueryCustomDecimalIdName)
- [RollUpQueryCustomIntegerIdName](#BKMK_RollUpQueryCustomIntegerIdName)
- [RollUpQueryCustomMoneyIdName](#BKMK_RollUpQueryCustomMoneyIdName)
- [RollUpQueryInprogressDecimalIdName](#BKMK_RollUpQueryInprogressDecimalIdName)
- [RollUpQueryInprogressIntegerIdName](#BKMK_RollUpQueryInprogressIntegerIdName)
- [RollUpQueryInprogressMoneyIdName](#BKMK_RollUpQueryInprogressMoneyIdName)
- [StretchTargetMoney_Base](#BKMK_StretchTargetMoney_Base)
- [StretchTargetString](#BKMK_StretchTargetString)
- [TargetMoney_Base](#BKMK_TargetMoney_Base)
- [TargetString](#BKMK_TargetString)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [TreeId](#BKMK_TreeId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ActualMoney_Base"></a> ActualMoney_Base

|Property|Value|
|--------|-----|
|Description|Shows the actual value (money type) in base currency to track goal results against the target.|
|DisplayName|Actual (Money) (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualmoney_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_ActualString"></a> ActualString

|Property|Value|
|--------|-----|
|Description|Actual Value of the goal.|
|DisplayName|Actual|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|actualstring|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ComputedTargetAsOfTodayDecimal"></a> ComputedTargetAsOfTodayDecimal

|Property|Value|
|--------|-----|
|Description|Shows the expected amount for actual value (decimal type) against the target goal.|
|DisplayName|Today's Target (Decimal)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedtargetasoftodaydecimal|
|MaxValue|100000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ComputedTargetAsOfTodayInteger"></a> ComputedTargetAsOfTodayInteger

|Property|Value|
|--------|-----|
|Description|Shows the expected amount for actual value (integer type) against the target goal as of the current date.|
|DisplayName|Today's Target (Integer)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedtargetasoftodayinteger|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ComputedTargetAsOfTodayMoney"></a> ComputedTargetAsOfTodayMoney

|Property|Value|
|--------|-----|
|Description|Shows the expected amount for actual value (money type) against the target goal as of the current date.|
|DisplayName|Today's Target (Money)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedtargetasoftodaymoney|
|MaxValue|922337203685477|
|MinValue|0|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_ComputedTargetAsOfTodayMoney_Base"></a> ComputedTargetAsOfTodayMoney_Base

|Property|Value|
|--------|-----|
|Description|Shows the expected amount in base currency for actual value (money type) against the target goal as of the current date.|
|DisplayName|Today's Target (Money) (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedtargetasoftodaymoney_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_ComputedTargetAsOfTodayPercentageAchieved"></a> ComputedTargetAsOfTodayPercentageAchieved

|Property|Value|
|--------|-----|
|Description|Shows the expected value for percentage achieved against the target goal as of the current date.|
|DisplayName|Today's Target (Percentage Achieved)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedtargetasoftodaypercentageachieved|
|MaxValue|100000000000|
|MinValue|0|
|Precision|0|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
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


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_CustomRollupFieldMoney_Base"></a> CustomRollupFieldMoney_Base

|Property|Value|
|--------|-----|
|Description|Indicates a placeholder rollup field for a money value in base currency to track a third category of results other than actuals and in-progress results.|
|DisplayName|Custom Rollup Field (Money) (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customrollupfieldmoney_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_CustomRollupFieldString"></a> CustomRollupFieldString

|Property|Value|
|--------|-----|
|Description|Placeholder rollup field for the goal.|
|DisplayName|Custom Rollup Field|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|customrollupfieldstring|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Depth"></a> Depth

|Property|Value|
|--------|-----|
|Description|Depth of the goal in the tree.|
|DisplayName|Depth|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|depth|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Entity Image Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_GoalOwnerIdName"></a> GoalOwnerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|goalowneridname|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_GoalOwnerIdYomiName"></a> GoalOwnerIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|goalowneridyominame|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_GoalWithErrorIdName"></a> GoalWithErrorIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|goalwitherroridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_InProgressMoney_Base"></a> InProgressMoney_Base

|Property|Value|
|--------|-----|
|Description|Shows the in-progress value (money) in base currency to track goal results against the target.|
|DisplayName|In-progress (Money) (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|inprogressmoney_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_InProgressString"></a> InProgressString

|Property|Value|
|--------|-----|
|Description|In-progress value of the goal.|
|DisplayName|In-Progress|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|inprogressstring|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MetricIdName"></a> MetricIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|metricidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record on behalf of another user.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description|Name of the manager|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the goal.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user who owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentGoalIdName"></a> ParentGoalIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentgoalidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryActualDecimalIdName"></a> RollUpQueryActualDecimalIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupqueryactualdecimalidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollupQueryActualIntegerIdName"></a> RollupQueryActualIntegerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupqueryactualintegeridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryActualMoneyIdName"></a> RollUpQueryActualMoneyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupqueryactualmoneyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryCustomDecimalIdName"></a> RollUpQueryCustomDecimalIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupquerycustomdecimalidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryCustomIntegerIdName"></a> RollUpQueryCustomIntegerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupquerycustomintegeridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryCustomMoneyIdName"></a> RollUpQueryCustomMoneyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupquerycustommoneyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryInprogressDecimalIdName"></a> RollUpQueryInprogressDecimalIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupqueryinprogressdecimalidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryInprogressIntegerIdName"></a> RollUpQueryInprogressIntegerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupqueryinprogressintegeridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RollUpQueryInprogressMoneyIdName"></a> RollUpQueryInprogressMoneyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rollupqueryinprogressmoneyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StretchTargetMoney_Base"></a> StretchTargetMoney_Base

|Property|Value|
|--------|-----|
|Description|Shows the stretch target (money) in base currency to indicate a higher or difficult level of goal than the usual ones.|
|DisplayName|Stretch Target (Money) (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stretchtargetmoney_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_StretchTargetString"></a> StretchTargetString

|Property|Value|
|--------|-----|
|Description|Stretch target value for all data types.|
|DisplayName|Stretched Target|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stretchtargetstring|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TargetMoney_Base"></a> TargetMoney_Base

|Property|Value|
|--------|-----|
|Description|Shows the goal target of the money type in base currency.|
|DisplayName|Target (Money) (Base)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|targetmoney_base|
|MaxValue|922337203685477|
|MinValue|-922337203685477|
|Precision|4|
|PrecisionSource|2|
|RequiredLevel|None|
|Type|Money|


### <a name="BKMK_TargetString"></a> TargetString

|Property|Value|
|--------|-----|
|Description|Target value of the goal.|
|DisplayName|Target|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|targetstring|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Choose the local currency for the record to make sure budgets are reported in the correct currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


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


### <a name="BKMK_TreeId"></a> TreeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the goal tree.|
|DisplayName|Tree ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|treeid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the goal.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [goal_parent_goal](#BKMK_goal_parent_goal)
- [Goal_DuplicateBaseRecord](#BKMK_Goal_DuplicateBaseRecord)
- [Goal_RollupError_Goal](#BKMK_Goal_RollupError_Goal)
- [Goal_SyncErrors](#BKMK_Goal_SyncErrors)
- [Goal_Annotation](#BKMK_Goal_Annotation)
- [Goal_AsyncOperations](#BKMK_Goal_AsyncOperations)
- [Goal_ProcessSessions](#BKMK_Goal_ProcessSessions)
- [goal_connections1](#BKMK_goal_connections1)
- [goal_connections2](#BKMK_goal_connections2)
- [Goal_DuplicateMatchingRecord](#BKMK_Goal_DuplicateMatchingRecord)
- [goal_principalobjectattributeaccess](#BKMK_goal_principalobjectattributeaccess)


### <a name="BKMK_goal_parent_goal"></a> goal_parent_goal

Same as goal table [goal_parent_goal](goal.md#BKMK_goal_parent_goal) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|parentgoalid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|goal_parent_goal|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 140|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Goal_DuplicateBaseRecord"></a> Goal_DuplicateBaseRecord

Same as duplicaterecord table [Goal_DuplicateBaseRecord](duplicaterecord.md#BKMK_Goal_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Goal_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Goal_RollupError_Goal"></a> Goal_RollupError_Goal

Same as goal table [Goal_RollupError_Goal](goal.md#BKMK_Goal_RollupError_Goal) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|goalwitherrorid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Goal_RollupError_Goal|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Goal_SyncErrors"></a> Goal_SyncErrors

Same as syncerror table [Goal_SyncErrors](syncerror.md#BKMK_Goal_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Goal_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Goal_Annotation"></a> Goal_Annotation

Same as annotation table [Goal_Annotation](annotation.md#BKMK_Goal_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Goal_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Goal_AsyncOperations"></a> Goal_AsyncOperations

Same as asyncoperation table [Goal_AsyncOperations](asyncoperation.md#BKMK_Goal_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Goal_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Goal_ProcessSessions"></a> Goal_ProcessSessions

Same as processsession table [Goal_ProcessSessions](processsession.md#BKMK_Goal_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Goal_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_goal_connections1"></a> goal_connections1

Same as connection table [goal_connections1](connection.md#BKMK_goal_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|goal_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_goal_connections2"></a> goal_connections2

Same as connection table [goal_connections2](connection.md#BKMK_goal_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|goal_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Goal_DuplicateMatchingRecord"></a> Goal_DuplicateMatchingRecord

Same as duplicaterecord table [Goal_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Goal_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Goal_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_goal_principalobjectattributeaccess"></a> goal_principalobjectattributeaccess

Same as principalobjectattributeaccess table [goal_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_goal_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|goal_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [team_goal](#BKMK_team_goal)
- [goalrollupquery_actualint](#BKMK_goalrollupquery_actualint)
- [goal_rollupquery_actualmoney](#BKMK_goal_rollupquery_actualmoney)
- [goal_rollupquery_actualdecimal](#BKMK_goal_rollupquery_actualdecimal)
- [goal_rollupquery_customint](#BKMK_goal_rollupquery_customint)
- [goal_rollupquery_custommoney](#BKMK_goal_rollupquery_custommoney)
- [goal_rollupquery_customdecimal](#BKMK_goal_rollupquery_customdecimal)
- [goal_rollupquery_inprogressint](#BKMK_goal_rollupquery_inprogressint)
- [goal_rollupquery_inprogressmoney](#BKMK_goal_rollupquery_inprogressmoney)
- [goal_rollupquery_inprogressdecimal](#BKMK_goal_rollupquery_inprogressdecimal)
- [lk_goal_createdby](#BKMK_lk_goal_createdby)
- [lk_goal_createdonbehalfby](#BKMK_lk_goal_createdonbehalfby)
- [lk_goal_modifiedby](#BKMK_lk_goal_modifiedby)
- [lk_goal_modifiedonbehalfby](#BKMK_lk_goal_modifiedonbehalfby)
- [user_goal](#BKMK_user_goal)
- [business_unit_goal](#BKMK_business_unit_goal)
- [user_goal_goalowner](#BKMK_user_goal_goalowner)
- [goal_parent_goal](#BKMK_goal_parent_goal)
- [TransactionCurrency_Goal](#BKMK_TransactionCurrency_Goal)
- [metric_goal](#BKMK_metric_goal)
- [Goal_RollupError_Goal](#BKMK_Goal_RollupError_Goal)
- [team_goal_goalowner](#BKMK_team_goal_goalowner)


### <a name="BKMK_team_goal"></a> team_goal

See team Table [team_goal](team.md#BKMK_team_goal) One-To-Many relationship.

### <a name="BKMK_goalrollupquery_actualint"></a> goalrollupquery_actualint

See goalrollupquery Table [goalrollupquery_actualint](goalrollupquery.md#BKMK_goalrollupquery_actualint) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_actualmoney"></a> goal_rollupquery_actualmoney

See goalrollupquery Table [goal_rollupquery_actualmoney](goalrollupquery.md#BKMK_goal_rollupquery_actualmoney) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_actualdecimal"></a> goal_rollupquery_actualdecimal

See goalrollupquery Table [goal_rollupquery_actualdecimal](goalrollupquery.md#BKMK_goal_rollupquery_actualdecimal) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_customint"></a> goal_rollupquery_customint

See goalrollupquery Table [goal_rollupquery_customint](goalrollupquery.md#BKMK_goal_rollupquery_customint) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_custommoney"></a> goal_rollupquery_custommoney

See goalrollupquery Table [goal_rollupquery_custommoney](goalrollupquery.md#BKMK_goal_rollupquery_custommoney) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_customdecimal"></a> goal_rollupquery_customdecimal

See goalrollupquery Table [goal_rollupquery_customdecimal](goalrollupquery.md#BKMK_goal_rollupquery_customdecimal) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_inprogressint"></a> goal_rollupquery_inprogressint

See goalrollupquery Table [goal_rollupquery_inprogressint](goalrollupquery.md#BKMK_goal_rollupquery_inprogressint) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_inprogressmoney"></a> goal_rollupquery_inprogressmoney

See goalrollupquery Table [goal_rollupquery_inprogressmoney](goalrollupquery.md#BKMK_goal_rollupquery_inprogressmoney) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_inprogressdecimal"></a> goal_rollupquery_inprogressdecimal

See goalrollupquery Table [goal_rollupquery_inprogressdecimal](goalrollupquery.md#BKMK_goal_rollupquery_inprogressdecimal) One-To-Many relationship.

### <a name="BKMK_lk_goal_createdby"></a> lk_goal_createdby

See systemuser Table [lk_goal_createdby](systemuser.md#BKMK_lk_goal_createdby) One-To-Many relationship.

### <a name="BKMK_lk_goal_createdonbehalfby"></a> lk_goal_createdonbehalfby

See systemuser Table [lk_goal_createdonbehalfby](systemuser.md#BKMK_lk_goal_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_goal_modifiedby"></a> lk_goal_modifiedby

See systemuser Table [lk_goal_modifiedby](systemuser.md#BKMK_lk_goal_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_goal_modifiedonbehalfby"></a> lk_goal_modifiedonbehalfby

See systemuser Table [lk_goal_modifiedonbehalfby](systemuser.md#BKMK_lk_goal_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_goal"></a> user_goal

See systemuser Table [user_goal](systemuser.md#BKMK_user_goal) One-To-Many relationship.

### <a name="BKMK_business_unit_goal"></a> business_unit_goal

See businessunit Table [business_unit_goal](businessunit.md#BKMK_business_unit_goal) One-To-Many relationship.

### <a name="BKMK_user_goal_goalowner"></a> user_goal_goalowner

See systemuser Table [user_goal_goalowner](systemuser.md#BKMK_user_goal_goalowner) One-To-Many relationship.

### <a name="BKMK_goal_parent_goal"></a> goal_parent_goal

See goal Table [goal_parent_goal](goal.md#BKMK_goal_parent_goal) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Goal"></a> TransactionCurrency_Goal

See transactioncurrency Table [TransactionCurrency_Goal](transactioncurrency.md#BKMK_TransactionCurrency_Goal) One-To-Many relationship.

### <a name="BKMK_metric_goal"></a> metric_goal

See metric Table [metric_goal](metric.md#BKMK_metric_goal) One-To-Many relationship.

### <a name="BKMK_Goal_RollupError_Goal"></a> Goal_RollupError_Goal

See goal Table [Goal_RollupError_Goal](goal.md#BKMK_Goal_RollupError_Goal) One-To-Many relationship.

### <a name="BKMK_team_goal_goalowner"></a> team_goal_goalowner

See team Table [team_goal_goalowner](team.md#BKMK_team_goal_goalowner) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.goal?text=goal EntityType" />