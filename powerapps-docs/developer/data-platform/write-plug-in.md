---
title: "Write a plug-in (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to write custom code to be executed in response to data processing events." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/31/2023
ms.reviewer: "pehecke"
ms.topic: "article"
author: "divkamath" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "dikamath" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - phecke
---

# Write a plug-in

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can create plug-ins by using one of the following two methods:

- Power Platform development tools provide a modern way to create plug-ins. The tools being referred to here are *Power Platform Tools for Visual Studio* and *Power Platform CLI*. Both these Power Platform tools generate similar plug-in code so moving from one tooling method to the other is fairly easy and understandable.

  - Use [Power Platform Tools for Visual Studio](tools/devtools-install.md) to quickly create and register (deploy) plug-ins. A [quickstart](tools/devtools-create-plugin.md) article is available to show you how. Use this tool if you like to work in Visual Studio.

  - Use [Power Platform CLI](/power-platform/developer/cli/introduction) to create a basic (Visual Studio compatible) plug-in project with template plug-in code using a single [pac plugin](/power-platform/developer/cli/reference/plugin) command. Afterwards, using the [pac tool prt](/power-platform/developer/cli/reference/tool#pac-tool-prt) command, you interactively use the Plug-in Registration tool to register your creation with Microsoft Dataverse. Use this CLI tool set if you like working in a terminal window or Visual Studio Code.

- Manually write code using your favorite editor or IDE. The rest of the plug-in documentation in this article and the other related articles is written with the developer writing code in mind, however the concepts introduced apply to all methods of plug-in development.

## IPlugin interface

A plug-in is a compiled class within an assembly built to target .NET Framework 4.6.2. Each class in a plug-in project that is registered on an [event pipeline step](event-framework.md) must implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface, which defines a single <xref:Microsoft.Xrm.Sdk.IPlugin.Execute%2A?displayProperty=nameWithType> method.

```csharp
public class MyPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        throw new NotImplementedException();
    }
}
```

The <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method accepts a single <xref:System.IServiceProvider> parameter. The `IServiceProvider` has a single method:  <xref:System.IServiceProvider.GetService*>. Use this method to get several different types of services that you can use in your code.

More information: [Services you can use in your code](#services-you-can-use-in-your-code)

> [!IMPORTANT]
> When deriving from `IPlugin`, the class should be written *stateless*. This is because the platform caches a class instance and re-uses it for performance reasons. A simple way of thinking about this is that you shouldn't add any properties or methods to the class and everything should be included within the `Execute` method.
>
> When using Power Platform tools for plug-in creation, the generated `PluginBase` class is derived from `IPlugin`.

There are some exceptions to the statement about adding properties or methods in the note above. For example, you can have a property that represents a constant and you can have methods that are called from the `Execute` method. The important thing is that you never store any service instance or context data as a property in your class. These values change with every invocation and you don't want that data to be cached and applied to subsequent invocations.

More information: [Develop IPlugin implementations as stateless](/dynamics365/customer-engagement/guidance/server/develop-iplugin-implementations-stateless)

### Pass configuration data to your plug-in

When you register a plug-in, you may optionally specify configuration data to pass to the plug-in at run-time. Configuration data allows you to define how a specific instance of a registered plug-in should behave. This information is passed as string data to parameters in the constructor of your class. There are two parameters named `unsecure` and `secure`. Use the first `unsecure` parameter for data that you don't mind if someone else can see. Use the second `secure` parameter for sensitive data.

The following code shows the three possible constructor signatures for a plug-in class named MyPlugin.

```csharp
public MyPlugin() {}
public MyPlugin(string unsecure) {}  
public MyPlugin(string unsecure, string secure) {}
```

The secure configuration data is stored in a separate table that only system administrators have privileges to read.

More information: [Register plug-in step > Set configuration data](register-plug-in.md#set-configuration-data)

## Services you can use in your code

Typically, within your plug-in you will:

- Access the contextual data passed to your plug-in to determine information about the entity and message request that caused the event and invoked your plug-in. This data is called the *execution context*.
- Access the Organization web service using SDK for .NET calls to perform message request operations like query, create, update, delete, and more.
- Write messages to the Tracing service so you can evaluate how your plug-in code is executing.

The <xref:System.IServiceProvider>.<xref:System.IServiceProvider.GetService%2A> method provides you with a way to access service references passed in the execution context when needed. To get an instance of a service, you invoke the `GetService` method passing the type of service. Read more about this in the next sections.

### Execution context

The execution context contains a wealth of information that a plug-in may need. The context is obtained using the following code.

```csharp
IPluginExecutionContext context = (IPluginExecutionContext)
    serviceProvider.GetService(typeof(IPluginExecutionContext));
```

More information: <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext>, [Understand the execution context](understand-the-data-context.md)

### Organization web service

In addition to the data passed in the execution context, Dataverse table row data can be read or written from plug-in code using SDK calls to the Organization web service. Don't try to use the Web API as it isn't supported in plug-ins. Also, don't authenticate the user before accessing the web services as the user is preauthenticated before plug-in  execution.

More information: [Table Operations](org-service/entity-operations.md), [Use messages](org-service/use-messages.md)

To obtain an object reference to the Organization web service use the following code:

```csharp
IOrganizationServiceFactory serviceFactory =
    (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
IOrganizationService orgService = serviceFactory.CreateOrganizationService(context.UserId);
```

### Tracing service

Use the tracing service to write messages to the [PluginTraceLog Table](reference/entities/plugintracelog.md) so that you can review the logs to understand what occurred when the plug-in ran.

To write to the tracelog, you need to get an instance of the Tracing service. The following code shows how to get an instance of the Tracing service using the <xref:System.IServiceProvider>.<xref:System.IServiceProvider.GetService*> method.


```csharp
ITracingService tracingService =
    (ITracingService)serviceProvider.GetService(typeof(ITracingService));
```

To write to the trace, use the <xref:Microsoft.Xrm.Sdk.ITracingService>.<xref:Microsoft.Xrm.Sdk.ITracingService.Trace*> method.

```csharp
tracingService.Trace("Write {0} {1}.", "your", "message");
```

More information: [Use Tracing](debug-plug-in.md#use-tracing), [Tracing and logging](logging-tracing.md).

### Other services

When you write a plug-in that uses Azure Service Bus integration, use the notification service that implements the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService> interface, but this won't be described here.

More information: [Azure Integration](azure-integration.md)

## Putting it all together

Applying the plug-in concepts detailed previously results in plug-in code that looks like the following.

```csharp
public class MyPlugin : IPlugin
{
  public MyPlugin() {} // Constructor, does nothing

  public void Execute(IServiceProvider serviceProvider)
  {
    // Obtain the execution context
    IPluginExecutionContext context = (IPluginExecutionContext)
      serviceProvider.GetService(typeof(IPluginExecutionContext));

    // Obtain the Organization service reference 
    IOrganizationServiceFactory serviceFactory =
      (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    IOrganizationService orgService = serviceFactory.CreateOrganizationService(context.UserId);

    // Obtain the Tracing service reference
    ITracingService tracingService =
      (ITracingService)serviceProvider.GetService(typeof(ITracingService));

    try
    {
      // TODO Plug-in business logic goes here. You can access data in the context,
      // and make calls to the Organization web service using the Dataverse SDK.
    }
    catch (FaultException<OrganizationServiceFault> ex)
    {
      throw new InvalidPluginExecutionException("The following error occurred in MyPlugin.", ex);
    }
    catch (Exception ex)
    {
        tracingService.Trace("MyPlugin: error: {0}", ex.ToString());
        throw;
    }
}
```

More information about handling exceptions: [Handle exceptions in plug-ins](handle-exceptions.md)

## Plug-in design impacts performance

When writing your plug-in, it's critical that it must execute efficiently and quickly. However long your plug-in takes to execute causes the end user that invoked the message operation (which triggered your plug-in) to wait. In addition to processing the message operation, Dataverse executes all registered synchronous plug-ins in the pipeline including your plug-in. When plug-ins take too long to execute, or if too many plug-ins are registered in a pipeline, this can result in a nonresponsive application UI or worst case a timeout error with pipeline rollback.

> [!IMPORTANT]
> Plug-ins must adhere to an execution time limit and resource constraints.
> More information: [Anaylyze plug-in performance](analyze-performance.md)

## Using early-bound types in plug-in code

You can optionally use [early-bound](org-service/early-bound-programming.md) types within plug-in code. Include the generated types file in your plug-in project. All table types provided in the execution context's [InputParameters](xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters) collection are late-bound types. You would need to convert those late-bound types to early-bound types.

For example, you can do the following when you know the `Target` parameter represents an account table. In this example, "Account" is an early-bound type.

```csharp
Account acct = context.InputParameters["Target"].ToEntity<Account>();
```

But you should never try to set the value using an early-bound type. Doing so causes an <xref:System.Runtime.Serialization.SerializationException> to occur.

```csharp
context.InputParameters["Target"] = new Account() { Name = "MyAccount" }; // WRONG: Do not do this. 
```

## Building the plug-in assembly

When building a plug-in project, keep the following output assembly constraints in mind.

### Use .NET Framework 4.6.2

Plug-in and custom workflow activity assembly projects must target .NET Framework 4.6.2. While assemblies built using later versions of the Framework should generally work, if the plug-in code uses any features introduced after 4.6.2, an error will occur.

### Optimize assembly development

The assembly may include multiple plug-in classes (or types), but can be no larger than 16 MB in size. It's recommended to consolidate plug-ins and workflow assemblies into a single assembly as long as the size remains below 16 MB.

Best practice information: [Optimize assembly development](/dynamics365/customer-engagement/guidance/server/optimize-assembly-development)

### Assemblies must be signed

All assemblies must be signed before they can be registered. You can use the Visual Studio **Signing** tab on the project or by using [Sn.exe (Strong Name Tool)](/dotnet/framework/tools/sn-exe-strong-name-tool).

### Don't depend on .NET assemblies that interact with low-level Windows APIs

Plug-in assemblies must contain all the necessary logic within the respective DLL. Plug-ins may reference some core .NET assemblies. However, we don't support dependencies on .NET assemblies that interact with low-level Windows APIs, such as the graphics design interface.

### Dependency on any other (non-Dataverse) assemblies

Adding the `Microsoft.CrmSdk.CoreAssemblies` NuGet package to your project includes the necessary Dataverse assembly references in your project, but it doesn't upload these assemblies along with your plug-in assembly as these Dataverse assemblies already exist in the server's sandbox run-time.

#### Don't depend on System.Text.Json

Because the [Microsoft.CrmSdk.CoreAssemblies NuGet package has a dependency on System.Text.Json](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies#dependencies-body-tab), you're able to refer to [System.Text.Json](xref:System.Text.Json) types at design time. However, the System.Text.Json.dll file in the sandbox run-time can't be guaranteed to be the same version that you reference in your project. If you need to use `System.Text.Json`, you should use the dependent assembly feature and explicitly include it in your NuGet package.

The dependent assembly capability, currently in a Preview release, can be used to include other .NET compiled assemblies with your plug-in assembly in a single package to upload.

More information: [Dependent Assembly plug-ins](dependent-assembly-plugins.md).

> [!IMPORTANT]
> The dependent assembly capability is so important to plug-in development that you should consider using it from the start even if you do not have an immediate need to do so. Adding support for dependent assemblies to your plug-in project is much more difficult later on in the development cycle.
>
> Since this feature is a Preview release, do not use this feature for production work.

## Next steps

[Register a plug-in](register-plug-in.md)<br />
[Debug Plug-ins](debug-plug-in.md)

### See also

[Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)  
[Handle exceptions](handle-exceptions.md)  
[Best practices and guidance regarding plug-in and workflow development](best-practices/business-logic/index.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
