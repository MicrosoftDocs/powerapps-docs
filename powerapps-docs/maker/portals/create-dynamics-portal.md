---
title: Create a portal in an environment containing model-driven apps in Dynamics 365 | Microsoft Docs
description: Instructions to create a a portal in an environment containing model-driven apps in Dynamics 365.
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: shjais
ms.reviewer:
---

# Create a portal in an environment containing model-driven apps in Dynamics 365

If you select an environment that contains model-driven apps in Dynamics 365 (such as Dynamics 365 Sales and Dynamics 365 Customer Service), you can create the portals mentioned in [Portal templates](portal-templates.md).

1.	Sign in to [PowerApps](https://make.powerapps.com).

2.	Select **Create** on the left pane and enter **portal** in the **Search templates** field to display all Dynamics 365 portal templates.

    > [!div class=mx-imgBorder]
    > ![Dynamics 365 portal templates](media/dynamics-portals.png "Dynamics 365 portal templates")  

3.	Select the required portal template.

4.	In the create portal window, enter a name for the portal and address for the website, and select a language from the drop-down list. When you're done, select **Create**. The creation process is same as described in the [Create a Common Data Service starter portal](create-portal.md) section.

> [!NOTE]
> - If you have purchased an older portal add-on, and want to provision a portal using the add-on, you must go to the **Dynamics 365 Administration Center** page. More information: [Provision a portal using the older portal add-on](provision-portal-add-on.md)
> - If you have provisioned a portal using the older portal add-on, you can still customize and manage it from [make.powerapps.com](https://make.powerapps.com).
> - Provisioning portals from [make.powerapps.com](https://make.powerapps.com) does not consume the older portal add-ons. Also, these portals are not listed under the **Applications** tab on the **Dynamics 365 Administration Center** page.
> - A Common Data Service starter portal cannot be created from the **Dynamics 365 Administration Center** page.
> - To disable portal creation in a tenant, see [Disable portal creation in a tenant](create-portal.md#disable-portal-creation-in-a-tenant).

