---
title: "Use custom process actions | MicrosoftDocs"
description: "With custom process actions, you can perform operations, such as Create, Update, Delete, Assign, or Perform Action. Internally, an custom process action creates a custom message."
ms.custom: intro-internal
ms.date: 04/28/2021
ms.reviewer: ""
ms.service: powerapps
author: MSFTMAN
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
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

# Use custom process actions

Custom process actions, also known as *Custom actions*, or just *actions*. open a range of possibilities for composing business logic. With custom process actions, you can perform operations, such as Create, Update, Delete, Assign, or Perform Action. Internally, a custom process action creates a custom message. Developers refer to these actions as *messages*. If the goal of a process is to create a row, then update it, and then assign it, there are three separate steps. Each step is defined by the capabilities of the table—not necessarily your business process.  
  
Custom process actions provide the ability to define a single verb (or message) that matches an operation you need to perform for your business. These new messages are driven by a process or behavior rather than what can be done with a table. These messages can correspond to verbs like Escalate, Convert, Schedule, Route, or Approve—whatever you need. The addition of these verbs helps provide a richer vocabulary for you to fluently define your business processes. You can apply this richer vocabulary from clients or integrations rather than having to write the action within clients. This also makes it easier because you can manage and log the success or failure of the entire action as a single unit.  
  
<a name="BKMK_ConfigurableMessages"></a>

## Configurable messages

Once an action is defined and activated, a developer can use that message like any of the other messages provided by the platform. However, a significant difference is that now someone who is not a developer can apply changes to what should be done when that message is used. You can configure the action to modify steps as your business processes change. Any custom code that uses that message does not need to be changed as long as the process arguments do not change.  
  
Workflow processes and plug-ins continue to provide similar capabilities for defining automation. Workflow processes still provide the capability for a non-developer to apply changes. But the difference is in how the business processes are composed and how a developer can write their code. An custom process action is a message that operates on the same level as any of the messages provided by the platform. Developers can register plug-ins for actions.  

> [!NOTE]
> Custom API is a newer way to define custom messages with many advantages for developers. If you do not intend to use the no-code capabilities that custom process actions provide to configure business logic, Custom API provides better capabilities for developers to create their own messages. More information: 
>
> - [Compare Custom Process Action and Custom API](../../developer/data-platform/custom-actions.md#compare-custom-process-action-and-custom-api)
> - [Create and use Custom APIs](../../developer/data-platform/custom-api.md)
  
<a name="BKMK_GlobalMessages"></a>

## Global messages 
 
Unlike Microsoft Dataverse workflows or [plug-ins](../../developer/data-platform/apply-business-logic-with-code.md?branch=master#create-a-plug-in), an custom process action doesn’t have to be associated with a specific table. You can define global custom process actions that can be called on their own.

## Next steps

[Create a custom process action](create-actions.md)  
  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]