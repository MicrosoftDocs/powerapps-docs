---
title: Understand Power Apps Studio | Microsoft Docs
description: Learn the components inside Power Apps Studio.
author: emcoope-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/16/2021
ms.subservice: teams
ms.author: emcoope
ms.reviewer: tapanm
contributors:
  - tapanm-msft
---

# Understand Power Apps Studio

When you create a canvas app by using any method, you're taken to the canvas app
builder called Power Apps Studio. You can use Power Apps Studio to design, build, and manage your canvas app.

## Overview of Power Apps Studio

![Power Apps Studio.](media/studio-power-apps.png "Power Apps Studio")

1. [Build hub](#1---build-hub) – select different pages in the Power Apps app.

1. [Power Apps Studio options](#2--power-apps-studio-options) – options relevant to the settings in a Power Apps Studio session.

1. [App actions](#3--app-actions) - options to rename, save, preview, or publish the app.

1. [Properties list](#4--properties-list) - list of properties for the selected object.

1. [Formula bar](#5--formula-bar) - compose or edit a formula for the selected property with one
or more functions.

1. [Power Apps app](#6--power-apps-app) – Power Apps app in Microsoft Teams.

1. [App authoring menu](#7--app-authoring-menu) - selection pane to switch between data sources and
insert options.

1. [App authoring options](#8--app-authoring-options) - details pane with options relevant to the selected
menu item for authoring the app.

1. [Canvas/screen](#9--canvasscreen) - primary canvas for composing the app structure.

1. [Properties pane](#10--properties-pane) - properties list for the selected object in UI format.

1. [Screen selector](#11--screen-selector) - switch between different screens in an app.

1. [Change canvas screen size](#12--change-canvas-screen-size) - change the size of the canvas during an authoring experience in Power Apps Studio.

Let's understand each option in Power Apps Studio in detail.

## 1 - Build hub

Opening Power Apps Studio from the build hub opens an app authoring experience
that inherits the Teams interface and options. The **Home**, **Build**, and **About** tabs are described in [Overview of the Power Apps app](overview-of-the-power-apps-app.md).

## 2 – Power Apps Studio options

Power Apps Studio options are available on the menu in the upper-left corner. The
options are relevant to the current session and app-related settings.

![Power Apps Studio options.](media/studio-options.png "Power Apps Studio options")

### Undo and redo

![Undo and redo.](media/studio-undo-redo.png "Undo and redo")

- **Undo** – undo the last action.
- **Redo** – repeat the last action.

### Cut, copy, and paste

![Cut, copy and paste.](media/studio-cut-copy-paste.png "Cut, copy and paste")

- **Cut** – Cut the selection, and store it in the clipboard.
- **Copy** – Copy the selection, and store it in the clipboard.
- **Paste** - Paste the last cut, or copied selection from the clipboard.

### Add data

![Add data.](media/studio-add-data.png "Add data")

- Create a new table by selecting **Create new table**.
- Select any other existing tables from the current environment.
- Search and select a connector, such as **SharePoint** or **SQL Server**.

### New screen

Add screens based on the available layouts.

#### Layouts

Select a new screen to add to the app based on the layout of the screen.

![Layout scenarios.](media/studio-scenarios.png "Layout scenarios")

Select a screen type based on the available scenarios, such as **Blank**, **Scrollable**, **List**, **Success**, **Tutorial**, **Email**, **People**, **Meeting**, or **Calendar**.

### App checker

Runs the [App checker](https://powerapps.microsoft.com/blog/powerapps-checker-now-includes-app-checker-results-for-canvas-apps-in-solutions/) with available rules and shows the results.

![App-checker.](media/studio-app-checker.png "App-checker")

### Settings

Configure the app's general settings.

![App settings.](media/studio-general-settings.png "App settings")

#### Name + icon

Shows app name, and allows changing the app icon. To update the icon, select a new icon or background color. To add or update description, enter text in the text box. You can also upload a custom icon for the app using the **Browse** option.

### Screen size + orientation

Shows the screen size and orientation. To change, select the radio buttons for **Orientation** and **Size**.

Advanced settings allow you to further customize the app screen configuration.

- **Scale to it**: Scales the app to fit available space.
- **Lock aspect ratio**: Locks the height and width ratio.
- **Lock orientation**: Maintains app orientation when device rotates.

To change the setting, toggle the switch.

More information: [Change screen size and orientation](../maker/canvas-apps/set-aspect-ratio-portrait-landscape.md)

#### Advanced settings

Allows you to configure advanced settings for the app.

- **Data row limit for non-delegable views** - Set the delegable data row limit. More information: [Understand delegation in canvas apps](../maker/canvas-apps/delegation-overview.md)
- **Improve data source experience and Dataverse views** - Use the improved data source experience when working with Dataverse. More information: [Dataverse and the improved data source experience](../maker/canvas-apps/use-native-cds-connector.md)
- **Preview, experimental and deprecated features** - Features that are in preview or experimental phases, or deprecated. More information: [Understand experimental, preview, and deprecated features in Power Apps](../maker/canvas-apps/working-with-experimental-preview.md)

### Power Automate

Create a new flow with Power Automate, or select any available flow.

![Power Automate.](media/studio-power-automate.png "Power Automate")

More information: [Create flows using the Power Apps app in Teams](/power-automate/teams/create-flows-power-apps-app)

### Collections

A collection is a group of items that are similar, such as products in a product list. This section lists the collections used by the current app. More information: [Collections in canvas apps](../maker/canvas-apps/create-update-collection.md) used by the app.

![Collections.](media/settings-collections.png "Collections")

### Variables

You can save data such as the result values from a data set into temporary storage by using variables. This section lists variables used by the current app. More information: [Variables in canvas apps](../maker/canvas-apps/working-with-variables.md) used by the app.

![Variables.](media/studio-variables.png "Variables")

### Account details

Shows account details including session details, current Power Apps app build
version, and other session details. You can also turn the **Auto save** option **On** or **Off**.

![Account details.](media/studio-account-details.png "Account details")

| Name | Description |
| - | - |
| Account | Allows to sign out from the current session. |
| Environment | Shows the current environment name. |
| Auto save | Set **Auto save** *On* or *Off*. When *On*, saves your changes at the interval of 2 minutes. |
| Power Apps version | Shows the version of Power Apps. |
| About Power Apps | Additional information and help. |
| Session details | Details about the current session. More information: [Session details](overview-of-the-power-apps-app.md#about)

> [!NOTE]
> We recommend that you keep the **Auto save** setting turned **On** and
save the changes to your app before closing Power Apps Studio.

## 3 – App actions

Use the options in the upper-right corner of Power Apps Studio to work with app-specific actions.

![App actions.](media/studio-app-actions.png "App actions")

### App name editor

Select the name of the app to edit it.

![App name editor.](media/studio-app-name-editor.png "App name editor")

### Save

Saves recent and unsaved changes you made to the app in Power Apps Studio. Each time you save changes, a new version is created.

### Preview

This will show a preview version of the app in Microsoft Teams that you can interact with.

### Publish to Teams

Publishes the app’s current version to a channel within Microsoft Teams. For more
information about publishing an app, go to [Publish an app](publish-and-share-apps.md#publish-and-add-an-app-to-teams).

## 4 – Properties list

Shows the list of available properties for the selected object on the canvas.
The properties list changes based on your selection. For a complete list of all properties, go to [All properties](../maker/canvas-apps/reference-properties.md#all-properties).

![Properties list.](media/studio-properties-list.png "Properties list")

## 5 – Formula bar

Use the formula bar to add, edit, or remove functions relevant to the selected
object and the property selected from the properties list. For example, select
the screen to update the background by using the [RGBA function](../maker/canvas-apps/functions/function-colors.md).

![Formula bar.](media/studio-formula-bar.png "Formula bar")

The formula bar is IntelliSense-enabled, and provides tips as you enter text to help you with the function syntax. If a formula returns an error, tips relevant to the syntax error and mitigation steps are displayed. When you start entering text that matches one or more functions, the formula bar shows inline function help and highlights help text relevant to the cursor position.

![Function in the formula bar.](media/studio-function-1.png "Function in the formula bar")

Similarly, you'll find help when working with complex functions, nested
functions, or when correcting a formula syntax.

For a quick and easy function reference, you can also select the formula drop-down menu.

![Formula drop-down menu.](media/studio-function-2.png "Formula drop-down menu")

Select an event type from the drop-down menu at the top of the dialog box, such as
**Action** instead of **Text**.

![Function event selection.](media/studio-function-3.png "Function event selection")

Select an action that you want to add a function for.

![Change in function event selection.](media/studio-function-4.png "Change in function event selection")

The available functions for the selected event type are dynamically updated
depending on the object you select. For example, if you selected a button on the
canvas, the available **Action** functions also include the function
*ClearCollect()*.

![Function ClearCollect() selected.](media/studio-function-5.png "Function ClearCollect() selected")

You can read the description of the selected **Action** function. Double-clicking a function name adds it into the formula bar.

For a complete list of all canvas app functions, go to [Formula reference](../maker/canvas-apps/formula-reference.md).

## 6 – Power Apps app

The Power Apps app in Teams is described in detail in [Overview of the Power Apps app](overview-of-the-power-apps-app.md).

## 7 – App authoring menu

On the left pane in Power Apps Studio, you switch between options such as **Insert**, **Data Sources**, and **Media**.

![App authoring menu.](media/studio-app-1.png "App authoring menu")

You can also select the expand button to expand the list to include names instead of just icons.

## 8 – App authoring options

The options for working with canvas apps change depending on the selection on the left pane, such as **Tree view**, **Insert**, **Data sources**, or **Media**.

![App authoring options.](media/studio-app-2.png "App authoring options")

### Tree view

Select the tree view to show the screens available in the app,

![Tree view.](media/studio-tree-view.png "Tree view")

> [!TIP]
> Select **App** in the tree view to work with app-specific controls or to
change app behavior, such as adding a formula on *OnStart* event of the app.

Switch to the **Components** tab to work with component library features. You can add
new components or reuse those that were already published from published
component libraries. More information: [Component library](../maker/canvas-apps/component-library.md)

![Tree view - components.](media/studio-tree-view-1.png "Tree view - components")

### Insert

**Insert** shows all the popular objects or controls that you can
add on the selected screen in your canvas app. You can also expand other
choices or use the components option to insert controls from a component
library.

![Insert.](media/studio-insert.png "Insert")

To insert controls on the canvas, you can drag the control to the canvas,
select the control, or select **(...)** and then select **Add to canvas**.

> [!TIP]
> Dataverse for Teams provides new components built on the [Fluent UI framework](https://www.microsoft.com/design/fluent/#/). More information: [Fluent UI controls](use-the-fluent-ui-controls.md).

#### Popular controls
| **Name**      | **Description**                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
|*Label* | A box that shows data such as text, numbers, dates, or currency. |
|*Edit form*|Display, edit, or create a record in a data source.|
|*Text*|A box that shows text.|
|*Text box*|A box in which the user can enter text, numbers, and other data.|
|*Vertical gallery*|A control that contains other controls and shows a set of data.|
|*Add icon*|Graphics for which you can configure appearance and behavior properties.|
|*Rectangle*|A rectangular shape to configure the canvas appearance.|
|*Date Picker*|A control that the user can select to specify a date.|
|*Button*|A control that the user can select to interact with the app.|

For more information about the controls that you can insert, and their properties
and definitions, go to [Controls and properties in Power Apps](../maker/canvas-apps/reference-properties.md).

#### Classic controls

Dataverse for Teams uses [Fluent UI controls](use-the-fluent-ui-controls.md) by default. If necessary, you can enable classic controls by using the experimental feature setting. To do this, go to **Settings** -> **Advanced settings** -> toggle **Classic controls** to **On** under experimental features.

After you enable classic controls, you'll be able to see and add them from the **Classic** category.

![Classic controls.](media/classic-control.png "Classic controls")

For example, you may need to enable classic controls when using [dependent drop-down lists](../maker/canvas-apps/dependent-drop-down-lists.md) when using Dataverse for Teams.

### Data

Add, refresh, or remove data sources from your canvas app. You
can add one or more
[connections](../maker/canvas-apps/connections-list.md)
by using data sources.  

In addition to data stored within tables, there are many connectors available to interact with data in popular SaaS, services, and systems.

![Data.](media/studio-data.png "Data")

![Add data - select data source.](media/studio-add-1.png "Add data - select data source")

Select **Create new table** to create a new table in the Dataverse for Teams
environment.

To choose other connectors such as SharePoint, OneDrive, or SQL Server, you can
enter text in the data source search box or select from the list of connectors.

![Select data source.](media/studio-select-1.png "Select data source")

More information: [List of all Power Apps connectors](/connectors/connector-reference/connector-reference-powerapps-connectors)

### Visual editor

When you select **Create new table** and enter a name for the new table, you open visual editor where you can design the table, add columns of different data types, enter data in rows, and save the changes.

![Visual editor.](media/studio-table-designer.png "Visual editor")

To get started with visual editor, select **Create a table** and enter
the table name. You can also expand the *Advanced settings* to update the table's plural name. For example, a table name can be *Shape*, and the plural table name can be *Shapes*.

![Create table.](media/studio-create-table.png "Create table")

Watch this video that shows you how to quickly create table and columns.
[!VIDEO https://www.microsoft.com/videoplayer/embed/RWJ4MI]

> [!NOTE]
> You can use visual editor in Power Apps Studio to quickly create a table while authoring an app. However, you can also use the [Build tab](edit-delete-table.md) to edit or delete the tables you create by using Power Apps Studio. Go to [Create tables in Microsoft Teams](create-table.md) for more information about creating tables by using the **Build** tab.

#### Understand visual editor

Visual editor allows you to work with table rows, columns, and data.

![Authoring a table in visual editor.](media/studio-table-1.png "Authoring a table in visual editor")

##### Table name

Select **Edit** ![Edit icon.](media/studio-edit-icon.png "Edit icon") to edit the name of the table.

![Edit the table name.](media/studio-edit-1.png "Edit the table name")

##### Add row

Select **Add row** to add a new row to the table.

![Add a row.](media/studio-add-row.png "Add a row")

##### Add columns

Select **Add columns** to add new columns of the available column types
supported by visual editor.

###### Supported column types

Visual editor supports specific data types as columns. The following options
are available when creating a new column using visual editor inside Power Apps Studio:

- Text
- Email
- URL
- Phone
- Auto number
- Number
- Date (Only dates without the user locale (time zone) settings are supported.)
- Decimal
- Lookup
- Choice
- Yes/No

> [!IMPORTANT]
> To add columns of types that aren't supported by visual editor, such as file or image, [create a table](create-table.md) by using the solution explorer instead.

###### Advanced options

The advanced options for columns change depending on the type of column. For example, a **Text** column type has an advanced option for **Max length**. By contrast, an **Auto number** column type has options such as the type of autonumbering, prefixes, and maximum number of digits. More information: [Types of fields](../maker/data-platform/types-of-fields.md)

##### Show/hide columns

Use the **Show/hide columns** option to show or hide available columns, including columns automatically created as part of the table metadata.

For example, you can add an *Owner* column created by default to the existing table.

![Show/hide columns.](media/show-hide-columns.png "Show/hide columns")

##### Refresh

Refreshes the current table with data.

##### Save

To save changes to a table, select **Save.** When you change a table and try to close it without saving changes, you're prompted to discard changes.

![Save changes.](media/studio-save-table-changes.png "Save changes")

To ensure that changes to the table are saved, you can select the next row inside the table, or select any other cell after editing a cell to trigger the auto save functionality.

![Saving changes.](media/studio-saving-changes.png "Saving changes")

After you close a saved table, you'll see the table added to the list of
available data sources in **Data** on the left pane.

![Data source added.](media/studio-data-1.png "Data source added")

##### Visual editor view

Select from the options of **Compact**, **Default**, or **Comfortable** layouts to switch the view with columns and rows spacing to change visual editor layout.

##### Row count

Shows the row counts in the table.

##### Column options

Select the drop-down menu next to the column heading to view column-related options.

![Column options.](media/studio-column-options.png "Column options")

| **Option**      | **Description**                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
| *Edit column*   | Edit the column name or advanced options. After it's created, you can't change the name of the column. |
| *Hide*          | Hide or unhide the column.                                                                           |
| *Insert column* | Insert a new column at the selected column location.                                                 |
| *A to Z*        | Sort records in ascending order.                                                                     |
| *Z to A*        | Sort records in descending order.                                                                    |
| *Filter by*     | Filter column data based on the filter criteria you define.                                                 |
| *Move left*     | Move the column to the left from the current position.                                               |
| *Move right*    | Move the column to the right from the current position.                                              |
| *Pin left*      | Pin the column to the left side of the table.                                                        |
| *Pin right*     | Pin the column to the right side of the table.                                                       |
| *Delete column* | Delete the column.                                                                                   |

##### Edit existing table

After you add rows and columns, and add data, you can close the table and use it as
the data source in your app. To edit content in the table, you can use
the app controls or go back to visual editor.

To edit the table, select the table data source, and then select **Edit data** to
open the table in visual editor.

![Edit table data.](media/studio-edit-2.png "Edit table data")

After you close visual editor, the data source is automatically refreshed
to reflect the updated data in Power Apps Studio. You can also select **Refresh**
to manually refresh Power Apps Studio to reflect the data in the controls you added on the canvas.

### Media

Select **Media** to add images, video, or audio files to your app. Adding media directly to your app uploads the files to the app and uses the app storage. Each file uploaded to the app as media must be 64 MB or smaller, and the size of all media files uploaded to an app can't exceed 200 MB.

![Media.](media/studio-media.png "Media")

If you want to reference more media, consider using [audio and video controls with URLs](../maker/canvas-apps/add-images-pictures-audio-video.md#add-images-audio-or-video-using-the-controls),
using media from [Azure Media Services](../maker/canvas-apps/add-images-pictures-audio-video.md#add-media-from-azure-media-services),
or from [Microsoft Stream](../maker/canvas-apps/controls/control-stream-video.md#example).
More information: [Using multimedia files in Power Apps](../maker/canvas-apps/add-images-pictures-audio-video.md)

## 9 – Canvas/screen

The canvas shows the currently selected screen from the left pane.

## 10 – Properties pane

The properties pane shows properties and options available for the currently
selected object on the canvas. The **Properties** tab shows generic options such as the name, color, size, or position. The **Advanced** tab shows more options for advanced customization. The advanced properties might sometimes be locked for editing, such as when working with data cards. You can select [Unlock to change properties](../maker/canvas-apps/working-with-cards.md#unlock-a-card) in such situations.

![Properties pane.](media/studio-properties-pane.png "Properties pane")

## 11 – Screen selector

Use the screen selector to switch between screens when your canvas app has multiple screens. You can also select a screen from the left pane by selecting the
tree view. If the current selection is inside a container, or inside an individual cell in a gallery, the selector shows the breadcrumbs for the parent elements at each level.

## 12 – Change canvas screen size

You can zoom in or zoom out while authoring the canvas app. Select **Ctrl**+**0**
**Fit to window** to fit the screen size
based on the current authoring window size. The zoom percentage or screen size you use while
authoring a canvas app has no impact on the aspect ratio configured for the app when you preview your app or play a published app.

### See also

[Use the Fluent UI controls](use-the-fluent-ui-controls.md)  
[Overview of the Power Apps app](overview-of-the-power-apps-app.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]