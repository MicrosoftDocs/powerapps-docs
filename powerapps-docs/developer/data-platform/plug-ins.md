---
title: "Use plug-ins to extend business processes (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how plug-ins execute in response to a data processing event to augment or modify the default behavior of the platform." # 115-145 characters including spaces. This abstract displays in the search result.
ms.collection: get-started
ms.date: 02/14/2023
ms.reviewer: "phecke"
ms.topic: "article"
author: "divkamath" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "dikamath" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - phecke
---

# Use plug-ins to extend business processes

A *plug-in* is a custom event handler that executes in response to a specific event raised during processing of a Microsoft Dataverse data operation. The plug-in is implemented as a custom class compiled into a .NET Framework assembly that can be uploaded and registered with Dataverse. One or more compiled plug-in classes within an assembly can be registered on specific events (steps) within the Dataverse [event framework](event-framework.md). When the target event occurs during a data processing operation, the code within the registered plug-in class executes providing a means to augment or modify the default data processing behavior of the platform.

> [!TIP]
> Whenever possible, you should first consider applying one of the several declarative options to define business logic. More information: [Apply business logic in Dataverse](../../maker/data-platform/processes.md)<br/><br/>
> Use plug-ins when a declarative process doesn’t meet your requirement.

## More details about plug-ins

Any classes in an assembly that are to be registered on an event framework (pipeline) step must implement the 
<xref:Microsoft.Xrm.Sdk.IPlugin> interface. This interface exposes a single method called <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*>. When an event occurs that has a compiled class registered to it, contextual data about the data operation being processed is passed to the plug-in's `Execute` method. Within the `Execute` method your custom code can:

- Cancel the current data processing pipeline operation and optionally display an error to the user
- Make changes to the business data being processed in the current pipeline operation
- Invoke other data operations
- Connect to external systems
- Pass information to another 'downstream' plug-in registered in the same pipeline
- More...

Plug-ins can be registered to execute synchronously or asynchronously. A synchronous plug-in will cause the data operation to wait until the code in the plug-in completes. This has an impact on end-user perceived performance of the system, which is why synchronous plug-ins must execute and complete quickly. Asynchronous plug-in execution is queued and later executed after the data operation has completed.

## When to use plug-ins

People frequently compare workflows and plug-ins as the choices to apply custom business logic. There is significant overlap in the capabilities of workflows and plug-ins. Plug-ins can do everything workflows can do but the inverse is not true. But this doesn't mean you should just use plug-ins for anything that can't be done with a workflow. There are other capabilities to achieve requirements without using plug-ins.

- Workflows can use custom workflow extensions (workflow activities) which allow you to create re-usable conditions and actions with code that can be used within multiple workflows.

- Calculated and rollup fields provide capabilities that could previously only be done using workflows.

- Custom Actions are a type of process similar to workflows that allow for creating re-usable messages that can be called from other workflows or from the web service endpoints.

- Azure Service Bus integration and Webhooks can be used to push data to external systems where logic can be applied using many different resources.

- Power Automate provides many capabilities that previously were performed using plug-ins.

You have many options available to you. You should evaluate each of them to understand the best way to meet your requirements.

### Advantages of plug-ins

These are the main advantages of plug-ins:

- Plug-ins perform well. A well written plug-in provides the most performant way to apply custom business logic.
- Plug-ins are powerful. Many developers would prefer to use the skills and knowledge they possess to define logic and use the capabilities to work directly with the organization web service or external services in code. An experienced plug-in developer can be very productive.
- Plug-ins extend the capability of Dataverse when an out-of-box business solution does not exist.

### Disadvantages of plug-ins

- Plug-ins require the special skills of a software developer to create and maintain the plug-in code. Smaller businesses may not have access to a developer with the needed skills. Business processes can change rapidly and providing options to enable change without requiring a developer can allow the system to adapt more rapidly.
- Plug-ins can be abused. A poorly written plug-in can cause significant impact on the performance of the data processing pipeline and ultimately the environment. The great power of plug-ins needs to be applied with some restraint and consideration for the impact it has on the system as a whole.

## Next Steps

Use the following tutorial and how-to topics to learn more about using plug-ins

### Tutorials

These topics walk you through the basic process of creating, registering, and debugging some simple plug-ins.

- [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)
- [Tutorial: Debug a plug-in](tutorial-debug-plug-in.md)

### How to topics

These topics provide additional details common to plug-in development.

- [Write a plug-in](write-plug-in.md)
- [Handle exceptions](handle-exceptions.md)
- [Register a plug-in](register-plug-in.md)
- [Debug Plug-ins](debug-plug-in.md), and [Tracing and logging](logging-tracing.md)
- [Troubleshoot plug-ins](troubleshoot-plug-in.md)
- [Dependent Assembly plug-ins](dependent-assembly-plugins.md)

Once you have read and understand the plug-in concepts listed above, consider exploring these additional plug-in related capabilities and technologies.

- [Impersonate a user](impersonate-a-user.md)
- [Analyze performance](analyze-performance.md)
- [Access external web resources](access-web-services.md)
- [Write Telemetry to your Application Insights resource using ILogger](application-insights-ilogger.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
