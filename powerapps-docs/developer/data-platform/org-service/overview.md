---
title: "Use the SDK for .NET"
description: "Learn how you can use the Microsoft Dataverse SDK for .NET to work with business data."
ms.date: 08/20/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
ms.topic: overview
ms.custom: bap-template
contributors:
 - JimDaly
 - phecke
---

# Use the SDK for .NET

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The SDK for .NET provides access to the business data, data table definitions (metadata), and data operations supported by the Dataverse platform.

Certain development scenarios require the use of the Dataverse SDK for .NET. When you write custom code to extend the functionality of Dataverse, such as when you create plug-ins and custom workflow activities, you must build your code by using the .NET Framework and Dataverse SDK.

## Obtain the SDK assemblies

Use the SDK for .NET assemblies for .NET Framework or .NET Core based applications. For .NET Framework only development, get the SDK assemblies in the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) NuGet package. For .NET Framework or .NET Core development, get the SDK assemblies in the [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client) NuGet package.

After you add the NuGet package to your Visual Studio project, you have access to the namespaces and classes that enable your application to interact with the Organization and Discovery web services.

## Interact with the Organization service

This section covers some key concepts about using provided SDK classes to connect with the web services and perform operations.

### Establish a web service connection

The <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface provides a connection to the Organization service enabling applications to work with business data, and table and column definitions. The SDK includes two implementations of this interface: <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> and <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient>. For new application development, use the `ServiceClient` class that supports newer authentication technologies (MSAL) and has a few more features not available in `CrmServiceClient`. However, both client classes are mostly the same from an API perspective. You see code samples in this documentation using either of these classes, and it's fairly easy to convert code that uses `CrmServiceClient` to use `ServiceClient`.

More information: [Transition apps to Dataverse ServiceClient](../sdk-client-transition.md), [IOrganizationService Interface](iorganizationservice-interface.md)

### Web service operations

In the Dataverse SDK for .NET, you initiate web service operations by sending *messages* or *message requests* to the service. Each message has a name that indicates the purpose of the message, and the corresponding request class name is based on that message name. For example, to create a row of data in a table, you populate a create request with data and have the service client send (Execute) this request to the Organization service. The operation is 'create' and the message request is named <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>. When you execute a request, the service returns a response class object (for example, <xref:Microsoft.Xrm.Sdk.Messages.CreateResponse>) which contains an execution status and results data. This pattern is the same for the other operations that the service supports.

Take a look at the available message request and response classes in the <xref:Microsoft.Xrm.Sdk.Messages> and <xref:Microsoft.Crm.Sdk.Messages> namespaces.

## About the legacy SOAP endpoint

Microsoft introduced the Organization service endpoint, known as the SOAP endpoint, in 2011. This endpoint is deprecated. This means that it continues to work and be supported until Microsoft removes it. Microsoft also announced that they'll update the SDK for .NET assemblies so that they'll continue to work after the endpoint is removed. This means that updated SDK for .NET assemblies will be available before the endpoint is removed. Developers will be required to update their code to use these new assemblies at some point in the future. The key takeaway is that developers access the Organization service by using the SDK for .NET and ignore the endpoint and its protocol. For more information, see [Transition apps to Dataverse ServiceClient](../sdk-client-transition.md).

Since the Web API uses a different endpoint, it isn't affected by this 2011 SOAP endpoint deprecation.

## Next steps

Let's write some code! [Quickstart: SDK for .NET sample (C#)](quick-start-org-service-console-app.md)

### See also

[Discover user organizations](../discovery-service.md)  
[Use plug-ins to extend business processes](../plug-ins.md)  
[Workflow extensions](../workflow/workflow-extensions.md)  

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
