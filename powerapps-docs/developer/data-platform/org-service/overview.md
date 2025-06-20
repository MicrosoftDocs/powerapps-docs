---
title: "Use the SDK for .NET"
description: "Learn how you can use the Microsoft Dataverse SDK for .NET to work with business data."
ms.date: 09/27/2022
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

There are certain development scenarios in which the Dataverse SDK for .NET must be used. When writing custom code to extend the functionality of Dataverse, such as when creating plug-ins and custom workflow activities, you must build your code using the .NET Framework and Dataverse SDK.

## Obtaining the SDK assemblies

Use the SDK for .NET assemblies for .NET Framework or .NET Core based applications. For .NET Framework only development, the SDK assemblies are available in the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) NuGet package. For .NET Framework or .NET Core development, the SDK assemblies are available in the [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client) NuGet package.

After adding the NuGet package to your Visual Studio project, you then have access to the namespaces and classes that enable your application to interact with the Organization and Discovery web services.

## Interacting with the Organization service

In this section we cover some key concepts about using provided SDK classes to connect with the web services and perform operations.

### Establishing a web service connection

The <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface provides a connection to the Organization service enabling applications to work with business data, and table and column definitions. There are two implementations of this interface in the SDK: <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> and <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient>. For new application development, you should be using the `ServiceClient` class which supports newer authentication technologies (MSAL) and has a few additional features not available in `CrmServiceClient`. However, both client classes are mostly the same from an API perspective. You will see code samples in this documentation using either of these classes, and it is fairly easy to convert code that uses `CrmServiceClient` to use `ServiceClient`.

More information: [Transition apps to Dataverse ServiceClient](../sdk-client-transition.md), [IOrganizationService Interface](iorganizationservice-interface.md)

### Web service operations

In the Dataverse SDK for .NET, web service operations are initiated by sending *messages* or *message requests* to the service. Each message has a name which indicates the purpose of the message, and the corresponding request class name is based on that message name. For example, to create a row of data in a table, you populate a create request with data and have the service client send (Execute) this request to the Organization service. The operation is 'create' and the message request is named <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>. After executing a request, the service returns a response class object (e.g., <xref:Microsoft.Xrm.Sdk.Messages.CreateResponse>) which contains an execution status and results data. This pattern is the same for the other operations that the service supports.

Take a look at the available message request and response classes in the <xref:Microsoft.Xrm.Sdk.Messages> and <xref:Microsoft.Crm.Sdk.Messages> namespaces.

## About the legacy SOAP endpoint

The Organization service endpoint that was introduced in 2011, known as the SOAP endpoint, has been deprecated for some time now. This means that it will continue to work and be supported until we remove it. We have also announced that we will update the SDK for .NET assemblies so that they will continue to work after the endpoint is removed. This means that there will be updated SDK for .NET assemblies available before the endpoint is removed. Developers will be required to update their code to use these new assemblies at some point in the future. The key takeaway is that developers will access the Organization service using the SDK for .NET and ignore the endpoint and its protocol. More information: [Transition apps to Dataverse ServiceClient](../sdk-client-transition.md)

Since the Web API uses a different endpoint, it is not affected by this 2011 SOAP endpoint deprecation.

## Next steps

Let's write some code! [Quickstart: SDK for .NET sample (C#)](quick-start-org-service-console-app.md)

### See also

[Discover user organizations](../discovery-service.md)  
[Use plug-ins to extend business processes](../plug-ins.md)  
[Workflow extensions](../workflow/workflow-extensions.md)  

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
