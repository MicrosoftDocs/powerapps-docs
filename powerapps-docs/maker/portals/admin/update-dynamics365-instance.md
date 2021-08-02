---
title: Update the Dynamics 365 instance for your portal
description: Learn how to update the Dynamics 365 instance for your portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Update the Dynamics 365 instance for your portal

You can use the Power Platform admin center to update the Dynamics 365 instance for your portal.

> [!IMPORTANT]
> When changing the Dynamics 365 instance for your portal, ensure that the new instance is from the same [region](/power-platform/admin/regions-overview) as the current instance. Changing the Dynamics 365 instance for Power Apps portals across regions isn't supported.

1. Using one of the methods described in the [Manage portals from the Power Platform admin center](power-platform-admin-center.md) article, select **Manage** to manage your portal.

1. On the left pane, select **Manage Dynamics 365 Instance**.

1. Select **Update Dynamics 365 Instance**.

    ![Update your Dynamics 365 instance.](media/power-platform-admin-center/update-dynamics365-instance.png "Update your Dynamics 365 instance")

1. Select your existing instance and portal.

    ![Select your Dynamics 365 instance.](media/power-platform-admin-center/select-dynamics365-instance.png "Select your Dynamics 365 instance")

1. Select **OK**.

1. Select **Submit** to confirm.

    ![Submit Dynamics 365 solution update.](media/power-platform-admin-center/submit-selection.png "Submit Dynamics 365 solution update")

    You'll see a confirmation that the update request is in progress.

    ![Update request submitted.](media/power-platform-admin-center/update-request-submitted.png "Update request submitted")

The update might take a while after you select **Submit**. More information: [Upgrade a portal](upgrade-portal.md)

## Next steps

[Configure portal details](portal-details.md)

### See also

[Upgrade a portal](upgrade-portal.md) <br>
[Administer Microsoft Power Platform](/power-platform/admin/admin-documentation) <br>
[Manage Dynamics 365 apps](/power-platform/admin/manage-apps)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]