---
title: "Write a plug-in (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to write custom code to be executed in response to specific Dataverse data processing events." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/15/2023
ms.reviewer: "pehecke"
ms.topic: "article"
author: "divkamath" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "dikamath" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - phecke
---

# Write a plug-in

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

In the past, plug-ins were created by manually writing code using your favorite editor or IDE. Today you can still write plug-ins that way, but the easier and more modern method is to use one of the available Power Platform development tools. The tools being referred to here are *Power Platform Tools for Visual Studio*, and *Power Platform CLI*. Both these Power Platform tool sets generate similar plug-in code so moving from one tooling method to the other is fairly easy and understandable.

| Plug-in coding methods |
| --- | --- | --- |
| Manually write code | Use Power Platform Tools for Visual Studio | Use Power Platform CLI |

You can use Power Platform Tools for Visual Studio to quickly create and register (deploy) plug-ins. A [Quickstart](tools/devtools-create-plugin.md) article is available to show you how. Use this tool if you like to work in Visual Studio.

The Power Platform CLI can create a basic (Visual Studio compatible) plug-in project with template plug-in code using a single [pac plugin](/power-platform/developer/cli/reference/plugin) command. Afterwards, using the [pac tool prt](/power-platform/developer/cli/reference/tool#pac-tool-prt) command, you interactively use the Plug-in Registration tool to register your creation with Microsoft Dataverse. Use this CLI tool set if you like working in a terminal window or Visual Studio Code.

The rest of the plug-in documentation in this topic and the other related topics is written with the developer writing code in mind, however the concepts introduced apply to all methods of plug-in development.

## IPlugin interface

A plug-in is a compiled class within an assembly created using a .NET Framework 4.6.2 Class library project. Each class in the project that will be registered on a pipeline step must implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface which requires implementation of the <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method.

> [!IMPORTANT]
> When deriving from `IPlugin`, the class should be *stateless*. This is because the platform caches a class instance and re-uses it for performance reasons. A simple way of thinking about this is that you shouldn't add any properties or methods to the class and everything should be included within the `Execute` method. There are some exceptions to this. For example you can have a property that represents a constant and you can have methods that represent functions that are called from the `Execute` method. The important thing is that you never store any service instance or context data as a property in your class. These change with every invocation and you don't want that data to be cached and applied to subsequent invocations.  More information: [Develop IPlugin implementations as stateless](/dynamics365/customer-engagement/guidance/server/develop-iplugin-implementations-stateless)

The <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method accepts a single <xref:System.IServiceProvider> parameter. The `IServiceProvider` has a single method:  <xref:System.IServiceProvider.GetService*>. You will use this method to get several different types of services that you can use in your code. More information: [Services you can use in your code](#services-you-can-use-in-your-code)

### Pass configuration data to your plug-in

When you register a plug-in you have the ability to pass configuration data to it. Configuration data allows you to define how a specific instance of a registered plug-in should behave. This information is passed as string data to parameters in the constructor of your class. There are two parameters: `unsecure` and `secure`.
Use the first `unsecure` parameter for data that you don't mind if people can see. Use the second `secure` parameter for sensitive data.

The following code shows the three possible signatures for a plug-in class named `SamplePlugin`.

```csharp
public SamplePlugin()  
public SamplePlugin(string unsecure)  
public SamplePlugin(string unsecure, string secure)
```

The secure configuration data is stored in a separate table which only system administrators have privileges to read. More information: [Register plug-in step > Set configuration data](register-plug-in.md#set-configuration-data)

## Services you can use in your code

Within your plug-in you will need to:

- Access the contextual information about what is happening in the event your plug-in was registered to handle. This is called the *execution context*.
- Access the Organization web service so you can write code to query data, work with table records, use messages to perform operations.
- Write messages to the Tracing service so you can evaluate how your code is executing.

The <xref:System.IServiceProvider>.<xref:System.IServiceProvider.GetService*> method provides you with a way to access these services as needed. To get an instance of the service you invoke the `GetService` method passing the type of service.

> [!NOTE]
> When you write a plug-in that uses Azure Service Bus integration, you will use a notification service that implements the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService> interface, but this will not be described here. More information: [Azure Integration](azure-integration.md)

### Organization web service

To work with data within a plug-in you use the Organization service. Do not try to use the Web API. Plug-ins can only be written using the SDK API and compiled as .NET assemblies.

To obtain an object reference to the Organization service use the following code:


```csharp
// Obtain the Organization service reference  
IOrganizationServiceFactory serviceFactory =
    (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
IOrganizationService svc = serviceFactory.CreateOrganizationService(context.UserId);
```

The `context.UserId` variable used with <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> comes from execution context the <xref:Microsoft.Xrm.Sdk.IExecutionContext.UserId> property, so this is call is done after the execution context has been accessed.

More information:

- [Table Operations](org-service/entity-operations.md)
- [Query data](org-service/entity-operations-query-data.md)
- [Create tables](org-service/entity-operations-create.md)
- [Retrieve a table](org-service/entity-operations-retrieve.md)
- [Update and Delete tables](org-service/entity-operations-update-delete.md)
- [Associate and disassociate tables](org-service/entity-operations-associate-disassociate.md)
- [Use messages](org-service/use-messages.md)
- [Late-bound and Early-bound programming](org-service/early-bound-programming.md)

You can use early bound types within a plug-in. Just include the generated types file in your project. But you should be aware that all table types that are provided by the execution context input parameters will be late-bound types. You will need to convert them to early bound types. For example you can do the following when you know the `Target` parameter represents an account table.

```csharp
Account acct = context.InputParameters["Target"].ToEntity<Account>();
```

But you should never try to set the value using an early-bound type. Don't try to do this:

```csharp
context.InputParameters["Target"] = new Account() { Name = "MyAccount" }; // WRONG: Do not do this. 
```

This will cause an <xref:System.Runtime.Serialization.SerializationException> to occur.

### Tracing service

Use the tracing service to write messages to the [PluginTraceLog Table](reference/entities/plugintracelog.md) so that you can review the logs to understand what occurred when the plug-in ran.

To write to the tracelog, you need to get an instance of the Tracing service. The following code shows how to get an instance of the Tracing service using the <xref:System.IServiceProvider>.<xref:System.IServiceProvider.GetService*> method.


```csharp
// Obtain the tracing service
ITracingService tracingService =
(ITracingService)serviceProvider.GetService(typeof(ITracingService));
```

To write to the trace, use the <xref:Microsoft.Xrm.Sdk.ITracingService>.<xref:Microsoft.Xrm.Sdk.ITracingService.Trace*> method.

```csharp
tracingService.Trace("Write {0} {1}.", "your", "message");
```

More information: [Use Tracing](debug-plug-in.md#use-tracing), [Logging and tracing](logging-tracing.md).

## Assembly constraints

When building a plug-in project, keep the following output assembly constraints in mind.

### Use .NET Framework 4.6.2

Plug-in and custom workflow activity assembly projects must target .NET Framework 4.6.2. While assemblies built using later versions of the Framework should generally work, if the plug-in code uses any features introduced after 4.6.2, an error will occur.

### Optimize assembly development

The assembly should include multiple plug-in classes (or types), but can be no larger than 16 MB. It is recommended to consolidate plug-ins and workflow assemblies into a single assembly as long as the size remains below 16 MB. More information: [Optimize assembly development](/dynamics365/customer-engagement/guidance/server/optimize-assembly-development)

### Assemblies must be signed

All assemblies must be signed before they can be registered. This can be done using Visual Studio Signing tab on the project or by using [Sn.exe (Strong Name Tool)](/dotnet/framework/tools/sn-exe-strong-name-tool).

### Do not depend on .NET assemblies that interact with low-level Windows APIs

Plug-in assemblies must contain all the necessary logic within the respective DLL.  Plug-ins may reference some core .NET assemblies. However, we do not support dependencies on .NET assemblies that interact with low-level Windows APIs, such as the graphics design interface.

### Dependency on any other (non-Dataverse) assemblies

Adding the `Microsoft.CrmSdk.CoreAssemblies` NuGet package to your project will include the necessary Dataverse assembly references in your project, but you will not upload these assemblies along with your plug-in assembly as these Dataverse assemblies already exist in the server's sandbox run-time.

In the past, non-Dataverse assemblies could not be included in your plug-in projects in a supported way. However, that has changed with the new dependent assembly (preview) capability. For more information see [Dependent Assembly plug-ins](dependent-assembly-plugins.md).

> [!IMPORTANT]
> The dependent assembly capability is so important to plug-in development that you should consider using it from the start even if you do not have an immediate need to do so. Adding support for dependent assemblies to your plug-in project is much more difficult later on in the development cycle.

## Performance considerations

When you add the business logic for your plug-in you need to be very aware of the impact they will have on overall performance.

> [!IMPORTANT]
> The business logic in plug-ins registered for synchronous steps should take no more than 2 seconds to complete.

### Time and resource constraints

There is a 2-minute time limit for message operations to complete. There are also limitations on the amount of CPU and memory resources that can be used by extensions. If the limits are exceeded an exception is thrown and the operation will be cancelled.

If the time limit is exceeded, an <xref:System.TimeoutException> will be thrown. If any custom extension exceeds threshold CPU, memory, or handle limits or is otherwise unresponsive, that process will be killed by the platform. At that point any current extension in that process will fail with exceptions. However, the next time that the extension is executed it will run normally.

### Monitor Performance

Run-time information about plug-ins and custom workflow extensions is captured and stored in the [PluginTypeStatistic Table](reference/entities/plugintypestatistic.md). These records are populated within 30 minutes to one hour after the custom code executes. This table provides the following data points:

|**Column**|**Description**|
|--|--|
|AverageExecuteTimeInMilliseconds|The average execution time (in milliseconds) for the plug-in type. |
|CrashContributionPercent|The plug-in type percentage contribution to crashes. |
|CrashCount|Number of times the plug-in type has crashed. |
|CrashPercent|Percentage of crashes for the plug-in type. |
|ExecuteCount|Number of times the plug-in type has been executed. |
|FailureCount |Number of times the plug-in type has failed. |
|FailurePercent|Percentage of failures for the plug-in type. |
|PluginTypeIdName|Unique identifier of the user who last modified the plug-in type statistic. |
|TerminateCpuContributionPercent |The plug-in type percentage contribution to Worker process termination due to excessive CPU usage. |
|TerminateHandlesContributionPercent |The plug-in type percentage contribution to Worker process termination due to excessive handle usage. |
|TerminateMemoryContributionPercent|The plug-in type percentage contribution to Worker process termination due to excessive memory usage. |
|TerminateOtherContributionPercent|The plug-in type percentage contribution to Worker process termination due to unknown reasons. |

This data is also available for you to browse using the [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/). Select **Analytics** > **Dataverse** > **Plug-ins**.

## Next steps

[Register a plug-in](register-plug-in.md)<br />
[Debug Plug-ins](debug-plug-in.md)

### See also

[Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)  
[Handle exceptions](handle-exceptions.md)  
[Best practices and guidance regarding plug-in and workflow development](best-practices/business-logic/index.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
