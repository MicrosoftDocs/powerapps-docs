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
    | Metadata address | The [WS-Federation](https://msdn.microsoft.com/library/bb498017.aspx) metadata URL of the ADFS (STS) server. It commonly ends with the path:/FederationMetadata/2007-06/FederationMetadata.xml. <br> Example: `https://adfs.contoso.com/FederationMetadata/2007-06/FederationMetadata.xml` <br> More information: [WsFederationAuthenticationOptions.MetadataAddress](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.metadataaddress.aspx) |
    | Authentication type | The OWIN authentication middleware type. Enter the value of the [entityID](https://docs.microsoft.com/azure/active-directory/develop/active-directory-federation-metadata) attribute at the root of the federation metadata XML. <br> Example: `https://adfs.contoso.com/adfs/services/trust` <br> More information: [AuthenticationOptions.AuthenticationType](https://msdn.microsoft.com/library/microsoft.owin.security.authenticationoptions.authenticationtype.aspx) |
    | Service provider realm | The ADFS relying party identifier. <br> Example: `https://portal.contoso.com/` <br> More information: [WsFederationAuthenticationOptions.Wtrealm](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.wtrealm.aspx) |
    | Assertion consumer service URL | The ADFS SAML Consumer Assertion endpoint. <br> Example: `https://portal.contoso.com/signin-saml2` <br> More information: [WsFederationAuthenticationOptions.Wreply](https://msdn.microsoft.com/library/microsoft.owin.security.wsfederation.wsfederationauthenticationoptions.wreply.aspx) |

1. Select **Next**.

1. (Optional) Configure additional settings.

    ![Additional settings](media/authentication/saml2-site-settings-additional.png "Additional settings")

    | Name | Description
    | - | - |
    | Validate audience | A Boolean to control whether the audience will be validated during token validation. |
    | Valid audiences | Comma-separated list of audience URLs. <br> More information: [TokenValidationParameters.AllowedAudiences](https://msdn.microsoft.com/library/system.identitymodel.tokens.tokenvalidationparameters.allowedaudiences.aspx) |

1. Select **Confirm**.

### See also

[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[OAuth2 provider settings for portals](configure-oauth2-settings.md)  
[Open ID Connect provider settings for portals](configure-openid-settings.md)  
[WS-Federation provider settings for portals](configure-ws-federation-settings.md)  
