---
title: "Reset a portal | MicrosoftDocs"
description: "Learn how to reset a portal."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: shjais
ms.reviewer:
---

# Reset a portal

Once a portal is provisioned, you might need to delete resources from your portal under certain circumstances, such as if you move your organization to another tenant or another datacenter or if you want to remove the portal from your organization.

To do this, you can reset your portal, which will delete all the hosted resources associated with it. Then you can provision the portal again. Once the reset operation is finished, your portal URL will not be accessible anymore.

It is important to note that resetting your portal doesn’t remove portal configuration or solutions present in your instance and they will remain as is.

You can reset a completely configured portal, or a portal for which provisioning or updating of an instance has failed.

To reset a configured portal:

1.	Open [PowerApps Portals admin center](admin-overview.md).

2.	Go to **Portal Actions** > **Reset Portal**.

    > [!div class=mx-imgBorder]
    > ![Reset a portal](../media/reset-portal.png "Reset a portal")

3.	Select **Reset** in the confirmation window.

> [!NOTE]
> - If you don't have appropriate permissions on an associated Azure Active Directory application, an error is displayed. You must contact the global administrator for the appropriate permissions.
> - If you have provisioned a portal using the older portal add-on and the portal is reset successfully, the portal name and its status on the **Applications** tab on the **Dynamics 365 Administration Center** page does not change. For example, if your portal name and status were Portal 1 and Configured respectively, then after resetting the portal, these values do not change. If you want to change the portal name, you can change it on the **Portal Details** tab in the PowerApps Portals admin center. However, the status value cannot be reverted to Not Configured.
> - It is important to note that the portal's status on the **Applications** tab does not represent its provisioning status and does not affect the functioning of your portal. It just shows whether you have ever accessed the PowerApps Portals admin center for that corresponding portal or not.

If your portal is not provisioned correctly, it goes into an error state and the following screen is displayed. In this case, you can also reset the portal by selecting **Reset Portal** on the error screen.

> [!div class=mx-imgBorder]
> ![Error while provisioning a portal](../media/provision-portal-error.png "Error while provisioning a portal")

## Troubleshooting

This section provides information about troubleshooting issues while resetting a portal.

### Reset request could not be submitted

If a portal reset request could not be submitted, an error is displayed as shown in the following image. In this case, you must close and reopen the PowerApps Portals admin center, and try to reset the portal again. If the issue persists, contact Microsoft support.

> [!div class=mx-imgBorder]
> ![Error while resetting a portal](../media/reset-portal-request-error.png "Error while resetting a portal")

### Reset portal job fails

If a reset portal job fails, an error message is displayed along with the **Reset Portal** action.

> [!div class=mx-imgBorder]
> ![Error while resetting a portal](../media/reset-portal-error.png "Error while resetting a portal")

Typically, these are transient errors and you must select **Reset Portal** to restart the job. If the issue persists, contact Microsoft support.

