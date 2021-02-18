---
title: "Use actions | MicrosoftDocs"
description: "With actions, you can perform operations, such as Create, Update, Delete, Assign, or Perform Action. Internally, an action creates a custom message."
ms.custom: ""
ms.date: 08/07/2018
ms.reviewer: ""
ms.service: flow
author: MSFTMAN
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1475985f-d3c4-429d-beac-cb455965e792
caps.latest.revision: 20
ms.author: "DEONHE"
manager: "kvivek"
search.app: 
  - Flow
search.audienceType: 
  - flowmaker
  - enduser
---
# Use actions


[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Actions open a range of possibilities for composing business logic. With actions, you can perform operations, such as Create, Update, Delete, Assign, or Perform Action. Internally, an action creates a custom message. Developers refer to these actions as *messages*. Each of these messages is based on actions taken on a table row. If the goal of a process is to create a row, then update it, and then assign it, there are three separate steps. Each step is defined by the capabilities of the table—not necessarily your business process.  
  
Actions provide the ability to define a single verb (or message) that matches an operation you need to perform for your business. These new messages are driven by a process or behavior rather than what can be done with a table. These messages can correspond to verbs like Escalate, Convert, Schedule, Route, or Approve—whatever you need. The addition of these verbs helps provide a richer vocabulary for you to fluently define your business processes. You can apply this richer vocabulary from clients or integrations rather than having to write the action within clients. This also makes it easier because you can manage and log the success or failure of the entire action as a single unit.  
  
<a name="BKMK_ConfigurableMessages"></a>   
## Configurable messages  
Once an action is defined and activated, a developer can use that message like any of the other messages provided by the platform. However, a significant difference is that now someone who is not a developer can apply changes to what should be done when that message is used. You can configure the action to modify steps as your business processes change. Any custom code that uses that message does not need to be changed as long as the process arguments do not change.  
  
Workflow processes and plug-ins continue to provide similar capabilities for defining automation. Workflow processes still provide the capability for a non-developer to apply changes. But the difference is in how the business processes are composed and how a developer can write their code. An action is a message that operates on the same level as any of the messages provided by the platform. Developers can register plug-ins for actions.  
  
<a name="BKMK_GlobalMessages"></a>   
## Global messages 
 
Unlike Microsoft Dataverse workflows or [plug-ins](/powerapps/developer/data-platform/apply-business-logic-with-code?branch=master#create-a-plug-in), an action doesn’t have to be associated with a specific table. You can define global actions that can be called on their own.

## Next steps

[Create a custom action](create-actions.md)  
  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]