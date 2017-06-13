<properties
	pageTitle="Understand data cards | Microsoft PowerApps"
	description="Use form cards to collect and display information from a data source."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/26/2016"
   ms.author="gregli"/>

# Understand data cards #
**[Card](controls/control-card.md)** controls are the building blocks of the **[Edit form](controls/control-form-detail.md)** and **[Display form](controls/control-form-detail.md)** controls. The form represents the entire record, and each card represents a single field of that record.

The easiest way to interact with cards is through the right-hand pane when a form control has been selected in the design workspace. In that pane, you can choose which fields to show, pick how each field should be shown, and rearrange the fields.

![](./media/working-with-cards/first-screen.png)

To get started with cards, see [add a form](add-form.md) and [understand data forms](working-with-forms.md). The remainder of this topic goes into more detail about how cards work and how you can customize or even create your own.

## Predefined cards ##
PowerApps offers a predefined set of cards for strings, numbers, and other data types. In the right-hand pane, you can see the variations available and change the card used for a field:

![](./media/working-with-cards/second-screenshot.png)

In this example, a single-line text card is selected, but the URL's text is longer than can be shown on a single line. Let's change this to a multi-line text card to give our users more room to edit:

![](./media/working-with-cards/third-screen.png)

You'll also notice that several fields of this data source aren't being shown. Show and hide a field by selecting its checkbox:

![](./media/working-with-cards/add-field.png)

## Customize a card ##
Cards comprise other controls. The user enters data in a standard **[Text input](controls/control-text-input.md)** control that you add from the **Insert** tab.  

Let's walk through some examples of changing the card's appearance by manipulating controls.

1. First, let's return to the card that we inserted most recently, for the **SecurityCode** field. Select this card by clicking or tapping it once:

	![](./media/working-with-cards/customize-textbox0.png)

2. Select the **[Text input](controls/control-text-input.md)** control inside the card by clicking or tapping the input control itself.

	![](./media/working-with-cards/customize-textbox1.png)

3. Move this control within the card by dragging the selection box, and resize the control by dragging the handles along the edge of the selection box:

	![](./media/working-with-cards/customize-textbox2.png)  

	You can resize, move, and make other modifications to the control, but you can't delete it without unlocking it first. The next section describes how to unlock a card.

4. Insert one or more controls into the card, such as this star shape from the **Shapes** menu on the **Insert** tab:

	![](./media/working-with-cards/customize-textbox3.png)

	This new control is now a part of the card and will travel with the card if, for example, you reorder the cards within the form.

	As another example, show an image in an **[Image](controls/control-image.md)** control instead of the image's URL in a **Text input** control, as this graphic shows

	![](./media/working-with-cards/customize-image1.png)

2. On the **Insert** tab, add an image control under the **ImageURL** card:

	![](./media/working-with-cards/customize-image2.png)

3. In the formula bar, set the **[Image](controls/properties-visual.md)** property of this control to *TextBox*.**Text**, where *TextBox* is the name of the **Input text** control that holds the URL:

	**Tip**: Press the Alt key to show the name of each control.

	![](./media/working-with-cards/customize-image3.png)

	And now we can see the images and edit their URLs. Note that we could have used **Parent.Default** as the **[Image](controls/properties-visual.md)** property, but it wouldn't have updated as the user entered a new URL.

4. We can do the same thing on the second screen of this app, where we use a **[Display form](controls/control-form-detail.md)** control to display the details of a record.  Here we may want to hide the label (set the **[Visible](controls/properties-core.md)** property of the text-box control, not the card, to *false*) because the user won't edit the URL on that screen:

	![](./media/working-with-cards/customize-image4.png)

## Unlock a card ##
In addition to containing controls, cards themselves are controls that have properties and formulas just like any other control. When you choose to display a field on a form, the right-hand pane automatically creates the card for you and generates the needed formulas.  We can see these formulas in the **Advanced** pane, available from the **View** tab:

![](./media/working-with-cards/locked-advanced-view.png)

We immediately see one of the most important properties of the card: the **[DataField](controls/control-card.md)** property. This property indicates which field of the data source the user sees and can edit in this card.  

In the **Advanced** view, the large banner at the top indicates that the properties of this card are locked. A lock icon also appears next to the **[DataField](controls/control-card.md)**, **[Default](controls/properties-core.md)**, and **[DisplayName](controls/control-card.md)** properties. The right-hand pane created these formulas, and the lock prevents accidental changes to these properties.  

Click or tap the banner at the top to unlock the card so that you can modify these properties:

![](./media/working-with-cards/unlocked-advanced-view.png)

Let's modify the **[DisplayName](controls/control-card.md)** to put a space between **Asset** and **ID**. By making this change, we're altering what was generated for us.  In the right-hand pane, this card has a different label:

![](./media/working-with-cards/custom-card-new.png)

We've now taken control over this card and can modify it further to fit our need. But we've lost the ability to change the card from one representation to another (for example, single-line text to multi-line text) as we did before. We've transformed the predefined card into a "custom card" that we now control.  

A word of caution: you can't relock a card if you unlock it. To get back to a locked state, remove the card, and reinsert it in the right-hand pane.   

## Interact with the form ##

After you unlock the card, you can change how it interacts with the form that contains it.

Below are some guidelines for how controls should work with their card and how the cards should work with the form. These are only guidelines. As with any control in PowerApps, you can create formulas that reference any other control in PowerApps, and that's no less true for cards and controls within cards. Be creative: you can create an app in many ways.  

### DataField property ###
The most important property on the card is the **[DataField](controls/control-card.md)** property.  This property drives validation, what field is updated, and other aspects of the card.

### Information flowing in ###
As a container, the form makes **ThisItem** available to all cards within it. This record contains all of the fields for the current record of interest.  

The **[Default](controls/properties-core.md)** property of every card should be set to **ThisItem**.*FieldName*.  Under certain circumstances, you might want to transform this value on the way in. For example, you might want to format a string or translate the value from one language to another.

Each control within the card should reference **Parent.Default** to get at the field's value. This strategy provides a level of encapsulation for the card so that the card's **[Default](controls/properties-core.md)** property can change without changing the internal formulas of the card.

By default, **DefaultValue** and **[Required](controls/control-card.md)** properties are taken from the data source's metadata based on the **[DataField](controls/control-card.md)** property. You can override these formulas with your own logic, integrating the data source's metadata by using the **[DataSourceInfo](functions/function-datasourceinfo.md)** function.

### Information flowing out ###
After the user modifies a record by using controls in the cards, the **[SubmitForm](functions/function-form.md)** function saves those changes to the data source. When that function runs, the form control reads the values of each card's **[DataField](controls/control-card.md)** property to know what field to change.  

The form control also reads the value of each card's **[Update](controls/control-card.md)** property. This value will be stored in the data source for this field. This is the place to apply another transform, perhaps to reverse the transform that was applied in the card's **[Default](controls/properties-core.md)** formula.

The **Valid** property is driven from the metadata of the data source, based on the **[DataField](controls/control-card.md)** property. It's also based on the **[Required](controls/control-card.md)** property and whether the **[Update](controls/control-card.md)** property contains a value. If the value on the **[Update](controls/control-card.md)** property isn't valid, the **Error** property provides a user-friendly error message.

If the **[DataField](controls/control-card.md)** property of a card is *blank*, the card is just a container of controls. Its **Valid** and **[Update](controls/control-card.md)** properties don't participate when the form is submitted.

## Dissecting an example ##
Let's look at the controls that make up a basic data-entry card. The space between controls has been increased to show each more clearly:

![](./media/working-with-cards/dissect-card1.png)

Hold down the Alt key to show the names of the controls that make up this card:

![](./media/working-with-cards/dissect-card2.png)

Four controls make this card work:

| Name | Type | Description |
|--------------|--------------|-------------|
| **TextRequiredStar** | **[Label](controls/control-text-box.md)** control | Displays a star, which is commonly used on data-entry forms to indicate that a field is required. |
| **TextFieldDisplayName** | **[Label](controls/control-text-box.md)** control | Displays the user-friendly name of this field. This name can differ from what is in the data source's schema. |
| **InputText** | **Input text** control | Displays the initial value of the field and allows the user to change that value. |
| **TextErrorMessage** | **[Label](controls/control-text-box.md)** control | Displays a user-friendly error message to the user if a problem occurs with validation. Also ensures that the field has a value if one is required. |

To populate these controls with data, their properties can be driven from the properties of the card, through these key formulas. Note that none of these formulas refers to a specific field. Instead, all information comes from the card.

| Control property| Formula | Description |
| -------------|---------|-------------|
| **TextRequiredStar.Visible** | **Parent.Required** | The star appears only if the field is required. Required is a formula that's driven by you or the metadata of the data source. |
| **TextFieldDisplayName.Text** | **Parent.DisplayName** | The text-box control shows the user-friendly name, which you or the data source's metadata provides, and which is set on the card's **[DisplayName](controls/control-card.md)** property. |
| **InputText.Default** | **Parent.Default** | The text-input control initially shows the value of the field from the data source, as provided by the card's default value. |
| **TextErrorMessage.Text** | **Parent.Error** | If a validation problem occurs, the card's **Error** property provides an appropriate error message.

To pull information out of these controls and push it back into the data source, we have the following key formulas:

| Control name | Formula | Description |
| -------------|---------|-------------|
| **DataCard.DataField** | **"ApproverEmail"** | The name of the field that the user can display and edit in this card. |  
| **DataCard.Update** | **InputText.Text** | The value to validate and push back into the data source when **[SubmitForm](functions/function-form.md)** runs. |
