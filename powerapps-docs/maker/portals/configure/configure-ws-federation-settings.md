---
title: Configure a WS-Federation provider for portals with AD FS
description: Learn how to configure WS-Federation provider for a portal with AD FS.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
    - dileepsinghmicrosoft
---

# Configure a WS-Federation provider for portals with AD FS

> [!IMPORTANT]
> The steps for the configuration of Active Directory Federation Services (AD FS) might vary depending on the version of your AD FS server.

## Create an AD FS relying party trust

1. Using the AD FS Management tool, go to **Trust Relationships** > **Relying Party Trusts**.

    1.  Select **Add Relying Party Trust**.
    2.  Welcome: Select **Start**.
    3.  Select Data Source: select **Enter data about the relying party manually**, and then select **Next**.
    4.  Specify Display Name: Enter a name, and then select **Next**.
        <br> Example: `https://portal.contoso.com/`
    5.  Choose Profile: Select **AD FS 2.0 profile**, and then select **Next**.
    6.  Configure Certificate: Select **Next**.
    7.  Configure URL: Select the **Enable support for the WS-Federation Passive protocol** check box.<br>
    Relying party WS-Federation Passive protocol URL: Enter `https://portal.contoso.com/signin-federation`<br> Note that AD FS requires that the portal run on HTTPS.
    
    > [!NOTE]
    > The resulting endpoint has the following settings:
    > - Endpoint type: **WS-Federation**
    > - Binding: **POST**
    > - Index: n/a (0)
    > - URL: `https://portal.contoso.com/signin-federation`
    
    8.  Configure Identities: Enter `https://portal.contoso.com/`, select **Add**, and then select **Next**.
        If applicable, you can add more identities for each additional relying party portal. Users can authenticate across any or all available identities.
    9.  Choose Issuance Authorization Rules: Select **Permit all users to access this relying party**, and then select **Next**.
    10.  Ready to Add Trust: Select **Next**.
    11.  Select **Close**.

2. Add the **Name ID** claim to the relying party trust:

    **Transform [!INCLUDE[pn-ms-windows-short](../../../includes/pn-ms-windows-short.md)] account name** to **Name ID** claim (Transform an Incoming Claim):
    - Incoming claim type: Windows account name
    - Outgoing claim type: Name ID
    - Outgoing name ID format: Unspecified
    - Pass through all claim values

## Configure the WS-Federation provider

After setting up the AD FS relying party trust, you can follow the steps in [Configure a WS-Federation provider for portals](configure-ws-federation-provider.md).

### See also

[Configure a WS-Federation provider for portals with Azure AD](configure-ws-federation-settings-azure-ad.md)  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]