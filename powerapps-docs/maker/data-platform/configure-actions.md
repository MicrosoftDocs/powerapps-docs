---
title: "Configure custom process actions from a workflow | MicrosoftDocs"
description: "Learn how to configure actions for workflows in Power Apps."
ms.custom: ""
ms.date: 04/28/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "Power Apps"
author: "Mattp123"
ms.assetid: 6dbc0f10-7ac5-4685-ab74-22d24bf7102d
caps.latest.revision: 19
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.app: 
  - Flow
search.audienceType: 
  - flowmaker
  - enduser
---

# Configure custom process actions from a workflow

You can enable a custom process action from a real-time workflow without writing code. More information: [Invoke custom actions from a workflow](invoke-custom-actions-workflow-dialog.md)  
  
You also can create a custom process action so that a developer can use it in code, or you might need to edit an action that was previously defined. Like real-time workflow processes, consider the following:  
  
- What should the action do?  
  
- Under what conditions should the action be performed?  
 
Unlike real-time workflow processes, you don’t need to set the following options:  
  
- **Start When**: Custom process actions start when code calls the message generated for them.  
  
- **Scope**: Custom process actions always run in the context of the calling user.  
  
- **Run in the background**: Custom process actions are always real-time workflows.  
  
Custom process actions also have something that real-time workflow processes don’t—input and output arguments. More information: [Define process arguments](configure-actions.md#BKMK_DefineProcessArgs)  
  
<a name="create"></a>

## Create a custom process action  
  
> [!IMPORTANT]
> If you’re creating an action to include as part of a solution that will be distributed, create it in the context of the solution. Go to **[Settings](../model-driven-apps/advanced-navigation.md#settings)** > **Solutions** and locate the unmanaged solution that this action will be part of. Then, in the menu bar, select **New** > **Process**. This ensures that the customization prefix associated with the name of the action will be consistent with other components in the solution. After you create the action, you can’t change the prefix.  


> [!NOTE]
> If you intend to write a plug-in to implement your logic for a custom process action instead of using the workflow designer, you should use Custom API instead. More information: [Compare Custom Process Action and Custom API](../../developer/data-platform/custom-actions.md#compare-custom-process-action-and-custom-api)
  
Like real-time workflow processes, actions have the following properties in the **Create Process** dialog box:  
  
- **Process name**  

  After you enter a name for the process, a unique name will be created for it by removing any spaces or special characters from the process name.  
  
- **Category**  

  This property establishes that this is an action process. You can’t change this after you save the process.  
  
- **Entity**  

  With action processes, you can select a table to provide context for the real-time workflow just like other types of processes, but you also have the option to choose **None (global)**. Use this if your action doesn’t require the context of a specific table. You can’t change this after you save the process.  
  
- **Type**  

  Use this property to choose whether to build a new custom process action from scratch or to start from an existing template.  
  
<a name="edit"></a>

## Edit an action

You must deactivate processes before you can edit them.  
  
You can edit a custom process action that was created as part of an unmanaged solution or included in a solution installed in your organization. If the solution is a managed solution, you might not be able to edit it. The solution publisher has the option to edit the managed properties so that the action installed with a managed solution can’t be edited.  
  
When an action is saved, a unique name is generated based on the process name. This unique name has the customization prefix added from the solution publisher. This is the name of the message that a developer will use in their code.  
  
When editing an action, you have the following options:  
  
- **Process Name**  

  After the process is created and the unique name is generated from the process name, you can edit the process name. You might want to apply a naming convention to make it easier to locate specific processes.  
  
- **Unique Name**  

  When a custom process action is saved, a unique name is generated based on the process name. This unique name has the customization prefix from the solution publisher added. This is the name of the message that a developer will use in their code. Don’t change this unique name if the process has been activated and code is in place expecting to call the action using this name.  
  
  > [!IMPORTANT]
  > After the action is activated and code is written to use a unique name, the unique name must not be changed without also changing the code that references it.  
  
- **Enable rollback**  

  Generally, processes that support transactions will “undo” (or roll back) the entire operation if any part of them fails. There are exceptions to this. Actions executed in code by a developer initiated by the custom process action might not support transactions. An example would be when the code perform actions in other systems that are beyond the scope of the transaction. Those can’t be rolled back by the action running in an app. Some messages in the platform don’t support transactions. But everything you can do just with the user interface of the action will support transactions. All the actions that are part of a real-time workflow are considered in transaction, but with actions you have the option to opt out of this.  
  
  You should consult with the developer who will use this message to determine whether it must be in transaction or not. Generally, an action should be in transaction if the actions performed by the business process don’t make sense unless all of them are completed successfully. The classic example is transferring funds between two bank accounts. If you withdraw funds from one account you must deposit them in the other. If either fails, both must fail.  
  
  > [!NOTE]
  > - You can’t enable rollback if a custom process action is invoked directly from within a workflow. You can enable rollback if an custom process action is triggered by a Power Apps web services message.  
  > - If the action defined does not change data, but only retrieves data, there are certain situations where performance can be improved by disabling **Enable rollback.**
  
- **Activate As**  

  Like all processes, you can activate the process as a template and use it as an advanced starting point for processes that follow a similar pattern.  
  
- **Define Process Arguments**  

  In this area, you’ll specify any data that the action expects to start and what data will be passed out of the action. More information: [Define process arguments](configure-actions.md#BKMK_DefineProcessArgs)  
  
- **Add Stages, Conditions and Actions**  

  Like other processes, you specify what actions to perform and when to perform them. More information: [Add stages, conditions and actions](configure-actions.md#BKMK_AddStagesConditionsAndActions)

<a name="BKMK_DefineProcessArgs"></a>

### Define process arguments

When a developer uses a message, they might begin with some data that they can pass into the message. For example, to create a new case row, there might be the case title value that is passed in as the input argument.  
  
When the message is finished, the developer might need to pass some data that was changed or generated by the message to another operation in their code. This data is the output argument.  
  
Both input and output arguments must have a name, a type, and some information about whether the argument is always required. You can also provide a description.  
  
The name of the message and the information about all the process arguments represent the *signature* for the message. After an action is activated and is being used in code, the signature must not change. If this signature changes, any code that uses the message will fail. The only exception to this might be changing one of the parameters so that it is not always required.  
  
You can change the order of the arguments by sorting them or moving them up or down because the arguments are identified by name, not by the order. Also, changing the description won’t break code using the message.  
  
#### Action process argument types

The following table describes the action process argument types.  
  
|Type|Description|  
|----------|-----------------|  
|Boolean|A `true` or `false` value.|  
|DateTime|A value that stores date and time information.|  
|Decimal|A number value with decimal precision. Used when precision is extremely important.|  
|Table|A row for the specified table. When you select **Table**, the drop-down list is enabled, allowing you to select the table type.|  
|entityCollection|A collection of table rows.|  
|entityReference|An object that contains the name, ID, and type of a table row that uniquely identifies it. When you select tableReference, the drop-down list is enabled and allows you to select the table type.|  
|Float|A number value with decimal precision. Used when data comes from a measurement that isn’t absolutely precise.|  
|Integer|A whole number.|  
|Money|A value that stores data about an amount of money.|  
|Picklist|A value that represents an option for an OptionSet attribute.|  
|String|A text value.|  
  
> [!NOTE]
> **entityCollection** argument values can’t be set in the user interface for conditions or actions. These are provided for use by developers in custom code. More information: [Create your own messages](../../developer/data-platform/custom-actions.md)
  
<a name="BKMK_AddStagesConditionsAndActions"></a>

### Add stages and steps

Actions are a type of process very similar to real-time workflows. All the steps that can be used in real-time workflows can be used in actions. For information about the steps that can be used for both real-time workflows and actions, go to [Workflow stages and steps](configure-workflow-steps.md).  
  
In addition to the steps that can be used for real-time workflows, actions also have the **Assign Value** step.  In actions, these can be used only to set output arguments. You can use the form assistant to set output arguments to specific values or, more likely, to values from the row that the action is running against, rows related to that row with a many-to-one relationship, rows created in an earlier step, or values that are part of the process itself.  
  
## Managed properties

Custom process actions have two relevant managed properties

### Is Customizable

The **Is Customizabl**e managed property controls whether on not someone who installs a managed solution containing the custom process action can edit or delete it. If wish for the custom process action to be edited or deleted when included in a managed solution, you should set this property to true.

### Is Custom Processing Step Allowed for Other Publishers

The **Is Custom Processing Step Allowed for Other Publishers** managed property controls whether third party plug-in developers can register plug-in steps on the message created by the custom process action. When this is true, plug-ins registered by anyone on this message will run and can modify the behavior of the custom process action. When false, only plug-ins steps registered within a solution from the same solution publisher will run.
  

## Next steps

[Use actions](actions.md)  
[Invoke custom actions from a workflow](invoke-custom-actions-workflow-dialog.md)   
[Monitoring real-time workflows and actions](monitor-manage-processes.md#BKMK_MonitorSyncWorkflows)
 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]