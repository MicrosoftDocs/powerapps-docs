---
title: "About the Power Apps portals lifecycle | MicrosoftDocs"
description: "Information about the Power Apps portals lifecycle and converting it from trial to production."
author: neerajnandwana-ms
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/29/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# About the portal lifecycle

A portal is always created as a trial. A trial portal, which expires after 30 days, is useful for trying out its capabilities at no cost. After it expires, the portal is suspended and shut down. Seven days after it's suspended, the trial portal is deleted. You'll be notified at every stage of the portal lifecycle&mdash;nearing suspension, suspended, deleted, and converted from trial to production&mdash;through toast notifications and email.

As an administrator, you can convert a trial or suspended portal to a production portal. When converting a portal from trial to production, you must ensure that the environment is also a production environment. You can't convert a trial portal to a production portal in a trial environment. If you delete the environment in which a trial portal is created, the portal is also deleted.

The first portal is free to be created in an environment in a tenant. If you need to create more than one portal, you must have 1 GB of unused storage space in the tenant.

## Stages in the portal lifecycle

### Trial portal

Every portal begins as a trial portal that expires after 30 days. You can convert it to a production portal from the Power Apps Portals admin center if you have the required licenses. More information: [Convert a portal from trial to production](#convert-a-portal-from-trial-to-production)

To convert a trial portal to a production portal, the environment should have required add-ons for external users or a license for internal users. More information: [Power Apps and Power Automate licensing FAQs](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq) and [Power Apps portals licensing](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#can-you-share-more-details-regarding-the-new-power-apps-portals-licensing)

### Suspended portal

You'll continue to see notifications in the Power Apps Portals admin center about the expiration of your trial portal. Trial portals expire after 30 days. If you don't convert your portal to production within the trial period, the portal is shut down and placed in suspended status.

You can't access your portal after it expires. However, you can still convert the suspended portal to production within seven days of suspension.

### Deleted portal

If you don't convert your portal to production within the seven-day suspension period, the portal is deleted. The portal data isn't deleted from the environment, but the space used by the portal in the environment will be released, and you can create a new portal.

## Convert a portal from trial to production

You can convert a trial portal to a production portal from the notifications displayed in the Power Apps Portals admin center.

> [!NOTE]
> You must be assigned one of the following roles to convert a portal from trial to production:
> - Global administrator
> - System administrator

When you open the [Power Apps Portals admin center](admin-overview.md) and go to the **[Portal Details](portal-details.md)** tab, you'll see the notification about the trial expiration displayed below the **Type** field.

> [!div class=mx-imgBorder]
> ![Trial notification on the Portal Details tab](../media/admin-center-convert-notif.png "Trial notification on the Portal Details tab")

On other pages in the admin center, the notification is displayed at the top of the page.

> [!div class=mx-imgBorder]
> ![Trial notification on other pages](../media/admin-center-convert-notif-all.png "Trial notification on other pages")

To convert your portal from trial to production:

1.	In the notification, select **Convert**.

2.	Select **Confirm**.

    > [!div class=mx-imgBorder]
    > ![Trial to production confirmation](../media/trial-to-prod-confirm.png "Trial to production confirmation")

## Convert an existing portal to a capacity-based model

> [!IMPORTANT]
> This feature is being deployed. During the deployment period, this feature may not be available.

You can convert your existing portal license to [capacity-based licensing model](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#can-you-share-more-details-regarding-the-new-power-apps-portals-licensing). To change your portal license to capacity-based model:

1. Go to [Portal Details](portal-details.md).
1. Select **Change License**.

    ![Convert an existing portal to a capacity-based model](media/portal-lifecycle/convert-to-capacity-based-licensing.gif "Convert an existing portal to a capacity-based model")

Consider the following before changing your portal license:

- Your portal will restart and won't be available for a few minutes during license conversion. You might need to schedule this for a downtime period for business users.
- Your environment must have an appropriate [license](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#portals) available and assigned before you convert the license.
- You must have administrative privileges to convert the license.
- Only production environments can be converted from an existing license to a capacity-based license. If you have a [trial environment](https://docs.microsoft.com/power-platform/admin/trial-environments), you must convert it to a production environment first.

## Considerations for add-on portals

The following sections describe the conditions that apply to portals that were [provisioned by using the portal add-on plan](../provision-portal-add-on.md).

### Trial add-on portal

A trial add-on portal expires after 30 days. An expired portal is suspended for seven days. The portal is deleted after the suspension period ends. A trial add-on portal can still be converted to a production portal during the period when it has either been configured to an environment or suspended.

### Production add-on portal

A production add-on portal expires at the end of the purchased license period. The suspension period for a production add-on portal can vary depending on the license plan you purchased. The portal is deleted after the suspension period ends. You can extend the license of a production add-on portal while the portal is in a configured or suspended state. If it has been suspended, the portal can be converted to a configured state after you extend the license period.

> [!IMPORTANT]
> To avoid functionality loss by having your portal suspended or deleted, ensure that you've extended the license period in a timely manner, well before expiry.

### Reset add-on portal

Follow the steps in [Reset a portal](reset-portal.md) to reset a portal that was provisioned by using a previously purchased, portal add-on plan.

### See also

[Power Apps portals FAQ](../faq.md)
