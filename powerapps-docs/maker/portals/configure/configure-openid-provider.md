---
title: "Configure the OpenID Connect provider for Power Apps portals.  | MicrosoftDocs"
description: "Learn how to configure the OpenID Connect provider for Power Apps portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure the Open ID Connect provider for portals

[OpenID Connect](https://openid.net/connect/) external identity providers are services that conform to the [Open ID Connect specifications](https://openid.net/specs/openid-connect-core-1_0.html). OpenID Connect introduces the concept of an "ID token", which is a security token that allows the client to verify the identity of the user. The ID token also gets basic profile information about the user; commonly known as "claims".

This article explains how an identity provider&mdash;that supports OpenId Connect&mdash;can be integrated with Power Apps portals.

## Supported and unsupported authentication flows in portals

- Implicit Grant Flow
    - This flow is the default authentication method used by portals.
- Authorization Code Flow
    - Portals uses *client_secret_post* method to communicate with token endpoint of identity server.
    - *private_key_jwt* method to authenticate with token endpoint isn't supported.
- Hybrid Flow (restricted support)
    - Portals requires *id_token* to be present in the response. So, *response_type* value as *code token* isn't supported.
    - Hybrid Flow in portals follows the same flow as Implicit Grant Flow, and uses *id_token* to directly sign in the users.
- Portals doesn’t support PKCE-based techniques (Proof Key for Code Exchange) to authenticate users.

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

    > [!TIP]
    > Examples of the OpenID Connect providers for portals:
    > 
    > - [Azure AD B2C](configure-azure-ad-b2c-provider.md)
    > - [Azure AD](configure-openid-settings.md)
    > - [Azure AD with multi-tenancy](configure-openid-settings.md#enable-authentication-using-a-multi-tenant-azure-active-directory-application)

1. Enter the following site settings for portal configuration.

    ![Configure OpenID site settings](media/authentication/openid-site-settings-1.png "ConfigureOpenID site settings")

    > [!NOTE]
    > Ensure that you review&mdash;and if required, change&mdash;the default values.

    | Name | Description |
    | - | - |
    | Authority | The authority (or issuer) URL associated with the identity provider. <br> Example (Azure AD) : `https://login.microsoftonline.com/22a47203-270e-4476-a9fd-189d82e4b467/` |
    | Client ID | The ID of the application created with the identity provider and to be used with the portal. |
    | Redirect URL | The location where the identity provider will send the authentication response. <br> Example: `https://contoso-portal.powerappsportals.com/signin-openid_1` <br> **Note**: If you're using the default portal URL, you can copy and paste the **Reply URL** as shown in *Create and configure OpenID Connect provider* settings. If you're using a custom domain name, enter the URL manually. However, ensure that the value enter here is exactly the same as the **Redirect URI** value for the application in the Azure portal. |
    | Metadata address | The discovery endpoint for obtaining metadata. Common format: [Authority URL]/.well-known/openid-configuration. <br> Example (Azure AD) : `https://login.microsoftonline.com/22a47203-270e-4476-a9fd-189d82e4b467/v2.0/.well-known/openid-configuration` |
    | Scope | A space-separated list of scopes to request via the OpenID Connect scope parameter. <br> Default value: `openid` <br> Example: `openid profile email` |
    | Response type | The value for the OpenID Connect 'response_type' parameter. <br> Possible values: <ul> <li> `code` </li> <li> `code id_token` </li><li> `id_token` </li><li> `id_token token` </li><li> `code id_token token` </li> </ul> <br> Default: `code id_token` |
    | Client secret | The client secret value from the provider application. It may also be referred to as an "App Secret" or "Consumer Secret". This setting is required if the selected response type is “code”. |
    | Response mode | The value for the OpenID Connect “response_mode” parameter. The value should be  “query”  if the selected response type is “code”. Default value: ‘form_post’. |

1. Configure logout settings.

    ![Logout settings](media/authentication/openid-logout-settings.png "Logout settings")

    | Name | Description |
    | - | - |
    | External logout | Enables or disables external account sign-out. When enabled, users are redirected to the external sign-out user experience when they sign out from the portal. When disabled, users are only signed out from the portal. |
    | Post logout redirection URL | The location where the identity provider will redirect post external logout. This location should be set appropriately in the identity provider configuration. |
    | RP initiated logout | Enables / disables a relying party initiated logout. To use this setting, the external logout should be enabled first. |

1. (Optional) Configure additional settings.

    ![Additional settings](media/authentication/openid-additional-settings.png "Additional settings")

    | Name | Description
    | - | - |
    | Issuer filter | A wildcard-based filter that matches on all issuers across all tenants. <br> Example: `https://sts.windows.net/*/` |
    | Validate audience | If enabled, the audience will be validated during the token validation.  |
    | Valid audiences | Comma-separated list of audience URLs.  |
    | Validate issuers | If enabled, the issuer will be validated during token validation. |
    | Valid issuers | Comma-separated list of issuer URLs. |
    | Registration claims mapping | List of logical name-claim pairs to map claim values returned from the provider during the sign-up for the attributes of the contact record. <br> Example: `firstname=given_name,lastname=family_name` when using *Scope* as `profile` for Azure AD |
    | Login claims mapping | List of logical name-claim pairs to map claim values returned from the provider during the sign-up for the attributes of the contact record. <br> Example: `firstname=given_name,lastname=family_name` when using *Scope* as `profile` for Azure AD  |
    | Nonce lifetime | Lifetime of nonce, in minutes. Default: 10 minutes. |
    | Use token lifetime | Indicates that the authentication session lifetime (such as cookies) should match that of the authentication token. If specified, this value will override the Application Cookie Expire Timespan value in the *Authentication/ApplicationCookie/ExpireTimeSpan* site setting. |
    | Contact mapping with email | Specify whether the contacts are mapped to a corresponding email. <br> When set to *On*, a unique contact record is associated with a matching email address, assigning the external identity provider to the contact after a successful user sign-in. |

## Edit OpenID Connect provider

To edit a configured OpenID Connect provider, see [Edit a provider](use-simplified-authentication-configuration.md#edit-a-provider).

### See also

- [Example: Configure OpenID Connect for portals with Azure Active Directory](configure-openid-settings.md)
- [Frequently Asked Questions (FAQs) when using OpenID Connect in portals](configure-openid-faqs.md)
