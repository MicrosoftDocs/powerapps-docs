---
title: Get started with formulas in canvas apps
description: Learn about how to use formulas to customize a canvas app.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.custom: 
- "intro-internal"
- "canvas"
ms.topic: conceptual
ms.reviewer: tapanm
ms.date: 03/01/2019
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - gregli-msft
---
# Get started with formulas in canvas apps

> [!NOTE]
> Have you checked out new [Microsoft Power Fx](/power-platform/power-fx/overview)? 

Configure your canvas app with formulas that not only calculate values and perform other tasks (as they do in Excel) but also respond to user input (as an app requires).

* In Excel, you build formulas that, for example, populate cells and create tables and charts.
* In Power Apps, you build similar formulas as you configure controls instead of cells. In addition, you build formulas that apply specifically to apps instead of spreadsheets.

For example, you build a formula to determine how your app responds when users select a button, adjust a slider, or provide other input. These formulas might show a different screen, update a data source that's external to the app, or create a table that contains a subset of the data in an existing table.

You can use formulas for a wide variety of scenarios. For example, you can use your device's GPS, a map control, and a formula that uses **Location.Latitude** and **Location.Longitude** to display your current location. As you move, the map automatically tracks your location.

This topic provides only an overview of working with formulas. Browse the [formula reference](formula-reference.md) for more details and the complete list of functions, operators, and other building blocks you can use.

## Prerequisites

* [Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) by providing the same credentials that you used to sign up.
* Learn how to [configure a control](add-configure-controls.md) in Power Apps.

## Show a simple value

In Excel, you can enter a specific piece of data, such as the number **42** or the phrase **Hello World**, by typing it into a cell. That cell will always show that data exactly as you typed it. In Power Apps, you can similarly specify a piece of data that doesn't change by setting the **[Text](controls/properties-core.md)** property of a label to the exact sequence of characters that you want, surrounded by double quotation marks.

1. Select **New** on the **File** menu (near the left edge of the screen).
2. Under **Create an app**, select **Phone layout** on the **Blank app** tile.

    The formula bar sits at the top of the screen.

    ![Formula bar.](./media/working-with-formulas/formula-bar.png)

    This bar has two parts:

   * *Property list*:  Each control and screen has a [set of properties](reference-properties.md).  Use this list to select a specific property.  
   * *Formula*:  The formula to be calculated for this property, made up of [values, operators, and functions](formula-reference.md).

     In the formula bar, you can see and edit properties for the selected control or for the screen if no controls are selected.  You can see the name of the selected control on the **Content** tab:

     ![Content bar shows the currently selected control.](./media/working-with-formulas/content-tab-selection.png)

     You can change the name of the selected control in the **Content** tab by clicking the name.
3. Add a **[Label](controls/control-text-box.md)** control to the screen.

    ![Added a TextBox control.](./media/working-with-formulas/add-a-label.png)

    When you add a label, the property list automatically shows the **[Text](controls/properties-core.md)** property, which drives what the control shows. By default, the value of this property is **"Text"**.  
4. Set the value of the **[Text](controls/properties-core.md)** property to **"Hello World"** by typing that string, surrounded by double quotes, into the formula bar:

    ![Using the label "Hello World."](./media/working-with-formulas/label-hello-world.png)

    The label reflects this new value as you type it.  The screen may show yellow exclamation-point icons while you type. These icons indicate errors, but they'll go away when you finish entering a valid value. For example, a string without double quotation marks on both ends isn't valid.

    In Excel, you can show a number, such as **42**, by typing it into a cell or by typing a formula that resolves to that number, such as **=SUM(30,12)**. In Power Apps, you can achieve the same effect by setting the **Text** property of a control, such as a label, to **42** or **Sum(30,12)**. The cell and the label will always show that number regardless of what else changes in the worksheet or the app.

    > [!NOTE]
   > In Power Apps, you don't precede a formula with an equals sign or a plus sign as you do in Excel. The formula bar treats anything you type there as a formula by default. You also don't surround a formula with double quotation marks ("), as you did earlier to specify a string of text.
5. In the **[Text](controls/properties-core.md)** property of the label, replace **"Hello World"** with **Sum(1,2,3)**.

    ![Typing the partial function Sum(1,2,3 without a closing parenthesis shows errors.](./media/working-with-formulas/label-sum-partial.png)

    While you type, the formula bar helps you by showing the description and the expected arguments for this function.  As with the final double quotation mark in **"Hello World"**, the screen shows yellow exclamation points to indicate an error until you type the final parenthesis of this formula:

    ![Using the complete formula Sum(1,2,3).](./media/working-with-formulas/label-sum.png)

## Change a value based on input

In Excel, you type **=A1+A2** into a cell to show the sum of whatever values cells **A1** and **A2** contain. If either or both of those values change, the cell that contains the formula automatically shows the updated result.

![Animation of Excel recalculating the sum of two numbers.](./media/working-with-formulas/excel-recalc.gif)

In Power Apps, you can achieve a similar result by adding controls to a screen and setting their properties. This example shows a label control named **Label1** and two **[Text input](controls/control-text-input.md)** controls, named **TextInput1** and **TextInput2**.

![Illustration of Power Apps recalculating the sum of two numbers.](./media/working-with-formulas/recalc1.png)

Regardless of what numbers you type in the text-input controls, the label always shows the sum of those numbers because its **[Text](controls/properties-core.md)** property is set to this formula:

`TextInput1 + TextInput2`

![Animation of Power Apps recalculating the sum of two numbers.](./media/working-with-formulas/recalc2.gif)

In Excel, you can use conditional-formatting formulas to show, for example, negative values in red. In Power Apps, you can use formulas to determine not only the primary value of a control but also properties such as formatting. In the next example, a formula for the **[Color](controls/properties-color-border.md)** property of the label automatically shows negative values in red. The **[If](functions/function-if.md)** function should look very familiar from Excel:

`If( Value(Label1.Text) < 0, Red, Black )`

![Animation of conditional formatting.](media/working-with-variables/recalc-color.gif)

## Change a color based on user input

You can configure your app with formulas so that users can change your app's appearance or behavior. For example, you can create a filter to show only data that contains a string of text that the user specifies, or you can let users sort a set of data based on a certain column in the data set. In this procedure, you'll let users change the color of the screen by adjusting one or more sliders.

1. Remove the controls from the previous procedures, or create a blank app as you did previously, and add three slider controls to it:

    ![Insert a slider control.](./media/working-with-formulas/insert-slider.png)
2. Arrange the sliders so they don't overlap, add three labels, and configure them to show **Red**, **Green**, and **Blue**:

    ![Arrange sliders and add labels for each color component.](./media/working-with-formulas/three-sliders.png)
3. Set the **Max** property of each slider to 255, which is the maximum value of a color component for the **[RGBA](functions/function-colors.md)** function.

    You can specify the **Max** property by selecting it on the **Content** tab or in the property list:

    ![Change the maximum value of each slider.](./media/working-with-formulas/three-sliders-max.png)
4. Select the screen by clicking away from any control, and then set the screen's **[Fill](controls/properties-color-border.md)** property to this formula:<br>**RGBA( Slider1.Value, Slider2.Value, Slider3.Value, 1 )**

    As already described, you access control properties by using the **.** operator.  **Slider1.Value** refers to the slider's **[Value](controls/properties-core.md)** property, which reflects where the user has placed the slider between the **Min** and **Max** values. As you type this formula, each control that it contains is color coded between the screen and the formula bar:

    ![Change the formula for the background fill color of the screen, but not yet complete.](./media/working-with-formulas/three-sliders-partial-rgba.png)

    As you type the closing parenthesis, the screen's background will change to dark gray based on the default value of each slider, which is **50**. At the moment when you finish typing the formula, it's calculated and used as the value of the background fill color. You can interact with your app while in the default workspace without needing to open Preview:

    ![Change the maximum value of each slider 1.](./media/working-with-formulas/three-sliders-complete-rgba.png)
5. Adjust the sliders, and see how your changes affect the background color.

    As each slider changes, the formula that contains the **[RGBA](functions/function-colors.md)** function is recalculated, which immediately changes how the screen appears.

    ![Change the formula for the background fill color of the screen, now complete.](./media/working-with-formulas/color-sliders.gif)

## Manage app behavior

You can use formulas not only to perform calculations and change appearance but also to take action. For example, you can set the **[OnSelect](controls/properties-core.md)** property of a button to a formula that includes the **[Navigate](functions/function-navigate.md)** function. When a user selects that button, the screen that you specify in the formula appears.

You can use some functions, such as **[Navigate](functions/function-navigate.md)** and **[Collect](functions/function-clear-collect-clearcollect.md)**, only in behavior formulas.  The formula reference calls out if you can use a function only in this context.  

You can take more than one action in a behavior formula if you separate functions with a semi-colon (;). For example, you might want to update a context variable, push data to a data source, and finally navigate to another screen.

## View a list of properties by category

The properties list shows properties alphabetically, but you can also view all the properties of a control, organized by category, if you select the **Advanced** option on the **View** tab:

![Advanced view.](./media/working-with-formulas/advanced-open.png)

You can edit formulas directly within this view.  With the control selector at the top of the pane, you can quickly find a control to work with.  And with the property search, you can quickly find a property of that control.

Initially, this view shows the most important properties.  To reveal all the properties, click the down arrow at the bottom of the pane.  Each control has a long list of properties that govern all aspects of the control's behavior and appearance. You can scroll through the list or search for a property by typing in the box at the top of the pane.

## Formula syntax

As you type a formula in the formula bar, different syntax elements appear in different colors to improve readability and help you understand long formulas. Here is the color code list in Power Apps.

![syntax highlighting.](./media/working-with-formulas/syntax-highlighting.png)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]