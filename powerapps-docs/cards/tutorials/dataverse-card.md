---
title: Create a card with data from Dataverse
description: Learn how to use Dataverse connectors in a card.
keywords: "Card Designer, Power Apps, cards, tutorial, Dataverse, connectors"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Create a card with data from Dataverse (preview)

In this tutorial, you'll create a card that uses the Microsoft Dataverse connector to display and update information about an account. You'll use the [card designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), [connectors](../make-a-card/connectors/connector-intro.md), and more complex [Power Fx expressions](../make-a-card/power-fx/intro-to-pfx.md).

We'll assume that you've honed your Power Apps card skills in the [Hello World tutorial](hello-world-card.md) and the [shopping list tutorial](simple-shopping-list.md) and are familiar with using the card designer. If you haven't explored those tutorials yet, we recommend that you do that first, and then return to this tutorial.

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../tutorials/hello-world-card.md)

## Create a card

1. Sign in to [Power Apps](https://make.powerapps.com) and select **Cards**. If the **Cards** tab is not visible, select **More** and pin the **Cards** tab.

1. Name the card *DataverseCard* and then select **Create**.

## Connect the card to the Dataverse account table

1. Select **Data** > **+ Add data**.

1. Search for **Dataverse** and then select the **Microsoft Dataverse** connector.

1. Select the **account** table, and then select **Select**.

    :::image type="content" source="..\media\tutorial-dataverse-card\dataverse-connector-added.png" alt-text="Screenshot of the Dataverse account table connector added to a card in the card designer.":::

## Ask for the account name

1. Insert a text label control and set its **Text** property to *Enter account name*.

1. Insert a text input control and set its **Name** property to *AccountName*.

1. Insert a button and set its **Title** property to *View details*.

1. Select **Variables** > **+ New variable**.

1. Set **Name** to *EnteredAccountName*. Leave all other values as they are. Select **Save**.

1. Open the Tree View and select **+ New screen**.

1. Name the screen *DetailsScreen* and then select **Create**.

1. In the Tree View, select the **main** screen.

1. Select the button and set its **OnSelect** property to *Set(EnteredAccountName, AccountName); Navigate(DetailsScreen);*

    This expression has two parts, separated by a semicolon (;). The first part assigns the value of the user's input, `AccountName`, to the `EnteredAccountName` variable. The second part opens the screen named `DetailsScreen`. Since the expression is bound to the button's **OnSelect** property, it runs when the user selects the button.

    :::image type="content" source="..\media\tutorial-dataverse-card\button-pfx.png" alt-text="Screenshot of a card with a Run Power Fx button in the card designer.":::

## Show account details

1. In the Tree View, select the **DetailsScreen** screen.

1. Select the card title and set its **Text** property to *LookUp(account, 'Account Name' = EnteredAccountName).'Account Name'*.

    This expression changes the card title to a string incorporating the account name. You can enter the expression in the formula bar or the properties pane.

    :::image type="content" source="..\media\tutorial-dataverse-card\details-title-pfx.png" alt-text="Screenshot of the Detailsscreen title set to a Power Fx expression.":::

1. Select the second text label and set its **Text** property to *LookUp(account, 'Account Name' = EnteredAccountName).'Account Number'*.

1. Insert a button. Set its **Title** property to *Search for a different account* and its **OnSelect** property to *Back()*.

    :::image type="content" source="..\media\tutorial-dataverse-card\details-filled.png" alt-text="Screenshot of a card with two text labels and a Run Power Fx button in the card designer.":::

### Change the account description

1. Insert a text input control and set its **Name** property to *NewName*.

1. Insert a button. Set its **Title** property to *Update name* and its **OnSelect** property to *Patch(account, LookUp(account, 'Account Name' = EnteredAccountName), { Description: NewName })*.

    :::image type="content" source="..\media\tutorial-dataverse-card\details-update-button.png" alt-text="Screenshot of the properties of a second Run Power Fx button in the card designer.":::

### List all accounts

1. In the Tree View, select the **main** screen.

1. Insert a text label. Set its **Text** property to *ThisItem.'Account Name'* and set its **Repeat for every** advanced property to *account*.

## Test the card

You should permanently save your changes before you play a card. Select **Save**, and then select **Play**.

Test all the controls on both screens on your card. The first screen should list all the accounts and allow you to type the name of an account to open a screen with more details. The second screen should show the account name and number and enable you to change the account name.
