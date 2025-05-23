---
title: "Use OAuth with CORS to connect a SPA"
description: "Learn how to use OAuth with Cross-Origin Resource Sharing (CORS) to connect a Single-Page Application (SPA) that connects to Microsoft Dataverse using the Web API and JavaScript."
ms.date: 03/22/2025
ms.reviewer: jdaly
ms.topic: how-to
author: ritesp
ms.author: ritesp
ms.subservice: dataverse-developer
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
---

# Use OAuth with CORS to connect a SPA

You can create a [Single-Page Application (SPA)](https://developer.mozilla.org/docs/Glossary/SPA) which uses JavaScript to work with Microsoft Dataverse data using Web API. To enable creation of apps like these, Dataverse enabled [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/docs/Web/HTTP/Guides/CORS) so that your SPAs can bypass browser restrictions that normally prevent requests that cross domain boundaries.
  
<a name="bkmk_Spas_and_same_origin_policy"></a> 
  
## SPAs and Same-Origin policy  

SPAs depend on extensive use of client-side JavaScript to create a single dynamic page which doesn't need to load new pages. Instead they use programming patterns using [network requests](https://developer.mozilla.org/docs/Learn_web_development/Core/Scripting/Network_requests), sometimes called 'Ajax', to retrieve data and other resources from the server. SPAs work well when the data and resources exist in the same domain as the application. But to protect access to data and resources on other domains, all modern browsers enforce a [Same-Origin policy](https://developer.mozilla.org/docs/Web/Security/Same-origin_policy) to prevent sites from using data and resources from sites on a different domain. CORS provides a way to gain access to resources on another domain. Creating a SPA to access Dataverse data without CORS isn't a viable option.
  
<a name="bkmk_use_cors"></a>

## Use CORS with Dataverse

The [CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol) provides a detailed description of how to implement and use CORS. It explains all about the various headers and preflight requests that you need to apply to make CORS work. The good news is that you don't need to become an expert in CORS to use it with Dataverse. The server-side part was done for you and all you need is to know how to consume it. You don't need to understand all the inner workings of CORS to use it with Dataverse. Instead you can use the [Microsoft Authentication Library for JavaScript (MSAL.js)](/javascript/api/overview/msal-overview?view=msal-js-latest&preserve-view=true) and it takes care of much of the CORS complexity for you. Since Dataverse users are authenticated using Microsoft Entra ID, MSAL.js is the supported way to authenticate SPA users.

## Preparing to use MSAL.js with a SPA

In order to configure your SPA to work with MSAL.js, you need to:

1. Register your application with the Microsoft Entra ID tenant.
1. Set configuration variables in your SPA with information from that registration.  
   You need to include the following items: 
   - The URL to your Dataverse organization.
   - The ID of the Microsoft Entra ID tenant your organization uses to authenticate.
   - The client ID you get when you register your application.
   - The URL to where the SPA is deployed or debugged during development.

The set of steps required are described in [Quickstart: Web API with client-side JavaScript and Visual Studio Code](webapi/quick-start-js-spa.md).

### See also

[Use OAuth to connect to Dataverse web services](authenticate-oauth.md)   
[Quickstart: Web API with client-side JavaScript and Visual Studio Code](webapi/quick-start-js-spa.md)   
[Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
