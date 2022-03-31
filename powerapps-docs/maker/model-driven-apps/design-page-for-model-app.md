---
title: "Design a custom page for your model-driven app" 
description: "Learn how to design a custom page for your model-driven app"
ms.custom: ""
ms.date: 07/21/2021
ms.reviewer: ""

ms.subservice: mda-maker
ms.topic: "conceptual"
author: "aorth"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Design a custom page for your model-driven app (preview)

This article provides tips for designing a custom page for use in a model-driven app.

> [!IMPORTANT]
> - The base functionality of custom pages has moved to general availability in all regions.  However some specific or new capabilities are still in public preview and are marked with _(preview)_.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 
> - Custom pages are a new feature with significant product changes and currently have a number of known limitations outlined in [Custom Page Known Issues](model-app-page-issues.md).

## Supported controls in a custom page

Custom page authoring currently supports a subset of canvas app controls. The table below lists the currently supported controls.

  | Control | Control Type | Notes |
  | --- | --- | --- |
  |Label<sup>1</sup>|Display||
  |Text Box<sup>1</sup>|Input||
  |Date Picker<sup>1</sup>|Input|
  |Button<sup>1</sup>|Input|
  |Combo Box<sup>1</sup>|Input|
  |Check Box<sup>1</sup>|Input|
  |Toggle<sup>1</sup>|Input|
  |Radio Group<sup>1</sup>|Input|
  |Slider<sup>1</sup>|Input|
  |Rating<sup>1</sup>|Input|
  |[Vertical Container](../canvas-apps/controls/control-vertical-container.md)|Layout|New responsive horizontal layout container|
  |[Horizontal Container](../canvas-apps/controls/control-horizontal-container.md)|Layout|New responsive horizontal layout container|
  |[Rich Text Editor](../canvas-apps/controls/control-richtexteditor.md)|Input|
  |[Gallery](../canvas-apps/controls/control-gallery.md)|List|
  |[Icon](../canvas-apps/controls/control-shapes-icons.md)|Media|
  |[Image](../canvas-apps/controls/control-image.md)|Media|
  |[Edit Form](../canvas-apps/controls/control-form-detail.md)|Input|
  |[Display Form](../canvas-apps/controls/control-form-detail.md)|Input|
  |Code components|Custom| [Add code components to a custom page](page-code-components.md)|
  |Canvas components (preview) |Custom| [Add canvas components to a custom page](page-canvas-components.md)|
  
<sup>1</sup> Control is a new modern control. The control was introduced for [canvas apps in Teams]( /power-platform-release-plan/2020wave1/microsoft-powerapps/build-apps-teams-modern-controls). The control is based on [Fluent UI library](https://developer.microsoft.com/fluentui#/controls/web) wrapped with  [Power Apps Component Framework](../../developer/component-framework/overview.md).

## Custom components support for custom page

You can add both low-code (canvas components) and pro-code (code components) custom UX components to your environment and make them available for all makers. For custom page specific UX extensibility articles, see [add canvas components to a custom page for your model-driven app](/powerapps/maker/model-driven-apps/page-canvas-components) and [add code components to a custom page for your model-driven app.](/powerapps/maker/model-driven-apps/page-code-components) 

In general, the low-code extensibility approach is simpler to build, test, and has a lower maintenance cost. We recommend evaluating canvas components first and then use code components only if there is a need for more complex and advanced customization.

More information:
- [Canvas component gallery](https://powerusers.microsoft.com/t5/Canvas-Apps-Components-Samples/bd-p/ComponentsGallery)
- [Code components samples](../../developer/component-framework/use-sample-components.md)
- [Code components community resources](../../developer/component-framework/community-resources.md)

## Enable responsive layout with container control

Responsive custom page layouts are defined by building a hierarchy of **Horizontal layout container** and **Vertical layout container** controls.  These controls are found in the canvas app designer under **Layout** on the **Insert** tab.

Set the minimum screen height and width on the **App** object to prevent page level scroll bars and use a vertical body scroll bar.

  ```powerappsfl
  MinScreenHeight=200
  MinScreenWidth=200
  ```

Optionally, the custom page design size can be adjusted in **Settings** > **Display** with **Size** set to **Custom**.  Then set the **Width** and **Height** to a more typical desktop custom page size like width 1080 and height 768.  Changing this setting after controls are added to the screen may cause some layout properties to become reset.

Set the topmost container to fill the entire space and resize based on available space.  

  ```powerappsfl
  X=0
  Y=0
  Width=Parent.Width
  Height=Parent.Height
  ```

### Horizontal wrapping of a flexible height container 

To support pages adjusting from desktop down to a narrow width, enable these properties on a horizontal container with flexible height.  Without these settings, the page will clip controls when the page is narrow.

  ```powerappsfl
  Direction=Horizontal
  FlexibleHeight=true
  Justify=Stretch
  Align=Stretch
  VerticalOverflow=Scroll
  Wrap=True
  ```

Child containers or controls directly under this container should be set to have a minimum width that allows the page to fit within a 300 px width.  Consider the padding on the container or control as well as parent containers. 

### Vertical wrapping of a flexible width container 

To support pages adjusting from desktop down to a narrow width, enable these properties on a vertical container with flexible width.  Without these settings, the page will clip controls when the page is narrow.

  ```powerappsfl
  Direction=Vertical
  FlexibleWidth=true
  Justify=Stretch
  Align=Stretch
  HorizontalOverflow=Scroll
  Wrap=True
  ```

Child containers or controls directly under this container should be set to have a minimum height that allows the page to fit within a 300 px width.  Consider the padding on the container or control as well as parent containers. 

More information: [Building responsive layout](../canvas-apps/build-responsive-apps.md "Building responsive layout").

### Vertical container with fixed header, flexible body, fixed footer

1. On the **Vertical Container**, set **Align (horizontal)** to **Stretch**

1. Insert three **Horizontal Container** controls within the parent **Vertical Container**

1. On the first and third child horizontal container controls, set **Stretch height** off and reduce height to space needed, such as *Height=80*.

### Horizontal container with two even child containers

1. On the parent horizontal container, set **Align (vertical)** to **Stretch**.

1. Insert two **Vertical Container** controls within the parent **Horizontal Container**.


## Styling custom page controls to align to model-driven app controls

By creating the custom page from the modern app designer, these features use the default values.  

- Theme for the custom page. Theme values for the controls used in a custom page are automatically set to match the default blue theme of the Unified Interface. This default theme is used both in the studio and at application runtime. Explicit theme selecting is removed from custom page authoring experience.

- Controls need to use a different font size, which is based on their position in the page hierarchy.

    > [!Note]
    > Custom page text has a upscaling of 1.33 so you need to divide the target **FontSize** by 1.33 to get the desired size.

    | Label Type | Target FontSize | FontSize to use |
    | --- | --- | --- |
    |Page title|17|12.75|
    |Normal labels|14|10.52|
    |Small labels|12|9.02|

- Primary and secondary button controls need the following styling changes:

    Primary buttons
    ```powerappsfl
    Color=RGBA(255, 255, 255, 1)
    Fill=RGBA(41,114,182,1)
    Height=35
    FontWeight=Normal
    ```

    Secondary buttons
    ```powerappsfl
    Color=RGBA(41,114,182,1)
    Fill=RGBA(255, 255, 255, 1)
    BorderColor=RGBA(41,114,182,1)
    Height=35
    FontWeight=Normal
    ```

## Tab navigation and keyboard accessibility for custom pages

Custom pages follow the same tab navigation design that's used by the hosting model-driven app. Visually aligned semantic HTML structure helps users navigate the custom pages seamlessly when using a keyboard or a screen reader. Note that unlike stand alone canvas apps, custom page controls and other UX elements don't need explicit tab numbers assignments. Modern controls don't have a `TabIndex` property and utilize the semantic HTML structure for navigation. 

Various elements like controls, canvas and code components, containers and so on can be tabbed based on their position in the custom page layout. The tab navigation follows Z order navigation. Individual tab-stops inside larger grouping elements like components, containers are navigated first before the tab moves out to the next element in the document object model (DOM) tree.

Here is an example navigation with the page containing controls, code, and canvas components and containers.

:::image type="content" source="media/add-component-to-model-app/tab-navigation-with-components-pcf-containers-and-controls.png" alt-text="Custom page tab navigation." lightbox="media/add-component-to-model-app/tab-navigation-with-components-pcf-containers-and-controls.png":::

> [!NOTE]
> Overlapping controls and elements on the custom page will not have their DOM merged so tab stops can be out of sync from visual layout. The same is true for the dynamic element positioning using formulas.  

### See also

[Model-driven app custom page overview](model-app-page-overview.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Building responsive layout](../canvas-apps/build-responsive-apps.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)
