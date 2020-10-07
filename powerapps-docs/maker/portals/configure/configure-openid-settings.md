---
title: "Configure OpenID Connect provider settings for a portal  | MicrosoftDocs"
description: "Instructions to add and configure OpenID Connect provider settings for a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: sandhan
ms.reviewer: tapanm
---

# OpenID settings for [!INCLUDE[pn-azure-active-directory](../../../includes/pn-azure-active-directory.md)]

In this article, you'll learn about configuring OpenID Connect provider for portals with Azure Active Directory, and multi-tenant Azure AD.

> [!NOTE]
> Portals isn't limited to only Azure AD, multi-tenant Azure AD, or Azure AD B2C as the OpenID Connect providers. You can use any other provider that confirms to the OpenID Connect specifications with portals.

Configuration of Azure AD as the OpenID Connect provider involves the following stages:

1. [Add OpenID Connect provider](#add-openid-connect-provider-for-azure-ad)
1. [Configure app registrations on Azure portal](#configure-app-registration-on-azure-portal)
1. [Configure site settings](#configure-site-settings)

The next sections explain each stage in detail.

## Add OpenID Connect provider for Azure AD

1. Select [Add provider](use-simplified-authentication-configuration.md#add-configure-or-delete-an-identity-provider) for your portal.

1. Select **Login provider** as **Other**.

1. Select **Protocol** as **OpenID Connect**.

1. Enter a provider name.

    ![Provider name](media/authentication/select-other-openid.png "Provider name")

1. Select **Next**.

## Configure app registration on Azure portal

Create the application and configure the settings with your identity provider.

![Create application](media/authentication/step-1-openid.png "Create application")

> [!NOTE]
> The Reply URL is used by the app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you might have a different URL than the one provided here.

## Configure site settings

Enter the following site settings for portal configuration.

![Configure OpenID site settings](media/authentication/openid-site-settings-1.png "ConfigureOpenID site settings")



1. Under the **Applications** menu of the directory, select **Add**.
2. Choose **Add an application my organization is developing**.
3. Specify a custom **name** for the application and choose the type **web application and/or web API**.
4. For the **Sign-On URL** and the **App ID URI**, specify the URL of the portal for both fields https://portal.contoso.com/
5. At this point, a new application is created. Navigate to the **Configure** section in the menu.

    Under the **single sign-on** section, update the first **Reply URL** entry to include a path in the URL: https://portal.contoso.com/signin-azure-ad. This corresponds to the **RedirectUri** site setting value

6. Under the **properties** section, locate the **client ID** field. This corresponds to the **ClientId** site setting value.
7. In the footer menu, select **View Endpoints** and note the **Federation Metadata Document** field

The left portion of the URL is the **Authority** value and is in one of the following formats:

- https://login.microsoftonline.com/01234567-89ab-cdef-0123-456789abcdef/
- https://login.microsoftonline.com/contoso.onmicrosoft.com/

To get the service configuration URL, replace the FederationMetadata/2007-06/FederationMetadata.xml path tail with the path .well-known/openid-configuration. For instance,   <https://login.microsoftonline.com/contoso.onmicrosoft.com/.well-known/openid-configuration>

This corresponds to the **MetadataAddress** site setting value.

### Related site settings

Apply portal site settings referencing the above application.

> [!Note]
> A standard [!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] AD configuration only uses the following settings (with example values):                                 
> - Authentication/OpenIdConnect/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD/Authority - <https://login.microsoftonline.com/01234567-89ab-cdef-0123-456789abcdef/>                                                    
> - Authentication/OpenIdConnect/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD/ClientId - fedcba98-7654-3210-fedc-ba9876543210                                      
>   The Client ID and the authority URL do not contain the same value and should be retrieved separately.           
> - Authentication/OpenIdConnect/[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD/RedirectUri - https://portal.contoso.com/signin-azure-ad
 
Multiple identity providers can be configured by substituting a label for the \[provider\] tag. Each unique label forms a group of settings related to an identity provider. Examples: [!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)]AD, MyIdP


|                          Site Setting Name                           |                                                                                                                                                                                                         Description                                                                                                                                                                                                          |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           Authentication/Registration/ExternalLoginEnabled           |                                                                                                                                                                         Enables or disables external account sign-in and registration. Default: true                                                                                                                                                                         |
|         Authentication/OpenIdConnect/\[provider\]/Authority          |                                               Required. The Authority to use when making OpenIdConnect calls. <br> Example: `https://login.microsoftonline.com/contoso.onmicrosoft.com/`                                                |
|      Authentication/OpenIdConnect/\[provider\]/MetadataAddress       | The discovery endpoint for obtaining metadata. Commonly ending with the path:/.well-known/openid-configuration . <br> Example: `https://login.microsoftonline.com/contoso.onmicrosoft.com/.well-known/openid-configuration` |
|     Authentication/OpenIdConnect/\[provider\]/AuthenticationType     |                                   The OWIN authentication middleware type. Specify the value of the issuer in the service configuration metadata. <br> Example: `https://sts.windows.net/contoso.onmicrosoft.com/`                                   |
|          Authentication/OpenIdConnect/\[provider\]/ClientId          |                                                  Required. The client ID value from the provider application. <br> It may also be referred to as an "App ID" or "Consumer Key".                                                   |
|        Authentication/OpenIdConnect/\[provider\]/ClientSecret        |                                              The client secret value from the provider application. <br> It may also be referred to as an "App Secret" or "Consumer Secret".                                              |
|        Authentication/OpenIdConnect/\[provider\]/RedirectUri         |                                                        Recommended. The AD FS WS-Federation passive endpoint. <br> Example: https://portal.contoso.com/signin-saml2.                                                        |
|          Authentication/OpenIdConnect/\[provider\]/Caption           |                                                              Recommended. The text that the user can display on a sign in user interface. Default: \[provider\].                                                               |
|          Authentication/OpenIdConnect/\[provider\]/Resource          |                                                                                                       The 'resource'.                                                                                                        |
|        Authentication/OpenIdConnect/\[provider\]/ResponseType        |                                                                                                The 'response\_type'.                                                                                                 |
|           Authentication/OpenIdConnect/\[provider\]/Scope            |                                                                                A space separated list of permissions to request. Default: openid.                                                                                  |
|        Authentication/OpenIdConnect/\[provider\]/CallbackPath        |                      An optional constrained path on which to process the authentication callback. <br> If not provided and RedirectUri is available, this value will be generated from RedirectUri.                       |
|     Authentication/OpenIdConnect/\[provider\]/BackchannelTimeout     |                                                                Timeout value for back channel communications. <br> Example: 00:05:00 (5 mins).                                                               |
| Authentication/OpenIdConnect/\[provider\]/RefreshOnIssuerKeyNotFound |                                      Determines whether a metadata refresh should be attempted after a SecurityTokenSignatureKeyNotFoundException.                                       |
|      Authentication/OpenIdConnect/\[provider\]/UseTokenLifetime      |                                               Indicates that the authentication session lifetime (for example, cookies) should match that of the authentication token.                                              |
|     Authentication/OpenIdConnect/\[provider\]/AuthenticationMode     |                                                                                                     The OWIN authentication middleware mode.                                                                                                   |
| Authentication/OpenIdConnect/\[provider\]/SignInAsAuthenticationType |                                                   The AuthenticationType used when creating the System.Security.Claims.ClaimsIdentity.                                                  |
|   Authentication/OpenIdConnect/\[provider\]/PostLogoutRedirectUri    |                                                                                 The 'post\_logout\_redirect\_uri'.                                                                               |
|       Authentication/OpenIdConnect/\[provider\]/ValidAudiences       |                                                                                                  Comma-separated list of audience URLs.                                                                                                 |
|        Authentication/OpenIdConnect/\[provider\]/ValidIssuers        |                                                                                                       Comma-separated list of issuer URLs.                                                                                                      |
|         Authentication/OpenIdConnect/\[provider\]/ClockSkew          |                                                                                                                                                                                        The clock skew to apply when validating times.                                                                                                                                                                                        |
|       Authentication/OpenIdConnect/\[provider\]/NameClaimType        |                                                                                                                                                                              The claim type used by the ClaimsIdentity to store the name claim.                                                                                                                                                                              |
|       Authentication/OpenIdConnect/\[provider\]/RoleClaimType        |                                                                                                                                                                              The claim type used by the ClaimsIdentity to store the role claim.                                                                                                                                                                              |
|   Authentication/OpenIdConnect/\[provider\]/RequireExpirationTime    |                                                                                                                                                                              A value indicating whether tokens must have an 'expiration' value.                                                                                                                                                                              |
|    Authentication/OpenIdConnect/\[provider\]/RequireSignedTokens     |                                                                                                                               A value indicating whether a System.IdentityModel.Tokens.SecurityToken xmlns=<https://ddue.schemas.microsoft.com/authoring/2003/5> can be valid if not signed.                                                                                                                                |
|      Authentication/OpenIdConnect/\[provider\]/SaveSigninToken       |                                                                                                                                                                        A Boolean to control if the original token is saved when a session is created.                                                                                                                                                                        |
|       Authentication/OpenIdConnect/\[provider\]/ValidateActor        |                                                                                                                                                            A value indicating whether the System.IdentityModel.Tokens.JwtSecurityToken.Actor should be validated.                                                                                                                                                            |
|      Authentication/OpenIdConnect/\[provider\]/ValidateAudience      |                                                                                                                                                                       A Boolean to control if the audience will be validated during token validation.                                                                                                                                                                        |
|       Authentication/OpenIdConnect/\[provider\]/ValidateIssuer       |                                                                                                                                                                        A Boolean to control if the issuer will be validated during token validation.                                                                                                                                                                         |
|      Authentication/OpenIdConnect/\[provider\]/ValidateLifetime      |                                                                                                                                                                       A Boolean to control if the lifetime will be validated during token validation.                                                                                                                                                                        |
|  Authentication/OpenIdConnect/\[provider\]/ValidateIssuerSigningKey  |                                                                                                                  A Boolean that controls if validation of the System.IdentityModel.Tokens.SecurityKey that signed the securityToken xmlns=<https://ddue.schemas.microsoft.com/authoring/2003/5> is called.                                                                                                                  |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                              |


## Enable authentication using a multi-tenant Azure Active Directory application

You can configure your portal to accept [!include[](../../../includes/pn-azure-active-directory.md)] users from any tenant in [!include[](../../../includes/pn-azure-shortest.md)] and not just a specific tenant by using the multi-tenant application registered in [!include[](../../../includes/pn-azure-active-directory.md)]. To enable multi-tenancy, [update the application registration](https://docs.microsoft.com/azure/active-directory/develop/howto-convert-app-to-be-multi-tenant#update-registration-to-be-multi-tenant) in the [!include[](../../../includes/pn-azure-active-directory.md)] application.

### Related site settings

You can create or configure the additional **Issue Filter** site setting in portals to support authentication against [!include[](../../../includes/pn-azure-active-directory.md)] using a multi-tenanted application:

|Site Setting Name    |Description   |
|---|---|
|Authentication/OpenIdConnect/[provider]/IssuerFilter   |A wildcard-based filter that matches on all issuers across all tenants. In most cases, use the value: `https://sts.windows.net/*/`   |
