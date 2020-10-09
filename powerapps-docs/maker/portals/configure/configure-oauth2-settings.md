---
title: "Configure additional site settings for OAuth 2.0 providers in Power Apps portals.  | MicrosoftDocs"
description: "Learn how to configure additional site settings for OAuth 2.0 providers in Power Apps portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure additional settings for OAuth 2.0 providers

As explained in the [OAuth 2.0 providers in portals](configure-oauth2-provider.md) article, you can configure several identity providers using the OAuth 2.0 protocol. The additional authentication settings in this section apply to the [Microsoft](configure-oauth2-microsoft.md), [LinkedIn](configure-oauth2-linkedin.md), [Facebook](configure-oauth2-facebook.md), [Google](configure-oauth2-google.md), and [Twitter](configure-oauth2-twitter.md) providers.

To configure the additional settings for any OAuth 2.0 identity provider, select **Configure** from [provider settings](use-simplified-authentication-configuration.md#add-configure-or-delete-an-identity-provider) page, and expand **Additional settings**.

![Configure additional settings](media/use-simplified-authentication-configuration/additional-oauth-settings.png "Configure additional settings")

- **Authentication type** - The OWIN authentication middleware type. <br> Example: `https://sts.windows.net/contoso.onmicrosoft.com/`
- **Authentication mode** - The OWIN authentication middleware mode.
- **Backchannel timeout** - Time out value in milliseconds for back-channel communications: MicrosoftAccountAuthenticationOptions.BackchannelTimeout.
- **Callback path** - The request path within the application's base path where the user-agent will be returned: MicrosoftAccountAuthenticationOptions.CallbackPath.​
- **Sign in As authentication type** - The name of another authentication middleware that will be responsible for actually issuing a user Claims Identity: MicrosoftAccountAuthenticationOptions.SignInAsAuthenticationType.​
- **Scope** - A comma-separated list of permissions to request: MicrosoftAccountAuthenticationOptions.Scope.​
- ​**Registration Enabled**​ - Enables or disables the registration requirement for the existing identity provider. When disabled, the user is denied registration with an error if no contact record exists for the user. When enabled, user registration is allowed for a new user only if the site setting **Authentication/Registration/Enabled** is set to true.​

### See also

[Overview of OAuth 2.0 providers in portals](configure-oauth2-provider.md)
