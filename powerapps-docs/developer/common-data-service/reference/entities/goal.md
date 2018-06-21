---
title: "Goal Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Goal entity."

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
# Goal Entity Reference

Target objective for a user or a team for a specified time period.

## Entity Properties

**DisplayName**: Goal<br />
**DisplayCollectionName**: Goals<br />
**SchemaName**: Goal<br />
**CollectionSchemaName**: Goals<br />
**LogicalName**: goal<br />
**LogicalCollectionName**: goals<br />
**EntitySetName**: goals<br />
**PrimaryIdAttribute**: goalid<br />
**PrimaryNameAttribute**: title<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Shows the actual value (Decimal type) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount and the amount data type is Decimal.<br />
**DisplayName**: Actual (Decimal)<br />
**LogicalName**: actualdecimal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: -100000000000<br />
**Precision**: 10


### <a name="BKMK_ActualInteger"></a> ActualInteger

**Description**: Shows the actual value (integer) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount or Count and the amount data type is Integer.<br />
**DisplayName**: Actual (Integer)<br />
**LogicalName**: actualinteger<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ActualMoney"></a> ActualMoney

**Description**: Shows the actual value (Money type) achieved towards the target as of the last rolled-up date. This field appears when the metric type of the goal is Amount and the amount data type is Money.<br />
**DisplayName**: Actual (Money)<br />
**LogicalName**: actualmoney<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_AmountDataType"></a> AmountDataType

**Description**: Data type of the amount.<br />
**DisplayName**: Amount Data Type<br />
**LogicalName**: amountdatatype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Money
- **Value**: 1 **Label**: Decimal
- **Value**: 2 **Label**: Integer



### <a name="BKMK_ConsiderOnlyGoalOwnersRecords"></a> ConsiderOnlyGoalOwnersRecords

**Description**: Select whether only the goal owner's records, or all records, should be rolled up for goal results.<br />
**DisplayName**: Record Set for Rollup<br />
**LogicalName**: consideronlygoalownersrecords<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Owned by goal owner
- **FalseOption Value**: 0 **Label**: All

**DefaultValue**: True


### <a name="BKMK_CustomRollupFieldDecimal"></a> CustomRollupFieldDecimal

**Description**: Indicates a placeholder rollup field for a decimal value to track a third category of results other than actuals and in-progress results.<br />
**DisplayName**: Custom Rollup Field (Decimal)<br />
**LogicalName**: customrollupfielddecimal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: -100000000000<br />
**Precision**: 10


### <a name="BKMK_CustomRollupFieldInteger"></a> CustomRollupFieldInteger

**Description**: Indicates a placeholder rollup field for an integer value to track a third category of results other than actuals and in-progress results.<br />
**DisplayName**: Custom Rollup Field (Integer)<br />
**LogicalName**: customrollupfieldinteger<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CustomRollupFieldMoney"></a> CustomRollupFieldMoney

**Description**: Indicates a placeholder rollup field for a money value to track a third category of results other than actuals and in-progress results.<br />
**DisplayName**: Custom Rollup Field (Money)<br />
**LogicalName**: customrollupfieldmoney<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_EntityImage"></a> EntityImage

**Description**: The default image for the entity.<br />
**DisplayName**: Entity Image<br />
**LogicalName**: entityimage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Image<br />
**IsPrimaryImage**: False<br />
**MaxHeight**: 144<br />
**MaxWidth**: 144


### <a name="BKMK_FiscalPeriod"></a> FiscalPeriod

**Description**: Select the fiscal period for the goal.<br />
**DisplayName**: Fiscal Period<br />
**LogicalName**: fiscalperiod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Quarter 1
- **Value**: 2 **Label**: Quarter 2
- **Value**: 3 **Label**: Quarter 3
- **Value**: 4 **Label**: Quarter 4
- **Value**: 101 **Label**: January
- **Value**: 102 **Label**: February
- **Value**: 103 **Label**: March
- **Value**: 104 **Label**: April
- **Value**: 105 **Label**: May
- **Value**: 106 **Label**: June
- **Value**: 107 **Label**: July
- **Value**: 108 **Label**: August
- **Value**: 109 **Label**: September
- **Value**: 110 **Label**: October
- **Value**: 111 **Label**: November
- **Value**: 112 **Label**: December
- **Value**: 201 **Label**: Semester 1
- **Value**: 202 **Label**: Semester 2
- **Value**: 301 **Label**: Annual
- **Value**: 401 **Label**: P1
- **Value**: 402 **Label**: P2
- **Value**: 403 **Label**: P3
- **Value**: 404 **Label**: P4
- **Value**: 405 **Label**: P5
- **Value**: 406 **Label**: P6
- **Value**: 407 **Label**: P7
- **Value**: 408 **Label**: P8
- **Value**: 409 **Label**: P9
- **Value**: 410 **Label**: P10
- **Value**: 411 **Label**: P11
- **Value**: 412 **Label**: P12
- **Value**: 413 **Label**: P13



### <a name="BKMK_FiscalYear"></a> FiscalYear

**Description**: Select the fiscal year for the goal that's being tracked.<br />
**DisplayName**: Fiscal Year<br />
**LogicalName**: fiscalyear<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1970 **Label**: FY1970
- **Value**: 1971 **Label**: FY1971
- **Value**: 1972 **Label**: FY1972
- **Value**: 1973 **Label**: FY1973
- **Value**: 1974 **Label**: FY1974
- **Value**: 1975 **Label**: FY1975
- **Value**: 1976 **Label**: FY1976
- **Value**: 1977 **Label**: FY1977
- **Value**: 1978 **Label**: FY1978
- **Value**: 1979 **Label**: FY1979
- **Value**: 1980 **Label**: FY1980
- **Value**: 1981 **Label**: FY1981
- **Value**: 1982 **Label**: FY1982
- **Value**: 1983 **Label**: FY1983
- **Value**: 1984 **Label**: FY1984
- **Value**: 1985 **Label**: FY1985
- **Value**: 1986 **Label**: FY1986
- **Value**: 1987 **Label**: FY1987
- **Value**: 1988 **Label**: FY1988
- **Value**: 1989 **Label**: FY1989
- **Value**: 1990 **Label**: FY1990
- **Value**: 1991 **Label**: FY1991
- **Value**: 1992 **Label**: FY1992
- **Value**: 1993 **Label**: FY1993
- **Value**: 1994 **Label**: FY1994
- **Value**: 1995 **Label**: FY1995
- **Value**: 1996 **Label**: FY1996
- **Value**: 1997 **Label**: FY1997
- **Value**: 1998 **Label**: FY1998
- **Value**: 1999 **Label**: FY1999
- **Value**: 2000 **Label**: FY2000
- **Value**: 2001 **Label**: FY2001
- **Value**: 2002 **Label**: FY2002
- **Value**: 2003 **Label**: FY2003
- **Value**: 2004 **Label**: FY2004
- **Value**: 2005 **Label**: FY2005
- **Value**: 2006 **Label**: FY2006
- **Value**: 2007 **Label**: FY2007
- **Value**: 2008 **Label**: FY2008
- **Value**: 2009 **Label**: FY2009
- **Value**: 2010 **Label**: FY2010
- **Value**: 2011 **Label**: FY2011
- **Value**: 2012 **Label**: FY2012
- **Value**: 2013 **Label**: FY2013
- **Value**: 2014 **Label**: FY2014
- **Value**: 2015 **Label**: FY2015
- **Value**: 2016 **Label**: FY2016
- **Value**: 2017 **Label**: FY2017
- **Value**: 2018 **Label**: FY2018
- **Value**: 2019 **Label**: FY2019
- **Value**: 2020 **Label**: FY2020
- **Value**: 2021 **Label**: FY2021
- **Value**: 2022 **Label**: FY2022
- **Value**: 2023 **Label**: FY2023
- **Value**: 2024 **Label**: FY2024
- **Value**: 2025 **Label**: FY2025
- **Value**: 2026 **Label**: FY2026
- **Value**: 2027 **Label**: FY2027
- **Value**: 2028 **Label**: FY2028
- **Value**: 2029 **Label**: FY2029
- **Value**: 2030 **Label**: FY2030
- **Value**: 2031 **Label**: FY2031
- **Value**: 2032 **Label**: FY2032
- **Value**: 2033 **Label**: FY2033
- **Value**: 2034 **Label**: FY2034
- **Value**: 2035 **Label**: FY2035
- **Value**: 2036 **Label**: FY2036
- **Value**: 2037 **Label**: FY2037
- **Value**: 2038 **Label**: FY2038



### <a name="BKMK_GoalEndDate"></a> GoalEndDate

**Description**: Enter the date when the goal ends.<br />
**DisplayName**: To<br />
**LogicalName**: goalenddate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_GoalId"></a> GoalId

**Description**: Unique identifier of the goal.<br />
**DisplayName**: Goal<br />
**LogicalName**: goalid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_GoalOwnerId"></a> GoalOwnerId

**Description**: Choose the user or team responsible for meeting the goal.<br />
**DisplayName**: Goal Owner<br />
**LogicalName**: goalownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: systemuser,team


### <a name="BKMK_GoalOwnerIdType"></a> GoalOwnerIdType

**Description**: <br />
**DisplayName**: Goal Owner Type<br />
**LogicalName**: goalowneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_GoalStartDate"></a> GoalStartDate

**Description**: Enter the date and time when the period for tracking the goal begins.<br />
**DisplayName**: From<br />
**LogicalName**: goalstartdate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_GoalWithErrorId"></a> GoalWithErrorId

**Description**: Unique identifier of the goal that caused an error in the rollup of the goal hierarchy.<br />
**DisplayName**: Goal With Error<br />
**LogicalName**: goalwitherrorid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Lookup<br />
**Targets**: goal


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Sequence number of the import that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_InProgressDecimal"></a> InProgressDecimal

**Description**: Shows the in-progress value (decimal) against the target. This value could contribute to a goal, but is not counted yet as actual.<br />
**DisplayName**: In-progress (Decimal)<br />
**LogicalName**: inprogressdecimal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: -100000000000<br />
**Precision**: 10


### <a name="BKMK_InProgressInteger"></a> InProgressInteger

**Description**: Shows the in-progress value (integer) against the target. This value could contribute to a goal, but is not counted yet as actual.<br />
**DisplayName**: In-progress (Integer)<br />
**LogicalName**: inprogressinteger<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_InProgressMoney"></a> InProgressMoney

**Description**: Shows the in-progress value (money) against the target. This value could contribute to a goal, but is not counted yet as actual.<br />
**DisplayName**: In-progress (Money)<br />
**LogicalName**: inprogressmoney<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_IsAmount"></a> IsAmount

**Description**: Indicates whether the metric type is Count or Amount.<br />
**DisplayName**: Metric Type<br />
**LogicalName**: isamount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Amount
- **FalseOption Value**: 0 **Label**: Count

**DefaultValue**: True


### <a name="BKMK_IsFiscalPeriodGoal"></a> IsFiscalPeriodGoal

**Description**: Select whether the goal period is a fiscal period or custom period.<br />
**DisplayName**: Goal Period Type<br />
**LogicalName**: isfiscalperiodgoal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Fiscal Period
- **FalseOption Value**: 0 **Label**: Custom Period

**DefaultValue**: True


### <a name="BKMK_IsOverridden"></a> IsOverridden

**Description**: Select whether the system rollup fields are updated. If set to Yes, the next system rollup will not update the values of the rollup fields with the system calculated values.<br />
**DisplayName**: Overridden<br />
**LogicalName**: isoverridden<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsOverride"></a> IsOverride

**Description**: Indicates whether the values of system rollup fields can be updated.<br />
**DisplayName**: Override<br />
**LogicalName**: isoverride<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_LastRolledupDate"></a> LastRolledupDate

**Description**: Shows the date and time when the goal was last rolled up. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Last Rolled Up Date<br />
**LogicalName**: lastrolledupdate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MetricId"></a> MetricId

**Description**: Choose the metric for the goal. This metric determines how the goal is tracked.<br />
**DisplayName**: Goal Metric<br />
**LogicalName**: metricid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: metric


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
**DisplayName**: Manager<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Owner Id Type<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_ParentGoalId"></a> ParentGoalId

**Description**: Choose a parent goal if the current goal is a child goal. This sets up a parent-child relationship for reporting and analytics.<br />
**DisplayName**: Parent Goal<br />
**LogicalName**: parentgoalid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goal


### <a name="BKMK_Percentage"></a> Percentage

**Description**: Shows the percentage achieved against the target goal.<br />
**DisplayName**: Percentage Achieved<br />
**LogicalName**: percentage<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: -100000000000<br />
**Precision**: 0


### <a name="BKMK_RollupErrorCode"></a> RollupErrorCode

**Description**: Error code associated with rollup.<br />
**DisplayName**: Rollup Error Code<br />
**LogicalName**: rolluperrorcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_RollupOnlyFromChildGoals"></a> RollupOnlyFromChildGoals

**Description**: Select whether the data should be rolled up only from the child goals.<br />
**DisplayName**: Roll Up Only from Child Goals<br />
**LogicalName**: rolluponlyfromchildgoals<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RollUpQueryActualDecimalId"></a> RollUpQueryActualDecimalId

**Description**: Choose the query that will be used to calculate the actual data for the goal (decimal).<br />
**DisplayName**: Rollup Query - Actual(Decimal)<br />
**LogicalName**: rollupqueryactualdecimalid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollupQueryActualIntegerId"></a> RollupQueryActualIntegerId

**Description**: Choose the query that will be used to calculate the actual data for the goal (integer).<br />
**DisplayName**: Rollup Query - Actual(Integer)<br />
**LogicalName**: rollupqueryactualintegerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollUpQueryActualMoneyId"></a> RollUpQueryActualMoneyId

**Description**: Choose the query that will be used to calculate the actual data for the goal (money).<br />
**DisplayName**: Rollup Query - Actual(Money)<br />
**LogicalName**: rollupqueryactualmoneyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollUpQueryCustomDecimalId"></a> RollUpQueryCustomDecimalId

**Description**: Choose the query that will be used to calculate data for the custom rollup field (decimal).<br />
**DisplayName**: Rollup Query - Custom Rollup Field (Decimal)<br />
**LogicalName**: rollupquerycustomdecimalid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollUpQueryCustomIntegerId"></a> RollUpQueryCustomIntegerId

**Description**: Choose the query that will be used to calculate data for the custom rollup field (integer).<br />
**DisplayName**: Rollup Query - Custom Rollup Field (Integer)<br />
**LogicalName**: rollupquerycustomintegerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollUpQueryCustomMoneyId"></a> RollUpQueryCustomMoneyId

**Description**: Choose the query that will be used to calculate data for the custom rollup field (money).<br />
**DisplayName**: Rollup Query - Custom Rollup Field (Money)<br />
**LogicalName**: rollupquerycustommoneyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollUpQueryInprogressDecimalId"></a> RollUpQueryInprogressDecimalId

**Description**: Choose the query that will be used to calculate data for the in-progress rollup field (decimal).<br />
**DisplayName**: Rollup Query - In-progress(Decimal)<br />
**LogicalName**: rollupqueryinprogressdecimalid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollUpQueryInprogressIntegerId"></a> RollUpQueryInprogressIntegerId

**Description**: Choose the query that will be used to calculate data for the in-progress rollup field (integer).<br />
**DisplayName**: Rollup Query - In-progress(Integer)<br />
**LogicalName**: rollupqueryinprogressintegerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_RollUpQueryInprogressMoneyId"></a> RollUpQueryInprogressMoneyId

**Description**: Choose the query that will be used to calculate data for the in-progress rollup field (money).<br />
**DisplayName**: Rollup Query - In-progress(Money)<br />
**LogicalName**: rollupqueryinprogressmoneyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: goalrollupquery


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the goal is open, completed, or canceled. Completed and canceled goals are read-only and can't be edited.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 0 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 1 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the goal's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Open **State**: 0
- **Value**: 1 **Label**: Closed **State**: 1
- **Value**: 2 **Label**: Discarded **State**: 1



### <a name="BKMK_StretchTargetDecimal"></a> StretchTargetDecimal

**Description**: Select a stretch target (decimal) of the goal to define a higher or difficult level of goal than the usual ones.<br />
**DisplayName**: Stretch Target (Decimal)<br />
**LogicalName**: stretchtargetdecimal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_StretchTargetInteger"></a> StretchTargetInteger

**Description**: Select the stretch target (integer) of the goal to define a higher or difficult level of goal than the usual ones.<br />
**DisplayName**: Stretch Target (Integer)<br />
**LogicalName**: stretchtargetinteger<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_StretchTargetMoney"></a> StretchTargetMoney

**Description**: Select stretch target (money) of the goal to define a higher or difficult level of goal than the usual ones.<br />
**DisplayName**: Stretch Target (Money)<br />
**LogicalName**: stretchtargetmoney<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: 0<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_TargetDecimal"></a> TargetDecimal

**Description**: Select a goal target of the decimal type to use for tracking data that include partial numbers, such as pounds sold of a product sold by weight.<br />
**DisplayName**: Target (Decimal)<br />
**LogicalName**: targetdecimal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_TargetInteger"></a> TargetInteger

**Description**: Select a goal target of the integer type to use for tracking anything countable in whole numbers, such as units sold.<br />
**DisplayName**: Target (Integer)<br />
**LogicalName**: targetinteger<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_TargetMoney"></a> TargetMoney

**Description**: Select a goal target (money) to track a monetary amount such as revenue from a product.<br />
**DisplayName**: Target (Money)<br />
**LogicalName**: targetmoney<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: 0<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_Title"></a> Title

**Description**: Type a title or name that describes the goal.<br />
**DisplayName**: Name<br />
**LogicalName**: title<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: UTC Conversion Time Zone Code<br />
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

**Description**: Shows the actual value (money type) in base currency to track goal results against the target.<br />
**DisplayName**: Actual (Money) (Base)<br />
**LogicalName**: actualmoney_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_ActualString"></a> ActualString

**Description**: Actual Value of the goal.<br />
**DisplayName**: Actual<br />
**LogicalName**: actualstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ComputedTargetAsOfTodayDecimal"></a> ComputedTargetAsOfTodayDecimal

**Description**: Shows the expected amount for actual value (decimal type) against the target goal.<br />
**DisplayName**: Today's Target (Decimal)<br />
**LogicalName**: computedtargetasoftodaydecimal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_ComputedTargetAsOfTodayInteger"></a> ComputedTargetAsOfTodayInteger

**Description**: Shows the expected amount for actual value (integer type) against the target goal as of the current date.<br />
**DisplayName**: Today's Target (Integer)<br />
**LogicalName**: computedtargetasoftodayinteger<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ComputedTargetAsOfTodayMoney"></a> ComputedTargetAsOfTodayMoney

**Description**: Shows the expected amount for actual value (money type) against the target goal as of the current date.<br />
**DisplayName**: Today's Target (Money)<br />
**LogicalName**: computedtargetasoftodaymoney<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: 0<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_ComputedTargetAsOfTodayMoney_Base"></a> ComputedTargetAsOfTodayMoney_Base

**Description**: Shows the expected amount in base currency for actual value (money type) against the target goal as of the current date.<br />
**DisplayName**: Today's Target (Money) (Base)<br />
**LogicalName**: computedtargetasoftodaymoney_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_ComputedTargetAsOfTodayPercentageAchieved"></a> ComputedTargetAsOfTodayPercentageAchieved

**Description**: Shows the expected value for percentage achieved against the target goal as of the current date.<br />
**DisplayName**: Today's Target (Percentage Achieved)<br />
**LogicalName**: computedtargetasoftodaypercentageachieved<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0<br />
**Precision**: 0


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_CustomRollupFieldMoney_Base"></a> CustomRollupFieldMoney_Base

**Description**: Indicates a placeholder rollup field for a money value in base currency to track a third category of results other than actuals and in-progress results.<br />
**DisplayName**: Custom Rollup Field (Money) (Base)<br />
**LogicalName**: customrollupfieldmoney_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_CustomRollupFieldString"></a> CustomRollupFieldString

**Description**: Placeholder rollup field for the goal.<br />
**DisplayName**: Custom Rollup Field<br />
**LogicalName**: customrollupfieldstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_Depth"></a> Depth

**Description**: Depth of the goal in the tree.<br />
**DisplayName**: Depth<br />
**LogicalName**: depth<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_timestamp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_url<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_EntityImageId"></a> EntityImageId

**Description**: For internal use only.<br />
**DisplayName**: Entity Image Id<br />
**LogicalName**: entityimageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_GoalOwnerIdName"></a> GoalOwnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: goalowneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_GoalOwnerIdYomiName"></a> GoalOwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: goalowneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_GoalWithErrorIdName"></a> GoalWithErrorIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: goalwitherroridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_InProgressMoney_Base"></a> InProgressMoney_Base

**Description**: Shows the in-progress value (money) in base currency to track goal results against the target.<br />
**DisplayName**: In-progress (Money) (Base)<br />
**LogicalName**: inprogressmoney_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_InProgressString"></a> InProgressString

**Description**: In-progress value of the goal.<br />
**DisplayName**: In-Progress<br />
**LogicalName**: inprogressstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_MetricIdName"></a> MetricIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: metricidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who last updated the record on behalf of another user.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the manager<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: Yomi name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier for the business unit that owns the record.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the goal.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier for the user who owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ParentGoalIdName"></a> ParentGoalIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentgoalidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryActualDecimalIdName"></a> RollUpQueryActualDecimalIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupqueryactualdecimalidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollupQueryActualIntegerIdName"></a> RollupQueryActualIntegerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupqueryactualintegeridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryActualMoneyIdName"></a> RollUpQueryActualMoneyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupqueryactualmoneyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryCustomDecimalIdName"></a> RollUpQueryCustomDecimalIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupquerycustomdecimalidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryCustomIntegerIdName"></a> RollUpQueryCustomIntegerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupquerycustomintegeridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryCustomMoneyIdName"></a> RollUpQueryCustomMoneyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupquerycustommoneyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryInprogressDecimalIdName"></a> RollUpQueryInprogressDecimalIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupqueryinprogressdecimalidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryInprogressIntegerIdName"></a> RollUpQueryInprogressIntegerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupqueryinprogressintegeridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RollUpQueryInprogressMoneyIdName"></a> RollUpQueryInprogressMoneyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rollupqueryinprogressmoneyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_StretchTargetMoney_Base"></a> StretchTargetMoney_Base

**Description**: Shows the stretch target (money) in base currency to indicate a higher or difficult level of goal than the usual ones.<br />
**DisplayName**: Stretch Target (Money) (Base)<br />
**LogicalName**: stretchtargetmoney_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_StretchTargetString"></a> StretchTargetString

**Description**: Stretch target value for all data types.<br />
**DisplayName**: Stretched Target<br />
**LogicalName**: stretchtargetstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_TargetMoney_Base"></a> TargetMoney_Base

**Description**: Shows the goal target of the money type in base currency.<br />
**DisplayName**: Target (Money) (Base)<br />
**LogicalName**: targetmoney_base<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Money<br />
**MaxValue**: 922337203685477<br />
**MinValue**: -922337203685477<br />
**Precision**: 4<br />
**PrecisionSource**: 2


### <a name="BKMK_TargetString"></a> TargetString

**Description**: Target value of the goal.<br />
**DisplayName**: Target<br />
**LogicalName**: targetstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Choose the local currency for the record to make sure budgets are reported in the correct currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


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


### <a name="BKMK_TreeId"></a> TreeId

**Description**: Unique identifier of the goal tree.<br />
**DisplayName**: Tree ID<br />
**LogicalName**: treeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the goal.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

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
- [userentityinstancedata_goal](#BKMK_userentityinstancedata_goal)
- [goal_connections1](#BKMK_goal_connections1)
- [goal_connections2](#BKMK_goal_connections2)
- [Goal_DuplicateMatchingRecord](#BKMK_Goal_DuplicateMatchingRecord)
- [goal_principalobjectattributeaccess](#BKMK_goal_principalobjectattributeaccess)


### <a name="BKMK_goal_parent_goal"></a> goal_parent_goal

Same as goal entity [goal_parent_goal](goal.md#BKMK_goal_parent_goal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: parentgoalid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: goal_parent_goal<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 140

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Goal_DuplicateBaseRecord"></a> Goal_DuplicateBaseRecord

Same as duplicaterecord entity [Goal_DuplicateBaseRecord](duplicaterecord.md#BKMK_Goal_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Goal_DuplicateBaseRecord<br />
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


### <a name="BKMK_Goal_RollupError_Goal"></a> Goal_RollupError_Goal

Same as goal entity [Goal_RollupError_Goal](goal.md#BKMK_Goal_RollupError_Goal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: goalwitherrorid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Goal_RollupError_Goal<br />
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


### <a name="BKMK_Goal_SyncErrors"></a> Goal_SyncErrors

Same as syncerror entity [Goal_SyncErrors](syncerror.md#BKMK_Goal_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Goal_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_Goal_Annotation"></a> Goal_Annotation

Same as annotation entity [Goal_Annotation](annotation.md#BKMK_Goal_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Goal_Annotation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_Goal_AsyncOperations"></a> Goal_AsyncOperations

Same as asyncoperation entity [Goal_AsyncOperations](asyncoperation.md#BKMK_Goal_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Goal_AsyncOperations<br />
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


### <a name="BKMK_Goal_ProcessSessions"></a> Goal_ProcessSessions

Same as processsession entity [Goal_ProcessSessions](processsession.md#BKMK_Goal_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Goal_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_userentityinstancedata_goal"></a> userentityinstancedata_goal

Same as userentityinstancedata entity [userentityinstancedata_goal](userentityinstancedata.md#BKMK_userentityinstancedata_goal) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_goal<br />
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


### <a name="BKMK_goal_connections1"></a> goal_connections1

Same as connection entity [goal_connections1](connection.md#BKMK_goal_connections1) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record1id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: goal_connections1<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_connections2"></a> goal_connections2

Same as connection entity [goal_connections2](connection.md#BKMK_goal_connections2) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record2id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: goal_connections2<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Goal_DuplicateMatchingRecord"></a> Goal_DuplicateMatchingRecord

Same as duplicaterecord entity [Goal_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Goal_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Goal_DuplicateMatchingRecord<br />
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


### <a name="BKMK_goal_principalobjectattributeaccess"></a> goal_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [goal_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_goal_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_principalobjectattributeaccess<br />
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

See team Entity [team_goal](team.md#BKMK_team_goal) One-To-Many relationship.

### <a name="BKMK_goalrollupquery_actualint"></a> goalrollupquery_actualint

See goalrollupquery Entity [goalrollupquery_actualint](goalrollupquery.md#BKMK_goalrollupquery_actualint) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_actualmoney"></a> goal_rollupquery_actualmoney

See goalrollupquery Entity [goal_rollupquery_actualmoney](goalrollupquery.md#BKMK_goal_rollupquery_actualmoney) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_actualdecimal"></a> goal_rollupquery_actualdecimal

See goalrollupquery Entity [goal_rollupquery_actualdecimal](goalrollupquery.md#BKMK_goal_rollupquery_actualdecimal) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_customint"></a> goal_rollupquery_customint

See goalrollupquery Entity [goal_rollupquery_customint](goalrollupquery.md#BKMK_goal_rollupquery_customint) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_custommoney"></a> goal_rollupquery_custommoney

See goalrollupquery Entity [goal_rollupquery_custommoney](goalrollupquery.md#BKMK_goal_rollupquery_custommoney) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_customdecimal"></a> goal_rollupquery_customdecimal

See goalrollupquery Entity [goal_rollupquery_customdecimal](goalrollupquery.md#BKMK_goal_rollupquery_customdecimal) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_inprogressint"></a> goal_rollupquery_inprogressint

See goalrollupquery Entity [goal_rollupquery_inprogressint](goalrollupquery.md#BKMK_goal_rollupquery_inprogressint) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_inprogressmoney"></a> goal_rollupquery_inprogressmoney

See goalrollupquery Entity [goal_rollupquery_inprogressmoney](goalrollupquery.md#BKMK_goal_rollupquery_inprogressmoney) One-To-Many relationship.

### <a name="BKMK_goal_rollupquery_inprogressdecimal"></a> goal_rollupquery_inprogressdecimal

See goalrollupquery Entity [goal_rollupquery_inprogressdecimal](goalrollupquery.md#BKMK_goal_rollupquery_inprogressdecimal) One-To-Many relationship.

### <a name="BKMK_lk_goal_createdby"></a> lk_goal_createdby

See systemuser Entity [lk_goal_createdby](systemuser.md#BKMK_lk_goal_createdby) One-To-Many relationship.

### <a name="BKMK_lk_goal_createdonbehalfby"></a> lk_goal_createdonbehalfby

See systemuser Entity [lk_goal_createdonbehalfby](systemuser.md#BKMK_lk_goal_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_goal_modifiedby"></a> lk_goal_modifiedby

See systemuser Entity [lk_goal_modifiedby](systemuser.md#BKMK_lk_goal_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_goal_modifiedonbehalfby"></a> lk_goal_modifiedonbehalfby

See systemuser Entity [lk_goal_modifiedonbehalfby](systemuser.md#BKMK_lk_goal_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_goal"></a> user_goal

See systemuser Entity [user_goal](systemuser.md#BKMK_user_goal) One-To-Many relationship.

### <a name="BKMK_business_unit_goal"></a> business_unit_goal

See businessunit Entity [business_unit_goal](businessunit.md#BKMK_business_unit_goal) One-To-Many relationship.

### <a name="BKMK_user_goal_goalowner"></a> user_goal_goalowner

See systemuser Entity [user_goal_goalowner](systemuser.md#BKMK_user_goal_goalowner) One-To-Many relationship.

### <a name="BKMK_goal_parent_goal"></a> goal_parent_goal

See goal Entity [goal_parent_goal](goal.md#BKMK_goal_parent_goal) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Goal"></a> TransactionCurrency_Goal

See transactioncurrency Entity [TransactionCurrency_Goal](transactioncurrency.md#BKMK_TransactionCurrency_Goal) One-To-Many relationship.

### <a name="BKMK_metric_goal"></a> metric_goal

See metric Entity [metric_goal](metric.md#BKMK_metric_goal) One-To-Many relationship.

### <a name="BKMK_Goal_RollupError_Goal"></a> Goal_RollupError_Goal

See goal Entity [Goal_RollupError_Goal](goal.md#BKMK_Goal_RollupError_Goal) One-To-Many relationship.

### <a name="BKMK_team_goal_goalowner"></a> team_goal_goalowner

See team Entity [team_goal_goalowner](team.md#BKMK_team_goal_goalowner) One-To-Many relationship.
goal

