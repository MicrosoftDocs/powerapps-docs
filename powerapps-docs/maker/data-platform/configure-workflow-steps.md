---
title: "Configure real-time workflow stages and steps in Power Apps | MicrosoftDocs"
description: "Learn how to configure real-time workflow steps"
ms.custom: ""
ms.date: 07/30/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
author: "Mattp123"
ms.assetid: 0b47dfd5-76db-464f-90c0-c64a0173dcdd
caps.latest.revision: 18
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.app: 
  - Flow
search.audienceType: 
  - flowmaker
  - enduser
---
# Configure real-time workflow stages and steps

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

When you design workflows, you have the option to contain the logic you want to perform in stages and steps.  
  
**Stages**  
Stages make the real-time workflow logic easier to read, and explain the real-time workflow logic. However, stages do not affect the logic or behavior of workflows. If a process has stages, all the steps within the process must be contained with a stage.  
  
**Steps**  
Steps are a unit of business logic within a workflow. Steps can include conditions, actions, other steps, or a combination of these elements.  
  
<a name="BKMK_ActionsWorkflowProcessesCanPerform"></a>  
 
## Actions that real-time workflow processes can perform  

Real-time workflow processes can perform the actions listed in the following table.  
  
|Action|Description|  
|------------|-----------------|  
|**Create Row**|Creates a new row for a table and assigns values that you choose to attributes.|  
|**Update Row**|You can update the row that the real-time workflow is running on, any of the rows linked to that row in an N:1 relationship, or any rows created by earlier steps.|  
|**Assign Row**|You can assign the row that the real-time workflow is running on, any of the rows linked to that row in an N:1 relationship, or any rows created by earlier steps.|  
|**Send Email**|Sends an email. You can choose to create a new email message or use an email template configured for the table of the row that the real-time workflow is running on or any tables that have an N:1 relationship with the table, or the table for any rows created by earlier steps.|  
|**Start Child Workflow**|Starts a real-time workflow process that has been configured as a child workflow.|  
|**Change Status**|Changes the status of the row that the process is running on, any of the rows linked to that row in an N:1 relationship, or any rows created by earlier steps.|  
|**Stop Workflow**|Stops the current workflow. You can set a status of either **Succeeded** or **Canceled** and specify a status message.<br /><br /> When real-time workflows are configured for an event, stopping a real-time workflow with a status of canceled will prevent the event action from completing. Go to [Using real-time workflows](configure-workflow-steps.md#BKMK_SynchronousWorkflows) for more information.|  
|**Custom Step**|Developers can create custom real-time workflow steps that define actions. No custom steps are available by default.|  
  
### Setting row values  

When you create a row, you can set values for the row. When you update a row, you can set, append, increment, decrement, multiply, or clear values.  
  
When you select **Set Properties**, a dialog box opens showing you the default form for the table.  
  
At the bottom of the dialog box you can see a list of additional columns not present in the form.  
  
For any column, you can set a static value and that will be set by the workflow.  
  
On the right side of the dialog box, the **Form Assistant** gives you the ability to set or append dynamic values from the context of the current row. This includes values from related rows that can be accessed from the N:1 (many-to-one) relationships for the table.  
  
The options available in the **Form Assistant** depend on the column you have selected in the form. When you set a dynamic value, you will see a yellow placeholder known as a ‘slug’ that shows where the dynamic data will be included. If you want to remove the value, select the slug and delete it. For text columns, you can use a combination of static and dynamic data.  
  
With dynamic values, you don’t know for certain that a column or related table has the value you want to set. You can actually set a number of columns to try to set the value and sort them in order using the green arrows. If the first column doesn’t have data, try the second column and so on. If none of the columns have data, you can specify a default value to be used.  
  
<a name="BKMK_SettingConditionsForWorkflowActions"></a>   

## Setting conditions for real-time workflow actions  

The actions that you will apply often depend on conditions. Real-time workflow processes provide several ways to set conditions and create branching logic to get the results you want. You can check values of the row that the real-time workflow process is running against, any of the rows linked to that row with an N:1 relationship, or values within the process itself.  
  
|Condition Type|Description|  
|--------------------|-----------------|  
|**Check Condition**|A logical "if \<condition> then" statement.<br /><br /> You can check the current values for the row that the real-time workflow is running on, any of the rows linked to that row in an N:1 relationship, or any rows created by earlier steps. Based on these values, you can define additional steps when the condition is true.<br /><br /> In the "if \<condition> then" statement, you can use the following operators: **Equals**, **Does Not Equal**, **Contains Data**, **Does Not Contain Data**, **Under** and **Not Under**. <br /><br />**Note:**  The **Under** and **Not Under** are hierarchical operators. They can only be used on the tables that have a hierarchical relationship defined. If you’re trying to use these operators on the tables that don’t have the hierarchical relationship defined, you’ll see the error message: “You’re using a hierarchical operator on a table that doesn’t have a hierarchical relationship defined. Either make the table hierarchical (by marking a relationship as hierarchical) or use a different operator.” <br /><br />For more information about hierarchical relationships, go to [Define and query hierarchically related data](./define-query-hierarchical-data.md). A screenshot that follows the table is an example of the definition of the real-time workflow process that uses the **Under** and **Not Under** hierarchical operators.|  
|**Conditional Branch**|A logical "else-if-then" statement, the editor uses the text “Otherwise, if \<condition> then:”<br /><br /> Select a check condition you have previously defined and you can add a conditional branch to define additional steps when the check condition returns false.|  
|**Default Action**|A logical "else" statement. The editor uses the text “Otherwise:”<br /><br /> Select a check condition, conditional branch, wait condition, or parallel wait branch that you have previously defined and you can use a default action to define steps for all cases that do not match the criteria defined in condition or branch elements.|  
|**Wait Condition**|Enables a real-time workflow to pause itself until the criteria defined by the condition have been met. The real-time workflow starts again automatically when the criteria in the wait condition have been met.<br /><br /> Real-time workflows cannot use wait conditions.|  
|**Parallel Wait Branch**|Defines an alternative wait condition for a real-time workflow with a corresponding set of additional steps that are performed only when the initial criterion is met. You can use parallel wait branches to create time limits in your real-time workflow logic. They help prevent the real-time workflow from waiting indefinitely until the criteria defined in a wait condition have been met.|  
|**Custom Step**|Developers can create custom real-time workflow steps that define conditions. There are no custom steps available by default.|  
  
The following screenshot contains an example of the workflow process definition with the **Under** and **Not Under** hierarchical operators. In our example, we apply two different discounts to two groups of accounts. In **Add Step**, we selected the **Check Condition** to specify the **if-then** condition containing the **Under** or **Not Under** operators. The first **if-then** condition applies to all accounts that are **Under** the Alpine Ski House account. These accounts receive a 10% discount on purchased good and services. The second **if-then** condition applies to all accounts that are **Not Under** the Alpine Ski House account and they receive a 5% discount. Then, we selected **Update Row** to define the action to be performed based on the condition.  
  
![Workflow process with Under&#47;Not Under operators.](media/wfp-under-not-under.PNG "Workflow process with Under/Not Under operators")  
  
<a name="BKMK_SynchronousWorkflows"></a>   

### Initiating real-time workflows before or after status changes  

 When you configure **Options for Automatic Processes** for real-time workflows, the **Start When** options for the status changes event let you select **After** or **Before** for when status changes. The default option is **After**.  
  
 When you select **Before** you are saying that you want the logic in the real-time workflow to be applied before data changing the status is saved. This provides you with the ability to check the values before other logic has been applied after the operation and prevent further logic from being performed. For example, you may have additional logic in a plug-in or custom real-time workflow action which could initiate actions on another system. By stopping further processing you can avoid cases where external systems are affected. Applying real-time workflows before this event also means that other real-time workflow or plug-in actions that may have saved data don’t need to be “rolled back” when the operation is canceled.  


|Action  |Start when  |Explanation  |
|---------|---------|---------|
|Row is created   | After    | Only **After** is available. The row won't have a unique identifier until after the internal MainOperation stage so can’t occur before the row is created.      |
|Row status changes   |  Before <br />  After     |  Corresponds to an update operation that provides the ability to apply real-time workflow logic either after or before the status changes. **Before** corresponds to the preoperation stage. **After** corresponds to the postoperation stage.       |
|Row is assigned   |  Before <br />  After     |  Corresponds to an update operation that provides the ability to apply real-time workflow logic either after or before the status changes. **Before** corresponds to the preoperation stage. **After** corresponds to the postoperation stage.       |
|Row columns change     |  Before <br />  After   |  Corresponds to an update operation that provides the ability to apply real-time workflow logic either after or before the status changes. **Before** corresponds to the preoperation stage. **After** corresponds to the postoperation stage.        |
|Row is deleted     |  Before       |  Only **Before** is available. Row deletion corresponds to the PreOperation stage. After the MainOperation occurs, the row is deleted and there is no further status change that can occur.       |

For more information about preoperation, mainoperation, and postoperation stages, see [Event execution pipeline](../../developer/data-platform/event-framework.md#event-execution-pipeline).

## Using real-time workflows  

You can configure real-time workflows but you should use them with care. Background workflows are generally recommended because they allow the system to apply them when resources on the server are available. This helps smooth out the work the server has to do and helps maintain the best performance for everyone using the system. The drawback is that actions defined by background workflows are not immediate. You can’t predict when they will be applied, but generally it will take a few minutes. For most automation of business processes, this is fine because people using the system don’t need to be consciously aware that the process is running.  
  
Use real-time workflows when a business process requires someone to immediately see the results of the process or if you want the ability to cancel an operation. For example, you might want to set certain default values for a row the first time it’s saved, or you want to make sure that some rows are not deleted.  
  
### Converting between real-time and background workflows  

You can change a real-time workflow into a background workflow by choosing **Convert to a background workflow** on the toolbar.  
  
You can change a background workflow into a real-time workflow by choosing **Convert to a real-time workflow** on the toolbar. If the background workflow uses a wait condition, it will become invalid and you won’t be able to activate it until you remove the wait condition.  
  

### Initiating real-time workflows before or after status changes  

When you configure **Options for Automatic Processes** for real-time workflows, the **Start When** options for the status changes event let you select **After** or **Before** for when status changes. The default option is **After**.  
  
When you select **Before**, you are saying that you want the logic in the real-time workflow to be applied before data changing the status is saved. This provides you with the ability to check the values before other logic has been applied after the operation and prevents further logic from being performed. For example, you might have additional logic in a plug-in or custom real-time workflow action that could initiate actions on another system. By stopping further processing you can avoid cases where external systems are affected. Applying real-time workflows before this event also means that other real-time workflow or plug-in actions that might have saved data don’t need to be “rolled back” when the operation is canceled.  
  

### Using the Stop Workflow action with real-time workflows  

When you apply a **Stop Workflow** action in a real-time workflow, you have the option to specify a status condition that can be either **Succeeded** or **Canceled**. When you set the status to canceled, you prevent the operation. An error message containing the text from the stop action status message will be displayed to the user with the heading **Business Process Error**.  
  
## Next steps  
<!-- [Create custom business logic with processes](./guide-staff-through-common-tasks-processes.md)   
[Workflow processes overview](workflow-processes.md)    -->
[Monitor and manage real-time workflow processes](monitor-manage-processes.md)   
[Best practices for real-time workflow processes](best-practices-workflow-processes.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]