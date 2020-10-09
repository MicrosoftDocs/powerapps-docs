---
title: "Configure WS-Federation provider for Power Apps portals.  | MicrosoftDocs"
description: "Instructions to configure WS-Federation provider for Power Apps portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure WS-Federation provider for portals

A single [!INCLUDE[pn-active-directory](../../../includes/pn-active-directory.md)] Federation Services server can be added (or another WS-Federation–compliant security token service) as an identity provider. In addition, a single [[!INCLUDE[pn-azure-shortest](../../../includes/pn-azure-shortest.md)] ACS](https://azure.microsoft.com/documentation/articles/active-directory-dotnet-how-to-use-access-control/) namespace can be configured as a set of individual identity providers. The settings for both AD FS and ACS are based on the properties of the WsFederationAuthenticationOptions class.

To configure SAML 2.0 provider:

1. Select [Add provider](use-simplified-authentication-configuration.md#add-configure-or-delete-an-identity-provider) for your portal.

1. Select **Login provider** as **Other**.

1. Select **Protocol** as **WS FED**.

1. Enter a provider name.

    ![Provider name](media/authentication/wsfed-provider-name.png "Provider name")

1. Select **Next**.

1. Create the application and configure the settings with your identity provider.

    ![Create WS-Federation application](media/authentication/step-1-wsfed.png "Create WS-Federation application")

1. Enter the following site settings for portal configuration.

    ![Configure WS-FED site settings](media/authentication/configure-wsfed-site-settings.png "Configure WS-FED site settings")

    > [!NOTE]
    > Ensure that you review&mdash;and if required, change&mdash;the default values.

    | Name | Description |
    | - | - |
    | Metadata address | The WS-Federation identity provider metadata file location. <br> Example: `https://adfs.contoso.com/FederationMetadata/2007-06/FederationMetadata.xml` |
    | Authentication type | The Entity Id value that specifies a globally unique name for the WS-Federation identity provider. <br> Example: `https://adfs.contoso.com/adfs/services/trust` |
    | Service provider realm | The portal URL that specifies the service provider realm for the WS-Federation identity provider. <br> Example: `https://portal.contoso.com/` |
    | Assertion consumer service URL | The portal URL that corresponds to the service provider's endpoint (URL). |

1. Select **Next**.

1. (Optional) Configure additional settings.

    ![Additional settings](media/authentication/wsfed-site-settings-additional.png "Additional settings")

    | Name | Description
    | - | - |
    | Sign-out reply | The URL to return to (sign-out wreply) once the sign-out is complete. <br> Example: `https://portal.contoso.com/signin-federation` |
    | Valid audiences | Comma-separated list of audience URLs. |
    | Validate audiences | If enabled, the audience will be validated during the token validation. |
    | WHR | The home realm of the identity provider (IdP) to use for authentication. Sets the WS-Federation sign-in request **whr** parameter. If empty, the **whr** parameter is not included in the request. <br> More information: [wsFederation](https://docs.microsoft.com/dotnet/framework/configure-apps/file-schema/windows-identity-foundation/wsfederation) |
    | Contact mapping with email | Specify whether the contacts are mapped to a corresponding email. When set to On, a unique contact record is associated with a matching email address, assigning the external identity provider to the contact after a successful user sign-in. |

1. Select **Confirm**.

### See also

[Configure portal authentication](configure-portal-authentication.md)  
[Set authentication identity for a portal](set-authentication-identity.md)  
[OAuth2 provider settings for portals](configure-oauth2-settings.md)  
[Open ID Connect provider settings for portals](configure-openid-settings.md)  
[SAML 2.0 provider settings for portals](configure-saml2-settings.md)  
