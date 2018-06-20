---
title: "Use OAuth with Cross-Origin Resource Sharing to connect a Single Page Application (Common Data Service for Apps)| Microsoft Docs"
description: "Learn how to use OAuth with Cross-Origin Resource Sharing to connect a Single Page Application"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: oauth-cross-origin-resource-sharing-connect-single-page-application
caps.latest.revision: 11
author: "JimDaly"
ms.author: "jdaly"
---
# Use OAuth with Cross-Origin Resource Sharing to connect a Single Page Application

You can create a Single Page Apps (SPAs) which uses JavaScript to work with Common Data Service for Apps data. To provide this, Cross-Origin Resource Sharing (CORS) is enabled so that your SPAs can bypass browser restrictions that normally prevent requests that cross domain boundaries.  
  
> [!NOTE]
>  CORS support is only provided when using the Web API. You cannot use the organization service or the deprecated organization data service.  
  
<a name="bkmk_Spas_and_same_origin_policy"></a> 
  
## SPAs and Same-Origin policy  

SPAs depend on extensive use of client-side JavaScript to create a single dynamic page which doesn't need to load new pages. Instead they use XMLHTTPRequests to retrieve data and other resources from the server. SPAs work well when the data and resources exist in the same domain as the application. But to protect access to data and resources on other domains, all modern browsers enforce a Same-Origin policy to prevent sites from using data and resources from sites on a different domain. CORS provides a way to gain access to resources on another domain. Creating a SPA to access CDS for Apps data without CORS is not a viable option.  
  
<a name="bkmk_use_cors"></a>

## Use CORS with Common Data Service for Apps 
 
The [Cross-Origin Resource Sharing specification](http://www.w3.org/TR/cors/) provides a detailed description of how to implement and use CORS. It explains all about the various headers and preflight requests that you need to apply to make CORS work. The good news is that you don't need to become an expert in CORS to use it with CDS for Apps. The server-side part has been done for you and all you need is to know how to consume it.  You don't need to understand all the inner workings of CORS to use it with CDS for Apps. Instead you can use the [Azure Active Directory Authentication Library for JavaScript](https://github.com/AzureAD/azure-activedirectory-library-for-js) (adal.js) and it will take care of much of the CORS complexity for you. Since CDS for Apps are authenticated using Azure Active Directory, ADAL.js is the supported way to authenticate SPA users.  
  
<a name="bkmk_how_adaljs_works"></a>

## How adal.js works

The core library is `adal.js`. You can access the minimized version of this library at [https://secure.aadcdn.microsoftonline-p.com/lib/1.0.0/js/adal.min.js](https://secure.aadcdn.microsoftonline-p.com/lib/1.0.0/js/adal.min.js). The Github project and documentation is at [https://github.com/AzureAD/azure-activedirectory-library-for-js](https://github.com/AzureAD/azure-activedirectory-library-for-js).  
  
The adal.js library contains the low-level capabilities to authenticate using OAuth2. Adal.js is designed so that it can be used with other frameworks, for example there is an `adal-angular.js` library that is designed to be used with the Angular framework.The way you work with this library is to set certain configuration properties and then it will wait until events occur that trigger the interaction flow. This could be simply calling the `login` function or if your application has routing behaviors, the authentication can be initiated by how the controller for that route is configured.  
  
When authentication is required, the user is taken to the sign-in page where they can enter their credentials. After they successfully authenticate, they are re-directed back to the calling page with the token information attached as a fragment (using `#`) to the URL. This allows the SPA to acquire the token and cache it in local or session storage in the browser. This means that the entire page is re-loaded after authentication, but this time the information about the authorized user is available and the application can proceed to make calls the CDS for Apps Web API or other resources.  
  
When calling the CDS for Apps Web API, you must include the token value in an Authorization header with your XMLHTPPRequest. However, because tokens have an expiration you want to be sure that it doesn't expire while people are using your SPA. Remember, entering new credentials requires that the entire content of your SPA page is transferred to the sign-in page. This would cause a very bad user experience if it were to happen while people are in the middle of doing something. In order to ensure this doesn't happen, you wrap your Web API calls within an `acquireToken` function so that the validity of the token can be checked and refreshed if necessary without taking the user to a sign-in page.  
  
<a name="bkmk_preparing_to_use_adaljs"></a>

## Preparing to use ADAL.js with a SPA

 In order to configure your SPA to work with adal.js you will need to :  
  
1.  Register your application with the Azure Active Directory tenant  
2.  Export your registered application manifest and edit it to allow OAuth2 Implicit Flow, and then import the JSON file back to your application registration.  
3.  Set configuration variables in your SPA with information from that registration.  
     You will need to include the following:  
  
    -   The URL to your CDS for Apps organization  
    -   The name of the Active Directory tenant your organization uses to authenticate  
    -   The client ID you get when you register your application  
    -   The URL to where the SPA will be deployed or debugged during development  
<!-- 
TODO:  
 The set of steps required are described in [Walkthrough: Registering and configuring SimpleSPA application with adal.js](walkthrough-registering-configuring-simplespa-application-adal-js.md).  
   -->
### See also  
<!-- 
TODO:
[Authenticate users in CDS for Apps](authenticate-users.md)   
[Use OAuth to connect to CDS for Apps web Services](connect-customer-engagement-web-services-using-oauth.md)   
[Active Directory and Claims-Based Authentication](active-directory-claims-based-authentication.md)
-->
