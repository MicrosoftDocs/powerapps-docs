---
title: Use Dataverse actions
description: Microsoft Dataverse actions  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/20/2023
ms.custom: template-how-to
---
# Use Dataverse actions (preview)

Optimize your data architecture by reducing client-side load by calling Microsoft Dataverse actions directly with Power Fx based functions. The authoring experience for actions is targeted for makers to define their logic using the Power Fx language. Dataverse actions are an alternative to custom APIs and custom process actions. Custom process actions provide a no-code way to include custom messages but have limitations for developers. Custom APIs provide capabilities specifically for developers to define their logic in code with more options.

## Decide whether to use Power Automate or Dataverse actions

Imagine you have a custom table named *jobapplication* that's used for job applications in your organization.

### When to use Power Automate
<!-- Need clarification on what Jobapplication is. Is it a Dataverse table? Also, need a high level explanation before these examples.-->
When you want to create Jobapplication statistic record every night, which is a recurring task that runs every night. For this situation, create a flow in Power Automate.

:::image type="content" source="media/jobapplication-flow.png" alt-text="Job application flow":::

When you want to create a Jobapplication record only when the student name is not available in the system. For this situation, use a Dataverse action.

## Prerequisites

Download and install the Creator Kit. <!-- Need link to appsource -->

## Create a Dataverse action

1. Sign into the environment where the Creator Kit solution is installed and run the Dataverse Accelerator app.
1. On the app left navigation pane select **Dataverse actions**, and then on the command bar select **New action**.
1. On the **New action** page, enter the following information, and then select **Next**:

   - **Display name**. Enter a name for the action.
   - **Description**. Enter a description for the action.
   - **Advanced options** > **Allowed custom processing step type**:
     - **None**. <!-- Need descriptions for these.-->
     - **Async**.
1. Enter your input and output parameters. 
   - Select **New input parameter**. Set input parameters, which are used before making an API call. These parameters pass required information to the API to enable it to perform a function​. Available data types are **Boolean**, **String**, or **Integer**.
   - Select **New output parameter**. When a return to the application is successful, the application accesses the information returned in output parameters.​ Available data types are **Boolean**, **String**, or **Integer**.
1. Add more input and output parameters as necessary.
1. Optionally, enter a Power Fx formula in the **Formula** box. For example, `Collect(Accounts,{'Account Name':"test"})`.
<!-- Would be good to have a screenshot with valid plausible values -->
1. Select Next.
1. Verify the settings for the action on the summary page, and then select **Save**.

## Create a Dataverse rule

1. Sign into the environment where the Creator Kit solution is installed and run the Dataverse Accelerator app.
1. On the app left navigation pane select **Dataverse rules**, and then on the command bar select **New rule**.
1. On the **New rule** page, enter the following information:
   - Name: Enter a name for the rule.
   - Table. Select a table for the rule.
   - Run this rule when the row is: 
      - Create. Triggers the rule during a row create operation.
      - Update. Triggers the rule during a row change operation.
      - Delete. . Triggers the rule during a row delete operation.
1. Formula. Optionally, enter a Power Fx formula in the **Formula** box. For example, `Collect(account_primary_contact,{name:"test from contact",primarycontactid:ThisRecord})`.
1. Advanced options > When should this run.
   - Pre-operation.
   - Post operation. 
1. Select **Save**.