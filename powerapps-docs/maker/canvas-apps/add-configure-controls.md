---
title: Add and configure controls in canvas apps
description: Step-by-step instructions for adding and configuring canvas-app controls directly, from the toolbar, in the Properties tab, or in the formula bar.
author: mduelae

ms.topic: how-to
ms.reviewer: 
ms.date: 10/29/2024
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
  - chmoncay
ms.custom: canvas
ms.collection: get-started
---
# Add and configure controls in canvas apps

Add a variety of UI elements to your canvas app, and configure aspects of their appearance and behavior directly, from the toolbar, in the **Properties** tab, or in the formula bar. These UI elements are called controls, and the aspects that you configure are called properties.

## Prerequisites

1. If you don't already have a Power Apps license, [sign up](../signup-for-powerapps.md), and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Create a [blank canvas app](create-blank-app.md).

    You can always take the tour later by selecting the question-mark icon near the upper-right corner of your screen and then selecting **Take the intro tour**.

## Add and select a control

Let's add a new screen and a button control. However, you can add any type of control.

1. Select **Insert** from the [authoring menu](power-apps-studio.md#5--app-authoring-menu), then select **New screen**.
1. Choose **Blank** to add a blank screen to your app. (Screens are a type of control that can contain other types of controls.)

   :::image type="content" source="./media/add-configure-controls/add-screen.png" alt-text="Screenshot that shows how to add a new screen from the Insert menu option.":::

   The new screen is named **Screen2** and appears in the **Tree view**. This pane shows a hierarchical list of controls in your app so that you can easily find and select each control.

   :::image type="content" source="./media/add-configure-controls/list-screen2.png" alt-text="Screenshot that shows the new screen added in the Tree view of your app.":::

1. With **Screen2** selected, select **Insert** again.
1. Select the **Button** control. The new control appears under **Screen2** in the hierarchical list of **Tree view**.

   :::image type="content" source="./media/add-configure-controls/add-button.png" alt-text="Screenshot that shows the new button on the canvas and the button control name in the list under Screen2.":::

   In the screen, a box with six handles surrounds the button by default. These handles surround any control selected and are used to size the control.

1. Select the screen (outside the button) and the box handles disappear. To select the control again, select it directly on the canvas or from the **Tree view** list.

   > [!IMPORTANT]
   > You must always select a control before you can configure it.

## Rename a control

1. In the list of controls, hover over the control that you want to rename to reveal the overflow menu (ellipsis).
1. Select the ellipses.
1. Select **Rename**. Add a unique, memorable name to make building your app easier.

   :::image type="content" source="./media/add-configure-controls/rename-control.png" alt-text="Screenshot that shows where to rename a control through the overflow menu.":::

## Delete a control

You can delete a control either through control in the **Tree view** list or directly from the canvas.

### Delete a control from Tree view

1. In the list of controls, hover over the control that you want to delete to reveal the overflow menu (ellipsis).
1. Select the ellipses.
1. Select **Delete**.

### Delete a control from the canvas

Select the control on the canvas, then press the `Delete` key.

## Reorder screens

1. In **Tree view**, hover over a screen that you want to move up or down to reveal the overflow menu (ellipses).
1. Select the ellipsis, then choose **Move up** or **Move down**. If you don't see a **Move down** option, your screen is at the lowest point in the list already.

   :::image type="content" source="./media/add-configure-controls/reorder-screen.png" alt-text="Screenshot that shows you how to reorder your screens in the Tree view through the overflow menu of a screen.":::

> [!NOTE]
> When the app is opened, the screen at the top of the list of controls usually appears first. However, you can specify a different screen by setting the **[OnStart](controls/control-screen.md)** property to a formula that includes the **[Navigate](functions/function-navigate.md)** function.

## Move and resize a control

To move a control, select it, hover over its center so that the four-headed arrow appears, and then drag the control to a different location.

![Move control.](./media/add-configure-controls/move-control.png)

To resize a control, select it, hover over any handle in the selection box so that the two-headed arrow appears, and then drag the handle.

![Drag control.](./media/add-configure-controls/resize-control.png)

> [!NOTE]
> As this topic describes later, you can also move and resize a control by modifying any combination of its **[X](controls/properties-size-location.md)**, **[Y](controls/properties-size-location.md)**, **[Height](controls/properties-size-location.md)**, and **[Width](controls/properties-size-location.md)** properties in the formula bar.

## Configure a control in the Properties pane

By using the **Properties** pane, specific to the control you select, you can specify a wide variety of options.

For example, if you select a button control, you can replace the value of the text displayed through the control's **Properties** pane.

:::image type="content" source="./media/add-configure-controls/change-text.png" alt-text="Screenshot that shows how to change the display text on a button control through the Properties pane.":::

> [!NOTE]
> You can alternatively change display text by modifying its [Text](controls/properties-core.md) property in the formula bar.

## Configure a control in the formula bar

You can configure a control by selecting a property in the property list and then specifying a value in the formula bar. Autocomplete can be helpful in the formula bar to see values you can use for a control.

### Change the font color of a control

For example, if you want to change the font color for your control's text. You see many color options.

:::image type="content" source="./media/add-configure-controls/formula-bar-options.png" alt-text="Screenshot that shows the control options you can set in the formula bar for a control.":::

### Change the position on the canvas of a control

You can set the X and Y coordinates for the position of the control using the formula bar. Setting coordinates in the formula bar gives you greater precision of control placement.

For example, if you select **X** or **Y** in the properties list and specify a number in the formula bar, you see the control move to that coordinate. In this case, the button moves to position 100 on the X axis, assuming the far left side of the canvas is the zero point.

:::image type="content" source="./media/add-configure-controls/x-property.png" alt-text="Screenshot that shows where to set the X coordinate in the formula bar.":::

### Change the control's size

You can resize a control by selecting **Height** or **Width** in the properties list and then specifying a different number in the formula bar.

:::image type="content" source="./media/add-configure-controls/change-height.png" alt-text="Screenshot that shows how to change the height of a control through the formula bar.":::

### Change the control's display text

You can change a control's display text by selecting **Text** in the properties list and then specifying any combination of a literal string, an expression, or a formula in the formula bar.

#### Literal string

A literal string is surrounded by quotation marks and appears exactly as you type it. **"Hello, world"** is a literal string.

:::image type="content" source="./media/add-configure-controls/literal-string.png" alt-text="Screenshot that shows where to add a literal string in the formula bar for a control's display text.":::

> [!NOTE]
> When you add text that is longer than the width of your control, the control doesn't change its width to accomodate the text. You must manually change the control's size to fit the text.

#### Expression

An expression is often based on a property of another control. **Screen2.Height** is an expression that shows the height of **Screen2** where the display text is shown for a button control.

:::image type="content" source="./media/add-configure-controls/expression.png" alt-text="Screenshot showing how to add a control property as display text for another control.":::

Using an expression, for example, you can set a background image or icon as the fill for your button.

#### Formula

A formula includes one or more functions. The **Now** function returns the current date and time in your local time zone, and the **Text** function formats values such as dates, times, and currency.

For example, you can display the date and time in a **Label**:

:::image type="content" source="./media/add-configure-controls/formula.png" alt-text="Screenshot that shows how to create a Text() function that displays a shortened version of DateTime." lightbox="./media/add-configure-controls/formula.png":::

Formulas are usually much more complex than this example so that they can update data, sort it, filter it, and perform other operations. For more information, see the [formula reference](/power-platform/power-fx/formula-reference-canvas-apps).

## Related information

- Find step-by-step procedures for configuring common controls such as [screens](add-screen-context-variables.md), [lists](add-list-box-drop-down-list-radio-button.md), [galleries](add-gallery.md), [forms](add-form.md), and [charts](use-line-pie-bar-chart.md).
- Find reference information about each type of control in the [control reference](reference-properties.md).

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
