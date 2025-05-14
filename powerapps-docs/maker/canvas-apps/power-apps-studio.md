---
title: Understand Power Apps Studio
description:  Learn the components inside Power Apps Studio.
author: lancedMicrosoft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 5/14/2025
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

1. [App actions](#2--app-actions): Options to view properties, add comments, run the app checker, share, preview, save, or publish the app.

1. [Properties list](#3--properties-list): List of properties for the selected object, such as *fill* or *height*.

1. [Formula bar](#4--formula-bar): Compose or edit a formula for the selected property with one or more functions.

1. [App authoring menu](#5--app-authoring-menu): Selection pane to switch between data sources and allows you to insert options.

1. [App authoring options](#6--app-authoring-options): This pane reveals the corresonding authoring feature when a feature is selected from the app authoring menu.

1. [Canvas/screen](#7--canvasscreen): Primary canvas for composing the app structure.

1. [Properties pane](#8--properties-pane): Properties list for the selected object in Tree view.

1. [Settings](#9--settings): Configure your app in settings.

1. [Screen selector](#10--screen-selector): Switch between different screens in your app. Tree view selections display here.

1. [Change canvas screen size](#11--change-canvas-screen-size): Change the display size of the canvas as you author your app.

Let's understand each option in Power Apps Studio in detail.

### 1 – Power Apps Studio modern command bar

Power Apps Studio options are available on the command bar. The options are relevant to the current session and app-related settings.

:::image type="content" source="media/studio/pa-studio-options.png" alt-text="Screenshot that shows the command bar menu with lots of development options." lightbox="media/studio/pa-studio-options.png":::

#### Modern command bar

The modern command bar displays the relevant set of commands depending on the control that is selected. For example, if you select an item to *insert* like a text label, you see the modern command bar change to accommodate your selection. The bar now has font type, size, color, and other text label controls.

:::image type="content" source="media/studio/pa-studio-command-bar.png" alt-text="Moving image that shows how the command bar changes depending on which control is selected." lightbox="media/studio/pa-studio-command-bar.png":::

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

 > [!NOTE]
 > You can't undo or redo data operations, such as insert or delete a datasource.

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

##### Popular controls to insert

| **Name**      | **Description** |
|---------------|-----------------|
| *Form* | Display, edit, or create a record in a data source. |
| *Input* > *Button* | A control that the user can select to interact with the app. |
| *Input* > *Date picker* | A control that the user can select to specify a date. |
| *Input* > *Text input* | A text box that allows user input |
| *Shapes* > *Rectangle* | A rectangular shape to configure the canvas appearance. |
| *Text* | A box that displays data such as text, numbers, dates, or currency. |
| *Vertical gallery* | A control that allows you to add other controls and display a set of data. For example, list items made up of an image, title, and description is contained within a vertical gallery. <br> :::image type="content" source="media/studio/vertical-gallery-example.png" alt-text="Screenshot showing what the vertical gallery template looks like."::: |

For more information about the controls you can insert, including their properties and definitions, go to [Controls and properties in canvas apps](reference-properties.md).

#### Add data

Add, refresh, or remove data sources from your canvas app. You can add one or more [connections](connections-list.md) by using data sources.  

:::image type="content" source="media/studio/pa-studio-add-data.png" alt-text="Screenshot that shows how to add data from the Add data dropdown list.":::

From the **Add data** menu, you can:

- Select any other existing tables from the current environment.
- Search and select a connector, such as **SharePoint** or **SQL Server**.

##### Connectors

In addition to data stored within tables, there are many connectors available to interact with data in popular software as a service (SaaS), services, and systems.

To choose other connectors such as SharePoint, OneDrive, or SQL Server, you can enter text in the data source search box or select from the list of connectors.

:::image type="content" source="media/studio/pa-studio-data-source-connector.png" alt-text="Screenshot that shows how to select a data source by choosing the Add data dropdown.":::

For more information, see [List of all Power Apps connectors](/connectors/connector-reference/connector-reference-powerapps-connectors).

#### New screen layouts

You can add a new screen to your app from the **New screen** option in the command bar or the **+ New screen** option in **Tree view**.

:::image type="content" source="media/studio/new-screen-from-command-bar.png" alt-text="Screenshot that shows the location of the New screen menu from the command bar.":::

Select from the list of available screen layouts such as **Sidebar**, new layouts in preview such as **Header and form**, or templates like **Email**.

:::image type="content" source="media/studio/pa-add-screen.png" alt-text="Screenshot that shows how to choose a layout from the New screen menu":::

#### Background color

Select a background color for a screen. You can select from the list of standard colors or select the **Custom** tab and choose your own color.

:::image type="content" source="media/studio/pa-studio-background-color.png" alt-text="Screenshot that shows where to choose a background color from the command bar.":::

#### Background image

Select **Upload** to upload images to set as the background image.

:::image type="content" source="media/studio/pa-studio-background-image.png" alt-text="Screenshot that shows where to choose a background image from the command bar.":::

#### Settings

Configure the app's settings from the [General](#general), [Display](#display), [Copilot](#copilot), [Updates](#updates), or [Support](#support) tab.

:::image type="content" source="media/studio/pa-studio-general-settings.png" alt-text="Screenshot that shows where to choose settings from the command bar."  lightbox="media/studio/pa-studio-general-settings.png":::

##### General

- Edit the app **Name** and **Description**.
- Add or update the **App icon**. Add a custom icon with **+ Add image**.
- Select an **Icon background fill** or **Icon fill** color.
- Toggle **Auto save** to save every two minutes automatically.
- Configure offline use.
- Set your **Data row limit**.
- Include debug information when you publish.
- Enable autocreation of environment variables.
- Enable the `App.OnStart` property.

For example, to edit the app **Name**, go to the **General** tab of **Settings**.

:::image type="content" source="media/studio/pa-studio-app-name-editor.png" alt-text="Screenshot where you edit your app name in the Settings popup.":::

##### Display

- Select the **Orientation** and screen **Size**.
- **Scale to fit**: Scales the app to fit available space.
- **Lock aspect ratio**: Locks the height and width ratio.
- **Lock orientation**: Maintains app orientation when device rotates.
- **Show mobile device notifications area**: Displays notifications at the top of the screen.

For more information, see [Change screen size and orientation](set-aspect-ratio-portrait-landscape.md).

##### Copilot

You can [add a custom Copilot to a canvas app (preview)](/power-apps/maker/canvas-apps/add-custom-copilot).

##### Updates

Allows you to configure advanced settings for the app that include features under preview, experimental or retired features.

For more information, see [Understand experimental, preview, and retired features in Power Apps](working-with-experimental-preview.md).

##### Support

Access current Power Apps Studio information such as environment, authoring version, session ID, and session details. This information is useful for Microsoft Support sessions.

### 2 – App actions

To perform app-specific actions, use the options such as **Properties**, **Comments**, **App checker**, **Share**, **Preview the app**, **Save**, and **Publish**.

:::image type="content" source="media/studio/pa-studio-actions-menu.png" alt-text="Screenshot that shows the app actions in the command bar.":::

#### Share

When you select the **Share** app action, you see a new tab or window open where you can share the app. You can share with other users or add them as co-owners of your app.

:::image type="content" source="media/studio/pa-studio-share-app.png" alt-text="Screenshot that shows the Share app action selected, opening in a new window or tab, where you can share the app with users and co-owners." lightbox="media/studio/pa-studio-share-app.png":::

> [!TIP]
> You must save the app before you can share it.

#### App checker

Select **App checker** to run a check.

For more information, see [PowerApps checker now includes App checker results for Canvas apps in solutions](https://powerapps.microsoft.com/blog/powerapps-checker-now-includes-app-checker-results-for-canvas-apps-in-solutions/).

:::image type="content" source="media/studio/pa-studio-app-checker.png" alt-text="Screenshot that shows where the App checker app action is located and its menu contents." lightbox="media/studio/pa-studio-app-checker.png":::

#### Comments

Comments are notes associated with items in your app. Use comments to help your team review the app and provide feedback, or provide additional information on implementation details in your app.

:::image type="content" source="media/studio/pa-studio-comments.png" alt-text="Screenshot that shows where the Comments app action is located and its menu where you can add a new comment.":::

#### Preview

Select **Preview the app** to go into preview mode. Here you can view and interact with the current version of the app.

:::image type="content" source="media/studio/pa-studio-preview.png" alt-text="Screenshot that shows where the Preview app action is located.":::

#### Save

You can save your app in different ways, such as **Save**, **Save with version notes**, **Save as**, or **Download a copy**. The save options dropdown is located next to the **Save** app action.

:::image type="content" source="media/studio/pa-studio-save-options.png" alt-text="Screenshot that shows where save options are located.":::

**Save options include**:

- **Save**: Saves recent and unsaved changes you made to the app. Each time you save changes, a new version is created.
- **Save with version notes**: Save and add notes about your updates.
- **Save as**: Duplicate the app by saving it with a different name.
- **Download a copy**: Download a local copy of the app.

#### Publish

Select **Publish** to publish the app’s current version. For more information, see [Save and publish canvas apps](save-publish-app.md).

:::image type="content" source="media/studio/pa-studio-publish.png" alt-text="Screenshot that shows where the Publish app action is located and its popup where you can add details to the publishing of your app." lightbox="media/studio/pa-studio-publish.png":::

### 3 – Properties list

When you select an object in your canvas, you can choose one of the object's properties from its properties list. For a complete list of all possible properties, see [All properties](reference-properties.md#all-properties).

:::image type="content" source="media/studio/pa-studio-prop-list.png" alt-text="Screenshot that shows the properties list of an object you select in your app canvas.":::

### 4 – Formula bar

The formula bar lets you add, edit, or remove functions of a property from your selected object. For example, select the app screen to update the background color by using the [RGBA function](/power-platform/power-fx/reference/function-colors).

:::image type="content" source="media/studio/pa-studio-formula-bar.png" alt-text="Screenshot that shows the formula bar." lightbox="media/studio/pa-studio-formula-bar.png":::

The formula bar is IntelliSense-enabled. When you start entering text that matches one or more functions, the formula bar shows a list of functions.

:::image type="content" source="media/studio/pa-studio-formula-bar-1.png" alt-text="Screenshot that shows the formula bar with IntelliSense in action as you type." lightbox="media/studio/pa-studio-formula-bar-1.png":::

When you select a function, the formula bar shows inline function help and highlights help text relevant to the cursor position.

:::image type="content" source="media/studio/pa-studio-formula-bar-2.png" alt-text="Screenshot that shows inline help for a function in the formula bar." lightbox="media/studio/pa-studio-formula-bar-2.png":::

If a formula returns an error, you can view the error details in **App checker** or directly from the app view in the canvas.

:::image type="content" source="media/studio/pa-studio-formula-bar-3.png" alt-text="Screenshot that shows formula errors viewed, using the App checker." lightbox="media/studio/pa-studio-formula-bar-3.png":::

Similarly, you find help when working with complex functions, nested functions, or when correcting a formula syntax.

For a complete list of all canvas app functions, see [Formula reference - Power Apps](/power-platform/power-fx/formula-reference).

### 5 – App authoring menu

Switch between various authoring options while working with the app.

:::image type="content" source="media/studio/pa-studio-app-authoring-menu.png" alt-text="Screenshot that shows the app authoring menu.":::

- **Tree view**: Shows a tree view of all screens and controls in the current app.
- [Insert](#insert): Allows you to add different controls to the screen.
- **Data**: [Add data](#add-data) and other [connectors](#connectors), such as tables that connect to your app.
- **Variables**: Work with [variables](working-with-variables.md) and [collections](create-update-collection.md) while editing your app.
- **Search**: Select to search for media, formulas, text, and more in your app.
- **Themes**: Choose a colored theme for the Power Apps UI.
- **Media**: Insert or remove media from the app.
- **Power Automate**: Add a flow using the [Power Automate pane](working-with-flows.md).
- **Advanced tools**: Allows you to access the [Monitor](../monitor-canvasapps.md) and [Test](test-studio.md) tools to debug and test your app.

The options for working with canvas apps change depending on your selection from the authoring menu. For example, when you select the **Tree view** menu option, you see a **Tree view** pane appear.

### 6 – App authoring options

#### Tree view

Select the tree view to show the screens available in the app.

:::image type="content" source="media/studio/pa-studio-tree-view.png" alt-text="Screenshot that shows the Tree view pane when you select Tree view from the authoring menu.":::

> [!TIP]
> Select **App** in the tree view to work with app-specific controls. You can change app behavior, such as adding a formula for the *OnStart* event of the app.

Switch to the **Components** tab of **Tree view** to work with component library features. You can add new components or reuse ones from the published component libraries. For more information, see [Component library](component-library.md).

:::image type="content" source="media/studio/pa-studio-components-tab.png" alt-text="Screeshot showing the Components tab of the Tree view pane.":::

For more information on adding components by selecting **+ New component**, see the [Insert](#insert) section.

#### Variables

You can save data such as resulting values from a data set into temporary storage by using variables. This section lists variables used by the current app. For more information, see [Variables in canvas apps](working-with-variables.md).

:::image type="content" source="media/studio/pa-studio-collections.png" alt-text="Screenshot that shows the collections in the app that are found in the Variables section.":::

A collection is a group of items that are similar, such as products in a product list. For more information, see [Collections in canvas apps](create-update-collection.md).

#### Search

You can find components in your app or find and replace them.

:::image type="content" source="media/studio/pa-studio-search.png" alt-text="Screenshot that shows how to select the Search option from the authoring menu.":::

#### Themes

You can choose a premade colored theme or custom-make your own colored theme by selecting **+ Add a theme**.

:::image type="content" source="media/studio/pa-studio-themes.png" alt-text="Screenshot that shows how to select the Themes option from the authoring menu.":::

#### Media

Select **Media** to add images, video, or audio files to your app. Adding media directly to your app uploads the files to the app and uses the app storage.

:::image type="content" source="media/studio/pa-studio-add-media.png" alt-text="Screenshot that shows how to select the Media option from the authoring menu.":::

> [!TIP]
>
> - Each file uploaded to the app as media must be 64 MB or smaller.
> - The size of all media files uploaded to an app can't exceed 200 MB.

If you want to reference more media, consider using [audio and video controls with URLs](add-images-pictures-audio-video.md#add-images-audio-or-video-using-the-controls), media from [Azure Media Services](add-images-pictures-audio-video.md#add-media-from-azure-media-services), or from [Microsoft Stream](./controls/control-stream-video.md#example).

For more information, see [Using multimedia files in Power Apps](add-images-pictures-audio-video.md).

#### Power Automate

Create a new flow with Power Automate, or select a flow you added previously.

:::image type="content" source="media/studio/pa-studio-create-flow.png" alt-text="Screenshot that shows where the Power Automate section is located.":::

For more information, see [Use Power Automate pane](working-with-flows.md).

#### Advanced tools

Advanced tools include **Monitor** and **Tests** where you can track and test your app.

:::image type="content" source="media/studio/pa-studio-advanced-tools.png" alt-text="Screenshot that shows where the Advanced tools section is located.":::

### 7 – Canvas/screen

The canvas shows the currently selected screen in the **Tree view** from the authoring menu.

You can [Use inline actions in Power Apps Studio](inline-actions.md) when you're editing a canvas app so you don't have to leave your current view. Inline actions help the development process to be more efficient.

### 8 – Properties pane

The properties pane shows properties and options available for the currently selected object on the canvas.

- The **Display** tab shows generic options such as the name, description, exit or exit message, and more.
- The **Advanced** tab shows options for customization with key value pairs in areas of action, data, and design in your app.

  > [!TIP]
  > The advanced properties might be locked for editing, such as when working with data cards. You can select [Unlock to change properties](working-with-cards.md#unlock-a-card) in such situations.

:::image type="content" source="media/studio/pa-studio-prop-pane.png" alt-text="Screenshot that shows the properties pane that appears when you select an object in your canvas. You see two tabs in this pane: **Display** and **Advanced**.":::

### 9 – Settings

You can access [Settings](#settings) at the bottom of the app authoring menu or from the command bar as previously described.


### 10 – Screen selector

Use the screen selector to switch between screens when your canvas app has multiple screens. You can also select a screen from the authoring menu by selecting the tree view. If the current selection is inside a container, or inside an individual cell in a gallery, the selector shows the breadcrumbs for the parent elements at each level.

:::image type="content" source="media/studio/pa-studio-screen-selector.png" alt-text="Screenshot that shows the location of the screen selector.":::

### 11 – Change canvas screen size

You can zoom in or out while authoring the canvas app. Select **Ctrl**+**0** (zero) to *fit to window*, which fits the canvas to the current authoring window size.

The following image shows what the canvas looks like when *fit to window*. You can also use the controls to zoom further in or out to view your canvas.

:::image type="content" source="media/studio/pa-studio-fit-canvas-to-window.png" alt-text="Screnshot that shows what a canvas fit to window looks like. This image also shows the zoom controls for your canvas." lightbox="media/studio/pa-studio-fit-canvas-to-window.png":::

> [!NOTE]
> The zoom percentage or screen size used in authoring a canvas app has no effect on the aspect ratio configured for the app. When you preview your app or play a published app, your screen size is temporary.
