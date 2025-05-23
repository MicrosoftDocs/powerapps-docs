---
title: "Add a custom page to your model-driven app" 
description: " Learn how to add a custom page to a model-driven app"
ms.date: 01/16/2025
ms.reviewer: "matp"
ms.subservice: mda-maker
ms.topic: "how-to"
author: "aorth"
ms.author: "aorth"
search.audienceType: 
  - maker
---
# Add a custom page to your model-driven app

This article guides you through creating and editing a custom page for a model-driven app using the modern app designer.

> [!IMPORTANT]
> Custom pages are a new feature with significant product changes and currently have a number of known limitations outlined in [Custom Page Known Issues](model-app-page-issues.md).

This article walks you through opening a model-driven apps in the app designer, which you use to add a custom page to a model-driven app. If you need to create a new model-driven app, go to [Create a model-driven app with the app designer](create-model-driven-app.md).

## Create or edit a custom page

Custom pages can be created from two places. The first is while authoring a model-driven app in the modern app designer. The other is from the **Solutions** area in Power Apps. Custom pages can be edited from the **Solutions** area but won't appear in the **Home** or **Apps** areas of make.powerapps.com.

> [!NOTE]
> Custom pages must be created from a solution either from the modern app designer and or the **Solutions** area in Power Apps using **New** > **App** > **Page**. The custom page is a different canvas app type than the normal standalone canvas app.

### Create new custom page from modern app designer

1. Open [make.powerapps.com](https://make.powerapps.com/?cds-app-module-designer.isCustomPageEnabled=true&oneCdsDesigner.enableCustomCanvasPage=true)

1. On the left navigation pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the solution containing the existing model-driven app.

1. Select the model-driven app where you want to add a custom page, and then select **Edit** on the command bar.

1. In the app designer, select **Add page** > **Custom page** on the command bar.

1. Select **Create custom page**.

   :::image type="content" source="media/add-page-to-model-app/app-designer-create-new-custom-page.png" alt-text="New page select custom page":::

1. Power Apps Studio opens for page authoring.

    > [!div class="mx-imgBorder"]
    > ![Power Apps Studio new page](media/add-page-to-model-app/canvas-designer-new-page.png "Power Apps Studio new page")

1. When you're finished creating your canvas app custom page, **Save**, **Publish**, and then close the Power Apps Studio browser tab to return to the model-driven app designer.

### Create new custom page from the solutions area

1. Sign in to [Power Apps](https://make.powerapps.com/?cds-app-module-designer.isCustomPageEnabled=true&oneCdsDesigner.enableCustomCanvasPage=true)

1. Select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open or create a solution to contain the new custom page

1. Select **New > App > Page**.

    > [!div class="mx-imgBorder"]
    > ![Solutions area create new page](media/add-page-to-model-app/solution-explorer-new-page.png "Solutions area create new page")

### Edit an existing custom page

1. Open up [make.powerapps.com](https://make.powerapps.com/?cds-app-module-designer.isCustomPageEnabled=true&oneCdsDesigner.enableCustomCanvasPage=true)

1. Select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)] 
1. Open or create a solution to contain the new custom page.

1. Select the custom page with **Page** type, and then select **Edit**.

    > [!div class="mx-imgBorder"]
    > ![Solutions area new page](media/add-page-to-model-app/solution-explorer-edit-page.png "Solutions area new page")

## Author custom page content

1. Design the custom page content. More information: [Design a custom page for your model-driven app](design-page-for-model-app.md)

1. Save and publish the custom page.

1. Close Power Apps Studio.

1. Return to the app designer browser tab and refresh the app designer by selecting **Dismiss**.

    > [!div class="mx-imgBorder"]
    > ![Dismiss creating your page prompt](media/add-page-to-model-app/app-designer-creating-page-prompt.png "Dismiss creating your page prompt")

1. Select **Publish** in the app designer to add the changed custom page into the model-driven app.

1. Select **Preview** to play the app in a new browser tab.

## Add an existing custom page into a site map

1. Sign into [make.powerapps.com](https://make.powerapps.com/?cds-app-module-designer.isCustomPageEnabled=true&oneCdsDesigner.enableCustomCanvasPage=true)

1. Open an existing model-driven app using modern app designer.

1. Select the **Add page** > **Custom page** on the command bar.

1. Select the custom page in the list of custom pages available in the environment, and then select **Add**.

   :::image type="content" source="media/add-page-to-model-app/app-designer-select-existing-page.png" alt-text="Select and existing custom page to add to the app":::

1. Select **Publish**, which also saves the app if there are changes.

1. Select **Play** to run the app in a new browser tab.

1. To close the app designer select **Back** and return to the solution.

## Publishing a custom page

> [!IMPORTANT]
> Currently, model-driven apps must be re-published after a custom page is published.  Otherwise the model-driven app continues to use the previous published custom page.

After saving changes to a custom page in Power Apps Studio, the custom page must be first published by Power Apps Studio. Then all model-driven apps referencing that custom page need to be published. 

1. From Power Apps Studio, select **Publish**

1. From app designer or solution explorer, select **Publish** on each model-driven app referencing the custom page

### See also

[Model-driven app custom page overview](model-app-page-overview.md)

[Design a custom page for your model-driven app](design-page-for-model-app.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Navigating to a custom page using client API](../../developer/model-driven-apps/clientapi/navigate-to-custom-page-examples.md)

[Code components for custom page designer](../../developer/component-framework/component-framework-for-canvas-apps.md)
