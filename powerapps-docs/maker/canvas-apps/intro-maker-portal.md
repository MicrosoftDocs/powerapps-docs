---
title: "Navigate the Power Apps home page| MicrosoftDocs"
description: How to navigate the Power Apps home page. 
ms.custom: ""
ms.date: 11/28/2022
ms.reviewer: "mkaur"
ms.topic: overview
author: "mkaur"
ms.subservice: common
ms.author: "mkaur"
manager: "tapanm"
search.audienceType: 
  - maker, admin
search.app: 
  - PowerApps
---


# Navigate the Power Apps home page 

The [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) home page offers you various options for creating your own apps, opening apps that you or others have created, and performing related tasks. These tasks range from the most simple, such as identifying the license or licenses that give you access, to more advanced capabilities like creating custom connections to specific data sources.

You can select options in three general areas:

- The left navigation pane 

    ![Navigation bar.](media/intro-maker-portal/left-nav-0.png)
    
- The header along the top of the page

    ![Header for environment selection.](media/intro-maker-portal/header.png)

- The large icons that feature prominently in the middle of the page

    :::image type="content" source="media/intro-maker-portal/center-area.png" alt-text="Center area of the home page.":::

For best results, start by ensuring that the home page is set to the right environment.



## Left navigation pane (preview)

Find what you need with the new left navigation experience. If this is the first time you're signing in to the [Power Apps home page](https://make.powerapps.com) the default left navigation pane will show the menu items:

- **Home**: Takes you to the Power Apps home page.
- **Create**: This is where you create apps.
- **Learn**: The [learn hub](../common/learn-hub.md) lets you explore documents, training material, get help from the Power Apps community, and other resources that will help you to create and build Power Apps.
- **Apps**: If you've created an app (or someone else has created one and shared it with you), you can play or edit it.
- **More**: Pin your most-used items to the left navigation such as tables, flows, and more.
- **Power Platform**: Takes you to Power Platform admin centers.

> [!div class="mx-imgBorder"]
> ![Power Apps left navigation pane.](media/intro-maker-portal/default-nav-1.png "Power Apps left navigation pane")


### Pin and unpin

You can pin your most used pages in the navigation pane so you quickly access features that you use frequently. Links to other pages are available through the **More** link. When you pin an item it appear in the middle section, aboce the **More** menu. 

When you sign in for the first with the new navigation, the system will automatically pin your most and recently used pages on the left navigation pane. However, you can customize the middle section of the left navigation pane to your preference. 

> [!div class="mx-imgBorder"]
> ![First time sign in dialog box.](media/intro-maker-portal/left-nav-dialog-2.png "First time signing in")

To pin a page to the left navigation pane, select **More** and then choose the page that you want to pin.

> [!div class="mx-imgBorder"]
> ![Pin an item.](media/intro-maker-portal/pin-3.png "Pin an item")

To unpin a page, from the left navigation menu select the more button next to the page that you want to unpin and then select **Unpin**.

### Move up or move down

Once you pinned a few items you can also move them up or down them up or down the list.

To move an item up or down, select the more button next to the page that you want to move, and then select **Move up** or **Move down**.

> [!div class="mx-imgBorder"] 
> ![Move up or down.](media/intro-maker-portal/move-up-down-4.png "Move up or down")


## Choose an environment

Whether you're creating an app, a flow, a data connection, or a table in Microsoft Dataverse, much of what you do in Power Apps is contained in a specific environment. Environments create boundaries between different types of work. For example, an organization might have separate environments for different departments. Many organizations use environments to separate apps that are still being developed from those that are ready for widespread use. You might have access to multiple environments or only one. If you have the appropriate permissions, you might even be able to create your own environments.

To verify which environment you're in, find the environment switcher near the right side of the header.

![Environment switcher.](media/intro-maker-portal/environment-switcher.png)

With the environment selector, environments are grouped into two categories:  **Build apps with Dataverse** and **Other environments**. Select **Filter** to filter the list of environments by your role, data platform (Dataverse or none), and environment type, such as production or sandbox.

:::image type="content" source="media/intro-maker-portal/environment-picker2.png" alt-text="Environment selector to filter and select an environment" lightbox="media/intro-maker-portal/environment-picker2.png":::

Environments where you have either system administrator and/or system customizer security role membership appear under **Build apps with Dataverse**. The **Other environments** list displays environments where you have only environment maker or editing privileges to at least one of the canvas apps in the environment.

> [!TIP]
> Hover over an environment in the list to view the details of the environment.

#### Filter environments by role

|Filter role  |Power Platform role or description  |
|---------|---------|
|Admin     | System administrator <br /> Environment admin        |
|Maker with data access     | System administrator <br />  System customizer        |
|Maker without full data access     | Environment maker (with or without Dataverse)     |
|Shared app contributor     | User without a maker-level security role assigned but with edit permission to at least one canvas app in the environment        |

> [!IMPORTANT]
> - To view the environment list in the environment switcher in Power Apps, you must have the Environment Maker, System Customizer, or System Administrator security role in the environment. For information about predefined security roles, see [Predefined security roles](/power-platform/admin/database-security#predefined-security-roles) in the Microsoft Power Platform admin guide.
> - Make sure that you're in the right environment *before* you create an app, a flow, or a similar component. You can't easily move components from one environment to another.

> [!NOTE]
> - Every member in an organization can access [the default environment](/power-platform/admin/environments-overview#the-default-environment). Like any environment, users can see apps where they have sufficient privileges to access an app.
> - All users with the Environment Maker security role in an environment can see all model-driven apps in that environment, including the default environment. More information: [Model-driven app privileges to view and access apps](../model-driven-apps/app-visibility-privileges.md).
> - When you create an app in one environment, you won't be able to see it from another environment. In addition, people who want to run your app must have access to the environment in which you created it.

For more information, see [Environments overview](/power-platform/admin/environments-overview).
