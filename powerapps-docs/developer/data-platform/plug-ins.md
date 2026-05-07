---
title: "Use Plug-ins to Extend Business Processes"
description: "Learn how plug-ins run during Dataverse data events to extend default behavior and implement custom business logic."
ms.collection: get-started
ms.date: 03/30/2026
ms.reviewer: pehecke
ms.topic: article
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - phecke
---

# Use plug-ins to extend business processes

A *plug-in* is a custom event handler that runs in response to a specific event raised during processing of a Microsoft Dataverse data operation. Implement the plug-in as a custom class compiled into a .NET Framework assembly that you can upload and register with Dataverse. You can register one or more compiled plug-in classes within an assembly on specific events (steps) within the Dataverse [event framework](event-framework.md). When the target event occurs during a data processing operation, the code within the registered plug-in class executes, providing a way to augment or modify the default data processing behavior of the platform.

> [!TIP]
> Whenever possible, first consider applying one of the several declarative options to define business logic. For more information, see [Apply business logic in Dataverse](../../maker/data-platform/processes.md).<br/><br/>
> Use plug-ins when a declarative process doesn't meet your requirement.

## More details about plug-ins

Any classes in an assembly that you register on an event framework (pipeline) step must implement the
<xref:Microsoft.Xrm.Sdk.IPlugin> interface. This interface exposes a single method called <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*>. When an event occurs that has a compiled class registered to it, the platform passes contextual data about the data operation being processed to the plug-in's `Execute` method. Within the `Execute` method, your custom code can:

- Cancel the current data processing pipeline operation and optionally display an error to the user
- Make changes to the business data being processed in the current pipeline operation
- Invoke other data operations
- Connect to external systems
- Pass information to another 'downstream' plug-in registered in the same pipeline
- More...

Register plug-ins to execute synchronously or asynchronously. A synchronous plug-in causes the data operation to wait until the code in the plug-in finishes. This delay affects the end-user perceived performance of the system, which is why synchronous plug-ins must execute and complete quickly. Asynchronous plug-in execution is queued and runs after the data operation finishes.

## When to use plug-ins

People frequently compare custom workflow activities and plug-ins as the choices to apply custom business logic. There's significant overlap in the capabilities of workflow activities and plug-ins. Plug-ins can do everything workflow activities can do, but the inverse isn't true. This fact doesn't mean you should just use plug-ins for anything that can't be done with a workflow. Other capabilities can achieve requirements without using plug-ins.

- Workflows can use custom workflow activities, which you can use to create reusable conditions and actions with code that you can use within multiple workflows.

- Calculated and rollup fields provide capabilities that previously could only be done by using workflows.

- Custom Actions are a type of process similar to workflows that you can use to create reusable messages that other workflows or web service endpoints can call.

- Azure Service Bus integration and webhooks can push data to external systems where you can apply logic by using many different resources.

- Power Automate provides many capabilities that previously were performed by using plug-ins.

Evaluate each of these options to understand the best way to meet your requirements.

### Advantages of plug-ins

These are the main advantages of plug-ins:

- Plug-ins perform well. A well-written plug-in provides the most performant way to apply custom business logic.
- Plug-ins are powerful. Many developers prefer to use the skills and knowledge they possess to define logic and use the capabilities to work directly with the Dataverse web service or external services in code. An experienced plug-in developer can be very productive.
- Plug-ins extend the capability of Dataverse when an out-of-box business solution doesn't exist.

### Disadvantages of plug-ins

- Plug-ins require the special skills of a software developer to create and maintain the plug-in code. Smaller businesses might not have access to a developer with the needed skills. Business processes can change rapidly, and providing options to enable change without requiring a developer can allow the system to adapt more rapidly.
- Plug-ins can be abused. A poorly written plug-in can cause significant impact on the perceived performance of the data processing pipeline and ultimately the end-user interactive environment. The great power of plug-ins needs to be applied with some restraint and consideration for the impact it has on the system as a whole.
- Plug-ins have only a short period of time (a hard limit) to complete their work.

## Next steps

To learn more about using plug-ins, see the following tutorial and how-to topics.

### Tutorials

These topics walk you through the basic process of creating, registering, and debugging some simple plug-ins.

- [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)
- [Tutorial: Debug a plug-in](tutorial-debug-plug-in.md)

### How-to topics

These topics provide additional details common to plug-in development.

- [Write a plug-in](write-plug-in.md)
- [Handle exceptions](handle-exceptions.md)
- [Register a plug-in](register-plug-in.md)
- [Debug Plug-ins](debug-plug-in.md), and [Tracing and logging](logging-tracing.md)
- [Troubleshoot plug-ins](/troubleshoot/power-platform/power-apps/dataverse/dataverse-plug-ins-errors)

After you read and understand the plug-in concepts, consider exploring these additional plug-in related capabilities and technologies.

- [Impersonate a user](impersonate-a-user.md)
- [Analyze performance](analyze-performance.md)
- [Access external web resources](access-web-services.md)
- [Write Telemetry to your Application Insights resource using ILogger](application-insights-ilogger.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
