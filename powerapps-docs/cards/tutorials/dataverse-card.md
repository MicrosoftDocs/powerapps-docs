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

# Use the Dataverse connector

In this tutorial, you'll learn how to build a card that utilizes the Dataverse connector to show and update information about an Account.

- Connectors, specifically Dataverse
- More advanced Power Fx expressions

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account.
- Familiarity with the [Card Designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), and [Power Fx](../make-a-card/power-fx/intro-to-pfx.md).

## Tutorial

### Create a card

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