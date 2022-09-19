---
title: "Create a card with data from Dataverse"
description: "Create a card that uses connectors"
keywords: "Card Designer, Power Apps, cards, tutorial, Dataverse, connectors"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Use connectors

This needs to be updated for specifically Dataverse

In this tutorial, you'll learn how to build a card that utilizes the Bing Connector to add search query results to a card. You'll also learn about:

- Connectors, specifically Bing Search
- How to use more of the elements
- More advanced PowerFX expressions

The result will look like the example below:

:::image type="content" source="../media/tutorial-use-connectors/use-connectors-card.png" alt-text="Screenshot of a finished card using the Bing search connector." border="false":::

## Basic data binding

1. Create your card. You'll be asked to name your card&mdash;use something you'll remember later when you go looking for it, like "Bing Search".

   :::image type="content" source="../media/tutorial-use-connectors/rename-card-title.png" alt-text="Screenshot of the card renamed to Bing search." border="false":::

1. Remove the default text box.

1. From the Elements side menu, drag and drop an **Input.Text** box under the card title.

   :::image type="content" source="../media/tutorial-use-connectors/add-new-input-text-box.png" alt-text="Screenshot of a new input text box added under the title box." border="false":::

1. Add a descriptive label to the input text box, such as `Search for:`

   :::image type="content" source="../media/tutorial-use-connectors/add-search-for-label.png" alt-text="Screenshot of how to add the search for label to the input text box." border="false":::

1. Set the following properties:
   1. **Name**: `query`
   1. **Default value**: `${query}`

   :::image type="content" source="../media/tutorial-use-connectors/adding-query-vars.png" alt-text="Screenshot of how to add query to the input text box properties." border="false":::

1. Drag and drop a **Button Group** into the card under the card description.

   :::image type="content" source="../media/tutorial-use-connectors/add-button-group-to-card.png" alt-text="Screenshot of an added button group." border="false":::

1. Click **Add Button**.

1. Set the button **Title** to `Back`.

   :::image type="content" source="../media/tutorial-use-connectors/add-button-title-back.png" alt-text="Screenshot showing a button renamed to back." border="false":::

1. In the PowerFX code line at the top, add the following for this button: `Back();`

   :::image type="content" source="../media/tutorial-use-connectors/add-back-pfx-to-button.png" alt-text="Screenshot showing Power FX expression to add to back button to make functional." border="false":::

1. Select the empty space around the Back button to re-select the Button Group.

1. Select **Add Button**.

   :::image type="content" source="../media/tutorial-use-connectors/add-new-button-to-group.png" alt-text="Screenshot showing how to add a second button to the button group." border="false":::

1. Name the new button `Search`.

   :::image type="content" source="../media/tutorial-use-connectors/add-button-title-search.png" alt-text="Screenshot showing a second button renamed to search." border="false":::

1. Select **Data Connections** from the Navigation bar and then select **Add data**.

   :::image type="content" source="../media/tutorial-use-connectors/go-to-data-connections.png" alt-text="Screenshot showing how to get to the data connections pane." border="false":::

1. Select the **+ plus** next to **Bing Search**.

   :::image type="content" source="../media/tutorial-use-connectors/add-bing-connector.png" alt-text="Screenshot showing how to add the Bing search connector to the card." border="false":::

1. Go to the **Variables** tab and select **New variable**.

   :::image type="content" source="../media/tutorial-use-connectors/add-new-var.png" alt-text="Screenshot showing how to add a new variable to the card." border="false":::

1. Create a variable to store the results of your Bing search, here called `searchResults`, then set the variable type to array.

   :::image type="content" source="../media/tutorial-use-connectors/create-search-results-array.png" alt-text="Screenshot showing how to set up the search results array variable." border="false":::

1. Save the card.

1. With the Search button selected, go to the PowerFX editor and enter the following: `Set(searchResults, bingSearch.GetNews(query));`

   :::image type="content" source="../media/tutorial-use-connectors/add-pfx-to-search-button.png" alt-text="Screenshot showing how to add power fx to the search button to use the bing connector." border="false":::

1. To output the search results as clickable links, add another text box below the buttons. Add the following to the text box: `[${name}](${url})`.

   :::image type="content" source="../media/tutorial-use-connectors/add-pfx-for-links.png" alt-text="Screenshot showing how to add power fx to a text box to make the resulting links clickable." border="false":::

1. With the text box selected, go to the PowerFX bar at the top and enter searchResults. Make sure the drop down to the left is set to **Repeat for Every**.

   :::image type="content" source="../media/tutorial-use-connectors/add-search-results-to-text-box.png" alt-text="Screenshot showing how to make each link show up in the results." border="false":::

1. Save and preview your card.

   :::image type="content" source="../media/tutorial-use-connectors/preview-search-card.png" alt-text="Screenshot showing a working bing search card, with clickable links for each result." border="false":::

### More advanced data binding

Instead of just showing a clickable link, you can also set the Bing search up to show a photo and a short description of each article in the search.

1. Remove the text box from your card and add a **ColumnSet** element.

   :::image type="content" source="../media/tutorial-use-connectors/add-column-set.png" alt-text="Screenshot showing a column set added to the card in place of the text box from previous steps." border="false":::

1. Add a column for the article photo and set the column width to **auto**.

   :::image type="content" source="../media/tutorial-use-connectors/set-column-to-auto.png" alt-text="Screenshot showing how to set the columns in the column set to auto width." border="false":::

1. Drag and drop an **Image** element into the column.

   :::image type="content" source="../media/tutorial-use-connectors/add-image-to-column.png" alt-text="Screenshot of an image block added to the first column in the column set." border="false":::

1. Add the following to the image **Url** box: `= image.thumbnail.contentUrl`

1. Select the empty space around the first column to re-select the ColumnSet.

1. Add a second column to the ColumnSet and make sure the column width is set to **stretch**.

   :::image type="content" source="../media/tutorial-use-connectors/add-second-column.png" alt-text="Screenshot showing a second column added to the column set." border="false":::

1. Add a **Text block** to the second column and add the following: `[${name}](${url})`

1. Drag a second **Text block** into the column underneath the first and add the following: `${description}`

   :::image type="content" source="../media/tutorial-use-connectors/add-pfx-to-second-col.png" alt-text="Screenshot of power fx expressions added to text blocks within the second column." border="false":::

1. With the ColumnSet selected, go to the PowerFX bar at the top and enter `searchResults`. Make sure the drop down to the left is set to **Repeat for Every**.

   :::image type="content" source="../media/tutorial-use-connectors/add-pfx-to-column-set.png" alt-text="Screenshot showing the power fx to add to the column set to view each search result in the card." border="false":::

1. Save and preview your card.
