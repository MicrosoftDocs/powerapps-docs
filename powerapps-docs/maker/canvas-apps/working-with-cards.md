---
title: "Understand data cards in Power Apps canvas apps"
description: Learn how to use data cards in Power Apps canvas app forms to collect and display information. Customize card types, unlock cards for advanced layouts, and understand data flow between forms and data sources.
author: gregli-msft

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 03/25/2026
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
contributors:
  - mduelae
  - gregli-msft
---
# Understand data cards in canvas apps

This article explains what a data card is, how to change the control users enter data into, when to unlock a card, and how the form saves changes back to Dataverse.

Data cards are the building blocks of Power Apps forms. Each data card displays and collects a value for a single field such as Name, Job Title, or Phone Number. 

The following screenshot shows a form with a data card  for **Account name** selected.

:::image type="content" source="media/working-with-cards/form-with-data-card-selected.png" alt-text="Screenshot show a form with the data card selected":::

 A **Display form** shows one record. **Edit forms** let users update an existing record or create a new one. In either type of form, each data card is connected to exactly one field (one column) in your data source—often a Dataverse table.

A data card is a container that includes the field label, required validation behavior, and the control that users interact with. A data card contains the following:

- **Required indicator (asterisk or star)**: Shows that the field must have a value.
- **Title**: The label shown to users for the field.
- **Data card value**: The input control (for example, a text box or dropdown) where users enter or edit the value
- **Error message**: Displays validation errors, usually after the form is submitted.

## Prerequisites

If you're new to forms, start by reading [add-form.md](add-form.md) and [working-with-forms.md](working-with-forms.md).

## Customize a card

A data card contains the controls that users see - usually a label such as the title, an input control like text input or dropdown, and an error message label. To customize how a field looks, select the control *inside* the card for example, the text input and adjust its size, position, or properties.

### Reorder fields on a form

Power Apps offers predefined cards for strings, numbers, and other data types. You edit the form and rearrange fields letting you change the layout without unlocking any cards.

1. Open your app for editing in [Power Apps Studio](power-apps-studio.md).
1. Select the form then select **Fields**.
1. Select **More actions** and then selet **Move up** or **Move down**. You can also select and then drag fields into the order you want. 

    :::image type="content" source="media/working-with-cards/reorder-fields-on-form.png" alt-text="Screenshot of how to reoder fields on a form ":::

### Change a card’s control type

You can easly change a card's control type. For exmaple you might want to change a single-line text card  to a multiline text card so users have more space to enter information.

1. Open your app for editing in [Power Apps Studio](power-apps-studio.md).
1. Select the form then select **Fields**.
1. Select **Expand field details** which is the down arrow next to the field that you want to edit.
1. Select the dropdown for **Control type** and then select a different control type. For example, switch from **Edit text** to **Edit multi-line text**.

    :::image type="content" source="media/working-with-cards/edit-control-type.png" alt-text="Screenshot show how to edit a cards's control type":::


### Resize a card

You can move and resize controls in a locked card.

You editing the controls inside a card without changing what field the card connects to.

1. In the form, select the data card that you want to resize such as **Account Name**.
1. Drag to move the text input within the card, and use the handles to resize it. This improves spacing and readability without unlocking the card.

    :::image type="content" source="media/working-with-cards/resize-field.png" alt-text="Screenshot of how to select a card and resize a field in the card":::


## Unlock a card

To make changes like deleting a control or adding a new control requires unlocking the card.

When you add a field to a form, Power Apps creates a data card for you and sets up the basic formulas that connect the card to the data source. By default, Power Apps locks these cards so you don't accidentally break that connection. If you need more control, such as a custom layout, extra controls, or different formulas, you can unlock the card.

The following screenshot shows a form with a data card that is locked.

:::image type="content" source="./media/working-with-cards/advanced-locked.png" alt-text="Screenshot of the Advanced tab showing a locked data card in Power Apps.":::

The key setting is [DataField](controls/control-card.md). It tells Power Apps which field (column) this card is responsible for. When the form submits, Power Apps uses the card's **DataField** value to know what field to update.

1. To unlock a card, select the card
1. In the **Properties** pane, select the **Advanced**.
1. Select lock icon or select **Unlock to change properties** to unlock properties such as  **DataField**, **DisplayName**, or **Required**. 
1. After you unlock the card, edit the generated formulas and add or remove controls inside the card.


    |Locked properties  |Unlocked properties  |
    |-------------------|---------------------|
    |:::image type="content" source="media/working-with-cards/locked-properties.png" alt-text="Screenshot of locked properties on a data card":::               |  :::image type="content" source="media/working-with-cards/unlocked-properties.png" alt-text="Screenshot of unlocked properties on a data card":::                   |


You now take control over this card and can modify it further to fit your needs. But you lose the ability to change the card from one representation to another (for example, single-line text to multi-line text) as you did before. You transformed the predefined card into a "custom card" that you now control.

> [!IMPORTANT]
> You can't relock a card after you unlock it. To get a card back to a locked state, remove it, and reinsert it in the right-hand pane.


## Interact with a form

After you unlock a card, you can control how values move between the form and the controls inside the card.

A helpful way to think about an Edit form is: **data flows in** to show the current record (defaults), and **data flows out** when you submit the form updates. The card sits in the middle - its properties tell the form which field it represents and what value should be saved.

### DataField property

The card's **DataField** property is the "this card edits this field" setting. It helps Power Apps decide what to validate, what value is required, and what field should be updated when you submit the form.

### Information flowing in

When a form shows a record, it exposes that record as **ThisItem**. Think of **ThisItem** as the current row you're editing. It contains every field for that record.

In Dataverse-backed forms, the card's **DataField** typically matches the field's logical name. The card's **Default** formula commonly references the current record, for example, **ThisItem.FieldName**, and the input control inside the card usually reads that value through **Parent.Default**. This pattern keeps the input control independent of the data source and lets the card encapsulate how the field value flows in.

Most cards set their **Default** property to the current record's value, like **ThisItem.FieldName**. You can optionally transform that value, for example, format text before it shows in the input.

Inside the card, the input control usually uses **Parent.Default** so it always shows whatever value the card provides. This approach keeps the card "self-contained". If you later change the card's default formula, you don't have to rewrite formulas inside the card.

By default, the data source's metadata sets the **DefaultValue** and **controls/control-card.md** properties based on the **controls/control-card.md** property. You can override these formulas with your own logic by using the **functions/function-datasourceinfo.md** function to integrate the data source's metadata.

### Information flowing out

When the user selects **Save**, this typically call **SubmitForm**. The form gathers values from each data card and writes them back to the data source. It uses each card’s **DataField** to know *which* field to update.

To save changes from an **Edit form**, trigger **SubmitForm(FormName)** (for example, from a **Save** button). If you want to clear the inputs after a successful submit, follow with **ResetForm(FormName)**. To create a new record instead of editing an existing one, set the form’s **DefaultMode** property to **FormMode.New** before the user starts entering data.

The form also reads each card’s **Update** property - this is the value that gets saved for that field. If you need to clean up a value before saving, such as removing extra spaces, converting text to a number, or reversing a formatting change you made in **Default**, **Update** is usually the right place to do it.

**Valid** is basically "is this field okay to submit?" Power Apps uses the data source rules and the card’s **Required** setting to decide this. If the value isn't valid, the card's **Error** property contains a message that you can show to the user, often through the **Error Message** label in the card.

If a card’s **DataField** is blank, the card isn't tied to any field - it's just a container you can use for layout. In that case, its **Update** and **Valid** values don't affect what gets saved when you submit the form.

## Dissecting an example

Take a closer look at what's inside a typical data-entry card. The following screenshots spread the controls out so you can see each piece clearly.

:::image type="content" source="./media/working-with-cards/dissect-card1.png" alt-text="Screenshot of a data-entry card in Power Apps with controls spread out for clarity.":::

In the next image, the controls inside the card are labeled so you can match what you see on the canvas to what’s in the tree view.

:::image type="content" source="./media/working-with-cards/dissect-card2.png" alt-text="Screenshot of labeled controls inside a data card in Power Apps.":::

Here are the main controls you usually see inside a card:

| Name | Type | What it does |
|---|---|---|
| **TextRequiredStar** | **Label** control | Shows a star or asterisk when the field is required. |
| **TextFieldDisplayName** | **Label** control | Shows the friendly field name the user sees. This name often differs from the internal schema name. |
| **InputText** | Text input control | Shows the current value and lets the user type a new one. |
| **TextErrorMessage** | **Label** control | Shows a message if the value can't be submitted, such as missing required data. |

These controls usually don't connect to Dataverse directly. Instead, they read simple values from the **parent card** by using **Parent**, and the card handles the connection to the data source. The following formulas are common examples.

| Control property | Formula | Beginner explanation |
|---|---|---|
| **TextRequiredStar.Visible** | **Parent.Required** | Only show the star when the field is required. |





[!INCLUDE[footer-include](../../includes/footer-banner.md)]
