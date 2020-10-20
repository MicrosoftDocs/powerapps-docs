---
title: "Configure WS-Federation provider for a portal with AD FS.  | MicrosoftDocs"
description: "Instructions to configure WS-Federation provider for a portal with AD FS."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/20/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Configure WS-Federation provider for a portal with AD FS

> [!IMPORTANT]
> The steps for the configuration of AD FS may vary depending on the version of your AD FS server.

Using the AD FS Management tool, go to **Trust Relationships** &gt; **Relying Party Trusts**.

1.  Select **Add Relying Party Trust**.
2.  Welcome: Select **Start**.
3.  Select Data Source: Select **Enter data about the relying party manually**, and then select **Next**.
4.  Specify Display Name: Enter a **name**, and then select **Next**.
    <br> Example: `https://portal.contoso.com/`
5.  Choose Profile: Select **AD FS 2.0 profile**, and then select **Next**.
6.  Configure Certificate: Select **Next**.
7.  Configure URL: Select the **Enable support for the WS-Federation Passive protocol** check box.

Relying party WS-Federation Passive protocol URL: Enter `https://portal.contoso.com/signin-federation`

-   Note: AD FS requires that the portal run on **HTTPS**.

    > [!Note]
    > The resulting endpoint has the following settings:
    > Endpoint type: **WS-Federation**
    > -   Binding: **POST**
    > -   Index: n/a (0)
    > -   URL: `https://portal.contoso.com/signin-federation`

8.  Configure Identities: Specify `https://portal.contoso.com/`, select **Add**, and then select **Next**.
    If applicable, more identities can be added for each additional relying party portal. Users can authenticate across any or all of the available identities.
9.  Choose Issuance Authorization Rules: Select **Permit all users to access this relying party**, and then select **Next**.
10.  Ready to Add Trust: Select **Next**.
11.  Select **Close**.

Add the **Name ID** claim to the relying party trust:

**Transform [!INCLUDE[pn-ms-windows-short](../../../includes/pn-ms-windows-short.md)] account name** to **Name ID** claim (Transform an Incoming Claim):
- Incoming claim type: Windows account name
- Outgoing claim type: Name ID
- Outgoing name ID format: Unspecified
- Pass through all claim values

### Configure the WS-Federation provider

After setting up the AD FS relying party trust, you can follow the steps to [configure the WS-Federation provider](configure-ws-federation-provider.md).

### See also

- [Configure WS-Federation provider for portals](configure-ws-federation-provider.md)
- [Example: Configure WS-Federation for portals with Azure Active Directory](configure-ws-federation-settings-azure-ad.md)
