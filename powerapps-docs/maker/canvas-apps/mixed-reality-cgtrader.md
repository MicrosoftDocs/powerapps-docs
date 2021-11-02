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
Like other connectors, the CGTrader connector is a proxy to the CGTrader API. It provides [_actions_](/connectors/connectors#actions) that let users make requests to the CGTrader API and retrieve model data. You may read the [custom connector overview](/connectors/custom-connectors/use-custom-connector-powerapps) to understand the full process. 

The following describes how to create a new CGTrader connector.

## Request access from CGTrader
Your connector will be linked to your CGTrader account, giving you access to any models you've purchased. To set up that access, contact CGTrader at [https://www.cgtrader.com/developers](https://www.cgtrader.com/developers).

CGTrader will provide an OAuth 2.0 API Key in the form of a Client ID and Client Secret. Be sure to store these in a secure location.

## Create a new CGTrader connector
Once you have your CGTrader API Key, go to the [Power Apps Maker Portal](https://make.powerapps.com/)

1. Expand the **Dataverse** tab.
2. Select **Connections**.
    :::image type="content" source="media/augmented-connector/mixed-reality-connector-connections.png" alt-text="Screenshot of the maker portal side panel.":::
3. In the Connections page, select **New connection**.
4. Search for CGTrader and select it.
    :::image type="content" source="media/augmented-connector/mixed-reality-connector-search.png" alt-text="Screenshot of the connections search result.":::
5. Enter the Client ID and Client Secret provided from CGTrader.
    :::image type="content" source="media/augmented-connector/mixed-reality-connector-key.png" alt-text="Screenshot of the new connection panel.":::

You should now have a new CGTrader connection listed on the Connections page.
    :::image type="content" source="media/augmented-connector/mixed-reality-connector-key.png" alt-text="Screenshot of the connections search result.":::


# Add the connector to your Power App

## Connector Actions

## Load CGTrader models directly into View in 3D or View in MR

## Browse through CGTrader models 
