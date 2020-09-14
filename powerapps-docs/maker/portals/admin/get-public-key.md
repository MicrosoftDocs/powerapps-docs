---
title: "Download public key of a portal | MicrosoftDocs"
description: "Learn how to download public key of a portal."
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: nenandw
ms.reviewer: tapanm
---

# Download public key of portal

The public key of a portal is used to configure Live Assist for customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, and Dynamics 365 Project Service Automation) to work with authenticated visitors for a portal. [Live Assist](https://www.cafex.com/en/products/live-assist-dynamics-365/), by CafeX, provides a chat solution through which users can embed live chat assistance in their portal. More information on how to use the public key to embed a chat on a portal: [Authenticated Visitors in the Dynamics Customer Portal](https://www.liveassistfor365.com/en/support/authenticated-visitors-in-the-dynamics-customer-portal/)

1. Open [Power Apps Portals admin center](admin-overview.md).

2.	Go to **Portal Actions** > **Get Public Key**. The key is displayed.

    > [!div class=mx-imgBorder]
    > ![Get public key of a portal](../media/get-public-key.png "Get public key of a portal")

3.	Select **Download as Text** to download the key in a text file.

Alternately, you can also get the public key by going to the URL: `<portal_base_URL>/_ services/auth/publickey` 

> [!NOTE]
> If the portal is currently being provisioned or the package install is not finished in the organization, an error is displayed if you try to download the public key. You must wait until portal provisioning is complete and the portal is up and running.
