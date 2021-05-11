---
title: "Authenticate to use the Online Management API for Microsoft Dataverse| MicrosoftDocs"
description: "Provides information about authenticating to the Online Management API to perform environment-related operations."
ms.date: 10/23/2020
ms.service: powerapps
ms.topic: conceptual
ms.assetid: c292c148-01f0-41f6-a2fe-7ed05a01a733
author: KumarVivek
ms.author: kvivek
manager: annbe
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# Authenticate to use the Online Management API

> [!NOTE]
> Effective August 26, 2020, the Online Management API is [deprecated](/power-platform/important-changes-coming##online-management-api-powershell-module-and-rest-api-are-deprecated). 

Online Management API supports OAuth 2.0 protocol for authentication. Use [Azure Active Directory (AAD)](/azure/active-directory/active-directory-whatis) to authenticate by obtaining a valid OAuth 2.0 access token, and pass it using the **Authorization** header in your requests to the Online Management API.

The recommended authentication API to use with the Online Management API is [Azure Active Directory Authentication Library (ADAL)](/azure/active-directory/develop/active-directory-authentication-libraries), which is available for a wide variety of platforms and programming languages. 

## How to authenticate?

These are the broad steps to authenticate to the Online Management API service. 

1. Register an app with Azure Active Directory to obtain *clientId* and *redirectUrl* values for your app. For information about this, see the "App registration for OAuth authentication" section in [Walkthrough: Register an app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md)

1. Specify the values obtained from step# 1 in the authentication [helper code](sample-authentication-helper.md):

    ```csharp
    // TODO: Substitute your app registration values here.
    // These values are obtained on registering your application with the 
    // Azure Active Directory.
    private static string _clientId = "<GUID>";    //e.g. "e5cf0024-a66a-4f16-85ce-99ba97a24bb2"
    private static string _redirectUrl = "<Url>";  //e.g. "app://s7cf7712-b773-4f16-92b3-34cs97a25cc7"
    ```

1. Discover authority information for Online Management API based on the service URL. For North America region, the service URL is: **https://admin.services.crm.dynamics.com**. For region-specific service URL, see [Service URL](get-started-online-management-api.md#service-url)<br /> Use Azure Active Directory challenge format to determine the authority information based on the service URL of the API.<br />We are also determining the resource for the Online Management API (different from the service URL), which will be used in the next step to acquire access token.

    ```csharp
    public static async Task<string> DiscoverAuthority(string _serviceUrl)
    {
        try
        {
            AuthenticationParameters ap = await AuthenticationParameters.CreateFromResourceUrlAsync(
                    new Uri(_serviceUrl + "/api/aad/challenge"));
            _resource = ap.Resource;
            return ap.Authority;
        }
        catch (HttpRequestException e)
        {
            throw new Exception("An HTTP request exception occurred during authority discovery.", e);
        }
        catch (Exception e)
        {
            throw e;
        }
    }
    ```
1. Use the resource you discovered in the previous step along with the client ID and redirect URL values of your client app to acquire an access token. Note that you must use the resource, and not service URL to acquire or refresh access token.

    ```csharp
    public AuthenticationResult AcquireToken()
    {
        return _authContext.AcquireToken(_resource, _clientId, new Uri(_redirectUrl),
                PromptBehavior.Always);
    }        
    ```

1. Once you have the access token, you must set the **Authorization** header of the message request to the access token value, and specify the token type as **Bearer**. Also, set the **Accept-Language** header to specify the preferred language for the response. The `SendAsync` method in the authentication sets these header values for all the message requests:

    ```csharp
    protected override Task<HttpResponseMessage> SendAsync(
                HttpRequestMessage request, System.Threading.CancellationToken cancellationToken)
    {
        // It is a best practice to refresh the access token before every message request is sent. Doing so
        // avoids having to check the expiration date/time of the token. This operation is quick.
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", _auth.AcquireToken().AccessToken);
        
        // Set the "Accept-Language" header
        request.Headers.Add("Accept-Language", "en-US");

        return base.SendAsync(request, cancellationToken);
    }
    ```

You are all set to execute messages against the Online Management API. For a sample code that demonstrates how to retrieve all Microsoft Dataverse environments in your Microsoft 365 tenant, see [Quick Start Sample: Retrieve environments in your tenant](sample-quick-start.md)


### Related Topics  

[Sample: Authentication helper for the Online Management API](sample-authentication-helper.md)

[Get started with Online Management API](get-started-online-management-api.md)

[Online Management API Reference](/rest/api/admin.services.crm.dynamics.com)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]