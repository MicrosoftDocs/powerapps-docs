---
title: "Actions overview | MicrosoftDocs"
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
  - "PowerApps"
ms.assetid: 1475985f-d3c4-429d-beac-cb455965e792
caps.latest.revision: 20
ms.author: "matp"
manager: "kvivek"
---
# Actions overview

Actions are a type of process. You can invoke actions, including custom actions, directly from a workflow or dialog without writing code! More information: [Invoke custom actions from a workflow](invoke-custom-actions-workflow-dialog.md)   
  
 Actions can also be invoked by running custom code that uses the Common Data Service for Apps web services.  
  
 You can call actions:  
  
-   From code that executes within a plug-in or custom workflow.  
  
-   From a command that is placed in the application and executes the operation using JavaScript code.  
  
-   From an integration with another system that uses the Common Data Service for Apps web services.  
  
-   From a custom client application that uses the Common Data Service for Apps web services.  
  
Developers can learn more in this topic:  [Create your own actions](https://docs.microsoft.com/dynamics365/customer-engagement/developer/create-own-actions). 
  
<a name="BKMK_WhyActions"></a>   
## Why use actions?  
 Actions open a range of possibilities for composing business logic. Before Actions, the primary way to implement business processes was limited to plug-ins or custom workflow activities. With Actions, you can perform operations, such as Create, Update, Delete, Assign, or Perform Action. Internally, an action creates a custom message. Developers refer to these actions as ”messages”. Each of these messages is based on actions taken on an entity record. If the goal of a process is to create a record, then update it, and then assign it, there are three separate steps. Each step is defined by the capabilities of the entity – not necessarily your business process.  
  
 Actions provide the ability to define a single verb (or message) that matches an operation you need to perform for your business. These new messages are driven by a process or behavior rather than what can be done with an entity. These messages can correspond to verbs like Escalate, Convert, Schedule, Route, or Approve – whatever you need. The addition of these verbs helps provide a richer vocabulary for you to fluently define your business processes. You can apply this richer vocabulary from clients or integrations rather than having to write the action within clients. This also makes it easier because you can manage and log the success or failure of the entire action as a single unit.  
  
<a name="BKMK_ConfigurableMessages"></a>   
## Configurable messages  
 Once an action is defined and activated, a developer can use that message like any of the other messages provided by the platform. However, a significant difference is that now someone who is not a developer can apply changes to what should be done when that message is used. You can configure the action to modify steps as your business processes change. Any custom code that uses that message does not need to be changed as long as the process arguments do not change.  
  
 Workflow processes and plug-ins continue to provide similar capabilities for defining automation. Workflow processes still provide the capability for a non-developer to apply changes. But the difference is in how the business processes are composed and how a developer can write their code. An action is a message that operates on the same level as any of the messages provided by the platform. Developers can register plug-ins for Actions.  
  
<a name="BKMK_GlobalMessages"></a>   
## Global messages  
 Unlike workflow processes or plug-ins, an action doesn’t have to be associated with a specific entity. You can define ”global” Actions that can be called on their own.  
  
## See also  
[Create your own actions](https://docs.microsoft.com/dynamics365/customer-engagement/developer/create-own-actions)

[Configure custom actions from a workflow](configure-actions.md)

[Invoke custom actions from a workflow or dialog](invoke-custom-actions-workflow-dialog.md) 

[Workflow processes overview](workflow-processes.md)   

[Business process flows overview](../model-driven-apps/business-process-flows-overview.md)   
