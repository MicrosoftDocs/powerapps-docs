---
title: "Write a plug-in (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to write custom code to be executed in response to data processing events."
ms.date: 03/26/2024
ms.reviewer: pehecke
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - phecke
  - JimDaly
---

# Write a plug-in

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can create [plug-ins](plug-ins.md) by using one of the following methods:

- Power Platform development tools provide a modern way to create plug-ins. The tools being referred to here are *Power Platform Tools for Visual Studio* and *Power Platform CLI*. Both these Power Platform tools generate similar plug-in code so moving from one tooling method to the other is fairly easy and understandable.

  - Use [Power Platform Tools for Visual Studio](tools/devtools-install.md) to quickly create template plug-in code and register (deploy) a plug-in. A [quickstart](tools/devtools-create-plugin.md) article is available to show you how. Use this tool if you like to work in Visual Studio.

  - Use [Power Platform CLI](/power-platform/developer/cli/introduction) to create a basic (Visual Studio compatible) plug-in project with template plug-in code using a single [pac plugin](/power-platform/developer/cli/reference/plugin) command. Afterwards, using the [pac tool prt](/power-platform/developer/cli/reference/tool#pac-tool-prt) command, you interactively use the Plug-in Registration tool to register your creation with Microsoft Dataverse. Use this CLI tool set if you like working in a terminal window or Visual Studio Code.

- Manually write code using Visual Studio or your favorite editor. This article focuses on writing code using Dataverse APIs, however the concepts introduced also apply to plug-in development using our tools mentioned previously.

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
> When using the Power Platform Tools extension or the Power Platform CLI for plug-in creation, the generated `PluginBase` class implements the `IPlugin` interface.

There are some exceptions to the statement about adding properties or methods in the note above. For example, you can have a property that represents a constant and you can have methods that are called from the `Execute` method. The important thing is that you never store any service instance or context data as a property in your class. These values change with every invocation and you don't want that data to be cached and applied to subsequent invocations.

More information: [Develop IPlugin implementations as stateless](best-practices/business-logic/develop-iplugin-implementations-stateless.md)

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

## PluginBase abstract class

The `PluginBase` class implements the `IPlugin` interface. We offer this class as it implements a robust programming pattern that has proven itself in commercial solutions. However, use of this class in your plug-in code is optional but recommended.

The class is not available in any SDK assembly, rather you must generate the class using one of our tools. To generate the class, create a plug-in project in the Power Platform Tools extension for Visual Studio or execute the Power Platform CLI command `pac plugin init`. You will find a PluginBase.cs file in the generated project.

More information: [pac plugin](/power-platform/developer/cli/reference/plugin), [Quickstart: Create a plug-in using Power Platform Tools](/power-apps/developer/data-platform/tools/devtools-create-plugin)

> [!IMPORTANT]
> The `PluginBase` class generated by the Power Platform Tools extension and the Power Platform CLI have slightly different class member signatures. It is best to choose one or the other and stick with it in all your plug-in code development. Both versions of the class have the same functionality and perform similarly.

This class diagram provides a visual on the key interfaces and classes related to `PluginBase`.

:::image type="content" source="media/plugin-base-class-diagram.png" alt-text="PluginBase class and other related types." lightbox="media/plugin-base-class-diagram.png":::

The example `Plugin1` class (in the diagram) derives from `PluginBase`. You would rename this `Plugin1` class to your own custom name and add code to implement the `ExecuteDataversePlugin` method and class constructor. The `LocalPluginContext` class is automatically initialized with the indicated service references and endpoints available to your plug-in. If you were implementing the `IPlugin` interface, you would have to write code to initialize all these services and endpoints prior to using them.

## Services you can use in your code

Typically, within your plug-in you will:

- Access the contextual data passed to your plug-in to determine information about the entity and message request that caused the event and invoked your plug-in. This data is called the *execution context*.
- Access the Organization web service using SDK for .NET calls to perform message request operations like query, create, update, delete, and more.
- Write messages to the Tracing service so you can evaluate how your plug-in code is executing.

> [!NOTE]
> All Dataverse services your plug-in would typically use and the plug-in execution context are pre-configured and available to your plug-in code when you derive your plug-in from the `PluginBase` class.

The <xref:System.IServiceProvider>.<xref:System.IServiceProvider.GetService%2A> method provides you with a way to access service references passed in the execution context when needed. To get an instance of a service, you invoke the `GetService` method passing the type of service. Read more about this method in the next sections.

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

> [!IMPORTANT]
> You must first enable trace logging in your environment before you are able to write to or view the logs. More information: [Tracing and logging](logging-tracing.md#enable-trace-logging)

To write to the Tracelog, you need to get an instance of the Tracing service. The following code shows how to get an instance of the Tracing service using the <xref:System.IServiceProvider>.<xref:System.IServiceProvider.GetService*> method.

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

When you write a plug-in that uses Azure Service Bus integration, use the notification service that implements the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService> interface, but this interface won't be described here.

More information: [Azure Integration](azure-integration.md)

## Putting it all together

Applying the plug-in concepts detailed previously results in plug-in code that looks like the following.

# [PluginBase example](#tab/pluginbase)

```csharp
public class MyPlugin : PluginBase
{
  // Constructor
  public MyPlugin(string unsecureConfiguration, string secureConfiguration)
       : base(typeof(MyPlugin))
  { }

  protected override void ExecuteDataversePlugin(ILocalPluginContext localPluginContext)
  {
    if (localPluginContext == null)
    {
      throw new ArgumentNullException(nameof(localPluginContext));
    }

    var context        = localPluginContext.PluginExecutionContext;
    var serviceFactory = localPluginContext.OrgSvcFactory;
    var tracingService = localPluginContext.TracingService;

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
}
```

# [IPlugin example](#tab/iplugin)

```csharp
public class MyPlugin : IPlugin
{
  public MyPlugin() {} // Constructor, does nothing

  public void Execute(IServiceProvider serviceProvider)
  {
    // Obtain the execution context
    IPluginExecutionContext context = (IPluginExecutionContext)
      serviceProvider.GetService(typeof(IPluginExecutionContext));

    // Obtain the IOrganizationService instance 
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

---

You can review these two methods of plug-in implementations in our [FollowupPlugin](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/FollowupPlugin) code sample. For more information about handling exceptions in plug-ins see [Handle exceptions in plug-ins](handle-exceptions.md).

## Plug-in design impacts performance

When writing your plug-in, it's critical that it must execute efficiently and quickly. However long your plug-in takes to execute causes the end user that invoked the message operation (which triggered your plug-in) to wait. In addition to processing the message operation, Dataverse executes all registered synchronous plug-ins in the pipeline including your plug-in. When plug-ins take too long to execute, or if too many plug-ins are registered in a pipeline, this performance impact can result in a nonresponsive application UI or worst case a timeout error with pipeline rollback.

> [!IMPORTANT]
> Plug-ins must adhere to an execution time limit and resource constraints.
> More information: [Analyze plug-in performance](analyze-performance.md)

## Using early-bound types in plug-in code

You can optionally use [early-bound](org-service/early-bound-programming.md) types within plug-in code. Include the generated types file in your plug-in project. All table types provided in the execution context's <xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> collection are late-bound types. You would need to convert those late-bound types to early-bound types.

For example, you can do the following when you know the `Target` parameter represents an account table. In this example, "Account" is an early-bound type.

```csharp
Account acct = context.InputParameters["Target"].ToEntity<Account>();
```

But you should never try to set the value using an early-bound type. Doing so causes an <xref:System.Runtime.Serialization.SerializationException> to occur.

```csharp
context.InputParameters["Target"] = new Account() { Name = "MyAccount" }; // WRONG: Do not do this. 
```

### See also

[Handle exceptions](handle-exceptions.md)  
[Register a plug-in](register-plug-in.md)  
[Debug Plug-ins](debug-plug-in.md)  
[Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)  
[Best practices and guidance regarding plug-in and workflow development](best-practices/business-logic/index.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
