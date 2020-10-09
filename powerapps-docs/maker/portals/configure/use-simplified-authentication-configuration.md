---
title: "Get started with configuring the authentication your portal authentication using different identity providers. | MicrosoftDocs"
description: "Learn how to configure the authentication your portal authentication using different identity providers."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---


# Get started with configuring the authentication your portal

Setting up authentication is a core customization in any portal. Simplified identity provider configuration in Power Apps portals provides in-app guidance for identity provider setup and abstracts setup complexities. Makers and administrators can easily configure the portal for supported identity providers.

## Overview

You can enable, disable, and configure portal identity providers from [Power Apps](https://make.powerapps.com) by using simplified portal authentication configuration. After you select an identity provider, you can then follow prompts to easily enter the provider settings.

### Authentication Settings

To begin configuring an identity provider for your portal:

1. Go to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation pane.

    ![Select Apps](media/use-simplified-authentication-configuration/select-apps.png "Select Apps")

1. Select your portal from the list of available apps.

1. Select **Settings** from the top menu. You can also select **More Commands** (**...**), and then select **Settings**.

    ![Select Settings](media/use-simplified-authentication-configuration/select-settings.png "Select Settings")

1. From the settings on the right side of your workspace, select **Authentication Settings**.

    ![Authentication Settings](media/use-simplified-authentication-configuration/portal-settings-right-pane.png "Authentication Settings")

You'll see a list of identity providers that you can configure.

![Identity providers](media/use-simplified-authentication-configuration/portal-authentication-settings.png "Identity providers")

#### Authentication settings from the portal details page

You can also view the identity providers from the portal details page.

1. Select your portal from the list of available apps.

1. Select **Details** from top menu. You can also select **More Commands** (**...**) and then select **Details**.

    ![Select details](media/use-simplified-authentication-configuration/select-details.png "Select details")

The details page displays the **Identity providers** section.

![Portal details](media/use-simplified-authentication-configuration/portal-details.png "Portal details")

> [!NOTE]
> Selecting **See all** from the portal details page takes you to the complete list of identity providers.

## General authentication settings

You can configure the following general authentication settings by selecting **Authentication Settings** on the **Identity providers** page.

![General authentication settings](media/authentication/general-authentication-settings.png "General authentication settings")

- **External login** - External authentication is provided by the ASP.NET Identity API. In this case, account credentials and password management are handled by third-party identity providers. For example, Facebook, LinkedIn, Google, Twitter, and Microsoft. Users sign up for access to the portal by selecting an external identity to register with the portal. After it's registered, an external identity has access to the same features as a local account. See [Manage external accounts](set-authentication-identity.md#manage-external-accounts) for related site settings. <br> When set to **Off**, disables and hides external account registration and sign-in.

- **[Open registration](configure-portal-authentication.md#open-registration)** - Enables or disables the sign-up registration form for creating new local users. The sign-up form allows any anonymous user to visit the portal and create a new user account. <br> When set to **Off**, disables and hides new user account registration.

- **Require unique email** - Specifies whether a unique email address is needed for validating a new user during sign-up. When set to **On**, may cause sign up attempts to fail if a user provides an email address already present in a contact record. <br> When set to **Off**, an existing contact email address is used to sign up if it matches with the user provided email address.

You can also go to general authentication settings from the portal details page by selecting **Settings** in the upper-right corner of the **Identity providers** section.

![General authentication settings from the details page](media/use-simplified-authentication-configuration/general-settings-from-details.png "General authentication settings from the details page")

### Default identity provider

You can set any identity provider as the default. When an identity provider is set as the default, users signing in to the portal aren't redirected to the portal sign-in page. Instead, the sign-in experience always defaults to signing in by using the selected provider.

![Default identity provider](media/use-simplified-authentication-configuration/set-default.png "Default identity provider")

> [!IMPORTANT]
> If you set an identity provider as the default, users won't have the option to choose any other identity provider.

After you set an identity provider as the default, you can select **Remove as default** to remove it as the default. If you remove an identity provider from being the default, users will be redirected to the portal sign-in page and can choose from the identity providers you've enabled.

> [!NOTE]
> You can only set a configured identity provider as the default. The **Set as default** option becomes available after you configure an identity provider.

## Add, configure, or delete an identity provider

Several identity providers are added by default that you can configure. You can add additional Azure Active Directory (Azure AD) B2C providers, or configure the available OAuth 2.0 providers such as LinkedIn and Microsoft.

> [!NOTE]
> - You can't change the configuration of the **Local sign in** and **Azure Active Directory** providers when using this interface.
> - You can have only one instance of each identity provider type for OAuth 2.0, such as **Facebook**, **LinkedIn**, **Google**, **Twitter**, and **Microsoft**.
> - Updates to identity provider configuration might take a few minutes to be reflected on the portal. To apply your changes immediately, you can [restart the portal](../admin/admin-overview.md#open-power-apps-portals-admin-center).

### Add or configure a provider

To add an identity provider, select **Add provider** from **Authentication Settings**.

![Add a provider from settings](media/use-simplified-authentication-configuration/add-provider-from-settings.png "Add a provider from settings")

> [!TIP]
> You can also select **Add provider** from the [portal details](#authentication-settings-from-the-portal-details-page).

Select from the available list of providers, enter a name, and then select **Next** to configure the provider settings.

![Add a new provider](media/use-simplified-authentication-configuration/add-provider.png "Add a new provider")

> [!NOTE]
> The **Provider name** you enter here is displayed on the sign-in page for users as the text on the button they use when selecting this provider.

To configure a provider, select **Configure** (or select **More Commands** (**...**), and then select **Configure**).

![Configure a provider](media/use-simplified-authentication-configuration/configure-provider.png "Configure a provider")

> [!NOTE]
> You can use **Add provider** or **Configure** to add or configure a provider for the first time. After you configure a provider, you can edit it. You can also select the provider name hyperlink to open the configuration options quickly.

The configuration steps after you select **Next** depend on the type of identity provider you select. For example, the Azure Active Directory B2C configuration is different from how you set up LinkedIn. Here's a list of providers and protocols that you can select from.

| Available providers | Available protocols | Description |
| - | - | - |
| Azure Active Directory B2C | OpenID Connect | Allows configuration of Azure AD B2C for authentication in portals using OpenID Connect protocol. <br> More information: [Configure the Azure AD B2C provider](configure-azure-ad-b2c-provider.md) |
| Facebook | OAuth 2.0 | Allows configuration of Facebook as the authentication provider in portals using OAuth 2.0 protocol. <br> More information: [Configure Facebook provider](configure-oauth2-facebook.md) |
| LinkedIn | OAuth 2.0 | Allows configuration of LinkedIn as the authentication provider in portals using OAuth 2.0 protocol. <br> More information: [Configure LinkedIn provider](configure-oauth2-linkedin.md) |
| Google | OAuth 2.0 | Allows configuration of Google as the authentication provider in portals using OAuth 2.0 protocol. <br> More information: [Configure Google provider](configure-oauth2-google.md) |
| Twitter | OAuth 2.0 | Allows configuration of Twitter as the authentication provider in portals using OAuth 2.0 protocol. <br> More information: [Configure Twitter provider](configure-oauth2-twitter.md) |
| Microsoft | OAuth 2.0 | Allows configuration of Microsoft as the authentication provider in portals using OAuth 2.0 protocol. <br> More information: [Configure Microsoft provider](configure-oauth2-microsoft.md) |
| Other | OpenID Connect | Allows configuration of any provider that conforms to the [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) protocol specifications. <br> Examples: [Configure Azure AD provider with OpenID Connect](configure-openid-settings.md), [Configure Azure AD B2C provider with OpenID Connect](configure-azure-ad-b2c-provider.md) |
| Other | SAML 2.0 | Allows configuration of any provider that conforms to the SAML 2.0 protocol specifications. <br> Examples: [Configure Azure AD provider with SAML 2.0](configure-saml2-settings-azure-ad.md), [Configure AD FS with SAML 2.0](configure-saml2-settings.md) |
| Other | WS-Federation | Allows configuration of any provider that conforms to the WS-Federation protocol specifications. <br> Examples: [Configure Azure AD with WS-Federation](configure-ws-federation-settings-azure-ad.md), [Configure Azure AD FS with WS-Federation](configure-ws-federation-settings.md) |

### Edit a provider

After you add and configure a provider, you can see the provider in the **Enabled** state on portal settings or details pages.

To edit a provider you've configured, select it, select **More Commands** (**...**), and then select **Edit configuration**.

![Edit a provider](media/use-simplified-authentication-configuration/edit-provider.png "Edit a provider")

Refer to the provider-specific sections later in this article to edit settings for the provider type you selected.

### Delete a provider

To delete an identity provider, select **More Commands** (**...**), and then select **Delete**.

![Delete a provider](media/use-simplified-authentication-configuration/delete-provider.png "Delete a provider")

Deleting a provider deletes your provider configuration for the selected provider type, and the provider becomes available again for configuration.

> [!NOTE]
> When you delete a provider, only the portal configuration for the provider is deleted. For example, if you delete the LinkedIn provider, your LinkedIn app and app configuration remain intact. Similarly, if you delete an Azure Active Directory B2C provider, only the portal configuration is deleted; the Azure tenant configuration for this provider won't change.

### Effects of the deleted and recreated portal

If you delete and recreate your portal, the users may receive the following error when signing in. When this issue happens, update the portal's identity provider configuration correctly.

`Sorry, but we're having trouble signing you in.`

`AADSTS700016: Application with identifier 'https://contoso.powerappsportals.com/' was not found in the directory 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'. This can happen if the application has not been installed by the administrator of the tenant or consented to by any user in the tenant. You may have sent your authentication request to the wrong tenant.`

### See also

- [Configure Azure AD B2C](configure-azure-ad-b2c-provider.md)
- [Configure different OAuth 2.0 providers](configure-oauth2-provider.md)
- [Configure OpenID Connect provider](configure-openid-provider.md)
- [Configure SAML 2.0 provider](configure-saml2-provider.md)
- [Configure WS-FED provider](configure-ws-federation-provider.md)
- [Microsoft Learn: Authentication and user management in Power Apps portals](https://docs.microsoft.com/learn/modules/authentication-user-management/)
