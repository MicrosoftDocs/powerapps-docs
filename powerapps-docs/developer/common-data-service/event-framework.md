---
title: " Event Framework (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes the event framework and information developers should know when working with it." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Event Framework

<!-- Re-write from
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/introduction-event-framework
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/event-execution-pipeline

See notes at https://microsoft-my.sharepoint.com/:w:/p/jdaly/EfmTW7DQXNREuqj1s7tBtIIB4VZmvasZ1Nsbl4F5zlD1ZQ?e=FNlBmr 


Make sure to call out the changes due to the legacy update messages. That information was moved.

See 
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/perform-specialized-operations-using-update#impact-of-this-change-on-plug-ins

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/perform-specialized-operations-using-update#impact-of-this-change-on-workflows


-->

The capability to extend the default behavior of Common Data Service for apps depends on detecting when events occur on the server. The *Event Framework* provides the capability to register custom code to be run in response to specific events. 

All capabilities to extend the default behavior of the platform depend on the event framework. When you configure a workflow to respond to an event using the workflow designer without writing code, that event is provided by the event framework. 

As a developer, you will use the *Plug-in registration tool* to configure plug-ins, Azure integrations, virtual entity data providers, and Web Hooks to respond to events that are provided by the event framework. When events occur and an extension is registered to respond to them, contextual information about the data involved in the operation is passed to the extension. Depending on how the registration for the event is configured, the extension can modify the data passed into it, intiate some automated process to be applied immediately, or define that an action is added to a queue to be be performed later.

To leverage the event framework for your custom extensions you must understand:

 - What events are available
 - How the event is processed
 - What kind of data is available to your extension when the event occurs
 - What time and resource constraints apply
 - How to monitor performance

## Available events

As described in [Use messages with the Organization service](org-service/use-messages.md), data operations in the CDS for Apps platform are based on messages and every message has a name. There are `Create`, `Retrieve`, `RetrieveMultiple`, `Update`, `Delete`, `Associate` and `Disassociate` messages that cover the basic data operations that happen with entities. There are also specialized messages for more complex operations. Custom actions add new messages.

When you use the Plug-in registration tool to associate an extension with a particular message, you will register it as a *step*. The screenshot below is the **Register New Step** dialog used when registering a plug-in.

![Dialog to register a step](media/register-new-step-plug-in.png)

A step provides the information about which message the extensions should respond to as well as a number of other configuration choices. Use the **Message** field to choose the message your extension will respond to.

Generally, you can expect to find a message for most of the **Request* classes in the <xref:Microsoft.Crm.Sdk.Messages> or <xref:Microsoft.Xrm.Sdk.Messages> namespaces, but you will also find messages for any custom actions that have been created in the organization. Any operations involving entity metadata are not available.

Data about messages is stored in the [SdkMessage](reference/entities/sdkmessage.md) and [SdkMessageFilter](reference/entities/sdkmessagefilter.md) entities. The Plug-in registration tool will filter this information to only show valid messages.

> [!CAUTION]
> The `Execute` message is available, but you should typically not register extensions for it since it is called by every operation.

> [!NOTE]
> There are certain cases where plug-ins and workflows that are registed for the Update event can be called twice. More information: [Behavior of specialized update operations](special-update-operation-behavior.md)

## Event execution pipeline

When you register a step using the Plug-in registration tool you must also choose the **Event Pipeline Stage of Execution**.  Each message is processed in a series of 4 stages as described in the following table:

|Name|Description|
|--|--|
|**PreValidation**<br />Stage: 10|[!INCLUDE [cc-prevalidation-description](../../includes/cc-prevalidation-description.md)]|
|**PreOperation**<br />Stage: 20|[!INCLUDE [cc-preoperation-description](../../includes/cc-preoperation-description.md)]|
|**MainOperation**<br />Stage: 30|For internal use only.|
|**PostOperation**<br />Stage: 40|[!INCLUDE [cc-postoperation-description](../../includes/cc-postoperation-description.md)]|

The stage you should choose depends on the purpose of the extension. You don't need to apply all your business logic within a single step. You can apply multiple steps so that your logic about whether to allow a operation to proceed can be in the **PreValidation** stage and your logic to make modifications to the message properties can occur in the **PostOperation** stage.

> [!IMPORTANT]
> An exception thrown by your code at any stage will cause the entire transaction to be rolled back. You should be careful to ensure that any possible exception cases are handled by your code. If you want to cancel the operation, you should detect this in the **PreValidation** stage and only throw a <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> containing an appropriate message describing why the operation was cancelled.

Multiple extensions can be registered for the same message and stage. Within the step registration the **Execution Order** value determines the order in which multiple extensions should be processed for a given stage.

Information about registered steps is stored in the [SdkMessageProcessingStep Entity](reference/entities/sdkmessageprocessingstep.md).

## Event context

If your extension is a Plug-in, it will recieve a parameter that implements the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> interface. This class provides some information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.Stage> that the plugin is registered for as well as information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.ParentContext> which provides information about any operation within another Plug-in that triggered the current operation.

If your extension is an a Web hook or an Azure Service bus endpoint, the data that will be posted to the registered endpoint will be in form of a <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext> which implements both <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> and <xref:Microsoft.Xrm.Sdk.IExecutionContext>

### Information about the operation

The properties of the <xref:Microsoft.Xrm.Sdk.IExecutionContext> interface are the ones which provide most of the details about the operation that occurred.

Two of the key properties about the event are found in the <xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> and <xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters> properties. These <xref:Microsoft.Xrm.Sdk.ParameterCollection> values contain the data of the operation.

All the properties of the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> are read-only, but your extension can modify the contents of properties that are collections.

In the **PreValidation** and **PreOperation** stages, the <xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> property contains the parameters for the  <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class.

In the **PostOperation** stage the <xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters> contain the parameters for the <xref:Microsoft.Xrm.Sdk.OrganizationResponse> class that will be returned by the operation.

### Shared variables

The <xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables> property allows for including data that can be passed from a plug-in to a step that occurrs later in the execution pipeline. Because this is a <xref:Microsoft.Xrm.Sdk.ParameterCollection> value, plug-ins can add, read, or modifiy properties to share data with subsequent steps

### Entity Images

When you register a step for a plug-in that includes an entity as one of the parameters, you have the option to specify that a copy of the entity data be included as *snapshot* or image using the <xref:Microsoft.Xrm.Sdk.IExecutionContext.PreEntityImages> and/or <xref:Microsoft.Xrm.Sdk.IExecutionContext.PostEntityImages> properties.

This data provides a comparison point for entity data as it flows through the event pipeline. Using these images provides much better performance than including code in a plug-in to retrieve an entity just to compare the attribute values



