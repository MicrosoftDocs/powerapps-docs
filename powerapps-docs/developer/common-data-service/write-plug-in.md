---
title: "Write a plug-in (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the concepts and technical details necessary when writing plug-ins" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Write a plug-in

<!-- This should be the how-to topic supporting the new tutorials

• Tutorial: Write a plug-in
• Tutorial: Debug a plug-in
• Tutorial: Update a plug-in

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/write-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/register-deploy-plugins

See Plug-in Tutorials written up at https://microsoft-my.sharepoint.com/:w:/p/jdaly/EZ1SzmOh-B5Bnt4C9rxGWysB6NtUQonOxq5sGSPkn5vNAA?e=wuehTb 

Plug-ins and workflow activities are both 'plug-ins'
Yet, I think workflow activities are easier to understand as 'workflow extensions' - because that is what they do... 

-->

The process of writing a plug-in is:

1. Create a .NET Framework Class library project in Visual Studio
1. Add the `Microsoft.CrmSdk.CoreAssemblies` NuGet package to the project
1. Implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface on classes that will be registered as steps.
1. Add your code to the <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method required by the interface
    1. Get references to services you need
    1. Add your business logic
1. Sign & build the assembly
1. Test the assembly
    1. Register the assembly in a test environment
    1. Test the behavior of the assembly
    1. Verify expected trace logs are written
    1. Debug the assembly as needed

Content in this topic supports the following tutorials:

- [Tutorial: Write a plug-in](tutorial-write-plug-in.md)
- [Tutorial: Debug a plug-in](tutorial-debug-plug-in.md)
- [Tutorial: Update a plug-in](tutorial-update-plug-in.md)

## Assembly constraints

When creating assemblies keep the following constraints in mind.

### Optimize assembly development

The assembly should include multiple types, but can be no larger than 16 MB. It is recommended to consolidate plug-ins and workflow assemblies into a single assembly as long as the size remains below 16 MB. More information: [Optimize assembly development](/dynamics365/customer-engagement/guidance/server/optimize-assembly-development)

### Assemblies must be signed
All assemblies must be signed before they can be registered. This can be done using Visual Studio Signing tab on the project or by using [Sn.exe (Strong Name Tool)](/dotnet/framework/tools/sn-exe-strong-name-tool).

### Do not depend on .NET assemblies that interact with low-level Windows APIs

Plug-in assemblies must contain all the necessary logic within the respective dll.  Plugins may reference some core .Net assemblies. However, we do not support dependencies on .Net assemblies that interact with low-level Windows APIs, such as the graphics design interface.


## IPlugin interface

A plug-in is a class within an assembly created using a .NET Framework Class library project using .NET Framework 4.5.2 in Visual Studio. Each class in the project that will be registered as a step must implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface which requires the <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method.

> [!IMPORTANT]
> When implementing `IPlugin`, the class should be *stateless*. This is because the platform caches a class instance and re-uses it for performance reasons. A simple way of thinking about this is that you shouldn't add any properties or methods to the class and everything should be included within the `Execute` method. There are some exceptions to this. For example you can have a property that represents a constant and you can have methods that represent functions that are called from the `Execute` method. The important thing is that you never store any service instance or context data as a property in your class. These change with every invocation and you don't want that data to be cached and applied to subsequent invocations.  More information: [Develop IPlugin implementations as stateless](/dynamics365/customer-engagement/guidance/server/develop-iplugin-implementations-stateless)

The <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method accepts a single <xref:System.IServiceProvider> parameter. The `IServiceProvider` has a single method:  <xref:System.IServiceProvider.GetService*>. You will use this method to get several different types of services that you can use in your code.



## Services you can use in your code

Within your plug-in you will need to:
 
- Access the contextual information about what is happening in the event your plug-in was registered to handle. This is called the *execution context*.
- Access the Organization web service so you can write code to query data, work with entity records, use messages to perform operations.
- Write messages to the Tracing service so you can evaluate how your code is executing.

The <xref:System.IServiceProvider>.<xref:System.IServiceProvider.GetService*> method provides you with a way to access these services as needed. To get an instance of the service you invoke the `GetService` method passing the type of service.

> [!NOTE]
> When you write a plug-in that uses Azure Service Bus integration, you will use a notification service that implements the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService> interface, but this will not be described here. More information: [Azure Integration](azure-integration.md)

## Execution Context

You can get a variable that implements the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> interface using the following code:

```csharp
// Obtain the execution context from the service provider.  
IPluginExecutionContext context = (IPluginExecutionContext)
    serviceProvider.GetService(typeof(IPluginExecutionContext));
```

This <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> provides some information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.Stage> that the plugin is registered for as well as information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.ParentContext> which provides information about any operation within another plug-in that triggered the current operation.

But the rest of the information available is provided by the <xref:Microsoft.Xrm.Sdk.IExecutionContext> interface that this class implements. All the properties of this class provide useful information you may need to access in your code, but two of the most important are the 
<xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> and <xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters> properties. 

Other frequently used properties are <xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables>, <xref:Microsoft.Xrm.Sdk.IExecutionContext.PreEntityImages>, and <xref:Microsoft.Xrm.Sdk.IExecutionContext.PostEntityImages>.

> [!TIP]
> A good way to visualize the data that is passed into the execution context is to install the plug-in profiler solution that is available as part of the plug-in registration tool. The profiler will capture the context information as well as information that allows for replaying event locally so you can debug. Within the plugin registration tool, you can download an xml document with all the data from the event that triggered the workflow. More information: [View Plug-in Profile data](debug-plug-in.md#view-plug-in-profile-data)

### Work with ParameterCollections

All the properties of the execution context are read-only. But the `InputParameters`, `OutputParameters`, and `SharedVariables` are <xref:Microsoft.Xrm.Sdk.ParameterCollection> values. You can manipulate the values of the items in these collections to change the behavior of the operation, depending on the stage in the event execution pipeline your plug-in is registered for.

The <xref:Microsoft.Xrm.Sdk.ParameterCollection> values are defined as <xref:System.Collections.Generic.KeyValuePair%602> structures. In order to access a property you will need to know the name of the property that is exposed by the message. For example, to access the <xref:Microsoft.Xrm.Sdk.Entity> property that is passed as part of the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>, you need to know that the name of that property is `Target`. Then you can access this value using code like this:

```csharp
var entity = (Entity)context.InputParameters["Target"];
```
Use the <xref:Microsoft.Xrm.Sdk.Messages> and <xref:Microsoft.Crm.Sdk.Messages> documentation to learn the names of the messages defined in the SDK assemblies. For custom actions, refer to the names of the parameters defined in the system.

### InputParameters

The `InputParameters` represent the value of the <xref:Microsoft.Xrm.Sdk.OrganizationRequest>.<xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> property that represents the operation coming in from the web services.

As described in [Use messages with the Organization service](org-service/use-messages.md), all operations that occur in the system are ultimately instances of the `OrganizationRequest` class being processed by the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

As described in [Event Framework](event-framework.md), operations go through a series of stages and you can register your plug-in on stages that occur before the data is written to the database. Within the **PreValidation** and **PreOperation** stages, you can read and change the values of the `InputParameters` so that you can control the expected outcome of the data operation.

If you find that the values in the `InputParameters` collection represent a condition that you cannot allow, you can throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> (preferably in the **PreValidation** stage) that will cancel the operation and display an error to the user with a synchronous plug-in, or log the error if the plug-in is asynchronous.

### OutputParameters

The `OutputParameters` represent the value of the <xref:Microsoft.Xrm.Sdk.OrganizationResponse>.<xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results> property that represents the return value of the operation. The `OutputParameters` are not populated until after the database transaction, so they are only available for plug-ins registered in the **PostOperation** stage. If you want to change the values returned by the operation, you can modify them within the `OutputParameters`.

### Shared variables

The <xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables> property allows for including data that can be passed from a plug-in to a step that occurs later in the execution pipeline. Because this is a <xref:Microsoft.Xrm.Sdk.ParameterCollection> value, plug-ins can add, read, or modify properties to share data with subsequent steps

### Entity Images

When you register a step for a plug-in that includes an entity as one of the parameters, you have the option to specify that a copy of the entity data be included as *snapshot* or image using the <xref:Microsoft.Xrm.Sdk.IExecutionContext.PreEntityImages> and/or <xref:Microsoft.Xrm.Sdk.IExecutionContext.PostEntityImages> properties.

This data provides a comparison point for entity data as it flows through the event pipeline. Using these images provides much better performance than including code in a plug-in to retrieve an entity just to compare the attribute values

## Organization Service

To work with data within a plug-in you use the organization service. Do not try to use the Web API. Plug-ins are optimized to use the .NET SDK assemblies.

To gain access to a `svc` variable that implements the <xref:Microsoft.Xrm.Sdk.IOrganizationInterface> interface, use the following code:


```csharp
// Obtain the organization service reference which you will need for  
// web service calls.  
IOrganizationServiceFactory serviceFactory =
    (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
IOrganizationService svc = serviceFactory.CreateOrganizationService(context.UserId);
```
The `context.UserId` variable used with <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> comes from execution context the <xref:Microsoft.Xrm.Sdk.IExecutionContext.UserId> property, so this is call is done after the execution context has been accessed.

You can use early bound types within a plug-in. Just include the generated types file in your project. But you should be aware that all entity types that are provided by the execution context input parameters will be late-bound types. You will need to convert them to early bound types. For example you can do the following when you know the `Target` parameter represents an account entity.

```csharp
Account acct = context.InputParameters["Target"].ToEntity<Account>();
``` 
But you should never try to set the value using an early bound type. Don't try to do this:

```csharp
context.InputParameters["Target"] = new Account() { Name = "MyAccount" }; // WRONG: Do not do this. 
```
This will cause an <xref:System.Runtime.Serialization.SerializationException> to occur.



## Tracing service

## Passing Configuration values to a plug-in

## Next steps
[Register a plug-in](register-plug-in.md#register-a-plug-in)<br />
[Debug Plug-ins](debug-plug-in.md#debug-plug-ins)


### See also
[Write plug-ins to extend business processes](plug-ins.md)<br />
[Tutorial: Write a plug-in](tutorial-write-plug-in.md)<br />
[Tutorial: Debug a plug-in](tutorial-debug-plug-in.md)<br />
[Tutorial: Update a plug-in](tutorial-update-plug-in.md)<br />
