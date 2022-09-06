---
title: "Debugging Cards"
description: "Learn how to debug your cards using the Play page in designer"
keywords: "Card Designer, Power Apps, cards, debugging, play page"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# The Play Page and Debugging Cards

Once you've created a card, you can view what your finished card will look like before sending it out to your teammates. This is done via the Play Page, which also has the tools to test your card and debug any issues.

Note: Card instances and their data, which is what you see on the Play Page, will only last 48 hours after being created. Press the play button from the Card Designer to get a new instance of that card. 

## Play page intro

The play page is made up of a few different components:

- Card title
- View mode
- Card viewer
- Customize button
- Debug pane

## Set up debugging

1. Create a card

1. Go to **Variables** and select **New variable**.

   1. In this example, create the following two variables:

      | Variable      | Type   |
      | ------------- | ------ |
      | `title`       | String |
      | `valuesArray` | Array  |

   1. When creating each variable, select the **Advanced settings** drop down in the variable making pane. Under **Input**, select **Required**.

1. Once you've created both variables, save your card.

1. Now that you have variables, add them to your card. In this example, add the following code to:

   1. Title block: `${title}`

   1. Text block: `${valuesArray}`

    :::image type="content" source="../../media/debugging-cards/add-vars-to-card.png" alt-text="Screenshot of variables added to the card for debugging":::

1. Save and play your card.

1. The first time you open the Play page, you’ll be prompted with the Customize Card pane. Enter the values for the required variables you created, then select **Done**.

    :::image type="content" source="../../media/debugging-cards/customize-card-popup.png" alt-text="Screenshot of the customize card popup, allowing values to be added to required variables for debugging." border="false":::

   1. If you need to edit any of these values later, you can do so by selecting **Customize** on the Play Page.

   > [!NOTE]
   > The Customize Card pane will only appear on first viewing of the card after you’ve set up the variables. On subsequent views of the Play Page, you’ll only be prompted with this pane if you add a new required variable to the card.

1. The values you provided will now show up on your card.

    :::image type="content" source="../../media/debugging-cards/added-vars-shown.png" alt-text="Screenshot of added required variable values in card play page":::

## Debugging pane


