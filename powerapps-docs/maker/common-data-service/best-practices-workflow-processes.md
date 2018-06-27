---
title: "Best practices for workflow processes in PowerApps | MicrosoftDocs"
description: "Understand the recommended ways to use workflows"
ms.custom: ""
ms.date: 06/27/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 34e34c33-003a-494f-858c-3d34aacb308c
caps.latest.revision: 10
ms.author: "matp"
manager: "kvivek"
---
# Best practices for workflow processes

This topic contains best practices for creating and managing workflow processes.  
  
<a name="BKMK_AvoidInfiniteLoops"></a>   
## Avoid infinite loops  
 It’s possible to create logic in a workflow that initiates an infinite loop, which consumes server resources and affects performance. The typical situation where an infinite loop might occur is if you have a workflow configured to start when an attribute is updated and then updates that attribute in the logic of the workflow. The update action triggers the same workflow that updates the record and triggers the workflow again and again.  
  
 The workflows you create include logic to detect and stop infinite loops. If a workflow process is run more than a certain number of times on a specific record in a short period of time, the process fails with the following error: **This workflow job was canceled because the workflow that started it included an infinite loop. Correct the workflow logic and try again**. The limit of times is 16.  
  
<a name="BKMK_UseWorkflowTemplates"></a>   
## Use workflow templates  
 If you have workflows that are similar and you anticipate creating more workflows that follow the same pattern, save your workflow as a workflow template. This way, the next time you need to create a similar workflow, create the workflow using the template and avoid entering all the conditions and actions from scratch.  
  
 In the **Create Process** dialog, choose **New process from an existing template (select from list)**.  
  
<a name="BKMK_UseChildWorkflows"></a>   
## Use child workflows  
 If you apply the same logic in different workflows or in conditional branches, define that logic as a child workflow so you don’t have to replicate that logic manually in each workflow or conditional branch. This helps make your workflows easier to maintain. Instead of examining many workflows that may apply the same logic, you can just update one workflow.  
  
<a name="BKMK_AutoDeleteCompletedWorkflowJobs"></a>   
## Keep fewer logs  
 To save disk space, clear the **Keep logs for workflow jobs that encounter errors** check box if you don’t need to keep this data.  
  
<a name="BKMK_DocumentChangesUsingNotes"></a>   
## Use Notes to keep track of changes  
 When you edit workflows you should use the Notes tab and type what you did and why you did it. This allows someone else to understand the changes you made.  
  
## Next steps  
 [Workflow processes overview](workflow-processes.md)   
 [Configure workflow processes](configure-workflow-steps.md)   
 [Monitor and manage workflow processes](monitor-manage-processes.md)
   
