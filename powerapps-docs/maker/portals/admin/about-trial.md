---
title: "About PowerApps Portals trial | MicrosoftDocs"
description: "Information about working with PowerApps Portals trial and converting it to production."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: shjais
ms.reviewer:
---

# About trial portals

When you create a portal, it is always created as a trial. A trial portal is useful for trying out its capabilities at no cost. Trial portals expire after 30 days. After expiration, the portal is put under the suspended state and is shutdown . After seven days of suspension, the trial portal is deleted.

As an administrator, you can convert a trial or a suspended portal to a production portal. While converting a trial portal to production, ensure that the environment is also a production environment. You can’t convert a trial portal to production in a trial environment.

If you delete the environment in which a trial portal is created, the portal is also deleted. If a trial portal is not used for 15 days, it is put under the suspended state.
The first portal is free to be created in an environment in a tenant. If you need to create more than one portal, you must have 1 GB of unused storage space in the tenant.

## License requirements

`To be added when info is available`

## Convert a trial portal to production

You can convert a trial portal to production from the notifications displayed in PowerApps Portals admin center.

> [!NOTE]
> You must be assigned one of the following roles to convert a trial portal to production:
> - Global administrator
> - System administrator

When you open [PowerApps Portals admin center](admin-overview.md) and navigate to the [Portal Details](portal-details.md) tab, the notification about trial expiration is displayed below the **Type** field.

> [!div class=mx-imgBorder]
> ![Trial notification on Portal Details tab](../media/admin-center-convert-notif.png "Trial notification on Portal Details tab")

On other pages in the admin center, the notification is displayed at the top of the page.

> [!div class=mx-imgBorder]
> ![Trial notification on other tabs](../media/admin-center-convert-notif-all.png "Trial notification on other tabs")

To convert your trial portal to production:

1.	In the notification, select **Convert**.

2.	Select **Confirm**.

    > [!div class=mx-imgBorder]
    > ![Trial to production confirmation](../media/trial-to-prod-confirm.png "Trial to production confirmation")
