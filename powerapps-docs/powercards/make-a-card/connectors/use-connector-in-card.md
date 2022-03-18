---
title: "Use a connector in a card"
description: "Learn how to add one connector to your card, and walk through an example"
keywords: "Power Cards, Power Cards Designer, Power Apps, Cards, connectors"
ms.date: 03/18/2022
ms.topic: article
author: v-eberhardts
ms.author: v-eberhardts
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Use a connector in a card

In this tutorial, you'll learn how to ask a user for their name and then show that name in the title of a card.

1. Create a card in Power Cards: in your environment, go to Cards in the left pane, select Create, then select Basic card.

1. Name your card something you'll remember; here, we're using "GetPrefilledCard". Once you've named your card, select Create card.

   :::image type="content" source="../../media/use-connector-in-card/name-card-getprefilledcard.png" alt-text="Screenshot of named card." border="false":::

1. Select the card title element and rename it; in this example, rename it to "Your profile".

   :::image type="content" source="../../media/use-connector-in-card/rename-card-title.png" alt-text="Screenshot of retitled card." border="false":::

1. Select the text element under the title and add the following text: `Name: ${userName}`

1. Drag and drop a Text.Input element from Elements underneath the previous step's text box.

1. Select the TextBlock and add the following text: `City: ${userCity}`

   :::image type="content" source="../../media/use-connector-in-card/profile-variables-added.png" alt-text="Screenshot showing textboxes with the name and city variables added to card." border="false":::

1. Go to Variables and select New variable

1. Create the following variables:

   | Name     | Default value |
   |----------|---------------|
   | userName | defaultName   |
   | userCity | defaultCity   |

1. Save each variable after you create it.

   :::image type="content" source="../../media/use-connector-in-card/created-variables-in-list.png" alt-text="Screenshot showing created variables in variable list." border="false":::

1. Go back to Elements and add a Button element onto the card, underneath the City text box.

1. Give the button a new title; here, we use "Get my profile".

   :::image type="content" source="../../media/use-connector-in-card/set-button-title.png" alt-text="Screenshot showing how to update the button title to a descriptive name." border="false":::

1. Go to Data connections and select Add data

   :::image type="content" source="../../media/use-connector-in-card/add-o365-users-connection.png" alt-text="Screenshot showing how to add the O365 Connector to the card." border="false":::

1. Select Office 365 users and wait for the green checkmark to appear. Once it does, select OK.

   :::image type="content" source="../../media/use-connector-in-card/connection-ready-to-add.png" alt-text="Screenshot of O365 connector ready to add to card." border="false":::

1. Select the Get my profile button on the card, and add the following PowerFX to it:

    ```powerfx
    Set(userName, office365Users.MyProfileV2().displayName);  
    Set(userCity, office365Users.MyProfileV2().city);
    ```

   :::image type="content" source="../../media/use-connector-in-card/add-pfx-to-card-button.png" alt-text="Screenshot showing where to add PowerFX expression to card button." border="false":::

1. Save the card and select Play to see your card in action.
