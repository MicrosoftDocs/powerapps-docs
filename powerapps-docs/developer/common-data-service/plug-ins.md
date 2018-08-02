---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Write plug-ins to extend business processes

A plug-in is a .NET assembly that you can upload to the Common Data Service for Apps. Classes within the assembly can be registered to specific events (steps) within the event framework. The code within the class provides a way for you to respond to the event so that you can augment or modify the default behavior of the platform.

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

[Write a plug-in](write-plug-in.md)

<!-- Needs major attention

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/plugin-development
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/write-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/understand-data-context-passed-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/handle-exceptions-plugins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/pass-data-between-plug-ins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/impersonation-plugins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/register-deploy-plugins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/debug-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/analyze-plugin-performance
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/walkthrough-register-plugin-using-plugin-registration-tool
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-create-basic-plugin

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/plug-in-entities
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/plug-in-registration-entities

Notes:
https://microsoft-my.sharepoint.com/:w:/p/jdaly/ETkwQsIe2VtCvxAyqTPKfTIBKDrLhcEjAm4JaJPfakQ8ww?e=2pxLqD 

See tutorials
https://microsoft-my.sharepoint.com/:w:/p/jdaly/EZ1SzmOh-B5Bnt4C9rxGWysB6NtUQonOxq5sGSPkn5vNAA?e=bGWQN3

This is conceptual
write-plug-in.md should be how-to?


Need to move the items below
-->

## Tracing

## Context information available to your code

## Impersonation

There are two ways to apply impersonation in plug-ins: at registration or execution.

### At plug-in registration

When you register a plug-in step you can specify a user account to use when the code is run by choosing from the **Run in User's Context** option. By default this is set to use the **Calling User**, which is the user account which initiated the action. When this default option is applied, the [SdkMessageProcessingStep.ImpersonatingUserId](reference/entities/sdkmessageprocessingstep.md#BKMK_ImpersonatingUserId) will be set to null or <xref:System.Guid.Empty>.

### During plug-in execution

You can override the setting specified at registration at run time by setting the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> `userId` parameter.

This is typically set to the <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.UserId> value which will apply the user account defined by the plug-in step registration.

```csharp
(IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    IOrganizationService service = serviceFactory.CreateOrganizationService(context.UserId);
```

If you want to override the step registration you can pass the value of the <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.InitiatingUserId> to have a service that will use the user account that initiated the action that caused the plug-in to run.

You can also provide the [SystemUser.SystemUserId](reference/entities/systemuser.md#BKMK_SystemUserId) from any valid user account. This will work as long as that user has the permissions to perform the operations in the plug-in.

## See also

[Sample: Web access from a sandboxed plug-in](org-service/samples/web-access-plugin.md)

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-web-access-sandboxed-plugin -->