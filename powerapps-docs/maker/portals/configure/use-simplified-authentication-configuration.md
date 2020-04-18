---
title: "Use simplified authentication and identity provider configuration (Preview) | MicrosoftDocs"
description: "Learn how to use quick, easy, and simplified portal configuration for authentication."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/17/2020
ms.author: tapanm
ms.reviewer:
---

# Simplified authentication and identity provider configuration (Preview)

Setting up authentication is a core customization in any portal. Simplified identity provider configuration in Power Apps portals provides in-app guidance for identity provider setup and abstracts setup complexities. Makers and administrators can easily configure the portal for supported identity providers.

> [!NOTE]
> **Simplified authentication and identity provider configuration** feature is in preview. To access this preview feature, you must use [Power Apps preview](https://make.preview.powerapps.com). After this preview feature is *Generally Available*, you'll be able to access it from [Power Apps](https://make.powerapps.com). You can't turn this preview feature *On* or *Off* for your portal. For more information about preview features, read [Understand experimental and preview features in Power Apps](https://docs.microsoft.com/powerapps/maker/canvas-apps/working-with-experimental-preview). 

## Overview

You can enable, disable, and configure portal identity providers from [Power Apps](https://make.preview.powerapps.com) using simplified portal authentication configuration. 

After you select an identity provider, you can then go through prompts to easily select and enter provider settings instead of setting up authentication [manually](set-authentication-identity.md).

### Authentication Settings

To begin configuring identity provider for your portal: 

1. Go to [Power Apps](https://make.preview.powerapps.com).

1. Select **Apps** from left pane:

    ![Select Apps](media/use-simplified-authentication-configuration/select-apps.png)

1. Select your portal from list of available apps.

1. Select **Settings** from top menu. You can also select **More Commands** (**...**) and then select **Settings** instead:

    ![Select Settings](media/use-simplified-authentication-configuration/select-settings.png)

1. From the settings on the right side, select **Authentication Settings**:

    ![Authentication Settings](media/use-simplified-authentication-configuration/portal-settings-right-pane.png)

You can see a list of identity providers that you can configure with Power Apps portal:

![Identity Providers](media/use-simplified-authentication-configuration/portal-authentication-settings.png)

> [!NOTE]
> Power Apps portals support multiple identity providers. However, the **Simplified authentication and identity provider configuration** feature only supports the identity providers listed above.

#### Authentication Settings from portal details

You can also view the **Identity providers** from the portal **Details**. 

To view **Identity providers** from portal details:

1. Select your portal from list of available apps.

1. Select **Details** from top menu. You can also select **More Commands** (**...**) and then select **Details** instead:

    ![Select details](media/use-simplified-authentication-configuration/select-details.png)

The details page shows you the **Identity providers** section:

![Portal details](media/use-simplified-authentication-configuration/portal-details.png)

> [!NOTE]
> Selecting **See all** from portal details takes you to the list of [*identity providers*](#authentication-settings).

## General authentication settings

You can configure the following general authentication settings by selecting the **Authentication Settings** when you view the **Identity providers**:

![General authentication settings](media/use-simplified-authentication-configuration/general-authentication-settings.png)

- **External login** - Turn [**External login**](set-authentication-identity.md#manage-external-accounts) for your portal *On* or *Off*. Setting to *Off* disables and hides external account registration and sign in.
- **Open registration** - Turn [**Open registration**](configure-portal-authentication.md#open-registration) for your portal *On* or *Off*. Setting to *Off* disables and hides external account registration.

You can also go to general authentication settings from **portal details** using **Settings** on top right in **Identity providers** section:

![General authentication settings from details](media/use-simplified-authentication-configuration/general-settings-from-details.png)

### Default identity provider

You can set any identity provider as **default**. When an identity provider is set as default, users signing into the portal aren't redirected to the portal sign in page. Instead, the signing experience always defaults to sign in with the selected provider:

![Default identity provider](media/use-simplified-authentication-configuration/set-default.png)

> [!IMPORTANT]
> If you set an identity provider as default, users won't have option to choose any other identity provider.

After you set an identity provider as default, you can then use **Remove as default** to remove the set default identity provider. If you remove an identity provider from being the default, users will be redirected to portal sign in page and can choose from the identity providers you enable.

> [!NOTE]
> You can only set **configured** identity provider as default. **Set as default** option becomes available after you configure an identity provider.

## Add, configure, or delete an identity provider

Several identity providers are added by default that you can configure. You can add additional *Azure Active Directory B2C* providers, or configure the available OAuth 2.0 providers such as LinkedIn and Microsoft.

> [!NOTE]
> - You can't change the configuration of the [**Local sign in**](configure-portal-authentication.md) and **Azure Active Directory** providers when using this interface. You can only **Enable** or **Disable** these two providers.
> - You can have only one instance of each identity provider type for OAuth 2.0, such as **Facebook**, **LinkedIn**, **Google**, **Twitter**, and **Microsoft**.

### Add or configure provider

To add an identity provider, select **Add provider** from **Authentication Settings**:

![Add provider from settings](media/use-simplified-authentication-configuration/add-provider-from-settings.png)

You can also select **Add provider** from **portal details** instead:

![Add provider from details](media/use-simplified-authentication-configuration/add-provider-from-details.png)

You can select from the available list of providers, enter a name, and then select **Next** to configure the provider settings:

![Add new provider](media/use-simplified-authentication-configuration/add-provider.png)

To configure a provider, select **Click to Configure** or use **More Commands** (**...**) and then select **Configure**:

![Configure provider](media/use-simplified-authentication-configuration/configure-provider.png)

> [!NOTE]
> You can use **Add provider** or **Configure** to add/configure a provider for the first time. After you configure a provider, you can edit it.

The configuration steps after you select **Next** depend on the identity provider type you select. For example, the *Azure Active Directory B2C* configuration is different from how you setup *LinkedIn*. Refer to the provider-specific sections later in this article to configure provider of your choice.

### Edit provider

After you add/configure a provider, you can see the provider in **Enabled** state on portal settings or details.

To edit a provider, select a configured provider, select **More Commands** (**...**) and then select **Edit Configuration**:

![Edit provider](media/use-simplified-authentication-configuration/edit-provider.png)

Refer to the provider-specific sections later in this article to edit provider setting for the provider type you selected.

### Delete provider

To delete an identity provider, select **More Commands** (**...**) and then select **Delete**:

![Delete provider](media/use-simplified-authentication-configuration/delete-provider.png)

Deleting a provider deletes your provider configuration for the selected provider type, and the provider becomes available again for configuration.

> [!NOTE]
> When you delete a provider, only the portal configuration for the provider is deleted. For example, if you delete **LinkedIn** provider, your **LinkedIn** app and app configuration remains intact. Similarly, if you delete an **Azure Active Directory B2C** provider, only portal configuration gets deleted. The Azure tenant configuration for this provider doesn't change.

## Configure Azure Active Directory B2C provider

### Step 1 - Configure Azure Active Directory B2C application

![Configure AD B2C app](media/use-simplified-authentication-configuration/configure-ad-b2c-step1.png)

To use Azure AD B2C as an identity provider, you must create and configure Azure AD B2C tenant. And then, [register an application](https://docs.microsoft.com/azure/active-directory-b2c/tutorial-register-applications?tabs=applications#register-a-web-application) in your tenant.

For more details, read [create and configure Azure AD B2C application](azure-ad-b2c.md#use-azure-ad-b2c-as-an-identity-provider-for-your-portal).

### Step 2 - Configure site settings

Configure site settings and password reset policy for your Azure AD B2C provider:

![Configure site settings](media/use-simplified-authentication-configuration/configure-ad-b2c-step2.png)

- **Authority** - The issuer URL defined in the metadata of the sign up & sign in policy user flow.​
- **Client ID​** - The ID associated with the application created in Azure Active Directory B2C tenant to be used with the portal.​
- **Redirect URI** - The location where Azure AD B2C will send an authentication response.

#### Password resets

- **Default policy ID** - ID of the sign in or sign up user flow created in Azure Active Directory B2C.​

- **Password reset policy ID** - ID of the password reset user flow created in Azure Active Directory B2C.​

- **Valid issuers** - A comma-delimited list of issuers that includes the issuer of the sign up or sign in user flow, and the issuer of the password reset user flow.

For a complete list of site settings, read [related site settings](azure-ad-b2c.md#related-site-settings).

### Step 3 - Configure additional settings

Third step to configure Azure AD B2C identity provider is the optional additional settings:

![Configure additional settings](media/use-simplified-authentication-configuration/configure-ad-b2c-step3.png)

- **Registration claims mapping​** - List of logical name/claim pairs to be used to map claim values returned from AD B2C created during sign up to the attributes in the contact record. Enter the values in the following format: ```attribute1=claim1,attribute2=claim2,attribute3=claim3​```
- **Login claims mapping** - List of logical name/claim pairs to be used to map claim values returned from AD B2C after sign in to the attributes in the contact record. Enter the values in the following format: ```attribute1=claim1,attribute2=claim2,attribute3=claim3​```
- **External logout** - Enables or disables federated sign out. When set to true, users are redirected to the federated sign out user experience when they sign out from the portal. When set to false, users are only signed out from the portal.
- **Contact mapping with email** - Specify whether contacts are mapped to a corresponding email.  When set to true, this setting associates a unique contact record with a matching email address, and then automatically assigns the external identity provider to the contact after a successful user sign in.​- **Registration Enabled**​ - Enables or disables the registration requirement for the existing identity provider. When disabled, the user is denied registration with an error if no contact record exists for the user. When enabled, user registration is allowed for a new user only if the Site Setting Authentication/Registration/Enabled is set to true.​
- **Post Logout Redirect Uri** - URL within the portal that the user is redirected to after sign out.

Select **Confirm** to view a summary of your configuration and complete the identity configuration.

For more information about claims mapping, read [Azure AD B2C claims mappings scenarios](azure-ad-b2c.md#claims-mapping).

For more information about configuring Azure AD B2C identity provider, read [Azure AD B2C provider settings for portals](azure-ad-b2c.md#customize-the--ad-b2c-user-interface).

## Configure Facebook provider

![Configure Facebook app](media/use-simplified-authentication-configuration/configure-facebook.png)

To use [Facebook](https://developers.facebook.com) as an identity provider, you need to create an app in Facebook with a redirect URL.

The Redirect URL is used by the Facebook app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you may have a different URL than the one provided here.​

**Portal site settings** for Facebook:

- **Client ID** - Unique app ID generated by Facebook for your app.​
- **Client Secret** -  App secret for your Facebook app.​

To configure **Additional settings** for Facebook, read [configure additional settings for OAuth 2 providers](#configure-additional-settings-for-oauth-2-providers).

For more information about configuring OAuth 2 providers, see [OAuth 2 provider settings for portals](configure-oauth2-settings.md).

## Configure LinkedIn provider

![Configure LinkedIn app](media/use-simplified-authentication-configuration/configure-linkedin.png)

To use [LinkedIn](https://www.linkedin.com/developers/apps) as an identity provider, you need to create an app in LinkedIn with a redirect URL.

The Redirect URL is used by the LinkedIn app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you may have a different URL than the one provided here.​

**Portal site settings** for LinkedIn:

- **Client ID** - Unique app ID generated by LinkedIn for your app.​
- **Client Secret** -  App secret for your LinkedIn app.​

To configure **Additional settings** for LinkedIn, read [configure additional settings for OAuth 2 providers](#configure-additional-settings-for-oauth-2-providers).

For more information about configuring OAuth 2 providers, see [OAuth 2 provider settings for portals](configure-oauth2-settings.md).

## Configure Google provider

![Configure Google app](media/use-simplified-authentication-configuration/configure-google.png)

To use [Google](https://console.developers.google.com/) as an identity provider, you need to create an app in Google with a redirect URL.

The Redirect URL is used by the Google app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you may have a different URL than the one provided here.​

**Portal site settings** for Google:

- **Client ID** - Unique app ID generated by Google for your app.​
- **Client Secret** -   Client secret generated by Google for your app.

To configure **Additional settings** for Google, read [configure additional settings for OAuth 2 providers](#configure-additional-settings-for-oauth-2-providers).

For more information about configuring OAuth 2 providers, see [OAuth 2 provider settings for portals](configure-oauth2-settings.md).

## Configure Twitter provider

![Configure Twitter app](media/use-simplified-authentication-configuration/configure-twitter.png)

To use [Twitter](https://developer.twitter.com/apps) as an identity provider, you need to create an app in Twitter with a redirect URL.

The Redirect URL is used by the Twitter app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you may have a different URL than the one provided here.​

**Portal site settings** for Twitter:

- **Client ID** - Unique app ID generated by Twitter for your app.​
- **Client Secret** -   Client secret generated by Twitter for your app.

To configure **Additional settings** for Twitter, read [configure additional settings for OAuth 2 providers](#configure-additional-settings-for-oauth-2-providers).

For more information about configuring OAuth 2 providers, see [OAuth 2 provider settings for portals](configure-oauth2-settings.md).

## Configure Microsoft provider

![Configure Microsoft app](media/use-simplified-authentication-configuration/configure-microsoft.png)

To use [Microsoft](https://aka.ms/AppRegistrations) as an identity provider, you need to create an app in Twitter with a redirect URL.

The Redirect URL is used by the Microsoft app to redirect users to the portal after the authentication succeeds. If your portal uses a custom domain name, you may have a different URL than the one provided here.​

**Portal site settings** for Microsoft:

- **Client ID** - Unique app ID generated by Microsoft for your app.​
- **Client Secret** -   Client secret generated by Microsoft for your app.

To configure **Additional settings** for Microsoft, read [configure additional settings for OAuth 2 providers](#configure-additional-settings-for-oauth-2-providers).

For more information about configuring OAuth 2 providers, see [OAuth 2 provider settings for portals](configure-oauth2-settings.md).

## Configure additional settings for OAuth 2 providers

Applies to authentication settings for **Facebook**, **Twitter**, **Microsoft**, **LinkedIn, and **Google**:

![Configure additional settings](media/use-simplified-authentication-configuration/additional-oauth-settings.png)

- **Authentication type** - The OWIN authentication middleware type:  [AuthenticationOptions.AuthenticationType](https://docs.microsoft.com/previous-versions/aspnet/mt152183(v=vs.113)?redirectedfrom=MSDN). For example, https://sts.windows.net/contoso.onmicrosoft.com/.
- **Authentication mode** - The OWIN authentication middleware mode:  [AuthenticationOptions.AuthenticationMode](https://docs.microsoft.com/previous-versions/aspnet/mt152179(v=vs.113)?redirectedfrom=MSDN).
- **Backchannel timeout** - Timeout value in milliseconds for back channel communications: [MicrosoftAccountAuthenticationOptions.BackchannelTimeout](https://docs.microsoft.com/previous-versions/aspnet/mt174421(v=vs.113)?redirectedfrom=MSDN).
- **Callback path** - The request path within the application's base path where the user-agent will be returned: [MicrosoftAccountAuthenticationOptions.CallbackPath](https://docs.microsoft.com/previous-versions/aspnet/mt174433(v=vs.113)?redirectedfrom=MSDN).​
- **Sign in As authentication type** - The name of another authentication middleware which will be responsible for actually issuing a user Claims Identity: [MicrosoftAccountAuthenticationOptions.SignInAsAuthenticationType](https://docs.microsoft.com/previous-versions/aspnet/mt174430(v=vs.113)?redirectedfrom=MSDN).​
- **Scope** - A comma separated list of permissions to request: [MicrosoftAccountAuthenticationOptions.Scope](https://docs.microsoft.com/previous-versions/aspnet/mt174435(v=vs.113)?redirectedfrom=MSDN).​
- ​**Registration Enabled**​ - Enables or disables the registration requirement for the existing identity provider. When disabled, the user is denied registration with an error if no contact record exists for the user. When enabled, user registration is allowed for a new user only if the Site Setting Authentication/Registration/Enabled is set to true.​

For more information, read [OAuth2 site settings](configure-oauth2-settings.md#create-site-settings-by-using-oauth2).

### See also

- [Set authentication identity for a portal](set-authentication-identity.md)
- [Configure Azure AD B2C provider settings](azure-ad-b2c.md)
- [Configure OAuth2 provider settings](configure-oauth2-settings.md)
