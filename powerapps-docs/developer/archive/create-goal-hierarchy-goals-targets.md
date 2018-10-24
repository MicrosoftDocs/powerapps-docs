---
title: "Create goal hierarchy, goals, and targets (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This article discusses how to create a goal hierarchy, set and monitor the targets, specify the time period and who manages and owns a goal" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
<!--

# Create goal hierarchy, goals, and targets

In preparation for goal management, you should specify a metric for a goal (amount or count), create a goal hierarchy, and set the targets. All goals in the hierarchy must be based on the same goal metric. A metric defines the type of the goal, and the rollup fields specify other important settings for the goal. For more information, see [Use Goal Metric and Rollup Fields to Define a Goal](define-goal-metric-rollup-fields.md).  

<a name="BKMK_CreateHierarchy"></a>   

## Create Goal Hierarchy  

 Typically, the manager’s goal is an aggregate of the goals assigned to the team members. A manager decides on the overall goal for the organization and then divides the goal into individual goals for each person. In a large organization, a goal for the company could be a combination of regional goals. In a simple goal hierarchy that is shown here, the manager’s goal is composed of two salesperson goals.  
  
 ![Goals hierarchy](media/crm-v5s-em-goalshierarchy.png "Goals hierarchy")  
  
 The manager’s goal can be referred to as a parent goal, and the salesperson goals as child goals. A goal can have multiple child goals (one-to-many relationship) and be a child goal of another goal. The relationship between a parent goal record and a child goal record can also be described as a referential relationship, in which a child goal references the parent goal. If you delete a parent goal, the child goal is not deleted, only a reference to the parent goal is removed. For more information, see [Entity Relationship Behavior](/dynamics365/customer-engagement/developer/entity-relationship-behavior).  
  
 The goal rollup is done from the bottom of the hierarchy to the top of the hierarchy. During rollup, the child goal totals are rolled into the parent goal totals. The ending total for the root goal at the top of hierarchy is a cumulative sum of all goal totals in the hierarchy.  
  
<a name="BKMK_WhoManages"></a>   

## Who Manages and Owns a Goal  

 A goal manager sets or modifies goal targets, adjusts the goal time period, and assigns a goal owner. A goal manager is the goal record owner (`Goal.OwnerID`) with full access rights to the goal. A goal owner (`Goal.GoalOwnerId`) is someone who has to meet the goal targets. A goal owner has Read and AppendTo access to the goal.  
  
 When a goal is created in Common Data Service for Apps, it is automatically shared with a goal owner and a parent goal’s manager. A parent goal’s manager is the record owner (`Goal.OwnerId`) of the parent goal, and has Read access to the newly created goal. When a parent goal’s manager or a goal owner is replaced, their access to the goal is revoked and the access is granted to the new parent goal’s manager or goal owner. If a goal was explicitly shared with a previous parent goal’s manager and goal owner, who were given specific access rights, these CDS for Apps users may not lose all access to the goal.  
  
<a name="BKMK_SetTargets"></a>   

## Set and Monitor the Targets  
 For each goal you can specify a target value against which the results of the goal rollup are measured. In addition, you can specify a stretch target. For example, your target revenue could be $100,000, and the stretch target revenue is $120,000.  
  
 Logically, the target values should increase towards the top of the goal hierarchy to reflect an upward increase of cumulative totals in the hierarchy.  
  
 Depending on the type of the rollup data, you can use one of the following goal entity attributes to set the targets: `Goal.TargetInteger`,  `Goal.TargetDecimal` or `Goal.TargetMoney`. To set the stretch targets, use:   `Goal.StretchTargetInteger`, `Goal.StretchTargetDecimal`, or `Goal.StretchTargetMoney`.  
  
 The following table lists the system-generated values that you can use to measure your progress against the target.  
  
|Goal entity attribute|Description|Formula|  
|---------------------------|-----------------|-------------|  
|`Goal.Percentage`|Percentage achieved against the target goal.|(Actual/Target) * 100|  
|`Goal.ComputedTargetAsOfTodayPercentageAchieved`|Expected value for percentage achieved against the target goal.|100 * (Today’s date – Start date)/(End date – Start date)|  
|`Goal.ComputedTargetAsOfTodayInteger`|Expected amount for Actual (integer) against the target goal.|Target (integer) * (Today’s date – Start date)/(End date – Start date)|  
|`Goal.ComputedTargetAsOfTodayDecimal`|Expected amount for Actual (decimal) against the target goal.|Target (decimal) * (Today’s date – Start date)/(End date – Start date)|  
|`Goal.ComputedTargetAsOfTodayMoney`|Expected amount for Actual (money) against the target goal.|Target (money) * (Today’s date – Start date)/(End date – Start date)|  
  
> [!NOTE]
>  The system-generated values are calculated against the target value. They are not calculated against the stretch target value.  
  
<a name="BKMK_specifytime"></a>   

## Specify the Time Period  
 For each goal you must specify a particular fiscal period or a custom time period. To select the fiscal period or custom period, use the `Goal.IsFiscalPeriodGoal` attribute. If you select a fiscal period, you must specify a fiscal year by using the `Goal.FiscalYear` attribute. The possible values for this attribute are defined in the  `goal_fiscalyear` global option set. A fiscal period, such as quarter or semi-annual, is specified in the `Goal.FiscalPeriod` attribute. The possible values for this attribute are defined in the `goal_fiscalperiod` global option set.  
  
 The goal’s fiscal year and fiscal period are tied to the organization’s fiscal year settings that are defined in the `Organization` entity. The fiscal year settings for the organization can be redefined at any time. If the settings change, you can continue to use the existing goals with the old fiscal settings or you can realign them with the new fiscal settings.  
  
> [!IMPORTANT]
>  To realign, you must update the hierarchy’s root goal with the new fiscal year and fiscal period values by using the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message.  
  
 The fiscal year and fiscal period values are defined in the `goal_fiscalperiod` global option set. All new goals can only be created by using the current fiscal year settings for the organization.  
  
 If you select a custom period for the goal, you have to specify the goal start and end dates by using the `Goal.GoalStartDate` attribute and the `Goal.GoalEndDate` attribute.  
  
 If you use a custom period, the `Goal.FiscalYear` and `Goal.FiscalPeriod` values are ignored. If you use a fiscal period, the start and end dates for the custom period are ignored.  
  
 All goals in the goal hierarchy must be based on the same fiscal period or custom period. If you specify a different time period for a child goal, a time period for a parent goal will be used.  
  
<a name="BKMK_other"></a>   

## Other Important Settings  
 Other important goal settings include the following:  
  
-   Specify a parent goal for the goal by using the `Goal.ParentGoalId` attribute. If you delete a parent goal, the child goal is not deleted, but a parent goal GUID value is replaced with a null value by the system.  
  
-   Specify to roll up data only from the child goals by setting `Goal.RollupOnlyFromChildGoals` to `true`. If set to `false`, data is rolled up from the child goals, and from the goal’s participating records specified in the goal’s metric and rollup query. For more information about the goal metric and the rollup query, see [Define Goal Metric and Perform Data Roll Up](define-goal-metric-rollup-fields.md) and [Add Complex Goal Criteria](add-complex-goal-criteria.md).  
  
-   Specify whether you want to roll up data from all available records or only from goal owner’s records by using the `Goal.ConsiderOnlyGoalOwnersRecords` attribute. For example, you can specify to roll up data only from the closed opportunities owned by the goal’s owner, instead of rolling up data from all closed opportunities.  
  
### See also  
 [Goal Management Entities](goal-management-entities.md)   
 [Define Goal Metric and Rollup Fields](define-goal-metric-rollup-fields.md)

 -->