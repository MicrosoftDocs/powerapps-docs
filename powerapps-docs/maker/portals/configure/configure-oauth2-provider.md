---
title: "Configure OAuth 2.0 identity providers in Power Apps portals - such as Microsoft, LinkedIn, Facebook, Google, and Twitter. | MicrosoftDocs"
description: "Learn how to configure OAuth 2.0 identity providers in Power Apps portals - such as Microsoft, LinkedIn, Facebook, Google, and Twitter."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/20/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure an OAuth 2.0 provider for portals

To use OAuth 2.0&ndash;based external identity providers, you register an application with a third-party service to obtain a *client ID* and *client secret* pair. Often this application requires that you specify a redirect URL to allow the identity provider to send users back to the portal (the *relying party*). The client ID and client secret are configured as portal site settings to establish a secure connection from the relying party to the identity provider. The settings are based on the properties of the [[!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)]AccountAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.microsoftaccount.microsoftaccountauthenticationoptions.aspx), [TwitterAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.twitter.twitterauthenticationoptions.aspx), [FacebookAuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.facebook.facebookauthenticationoptions.aspx), and [GoogleOAuth2AuthenticationOptions](https://msdn.microsoft.com//library/microsoft.owin.security.google.googleoauth2authenticationoptions.aspx) classes.  

To learn about individual OAuth 2.0 providers, select the name of the provider that you want to configure:

- [Microsoft](configure-oauth2-microsoft.md)
- [LinkedIn](configure-oauth2-linkedin.md)
- [Facebook](configure-oauth2-facebook.md)
- [Google](configure-oauth2-google.md)
- [Twitter](configure-oauth2-twitter.md)

> [!NOTE]
> - Custom OAuth providers aren't supported. For custom OAuth providers, use [OpenID Connect](configure-openid-provider.md) instead.
> Changes to the authentication settings [might take a few minutes](../admin/clear-server-side-cache.md#caching-changes-for-portals-with-version-926x-or-later) to be reflected on the portal. Restart the portal by using [portal actions](../admin/admin-overview.md) if you want the changes to be reflected immediately.

For general settings applicable to all OAuth 2.0 providers, go to [Configure additional settings for OAuth 2.0 providers](configure-oauth2-settings.md).


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]