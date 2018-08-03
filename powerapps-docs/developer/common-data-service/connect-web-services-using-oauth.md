---
title: "Connect to Common Data Service for Apps web services using OAuth (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to connect to Dynamics 365 Customer Engagement web services using OAuth and how the ADAL API manages OAuth 2.0 authentication with the Dynamics 365 web service identity provider" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Connect to web services using OAuth

OAuth is the authentication method supported by the Common Data Service for Apps Web API, and is one of two authentication methods for the Organization Service – the other being Azure Active Directory authentication. One benefit of using OAuth is that your application can support multi-factor authentication. You can use OAuth authentication when your application connects to either the Organization service or the Discovery service.  
  
 Method calls to the web services must be authorized with the identity provider for that service endpoint. Authorization is approved when a valid              OAuth 2.0 (user) access token, issued by Azure Active Directory, is provided in the headers of the message requests.  
  
 The recommended authentication API for use with the CDS for Apps Web API is [Azure Active Directory Authentication Library (ADAL)](https://azure.microsoft.com/en-us/documentation/articles/active-directory-authentication-libraries/), which is available for a wide variety of platforms and programming languages. The ADAL API manages OAuth 2.0 authentication with the CDS for Apps web service identity provider. For more details on the actual OAuth protocol used, see [Use OAuth to Authenticate with the CRM Service](http://blogs.msdn.com/b/crm/archive/2013/12/12/use-oauth-to-authenticate-with-the-crm-service.aspx).  
 
> [!NOTE]
> You must use the ADAL 2.0 libraries. All Dynamics 365 Customer Engagement tools, assemblies, and utilities require the patterns supported by ADAL 2.0.
> The ADAL 3.0 libraries require a sign-in screen to capture user account information and do not provide for passing this account information in a headless fashion as required by Dynamics 365 Customer Engagement. 

Before you can use OAuth authentication to connect with the CDS for Apps web services, your application must first be registered with Azure Active Directory. Azure Active Directory is used to verify that your application is permitted access to the business data stored in a CDS for Apps tenant.  
  
## Authenticate using ADAL  
 Basic OAuth web service authentication using ADAL is done using just a few lines of code.  
  
```csharp  
// TODO Substitute your correct CRM root service address,   
string resource = "https://mydomain.crm.dynamics.com";  
  
// TODO Substitute your app registration values that can be obtained after you  
// register the app in Active Directory on the Microsoft Azure portal.  
string clientId = "e5cf0024-a66a-4f16-85ce-99ba97a24bb2";  
string redirectUrl = "http://localhost/SdkSample";  
  
// Authenticate the registered application with Azure Active Directory.  
AuthenticationContext authContext =   
    new AuthenticationContext("https://login.windows.net/common", false);  
AuthenticationResult result = authContext.AcquireToken(resource, clientId, new Uri(redirectUrl));  
```  
  
 The authentication context is returned using a well-known authority provider. When you don’t know the Azure Active Directory tenant associated with the CDS for Apps instance you’re calling, you can use a constant string of `https://login.windows.net/common`, which is the authority URL for a multiple tenant scenario. An alternate method to dynamically discover the authority at run time is described later in this topic.  
  
 The next line of code gets the authentication result that contains the access token you’re looking for. You can send message requests to the web service with this token.  
  
 A few more items of interest in this code are the string values used. The resource variable contains the Transport Layer Security (TLS) or Secure Sockets Layer (SSL) root address, including the domain (organization), of your CDS for Apps server. The                  `clientId` and `redirectUrl` variables contain the app registration information that is the result of registering the app with Azure Active Directory. For more information on app registration, see [Walkthrough: Register a Dynamics 365 app with Azure Active Directory](/dynamics365/customer-engagement/developer/walkthrough-register-dynamics-365-app-azure-active-directory).  
  
## Use the access token in message requests  
 Depending on the CDS for Apps API you’re using, there are two different methods to send a message request to the web services. For the Web API, you would typically send an HTTP message request. For the Organization Service, you would send a message request using the web client proxy.  
  
### HTTP message request  
 Once you have the access token, you must set the Authorization header of the message request that you are sending to the web service to the access token value and specify the token type of `Bearer`. For more information on the Authorization header, see section 14.8 of the [HTTP/1.1 protocol](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). The following code demonstrates how this is done using the                          `System.Net.Http.HttpClient` class.  
  
```csharp  
using (HttpClient httpClient = new HttpClient())  
{  
    httpClient.Timeout = new TimeSpan(0, 2, 0);  // 2 minutes  
    httpClient.DefaultRequestHeaders.Authorization =   
        new AuthenticationHeaderValue("Bearer", result.AccessToken);  
```  
  
### Web client requests

Simply set the <xref:Microsoft.Xrm.Sdk.WebServiceClient.WebProxyClient`1.HeaderToken> property value to the access token when using <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> or <xref:Microsoft.Xrm.Sdk.WebServiceClient.DiscoveryWebProxyClient> of the Organization Service.  
  
## Refresh the access token

It’s a recommended best practice to refresh the access token before each call to a CDS for Apps web service method. To refresh the access token, which is cached by ADAL, you simply call the `AcquireToken` method again using the same context.  
  
```csharp    
AuthenticationResult result = authContext.AcquireToken(resource, clientId, new Uri(redirectUrl));  
```  
  
Afterwards, you once again set the Authorization header with `result.AccessToken` when using the Web API, or the <xref:Microsoft.Xrm.Sdk.WebServiceClient.WebProxyClient`1.HeaderToken> when using the Organization Service.  
  
```csharp    
httpClient.DefaultRequestHeaders.Authorization =   
    new AuthenticationHeaderValue("Bearer", result.AccessToken);  
```  
  
## Discover the authority at run time

The authentication authority URL, and the resource URL, can be determined dynamically at run time using the following ADAL code. This is the recommended method to use as compared to the well-known authority URL shown previously in a code snippet.  
  
```csharp    
AuthenticationParameters ap = AuthenticationParameters.CreateFromResourceUrlAsync(  
                        new Uri("https://mydomain.crm.dynamics.com/api/data/")).Result;  
  
String authorityUrl = ap.Authority;  
String resourceUrl  = ap.Resource;  
```  
  
For the Web API, another way to obtain the authority URL is to send any message request to the web service specifying no access token. This is known as a         *bearer challenge*. The response can be parsed to obtain the authority URL.  
  
```csharp  
httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", "");  
```  
  
### See also  
 [Walkthrough: Register a Dynamics 365 app with Azure Active Directory](walkthrough-register-dynamics-365-app-azure-active-directory.md)   
 [Multi-Factor Authentication documentation](https://azure.microsoft.com/en-us/documentation/services/multi-factor-authentication/)   
 [OAuth 2.0](http://oauth.net/2/)
