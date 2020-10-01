---
title: "Configure OAuth2 provider settings for a portal  | MicrosoftDocs"
description: "Instructions to add and configure OAuth2 provider settings for a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 01/17/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure OAuth2 provider settings for portals

The supported OAuth 2.0 providers are:

- [!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)] Account
- Twitter
- Facebook
- Google
- LinkedIn
- Yahoo

## Create OAuth applications

In general, if an OAuth provider uses app settings that require a redirect URI value, specify <https://portal.contoso.com/or> https://portal.contoso.com/signin-\[provider\] depending on how the provider performs redirect URI validation (some providers require the full URL path to be specified along with the domain name). Substitute the name of the provider in place of \[provider\] in the redirect URI.

## Google People API settings

> [!NOTE]
> [Google+ API](https://developers.google.com/people/legacy) is deprecated. We strongly recommend that you migrate to [Google People API](https://developers.google.com/people).

Following these steps to configure your Power Apps portal with [Google's OAuth 2.0 authentication] for user authentication.

1. Open [Google Developers Console](https://console.developers.google.com/).  
1. Create an API project or open an existing project.
1. Select **ENABLE APIS AND SERVICES** from dashboard of APIs and Services.
1. Search and enable API **Google People API**.
1. Inside **Google APIs**, select **Credentials** on left navigation.

    > [!NOTE]
    > If you have consent screen configured already with portals top level domain, you can skip steps 6 through 14 and directly move to step 15. However, go through step 11 before moving to step 15 if your consent screen is configured but portals top level domain is not added.

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
1. Type your Power Apps portal URL in **Authorized JavaScript Origins** list.
1. Type **Authorized redirect URIs** as the Power Apps portal URL followed by **/signin-google**. For example, if portal URL is https://contoso.powerappsportals.com, authorized redirect URIs field should be https://contoso.powerappsportals.com/signin-google.
1. Select **Create**.
1. Copy **client ID** and **client secret** from **OAuth client** dialog box and configure [OAuth2 site settings](https://docs.microsoft.com/powerapps/maker/portals/configure/configure-oauth2-settings#create-site-settings-by-using-oauth2) in Power Apps portals.

## Facebook app settings

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

## Twitter apps settings

1. Open [Twitter Application Management](https://apps.twitter.com/). 
2. Select **Create New App**.

    - Specify a **Name** and **Description** for your app.
    - Set the Website URL as https://portal.contoso.com.
    - Set the Callback URL as https://portal.contoso.com or https://portal.contoso.com/signin-twitter.

3. Select **Create your Twitter application**.

## LinkedIn app settings

1. Open [LinkedIn Developer Network](https://www.linkedin.com/secure/developer).  
2. Select **Add New Application**.

    - Specify an **Application Name**, **Description**, and so on.
    - Set Website URL as https://portal.contoso.com.
    - Set OAuth User Agreement/Default Scope: r\_basicprofie and r\_emailaddress
    - Set OAuth 2.0 Redirect url: https://portal.contoso.com/signin-linkedin.

3. Select **Add Application**.

## Yahoo! YDN App settings

> [!NOTE]
> Due to ongoing compatibility issues between the updated Yahoo YDN OAuth provider endpoint and Power Apps portals, users are temporarily unable to authenticate with Yahoo identity provider.

1. Open [Yahoo! Developer Network](https://developer.yahoo.com/apps).
2. Select **Create an App**.
    
    - Specify an **Application Name**.
    - Application Type: **Web Application**.
    - Callback Domain: portal.contoso.com

3. Select **Create App**.
                                                                                                                                   |  

### See also

[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[Open ID Connect provider settings for portals](configure-openid-settings.md)   
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
[SAML 2.0 provider settings for portals](configure-saml2-settings.md)
