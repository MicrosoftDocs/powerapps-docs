---
title: "Transition client applications to Dataverse ServiceClient | Microsoft Docs" 
description: "Learn about the benefits of and the changes needed to transitions your client application to use Dataverse ServiceClient class for web service connections." 
ms.custom: ""
ms.date: 10/17/2023
ms.reviewer: "pehecke"
ms.topic: "article"
author: "phecke" 
ms.service: powerapps
ms.subservice: dataverse-developer
ms.author: "pehecke"
search.audienceType:
  - developer
---

# Transition apps to Dataverse ServiceClient

We are transitioning from [Microsoft Dataverse SDK for .NET](developer-tools.md#dataverse-sdk-for-net) to include a new web service client that uses Microsoft Authentication Library (MSAL) for authentication. This article contains the information you need to understand why we are making these changes, what is impacted, and how to update your client applications so they continue to function as expected.

> [!NOTE]
> Some of our existing developer documentation and sample code uses the Dataverse SDK APIs found in the [CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) NuGet package. This article describes the newer and recommended [Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package and the changes required to make use of it. Updates to documentation and sample code is happening over time.

## Why the change?

There are quite a few good reasons for the changes to the Dataverse SDK for .NET. A few are called out below.

### Cross-platform application support

The new Dataverse [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class supports .NET Core development. Navigate to [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) and select the **Frameworks** tab to see what build targets are supported.

### MSAL authentication

Microsoft Azure Active Directory Authentication Library (ADAL.NET) is no longer receiving support. Microsoft Authentication Library (MSAL.NET) is the recommended authentication API going forward. Our new [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) API uses MSAL while our older [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) API uses ADAL.

### Performance and functional benefits

The Dataverse `ServiceClient` class supports a smaller interface surface, inline authentication by instance, and <xref:Microsoft.Extensions.Logging.ILogger?displayProperty=fullName>. As for inline authentication, you can pass a custom authentication handler function to the `ServiceClient` constructor. In this way you can have one authentication handler per web service connection instead of just one per process.

## What is impacted?

Below is a quick summary of the impact to certain types of coding projects.

- Plug-ins or custom workflow activities - no changes

- New or existing online applications - this article is for you

- On-premises applications - this article is not for you, yet

## What do you need to do?

The good news is that the class member signatures of `ServiceClient` and `CrmServiceClient` are the same, except for the class names themselves being slightly different. Application code should not need any significant changes.

### .NET Framework based (online) application projects

To update your application projects, follow these steps.

1. Remove the older [CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) (and related) NuGet packages from your project.
1. Add the newer [Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package to your project.
1. Change every mention of the [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) class to [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) in your code.
1. Fix any namespace mismatch as the new `ServiceClient` class is now in the `Microsoft.PowerPlatform.Dataverse.Client` namespace.

### .NET Core based (online) projects

Simply add the [Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package to your projects, add code to call the Dataverse SDK APIs, and build.

### Plug-ins or custom workflow activities

Nothing really for you to do here. Continue using the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) (and related) NuGet packages with .NET Framework 4.6.2.

### On-premises clients

Leave your application projects and code as is. Continue using the Microsoft.CrmSdk.CoreAssemblies NuGet package and `CrmServiceClient`class. However, plan to update your projects from using any custom service clients to instead use the `CrmServiceClient` or `ServiceClient` in the near future. See the planned [timeline](#timeline) for 2011 SOAP endpoint shutdown below.

> [!NOTE]
> If you are using custom authentication with `CrmServiceClient`, you can continue to use your custom authentication code with `ServiceClient`.

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
> The `CrmServiceClient` class will continue to function as documented even after ADAL authentication is turned off. Both service client classes will continue to function as documented after the 2011 SOAP endpoint has been turned off. If required, we may release an updated assembly containing revised service clients that your application will need to load at run-time.

### See also

[Overview of the Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/msal-overview)  
[Migrate applications to the Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/msal-migration)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
