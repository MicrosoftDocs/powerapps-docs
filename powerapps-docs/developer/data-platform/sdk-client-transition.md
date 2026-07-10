---
title: "Transition client applications to Dataverse ServiceClient | Microsoft Docs"
description: "Learn about the benefits of and the changes needed to transitions your client application to use Dataverse ServiceClient class for web service connections." 
ms.custom: ""
ms.date: 07/02/2026
ms.reviewer: "pehecke"
ms.topic: "article"
author: "phecke" # GitHub ID
ms.service: powerapps
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
search.audienceType:
  - developer
---

# Transition apps to Dataverse ServiceClient

Microsoft is transitioning from the [Microsoft Dataverse SDK for .NET](developer-tools.md#dataverse-sdk-for-net) to a new web service client that uses Microsoft Authentication Library (MSAL) for authentication. This article explains why Microsoft is making these changes, what is impacted, and how to update your client applications so they continue to function as expected.

> [!NOTE]
> Some existing developer documentation and sample code use the Dataverse SDK APIs found in the [CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) NuGet package. This article describes the newer and recommended [Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package and the changes required to make use of it. Microsoft is updating documentation and sample code over time.

## Why the change?

Several reasons justify the changes to the Dataverse SDK for .NET. A few reasons are described in the following sections.

### Cross-platform application support

The new Dataverse [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class supports .NET Core development. To see what build targets are supported, go to [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) and select the **Frameworks** tab.

### MSAL authentication

Microsoft Azure Active Directory Authentication Library (ADAL.NET) isn't receiving support. Microsoft Authentication Library (MSAL.NET) is the recommended authentication API going forward. The new [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) API uses MSAL while the older [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) API uses ADAL.

### Performance and functional benefits

The Dataverse `ServiceClient` class supports a smaller interface surface, inline authentication by instance, and <xref:Microsoft.Extensions.Logging.ILogger?displayProperty=fullName>. For inline authentication, you can pass a custom authentication handler function to the `ServiceClient` constructor. By using this approach, you can have one authentication handler per web service connection instead of just one per process.

## What is impacted?

The following list summarizes the impact on different types of coding projects.

- Plug-ins or custom workflow activities - no changes

- New or existing online applications - this article is for you

- On-premises applications - this article isn't for you, yet

## What do you need to do?

The class member signatures of `ServiceClient` and `CrmServiceClient` are the same, except for the class names (in some cases). You shouldn't need to make any significant changes to your application code.

### .NET Framework based (online) application projects

To update your application projects, follow these steps:

1. Remove the older [CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) (and related) NuGet packages from your project.
1. Add the newer [Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package to your project.
1. Change every mention of the [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) class to [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) in your code.
1. Fix any namespace mismatch as the new `ServiceClient` class is now in the `Microsoft.PowerPlatform.Dataverse.Client` namespace.

### .NET Core based (online) projects

Add the [Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package to your projects, add code to call the Dataverse SDK APIs, and build.

### Plug-ins or custom workflow activities

Now that the Event Framework (in the sandbox) supports .NET Framework 4.8 built code, rebuild your existing plug-ins and custom workflow activities to target that framework. However, since Dataverse continues to support legacy versions (4.6.2, 4.7, 4.7.x) of .NET Framework, you can choose to keep your custom code build targets set to those legacy versions for now.

Continue using the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) (and related) NuGet packages.

### On-premises clients

Leave your application projects and code as is. Continue using the Microsoft.CrmSdk.CoreAssemblies NuGet package and `CrmServiceClient` class. However, plan to update your projects from using any custom service clients to instead use the `CrmServiceClient` or `ServiceClient` in the near future. See the planned [timeline](#timeline) for 2011 SOAP endpoint shutdown below.

> [!NOTE]
> If you're using custom authentication with `CrmServiceClient`, you can continue to use your custom authentication code with `ServiceClient`.

## Code samples

Available here: [ServiceClient code samples](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/ServiceClient)

## Timeline

The following table lists some important dates to keep in mind.

| Timeframe        | Event                                                                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| June 2022        | GA release of the [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package |
| December 2022    | Microsoft support for ADAL ends                                                                                                                      |
| At a future date | Planned shutdown of the 2011 SOAP endpoint for access by client applications not using our service clients (`CrmServiceClient` or `ServiceClient`)   |

> [!IMPORTANT]
> The `CrmServiceClient` class continues to function as documented even after ADAL authentication is turned off. Both service client classes continue to function as documented after the 2011 SOAP endpoint is turned off. If required, Microsoft might release an updated assembly containing revised service clients that your application needs to load at run-time.

### See also

[Overview of the Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/msal-overview)  
[Migrate applications to the Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/msal-migration)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
