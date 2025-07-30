---
title: "Microsoft Dataverse real-time workflows"
description: "Learn about Microsoft Dataverse real-time workflows"
ms.date: 07/11/2024
ms.reviewer: "matp"
ms.topic: overview
ms.assetid: 1f3c9780-26ad-49ec-a3fb-fc226def19c5
author: msftman
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - flowmaker
  - enduser
---
# Microsoft Dataverse real-time workflows

Workflows automate business processes without a user interface. People usually use workflow processes to initiate automation that doesn’t require any user interaction.

There are two types of workflows:

- Background workflows. Background workflows run when the system has resource availability (asynchronously). Go to the [Power Automate](/power-automate/workflow-processes) documentation for more details about background workflows.
- Real-time workflows. Real-time workflows run immediately (synchronously).

## Create or edit real-time workflows

> [!IMPORTANT]
> There are better ways to create modern automations. Consider using Power Automate flows to automate your processes. More information: [Power Automate](/power-automate/)

1. Create a solution or open an existing one.
1. Select **New** > **Automation** > **Process** > **Workflow**.
1. Enter a **Display name**, select a **Table**, and then clear the **Run workflow in the background** option.
1. Select **Create**.

The workflow designer is displayed. Select the workflow attributes and steps needed. More information: [Configure real-time workflow stages and steps](configure-workflow-steps.md)

### View and edit real-time workflows

1. Sign in to [Power Apps](https://make.powerapps.com), select the **Settings** icon on the upper right, and then select **Advanced settings**.
1. Select the down arrow next to **Settings** on the top bar, and then select **Processes**.
1. In the list of processes, select the workflow that you want to edit.

## Learn more

- [Monitor and manage real-time workflow processes](monitor-manage-processes.md)
- [Best practices for real-time workflow processes](best-practices-workflow-processes.md)
- [Use actions](actions.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
