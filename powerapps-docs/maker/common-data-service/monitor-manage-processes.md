---
title: "Monitor and manage workflow processes with PowerApps | MicrosoftDocs"
ms.custom: ""
ms.date: 05/06/2018
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
ms.assetid: a987a803-4674-4eb0-87de-caefa003b1eb
caps.latest.revision: 12
ms.author: "matp"
manager: "kvivek"
---
# Monitor and manage workflow processes

To monitor and manage processes, you must locate the process, evaluate the status, and perform any actions necessary to address problems.  
  
<a name="BKMK_MonitorAsyncWorkflows"></a>   
## Monitoring background workflows  
 Background workflows generate System Job records to track their status. You can access information about these system jobs in several places within the application:  
  
 **[Settings](../model-driven-apps/advanced-navigation.md#settings) > System Jobs**  
 This will include all types of system jobs. You will need to filter records to those where **System Job Type** is **Workflow**.  
  
 **From the Workflow Process**  
 Open the background workflow definition and go to the **Process Session** tab. This will show only the system jobs for this background workflow.  
  
 **From the record**  
 You can edit the entity form so that the navigation will include the **Background Processes** relationship. This will show all the system jobs that have been started in the context of the record.  
  
> [!NOTE]
>  If an asynchronous system job (workflow) fails several times consecutively, the system starts to postpone execution of that job for longer and longer time intervals so that the administrator or app maker can investigate and resolve the issue. Once the job starts succeeding again, it will resume executing normally.  
  
<a name="BKMK_ActionsOnRunningWorkflows"></a>   
### Actions on running background workflows  
 While a background workflow is running, you have options to **Cancel**, **Pause**, or **Postpone** the workflow. If you have previously paused a workflow, you can **Resume** it.  
  
<a name="BKMK_MonitorSyncWorkflows"></a>   
## Monitoring real-time workflows and actions  
 Real-time workflows and actions do not use System Job records because they occur immediately. Any errors that occur will be displayed to the user in the application with the heading **Business Process Error**.  
  
 There is no log for successful operations. You can enable logging for errors by checking the **Keep Logs for workflow jobs that encountered errors** option in the **Workflow Log Retention** area at the bottom of the **Administration** tab for the process.  
  
 To view the log of errors for a specific process, open the real-time workflow or action definition and go to the **Process Session** tab. This will only show any errors logged for this process.  
  
 If you want a view of all the errors for any process, go to **Advanced Find** and create a view showing errors on the process session entity.  
  
<a name="BKMK_StatusOfWorkflowProcesses"></a>   
## Status of workflow processes  
 When you view a list of workflow processes, any individual process can have one of the following **State** and **Status Reason** values:  
  
|State|Status Reason|  
|-----------|-------------------|  
|Ready|Waiting for Resources|  
|Suspended|Waiting|  
|Locked|In Progress<br /><br /> Pausing<br /><br /> Canceling|  
|Completed|Succeeded<br /><br /> Failed<br /><br /> Canceled|  
  
## Next steps   
 [Best practices for workflow processes](best-practices-workflow-processes.md) <br />

