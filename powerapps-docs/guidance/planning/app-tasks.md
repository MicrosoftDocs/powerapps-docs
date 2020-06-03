---
title: Identifying the tasks to be done in the app | Microsoft Docs
description: Identifying the tasks to be done in the app
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/02/2020
ms.author: thground
ms.reviewer: kathyos
searchScope:  
  - PowerApps
---

# Identifying the tasks to be done in the app

To identify the tasks that are required in the app, you should refer to the
business process flow chart that you created in the planning phase and add
detail. Organize the information and list the tasks that are to be accomplished
on each screen.

When you write the tasks, remember to consider tasks for each persona that will
be using the screen/app. Try to separate them into sections.

Along with the tasks that users need to do, refer to your notes on what
information is required to complete each task. That will help you define what
information you need to store and display.

If you are working with multiple people, using tools like Microsoft Planner or
Whiteboard app would help you efficiently collaborate and work together on
listing the tasks.

## Example: Tasks for creating and viewing expense reports


We considered the tasks done by people who will be creating and viewing the
expense reports. We’ll separately consider the tasks for approvals and for
weekly budget reporting.

![Business process flowchart with tasks for the Expense Report creating and view app](media/app-tasks.png)

Based on the above, we think the Expense Report create/view app needs these
screens/components:

-   List of reports with filtering

-   Single report view with edit and view-only modes

-   Buttons to cancel/save/submit in editing view 

-   Button for Accounting to export data 

-   Various submit/cancel/save messages

-   Attach a receipt photo/ view attachments
