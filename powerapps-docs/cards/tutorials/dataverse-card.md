---
title: Create a card with data from Dataverse (Preview)
description: Learn how to use Dataverse connectors in a Microsoft Power Apps card.
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

# Create a card with data from Dataverse (Preview)

In this tutorial, you'll create a card that uses the Microsoft Dataverse connector to display and update information about an account. You'll use the [card designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), [connectors](../make-a-card/connectors/connector-intro.md), and more complex [Power Fx expressions](../make-a-card/power-fx/intro-to-pfx.md).

At the end of the tutorial, your card should look like the following example:

:::image type="content" source="../media/tutorial-use-connectors/use-connectors-card.png" alt-text="Screenshot of a finished card using the Bing search connector.":::

We'll assume that you've honed your Power Apps card skills in the [Hello World tutorial](hello-world-card.md) and the [shopping list tutorial](simple-shopping-list.md) and are familiar with using the card designer. If you haven't explored those tutorials yet, now is a good time to do that.

## Create a card

1. Go to [Power Apps](https://make.powerapps.com) and select **Cards (preview)** on the left.

1. Select **+ Create a card**.

1. Enter "DataverseCard" under **Card name** and then select **Create**.

### Add the Dataverse connector to the Accounts table

1. Go to the Data pane on the left-hand menu and select **Add data**

1. Select the **Microsoft Dataverse** connector, wait for it to configure the connection, press **OK** then select the **Accounts** table and press **Select**

### Ask for the account name

1. Navigate to the Insert pane in the left-hand menu and add a Text label control, setting the **Text** to `Enter account name`

1. Add a Text input control

1. Add a button and set the Title to `See details`

1. Navigate to the Variables pane and select **New variable**

1. Set the variable name to `enteredAccountName`, the type to `Text`, and select **Save**

1. Navigate to the Tree View pane in the left-hand menu and select **New screen**

1. Set the name to `DetailsScreen` and select **Create**

1. Select the button and set the **OnSelect** property to `Set(enteredAccountName, textInput1); Navigate(DetailsScreen);` 

### Show additional account details

1. In the DetailsScreen, set the Text property on the bolded text label that is added by default to `LookUp(account, 'Account Name' = enteredAccountName).'Account Name'`

1. Through the Insert pane, add a text label and set the **Text** property to `LookUp(account, 'Account Name' = enteredAccountName).'Account Number'`

1. Through the Insert pane, add a button and set the **Text** property to `"Search for a different account"` and the **OnSelect** property to `Back()`

### Change the account description

1. Navigate to the Insert pane in the left-hand menu and add a Text input control and button to your DetailsScreen

1. Set the button text to `"Update description"` and the **OnSelect** property to `Patch(account, LookUp(account, 'Account Name' = enteredAccountName), { Description: textInput2 })`

### List all accounts

1. On the main screen, add a text label

1. On the text label, set the **Text** property to `ThisItem.'Account Name'` and set the **Repeat for every** property on the Advanced tab to `account`

## Test the card

1. **Save** the card by selecting the button on the top right. You should always save changes before playing an updated card. Then select **Play**.

The card will have two screens - the first screen lists all accounts and allows the user to type in the exact name of an account to see additional details, the second screen shows the account name and number as well as lets the user modify the description.
