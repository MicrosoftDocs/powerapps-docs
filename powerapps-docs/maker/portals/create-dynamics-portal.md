---
title: Create a portal in an environment containing customer engagement apps | Microsoft Docs
description: Instructions to create a portal in an environment containing customer engagement apps.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/08/2021
ms.author: nenandw
ms.reviewer: tapanm
---

# Create a portal in an environment containing customer engagement apps

If you select an environment that contains customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, and Dynamics 365 Project Service Automation), you can create the portals mentioned in [Portal templates](portal-templates.md).

> [!NOTE]
> - There can be only one portal of each type and for a language created in an environment. For more information, go to [creating additional portals](create-additional-portals.md).
> - To learn about the roles required to create a portal, read [Admin roles required for portal administrative tasks](admin/portal-admin-roles.md).

To create a portal in an environment containing customer engagement apps:

1.	Sign in to [Power Apps](https://make.powerapps.com).

2.	Select **Create** on the left pane and enter **portal** in the **Search templates** field to display all Dynamics 365 portal templates.

    > [!div class=mx-imgBorder]
    > ![Dynamics 365 portal templates](media/dynamics-portals.png "Dynamics 365 portal templates")  

3.	Select the required portal template.

4.	In the create portal window, enter a name for the portal and address for the website, and select a language from the drop-down list. When you're done, select **Create**. The creation process is same as described in the [Create a Dataverse starter portal](create-portal.md) section.

> [!NOTE]
> - If you have purchased an older portal add-on, and want to provision a portal using the add-on, you must go to the **Dynamics 365 Administration Center** page. More information: [Provision a portal using the older portal add-on](provision-portal-add-on.md)
> - If you have provisioned a portal using the older portal add-on, you can still customize and manage it from [make.powerapps.com](https://make.powerapps.com).
> - Provisioning portals from [make.powerapps.com](https://make.powerapps.com) does not consume the older portal add-ons. Also, these portals are not listed under the **Applications** tab on the **Dynamics 365 Administration Center** page.
> - A Dataverse starter portal cannot be created from the **Dynamics 365 Administration Center** page.
> - To disable portal creation in a tenant, see [Control portal creation in a tenant](control-portal-creation.md).
> - When you create a portal, a few solutions are installed and sample data is imported.

## Next steps

[Manage a portal](manage-existing-portals.md)

### See also

[Common problems and resolutions while creating a portal](create-common-problems.md) <br>
[Control portal creation in a tenant](control-portal-creation.md) <br>
[Microsoft Learn: Administer Power Apps portals](https://docs.microsoft.com/learn/paths/administer-portals/)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]