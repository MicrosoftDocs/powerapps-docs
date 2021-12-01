---
title: FAQs for using SAML 2.0 in portals
description: Learn about Frequently Asked Questions when using SAML 2.0 providers for authentication in Power Apps portals.
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: dileeps
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - dileepsinghmicrosoft
---

# FAQs for using SAML 2.0 in portals

This article includes information about common Power Apps portals scenarios and frequently asked questions for using an authentication provider that conforms to the Security Assertion Markup Language (SAML) 2.0 standard.

## Does portals support SAML 1.0&ndash;based providers?

No. Portals only supports SAML 2.0&ndash;based providers.

## Does portals support Signed Assertion?

No. Portals doesn't support signed assertion requests. If you're using signed assertion, we suggest that you use OpenID Connect. If your identity provider doesn't support OpenID Connect, use an intermediary identity provider (preferably Azure AD B2C) that supports federation with SAML and can federate with portals by using OpenID Connect.

## Does portals support signed SAML responses?

Yes. Portals requires all SAML responses to be signed by the identity provider.

## Does portals support encrypted assertion and response?

No. Portals doesn't support encrypted SAML assertion or response.

## What type of name identifiers are supported?

Portals requires *persistent* identifiers that ensure that the user can always be uniquely identified across sessions. Portals doesn't support *transient* identifiers.

## Does portals require any specific AuthNContextClass in SAML assertion requests?

Yes. Portals will specify *PasswordProtectedTransport* in authentication requests, and requires that the identity provider support it.

### See also

[Configure a SAML 2.0 provider for portals with Azure AD](configure-saml2-settings-azure-ad.md)  
[Configure a SAML 2.0 provider for portals with AD FS](configure-saml2-settings.md)  
[Configure a SAML 2.0 provider for portals](configure-saml2-provider.md)  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]