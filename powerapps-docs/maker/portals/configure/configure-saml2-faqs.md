---
title: "Frequently Asked Questions (FAQs) about using SAML 2.0 providers for authentication in Power Apps portals.  | MicrosoftDocs"
description: "Learn about Frequently Asked Questions (FAQs) when using SAML 2.0 providers for authentication in Power Apps portals."
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/20/2020
ms.author: dileeps
ms.reviewer: tapanm
---

# Frequently Asked Questions (FAQs) when using SAML 2.0 in portals

In this article, learn about the common scenarios, or the FAQs when using an authentication provider with Power Apps portals that uses SAML 2.0 specifications.

## Does portals support SAML 1.0 based providers?

No. Portals only support SAML 2.0 based providers.

## Does portals support Signed Assertion?

No. Portals doesn't support signed assertion request. If you're using signed assertion, we suggest that you use OpenID Connect. If your identity provider (IDP) doesn’t support OpenID Connect, use an intermediary identity provider (Azure AD B2C preferred) that supports federation with SAML, and that can federate with portals using OpenID Connect.

## Does portals support signed SAML responses?

Yes. Portals requires all SAML responses to be signed by the identity provider (IDP).

## Does portals support encrypted assertion and response?

No. Portals doesn’t support encrypted SAML assertion or response.

## What type of Name Identifiers are supported?

Portals requires "Persistent" Identifiers that ensure that the user can always be uniquely identified across sessions. Portals doesn't support “Transient” Identifiers.

## Does portals require any specific AuthNContextClass in SAML assertion request?

Yes. Portals will specify *PasswordProtectedTransport* in authentication requests, and requires identity provider (IDP) to support it.

### See also

- [Example: Configure SAML 2.0 for portals with Azure Active Directory](configure-saml2-settings-azure-ad.md)
- [Example: Configure SAML 2.0 provider for portals with AD FS](configure-saml2-settings.md)
- [Configure SAML 2.0 provider for portals](configure-saml2-provider.md)
