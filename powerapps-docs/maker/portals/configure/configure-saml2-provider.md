---
title: "Configure SAML 2.0 provider settings for a portal | MicrosoftDocs"
description: "Instructions to add and configure SAML 2.0 provider settings for a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/18/2019
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure SAML 2.0 provider settings for portals

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

1. Select **Confirm**.

### See also

[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[OAuth2 provider settings for portals](configure-oauth2-settings.md)  
[Open ID Connect provider settings for portals](configure-openid-settings.md)  
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
