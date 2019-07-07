---
title: "Download public key of Dynamics 365 for Customer Engagement portals | MicrosoftDocs"
description: "Learn how to download public key of a portal."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/15/2019
ms.author: shjais
ms.reviewer:
---

# Download public key of portal

The public key of a portal is used to configure Live Assist for Dynamics 365 for Customer Engagement to work with authenticated visitors for a portal. [Live Assist](https://www.cafex.com/en/products/live-assist-dynamics-365/), by CafeX, provides a chat solution through which users can embed live chat assistance in their portal. More information on how to use the public key to embed a chat on a portal: [Authenticated Visitors in the Dynamics Customer Portal](https://www.liveassistfor365.com/en/support/authenticated-visitors-in-the-dynamics-customer-portal/)

1.	Go to the Dynamics 365 page and select the **Applications** tab.

2.	Select the name of the portal you want to get the public key, and then select **Manage**.

3.	Go to **Portal Actions** > **Get Public Key**. The key is displayed.

    ![Get public key of a portal](media/get-public-key.png "Get public key of a portal")

4.	Select **Download as Text** to download the key in a text file.

You can also get the public key by going to the URL: `<portal_base_URL>/_ services/auth/publickey` 

> [!NOTE]
> If the portal is currently being provisioned or the package install is not finished in the organization, an error is displayed if you try to download the public key. You must wait until portal provisioning is complete and the portal is up and running.
