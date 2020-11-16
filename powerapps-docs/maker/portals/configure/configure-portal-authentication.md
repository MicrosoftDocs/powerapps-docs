---
title: "Identity providers, protocols, and overview of authentication in Power Apps portals. | MicrosoftDocs"
description: "Learn about the available authentication providers, protocols, and examples to set up authentication for Power Apps portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/20/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Overview of authentication in Power Apps portals

In Power Apps portals, each authenticated portal user is associated with a [contact record in Microsoft Dataverse](../../../developer/common-data-service/customer-entities-account-contact.md#contact-entity). Portal users must be assigned to [web roles](create-web-roles.md) to gain permissions beyond unauthenticated users. To configure permissions for a web role, configure its [webpage access and website access control rules](webpage-access-control.md). Portals allows portal users to sign in with their choice of an external account based on [ASP.NET Identity](https://www.asp.net/identity). Though not recommended, portals also allows a local contact membership provider-based account for users to sign in.

> [!NOTE]
> Portal users must have an unique email address. If two or more contact records (including deactivated contact records) have the same email address, the contacts will not be able to authenticate on the portal.

The following table lists common identity providers for portals, the protocol that can be used with the provider, and the relevant documentation.

> [!IMPORTANT]
> Configuration information about common providers for protocols such as OpenID Connect, and SAML 2.0 are provided as examples. You can use any other provider of your choice for the given protocol, and follow similar steps to configure your provider.

| Provider | Protocol | Documentation |
| - | - | - |
| Azure Active Directory | OpenID Connect | [Azure AD with OpenID Connect](configure-openid-settings.md) |
| Azure Active Directory | SAML 2.0 | [Azure AD with SAML 2.0](configure-saml2-settings-azure-ad.md) |
| Azure Active Directory | WS-Federation | [Azure AD with WS-Federation](configure-ws-federation-settings-azure-ad.md) |
| Azure Active Directory B2C | OpenID Connect | [Azure AD B2C with OpenID Connect](configure-azure-ad-b2c-provider.md) |
| AD FS | SAML 2.0 | [AD FS with SAML 2.0](configure-saml2-settings.md) |
| AD FS | WS-Federation | [AD FS with WS-Federation](configure-ws-federation-settings.md)
| Microsoft | OAuth 2.0 | [Microsoft](configure-oauth2-microsoft.md) |
| LinkedIn | OAuth 2.0 | [LinkedIn](configure-oauth2-linkedin.md) |
| Facebook | OAuth 2.0 | [Facebook](configure-oauth2-facebook.md) |
| Google | OAuth 2.0 | [Google](configure-oauth2-google.md) |
| Twitter | OAuth 2.0 | [Twitter](configure-oauth2-twitter.md) |
| Local authentication <br>(not recommended) | Not applicable | [Local authentication](set-authentication-identity.md) |

> [!TIP]
> If you're already using an existing identity provider and would like to migrate your portal to use another identity provider, read [migrate identity providers](migrate-identity-providers.md). The example shows how you can migrate an existing identity provider to Azure Active Directory B2C, though you can use any provider of your choice to migrate to.

## Open registration

Portal administrators have several options for controlling account sign-up behavior. [Open registration](use-simplified-authentication-configuration.md#general-authentication-settings) is the least restrictive sign-up configuration where the portal allows a user account to be registered by providing a user identity. Alternative configurations may require users to provide an invitation code or valid email address to register with the portal. Whatever of the registration configuration, both local and external accounts participate equally in the registration workflow. Users can choose which type of account they want to register.

During sign-up, the user has the option of selecting an external identity from a list of identity providers, or, a not recommended approach of creating a local account (providing a username and password). If an external identity is selected, the user is required to sign in through the chosen identity provider to prove that they own the external account. In both external or local identity provider situations, the user is immediately registered and authenticated with the portal. A new [contact record](../../../developer/common-data-service/customer-entities-account-contact.md#contact-entity) is created in the Dataverse environment upon sign-up.

With open registration enabled, users aren't required to provide an invitation code to complete the sign-up process.

## Next steps

[Get started with configuring the authentication for your portal](use-simplified-authentication-configuration.md)

### See also

- [Configure Azure AD B2C](configure-azure-ad-b2c-provider.md)
- [Configure different OAuth 2.0 providers](configure-oauth2-provider.md)
- [Configure OpenID Connect provider](configure-openid-provider.md)
- [Configure SAML 2.0 provider](configure-saml2-provider.md)
- [Configure WS-Federation provider](configure-ws-federation-provider.md)
- [Microsoft Learn: Authentication and user management in Power Apps portals](https://docs.microsoft.com/learn/modules/authentication-user-management/)
