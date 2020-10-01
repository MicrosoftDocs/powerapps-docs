---
title: "Use simplified authentication and identity provider configuration (Preview) | MicrosoftDocs"
description: "Learn how to use quick, easy, and simplified portal configuration for authentication."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/29/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure additional settings for OAuth 2 providers

The additional authentication settings in this section apply to the **Facebook**, **Twitter**, **Microsoft**, **LinkedIn**, and **Google** providers.

![Configure additional settings](media/use-simplified-authentication-configuration/additional-oauth-settings.png "Configure additional settings")

- **Authentication type** - The OWIN authentication middleware type:  [AuthenticationOptions.AuthenticationType](https://docs.microsoft.com/previous-versions/aspnet/mt152183(v=vs.113)?redirectedfrom=MSDN). For example, https://sts.windows.net/contoso.onmicrosoft.com/.
- **Authentication mode** - The OWIN authentication middleware mode:  [AuthenticationOptions.AuthenticationMode](https://docs.microsoft.com/previous-versions/aspnet/mt152179(v=vs.113)?redirectedfrom=MSDN).
- **Backchannel timeout** - Timeout value in milliseconds for back-channel communications: [MicrosoftAccountAuthenticationOptions.BackchannelTimeout](https://docs.microsoft.com/previous-versions/aspnet/mt174421(v=vs.113)?redirectedfrom=MSDN).
- **Callback path** - The request path within the application's base path where the user-agent will be returned: [MicrosoftAccountAuthenticationOptions.CallbackPath](https://docs.microsoft.com/previous-versions/aspnet/mt174433(v=vs.113)?redirectedfrom=MSDN).​
- **Sign in As authentication type** - The name of another authentication middleware that will be responsible for actually issuing a user Claims Identity: [MicrosoftAccountAuthenticationOptions.SignInAsAuthenticationType](https://docs.microsoft.com/previous-versions/aspnet/mt174430(v=vs.113)?redirectedfrom=MSDN).​
- **Scope** - A comma-separated list of permissions to request: [MicrosoftAccountAuthenticationOptions.Scope](https://docs.microsoft.com/previous-versions/aspnet/mt174435(v=vs.113)?redirectedfrom=MSDN).​
- ​**Registration Enabled**​ - Enables or disables the registration requirement for the existing identity provider. When disabled, the user is denied registration with an error if no contact record exists for the user. When enabled, user registration is allowed for a new user only if the site setting **Authentication/Registration/Enabled** is set to true.​

For more information, see [OAuth2 site settings](configure-oauth2-settings.md#create-site-settings-by-using-oauth2).

### See also

- [Set authentication identity for a portal](set-authentication-identity.md)
- [Configure Azure AD B2C provider settings](azure-ad-b2c.md)
- [Configure OAuth2 provider settings](configure-oauth2-settings.md)
- [Microsoft Learn: Authentication and user management in Power Apps portals](https://docs.microsoft.com/learn/modules/authentication-user-management/)
