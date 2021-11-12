---
title: Load models from CGTrader into mixed reality components (preview)
description: Learn how to load models from CGTrader into mixed reality components
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/12/2021
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - olidum
  - tapanm-msft
  - anuitz
---

# Load models from CGTrader into mixed reality components (preview)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

Microsoft Power Platform offers the [CGTrader connector](/connectors/cgtrader/) for connecting with CGTrader, a large source of free and premium (paid) 3D content with thousands of models. Content from CGTrader can be browsed and loaded from inside a canvas app, and then used within the [View in 3D](mixed-reality-component-view-3d.md) and [View in MR](mixed-reality-component-view-mr.md) components.

This connector acts as a proxy to the CGTrader APIs. It provides [_actions_](/connectors/connectors#actions) that allow users to make requests to the CGTrader API and retrieve model data. More information: [Connectors overview](/connectors/custom-connectors/use-custom-connector-powerapps)

Connecting to an existing 3D content database allows you to build apps with mixed reality without having to create your own 3D models.

## Request access from CGTrader

CGTrader connector links to your CGTrader account, allowing you access to 3D models available to your CGTrader account, including purchased content. 

To request access, contact [CGTrader for Developers](https://www.cgtrader.com/developers). CGTrader will review your information and contact you with an OAuth 2.0 API Key in the form of a **Client ID** and **Client Secret**.

> [!NOTE]
> Ensure you store the API key (Client ID and Client Secret) received from CGTrader in a secure location.

## Create a new CGTrader connector

Follow these steps to create a new CGTrader connector after you receive your [CGTrader API key](#request-access-from-cgtrader).

1. Sign in to [Power Apps](https://make.powerapps.com/).

1. Select **Dataverse** from the left-pane.

1. Select **Connections**.

1. Select **+ New connection**.

1. Search for and select **CGTrader (preview)**.

    :::image type="content" source="media/augmented/mixed-reality-connector-search.png" alt-text="Screenshot of the connections search result.":::

1. Enter the **Client ID** and **Client Secret** received from CGTrader.

    :::image type="content" source="media/augmented/mixed-reality-connector-key.png" alt-text="Screenshot of the new connection panel.":::

A new CGTrader connection is now listed on the **Connections** page.

:::image type="content" source="media/augmented/mixed-reality-connector-new.png" alt-text="Screenshot of the Connections page.":::

## Add the connector to your canvas app

1. [Edit](edit-app.md) an existing canvas app, or create a [blank canvas app](add-data-connection.md#open-a-blank-app).

1. Select **Data** from the left-pane.

1. Select **Add data**.

1. Search for and select **CGTrader**.

    :::image type="content" source="media/augmented/mixed-reality-connector-data-source.png" alt-text="Screenshot of the Data Source panel searching for CGTrader.":::

1. Select the connection that you created earlier.

    :::image type="content" source="media/augmented/mixed-reality-connector-data-source-2.png" alt-text="Screenshot of the Data Source panel when selecting a CGTrader connection instance":::

You can now bind your components to the CGTrader connector actions, and browse and load models from CGTrader inside your app.

> [!TIP]
> A connection is an instance of a connector. You can have multiple connections with different configurations. You can also create new connections from within Power Apps Studio when adding the connector by selecting **+ Add a connection**.

## Load CGTrader models directly into View in 3D or View in MR

After adding a CGTrader connection to your app, you can load models directly into your app with the following steps.

1. Find the model you want in your app from the [CGTrader website](https://www.cgtrader.com/).

1. Select the model, and then note the **Model ID** and the supported file types.

    :::image type="content" source="./media/augmented/mixed-reality-connector-model-id.png" alt-text="The model ID listed on the CGTrader model page.":::

1. Open your app in Power Apps Studio.

1. Select and drag a **View in 3D** or **View in MR** component to the canvas screen.

    :::image type="content" source="./media/augmented/mixed-reality-connector-components.png" alt-text="Insert the View in 3D or View in MR component into the app.":::

1. Set the **Source** property of the component (View in 3D/View in MR) to `CGTrader.GetModel(model_id, "file_type")`, where **model_id** is the ID of your selected model, and **file_type** is one of the supported file types.

    :::image type="content" source="./media/augmented/mixed-reality-connector-example.png" alt-text="The View in 3D component with a source from CGTrader.":::

## Connector actions

The below table lists the most common actions and examples. For a complete list of all connector actions, their parameters, and return types, go to the [CGTrader connector reference](/connectors/cgtrader/#actions).

| Action | Description | Example |
|--|--|--|
| **[GetModel](/connectors/cgtrader/#downloads-a-model-with-the-given-id-and-file-type.)** | Downloads a model with the given ID and file type. | `CGTrader.GetModel(_model_id_, _"file_type"_)` |
| **[GetModelInfo](/connectors/cgtrader/#gets-the-info-of-a-model-with-the-given-id.)** | Gets the info of a model with the given ID. | `CGTrader.GetModelInfo(_model_id_)` |
| **[SearchModels](/connectors/cgtrader/#searches-for-models-from-cgtrader-based-on-the-given-filters.)** | Searches for models from CGTrader based on the given filters. _Consider binding the items in a Gallery to this action._ | `CGTrader.SearchModels({keywords:"_keywords_",extensions:"_file_types_"}).Models` |
| **[GetCategories](/connectors/cgtrader/#gets-the-available-category-names-and-ids.)** | Gets the available category names and IDs. | `CGTrader.GetCategories()` |

### See also

- [View 3D content in canvas apps](mixed-reality-component-view-3d.md) <br>
- [View 3D content or images in the real word](mixed-reality-component-view-mr.md)
