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

[OpenID Connect](https://openid.net/connect/) external identity providers are services that conform to the Open ID Connect [specifications](https://openid.net/developers/specs/). Integrating a provider involves locating the authority (or issuer) URL associated with the provider. A configuration URL can be determined from the authority which supplies metadata required during the authentication workflow. The provider settings are based on the properties of the [OpenIdConnectAuthenticationOptions](https://msdn.microsoft.com/library/microsoft.owin.security.openidconnect.openidconnectauthenticationoptions.aspx) class.

Examples of authority URLs are:

- [Google](https://developers.google.com/identity/protocols/OpenIDConnect): <https://accounts.google.com/><https://accounts.google.com/.well-known/openid-configuration>
- [[!INCLUDE[pn-azure-active-directory](../../../includes/pn-azure-active-directory.md)]](https://msdn.microsoft.com/library/azure/mt168838.aspx): [https://login.microsoftonline.com/&lt;[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] AD Application&gt;/](https://login.microsoftonline.com/contoso.onmicrosoft.com/.well-known/openid-configuration)

Each OpenID Connect provider also involves registering an application (similar to that of an OAuth 2.0 provider) and obtaining a Client Id. The authority URL and the generated application Client Id are the settings required to enable external authentication between the portal and the identity provider.

> [!Note]
> The Google OpenID Connect endpoint is currently not supported because the underlying libraries are still in the early stages of release with compatibility issues to address. The [OAuth2 provider settings for portals](configure-oauth2-settings.md) endpoint can be used instead.


### See also
[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[OAuth2 provider settings for portals](configure-oauth2-settings.md)  
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
[SAML 2.0 provider settings for portals](configure-saml2-settings.md)  

