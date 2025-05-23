---
title: "Overview of the model-driven app designer"
description: Learn about the app designer for model-driven apps in Power Apps.
ms.custom: ""
ms.date: 01/27/2025
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: overview
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "emcoope"
ms.reviewer: "matp"
search.audienceType: 
  - maker
---
# Overview of the model-driven app designer

The model-driven app designer provides a modern WYSIWYG authoring experience when you work with model-driven apps.

Changes to the app are instantly reflected in the preview, enabling you to see exactly how the app will appear to users when published.

The app designer interface has the following areas:

1. Command bar – Displays the available actions:

   - **Back**. Closes the model-driven app designer and returns you to the Power Apps website (make.powerapps.com).
   - **Add page**. Creates a new page, which can include table forms and views, table dashboards, or a custom page for the app.
   - **Settings**. Opens the app properties such as name and description.
   - **Edit form**: Open the form designer to edit the default form shown in app preview.
   - **Comments**. Add a comment to the app. More information: [Add comments in the model-driven app designer](comments.md)
   - **Save**. Saves the app.
   - **Publish**. Makes the changes made available to other users.
   - **Play**. Opens the app in a new tab in run mode.

2. App preview – Displays a real-time preview of the form as it will appear to users when published.

3. Panes - The left navigation pane consists of the following areas:

   - **Pages**. The **Navigation** section displays a layout of your app that is formed using areas, groups, and subareas. You can add or remove groups and subareas to the navigation. The **All other pages** portion displays the components in your app. From this section, you can choose to add or remove forms, views, and dashboards for each table.
   - **Data**. Provides a view of all available tables that are currently used within your app and a view of all tables that are available in your environment.
   - **Automation**. Displays business process flows that are a part of this app. You can add, remove, or create new business process flows to the app.

4. Property pane – Displays properties of the selected component and associated forms and views with the selected table. Selecting the pencil or ellipsis opens the form or view designer.

5. Preview size switcher - Changes the size of the form preview helping you to see how the form will appear on various screen sizes.

6. Zoom slider - Zooms in or out of the app preview helping you take a closer look.

7. Fit to screen - Quick action to fit the app preview to the available screen size.

   :::image type="content" source="media/app-designer-layout.png" alt-text="Layout of the model-driven app designer that has the account and contact tables added."lightbox="media/app-designer-layout.png":::

## Navigation pane options

To edit the app's navigation, select **...** next to **Navigation**, and then select **Settings**.
:::image type="content" source="media/app-designer-page-navigation.png" alt-text="Page navigation options in app designer.":::
The following options are available:

1. **Show Home**. Enabled by default. When selected, displays the **Home** page link for the app.
1. **Show Recent**. Enabled by default. When selected, displays the recently viewed pages link. Selecting the link displays all recently viewed pages.
1. **Show Pinned**. Enabled by default. When selected, displays the pages that have been pinned. App users select the push-pin icon next to a record listed under **Recent** to add it to their pinned rows.
1. **Enable collapsible groups**. Disabled by default. When selected, subareas displayed under groups in the site map can be expanded or collapsed.
1. **Enable Areas**. Disabled by default. When selected, new areas can be added to the app. For apps with existing multiple areas, this setting is enabled by default. You can't disable this setting while the app has multiple areas.

   :::image type="content" source="media/navigation-pane-options.png" alt-text="Options available for app navigation":::

## Known limitation

- The app’s URL can’t be specified.

## Next steps

[Create a model-driven app using the app designer](create-model-driven-app.md)

[Working with custom pages](model-app-page-overview.md)

[Understanding app navigation](app-navigation.md)
