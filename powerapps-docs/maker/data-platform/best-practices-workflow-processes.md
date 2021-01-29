---
title: "Best practices for managing real-time workflow processes | MicrosoftDocs"
description: "Understand the recommended ways to use workflows"
ms.custom: ""
ms.date: 06/27/2018
ms.reviewer: ""
ms.service: flow
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "Power Apps"
author: "Mattp123"
ms.assetid: 34e34c33-003a-494f-858c-3d34aacb308c
caps.latest.revision: 10
ms.author: "matp"
manager: "kvivek"
search.app: 
  - Flow
search.audienceType: 
  - flowmaker
  - enduser
---
# Best practices for real-time workflow processes


[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

This topic contains best practices for creating and managing workflow processes.  


<!-- from editor: If this was recently updated, please update the publication date. -->


<a name="BKMK_AvoidInfiniteLoops"></a>   
## Avoid infinite loops  
It’s possible to create logic in a workflow that initiates an infinite loop, which consumes server resources and affects performance. The typical situation where an infinite loop might occur is when you have a workflow configured to start when a column is updated for a row, and then updates said column in the logic of the workflow. This action triggers a new instance of the same workflow, which results in an infite recursion of workflow triggers.  
  
The workflows you create include logic to detect and stop infinite loops. If a workflow process is run more than a certain number of times on a specific row in a short period of time, the process fails with the following error: **This workflow job was canceled because the workflow that started it included an infinite loop. Correct the workflow logic and try again**. The limit of times is 16.  
  
<a name="BKMK_UseWorkflowTemplates"></a>   
## Use workflow templates  
If you have workflows that are similar and you anticipate creating more workflows that follow the same pattern, save your workflow as a workflow template. This way, the next time you need to create a similar workflow, you can create the workflow using the template and avoid entering all the conditions and actions from scratch.  
  
In the **Create Process** dialog, choose **New process from an existing template (select from list)**.  
  
<a name="BKMK_UseChildWorkflows"></a>   
## Use child workflows  
If you apply the same logic in different workflows or in conditional branches, define that logic as a child workflow so you don’t have to replicate that logic manually in each workflow or conditional branch. This helps make your workflows easier to maintain. Instead of examining many workflows that might apply the same logic, you can just update one workflow.  
  
## Automatically delete completed background workflow jobs
For background (asynchronous) workflows, we recommend selecting the **Automatically delete completed workflow jobs (to save disk space)** option in the workflow definition. Selecting this option allows the system to delete background workflow logs for successful executions to save space. Note that failed background workflow executions will always be saved for troubleshooting.  

![Workflow job retention](media/workflow-job-retention.png)

<a name="BKMK_AutoDeleteCompletedWorkflowJobs"></a>   
## Keep logs for real-time workflow jobs that encountered errors  
For workflows that don't run in the background (synchronous), we recommend selecting the **Keep logs for workflow jobs that encountered errors** option in the real-time workflow definition. Selecting this option allows logs from failed real-time workflow executions to be saved for troubleshooting. Logs from successful synchronous workflow executions will always be deleted to save space.   

![Keep logs for failed workflows option](media/keep-logs-for-workflows.png)

## Limit the number of workflows that update the same table
Running more than one real-time workflow that updates the same table can cause resource lock issues. Imagine several workflows running where every opportunity update triggers an update to the associated account. Multiple instances of these workflows running and attempting to update the same account row at the same time can result in resource locking issues. Real-time workflow failures occur and an error message, such as **SQL Timeout: Cannot obtain lock on resource _resource name_**, is rowed. 

  
<a name="BKMK_DocumentChangesUsingNotes"></a>   
## Use Notes to keep track of changes  
When you edit workflows you should use the Notes tab and type what you did and why. This allows someone else to understand the changes you made.  
<!-- from editor: Considering adding "see also" links to actions and power automate cloud flows. -->
