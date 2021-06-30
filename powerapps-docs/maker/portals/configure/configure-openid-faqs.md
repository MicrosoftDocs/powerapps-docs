---
title: FAQs for using OpenID Connect in portals
description: Learn about frequently asked questions when using OpenID Connect providers for authentication in Power Apps portals.
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.author: dileeps
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
    - dileepsinghmicrosoft
---

# FAQs for using OpenID Connect in portals

This article includes information about common Power Apps portals scenarios and frequently asked questions for using an authentication provider that conforms to the [OpenID Connect specification](https://openid.net/specs/openid-connect-core-1_0.html).

## Do I require an OpenID Connect Auto-Discovery Document to integrate with portals?

Yes. The Auto-Discovery Document (also known as `/.well-known/openid-configuration`) is required to integrate with portals. Information present in this document is used by portals to create authorization requests and validate the authentication tokens.

If your identity provider doesn't provide this document, you can create it manually and host it at any public location (including your portal).

> [!NOTE]
> Similar to the discovery document, portals also requires the identity provider to provide a public *JWKS URI* endpoint where the public keys are available to verify the signature of the ID token. This endpoint needs to be specified in the discovery document as the *jwks_uri* key.

## Does portals support *acr_values*, or *ui_locales* request parameters in the authentication requests?

No. Portals doesn't support *acr_values* or *ui_locales* request parameters in authorization requests. However, the portals feature does support all the required&mdash;and recommended&mdash;request parameters defined in the [OpenID Connect specification](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest).

The following optional parameters are supported:

- Response_mode
- Nonce

## Does portals support custom scope parameters in authentication requests?

Yes. Custom scope parameters can be specified by using the scope option during configuration.

## Why does the username value in a contact, or an external identity record in Common Data Service, show a different value compared to what the user entered on the sign-in page?

The username field on a contact record and an external identity record will show the value sent in either the sub-claim or object ID (OID) claim (for Azure AD&ndash;based providers). This is because the sub-claim represents the identifier for the end user and is guaranteed by the identity provider to be unique. An OID claim (where the object ID is a unique identifier for all users in a tenant) is supported when used with single-tenant Azure AD&ndash;based providers.

## Does portals support sign-out from OpenID Connect&ndash;based providers?

Yes. The portals feature supports the front-channel sign-out technique to sign out from both the application and the OpenID Connect&ndash;based providers.

## Does portals support single sign-out?

No. Portals doesn't support the single sign-out technique for OpenID Connect&ndash;based providers.

## Does portals require any specific claim in an ID token*?

In addition to all required claims, the portals feature requires a claim representing the email address of users in the ID token. This claim must be named `email`, `emails`, or `upn`.

Apart from all the required claims, portals requires a claim representing email address of the users in the *id_token*. This claim must be named as either “email”, “emails” or “upn”.

These claims are processed at in the following order of priority to set as the *Primary Email Address* of the contact record in Dataverse:

1. email
1. emails
1. upn

When in use, "emailclaimsmapping" is also used to search for an existing contact (Primary Email Address field in Dataverse).

## Can I get access to tokens (ID or access) by using JavaScript?

No. The ID token provided by the identity provider isn't made available through any standard technique on the client side, and is only used for the purpose of authentication. However, if you're using the Implicit Grant flow, you can use the methods provided by your identity provider to get access to ID or access tokens.

For example, Azure AD provides [Microsoft Authentication Library](/azure/active-directory/develop/msal-overview) to achieve this scenario in clients.

## Can I use a custom OpenID Connect provider instead of Azure AD?

Yes. Portals supports any OpenID Connect provider that supports the standard [OpenID Connect specification](https://openid.net/specs/openid-connect-core-1_0.html).

### See also

[Configure an OpenID Connect provider for portals](configure-openid-provider.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]