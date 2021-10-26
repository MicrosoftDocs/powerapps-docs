---
title: "Overview of the model-driven app designer | MicrosoftDocs"
description: Learn about the app designer for model-driven apps.
ms.custom: ""
ms.date: 10/26/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "emcoope"
ms.reviewer: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Overview of the model-driven app designer

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The new model-driven app designer provides a modern WYSIWYG authoring experience when you work with model-driven apps. The designer includes several improvements not available in the classic model-driven app designer.

The designer shows a real-time WYSIWYG preview while you author an app. Changes to the app are instantly reflected in the preview, enabling you to see exactly how the app will appear to users when published.

The app designer interface has the following areas:

1. Command bar – Displays available actions:

   - **New page**. Create a new page for one or more table forms and views or table dashboards for the app.
   - **Settings**. Opens the app properties such as name and description. <!-- and whether the app can be used offline-->
   - **Switch to classic**. Opens the app in the classic app designer.
   - **Save**. Saves the app.
   - **Publish**. Makes the app available to users in the environment.
   - **Play**. Opens a new tab to view the app at run time in a full browser window.

2. App preview – Displays a real-time preview of the form as it will appear to users when published.

3. Panes - The left navigation pane consists of the following areas: 

   - **Pages**. Displays the components for you app. From the page area you can choose the forms, views, and dashboards you want to add or remove for each table.
   - **Navigation**. Displays a site map view of your app that is formed using areas, groups, and subareas. Add or remove groups and subareas to structure your app's navigation. Select display options for home, recent, and pinned. More information: [Navigation pane options](#navigation-pane-options)
   - **Data**. Provides a view of all available data that’s currently included in your app or is available to add from your Dataverse environment.

4. Property pane – Displays properties of the selected component, and also allows you to make changes.

5. Preview size switcher - Changes the size of the form preview helping you to see how the form will appear on various screen sizes.

6. Zoom slider - Zooms in or out of the app preview helping you take a closer look.

7. Fit to width - Quick action to fit the app preview to the available width.

   :::image type="content" source="media/app-designer-layout.png" alt-text="Layout of the model-driven app designer that has the account and contact tables added.":::

## Navigation pane options

From the **Navigation** pane, you can set the following navigation bar options.
1. **Show Home**. Enabled by default. When selected, displays the Home page link for the app.
1. **Show Recent**. Enabled by default.When selected, displays the recently viewed pages link. Selecting the link displays all recently viewed pages.
1. **Show Pinned**. Enabled by default. When selected, displays the pages that have been pinned. App users select the push-pin icon next to a record listed under Recent to add it to their pinned rows.
1. **Enable collapsible groups**. Disabled by default. When selected, subareas displayed under groups in the site map can be expanded or collapsed.

   :::image type="content" source="media/navigation-pane-options.png" alt-text="Options available for app navigation":::

## Known limitations

- You can’t add the following model-driven app components: 
   - URLs
   - Business process flows
   - Charts
- You can’t add more than one area to the app’s navigation site map. 
- You can’t change the app’s icon.
- You can’t specify the app’s URL.

> [!TIP]
> Select **Switch to classic** to use the classic designer to complete the app design tasks that aren't currently available in the new designer.

## Next steps

[Create a model-driven app using the app designer](create-model-driven-app.md)
