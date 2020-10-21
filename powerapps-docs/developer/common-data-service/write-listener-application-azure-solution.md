---
title: "Write a listener application for a Microsoft Azure solution (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "The topic describes how to write an Azure solution listener application that can read and process Common Data Service messages that are posted to the Azure Service Bus." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 10/06/2019
ms.service: powerapps
ms.topic: article
ms.assetid: cf68e0a9-c240-59e7-c501-68cbfa0df455
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Write a listener application for a Azure solution

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

This topic describes how to write an Azure solution  listener application that can read and process Common Data Service messages that are posted to the Azure Service Bus. As a prerequisite, you should familiarize yourself with how to write a Azure Service Bus listener before trying to learn the specifics of a Common Data Service listener. For more information, see the [Azure Service Bus documentation](/azure/service-bus/).
  
<a name="bkmk_writequeued"></a>

## Write a queue listener

A message *queue* is a repository of messages received at a service bus endpoint. A *queue listener* is an application that reads and processes these queued messages. Because the service bus messages are stored in a queue, a listener doesn't have to be actively listening for messages to be received in the queue. A queue listener can be started after messages have arrived in the queue and still process those messages. Other types of listeners discussed in the next section must be actively listening or they will miss the opportunity to read a message. These messages can originate from Common Data Service or from some other source. 
  
> [!IMPORTANT]
>  When writing a queue listener, check each message header action to determine if the message originated from Common Data Service. For information on how to do this see [Filter messages](write-listener-application-azure-solution.md#filter).  
  
You can do a destructive message read using [Receive](/dotnet/api/microsoft.servicebus.messaging.queueclient.receive) in [ReceiveMode.ReceiveAndDelete](/dotnet/api/microsoft.servicebus.messaging.receivemode) mode, where the message is read and removed from the queue, or a non-destructive read using [ReceiveMode.PeekLock](/dotnet/api/microsoft.servicebus.messaging.receivemode) mode, where the message is read but still available in the queue. The persistent queue listener sample code provided in this SDK does a destructive read. For more information about reading messages from a queue, see [How to Receive Messages from a Queue](/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues#receive-messages-from-the-queue).  
  
A *topic* is similar to a queue but implements a publish/subscribe model. One or more listeners can subscribe to the topic and receive messages from its queue. More information: [Queues, Topics, and Subscriptions](/azure/service-bus-messaging/service-bus-queues-topics-subscriptions)  
  
> [!IMPORTANT]
>  To use these queue or topic contracts, you must write your listener applications using the [Azure SDK](https://azure.microsoft.com/downloads/archive-net-downloads/).
  
Use of queues and topics in your multi-system software design can result in the decoupling of systems. If the listener application ever becomes unavailable, the message delivery from Common Data Service will still succeed and the listener application can continue processing the queue message when it is back online. More information: [Queues, Topics, and Subscriptions](/azure/service-bus-messaging/service-bus-queues-topics-subscriptions)  
  
<a name="bkmk_writeoneway"></a>

## Write a one-way, two-way, or REST listener

In addition to the queue listener described previously, you can write a listener for three other service bus contracts that are supported by Common Data Service: one-way, two-way, and REST. A one-way listener can read and process a message posted to the service bus. A two-way listener can do the same but can also return a string of some information back to Common Data Service. A REST listener is the same as the two-way listener except that it works with a REST endpoint. Notice that these listeners must be actively listening at a service endpoint to read a message sent over the service bus. If the listener isn't listening when Common Data Service attempts to post a message to the service bus, the message doesn't get sent.
  
Writing a listener is structured around what is known as ABC: address, binding, and contract. 

### One-way listener
  
- Address: service URI  
  
- Binding: [WS2007HttpRelayBinding](/dotnet/api/microsoft.servicebus.ws2007httprelaybinding)  
  
- Contract: <xref:Microsoft.Xrm.Sdk.IServiceEndpointPlugin>  
  
After your listener is registered with an endpoint, the listener's <xref:Microsoft.Xrm.Sdk.IServiceEndpointPlugin.Execute*> method is invoked whenever a message is posted to the service bus by Common Data Service. The `Execute` method doesn't return any data from the method call. For more information, see the one-way listener sample, [Sample: One-way Listener](org-service/samples/one-way-listener.md).  
  
### Two-way listener
  
- Address: service URI  
  
- Binding: [WS2007HttpRelayBinding](/dotnet/api/microsoft.servicebus.ws2007httprelaybinding)  
  
- Contract: <xref:Microsoft.Xrm.Sdk.ITwoWayServiceEndpointPlugin>  
  
For this two-way contract, the <xref:Microsoft.Xrm.Sdk.ITwoWayServiceEndpointPlugin.Execute*> method returns a string from the method call. For more information, see the two-way listener sample, [Sample: Two-way Listener](org-service/samples/two-way-listener.md).  
  
### REST listener
  
- Address: service URI  
  
- Binding: [WebHttpRelayBinding](/dotnet/api/microsoft.servicebus.wshttprelaybinding)
  
- Contract: <xref:Microsoft.Xrm.Sdk.IWebHttpServiceEndpointPlugin>  
  
For the REST contract, the <xref:Microsoft.Xrm.Sdk.IWebHttpServiceEndpointPlugin.Execute*>  method returns a string from the method call. Refer to the REST listener sample, [Sample: REST Listener](org-service/samples/rest-listener.md), for more information. Notice that in the REST listener sample, a <xref:System.ServiceModel.Web.WebServiceHost> is instantiated and not a <xref:System.ServiceModel.ServiceHost> as was done in the two-way sample.
  
> [!NOTE]
>  When using the out-of-box (ServiceBusPlugin) plug-in with a two-way or REST listener, the plug-in doesn't use any string data returned from the listener. However, a custom Azure-aware plug-in could make use of this information.  
> 
>  When you run the listener samples, the issuer secret you're prompted for is the Azure Service Bus management key. The WS2007 Federation HTTP binding uses `token` mode and the WS-Trust 1.3 protocol.  
  
<a name="filter"></a>

## Filter messages

There is a property bag of extra information added to each brokered message [Properties](/dotnet/api/microsoft.servicebus.messaging.brokeredmessage#properties) property sent from Common Data Service. The property bag, available with queue, relay, and topic contract endpoints, contains the following information:  
  
- Organization URI
- Calling user ID
- Initiating user ID
- Entity logical name
- Request name  
  
This information identifies the organization, user, entity, and message request being processed by Common Data Service that resulted in the service bus message being posted. The availability of these properties indicates that the message was sent from Common Data Service. Your listener code can decide how to process the message based on these values.  
  
<a name="bkmk_multiple-formats"></a>
 
## Read the data context in multiple data formats

The data context from the current Common Data Service operation is passed to your Azure solution listener application in the body of a service bus message. In previous releases, only a .NET binary format was supported.  For cross-platform (non-.NET) interoperability, you can now specify one of three data formats for the message body: .NET Binary, JSON, or XML.  This format is specified in the [MessageFormat](reference/entities/serviceendpoint.md#BKMK_MessageFormat) attribute of the [ServiceEndpoint Entity](reference/entities/serviceendpoint.md).
  
When receiving messages, your listener application can read the data context in the message body based on the contentType of the message. Sample code to do so is shown below.  
  
```csharp
var receivedMessage = inboundQueueClient.Receive(TimeSpan.MaxValue);  
  
if (receivedMessage.ContentType = "application/msbin1")  
{  
    RemoteExecutionContext context = receivedMessage.GetBody<RemoteExecutionContext>();  
}  
else if (receivedMessage.ContentType = "application/json")  
{  
    //string jsonBody = new StreamReader(receivedMessage.GetBody<Stream>(), Encoding.UTF8).ReadToEnd();  
    RemoteExecutionContext contextFromJSON = receivedMessage.GetBody<RemoteExecutionContext>(  
        new DataContractJsonSerializer(typeof(RemoteExecutionContext)));  
}  
else if (receivedMessage.ContentType = "application/xml")  
{  
    //string xmlBody = new StreamReader(receivedMessage.GetBody<Stream>(), Encoding.UTF8).ReadToEnd();  
    RemoteExecutionContext contextFromXML = receivedMessage.GetBody<RemoteExecutionContext>(  
        new DataContractSerializer(typeof(RemoteExecutionContext)));  
}  
```  
  
### See also

[Azure Extensions](azure-integration.md)<br />
[Write a Custom Azure-aware Plug-in](write-custom-azure-aware-plugin.md)<br />
[Sample: Persistent Queue Listener](org-service/samples/persistent-queue-listener.md)<br />
[Sample: One-way Listener](org-service/samples/one-way-listener.md)<br />
[Sample: Two-way Listener](org-service/samples/two-way-listener.md)<br />
[Sample: REST Listener](org-service/samples/rest-listener.md)<br />
[Work with Common Data Service data in your Azure solution](work-data-azure-solution.md)<br />
[Work with Common Data Service event data in your Azure Event Hub solution](work-event-data-azure-event-hub-solution.md)
 