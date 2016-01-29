<properties
	pageTitle="Add and configure a control | Microsoft PowerApps"
	description="Step-by-step instructions for adding, moving, resizing, and renaming controls, such as buttons and text boxes."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="AFTOwen"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="01/28/2015"
   ms.author="anneta"/>

# Add and configure a control in PowerApps #

**Prerequisites**
1. Install [PowerApps](http://aka.ms/powerappsinstall) on a tablet, a laptop, or a desktop computer that's running Windows.  
1. Open PowerApps.  
1. Sign in for the first time by selecting the arrow near the lower-right corner to advance through the welcome screens and then providing your credentials.
1. Select **New** on the **File** menu (near the left edge), and then select **Get started** under **Create from scratch**.  

## Add a control ##
On the **Insert** tab, follow either of these steps:

- Select **Text box**, **Button**, or **Image**.
- Select a category, such as **Text** or **Controls**, and then select the control that you want to add.

If you need more space for controls, [add a screen](add-screen-context-variables.md).

## Configure a control directly ##
1. Add a control, such as a text box.

	When you add a control, it's selected by default, which means that you can configure its properties. For example, a selected text box resembles this graphic.

	![A selected text box](./media/add-configure-controls/selected-text-box.png)

	**Important:** If a control is selected and you select another control or a blank area of the screen, the first element is no longer selected.

1. Resize the control by dragging any handle of the selection box (or by modifying the **Height**, **Width**, or both properties, as this topic describes later).

	For example, make the text box shorter by dragging the middle handle on the right edge of the selection box.

	![A resized text box](./media/add-configure-controls/shorter-text-box.png)

1. Move the control by dragging the selection box itself (or by modifying the **X**, **Y**, or both properties, as this topic describes later).

1. If a control such as a text box or a button shows text, modify that text by triple-clicking it and then typing the text that you want (or by setting the **Text** property, as this topic describes later).

	![A text box with custom text](./media/add-configure-controls/change-text-directly.png)

	**Note:** To delete a control, select it, and then press Delete.

## Configure a control from the ribbon ##

1. With the control selected, select **Fill** on the **Home** tab, and then select a color such as aquamarine.

	![A text box with aquamarine fill](./media/add-configure-controls/change-fill.png)

1. On the **Home** tab, change the font family and the size of the text (for example, to 18 pt. Georgia).

	![A text box with 18 pt. Georgia text](./media/add-configure-controls/change-font.png)

1. On the tab for the control you're configuring, select an option that's specific to that control, and modify the value.

	For example, select **VerticalAlign** on the **Text box** tab, and then select **Top**.

	![A text box with text aligned to the top of the box](./media/add-configure-controls/change-align.png)

## Configure a control in the formula bar ##
Each change that you made earlier in this topic updated the value of a property for that control you configured.

- When you resized the control, you changed its **Width** property.
- When you moved the control, you changed its **X** and **Y** properties.
- When you changed the text that the control displays, you changed its **Text** property.

Instead of configuring a control directly or from the ribbon, you can also update the value of a property by selecting it in the property list and then specifying a value in the formula bar. By taking this approach, you can update any property of a control, and you can specify more types of values.

1. With the text box selected, select **Text** in the property list, and then type **"My Company Name"** (including the quotation marks) in the formula bar.

	![A text box with text aligned to the top of the box](./media/add-configure-controls/text-literal.png)

	When you surround a string of text with quotation marks, you specify that it should be treated exactly as you typed it. In contrast, you can specify a formula that determines the value of a property without specifying it exactly.

1. With the text box selected, select **Text** in the property list, and then type **Today()** (without quotation marks) in the formula bar.

	The control shows the current date.

	**Tip:** You can [format dates and times](show-text-dates-times.md) in various ways, in addition to performing calculations on them.

	By using the formula bar, you can set properties that aren't available directly or from the ribbon. For example, you can set a tooltip that appears when a user points to the control but doesn't select it.

	You can also specify complicated formulas to increase the power of your app.

1. Add a checkbox, and set its **Text** property to **Show text**.

1. Set the **Visible** property of the text box to this formula:

	**If(Checkbox1!Value = true, true, false)**

	**Note:** If you add a checkbox, remove it, and then add another checkbox, you might need to rename the checkbox you're using, as this topic describes later, to **Checkbox1** for the formula to work.

1. Press F5, and then select and clear the checkbox multiple times to show or hide the text box.

	[Build a formula](formula-reference.md) to configure the behavior and appearance of your app.

## Rename a control ##
1. Select the control that you want to rename, such as checkbox that you added in the previous procedure.

1. On the **Home** tab, select the name of the control (to the right of **New screen**), and then type the name you want.

	![Rename a checkbox](./media/add-configure-controls/rename-control.png)
