---
title: Working with expired tokens 
description: Learn how to manage tokens in Power Apps, Logic Apps, and Power Automate to ensure seamless connections even after credential changes or token revocations.
author: lancedMicrosoft

ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 04/02/2025
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - lancedMicrosoft

---

# Manage expired tokens

This article explains how tokens are managed to ensure apps continue to function smoothly when credentials change.

API Hub handles connections differently for Power Apps, Logic App, and Power Automate. When you change your credentials, Power Apps automatically reauthenticates using a new token, while Logic Apps and Power Automate might run into issues because they use stored tokens that can become stale.


## Manage tokens in Power Apps

When a connection is invoked from Power Apps, API Hub uses the OBO (on-behalf-of) token sent in the 'invoke' request from Power Apps. API Hub exchanges the OBO token for a token to the target service. The OBO token is generated and validated during each Power Apps session before invoking the connector.

For example, if a user **changes their password**, all tokens are revoked. When Power Apps directly invokes the connection, it uses the new token in the 'invoke' request to proceed. The request to the connector succeeds without the user having to reauthenticate the connection.

## Manage tokens in Logic Apps and Power Automate

When a connection is invoked from Logic Apps or Power Automate, API Hub uses the stored token in the connection to exchange it for a token to the target service.

For example, **changing passwords or enforcing an MFA policy** revokes all tokens. A Logic Apps or Power Automate SSO (single sign-on) connection call fails during token exchange because the tokens aren't marked as broken, and the token stored in the connection is stale.

## Refresh tokens in Power Apps, Logic Apps, and Power Automate

Power Apps automatically renews or reauthenticates any connection that is broken. However, connections aren't marked as broken when tokens are revoked. They're marked as broken when the token exchange on API Hub fails. 

Therefore, Logic Apps and Power Automate must first attempt to run the connector with expired tokens. This action causes the connection to be marked as broken. Once Power Apps encounters a broken connection, it refreshes its local cache of connections, and the connection is repaired.