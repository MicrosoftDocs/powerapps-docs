---
title: Load models from CGTrader into mixed reality components (preview)
description: Learn how to load models from CGTrader into mixed reality components
author: iaanw
manager: shellyha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/2/2021
ms.subservice: canvas-maker
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - olidum
  - iaanw
---

# Load models from CGTrader into mixed reality components (preview)

[!INCLUDE[Preview disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The Power Platform offers a connector that can directly connect with CGTrader, a large source of free and premium 3D content with thousands of models.

Content from CGTrader can be browsed and loaded from inside a Power App and then used within the **View in 3D** and **View in MR** components.

> [!TIP]
> Learn how to [display 3D content in the **View in 3D** component](mixed-reality-component-view-3d.md) or learn how to [view 3D content in the real world with the **View in MR** component](mixed-reality-component-view-mr.md)

Connecting to an existing database of 3D content allows makers to build apps with mixed reality without having to create their own 3D models.

# Getting started with a new connector

Like other connectors, the CGTrader connector is a proxy to the CGTrader API. It provides [_actions_](/connectors/connectors#actions) that let users make requests to the CGTrader API and retrieve model data. You may also read the [connectors overview](/connectors/custom-connectors/use-custom-connector-powerapps) to learn more about connectors.

## Request access from CGTrader

Your connector will be linked to your CGTrader account, giving you access to any models you've purchased. To set up that access, contact CGTrader at [https://www.cgtrader.com/developers](https://www.cgtrader.com/developers).

CGTrader will review your information and contact you with an OAuth 2.0 API Key in the form of a **Client ID** and **Client Secret**. Be sure to store these in a secure location.

## Create a new CGTrader connector

Once you have your CGTrader API Key, go to the [Power Apps Maker Portal](https://make.powerapps.com/)

1. Expand the **Dataverse** tab.

2. Select **Connections**.

    :::image type="content" source="media/augmented/mixed-reality-connector-connections.png" alt-text="Screenshot of the maker portal side panel.":::
    
3. In the Connections page, select **New connection**.

4. Search for CGTrader and select it.

    :::image type="content" source="media/augmented/mixed-reality-connector-search.png" alt-text="Screenshot of the connections search result.":::
    
5. Enter the Client ID and Client Secret provided from CGTrader.

    :::image type="content" source="media/augmented/mixed-reality-connector-key.png" alt-text="Screenshot of the new connection panel.":::

You should now have a new CGTrader connection listed on the Connections page.

    :::image type="content" source="media/augmented/mixed-reality-connector-new.png" alt-text="Screenshot of the Connections page.":::

# Add the connector to your Power App

With an app open for editing in the [Power Apps Studio](https://create.powerapps.com):

1. Open the **Data** tab.

2. Select **Add data**.

3. Search for CGTrader and select it.

    :::image type="content" source="media/augmented/mixed-reality-connector-data-source.png" alt-text="Screenshot of the Data Source panel.":::
    
4. Select the latest connection of the CGTrader connector.

    :::image type="content" source="media/augmented/mixed-reality-connector-data-source-2.png" alt-text="Screenshot of the Data Source panel.":::

You can now bind your components to the CGTrader connector actions and browse and load models from CGTrader inside your app.

> [!TIP]
> A connection is an instance of a connector. You can have multiple connections with different configurations. New connections can also be configured inside of Power Apps Studio from the Data tab.

# Load CGTrader models directly into View in 3D or View in MR

After adding your connector to your app, you may load models directly into your app with the following steps.

1. On the [CGTrader website](https://www.cgtrader.com/), find the model(s) you want in your app.

2. On the page of your selected model(s), note the **Model ID** and the supported file types.

    :::image type="content" source="./media/augmented/mixed-reality-connector-model-id.png" alt-text="The model ID listed on the CGTrader model page.":::

3. Open your app with the connector in the [Power Apps Studio](https://create.powerapps.com):

4. Select the **View in 3D** component and/or the **View in MR** component and drag it to where you want it in the app.

    :::image type="content" source="./media/augmented/mixed-reality-connector-components.png" alt-text="Insert the View in 3D or View in MR component into the app.":::
    
5. On your **View in 3D** and/or **View in MR** component, set the **Source** property to **CGTrader.GetModel(model_id, "file_type")**, where model_id is the ID of your selected model and file_type is one of the supported file types.

    :::image type="content" source="./media/augmented/mixed-reality-connector-example.png" alt-text="The View in 3D component with a source from CGTrader.":::

# All Connector Actions

For full details on all the connector actions and their parameters and return types, refer to the [CGTrader connector reference](/connectors/cgtrader/#actions).

Action | Description | Example
-- | -- | --
**[GetModel](/connectors/cgtrader/#downloads-a-model-with-the-given-id-and-file-type.)** | Downloads a model with the given ID and file type. | CGTrader.GetModel(_model_id_, _"file_type"_)
**[GetModelInfo](/connectors/cgtrader/#gets-the-info-of-a-model-with-the-given-id.)** | Gets the info of a model with the given ID. | CGTrader.GetModelInfo(_model_id_)
**[SearchModels](/connectors/cgtrader/#searches-for-models-from-cgtrader-based-on-the-given-filters.)** | Searches for models from CGTrader based on the given filters. _Consider binding the items in a Gallery to this action._ | CGTrader.SearchModels({keywords:"_keywords_",extensions:"_file_types_"}).Models
**[GetCategories](/connectors/cgtrader/#gets-the-available-category-names-and-ids.)** | Gets the available category names and IDs. | CGTrader.GetCategories()
