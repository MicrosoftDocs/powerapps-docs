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

## Create a Dataverse action

