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

# Configure Open ID Connect provider settings for portals

[OpenID Connect](https://openid.net/connect/) external identity providers are services that conform to the [Open ID Connect specifications](https://openid.net/specs/openid-connect-core-1_0.html). OpenID Connect introduces the concept of an "ID token", which is a security token that allows the client to verify the identity of the user. The ID token also gets basic profile information about the user; commonly known as "claims".

This article explains how an identity provider&mdash;that supports OpenId Connect&mdash;can be integrated with Power Apps portals.

## Supported and unsupported authentication flows in portals

- Implicit Grant Flow
    - This is the default authentication method used by portals.
- Authorization Code Flow
    - Portals uses *client_secret_post* method to communicate with token endpoint of identity server.
    - *private_key_jwt* method to authenticate with token endpoint is not supported.
- Hybrid Flow (restricted support)
    - Portals requires *id_token* to be present in the response. Hence, *response_type* value as *code token* is not supported.
    - Hybrid Flow in portals follows the same flow as Implicit Grant Flow, and uses *id_token* to directly sign in the users.
- Portals doesn’t support PKCE-based techniques (Proof Key for Code Exchange) to authenticate users.

## Examples

Integrating a provider involves locating the authority (or issuer) URL associated with the provider. A configuration URL can be determined from the authority which supplies metadata required during the authentication workflow. The provider settings are based on the properties of the [OpenIdConnectAuthenticationOptions](https://msdn.microsoft.com/library/microsoft.owin.security.openidconnect.openidconnectauthenticationoptions.aspx) class.

Examples of authority URLs are:

- [[!INCLUDE[pn-azure-active-directory](../../../includes/pn-azure-active-directory.md)]](https://msdn.microsoft.com/library/azure/mt168838.aspx): [https://login.microsoftonline.com/&lt;[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] AD Application&gt;/](https://login.microsoftonline.com/contoso.onmicrosoft.com/.well-known/openid-configuration)
- [Google](https://developers.google.com/identity/protocols/OpenIDConnect): <https://accounts.google.com/.well-known/openid-configuration>

Each OpenID Connect provider also involves registering an application (similar to that of an OAuth 2.0 provider) and obtaining a Client Id. The authority URL and the generated application Client Id are the settings required to enable external authentication between the portal and the identity provider.

Examples of the OpenID Connect providers for portals are:

- [Azure AD B2C](configure-azure-ad-b2c-provider.md)
- [Azure AD](configure-openid-settings.md)
- [Azure AD with multi-tenancy](configure-openid-settings.md#enable-authentication-using-a-multi-tenant-azure-active-directory-application)

## Configure OpenID Connect provider

Similar to all other providers, you have to sign in to [Power Apps](https://make.powerapps.com) to configure the OpenID Connect provider.

To configure OpenID Connect provider:

1. Select [Add provider](use-simplified-authentication-configuration.md#add-configure-or-delete-an-identity-provider) for your portal.

1. Select **Login provider** as **Other**.

1. Select **Protocol** as **OpenID Connect**.

1. Enter a provider name.

    ![Provider name](media/authentication/select-other-openid.png "Provider name")

1. Select **Next**.

1. Create the application and configure the settings with your identity provider.

    ![Create application](media/authentication/step-1-openid.png "Create application")

    > [!NOTE]
    > The Reply URL is used by the app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you might have a different URL than the one provided here.

1. Enter the following site settings for portal configuration.

    ![Configure OpenID site settings](media/authentication/openid-site-settings-1.png "ConfigureOpenID site settings")

    | Name | Description |
    | - | - |
    | Authority | The authority (or issuer) URL associated with the identity provider. <br> Example: `https://login.microsoftonline.com/contoso.onmicrosoft.com/` |
    | Client ID | The ID of the application created with the identity provider and to be used with the portal. |
    | Redirect URL | The location where the identity provider will send the authentication response. <br> Example: `https://portal.contoso.com/signin-saml2` |
    | Metadata address | The discovery endpoint for obtaining metadata. Common format: [Authority URL]/.well-known/openid-configuration. <br> Example: `https://login.microsoftonline.com/contoso.onmicrosoft.com/.well-known/openid-configuration` |
    | Scope | A space-separated list of permissions to request. Default value: ‘openid’.  <br> Example: `openid` |
    | Response type | The value for the OpenID Connect 'response_type' parameter. |
    | Client secret | The client secret value from the provider application. It may also be referred to as an "App Secret" or "Consumer Secret". This is required if the selected response type is “code”. |
    | Response mode | The value for the OpenID Connect “response_mode” parameter. The value should be  “query”  if the selected response type is “code”. Default value: ‘form_post’. |

1. Select **Next**.

1. Configure logout settings.

    ![Logout settings](media/authentication/openid-logout-settings.png "Logout settings")

    | Name | Description |
    | - | - |
    | External logout | Enables or disables external account sign-out. When enabled, users are redirected to the external sign-out user experience when they sign out from the portal. When disabled, users are only signed out from the portal. |
    | Post logout redirection URL | The location where the identity provider will redirect post logout.This location should also be set appropriately in the identity provider configuration. |
    | RP initiated logout | Enables / disables a relying party initiated logout.  To use this the external logout  should be enabled first. |

1. (Optional) Configure additional settings.

    ![Additional settings](media/authentication/openid-additional-settings.png "Additional settings")

    | Name | Description
    | - | - |
    | Validate audience | If enabled, the audience will be validated during the token validation.  |
    | Valid audiences | Comma-separated list of audience URLs.  |
    | Validate issuers | If enabled, the issuer will be validated during token validation. |
    | Valid issuers | Comma-separated list of Issuer URLs. |
    | Nonce lifetime | Lifetime of nonce, in minutes. Default: 10 minutes. |
    | Use token lifetime | Indicates that the authentication session lifetime (such as cookies) should match that of the authentication token. If specified, this will override the Application Cookie Ecpire Timespan value. |

1. Select **Confirm**.

## Claims to support sign-in scenarios

The data in Common Data Service and in the identity provider are not directly linked, so the data might get out of sync. The portal should have a list of claims that you want to accept from any sign-in event to update in Common Data Service. These claims can be a subset of, or equal to, the claims coming in from a sign-in scenario. This must be configured separately from sign-in claims mapping, because you might not want to overwrite some key portal attributes. The following site setting is required:

**Name**: Authentication/OpenIdConnect/[Federation-Name]/LoginClaimsMapping

**Description**: List of logical name/claim pairs to be used to map claim values to attributes in the contact record created after sign-in.

**Format**: attribute1=claim1, attribute2=claim2, attribute3=claim3

Example: <br> `firstname=<https://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname,lastname=https://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname,jobtitle=jobTitle>` 

The claim name is the CLAIM TYPE field listed next to the attribute in the sign-in policies Application claims.

### See also
[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[OAuth2 provider settings for portals](configure-oauth2-settings.md)  
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
[SAML 2.0 provider settings for portals](configure-saml2-settings.md)  

