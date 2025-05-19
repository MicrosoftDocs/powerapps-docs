---
title: App navigation in model-driven apps
description: Learn about app navigation in model-driven apps in Power Apps.
author: Mattp123
editor: ''
tags: ''
ms.topic: article
ms.component: model
ms.date: 01/27/2025
ms.author: matp
ms.subservice: mda-maker
search.audienceType: 
  - maker
---

# App navigation in model-driven apps

In a model-driven app, there are the three main app runtime navigation components.

1. *Areas* - For apps with more than one area, a switch control is displayed in the lower left navigation pane. In the screenshot below, the current area is named *Accounts*.
1. *Groups* - Group names appear as a navigation element in an app with the subarea names within the group listed beneath it. In the screenshot below, one group is named *Accounts* and one is named *New Group*.
1. *Pages* - Pages appear under the group that they're configured within in the app designer. In the screenshot below, one page is named *All accounts revenue* and another page is named *Contacts*.

   :::image type="content" source="media/default-sitemap.png" alt-text="Default model-driven app site map":::

## Create an area

By default, the ability to create additional areas is disabled. Areas are enabled by default for apps with existing multiple areas.

### Enable areas

1. On the command bar select **Settings**.
1. Select **Navigation** on the left pane, and then select **Enable Areas**.
1. Close the **Settings** dialog.

### Add a new area

1. On the left navigation pane, select **Pages**.
1. Select the area switcher under **Pages**, and then select **New area**. If the area switcher is missing, you need to [enable areas](#enable-areas).
   :::image type="content" source="media/app-designer-create-area.png" alt-text="Create an area for you app.":::
1. Complete the properties pane for the area:

   - **Title**: Enter a title used to describe the area.
   - **Icon**: Optionally set an icon for the area. More information: [Create or edit model-driven app web resources to extend an app](create-edit-web-resources.md)
   - **ID**: The system generates an identifier for the area. Accept the system generated ID or enter a new one.

1. To save your app navigation changes select **Save**.
1. To publish the changes and make them available to other users, select **Publish**.

## Create a group

To create a new group, complete the following steps:

1. On the left navigation pane, select **Pages**.
1. Select **...** next to **Navigation**.
1. Select **New group**.
   :::image type="content" source="media/add-navigation.png" alt-text="Add a group or page":::
1. Complete the properties pane for the group:

   - **Title**: Enter a title used to describe the group.
   - **ID**: The system generates an identifier for the group. Accept the system generated ID or enter a new one.
   - **Advanced Settings**:
     - **Localized titles**: Add localized titles for the group title. More information: [Translate localizable text for model-driven apps](translate-localizable-text.md)
     - **Localized descriptions**: Add localized descriptions for the group description. More information: [Translate localizable text for model-driven apps](translate-localizable-text.md)

1. To save your app navigation changes select **Save**.
1. To publish the changes and make them available to other users, select **Publish**.

## Create a page

Pages were formerly called *subareas* in the app designer. To create a new page, complete the following steps:

1. On the command bar, select **Add page**.
1. Select the content type you want.
   - **Dataverse table**. Select an existing table or create a new one. More information: [Create a custom table](../data-platform/data-platform-create-entity.md)
   - **Dashboard**. Select a dashboard. More information: [Create or edit model-driven app dashboards](create-edit-dashboards.md)
   - **Custom page**. Add a custom page, such as a canvas app page. More information: [Overview of custom pages for model-driven apps]
   - **Web resource**. Web resources represent files that can be used to extend an application such as HTML files, JavaScript, and CSS, and several image formats.
   - **Navigation link**. Add a URL, such as a website address. More information: [Add a URL to an app](#add-a-url-to-an-app)
 (model-app-page-overview.md)
1. Complete the choices that are on you screen to create the page, and then select **Add**.
1. To save your app navigation changes select **Save**.
1. To publish the changes and make them available to other users, select **Publish**.

### Add a URL to an app

A URL is a type of page in the app navigation. When the user selects the page, the URL opens in a new tab in the web browser.

:::image type="content" source="media/url-in-app.png" alt-text="URL component in a model-driven app":::

1. In the model-driven app designer, select **Add page** on the command bar.
1. On the **New page** screen, select **URL**, and then select **Next**.
1. In the properties pane for the URL, enter the following information, and then select **Add**:
   - **URL**: Enter the full URL, such as *https://www.microsoft.com*.
   - **Title**: Enter a title for the URL component.

     :::image type="content" source="media/create-url-page.png" alt-text="Add a URL subarea":::

1. To save your app navigation changes select **Save**.
1. To publish the changes and make them available to other users, select **Publish**.

## Remove a group or page

1. On the left navigation pane, select **Pages**.
1. Select the group or page you want, select the ellipses (**...**) and then select **Remove from navigation**.

## Remove an area

1. On the left navigation pane, select **Pages**.
1. Select the area switcher under **Pages**, select **...** next to the area you want to remove, and then select **Remove from navigation**.

### See also

[Overview of the model-driven app designer (preview)](app-designer-overview.md)
