---
title: "Configure OAuth2 provider settings for a portal  | MicrosoftDocs"
description: "Instructions to add and configure OAuth2 provider settings for a portal."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 01/17/2020
ms.author: tapanm
ms.reviewer:
---

# Configure OAuth2 provider settings for portals

The OAuth 2.0 based external identity providers involve registering an "application" with a third-party service to obtain a "client ID" and "client secret" pair. Often this application requires specifying a redirect URL that allows the identity provider to send users back to the portal (relying party). The client ID and client secret are configured as portal site settings in order to establish a secure connection from relying party to identity provider. The settings are based on the properties of the [[!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)]AccountAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.aspx), [TwitterAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.twitter.twitterauthenticationoptions.aspx), [FacebookAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.facebook.facebookauthenticationoptions.aspx), and [GoogleOAuth2AuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.google.googleoauth2authenticationoptions.aspx) classes.  

The supported providers are:

- [!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)] Account
- Twitter
- Facebook
- Google
- LinkedIn
- Yahoo

## Create OAuth applications

In general, if an OAuth provider uses app settings that require a redirect URI value, specify <https://portal.contoso.com/or> https://portal.contoso.com/signin-\[provider\] depending on how the provider performs redirect URI validation (some providers require the full URL path to be specified along with the domain name). Substitute the name of the provider in place of \[provider\] in the redirect URI.

### Google

> [!NOTE]
> [Google legacy API](https://developers.google.com/people/legacy) and [Google+ API](https://developers.google.com/people/legacy) are deprecated. We strongly recommend that existing callers migrate to [Google People API](https://developers.google.com/people).

Following these steps to configure your Power Apps portal with [Google OAuth2 API Credentials](https://developers.google.com/accounts/docs/OpenIDConnect#appsetup) for user authentication.

1. Open [Google Developers Console](https://console.developers.google.com/).  
1. Create an API project or open an existing project.
1. Select **ENABLE APIS AND SERVICES**.
1. Search and enable API **Google People API**.
1. Select **Credentials** on left navigation menu.
1. Select **CONFIGURE CONSENT SCREEN**.
1. Select **External** user type.
1. Select **Create**.
1. Type **Application name** and upload an image for logo if required.
1. Select appropriate **Support email**.
1. Type **powerappsportals.com** as the top level domain in **Authorized domains**. Use **microsoftcrmportals.com** if you have not [updated your Power Apps portal domain name](../admin/update-portal-domain.md). You can also type a [custom domain name](../admin/add-custom-domain.md) if you have configured. 
1. Provide links for home page, privacy policy and terms of service as required. 
1. Select **Save**.
1. Select **Credentials** from left navigation menu.
1. Select **OAuth client ID** from the **Create credentials** drop down menu.
1. Select application type as **Web application**.
1. Type **Name** for the OAuth Client ID.
1. Type your Power Apps portal URL in **Authorized domains** list.
1. Type **Authorized redirect URIs** as the Power Apps portal URL followed by **/signin-google**. For example, if portal URL is https://contoso.powerappsportals.com, authorized redirect URIs field should be https://contoso.powerappsportals.com/signin-google. 
1. Select **Create**.
1. Copy **client ID** and **client secret** from **OAuth client** dialog box and configure [OAuth2 site settings](https://docs.microsoft.com/powerapps/maker/portals/configure/configure-oauth2-settings#create-site-settings-by-using-oauth2) in Power Apps portals.

### Facebook app settings

1. Open [Facebook Developers App Dashboard](https://developers.facebook.com/apps)  
2. Select **Add a New App**.
3. Select **Website**.
4. Select **Skip and Create App ID**.
    - Specify a **Display Name**.
    - Choose a **Category**.
    - Select **Create App ID**.

5. While on the dashboard for the new app, go to **Settings** &gt;**Basic** (tab) and add the following details:
    - App Domains (optional): portal.contoso.com 
    - Contact Email: *&lt;email address of your choice&gt;* 
    - Select **Add Platform**, and then select **Website**. 
    - Site URL: https://portal.contoso.com/ or https://portal.contoso.com/signin-facebook

6. Select **Save Changes**.
7. Go to **Status & Review** &gt; **Status** tab.
8. Select **Yes** when prompted to make the app and all its features available to the general public. You must have filled in the valid data in Step 5 above to enable this setting.

### [!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)] application settings

1. Open [[!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)] account Developer Center](https://account.live.com/developers/applications/index)  
2. Select **Create application** and specify an **Application name**.
3. Select **I accept** to accept Terms and Conditions.
4. Go to **Settings** &gt;**API settings**, and then set the redirect URL as https://portal.contoso.com/signin-microsoft 

### Twitter apps settings

1. Open [Twitter Application Management](https://apps.twitter.com/). 
2. Select **Create New App**.

    - Specify a **Name** and **Description** for your app.
    - Set the Website URL as https://portal.contoso.com.
    - Set the Callback URL as https://portal.contoso.com or https://portal.contoso.com/signin-twitter.

3. Select **Create your Twitter application**.

### LinkedIn app settings

1. Open [LinkedIn Developer Network](https://www.linkedin.com/secure/developer).  
2. Select **Add New Application**.

    - Specify an **Application Name**, **Description**, and so on.
    - Set Website URL as https://portal.contoso.com.
    - Set OAuth User Agreement/Default Scope: r\_basicprofie and r\_emailaddress
    - Set OAuth 2.0 Redirect url: https://portal.contoso.com/signin-linkedin.

3. Select **Add Application**.

### Yahoo! YDN App settings

> [!NOTE]
> Due to ongoing compatibility issues between the updated Yahoo YDN OAuth provider endpoint and Power Apps portals, users are temporarily unable to authenticate with Yahoo identity provider.

1. Open [Yahoo! Developer Network](https://developer.yahoo.com/apps).
2. Select **Create an App**.
    
    - Specify an **Application Name**.
    - Application Type: **Web Application**.
    - Callback Domain: portal.contoso.com

3. Select **Create App**.

## Create site settings by using OAuth2

The application dashboard for each provider will display the client ID (app ID, consumer key) and client secret (app secret, consumer secret) for each application. Use these two values to configure the portal site settings.

>[!Note]
> A standard OAuth2 configuration only requires the following settings (with Facebook as an example):
> - `Authentication/OpenAuth/Facebook/ClientId`
> - `Authentication/OpenAuth/Facebook/ClientSecret`

Substitute the `[provider]` tag in the site setting name with a specific identity provider name: Facebook, Google, Yahoo,[!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)], LinkedIn, or Twitter.

|**Site Setting Name**                                           |**Description**                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authentication/Registration/ExternalLoginEnabled                | Enables or disables external account sign-in and registration. Default: true                                                                                                                                                                                                                                                                         |
| Authentication/OpenAuth/\[provider\]/ClientId                   | Required. The client ID value from the provider application. It may also be referred to as an App ID or Consumer Key.  The following setting names are allowed for backwards compatibility:  Authentication/OpenAuth/Twitter/ConsumerKey <ul><li>Authentication/OpenAuth/Facebook/AppId</li><li>Authentication/OpenAuth/LinkedIn/ConsumerKey</li> |
| Authentication/OpenAuth/\[provider\]/ClientSecret               | Required. The client secret value from the provider application. It may also be referred to as an App Secret or Consumer Secret.  The following setting names are allowed for backwards compatibility:  Authentication/OpenAuth/Twitter/ConsumerSecret <ul><li>Authentication/OpenAuth/Facebook/AppSecret</li><li>Authentication/OpenAuth/LinkedIn/ConsumerSecret</li> |
| Authentication/OpenAuth/\[provider\]/AuthenticationType         | The OWIN authentication middleware type. Example: yahoo. [authenticationoptions.authenticationtype](https://msdn.microsoft.com//library/microsoft.owin.security.authenticationoptions.authenticationtype.aspx).                                                                                                                                |  
| Authentication/OpenAuth/\[provider\]/Scope                      | A comma separated list of permissions to request. [microsoftaccountauthenticationoptions.scope](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.scope.aspx).                                                                                                                |  
| Authentication/OpenAuth/\[provider\]/Caption                    | The text that the user can display on a sign in user interface. [microsoftaccountauthenticationoptions.caption](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.caption.aspx).                                                                                              |  
| Authentication/OpenAuth/\[provider\]/BackchannelTimeout         | Timeout value in milliseconds for back channel communications. [microsoftaccountauthenticationoptions.backchanneltimeout](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.backchanneltimeout.aspx).                                                                         |  
| Authentication/OpenAuth/\[provider\]/CallbackPath               | The request path within the application's base path where the user-agent will be returned. [microsoftaccountauthenticationoptions.callbackpath](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.callbackpath.aspx).                                                         |  
| Authentication/OpenAuth/\[provider\]/SignInAsAuthenticationType | The name of another authentication middleware which will be responsible for actually issuing a**userClaimsIdentity**. [microsoftaccountauthenticationoptions.signinasauthenticationtype](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.signinasauthenticationtype.aspx). |  
| Authentication/OpenAuth/\[provider\]/AuthenticationMode         | The OWIN authentication middleware mode. [security.authenticationoptions.authenticationmode](https://msdn.microsoft.com//library/microsoft.owin.security.authenticationoptions.authenticationmode.aspx).                                                                                                                                       |  

### See also

[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[Open ID Connect provider settings for portals](configure-openid-settings.md)   
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
[SAML 2.0 provider settings for portals](configure-saml2-settings.md)
