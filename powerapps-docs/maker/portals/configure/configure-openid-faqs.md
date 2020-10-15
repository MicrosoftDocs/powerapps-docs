---
title: "Frequently Asked Questions (FAQs) about using OpenID Connect providers for authentication in Power Apps portals.  | MicrosoftDocs"
description: "Learn about Frequently Asked Questions (FAQs) when using OpenID Connect providers for authentication in Power Apps portals."
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/12/2020
ms.author: dileeps
ms.reviewer: tapanm
---

# Frequently Asked Questions (FAQs) when using OpenID Connect in portals

In this article, learn about the common scenarios, or the FAQs when using an authentication provider with Power Apps portals that uses [OpenID Connect specifications](https://openid.net/specs/openid-connect-core-1_0.html).

## Do I require OpenId Connect Auto-Discovery Document to integrate with portals?

Yes. Auto-Discovery Document (commonly known as `/.well-known/openid-configuration`) is required to integrate with portals. Information present in this document is used by portals to create authorization requests, and validate the authentication tokens.

If your identity provider (IDP) doesn’t provide this document, you can create it manually, and host it at any public location (including your portal).

> [!NOTE]
> Similar to the discovery document, portals also requires the IDP to provide a public *JWKS URI* endpoint where the public keys are available to verify the signature of the id token. This endpoint needs to be specified within the discovery document as “jwks_uri” key.

## Does portals support *acr_values*, or *ui_locales* request parameters in the authentication requests?

No. Portals doesn’t support *acr_values*, or *ui_locales* request parameters in authorization requests. However, portals supports all the required, and recommended request parameters defined in the [OpenId Connect specifications](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest).

The following optional parameters are supported:

- Response_mode
- Nonce

## Does portals support custom scope parameter(s) in authentication requests?

Yes. Custom scope parameter(s) can be specified using scope option in configuration.

## Why does the username value in contact, or external identity record in Common Data Service, show a different value compared to what the user entered on the sign-in page?

Username field on contact record, and externally identity record, will show the value sent in either the sub-claim or oid-claim (oid claim for only Azure AD-based providers). This is because the sub claim represents the identifier for end user, and is guaranteed by identity provider (IDP) to be unique. Oid claim (Object ID - a unique identifier for all users in a tenant) is supported when used with single-tenant Azure AD-based providers.

## Does portals support logout from OpenId Connect-based provider?

Yes. Portal supports front channel logout technique to log out from both the application, and the OpenId Connect-based providers.

## Does portals support Single Logout (SLO)?

No. Portals doesn't support single logout technique for OpenID Connect-based providers.

## Does portals require any specific claim in *id_token*?

Apart from all the required claims, portals requires a claim representing email address of the users in the *id_token*. This claim must be named as either “email”, “emails” or “upn”.

These claims are processed at in the following order of priority to set as the *Primary Email Address* of the contact record in Common Data Service:

1. email
1. emails
1. upn

When in use, "emailclaimsmapping" is also used to search for an existing contact (Primary Email Address field in Common Data Service).

## Can I get access to tokens (ID or Access) using JavaScript?

No. Id_token provided by the identity provider isn't made available through any standard technique on the client side; and is only used for authentication purpose.

However, if you're using Implicit Grant Flow, you can use the methods provided by your identity provider to get access to ID or Access tokens.

For example, Azure AD provides [MSAL library](https://docs.microsoft.com/azure/active-directory/develop/msal-overview) to achieve this scenario in clients.

## Can I use a custom OpenId Connect provider, instead of Azure AD?

Yes. Portals supports any OpenID Connect provider that supports the standard [OpenID Connect specifications](https://openid.net/specs/openid-connect-core-1_0.html).

### See also

[Configure the Open ID Connect provider for portals](configure-openid-provider.md)
