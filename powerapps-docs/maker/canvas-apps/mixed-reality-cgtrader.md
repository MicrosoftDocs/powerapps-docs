---
title: Load 3D models from CGTrader into mixed reality controls (preview)
description: Add 3D models from CGTrader into mixed reality controls in your canvas apps.
author: anuitz
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mduelae
ms.date: 3/3/2022
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - olidum
  - mduelae
  - anuitz
---

# Load 3D models from CGTrader into mixed reality controls (preview)

[This article is pre-release documentation and is subject to change.]

>[!IMPORTANT]
>This is a preview feature.
>[!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

Want to build apps with mixed-reality 3D content without having to create your own 3D models? Use the [CGTrader connector](/connectors/cgtrader/) to import 3D content from CGTrader into your canvas apps. CGTrader offers a library of thousands of free and premium 3D models. Browse and load models inside your app, and then use them with the [3D object](mixed-reality-component-view-3d.md) and [View in MR](mixed-reality-component-view-mr.md) controls.

The connector provides a no-code replacement for working with the CGTrader API. Using [*actions*](/connectors/connectors#actions), apps send requests to the CGTrader API and fetch model data. For more information, see the [Connectors overview](/connectors/custom-connectors/use-custom-connector-powerapps).

## Prerequisites

Request an API key (OAuth client ID and client secret) at https://www.cgtrader.com/developers. Be sure to store your API key in a secure location.

## Create a CGTrader connection

You'll need to create a CGTrader connection in Power Apps after you receive your API key. In this example, we'll create a connection on the Power Apps home page. You can also create a connection when you're editing an app in Power Apps Studio.

>[!TIP]
>A connection is an instance of a connector. You can create multiple connections with different configurations.

1. Sign in to [Power Apps](https://make.powerapps.com/).
1. In the navigation bar, select **Data** > **Connections** > **New connection**.

    :::image type="content" source="./media/augmented/mixed-reality-connector-create.png" alt-text="A screenshot of the Power Apps data connections window.":::

1. Search for and select **CGTrader (preview)**.

    :::image type="content" source="./media/augmented/mixed-reality-connector-search.png" alt-text="A screenshot of the Power Apps connections search result with CGTrader selected.":::

1. Enter the **Client ID** and **Client Secret** you received from CGTrader.

    :::image type="content" source="./media/augmented/mixed-reality-connector-key.png" alt-text="A screenshot of the CGTrader connector account window.":::

A CGTrader connection is now listed on the **Connections** page.

## Add a CGTrader connection to your canvas app

1. [Edit](./edit-app.md) or create a [canvas app](./create-blank-app.md).

1. In the navigation bar, select **Data** > **Add data**. Search for and select **CGTrader**.

    :::image type="content" source="media/augmented/mixed-reality-connector-data-source.png" alt-text="A screenshot of the Microsoft Power Apps Studio data source panel, with a search for CGTrader shown.":::

1. Select the connection you created earlier.

## Load CGTrader models directly into 3D object or View in MR controls

1. Find and select a model on the [CGTrader website](https://www.cgtrader.com/).
1. Note the supported file types and Model ID.

    :::image type="content" source="./media/augmented/mixed-reality-connector-model-id.png" alt-text="A screenshot of the file types and Model ID of a 3D object on CGTrader.com.":::

1. In Power Apps Studio, add a [**3D object**](./mixed-reality-component-view-3d.md) or [**View in MR**](./mixed-reality-component-view-mr.md) control to the app screen.
1. Set the control's **Source** property to **CGTrader.GetModel(*model_id*, "*file_type*")**, where *model_id* is the ID of the model you selected, and *file_type* is one of the supported file types.

    :::image type="content" source="./media/augmented/mixed-reality-connector-example.png" alt-text="A screenshot of a 3D object control under construction in Microsoft Power Apps Studio, shown with its Source property set to a CGTrader model.":::

## Connector actions

The following table lists the most common CGTrader connector actions and examples. For a list of all connector actions, their parameters, and return types, see the [CGTrader connector reference](/connectors/cgtrader/#actions).

| Action | Description | Example |
|-|-|-|
| **[GetModel](/connectors/cgtrader/#downloads-a-model-with-the-given-id-and-file-type.)** | Downloads a 3D object with the given Model ID and file type. | **CGTrader.GetModel(*model_id*, *"file_type"*)** |
| **[GetModelInfo](/connectors/cgtrader/#gets-the-info-of-a-model-with-the-given-id.)** | Gets information about a 3D object with the given Model ID. | **CGTrader.GetModelInfo(*model_id*)** |
| **[SearchModels](/connectors/cgtrader/#searches-for-models-from-cgtrader-based-on-the-given-filters.)** | Searches for models from CGTrader based on the given filters. Consider binding this action to the items in a gallery. | **CGTrader.SearchModels({keywords:"*keywords*",extensions:"*file_types*"}).Models** |
| **[GetCategories](/connectors/cgtrader/#gets-the-available-category-names-and-ids.)** | Gets available category names and Model IDs. | **CGTrader.GetCategories()** |

### See also

- [View 3D content in canvas apps](mixed-reality-component-view-3d.md)
- [View 3D content or images in the real world](mixed-reality-component-view-mr.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
