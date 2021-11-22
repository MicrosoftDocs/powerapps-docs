---
title: Overview of authentication in Power Apps portals
description: Learn about the available authentication providers, protocols, and examples to set up authentication for Power Apps portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 04/26/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - dileepsinghmicrosoft
---

# Overview of authentication in Power Apps portals

In Power Apps portals, each authenticated portal user is associated with a [contact record in Microsoft Dataverse](../../../developer/data-platform/customer-entities-account-contact.md#contact-table). Portal users must be assigned to [web roles](create-web-roles.md) to gain permissions beyond unauthenticated users. To configure permissions for a web role, configure its [webpage access and website access control rules](webpage-access-control.md). Portals allows portal users to sign in with their choice of an external account based on [ASP.NET Identity](https://www.asp.net/identity). Though not recommended, portals also allows a local contact membership provider-based account for users to sign in.

> [!NOTE]
> Portal users must have a unique email address. If two or more contact records (including deactivated contact records) have the same email address, the contacts won't be able to authenticate on the portal.

The following table lists common identity providers for portals, the protocol that can be used with the provider, and the relevant documentation.

> [!IMPORTANT]
> Configuration information about common providers for protocols such as OpenID Connect and SAML 2.0 are given as examples. You can use the provider of your choice for the given protocol, and follow similar steps to configure your provider.

| Provider | Protocol | Documentation |
| - | - | - |
| Azure Active Directory (Azure AD) | OpenID Connect | [Azure AD with OpenID Connect](configure-openid-settings.md) |
| Azure AD | SAML 2.0 | [Azure AD with SAML 2.0](configure-saml2-settings-azure-ad.md) |
| Azure AD | WS-Federation | [Azure AD with WS-Federation](configure-ws-federation-settings-azure-ad.md) |
| Azure AD B2C | OpenID Connect | [Azure AD B2C with OpenID Connect](configure-azure-ad-b2c-provider.md) <br> [Azure AD B2C with OpenID Connect (manual configuration)](configure-azure-ad-b2c-provider-manual.md) |
| Azure Directory Federation Services (AD FS) | SAML 2.0 | [AD FS with SAML 2.0](configure-saml2-settings.md) |
| AD FS | WS-Federation | [AD FS with WS-Federation](configure-ws-federation-settings.md)
| Microsoft | OAuth 2.0 | [Microsoft](configure-oauth2-microsoft.md) |
| LinkedIn | OAuth 2.0 | [LinkedIn](configure-oauth2-linkedin.md) |
| Facebook | OAuth 2.0 | [Facebook](configure-oauth2-facebook.md) |
| Google | OAuth 2.0 | [Google](configure-oauth2-google.md) |
| Twitter | OAuth 2.0 | [Twitter](configure-oauth2-twitter.md) <br> **Note**: Twitter authentication for portals is temporarily unavailable because of the compatibility issues. |
| Local authentication <br>(not recommended) | Not applicable | [Local authentication](set-authentication-identity.md) |

> [!NOTE]
> Because of the ongoing compatibility problem between the updated Yahoo YDN OAuth provider endpoint and Power Apps portals, users are temporarily unable to authenticate with Yahoo identity provider. Hence, Yahoo is not available as the authentication provider in the list of OAuth 2.0 based providers for portals.

If you're already using an existing identity provider and want to migrate your portal to use another identity provider, read [Migrate identity providers](migrate-identity-providers.md). The example shows how you can migrate an existing identity provider to Azure AD B2C, though you can use the provider of your choice to migrate to.

## Open registration

Portal administrators have several options for controlling account sign-up behavior. [Open registration](use-simplified-authentication-configuration.md#general-authentication-settings) is the least restrictive sign-up configuration, where the portal allows a user account to be registered by providing a user identity. Alternative configurations might require users to provide an invitation code or valid email address to register with the portal. Whatever the registration configuration, both local and external accounts participate equally in the registration workflow. Users can choose which type of account they want to register.

During sign-up, the user has the option of selecting an external identity from a list of identity providers or&mdash;in an approach that's not recommended&mdash;creating a local account (providing a username and password). If an external identity is selected, the user is required to sign in through the chosen identity provider to prove that they own the external account. In both external or local identity provider situations, the user is immediately registered and authenticated with the portal. A new [contact record](../../../developer/data-platform/customer-entities-account-contact.md#contact-table) is created in the Dataverse environment upon sign-up.

With open registration enabled, users aren't required to provide an invitation code to complete the sign-up process.

## Next step

[Get started with configuring the authentication for your portal](use-simplified-authentication-configuration.md)

### See also

[Configure the Azure AD B2C provider for portals](configure-azure-ad-b2c-provider.md)  
[Configure an OAuth 2.0 provider for portals](configure-oauth2-provider.md)  
[Configure an OpenID Connect provider for portals](configure-openid-provider.md)  
[Configure a SAML 2.0 provider for portals](configure-saml2-provider.md)  
[Configure a WS-Federation provider for portals](configure-ws-federation-provider.md)  
[Microsoft Learn: Authentication and user management in Power Apps portals](/learn/modules/authentication-user-management/)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]