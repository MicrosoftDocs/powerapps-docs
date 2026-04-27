---
title: "Use ITracingService in Plug-ins"
description: "Debugging and/or troubleshooting plug-in issues or behaviors are complicated without rich and insightful logging or tracing."
suite: powerapps
author: sakaralems
ms.author: sakarale
ms.reviewer: pehecke
ms.topic: article
ms.date: 03/02/2026
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Use ITracingService in plug-ins


**Category**: Maintainability, Supportability

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

Debugging and troubleshooting plug-in problems or behaviors is difficult without rich and insightful logging or tracing.

<a name='guidance'></a>

## Guidance

The <xref:Microsoft.Xrm.Sdk.ITracingService> interface helps developers by recording run-time custom information. This information aids in diagnosing the cause of code failures or unexpected behavior in plug-ins. Before writing to the tracing service, first extract the tracing service object from the passed execution context. Then, add [Trace](/dotnet/api/microsoft.xrm.sdk.itracingservice.trace) calls to your custom code where appropriate. Pass any relevant diagnostic information in that method call.

> [!NOTE]
> Trace logging by using the `ITracingService` interface works only when the plug-in is registered in sandbox mode. You must enable trace logging to get run-time data. For more information, see [Tracing and logging](../../logging-tracing.md).

```csharp
//Extract the tracing service for use in debugging sandboxed plug-ins.
ITracingService tracingService =
    (ITracingService)serviceProvider.GetService(typeof(ITracingService));

// Obtain the execution context from the service provider.
IPluginExecutionContext context = (IPluginExecutionContext)
    serviceProvider.GetService(typeof(IPluginExecutionContext));

// For this sample, execute the plug-in code only while the client is online. 
tracingService.Trace("AdvancedPlugin: Verifying the client is not offline.");
if (context.IsExecutingOffline || context.IsOfflinePlayback)
    return;

// The InputParameters collection contains all the data passed 
// in the message request.
if (context.InputParameters.Contains("Target") &&
    context.InputParameters["Target"] is Entity)
{
    // Obtain the target entity from the Input Parameters.
    tracingService.Trace("AdvancedPlugin: Getting the target entity from Input Parameters.");
    Entity entity = (Entity)context.InputParameters["Target"];

    // Obtain the image entity from the Pre Entity Images.
    tracingService.Trace("AdvancedPlugin: Getting image entity from PreEntityImages.");
    Entity image = (Entity)context.PreEntityImages["Target"];
}
```

<a name='additional'></a>

## Additional information

Tracing is especially useful for troubleshooting registered custom code, as it's the only supported troubleshooting method for that scenario. Tracing supports `sandboxed` (partial trust) registered custom code during synchronous or asynchronous execution.

<a name='seealso'></a>

### See also

[Write a plug-in](../../write-plug-in.md)  
[Tracing and logging](../../logging-tracing.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
