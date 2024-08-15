---
title: Understand Power Apps Studio
description:  Learn the components inside Power Apps Studio.
author: lancedMicrosoft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 07/7/2022
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  
---

# Understand Power Apps Studio

You can use Power Apps Studio to design, build, and manage your canvas app.

## Overview of Power Apps Studio

:::image type="content" source="media/studio/pa-studio.png" alt-text="Screenshot showing the Power Apps Studio user interface." lightbox="media/studio/pa-studio.png":::

1. [Power Apps Studio modern command bar](#1--power-apps-studio-modern-command-bar): Dynamic command bar that shows a different set of commands based on the control selected.

1. [App actions](#2--app-actions): Options to rename, share, run the app checker, add comments, preview, save, or publish the app.

1. [Properties list](#3--properties-list): List of properties for the selected object.

1. [Formula bar](#4--formula-bar): Compose or edit a formula for the selected property with one or more functions.

1. [App authoring menu](#5--app-authoring-menu): Selection pane to switch between data sources and insert options.

1. [App authoring options](#6--app-authoring-options): Details pane with options relevant to the selected menu item for authoring the app.

1. [Canvas/screen](#7--canvasscreen): Primary canvas for composing the app structure.

1. [Properties pane](#8--properties-pane) - properties list for the selected object in UI format.

1. [Settings and virtual agent](#9--virtual-agent): Go to the settings or get help building your app from a virtual agent.

1. [Screen selector](#10--screen-selector): Switch between different screens in an app.

1. [Change canvas screen size](#11--change-canvas-screen-size): Change the size of the canvas during an authoring experience in Power Apps Studio.

Let's understand each option in Power Apps Studio in detail.

## 1 – Power Apps Studio modern command bar

Power Apps Studio options are available on the command bar. The options are relevant to the current session and app-related settings.

:::image type="content" source="media/studio/pa-studio-options.png" alt-text="Screenshot that shows the command bar menu with lots of development options." lightbox="media/studio/pa-studio-options.png":::

### Modern command bar

The modern command bar displays the relevant set of commands depending on the control that is selected.

:::image type="content" source="media/studio/pa-studio-command-bar.gif" alt-text="Moving image that shows how the command bar changes depending on which control is selected." lightbox="media/studio/pa-studio-command-bar.gif":::

The command bar changes when one of the following controls or objects is selected:

1. App object
2. Screen
3. Button
4. Shape
5. Icon
6. Blank form
7. Form with data
8. Blank gallery
9. Gallery with data
10. Label
11. Text input
12. Date picker

When more than one type of control is selected, the command bar shows the common commands between the selected controls.

#### Back

Takes you back to the build hub, closing the current Power Apps Studio session.

#### Undo and redo

:::image type="content" source="media/studio/pa-undo-redo.png" alt-text="Screenshot that shows where the undo and redo controls are located in the command bar.":::

- **Undo**: Undo the last action.
- **Redo**: Repeat the last action.

#### Cut, copy, and paste

:::image type="content" source="media/studio/pa-studio-cut-copy-paste.png" alt-text="Screenshot that shows where the cut, copy, and paste controls are located in the command bar.":::

- **Cut**: Cut the selection, and store it in the clipboard.
- **Copy**: Copy the selection, and store it in the clipboard.
- **Paste**: Paste the last cut or copied selection from the clipboard.

#### Insert

:::image type="content" source="media/studio/pa-insert-controls.png" alt-text="Screenshot that shows where the two insert controls are located. One is in the command bar and the other control (plus sign) is in the navigation menu.":::

The **Insert** menu is available from the command bar and from the app authoring menu.

Insert shows all the popular objects or controls that you can add on the selected screen in your canvas app. You can also expand other choices or use the components option to insert controls from a component library.

To insert controls on the canvas, you can drag the control to the canvas or select the control.

##### Popular controls

| **Name**      | **Description** |
|---------------|-----------------|
|*Text label* | A box that shows data such as text, numbers, dates, or currency.|
|*Edit form*|Display, edit, or create a record in a data source.|
|*Text input*|A box that shows text.|
|*Vertical gallery*|A control that contains other controls and shows a set of data.|
|*Rectangle*|A rectangular shape to configure the canvas appearance.|
|*Date picker*|A control that the user can select to specify a date.|
|*Button*|A control that the user can select to interact with the app.|

For more information about the controls you can insert, including their properties and definitions, go to [Controls and properties in canvas apps](reference-properties.md).

#### Add data

:::image type="content" source="media/studio/pa-studio-add-data.png" alt-text="Screenshot that shows how to add data from the Add data dropdown list.":::

From the **Add data** menu, you can:

- Select any other existing tables from the current environment.
- Search and select a connector, such as **SharePoint** or **SQL Server**.

#### New screen layouts

Select from the list of available screen layouts.

:::image type="content" source="media/studio/pa-add-screen.png" alt-text="Screenshot that shows how to choose a layout from the New screen menu":::

##### Templates

You can use a template for a screen. Select **Templates** and choose **Blank**, **Scrollable**, **List**, **Success**, **Tutorial**, **Email**, **People**, **Meeting**, **Calendar**, **Portrait print**, or **Landscape print**.

:::image type="content" source="media/studio/pa-studio-add-screen-templates.png" alt-text="Screenshot that shows how to choose a template from the New screen menu":::

#### Background color

Select a background color for a screen. You can select from the list of standard colors or select the **Custom** tab and choose your own color.

:::image type="content" source="media/studio/pa-studio-background-color.png" alt-text="Screenshot that shows where to choose a background color from the command bar.":::

#### Background image

Select **Upload** to upload images to set as the background image.

:::image type="content" source="media/studio/pa-studio-background-image.png" alt-text="Screenshot that shows where to choose a background image from the command bar.":::

#### Settings

Configure the app's settings from the **General**, **Display**, **Upcoming features**, or **Support** tab.

:::image type="content" source="media/studio/pa-studio-general-settings.png" alt-text="Screenshot that shows where to choose settings from the command bar."  lightbox="media/studio/pa-studio-general-settings.png":::

##### General

- Edit the app **Name** and **Description**.
- Add or update the **App icon**. Add a custom icon with **+ Add image**.
- Select an **Icon background fill** or **Icon fill** color.
- Toggle **Auto save** to save every two minutes automatically.
- Configure offline use.
- Enable modern controls and themes to update automatically.
- Set your **Data row limit**.
- Include debug information when you publish.
- Enable autocreation of environment variables.
- **Enable App.OnStart property**.

For example, to edit the app **Name**, go to the **General** tab of **Settings**.

:::image type="content" source="media/studio/pa-studio-app-name-editor.png" alt-text="Screenshot where you edit your app name in the Settings popup.":::

##### Display

- Select the **Orientation** and screen **Size**.
- **Scale to fit**: Scales the app to fit available space.
- **Lock aspect ratio**: Locks the height and width ratio.
- **Lock orientation**: Maintains app orientation when device rotates.
- **Show mobile device notifications area**: Displays notifications at the top of the screen.

For more information, see [Change screen size and orientation](set-aspect-ratio-portrait-landscape.md).

##### Upcoming features

Allows you to configure advanced settings for the app that include features under preview, experimental or retired features.

For more information, see [Understand experimental, preview, and retired features in Power Apps](working-with-experimental-preview.md).

##### Support

Access current Power Apps Studio information such as environment, authoring version, session ID, and session details. This information is useful for Microsoft Support sessions.

#### Power Automate

Create a new flow with Power Automate, or select any available flow.

:::image type="content" source="media/studio/pa-studio-create-flow.png" alt-text="Screenshot that shows where the Power Automate section is located.":::

For more information, see [Use Power Automate pane](working-with-flows.md).

#### Collections

A collection is a group of items that are similar, such as products in a product list. This section lists the collections used by the current app. For more information, see [Collections in canvas apps](create-update-collection.md).

#### Variables

You can save data such as the result values from a data set into temporary storage by using variables. This section lists variables used by the current app. For more information, see [Variables in canvas apps](working-with-variables.md).

:::image type="content" source="media/studio/pa-studio-collections.png" alt-text="Screenshot that shows the collections in the app that are found in the Variables section.":::

## 2 – App actions

To work with app-specific actions, use the options such as **Share**, **App checker**, **Comments**, **Preview the app**, **Save**, and **Publish**.

:::image type="content" source="media/studio/pa-studio-actions-menu.png" alt-text="Screenshot that shows the app actions in the command bar.":::

### Share

When you select the **Share** app action, you see a new tab or window open where you can share the app. You can share with other users or add them as co-owners of your app.

:::image type="content" source="media/studio/pa-studio-share-app.png" alt-text="Screenshot that shows the Share app action selected, opening in a new window or tab, where you can share the app with users and co-owners." lightbox="media/studio/pa-studio-share-app.png":::

> [!TIP]
> You must save the app before you can share it.

### App checker

Select **App checker** to run a check.

For more information, see [PowerApps checker now includes App checker results for Canvas apps in solutions](https://powerapps.microsoft.com/blog/powerapps-checker-now-includes-app-checker-results-for-canvas-apps-in-solutions/).
:::image type="content" source="media/studio/pa-studio-app-checker.png" alt-text="Screenshot that shows where the App checker app action is located and its menu contents.":::

### Comments

Comments are notes associated with items in your app. Use comments to help your team review the app and provide feedback, or provide additional information on implementation details in your app.

:::image type="content" source="media/studio/pa-studio-comments.png" alt-text="Screenshot that shows where the Comments app action is located and its menu where you can add a new comment.":::

### Preview

Select **Preview the app** to go into preview mode. Here you can view and interact with the current version of the app.

:::image type="content" source="media/studio/pa-studio-preview.png" alt-text="Screenshot that shows where the Preview app action is located.":::

### Save

You can save your app in different ways, such as **Save**, **Save with version notes**, **Save as**, or **Download a copy**. The save options dropdown is located next to the **Save** app action.

:::image type="content" source="media/studio/pa-studio-save-options.png" alt-text="Screenshot that shows where save options are located.":::

Save options include:

- **Save**: Saves recent and unsaved changes you made to the app. Each time you save changes, a new version is created.
- **Save with version notes**: Save and add notes about your updates.
- **Save as**: Duplicate the app by saving it with a different name.
- **Download a copy**: Download a local copy of the app.

### Publish

Select **Publish** to publish the app’s current version. For more information, see [Save and publish canvas apps](save-publish-app.md).

:::image type="content" source="media/studio/pa-studio-publish.png" alt-text="Screenshot that shows where the Publish app action is located and its popup where you can add details to the publishing of your app." lightbox="media/studio/pa-studio-publish.png":::

## 3 – Properties list

When you select an object in your canvas, you can choose one of the object's properties from its properties list. For a complete list of all possible properties, see [All properties](reference-properties.md#all-properties).

:::image type="content" source="media/studio/pa-studio-prop-list.png" alt-text="Screenshot that shows the properties list of an object you select in your app canvas.":::

## 4 – Formula bar

The formula bar lets you add, edit, or remove functions of a property from your selected object. For example, select the app screen to update the background color by using the [RGBA function](/power-platform/power-fx/reference/function-colors).

:::image type="content" source="media/studio/pa-studio-formula-bar.png" alt-text="Screenshot that shows the formula bar." lightbox="media/studio/pa-studio-formula-bar.png":::

The formula bar is IntelliSense-enabled. When you start entering text that matches one or more functions, the formula bar shows a list of functions.

:::image type="content" source="media/studio/pa-studio-formula-bar-1.png" alt-text="Screenshot that shows the formula bar with IntelliSense in action as you type." lightbox="media/studio/pa-studio-formula-bar-1.png":::

When you select a function, the formula bar shows inline function help and highlights help text relevant to the cursor position.

:::image type="content" source="media/studio/pa-studio-formula-bar-2.png" alt-text="Screenshot that shows inline help for a function in the formula bar." lightbox="media/studio/pa-studio-formula-bar-2.png":::

If a formula returns an error, you can view the error details in **App checker**.

:::image type="content" source="media/studio/pa-studio-formula-bar-3.png" alt-text="Screenshot that shows formula errors viewed, using the App checker." lightbox="media/studio/pa-studio-formula-bar-3.png":::

Similarly, you find help when working with complex functions, nested functions, or when correcting a formula syntax.

For a complete list of all canvas app functions, see [Formula reference - Power Apps](/power-platform/power-fx/formula-reference).

## 5 – App authoring menu

Switch between various authoring options while working with the app.

:::image type="content" source="media/studio/pa-studio-app-authoring-menu.png" alt-text="Screenshot that shows the app authoring menu.":::

> [!TIP]
> You can select the tree view icon to collapse or expand the list to either include icons only or full names with icons.
> :::image type="content" source="media/studio/pa-studio-collapse-tree.png" alt-text="Screenshot that showswhere to select the tree view icon in order to collapse the menu.":::

- **Tree view**: Shows a tree view of all screens and controls in the current app.
- **Insert**: Allows you to add different controls to the screen.
- **Data**: Add or remove data such as tables that the app connects to.
- **Media**: Insert or remove media from the app.
- **Power Automate**: Add a flow using the [Power Automate pane](working-with-flows.md).
- **Variables**(preview): Work with [variables](working-with-variables.md) and [collections](create-update-collection.md) while editing your app.
- **Advanced tools**: Allows you to access the [Monitor](../monitor-canvasapps.md) and [Test](test-studio.md) tools to debug and test your app.
- **Search**: Select to search for media, formulas, text, and more in your app. You can also do a search and replace.

## 6 – App authoring options

The options for working with canvas apps change depending on the selection on the authoring menu.

### Tree view

Select the tree view to show the screens available in the app.

:::image type="content" source="media/studio/pa-studio-tree-view.png" alt-text="Screenshot that shows the Tree view pane when you select Tree view from the authoring menu.":::

> [!TIP]
> Select **App** in the tree view to work with app-specific controls. You can change app behavior, such as adding a formula for the *OnStart* event of the app.

Switch to the **Components** tab of **Tree view** to work with component library features. You can add new components or reuse ones from the published component libraries. For more information, see [Component library](component-library.md).

:::image type="content" source="media/studio/pa-studio-components-tab.png" alt-text="Screeshot showing the Components tab of the Tree view pane.":::

For more information on adding components, see the [Insert](#insert) section.

### Data

Add, refresh, or remove data sources from your canvas app. You can add one or more [connections](connections-list.md) by using data sources.  

In addition to data stored within tables, there are many connectors available to interact with data in popular software as a service (SaaS), services, and systems.

:::image type="content" source="media/studio/pa-studio-data.png" alt-text="Screenshot that shows where the Data section is located from the authoring menu. You can add data here.":::

To choose other connectors such as SharePoint, OneDrive, or SQL Server, you can enter text in the data source search box or select from the list of connectors.

:::image type="content" source="media/studio/pa-studio-data-source.png" alt-text="Screenshot that shows how to select a data source by choosing the Add data dropdown.":::

For more information, see [List of all Power Apps connectors](/connectors/connector-reference/connector-reference-powerapps-connectors).

### Media

Select **Media** to add images, video, or audio files to your app. Adding media directly to your app uploads the files to the app and uses the app storage.

:::image type="content" source="media/studio/pa-studio-add-media.png" alt-text="Screenshot that shows how to select the Media option from the authoring menu.":::

> [!TIP]
>
> - Each file uploaded to the app as media must be 64 MB or smaller.
> - The size of all media files uploaded to an app can't exceed 200 MB.

If you want to reference more media, consider using [audio and video controls with URLs](add-images-pictures-audio-video.md#add-images-audio-or-video-using-the-controls), media from [Azure Media Services](add-images-pictures-audio-video.md#add-media-from-azure-media-services), or from [Microsoft Stream](./controls/control-stream-video.md#example).

For more information, see [Using multimedia files in Power Apps](add-images-pictures-audio-video.md).

## 7 – Canvas/screen

The canvas shows the currently selected screen from the authoring menu.

Use inline actions when you're editing a canvas app. For more information, see [Use inline actions in Power Apps Studio](inline-actions.md).

## 8 – Properties pane

The properties pane shows properties and options available for the currently selected object on the canvas.

- The **Properties** tab shows generic options such as the name, color, size, or position.
- The **Advanced** tab shows options for advanced customization. The advanced properties might sometimes be locked for editing, such as when working with data cards. You can select [Unlock to change properties](working-with-cards.md#unlock-a-card) in such situations.

:::image type="content" source="media/studio/pa-studio-prop-pane.png" alt-text="Screenshot that shows the properties pane that appears when you select an object in your canvas. Advanced properties is a tab in that same pane.":::

## 9 – Virtual agent

Real-time, in-product help is available from the documentation using the Power Platform virtual agent. The virtual agent can help answer questions about common scenarios.

For more information, see [Get help building your app from a virtual agent](../common/virtual-agent.md).

## 10 – Screen selector

Use the screen selector to switch between screens when your canvas app has multiple screens. You can also select a screen from the authoring menu by selecting the tree view. If the current selection is inside a container, or inside an individual cell in a gallery, the selector shows the breadcrumbs for the parent elements at each level.

:::image type="content" source="media/studio/pa-studio-screen-selector.png" alt-text="Screenshot that shows the location of the screen selector.":::

## 11 – Change canvas screen size

You can zoom in or out while authoring the canvas app. Select **Ctrl**+**0** **Fit to window** to fit the screen size based on the current authoring window size.

> [!NOTE]
> The zoom percentage or screen size used in authoring a canvas app has no effect on the aspect ratio configured for the app. When you preview your app or play a published app, your screen size is temporary.
