---
title: Provision a site using the older add-on
description: Instructions to provision a portal using the older portal add-on.
author: neerajnandwana-msft
ms.topic: conceptual
ms.collection: get-started
ms.date: 04/21/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Provision a site using the older add-on


[!INCLUDE[cc-pages-banner](../../includes/cc-pages-banner.md)]

If you have purchased an older site (portal) add-on, and want to provision a portal using the add-on, you must go to the **Dynamics 365 Administration Center** page and provision the portal.

> [!NOTE]
> - To provision a portal, you must be assigned either System Administrator or System Customizer role of the Microsoft Dataverse environment selected for the portal. You must also have the [required permissions](/azure/active-directory/develop/howto-create-service-principal-portal#required-permissions) to create and register an application in Azure AD. If you don't have the required permissions, contact the Global Administrator to update your permissions or ask the Global Administrator to provision the portal.
> - There can be only one portal of each type and for a language created in an environment. For more information, go to [creating additional portals](create-additional-portals.md).
> - To learn about the roles required to create add-on portals, read [Admin roles required for portal administrative tasks](admin/portal-admin-roles.md).

## Provision add-on portal

To provision an add-on portal:

1. Create a [Power Pages website](/power-pages/getting-started/create-manage).
1. In the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select **Convert to Production**. The Convert trial to production window will appear.
1. Choose the **Add-on** option and select the **Confirm** button.
    :::image type="content" source="media/provision-portal-add-on/add-on-available.png" alt-text="A screenshot of the Convert to production options inside Power Platform admin center with teh Add-ons license option selected.":::

The table below summarizes the features associated with each portal option:

| Feature                                | Customer Self-Service Portal | Partner Portal | Employee Self-Service Portal | Community Portal | Custom Portal |
|----------------------------------------|------------------------------|----------------|------------------------------|------------------|---------------|
| World Ready                            | *                            | *              | *                            | *                | *             |
| Multi-Language Support                 | *                            | *              | *                            | *                | *             |
| Portal Administration                  | *                            | *              | *                            | *                | *             |
| Customization and Extensibility        | *                            | *              | *                            | *                | *             |
| Theming                                | *                            | *              | *                            | *                | *             |
| Content Management                     | *                            |                | *                            | *                |               |
| Knowledge Management                   | *                            | *              | *                            | *                |               |
| Support/Case Management                | *                            |                | *                            | *                |               |
| Forums                                 | *                            |                | *                            | *                |               |
| Faceted Search                         | *                            |                | *                            |                  |               |
| Profile Management                     | *                            |                | *                            |                  |               |
| Subscribe to Forum Thread              | *                            |                | *                            |                  |               |
| Comments                               | *                            |                | *                            | *                |               |
| [!INCLUDE[pn-azure-shortest](../../includes/pn-azure-shortest.md)] AD Authentication                |                              |                | *                            |                  |               |
| Ideas                                  |                              |                |                              | *                |               |
| Blogs                                  |                              |                |                              | *                |               |
| Project Service Automation Integration |                              | *              |                              |                  |               |
| Field Service Integration              |                              | *              |                              |                  |               |
| Partner Onboarding                     |                              | *              |                              |                  |               |
| Portal Base                            |  *                           | *              |  *                           | *                | *             |
| Portal Workflows                       |  *                           | *              |  *                           | *                | *             |
| Web Notifications                      |  *                           | *              |  *                           | *                | *             |
| [!INCLUDE[cc-microsoft](../../includes/cc-microsoft.md)] Identity                     |     *                         |  *              |     *                         |   *               | *             |
| Identity Workflows                     | *                            |  *             |     *                         |   *               | *             |
| Multistep Forms                              |  *                            | *               |    *                          | *                 | *             |
| Feedback                               |   *                           |  *              |  *                            | *                 | *             |
||

## Troubleshoot provisioning

Sometimes the package installation process or URL creation process can error out. In these cases, the processes can be restarted.

If *Name*-Configuring changes to *Name*-Provisioning Failed, you need to restart the provisioning process.

1. Go to the **Applications** page, and select the portal.
2. Select the blue pencil button labeled **Manage**.
3. Choose one of the following options:

   - **Restart Provisioning**: Restarts the installation process with the configuration that was previously defined.

   - **Change Values and Restart Provisioning**: Lets you change some of the values before restarting the provisioning process.

If the package installation has failed, the portal administrator page will open without any issues, but navigating to the actual portal URL will show a message Getting set up. To confirm this:

1. Go to the Solution Management page of the **Dynamics 365 Administration Center** page and check that the package status is **Install Failed**. 

2. If the package status is **Install Failed**, try retrying the installation from the solution page. Also, be sure to check that a system administrator is installing the solution with the default language in Dataverse set to the language the portal should be installed in.

> [!NOTE]
> Some solutions have prerequisites for their installation, so an installation will fail if the prerequisites are not met. For example, to install the Partner Field Service for a partner portal, the Partner Portal and Field Service solutions must have already been installed. If you attempt to install the Partner Field Service first, the installation will fail and give you an error message.

## Change portal type and audience

After you've provisioned a portal, the option to change the portal audience is disabled.

However, you can change the audience and type of portal after it's provisioned by following the steps in [Change the Dynamics 365 instance, audience, or type of portal](admin/change-dynamics-instance.md).

> [!NOTE]
> - It's recommended to reset and provision your portal again to change the audience, type of portal, organization, and so on. More information: [Reset a portal](admin/reset-portal.md)
> - The changing of Dynamics 365 instance is applicable only to the portals provisioned using the older portal add-ons.

## Next steps

[Manage a portal](manage-existing-portals.md)

### See also

[Administer Power Apps portals](/training/paths/administer-portals/)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
