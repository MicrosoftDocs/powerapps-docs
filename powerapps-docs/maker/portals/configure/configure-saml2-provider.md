---
title: "Configure SAML 2.0 provider for Power Apps portals. | MicrosoftDocs"
description: "Instructions to configure SAML 2.0 provider for Power Apps portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure SAML 2.0 provider for portals

To provide external authentication, you can add one or more [SAML 2.0](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html)–compliant identity providers (IdP). This document describes how to set up various identity providers to integrate with a portal that acts as a service provider.  

To configure SAML 2.0 provider:

1. Select [Add provider](use-simplified-authentication-configuration.md#add-configure-or-delete-an-identity-provider) for your portal.

1. Select **Login provider** as **Other**.

1. Select **Protocol** as **SAML 2.0**.

1. Enter a provider name.

    ![Provider name](media/authentication/saml2-provider-name.png "Provider name")

1. Select **Next**.

1. Create the application and configure the settings with your identity provider.

1. Enter the following site settings for portal configuration.

    ![Configure SAML 2.0 site settings](media/authentication/saml2-site-settings.png "Configure SAML 2.0 site settings")

    > [!NOTE]
    > Ensure that you review&mdash;and if required, change&mdash;the default values.

    | Name | Description |
    | - | - |
    | Metadata address | The SAML 2.0 identity provider metadata file location. <br> Example: `https://adfs.contoso.com/FederationMetadata/2007-06/FederationMetadata.xml` |
    | Authentication type | The Entity Id value that specifies a globally unique name for the SAML 2.0 identity provider. <br> Example: `https://adfs.contoso.com/adfs/services/trust` |
    | Service provider realm | The portal URL that specifies the service provider realm for the SAML 2.0 identity provider. <br> Example: `https://portal.contoso.com/` |
    | Assertion consumer service URL | The portal URL that corresponds to the service provider's endpoint (URL). This URL is responsible for receiving and parsing a SAML assertion. <br> Example: `https://portal.contoso.com/signin-saml2` |

1. Select **Next**.

1. (Optional) Configure additional settings.

    ![Additional settings](media/authentication/saml2-site-settings-additional.png "Additional settings")

    | Name | Description
    | - | - |
    | Validate audience | If enabled, the audience will be validated during the token validation. |
    | Valid audiences | Comma-separated list of audience URLs. |
    | Contact mapping with email | Specify whether the contacts are mapped to a corresponding email. When set to On, a unique contact record is associated with a matching email address, assigning the external identity provider to the contact after a successful user sign-in. |

1. Select **Confirm**.

## Edit SAML 2.0 provider

To edit a configured SAML 2.0 provider, see [Edit a provider](use-simplified-authentication-configuration.md#edit-a-provider).

### See also

- [Example: Configure SAML 2.0 for portals with Azure Active Directory](configure-saml2-settings-azure-ad.md)
- [Example: Configure SAML 2.0 provider for portals with AD FS](configure-saml2-settings.md)
- [Frequently Asked Questions (FAQs) when using SAML 2.0 in portals](configure-saml2-faqs.md)
- [Configure SAML 2.0 provider for portals](configure-saml2-provider.md)
