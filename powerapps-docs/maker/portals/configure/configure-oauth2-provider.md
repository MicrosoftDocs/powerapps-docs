---
title: "Configure OAuth 2.0 identity providers in Power Apps portals - such as Microsoft, LinkedIn, Facebook, Google, and Twitter. | MicrosoftDocs"
description: "Learn how to configure OAuth 2.0 identity providers in Power Apps portals - such as Microsoft, LinkedIn, Facebook, Google, and Twitter."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/29/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure OAuth 2.0 providers

The OAuth 2.0 based external identity providers involve registering an "application" with a third-party service to obtain a "client ID" and "client secret" pair. Often this application requires specifying a redirect URL that allows the identity provider to send users back to the portal (relying party). The client ID and client secret are configured as portal site settings in order to establish a secure connection from relying party to identity provider. The settings are based on the properties of the [[!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)]AccountAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.aspx), [TwitterAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.twitter.twitterauthenticationoptions.aspx), [FacebookAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.facebook.facebookauthenticationoptions.aspx), and [GoogleOAuth2AuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.google.googleoauth2authenticationoptions.aspx) classes.  

To learn about individual OAuth 2.0 providers, select the name of the provider that you want to configure.

- [Microsoft](configure-oauth2-microsoft.md)
- [LinkedIn](configure-oauth2-linkedin.md)
- [Facebook](configure-oauth2-facebook.md)
- [Google](configure-oauth2-google.md)
- [Twitter](configure-oauth2-twitter.md)

> [!NOTE]
> Custom OAuth providers aren't supported. For custom OAuth providers, use [OpenID Connect](configure-openid-provider.md) instead.

For general settings applicable to all OAuth 2.0 providers, go to [Additional OAuth 2.0 provider settings](configure-oauth2-settings.md).
