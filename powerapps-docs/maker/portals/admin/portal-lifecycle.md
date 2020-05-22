---
title: "About Power Apps portals lifecycle | MicrosoftDocs"
description: "Information about Power Apps portals lifecycle and converting it from trial to production."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/20/2020
ms.author: tapanm
ms.reviewer: tapanm
---

# About portal lifecycle

A portal is always created as a trial. A trial portal, which expires after 30 days, is useful for trying out its capabilities at no cost. After expiration, a portal is suspended and shut down. Seven days after suspension, the trial portal is deleted. On every change of portal lifecycle stage, such as nearing to suspension, suspended, deleted, and converted from trial to production, you'll receive notifications as a toast and through email.

As an administrator, you can convert a trial or suspended portal to a production portal. While converting a trial portal to production, ensure that the environment is also a production environment. You can’t convert a trial portal to production in a trial environment. If you delete the environment in which a trial portal is created, the portal is also deleted.

The first portal is free to be created in an environment in a tenant. If you need to create more than one portal, you must have 1 GB of unused storage space in the tenant.

## Stages in portal lifecycle

### Trial portal

A portal is always created as a trial portal. You can convert it to production from the Power Apps Portals admin center if you have the required licenses. For information on converting a trial portal to production, see [Convert a trial portal to production](#convert-a-trial-portal-to-production).

To convert a trial portal to production, the environment should have required add-ons for external users, or a license for internal users. For more information on licensing, see [Power Apps and Power Automate licensing FAQs](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq) and [Power Apps portals licensing](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#can-you-share-more-details-regarding-the-new-power-apps-portals-licensing).

### Suspended portal

You'll continue to see notifications in the Power Apps Portals admin center about the expiration of your trial portal. Trial portals expire after 30 days. If you don't convert your portal to production within the trial period, the portal is shut down and placed on the suspended status. You can't access your portal after its expiration.

However, the suspended portal can still be converted to production within seven days of suspension. 

### Deleted portal

If you don't convert your portal to production within the seven-day suspension period, the portal is deleted. The portal data isn't deleted from the environment, but the space used by the portal in an environment will be released, and you can create a new portal.

## Convert a trial portal to production

You can convert a trial portal to production from the notifications displayed in the Power Apps Portals admin center.

> [!NOTE]
> You must be assigned one of the following roles to convert a trial portal to production:
> - Global administrator
> - System administrator

When you open the [Power Apps Portals admin center](admin-overview.md) and navigate to the [Portal Details](portal-details.md) tab, you'll see the notification about the trial expiration displayed below the **Type** field.

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

## Convert existing portal to capacity-based model

> [!IMPORTANT]
> This feature is being deployed. During the deployment period, this feature may not be available.

You can convert your existing portal license to [capacity-based licensing model](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#can-you-share-more-details-regarding-the-new-power-apps-portals-licensing). To change your portal license to capacity-based model:

1. Go to [Portal details](portal-details.md).
1. Select **Change License**.

    ![Convert existing portal to capacity-based model](media/portal-lifecycle/convert-to-capacity-based-licensing.gif "Convert existing portal to capacity-based model")

Consider the following before changing your portal license:

- Your portal will restart and won't be available for a few minutes during license conversion. You may need to schedule downtime period for business users.
- Your environment must have appropriate [license](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#portals) available and assigned before you convert the license.
- You must have administrative privileges to convert the license.
- Only production environment can convert from existing to the capacity-based license. If you have a [trial environment](https://docs.microsoft.com/power-platform/admin/trial-environments), you must convert to production environment first.

## Considerations for add-on portals

Following conditions apply to portals [provisioned using portal add-on plan](../provision-portal-add-on.md) purchased earlier:

### Trial add-on portal

Trial add-on portal expires after 30 days. Expired portal is suspended for 7 days. The portal is deleted after suspension period ends. Trial add-on portal can still be converted to production during configured or suspended period.

### Production add-on portal

Production add-on portal expires at the end of purchased license period. Suspension period for a production add-on portal may vary depending on the purchased license plan. The portal is deleted after suspension period ends. You can extend the license of a production add-on portal while the portal is in configured or suspended state. If suspended, the portal can be converted to configured state after extending the license period.

> [!IMPORTANT]
> Suspension or deletion of a portal may cause functionality loss. Ensure timely license period extension of add-on portal nearing expiry to avoid suspension or deletion.

### Reset add-on portal

Follow the steps to [reset](reset-portal.md) the portal provisioned using a previously purchased older portal add-on plan.

## See also

[Power Apps portals FAQ](../faq.md)
