---
title: Change the Dynamics 365 instance, audience, or type of portal
description: "Learn how to change the Dynamics 365 instance, audience, or type of a portal."
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 02/10/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---
 
# Change the Dynamics 365 instance, audience, or type of portal

After your portal is created and provisioned, you can change the details of your Dynamics 365 instance and portal.

To learn about the roles required to perform this task, read [Admin roles required for portal administrative tasks](portal-admin-roles.md).

1. Go to the **Dynamics 365 Administration Center** page, and then select the **Applications** tab.

2. Select the name of the portal you want to edit, and then select **Manage**.

3. Select the **Manage Dynamics 365 Instance** tab. On this page, you can review the Dynamics 365 instance that is currently linked to your portal.

4. Select **Update Dynamics 365 Instance**. In the dialog box, use the provided fields to change your Dynamics 365 instance, portal development status, portal language, or your portal administrator. You can also keep the same Dynamics 365 instance, but change the portal audience or type of portal.

5. Select the ![Confirm action.](../media/confirm-action-icon.png "Confirm action") button to confirm your changes.  

   > [!div class="mx-imgBorder"]
   > ![Change Dynamics 365 instance.](../media/change-dynamics-365-instance.png "Change Dynamics 365 instance")  

> [!NOTE]
> You may be required to [reload SSL certificates](manage-ssl-certificates.md) after you have updated the Dynamics 365 instance. Go to **Manage SSL certificates** in the [Power Apps portals admin center](admin-overview.md) to verify if custom SSL certificates need to be reloaded.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]