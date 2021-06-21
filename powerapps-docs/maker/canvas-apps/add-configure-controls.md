---
title: Add and configure controls in canvas apps
description: Step-by-step instructions for adding and configuring canvas-app controls directly, from the toolbar, in the Properties tab, or in the formula bar.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 01/25/2019
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Add and configure controls in canvas apps

Add a variety of UI elements to your canvas app, and configure aspects of their appearance and behavior directly, from the toolbar, in the **Properties** tab, or in the formula bar. These UI elements are called controls, and the aspects that you configure are called properties.

## Prerequisites

1. If you don't already have a Power Apps license, [sign up](../signup-for-powerapps.md), and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Under **Make your own app**, hover over **Canvas app from blank**, and then select **Make this app**.
1. If you're prompted to take the intro tour, select **Next** to get familiar with key areas of the Power Apps interface (or select **Skip**).

    You can always take the tour later by selecting the question-mark icon near the upper-right corner of your screen and then selecting **Take the intro tour**.

## Add and select a control

On the **Insert** tab, perform either of these steps:

- Select **Label** or **Button** to add one of those types of controls.
- Select a category of controls, and then select the type of control that you want to add.

For example, select **New screen**, and then select **Blank** to add a blank screen to your app. (Screens are a type of control that can contain other types of controls.)

![Add screen](./media/add-configure-controls/add-screen.png)

The new screen is named **Screen2** and appears in the left navigation pane. This pane shows a hierarchical list of controls in your app so that you can easily find and select each control.

![Screen2 in list](./media/add-configure-controls/list-screen2.png)

To demonstrate how this list works, select **Label** on the **Insert** tab. The new control appears under **Screen2** in the hierarchical list.

![Insert label](./media/add-configure-controls/add-label.png)

In the screen, a box with six handles surrounds the label by default. That type of box surrounds whichever control is selected. If you select the screen by clicking or tapping in it (but outside the label), the box disappears from the label. To select the label again, you can click or tap in it, or you can click or tap its name in the hierarchical list of controls.

> [!IMPORTANT]
> You must always select a control before you can configure it.

## Rename a control

In the hierarchical list of controls, hover over the control that you want to rename, select the ellipsis button that appears, and then select **Rename**. You can then type a unique, memorable name to make building your app easier.

![Rename control](./media/add-configure-controls/rename-control.png)

## Delete a control

In the hierarchical list of controls, hover over the control that you want to delete, select the ellipsis button that appears, and then select **Delete**. To delete a control that isn't a screen, you can also select the control on the canvas, and then press the Delete key.

![Delete control](./media/add-configure-controls/delete-control.png)

## Reorder screens

In the hierarchical list of controls, hover over a screen that you want to move up or down, select the ellipsis button that appears, and then select **Move up** or **Move down**.

![Reorder screen](./media/add-configure-controls/reorder-screen.png)

> [!NOTE]
> When the app is opened, the screen at the top of the hierarchical list of controls usually appears first. But you can specify a different screen by setting the **[OnStart](controls/control-screen.md)** property to a formula that includes the **[Navigate](functions/function-navigate.md)** function.

## Move and resize a control

To move a control, select it, hover over its center so that the four-headed arrow appears, and then drag the control to a different location.

![Move control](./media/add-configure-controls/move-control.png)

To resize a control, select it, hover over any handle in the selection box so that the two-headed arrow appears, and then drag the handle.

![Drag control](./media/add-configure-controls/resize-control.png)

> [!NOTE]
> As this topic describes later, you can also move and resize a control by modifying any combination of its **[X](controls/properties-size-location.md)**, **[Y](controls/properties-size-location.md)**, **[Height](controls/properties-size-location.md)**, and **[Width](controls/properties-size-location.md)** properties in the formula bar.

## Change the text of a label or a button

Select a label or button, double-click the text that appears in the control, and then type the text that you want.

![Change text](./media/add-configure-controls/change-text.png)

> [!NOTE]
> As this topic describes later, you can also change this text by modifying its **[Text](controls/properties-core.md)** property in the formula bar.

## Configure a control from the toolbar

By configuring a control from the toolbar, you can specify a wider variety of options than you can by configuring a control directly.

For example, you can select a label, select the **Home** tab, and then change the font of the text in the label.

![Change font](./media/add-configure-controls/change-font.png)

## Configure a control from the Properties tab

By using the **Properties** tab, you can specify a wider variety of options than you can by configuring a control from the toolbar.

For example, you can select a control and then show or hide it by changing its **Visible** property.

![Set visibility](./media/add-configure-controls/set-visibility.png)

## Configure a control in the formula bar

Instead of configuring a control directly, from the toolbar, or in the **Properties** tab, you can configure a control by selecting a property in the property list and then specifying a value in the formula bar. By taking this approach, you can search for a property alphabetically, and you can specify more types of values.

For example, you can select a label and then configure it in these ways:

- Move it by selecting **X** or **Y** in the properties list and then specifying a different number in the formula bar.

    ![Set X property](./media/add-configure-controls/x-property.png)

- Resize it by selecting **Height** or **Width** in the properties list and then specifying a different number in the formula bar.

    ![Set Height property](./media/add-configure-controls/height-property.png)

- Change its text by selecting **Text** in the properties list and then specifying any combination of a literal string, an expression, or a formula in the formula bar.

    - A literal string is surrounded by quotation marks and appears exactly as you type it. **"Hello, world"** is a literal string.

        ![Set Text property to a literal string](./media/add-configure-controls/literal-string.png)

    - An expression doesn't include a function and is often based on a property of another control. **Screen1.Height** is an expression that shows the height of **Screen1**.

        ![Set Text property to an expression](./media/add-configure-controls/expression.png)

    - A formula includes one or more functions. The **Now** function returns the current date and time in your local time zone, and the **Text** function formats values such as dates, times, and currency.

        ![Set Text property to a formula](./media/add-configure-controls/formula.png)

        Formulas are usually much more complex than this example so that they can update data, sort it, filter it, and perform other operations. For more information, see the [formula reference](formula-reference.md).

## Next steps

- Find step-by-step procedures for configuring common controls such as [screens](add-screen-context-variables.md), [lists](add-list-box-drop-down-list-radio-button.md), [galleries](add-gallery.md), [forms](add-form.md), and [charts](use-line-pie-bar-chart.md).
- Find reference information about each type of control in the [control reference](reference-properties.md).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]