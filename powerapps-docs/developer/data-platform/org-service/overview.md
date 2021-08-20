---
title: "Use the Microsoft Dataverse Organization Service (Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can use Microsoft Dataverse Organization Service to work with data, and table and column definitions." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 04/15/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use the Microsoft Dataverse Organization Service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The Organization service is one of two web services you can use to work with data, and table and column definitions in Dataverse. The other is the [Web API](../webapi/overview.md).

The organization service is optimized for use with the .NET Framework and the SDK assemblies in the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) NuGet package provide the classes for the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface necessary work with data, and table and column definitions using this service. 

Some extension capabilities, such as plug-ins and workflow extensions, depend on the .NET Framework and classes defined in these assemblies so the organization service is the only option when using these methods to extend Dataverse.

## Organization service assemblies

It is valuable to recognize that the organization service is what defines the platform. The organization service defines the supported operations as messages. Each message has a name. These messages correspond to the events that are emitted by the event framework. More information: [Event Framework](../event-framework.md)

The .NET assemblies for the organization service currently use a SOAP endpoint. The assemblies were designed to closely model the underlying platform services based on <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface. However they are not the same components and should not be confused with one another. 

The SOAP endpoint for the organization service was introduced in 2011 and we have announced that it is deprecated. This means that it will continue to work and be supported until we remove it. We have also announced that we will update the .NET SDK assemblies so that they will continue to work after the SOAP endpoint is removed. This means that there will be updated SDK assemblies available before the SOAP endpoint is removed and developers will be required to update their code to use these new assemblies at some point in the future.

## Using the organization service without assemblies

It is possible for developers to use the SOAP endpoint of the organization service without using the .NET SDK assemblies, for example by creating a web service proxy using the WSDL exposed by the service,  but the RESTful nature of the Web API makes it a superior alternative.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]