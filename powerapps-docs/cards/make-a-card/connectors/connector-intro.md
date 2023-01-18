---
title: Add connectors to a card (preview)
description: Learn how to add connectors to your cards for Microsoft Power Apps.
ms.date: 09/20/2022
ms.topic: how-to
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add connectors to a card (preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

Connectors allow your card to connect to other apps, data sources, and devices in the cloud. Insert, modify, and remove them in the [card designer](../designer-overview.md). [Learn more about connectors in Power Platform](/connectors/connectors).

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Insert a connector

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards (preview)** > **Cards**, and then select a card.
1. In the left pane of the card designer, select **Data**.
1. Select **+ Add data**, and then select a data source from the list.

    :::image type="content" source="../../media/connector-intro/add-data-location.png" alt-text="Screenshot of a list of data sources in the card designer.":::

## Refresh a connector
When the schema provided by your connector changes, you can refresh the connector in your card to ensure you have access to the updated properties in your PowerFx expressions. An example of a schema change would be adding a column to the Dataverse table you are using in your card. After refreshing your connector, you would be able to use the new column in your PowerFx expressions.

> [!IMPORTANT]
> You should be careful not to remove properties from your data sources that existing cards depend on. Doing so could prevent your existing cards from functioning properly.

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards (preview)** > **Cards**, and then select a card.
1. In the left pane of the card designer, select **Data**.
1. Select **...** next to the connector you want to refresh.
1. Click **Refresh**

    :::image type="content" source="../../media/connector-intro/refresh-data-connector.png" alt-text="Screenshot of a refreshing data source in the card designer.":::

## Types of connectors

Only connections to Dataverse are currently available. Other connectors are shown in the data source list, but functionality for them will be added in future updates.

You can connect to Dataverse tables to create, read, update, and delete records. [Learn how to create a card with data from Dataverse](../../tutorials/dataverse-card.md).
