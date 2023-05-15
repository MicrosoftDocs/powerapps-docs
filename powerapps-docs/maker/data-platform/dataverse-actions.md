---
title: Use Dataverse actions
description: Microsoft Dataverse actions  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 05/15/2023
ms.custom: template-how-to
---
# Use low-code plugins (experimental)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Optimize your data architecture and reduce client-side load using Microsoft Dataverse low-code plugins. Makers use the action authoring experience to define their logic using the Power Fx language. Dataverse actions are an alternative to custom APIs and custom process actions. Although, custom process actions provide a no-code way to include custom messages, they have limitations for developers and custom APIs provide business logic capabilities used for developers.

Actions are reusable, server-side synchronous (real-time) business logic workflows that allow you to execute a set of specific commands in Dataverse, called from web services, such as the Dataverse connector or the web API.

Actions are defined using the Power Fx expression language. You define input and output parameters, which allow you to dynamically pass information between the formula and calling context. Actions can also perform operations on Dataverse tables, such as create and update with Patch or Delete.

This is an experimental feature. More information: 

## Rules

A rule is business logic that is invoked based on the data event for a particular table, expressed in Power Fx formulas. Any logic that can be defined in an action can also be defined in a rule. Another way to think of a rule is that it's an action that has an ‘automated’ trigger. You can interact with the record that invoked the rule by referencing `ThisRecord` in the formula to get specific values.

## Decide whether to use Power Automate or Dataverse actions

Imagine you have a custom table named *jobapplication* that's used for job applications in your organization.

### When to use Power Automate
<!-- Need clarification on what Jobapplication is. Is it a Dataverse table? Also, need a high level explanation before these examples.-->
When you want to create Jobapplication statistic record every night, which is a recurring task that runs every night. For this situation, create a flow in Power Automate.

:::image type="content" source="media/jobapplication-flow.png" alt-text="Job application flow":::

When you want to create a Jobapplication record only when the student name is not available in the system. For this situation, use a Dataverse action.

## Prerequisites

Download and install the Creator Kit. <!-- Need link to appsource -->

## Create an action

1. Sign into the environment where the Creator Kit solution is installed and play the Dataverse Accelerator app.
1. On the app left navigation pane select **Dataverse actions**, and then on the command bar select **New action**.
1. On the **New action** page, enter the following information, and then select **Next**:

   - **Display name**. Enter a name for the action, such as *Calculate sum*.
   - **Description**. Enter a description for the action.
   - **Advanced options** > **Allowed custom processing step type**:
     - **None**. Select this option when the action provides a capability that shouldn't be detected or customizable.​ This is the default option.
     - **Async**. This option allows other makers to detect when the action occurs, but doesn't allow the ability to cancel the action or customize the behavior.
     - **Sync and async**. This option allows other makers to have the ability to change the behavior of the action and even cancel it if their business logic allows for it.​
1. Enter your input and output parameters:
   - Select **New input parameter**. Available data types are **Boolean**, **String**, or **Integer**. Enter an input parameter, such as **Label:** *X* and **Data type**: *Integer*.
   - Select **New output parameter**. Available data types are **Boolean**, **String**, or **Integer**. Enter an output parameter, such as **Label**: *Sum* and **Data type**: *Integer*.
1. Add more input and output parameters as necessary. For example, Enter another input parameter, such as **Label**: *Y* and **Data type**: *Integer*.
1. Enter the Power Fx formula in the **Formula** box. For example, `{Out:  X + Y }`, to calculate the sum of two integers.
   :::image type="content" source="media/action-sum-example.png" alt-text="Action using Power Fx to derive a sum value with two integers":::
1. Select **Next**.
1. Verify the settings for the action on the summary page, and then select **Save**.
1. Select **Test** to verify the action. If there are parameters that must be specified enter the values you want. Then select **Run** to test the action.

## Create a Dataverse rule

1. Sign into the environment where the **Creator Kit** solution is installed and run the **Dataverse Accelerator** app.
1. On the app left navigation pane select **Dataverse rules**, and then on the command bar select **New rule**.
1. On the **New rule** page, enter the following information:
   - Name: Enter a name for the rule.
   - Table. Select a table for the rule, such as *Contact*.
   - **Run this rule when the row is**. Specify the trigger, such as *Update*.
      - Create. Triggers the rule during a row create operation.
      - Update. Triggers the rule during a row change operation.
      - Delete. . Triggers the rule during a row delete operation.
1. Formula. Enter a Power Fx formula in the **Formula** box. For example, `If( IsBlank( ThisRecord.Email ), Set(Contacts, ThisRecord, { ‘Email description’:  “No email” } ));`.
1. **Advanced options** > **When should this run**.
   - **Pre-operation**. Select this option if you want the logic to run after form validation and before the values are saved to Dataverse.
   - **Post operation**. Enables your plugin to run after the values have been inserted or changed in Dataverse.
1. Select **Save**.