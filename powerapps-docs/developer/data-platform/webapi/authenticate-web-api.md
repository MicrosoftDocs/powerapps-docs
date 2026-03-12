---
title: "Authenticate to Microsoft Dataverse with the Web API"
description: "Learn how to authenticate to Microsoft Dataverse with the Web API using OAuth, PowerShell, JavaScript web resources, and MSAL.js for single-page applications."
ms.date: 03/12/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Authenticate to Microsoft Dataverse with the Web API

You must use OAuth as described in [Use OAuth with Dataverse](../authenticate-oauth.md).

The code you write to manage authentication when using the Web API depends on the type of deployment and where your code is.


## Use the Az PowerShell module Azure application

You don't need to create your own app registration by using this method. You can use the Azure AD application to request an access token.

Use the [Connect-AzAccount](/powershell/module/az.accounts/connect-azaccount) command to launch an interactive browser sign-in or initiate a device code flow. After you sign in, use the Az PowerShell module [Get-AzAccessToken](/powershell/module/az.accounts/get-azaccesstoken) command to request an access token for your Dataverse organization URI resource.

[Learn how to connect to Dataverse using PowerShell](quick-start-ps.md).
  
## Authenticate by using JavaScript in web resources

When you use the Web API with JavaScript within HTML web resources, form scripts, or ribbon commands, you don't need to include any code for authentication. In each of these cases, the application already authenticates the user and manages authentication.  

## Use the Microsoft Authentication Library for JavaScript

If you're creating a single-page application (SPA) by using JavaScript, you can use the [Microsoft Authentication Library for JavaScript (MSAL.js)](/entra/msal/javascript/) as described in [Use OAuth with Cross-Origin Resource Sharing  to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md).  
  
### See also
 
[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Use OAuth with Dataverse](../authenticate-oauth.md)<br />
[Use OAuth with Cross-Origin Resource Sharing to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
