---
title: "Power Apps Portals settings on Power Platform admin center | MicrosoftDocs"
description: "Information about Power Apps Portals settings on Power Platform admin center."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/04/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# Manage portals from Power Platform admin center

You can now manage portals in the Power Platform admin center. The Power Platform admin center helps you manage both capacity-based and add-on portals. You an also see information such as how many days a trial portal has before it expires. For more information about the portal licensing, see [licensing FAQ](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#portals) and [portal differences](https://docs.microsoft.com/powerapps/maker/portals/faq#what-is-the-difference-between-power-apps-portals-dynamics-365-portals-and-add-on-portals).

You can manage the portals in Power Platform admin center in two different ways. You can manage all portals for the current tenant from **Resources** -> **Portals** option. And you can manage portals for a specific environment from **Environments** option.

## Manage all portals for a tenant

To see a list of all portals for your tenant:

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. Select **Resources** and then **Portals** from the left-side menu.

    ![Portals option on Power Platform admin center](media/power-platform-admin-center/manage-portals-all-environments.png "Portals option on Power Platform admin center")

1. Select a portal.

1. To manage a portal, select **More portal actions** (**...**) and then select **Manage**. Alternatively, you can also select the portal and then select **Manage** from the top navigation:

    ![Manage portal from Power Platform admin center](media/power-platform-admin-center/portals-manage-ppac.png "Manage portal from Power Platform admin center")

To continue and configure portal details, refer [portals details](https://docs.microsoft.com/powerapps/maker/portals/admin/portal-details).

## Manage all portals for an environment

Follow these steps to see a list of all portals for your environment.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. Select **Environments** from the left navigation:

    ![Environments list](media/power-platform-admin-center/environments-list.png "Environments list")

1. Hover over and select the environment name hyperlink to open environments details:

    ![Select environment](media/power-platform-admin-center/select-environment.png "Select environment")

1. Select **Portals** under the **Resources** option from the right-side of the screen:

    ![Environments details](media/power-platform-admin-center/environment-details.png "Environments details")

1. You'll see a list of Portals installed in the selected environment.

    ![Portals specific to an environment](media/power-platform-admin-center/environments-portals.png "Portals specific to an environment")

1. To manage a portal, select **More portal actions** (**...**) and then select **Manage**. Alternatively, you can also select the portal and then select **Manage** from the top navigation:

    ![Manage portal specific to an environment](media/power-platform-admin-center/manage-environments-portal.png "Manage portal specific to an environment")

To continue and configure portal details, refer [portals details](https://docs.microsoft.com/powerapps/maker/portals/admin/portal-details).

## Manage portal add-on

The ability to manage portal as explained above using **Power Platform admin center** replaces the following earlier functionality:

![Manage add-on portal](media/power-platform-admin-center/old-admin-center.png "Manage add-on portal")

### Portal types

The following table explains different types of portals that you can see listed on admin center with descriptions:

| **Type**            | **Description**                                                                    |
|---------------------|------------------------------------------------------------------------------------|
| Production          | Production portal based on capacity-based license.                                  |
| Trial (n days)      | Trial portal based on capacity-based license with n days remaining for suspension. |
| Production (add-on) | Production portal based on add-on license.                                          |
| Trial (add-on)      | Trial portal based on add-on license.                                               |

### Portal status

A portal can be in *Configured*, *Suspended*, or *Not-configured* status. The following table describes each status:

| **Status**     | **Description**                                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Configured     | This portal has been configured to an environment.                                                                              |
| Suspended      | This portal has been suspended due to trial period over. And this portal will be deleted in 7 days, if not converted to production. |
| Not-configured | This app is ready to be configured to an environment.                                                                           |

> [!NOTE]
> You can [create a new portal](https://docs.microsoft.com/powerapps/maker/portals/provision-portal-add-on) if the portal add-on status is *Not-configured*. The status will change to *Configured* after the portal is provisioned.

## Update Power Apps portal solution

You can update Power Apps portal solution using the Power Platform admin center.

To update the portal solution:

1. Go to manage your portal using one of the methods explained earlier in this article.

1. Select **Manage Dynamics 365 Instance** from left navigation pane.

1. Select **Update Dynamics 365 Instance**.

    ![Update Dynamics 365 Instance](media/power-platform-admin-center/update-dynamics365-instance.png "Update Dynamics 365 Instance")

1. Select your existing instance and portal.

    ![Select Dynamics 365 Instance](media/power-platform-admin-center/select-dynamics365-instance.png "Select Dynamics 365 Instance")

1. Select **OK**.

1. Select **Submit** to confirm.

    ![Submit Dynamics 365 solution update](media/power-platform-admin-center/submit-selection.png "Submit Dynamics 365 solution update")

1. You'll see a confirmation of the update request in progress.

    ![Request submitted to update](media/power-platform-admin-center/update-request-submitted.png "Request submitted to update")

The update to portal solution may take a while once submitted.

For additional information, go to [Upgrade a portal](upgrade-portal.md).

## Next steps

Configure [portals details](https://docs.microsoft.com/powerapps/maker/portals/admin/portal-details).

### See also

- Manage apps with [Power Platform admin center](https://docs.microsoft.com/power-platform/admin/manage-apps)
- [Upgrade a portal](upgrade-portal.md)
