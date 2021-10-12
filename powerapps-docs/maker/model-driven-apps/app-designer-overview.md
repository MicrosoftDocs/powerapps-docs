---
title: "Overview of the model-driven app designer | MicrosoftDocs"
description: Learn about the app designer for model-driven apps.
ms.custom: ""
ms.date: 06/17/2021
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

The new model-driven app designer provides a modern WYSIWYG authoring experience when you work with model-driven apps.

Changes to the app are instantly reflected in the preview, enabling you to see exactly how the app will appear to users when published.

   :::image type="content" source="media/app-designer-layout.png" alt-text="Layout of the model-driven app designer that has the account and contact tables added":::

The app designer interface has the following areas:

1. Command bar – Displays the available actions:

   - **Back**. Leaves the model-driven app designer.
   - **New page**. Creates a new page for one or more table forms and views or table dashboards for the app.
   - **Settings**. Opens the app properties such as name and description. <!-- and whether the app can be used offline-->
   - **Switch to classic**. Opens the app in the classic app designer.
   - **Save**. Saves the app.
   - **Publish**. Makes the changes made available to other users.
   - **Play**. Opens the app in a new tab in run mode.

2. App preview – Displays a real-time preview of the form as it will appear to users when published.

3. Panes - The left navigation pane consists of the following areas:

   - **Pages**. Displays the components in your app. From the page area you can choose to add or remove forms, views and dashboards for each table.
   - **Navigation**. Displays a navigation structure  of your app that is formed using areas, groups, and subareas. You can add or remove groups and subareas to the navigation.
   - **Data**. Provides a view of all available tables that are currently used within your app and a view of all tables that are available in your environment.

4. Property pane – Displays properties of the selected component and also allows you to make changes.

5. Preview size switcher - Changes the size of the form preview helping you to see how the form will appear on various screen sizes.

6. Zoom slider - Zooms in or out of the app preview helping you take a closer look.

7. Fit to screen - Quick action to fit the app preview to the available screen size.

   :::image type="content" source="media/app-designer-layout.png" alt-text="Layout of the model-driven app designer that has the account and contact tables added.":::
 
## Known limitations

- You can’t add the following model-driven app components:
   - URLs
   - Business process flows
   - Charts
- You can’t add more than one area to the app’s navigation.
- You can’t change the app’s icon.
- You can’t specify the app’s URL.

> [!TIP]
> Select **Switch to classic** to use the classic designer to complete the app design tasks that aren't currently available in the designer.

## Next steps

[Create a model-driven app using the app designer](create-model-driven-app.md)
