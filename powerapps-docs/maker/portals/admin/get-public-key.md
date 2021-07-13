---
title: Download public key of a portal
description: Learn how to download public key of a portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Download public key of portal

The public key of a portal is used to configure Live Assist for customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, and Dynamics 365 Project Service Automation) to work with authenticated visitors for a portal. [Live Assist](https://www.cafex.com/en/products/live-assist-dynamics-365/), by CafeX, provides a chat solution through which users can embed live chat assistance in their portal. More information on how to use the public key to embed a chat on a portal: [Authenticated Visitors in the Dynamics Customer Portal](https://www.liveassistfor365.com/en/support/authenticated-visitors-in-the-dynamics-customer-portal/)

> [!TIP]
> To learn about the roles required to perform this task, read [Admin roles required for portal administrative tasks](portal-admin-roles.md).

1. Open [Power Apps portals admin center](admin-overview.md).

2.	Go to **Portal Actions** > **Get Public Key**. The key is displayed.

    > [!div class=mx-imgBorder]
    > ![Get public key of a portal.](../media/get-public-key.png "Get public key of a portal")

3.	Select **Download as Text** to download the key in a text file.

Alternately, you can also get the public key by going to the URL: `<portal_base_URL>/_ services/auth/publickey` 

> [!NOTE]
> If the portal is currently being provisioned or the package install is not finished in the organization, an error is displayed if you try to download the public key. You must wait until portal provisioning is complete and the portal is up and running.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]