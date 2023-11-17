---
title: "Use OAuth with Cross-Origin Resource Sharing to connect a Single-Page Application (Microsoft Dataverse)| Microsoft Docs"
description: "Learn how to use OAuth with Cross-Origin Resource Sharing (CORS) to connect a Single-Page Application."
ms.date: 09/08/2022
ms.reviewer: jdaly
ms.topic: article
author: ritesp
ms.author: ritesp
ms.subservice: dataverse-developer
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
---

# Use OAuth with Cross-Origin Resource Sharing to connect a Single-Page Application

You can create a Single-Page Application (SPA) which uses JavaScript to work with Microsoft Dataverse data using Web API. To provide this, Cross-Origin Resource Sharing (CORS) is enabled so that your SPAs can bypass browser restrictions that normally prevent requests that cross domain boundaries.
  
<a name="bkmk_Spas_and_same_origin_policy"></a> 
  
## SPAs and Same-Origin policy  

SPAs depend on extensive use of client-side JavaScript to create a single dynamic page which doesn't need to load new pages. Instead they use [Ajax](https://developer.mozilla.org/docs/Web/Guide/AJAX) programming techniques to retrieve data and other resources from the server. SPAs work well when the data and resources exist in the same domain as the application. But to protect access to data and resources on other domains, all modern browsers enforce a [Same-Origin policy](https://developer.mozilla.org/docs/Web/Security/Same-origin_policy) to prevent sites from using data and resources from sites on a different domain. CORS provides a way to gain access to resources on another domain. Creating a SPA to access Dataverse data without CORS is not a viable option.
  
<a name="bkmk_use_cors"></a>

## Use CORS with Dataverse

The [CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol) provides a detailed description of how to implement and use CORS. It explains all about the various headers and preflight requests that you need to apply to make CORS work. The good news is that you don't need to become an expert in CORS to use it with Dataverse. The server-side part has been done for you and all you need is to know how to consume it.  You don't need to understand all the inner workings of CORS to use it with Dataverse. Instead you can use the [Microsoft Authentication Library for JavaScript (MSAL.js) 2.0 for Browser-Based Single-Page Applications](https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-browser) and it will take care of much of the CORS complexity for you. Since Dataverse users are authenticated using Microsoft Entra ID, MSAL.js is the supported way to authenticate SPA users.

## Preparing to use MSAL.js with a SPA

In order to configure your SPA to work with msal.js you will need to:

1. Register your application with the Microsoft Entra ID tenant.
1. Set configuration variables in your SPA with information from that registration.  
   You will need to include the following: 
   - The URL to your Dataverse organization.
   - The Id of the Microsoft Entra ID tenant your organization uses to authenticate.
   - The client ID you get when you register your application.
   - The URL to where the SPA will be deployed or debugged during development.

The set of steps required are described in [Quickstart: Register and configure a SPA application for Dataverse using msal.js](quick-start-register-configure-simplespa-application-msal-js.md)

### See also

[Use OAuth to connect to Dataverse web services](authenticate-oauth.md)<br />
[Quickstart: Register and configure a SPA application for Dataverse using msal.js](quick-start-register-configure-simplespa-application-msal-js.md)<br />
[Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
