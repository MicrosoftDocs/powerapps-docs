---
title: "Understand the execution context (Common Data Service for Apps) | Microsoft Docs" 
description: "Learn about the data that is passed to your plug-ins when it is executed." 
ms.custom: ""
ms.date: 1/23/2019
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: phecke
ms.author: pehecke
manager: kvivek
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Understand the execution context

The **Event Execution Pipeline** passes registered plug-ins a wealth of data about the current operation being processed and the plug-in's execution environment. You can access this data in your plug-in code by setting a variable that implements the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> interface:

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

## ParameterCollections

All the properties of the execution context are read-only. But the `InputParameters`, `OutputParameters`, and `SharedVariables` are <xref:Microsoft.Xrm.Sdk.ParameterCollection> values. You can manipulate the values of the items in these collections to change the behavior of the operation, depending on the stage in the event execution pipeline your plug-in is registered for.

The <xref:Microsoft.Xrm.Sdk.ParameterCollection> values are defined as <xref:System.Collections.Generic.KeyValuePair%602> structures. In order to access a property you will need to know the name of the property that is exposed by the message. For example, to access the <xref:Microsoft.Xrm.Sdk.Entity> property that is passed as part of the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>, you need to know that the name of that property is `Target`. Then you can access this value using code like this:

```csharp
var entity = (Entity)context.InputParameters["Target"];
```
Use the <xref:Microsoft.Xrm.Sdk.Messages> and <xref:Microsoft.Crm.Sdk.Messages> documentation to learn the names of the messages defined in the SDK assemblies. For custom actions, refer to the names of the parameters defined in the system.

## InputParameters

The `InputParameters` represent the value of the <xref:Microsoft.Xrm.Sdk.OrganizationRequest>.<xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters> property that represents the operation coming in from the web services.

As described in [Use messages with the Organization service](org-service/use-messages.md), all operations that occur in the system are ultimately instances of the `OrganizationRequest` class being processed by the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

As described in [Event Framework](event-framework.md), operations go through a series of stages and you can register your plug-in on stages that occur before the data is written to the database. Within the **PreValidation** and **PreOperation** stages, you can read and change the values of the `InputParameters` so that you can control the expected outcome of the data operation.

If you find that the values in the `InputParameters` collection represent a condition that you cannot allow, you can throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> (preferably in the **PreValidation** stage) that will cancel the operation and display an error to the user with a synchronous plug-in, or log the error if the plug-in is asynchronous. More information: [Cancelling an operation](#cancelling-an-operation)

## OutputParameters

The `OutputParameters` represent the value of the <xref:Microsoft.Xrm.Sdk.OrganizationResponse>.<xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results> property that represents the return value of the operation. The `OutputParameters` are not populated until after the database transaction, so they are only available for plug-ins registered in the **PostOperation** stage. If you want to change the values returned by the operation, you can modify them within the `OutputParameters`.

## Shared variables

The <xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables> property allows for including data that can be passed from a plug-in to a step that occurs later in the execution pipeline. Because this is a <xref:Microsoft.Xrm.Sdk.ParameterCollection> value, plug-ins can add, read, or modify properties to share data with subsequent steps.

The following example shows how a `PrimaryContact` value can be passed from a plug-in registered for a **PreOperation** step to a **PostOperation** step.

```csharp
public class PreOperation : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        // Obtain the execution context from the service provider.
        Microsoft.Xrm.Sdk.IPluginExecutionContext context = (Microsoft.Xrm.Sdk.IPluginExecutionContext)
            serviceProvider.GetService(typeof(Microsoft.Xrm.Sdk.IPluginExecutionContext));

        // Create or retrieve some data that will be needed by the post event
        // plug-in. You could run a query, create an entity, or perform a calculation.
        //In this sample, the data to be passed to the post plug-in is
        // represented by a GUID.
        Guid contact = new Guid("{74882D5C-381A-4863-A5B9-B8604615C2D0}");

        // Pass the data to the post event plug-in in an execution context shared
        // variable named PrimaryContact.
        context.SharedVariables.Add("PrimaryContact", (Object)contact.ToString());
    }
}

public class PostOperation : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        // Obtain the execution context from the service provider.
        Microsoft.Xrm.Sdk.IPluginExecutionContext context = (Microsoft.Xrm.Sdk.IPluginExecutionContext)
            serviceProvider.GetService(typeof(Microsoft.Xrm.Sdk.IPluginExecutionContext));

        // Obtain the contact from the execution context shared variables.
        if (context.SharedVariables.Contains("PrimaryContact"))
        {
            Guid contact =
                new Guid((string)context.SharedVariables["PrimaryContact"]);

            // Do something with the contact.
        }
    }
}
```


## Entity Images

When you register a step for a plug-in that includes an entity as one of the parameters, you have the option to specify that a copy of the entity data be included as *snapshot* or image using the <xref:Microsoft.Xrm.Sdk.IExecutionContext.PreEntityImages> and/or <xref:Microsoft.Xrm.Sdk.IExecutionContext.PostEntityImages> properties.

This data provides a comparison point for entity data as it flows through the event pipeline. Using these images provides much better performance than including code in a plug-in to retrieve an entity just to compare the attribute values.

When you define an entity image, you specify an entity alias value you can use to access the specific image. For example, if you define a pre entity image with the alias '`a`', you can use the following code to access the `name` attribute value.

```csharp
var oldAccountName = (string)context.PreEntityImages["a"]["name"];
```

More information: [Define entity images](register-plug-in.md#define-entity-images)

### See also

[Event Framework](event-framework.md)  
[Write a plug-in](write-plug-in.md)