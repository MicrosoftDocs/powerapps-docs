---
title: "Overview of the model-driven app designer | MicrosoftDocs"
description: Learn about the app designer for model-driven apps.
ms.custom: ""
ms.date: 09/12/2022
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
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Overview of the model-driven app designer

The new model-driven app designer provides a modern WYSIWYG authoring experience when you work with model-driven apps.

Changes to the app are instantly reflected in the preview, enabling you to see exactly how the app will appear to users when published.

   :::image type="content" source="media/app-designer-layout.png" alt-text="Layout of the model-driven app designer that has the account and contact tables added":::

The app designer interface has the following areas:

1. Command bar – Displays the available actions:

   - **Back**. Closes the model-driven app designer and returns you to the Power Apps website (make.powerapps.com).
   - **New page**. Creates a new page for one or more table forms and views or table dashboards for the app.
   - **Settings**. Opens the app properties such as name and description. <!-- and whether the app can be used offline-->
   - **Switch to classic**. Opens the app in the classic app designer.
   - **Save**. Saves the app.
   - **Publish**. Makes the changes made available to other users.
   - **Play**. Opens the app in a new tab in run mode.

2. App preview – Displays a real-time preview of the form as it will appear to users when published.

3. Panes - The left navigation pane consists of the following areas:

   - **Pages**. Displays the components in your app. From the page area you can choose to add or remove forms, views, and dashboards for each table.
   - **Navigation**. Displays a navigation structure  of your app that is formed using areas, groups, and subareas. You can add or remove groups and subareas to the navigation.
   - **Data**. Provides a view of all available tables that are currently used within your app and a view of all tables that are available in your environment.
   - **Automation**. Displays business process flows that are a part of this app. You can add, remove, or create new business process flows to the app.

4. Property pane – Displays properties of the selected component and also allows you to make changes.

5. Preview size switcher - Changes the size of the form preview helping you to see how the form will appear on various screen sizes.

6. Zoom slider - Zooms in or out of the app preview helping you take a closer look.

7. Fit to screen - Quick action to fit the app preview to the available screen size.

   :::image type="content" source="media/app-designer-layout.png" alt-text="Layout of the model-driven app designer that has the account and contact tables added.":::

## Navigation pane options

From the **Navigation** pane, select **Navigation bar** to set the following options.
1. **Show Home**. Enabled by default. When selected, displays the **Home** page link for the app.
1. **Show Recent**. Enabled by default. When selected, displays the recently viewed pages link. Selecting the link displays all recently viewed pages.
1. **Show Pinned**. Enabled by default. When selected, displays the pages that have been pinned. App users select the push-pin icon next to a record listed under **Recent** to add it to their pinned rows.
1. **Enable collapsible groups**. Disabled by default. When selected, subareas displayed under groups in the site map can be expanded or collapsed.
1. **Enable Areas**. Disabled by default. When selected, new areas can be added to the app. For apps with existing multiple areas, this setting is enabled by default. You can't disable this setting while the app has multiple areas.
1. **Enable web resources**. Disabled by default. When selected, web resources can be added to the app as a type of subarea. More information: [Add a web resource to an app (preview)](create-edit-web-resources.md#add-a-web-resource-to-an-app-preview).
1. **Enable URLs**. Disabled by default. When selected, URLs can be added to the app as a type of subarea. More information: [Add a URL to an app](app-navigation.md#add-a-url-to-an-app)

   :::image type="content" source="media/navigation-pane-options.png" alt-text="Options available for app navigation":::

## Discover who's working on an app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Find who's working on an app at the same time as you with copresence. Copresence provides the following benefits:

- Icons and names of people who have the app open and might be making changes are displayed.
- Contact those people working on the app via email or Teams.
- On the left navigation pane the structure of the app is displayed letting you know what part of the app is being worked on.
- Receive notification for saved changes made from other makers. Then, you'll be prompted to refresh the app to stay on the latest version so as not to lose your work or overwrite other's work later. More information: [Notifications](#notifications)
- The name of the maker who made the first save or the last save is displayed.

> [!IMPORTANT]
> - This is a public preview feature. More information: Public previews for [Portals, model-driven apps and app management](../powerapps-preview-program.md#portals-model-driven-apps-and-app-management)
> - This feature is being rolled out, and&mdash;depending on your region&mdash;it might not be available for your tenant yet.

### How copresence works

The first time someone joins your app in app designer while you working on it a notice appears that indicates other people are also working on the app. Advise is given to check with the other makers about the order you plan to make changes. Notice that it's possible that the other makers in the app might not want to save their changes.

Icons of copresent makers appear in both the toolbar area and the left navigation pane showing where other makers are working in the app.

When you have several tabs open, your icon is displayed in the left navigation pane as well. This way you’ll always see if you've more than one tab open, which helps you find the one you want to continue working on.

On the right side of the app designer toolbar, all the makers that have this app open are displayed. If  more than four makers are present, a +n, such as +1 or +30, is displayed that expands with all the makers’ names. Select a name to display **Send email** and **Chat in Teams** links to contact that person.

### Notifications

You may be working on the app, or you may be idle, but once someone else saves a change to the app, you’ll receive a notification in the upper bar indicating that another maker made changes. When this occurs, you're advised to refresh to be at the latest version so as not to lose changes you make afterwards.

> [!TIP]
> - If you weren’t expecting anyone to make changes to the app, and spent a long time adding changes, we recommend you contact the person immediately. For example, it might happen that another maker saved something minor and you can agree that your changes may overwrite their changes. In this case, do not select refresh, instead select save to present the option to overwrite changes.
> - We recommend that you to always stay at the latest version of the app and refresh when others save changes. If you were idle and didn't make changes and see this notification, select refresh.
>

If you've ignored or closed the refresh notification, you won’t be at the latest version of the app. At the time when you select save, you're prompted with a choice: refresh (and lose your changes) or overwrite (and lose other maker's changes).

> [!TIP]
> We recommend you chat with the team or the person who made the last change. Copresence provides the name of the maker to alert you before you overwrite their changes.

### Known copresence limitations and issues

- There may be a delay up to 20 seconds between when new members join the app and when you see their presence and location.
- There may also be a delay up to one minute between when someone saves a change and when you get a notification about the change. However, if there is a conflict, you will always get the prompt to choose whether to refresh or overwrite when you try to save.
- Making a comment on a new page or area triggers a background save and if your app is not on the latest version you'll be prompted to either refresh or overwrite.

## Known limitation

- The app’s URL can’t be specified.


## Next steps

[Create a model-driven app using the app designer](create-model-driven-app.md)

[Working with custom pages](model-app-page-overview.md)

[Understanding app navigation](app-navigation.md)
