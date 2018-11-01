---
title: "Use plug-ins to extend business processes (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "A plug-in is a .NET assembly that you can upload to the Common Data Service for Apps. Classes within the assembly can be registered to specific events (steps) within the event framework. The code within the class provides a way for you to respond to the event so that you can augment or modify the default behavior of the platform." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use plug-ins to extend business processes

A plug-in is a .NET assembly that you can upload to the Common Data Service for Apps. Classes within the assembly can be registered to specific events (steps) within the event framework. The code within the class provides a way for you to respond to the event so that you can augment or modify the default behavior of the platform.

> [!IMPORTANT]
> Whenever possible, you should first consider applying one of the several declarative options to define business logic. More information: [Apply business logic in CDS for Apps](../../maker/common-data-service/cds-processes.md)<br/><br/>
> Use plug-ins when a declarative process doesn’t meet your requirement.

The classes in the assembly that can be registered to a step must implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface. This interface exposes a single method: <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*>. When an event occurs that has a class registered to it, contextual data is passed to the `Execute` method. Within the `Execute` method you can:

- Cancel the event and display an error to the user
- Make changes to the data in the operation
- Initiate other actions using the Organization Service to add automation

Plug-ins can be configured to execute synchronously or asynchronously. A synchronous plug-in will cause the operation to wait until the code in the Plug-in completes. This has an impact on perceived performance of the system. The operations in an asynchronous plug-in are placed in a queue and are executed after the operation is completed so that the operation can complete with minimal interruption.

## When to use plug-ins

People frequently compare workflows and plug-ins as the choices to apply custom business logic. There is significant overlap in the capabilities of workflows and plug-ins. Plug-ins can do everything workflows can do but the inverse is not true. But this doesn't mean you should just use plug-ins for anything that can't be done with a workflow. There are other capabilities to achieve requirements without using plug-ins. 

- Workflows can use custom workflow extensions (workflow activities) which allow you to create re-usable conditions and actions with code that can be used within multiple workflows. 

- Calculated and rollup fields provide capabilities that could previously only be done using workflows.

- Custom Actions are a type of process similar to workflows that allow for creating re-usable messages that can be called from other workflows or from the web service endpoints.

- Azure service bus integration and Web hooks can be used to push data to external systems where logic can be applied using many different resources.

- Microsoft Flow provides many capabilities that previously were performed using plug-ins.

You have many options available to you. You should evaluate each of them to understand the best way to meet your requirements.

### Advantages of plug-ins

These are the main advantages of plug-ins:

- Plug-ins perform well. A well written plug-in provides the most performant way to apply business logic.
- Plug-ins are powerful. Many developers would prefer to use the skills and knowledge they possess to define logic and use the capabilities to work directly with the organization service or external services in code. An experienced plug-in developer can be very productive.

### Disadvantages of plug-ins

- Plug-ins require the special skills of a developer to create and maintain. Developers are expensive and many business don't have access to one when they have a need. Business processes can change rapidly and providing options to enable change without requiring a developer can allow the system to adapt more rapidly.
- Plug-ins can be abused. A poorly written plug-in can cause significant impact on the performance of the environment. The great power of plug-ins needs to be applied with some restraint and consideration for the impact they have on the system as a whole.


## Next Steps

Use the following tutorial and how-to topics to learn how to write plug-ins

### Tutorials

These topics walk you through the process of creating some simple plug-ins.

- [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)
- [Tutorial: Debug a plug-in](tutorial-debug-plug-in.md)
- [Tutorial: Update a plug-in](tutorial-update-plug-in.md)

### How to topics

These topics provide details that you will use to create plug-ins.

- [Write a plug-in](write-plug-in.md)
- [Register a plug-in](register-plug-in.md)
- [Debug Plug-ins](debug-plug-in.md)
