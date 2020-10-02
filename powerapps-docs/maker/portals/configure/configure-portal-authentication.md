---
title: "Identity providers, protocols, and overview of authentication in Power Apps portals. | MicrosoftDocs"
description: "Learn about the available authentication providers, protocols, and examples to set up authentication for Power Apps portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Overview of authentication in Power Apps portals

In a portal application, an authenticated portal user is associated with either a contact or system user. The default portals configuration is contact-based. To sign in, a contact must have the appropriate web authentication information configured. Portal users must be assigned to web roles to gain permissions beyond unauthenticated users. To configure permissions for a web role, configure its webpage access and website access control rules.

The latest portal authentication experience allows portal users to sign in with their choice of a local contact membership provider-based account or an external account based on [ASP.NET Identity](https://www.asp.net/identity).   

- **Local authentication**: Local authentication is the common forms-based authentication uses the contact records of a Common Data Service environment for authentication. To build custom authentication experiences, developers can use the ASP.NET Identity API to create custom sign in pages and tools.
- **External authentication**: External authentication is provided by the ASP.NET Identity API. In this case, account credentials and password management are handled by a third-party identity provider. This includes OpenID based providers such as LinkedIn and Google and OAuth 2.0 based providers such as Twitter, Facebook, and [!INCLUDE[cc-microsoft](../../../includes/cc-microsoft.md)]. Users sign up to the portal by selecting an external identity to register with the portal. After it's registered, an external identity has access to the same features as a local account. 

Both local and external account registration can use invitation codes for sign-up, and the email confirmation workflow. Also, portal administrators may choose to enable or disable any combination of authentication options through portal site settings.

> [!NOTE]
> Portal users must have an unique email address. If two or more contact records (including deactivated contact records) have the same email address, the contacts will not be able to authenticate on the portal.

## Identity providers in portals

The following table lists common identity providers for portals, the protocol that can be used with the provider, and the relevant documentation.

> [!IMPORTANT]
> Configuration information about common providers for protocols such as OpenID Connect, and SAML 2.0 are provided as examples. You can use any other provider of your choice for the given protocol, and follow similar steps to configure your provider.

| Provider | Protocol | Documentation |
| - | - | - |
| Azure Active Directory | OpenID Connect | [Configure Azure AD with OpenID Connect](configure-openid-settings.md) |
| Azure Active Directory | SAML 2.0 | [Configure Azure AD with SAML 2.0](configure-saml2-settings-azure-ad.md) |
| Azure Active Directory | WS-Federation | [Configure Azure AD with WS-FED](configure-ws-federation-settings-azure-ad.md) |
| Azure Active Directory B2C | OpenID Connect | [Configure Azure AD B2C with OpenID Connect](configure-azure-ad-b2c-provider.md) |
| AD FS | SAML 2.0 | [Configure AD FS with SAML 2.0](configure-saml2-settings-azure-ad.md) |
| AD FS | WS-Federation | [Configure AD FS with WS-FED](configure-ws-federation-settings.md)
| Microsoft | OAuth 2.0 | [Configure Microsoft provider](configure-oauth2-microsoft.md) |
| LinkedIn | OAuth 2.0 | [Configure LinkedIn provider](configure-oauth2-linkedin.md) |
| Facebook | OAuth 2.0 | [Configure Facebook provider](configure-oauth2-facebook.md) |
| Google | OAuth 2.0 | [Configure Google provider](configure-oauth2-google.md) |
| Twitter | OAuth 2.0 | [Configure Twitter provider](configure-oauth2-twitter.md) |
| Local authentication <br>(not recommended) | N/A | [Configure local authentication](set-authentication-identity.md) |

> [!TIP]
> If you're using an existing identity provider and would like to migrate, read [migrate identity providers](migrate-identity-providers.md). The example shows how you can migrate an existing identity provider to Azure Active Directory B2C, though you can use any provider of your choice to migrate to.

## Account sign-up (registration)

Portal administrators have several options for controlling account sign-up behavior. Open registration is the least restrictive sign-up configuration where the portal allows a user account to be registered by providing a user identity. Alternative configurations may require users to provide an invitation code or valid email address to register with the portal. Whatever of the registration configuration, both local and external accounts participate equally in the registration workflow. That is, users can choose which type of account they want to register.

## Open registration

During sign-up, the user has the option of creating a local account (providing a username and password) or selecting an external identity from a list of identity providers. If an external identity is selected, the user is required to sign in through the chosen identity provider to prove that they own the external account. In either case, the user is immediately registered and authenticated with the portal. A new contact record is created in the Common Data Service environment upon sign-up.

With open registration enabled, users aren't required to provide an invitation code to complete the sign-up process.

## Next steps

[Get started with configuring the authentication your portal](use-simplified-authentication-configuration.md)

### See also

- [Configure Azure AD B2C](configure-azure-ad-b2c-provider.md)
- [Configure different OAuth 2.0 providers](configure-oauth2-provider.md)
- [Configure OpenID Connect provider](configure-openid-provider.md)
- [Configure SAML 2.0 provider](configure-saml2-provider.md)
- [Configure WS-FED provider](configure-ws-federation-provider.md)
