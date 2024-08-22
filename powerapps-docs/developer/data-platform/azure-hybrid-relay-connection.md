---
title: Use a hybrid relay connection
description: Learn about sending Dataverse message processing data to Azure using the ServiceBus and a hybrid relay connection. 
author: phecke
ms.author: pehecke
ms.subservice: dataverse-developer
ms.topic: concept-article
ms.date: 08/22/2024
search.audienceType: 
  - developer
---

# Use a hybrid relay connection

There are different types of messaging contracts with Microsoft Azure that Microsoft Dataverse supports - queue, one-way, REST, topic, etc. This article delves into the hybrid relay connection, which uses a REST contract, as a means to send the Dataverse execution context across the Azure ServiceBus to a listener app.

The hybrid relay is presently the only supported Dataverse to Azure ServiceBus connection type that:

- You can target a .NET Core build of a listener app
- Uses the latest [Microsoft.Azure.Relay](https://www.nuget.org/packages/Microsoft.Azure.Relay#supportedframeworks-body-tab) messaging APIs

So if you're interested in developing a Dataverse compatible ServiceBus listener app targeting .NET Core today, read on.

## Transitioning to Azure relay messaging

All supported Dataverse to Azure ServiceBus connection types, except for the hybrid relay connection, target .NET Framework and use the (now) deprecated [WindowsAzure.ServiceBus](https://www.nuget.org/packages/WindowsAzure.ServiceBus) package and the [Microsoft.ServiceBus](/dotnet/api/microsoft.servicebus?view=azure-dotnet-legacy) namespace. Those non-relay connections continue to be supported for some time since the Microsoft.ServiceBus APIs are supported by Microsoft until the later part of year 2026.

Once Dataverse and the Plug-in Registration tool are updated to use the newer Azure ServiceBus messaging technologies, our documentation and code samples will be updated. For now, we provide this article and related code sample for you to get started developing a listener app that uses the Microsoft.Azure.Relay namespace and can target .NET Core.

## Configure an Azure namespace and connection

Read the Azure documentation, [Get started with Relay Hybrid Connections HTTP requests in .NET](/azure/azure-relay/relay-hybrid-connections-http-requests-dotnet-get-started#create-a-namespace), on how to configure a namespace and hybrid relay connection.

Here's an example namespace configuration named contoso-relay.
:::image type="content" source="media/azure-relay-namespace.png" alt-text="Example Azure namespace." lightbox="media/azure-relay-namespace.png":::

Here's an example hybrid relay connection configuration named contoso-hc.
:::image type="content" source="media/azure-hybrid-connection.png" alt-text="Example hybrid relay connection." lightbox="media/azure-hybrid-connection.png":::

## Write a listener app

Let's take a look at some example code for a listener app.

```csharp
class Program
{
    static async Task Main(string[] args)
    {
        // TODO Set the shared access key value and connection URL as configured in Azure. 
        var tokenProvider = TokenProvider.CreateSharedAccessSignatureTokenProvider(
            "RootManageSharedAccessKey", "<shared-access-key>");
        var listener = new HybridConnectionListener(
            new Uri("sb://<namespace>.servicebus.windows.net/<hybrid-connection>"), tokenProvider);

        // Define an anonymous request handler that accepts the posted request data.
        listener.RequestHandler = (context) =>
        {
            // Read the request body.
            string requestBody = String.Empty;
            using (var reader = new StreamReader(context.Request.InputStream, Encoding.UTF8))
            {
                requestBody = reader.ReadToEnd();
                Console.WriteLine($"Received request body");
            }

            // Post a response to the ServiceBus. A custom Azure-aware plug-in
            // can receive this response string from Azure.
            var response = JsonConvert.SerializeObject(new { Message = "Hello from Relay Listener!" });
            var responseJson = JsonConvert.SerializeObject(response);
            var responseBytes = Encoding.UTF8.GetBytes(responseJson);
            context.Response.StatusCode = (System.Net.HttpStatusCode)200;
            context.Response.Headers.Add("Content-Type", "application/json");
            context.Response.OutputStream.Write(responseBytes, 0, responseBytes.Length);
            context.Response.Close();

            // Serialize the request body in XML format into a RemoteExecutionContext object.
            RemoteExecutionContext remoteContext; 
            using (var stringReader = new StringReader(requestBody))
            {
                using (var xmlReader = XmlReader.Create(stringReader))
                {
                    var serializer = new DataContractSerializer(typeof(RemoteExecutionContext));
                    var result = serializer.ReadObject(xmlReader);
                    if (result is RemoteExecutionContext tempContext)
                    {
                        remoteContext = tempContext;
                    }
                    else
                    {
                        // Handle the null case appropriately
                        remoteContext = new RemoteExecutionContext(); // or throw an exception
                    }
                }
            }
            // TODO Do something with the context object here, like outputting
            // the context object data to the console window.
        };
        await listener.OpenAsync();
        Console.WriteLine("Listener opened, press any key to exit...");
        Console.ReadKey();
        await listener.CloseAsync();
    }
}
```

The full code sample is available in the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples/) repo at [dataverse/orgsvc/C#-NETCore](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23-NETCore).

## Configure a service endpoint and step

Follow the instructions in [Register a service endpoint](azure-register-service-endpoint.md) to configure a service endpoint and plug-in step that posts the Dataverse remote execution context to the Azure ServiceBus.

## Getting it all working

You can test the Dataverse-Azure connection by following these steps.

1. Enable the service endpoint plug-in step (if disabled).
1. Execute the listener app so that it starts listening on the hybrid relay connection.
1. Perform the intended Dataverse operation for which the step was registered. The operation triggers the service endpoint plug-in to post the execution context to the service bus.
1. Check the Dataverse System Job records for success or failure of the post.

If you are running the sample listener app linked in this article, the listener app outputs the received remote execution context data to the console window. If this does not happen, check the Dataverse System Job records for a failure. The system job description details the reason for failure.

You can access the system jobs in Power Apps under **Advanced settings** > **Settings** > **System Jobs**.

## Related content

- [Azure integration](azure-integration.md)
- [Register a Dataverse service endpoint](azure-register-service-endpoint.md)
