---
title: "Transition client applications to the new Dataverse ServiceClient | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the benefits of and the changes needed to transitions your client application to the next generation Dataverse web service client." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/26/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "phecke" # GitHub ID
ms.service: powerapps
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Transition apps to the next-generation Dataverse service client

The Microsoft Power Platform team is in the process of transitioning our current Microsoft Dataverse SDK for .NET to the next-generation version of our APIs (internally called Dataverse SDK vNext). This article contains the information you need to understand why we are making these changes, what is impacted, and how to update your client applications so they continue to function as expected.

## Why the change?

There are quite a few good reasons for the changes to the Dataverse SDK for .NET. A few are called out below.

### Cross-platform application support

Navigate to [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) and select the **Frameworks** tab to see what build targets are supported.

### MSAL authentication

Microsoft Azure Active Directory Authentication Library (ADAL) support ends soon. Microsoft Authentication Library (MSAL) is the recommended authentication API going forward. Our new client APIs use MSAL while our older client APIs use ADAL.

### Performance and functional benefits

The new Dataverse service client includes automatic handling of request retries, caching of the authentication token, and more. With the older service client, you had to write code to manage these.

## What is impacted?

Below is a quick summary of the impact to certain types of coding projects.

- Plug-ins or custom workflow activities - no changes, just business as usual

- New or existing online applications - this article is definitely for you

- On-premise applications - this article is not for you, yet

## What do you need to do?

The good news is that the API signatures from the older service client to the new service client are the same. Application code should not need any changes. You should just have to update the application project to use the new Dataverse.Client NuGet packages and re-build.

- .NET Framework based (online) application projects - remove the older [CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) (and related) NuGet packages from your project, add the new [Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package, and then rebuild.

- .NET Core based (online) projects - simply add the Microsoft.PowerPlatform.Dataverse.Client NuGet package to your projects, add code to call the Dataverse SDK APIs, and build.

- Plug-ins or custom workflow activities - nothing really to do here unless you want to swap out the older CoreAssemblies (and related) NuGet packages and add the new Dataverse.Client package. You will still be building your project using .NET Framework 4.6.2.

- On-premise clients - leave your application projects and code as is

## Timeline

The following table lists some important dates to keep in mind.

| Timeframe | Event |
| --- | --- |
|June 2022|GA release of the [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) NuGet package|
|Fall 2022|Planned shutdown of the 2011 SOAP endpoint for access by client applications not using our service clients (CrmServiceClient, DataverseServiceClient)|
|December 2022|Microsoft support for ADAL ends|

### See also

[Overview of the Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/msal-overview)  
[Migrate applications to the Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/msal-migration)  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]