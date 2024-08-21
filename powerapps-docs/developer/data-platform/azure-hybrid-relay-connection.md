---
title: Use a hybrid relay connection
description: Learn about sending Dataverse message processing data to Azure using the ServiceBus and a hybrid relay connection. 
author: phecke
ms.author: pehecke
ms.subservice: dataverse-developer
ms.topic: concept-article
ms.date: 08/19/2024
search.audienceType: 
  - developer
---

# Use a hybrid relay connection

There are different types of messaging contracts with Microsoft Azure that Microsoft Dataverse supports - queue, one-way, REST, topic, etc. This article will delve into the hybrid relay connection, which uses a REST contract, as a means to send the Dataverse execution context across the Azure ServiceBus to a listener app.

The hybrid relay is presently the only supported Dataverse to Azure ServiceBus connection type that:

- You can target a .NET Core build of a listener app
- Uses the latest [Microsoft.Azure.Relay](https://www.nuget.org/packages/Microsoft.Azure.Relay#supportedframeworks-body-tab) messaging APIs

So if you are interested in developing a .NET Core version of ServiceBus listener app today, read on.

## Prerequisites

TODO: [List the prerequisites if appropriate]

## Transitioning to Microsoft.Azure.Relay

All supported Dataverse to Azure ServiceBus connection types, except for the hybrid relay connection, target .NET Framework and use the (now) deprecated [WindowsAzure.ServiceBus](https://www.nuget.org/packages/WindowsAzure.ServiceBus) APIs. Those non-relay connections will continue to be supported for some time since the WindowsAzure.ServiceBus APIs will be supported by Microsoft until the year 2026.

Once Dataverse and the Plug-in Registration tool have been updated to use the newer Azure ServiceBus messaging technologies, our documentation and code samples will be updated. For now, we provide this article and related code sample for you to get started developing a listener app that uses Microsoft.Azure.Relay.

## Configuring an Azure namespace and connection

## Write a listener app

## Configure a Dataverse service endpoint and step

## Getting it all working

You can test the Dataverse-Azure connection by following these steps.

1. Enable the service endpoint step if it is disabled.
1. Execute the listener app so that it starts listening on the hybrid relay connection.
1. Perform the intended Dataverse operation for which the step was registered. The operation triggers a plug-in to post the execution context to the service bus.
1. Check the Dataverse asynchronous system log for success or failure of the post.

If all goes well, the listener app will print the received remote execution context data to the terminal window. If not, then check the asynchronous system log for a failure. The log entry description details the reason for failure.

## Related content

- [Azure integration](azure-integration.md)
- [Register a Dataverse service endpoint](azure-register-service-endpoint.md)
