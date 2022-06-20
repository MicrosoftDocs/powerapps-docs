---
title: Portal checker startup issue
description: Learn about Portal Checker diagnostics results for startup issue.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 06/20/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - dileepsinghmicrosoft
    - ProfessorKendrick
---

# Portal doesn't load and displays server error

This issue can be caused by several different reasons, such as when a portal isn't able to connect to the underlying Dataverse environment, the Dataverse environment doesn't exist or its URL has changed, or when a request to the Dataverse environment has timed out. When you run the Portal Checker tool, it will try to determine the exact reason and point you to the correct mitigation. 

Below is a list of common causes for this error and their corresponding mitigation steps:

## URL of the connected Microsoft Dataverse environment has changed 

This happens when the URL of the Dataverse environment is changed by a user after a portal is provisioned against the organization. To fix this issue, update the Dynamics 365 URL:

1. Open [Power Apps portals admin center](admin-overview.md).
1. Go to **Portal Actions** > **Update Dynamics 365 URL**. 

Once this action is successfully completed, your Dataverse environment URL will be updated and your portal will start working.

## Microsoft Dataverse environment connected to your portal is in administration mode

This issue occurs when the Dataverse environment is put in administration mode either when changing the organization from production to sandbox mode or manually by an organization administrator.

If this is the cause, you can disable administration mode by following the steps listed [here](/dynamics365/admin/manage-sandbox-instances#administration-mode). Once administration mode is disabled, your portal should work.

## Authentication connection between Dataverse environment and portal is broken

This issue occurs when the authentication connection between the Dynamics 365 organization and the portal is broken because the Dataverse environment was either restored from a backup or was deleted and recreated from a backup. To fix this issue:

1. Open [Power Apps portals admin center](admin-overview.md).
1. In the **Portal Details** tab, select **Off** from the **Portal State** list.
1. Select **Update**.
1. Select **On** from the **Portal State** list.
1. Select **Update**. 

Once these steps are completed, the portal restarts and can now make an authentication connection.

In certain situations, especially if the organization ID has changed after the restore operation (or if you reprovisioned the organization), these mitigation steps won't work. In these situations, you can reset and reprovision the portal against the same instance. For information on how to reset a portal, see [Reset a portal](reset-portal.md).

## Request to Microsoft Dataverse environment has timed out

This issue can occur if the API request to your Dataverse environment has timed out. This issue should automatically mitigate itself once the API request starts working. You can also try restarting the portal:

1. Open [Power Apps portals admin center](admin-overview.md).
1. Go to **Portal Actions** > **Restart**.

If restarting the portal doesn't work and the issue continues for a long period of time, contact Microsoft Support for help.

## Website binding not found

This issue occurs when the website binding records for the portal are deleted from the underlying Dataverse environment and the portal isn't able to create binding automatically. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. Go to **Portals** > **Website Bindings**.
1. Delete all the website binding records that are pointing to your portal. The **Sitename** field helps you to identify the website binding records for your portal.
1. Restart the portal.

Once you complete these steps, your portal will restart and should recreate website binding records automatically.

There are situations in which the portal won't be able to recreate website binding records automatically, such as when the GUID of the website record available in your instance is different than the one created during default installation of your portal. In this situation, do the following:

1. Delete all website binding records related to your portal.
1. Create a website binding record manually with the following values:

      - **Name**: This can be any string.
      - **Website**: Select the website record that you want to be rendered on your portal.
      - **Sitename**: Type in the host name of your portal (i.e portal URL without `https://` in the beginning). If your portal is using a custom domain name, use that custom domain name here.
      - Leave all other fields blank.
1. Once website binding record is recreated, restart your portal from the Power Apps portals admin center.

## An unexpected error has occurred while trying to connect to your Microsoft Dataverse environment

This situation can arise because of some unexpected issue. To mitigate this situation, try resetting or reprovisioning the portal. For information on how to reset a portal, see [Reset a portal](reset-portal.md).

If neither a portal reset nor reprovision solves the issue, contact Microsoft Support for help.

### See also

[Run Portal Checker](portal-checker.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
