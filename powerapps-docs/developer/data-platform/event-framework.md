---
title: Event Framework in Microsoft Dataverse
description: Learn how the Dataverse event framework processes events. Register plug-ins, webhooks, and Azure integrations to extend default platform behavior.
author: MsSQLGirl
ms.author: jukoesma
ms.date: 03/09/2026
ms.reviewer: pehecke
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Event framework in Microsoft Dataverse

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The Microsoft Dataverse event framework enables you to detect when events occur on the server and run custom code in response. Use the event framework to extend default platform behavior by registering plug-ins, workflows, Azure integrations, and webhooks.

All capabilities to extend the default behavior of the platform depend on the event framework. When you configure a workflow to respond to an event by using the workflow designer without writing code, the event framework provides that event.

As a developer, use the *Plug-in Registration tool* to configure plug-ins, Azure integrations, virtual table data providers, and webhooks to respond to events that the event framework provides. When events occur and you register an extension to respond to them, the framework passes contextual information about the data involved in the operation to the extension. Depending on how you configure the registration for the event, the extension can modify the data passed into it, initiate some automated process to apply immediately, or define that an action is added to a queue to perform later.

To leverage the event framework for your custom extensions, you must understand:

- What events are available
- How the event is processed
- What kind of data is available to your custom extension when the event occurs
- What time and resource constraints apply
- How to monitor performance

## Available events

As described in [Use messages with the SDK for .NET](org-service/use-messages.md), the Dataverse platform bases data operations on messages, and every message has a name. The platform includes `Create`, `Retrieve`, `RetrieveMultiple`, `Update`, `Delete`, `Associate`, and `Disassociate` messages that cover the basic data operations that happen with tables. The platform also includes specialized messages for more complex operations, and custom actions add new messages.

When you use the Plug-in Registration tool to associate an extension with a particular message, you register it as a *step*. The following screenshot is the **Register New Step** dialog used when registering a plug-in.

:::image type="content" source="media/register-new-step-plug-in.png" alt-text="Screenshot of the Register New Step dialog in the Plug-in Registration tool showing message, entity, and pipeline stage fields.":::

A step provides the information about which message the extensions should respond to, as well as a number of other configuration choices. Use the **Message** field to choose the message your extension responds to.

Generally, you can expect to find a message for most of the **Request** classes in the <xref:Microsoft.Crm.Sdk.Messages> or <xref:Microsoft.Xrm.Sdk.Messages> namespaces. You also find messages for any custom actions that you create in the organization. The platform doesn't make available any operations that involve table definitions.

The system stores data about messages in the [SdkMessage](reference/entities/sdkmessage.md) and [SdkMessageFilter](reference/entities/sdkmessagefilter.md) tables. The Plug-in registration tool filters this information to only show valid messages.

To verify if a message and table combination supports execution of plug-ins by using a database query, use the following Web API query:

```
[Organization URI]/api/data/v9.2/sdkmessages?$select=name
&$filter=isprivate eq false 
and (name ne 'SetStateDynamicEntity' 
and name ne 'RemoveRelated' 
and name ne 'SetRelated' and 
name ne 'Execute') 
and sdkmessageid_sdkmessagefilter/any(s:s/iscustomprocessingstepallowed eq true 
and s/isvisible eq true)
&$expand=sdkmessageid_sdkmessagefilter($select=primaryobjecttypecode;
$filter=iscustomprocessingstepallowed eq true and isvisible eq true)
&$orderby=name
```

> [!TIP]
> You can export this data to an Excel worksheet by using this query and the instructions provided in this blog post: [Find Messages and tables eligible for plug-ins using the Dataverse](https://www.microsoft.com/power-platform/blog/power-apps/find-messages-and-entities-eligible-for-plug-ins-using-the-common-data-service).


You can also use the following FetchXML to retrieve this information. The [FetchXML Builder](https://fxb.xrmtoolbox.com) is a useful tool to execute this kind of query.

```xml
<fetch>
  <entity name='sdkmessage'>
    <attribute name='name' />
    <link-entity name='sdkmessagefilter'
      alias='filter'
      to='sdkmessageid'
      from='sdkmessageid'
      link-type='inner'>
      <filter type='and'>
        <condition attribute='iscustomprocessingstepallowed' 
          operator='eq' 
          value='1' />
        <condition attribute='isvisible' 
          operator='eq' 
          value='1' />
      </filter>
      <attribute name='primaryobjecttypecode' />
    </link-entity>
    <filter>
      <condition attribute='isprivate' 
        operator='eq' 
        value='0' />
      <condition attribute='name' 
        operator='not-in'>
        <value>SetStateDynamicEntity</value>
        <value>RemoveRelated</value>
        <value>SetRelated</value>
        <value>Execute</value>
      </condition>
    </filter>
    <order attribute='name' />
  </entity>
</fetch>
```

> [!CAUTION]
> The `Execute` message is available, but you shouldn't register extensions for it since every operation calls it.

> [!NOTE]
> In certain cases, the platform can call plug-ins and workflows that you register for the Update event twice. For more information, see [Behavior of specialized update operations](special-update-operation-behavior.md).

## Event execution pipeline

When you register a step by using the Plug-in Registration tool, you must also choose the **Event Pipeline Stage of Execution**. Each message is processed in a series of four stages as described in the following table:

|Name|Description|
|--|--|
|**PreValidation**|[!INCLUDE [cc-prevalidation-description](../../includes/cc-prevalidation-description.md)]|
|**PreOperation**|[!INCLUDE [cc-preoperation-description](../../includes/cc-preoperation-description.md)]|
|**MainOperation**|[!INCLUDE [cc-mainoperation-description](../../includes/cc-mainoperation-description.md)]|
|**PostOperation**|[!INCLUDE [cc-postoperation-description](../../includes/cc-postoperation-description.md)]|


The stage you choose depends on the purpose of the extension. You don't need to apply all your business logic within a single step. You can apply multiple steps so that your logic about whether to allow an operation to proceed can be in the **PreValidation** stage and your logic to make modifications to the message properties can occur in the **PostOperation** stage.

> [!IMPORTANT]
> An exception thrown by your code at any synchronous stage within the database transaction causes the entire transaction to roll back. Make sure your code handles any possible exception cases. If you want to cancel the operation, detect this condition in the **PreValidation** stage and throw a <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> containing an appropriate message describing why the operation was cancelled.

You can register multiple extensions for the same message and stage. Within the step registration, the **Execution Order** value determines the order in which the system processes multiple extensions for a given stage.

The system stores information about registered steps in the [SdkMessageProcessingStep table](reference/entities/sdkmessageprocessingstep.md).

### Asynchronous plug-in steps

When you register for the **PostOperation** stage, you can register the step to run in **Asynchronous Execution Mode**. These plug-ins run after the record operation completes.

This behavior is often required when working with records that are associated with the current record but created in a different process. For example, `UserSettings` related to a specific `SystemUser` record isn't created until the `SystemUser` row is created.

More information: [Asynchronous service](asynchronous-service.md)


## Event context

If your extension is a plug-in, it receives a parameter that implements the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> interface. This class provides information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.Stage> that the plug-in registers for. It also provides information about the <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.ParentContext>, which gives details about any operation within another plug-in that triggered the current operation.

If your extension is an Azure Service Bus endpoint, Azure Event Hubs topic, or a web hook, the data posted to the registered endpoint comes in the form of a <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext>. This class implements both <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> and <xref:Microsoft.Xrm.Sdk.IExecutionContext>.

For more information about the execution context, see [Understand the execution context](understand-the-data-context.md).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
