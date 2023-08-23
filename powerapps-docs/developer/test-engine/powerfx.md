---
title: "Power Apps Test Engine Power Fx functions (preview)"
description: "Describes Power Fx functions you can use with Power Apps Test Engine."
author: jt000
ms.author: jasontre
ms.date: 08/11/2023
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---


# Power Apps Test Engine Power Fx functions (preview)


[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

There are several functions defined for the test framework.

- [Assert](#assert)
- [Screenshot](#screenshot)
- [Select](#select)
- [SetProperty](#setproperty)
- [Wait](#wait)

## Assert

`Assert(BooleanExpression)`

`Assert(BooleanExpression, Message)`

The `Assert` function takes in a Power Fx expression that should evaluate to a boolean value. If the value returned is false, the test fails.

### Assert example

`Assert(Label1.Text = "1");`

`Assert(Label1.Text = "1", "Checking that the Label1 text is set to 1");`

## Screenshot

`Screenshot(fileNameOfScreenshot)`

This function captures a screenshot of the app at the current point in time. The screenshot file is saved to the test output folder and with the name provided.

> **Note:** Only jpeg and png files are supported.

### Screenshot Example

`Screenshot("buttonClicked.png")`

## Select

`Select(control)`

`Select(control, row or column)`

`Select(control, row or column, child control)`

`Select(Index(gallerycontrol.AllItems, row or column).child control)`

This function has the same functionality as the Power Apps  [Select function](/power-platform/power-fx/reference/function-select).

When working with a nested gallery, use [Index()](/power-platform/power-fx/reference/function-first-last) within the select function.

### Select example

`Select(Button1)`

`Select(Gallery1,1)`

`Select(Gallery1,1,Button1)`

`Select(Index(Gallery1.AllItems, 2).Icon2)`

`Select(Index(Index(Gallery1.AllItems, 1).Gallery2.AllItems, 4).Icon3);`

## SetProperty

`SetProperty(control.propertyName, propertyValue)`

This function has the same functionality as the Power Apps [SetProperty function](/power-platform/power-fx/reference/function-setproperty).

When working with a nested gallery, use [Index()](/power-platform/power-fx/reference/function-first-last) within the `SetProperty` function.

### SetProperty example

`SetProperty(TextInput.Text, "Say Something")`

`SetProperty(Dropdown1.Selected, {Value:"2"})`

`SetProperty(ComboBox1.SelectedItems, Table({Value:"1"},{Value:"2"}))`

`SetProperty(Index(Gallery1.AllItems, 1).TextInput1.Text, "Change the text input")`

`Select(Index(Index(Gallery1.AllItems, 1).Gallery2.AllItems, 1).TextInput1.Text, "Change the text input")`

## Wait

`Wait(Control, Property, Value)`

This function waits for the property of the control to equal the specified value.

### Wait example

` Wait(Label1, "Text", "0")`

### See also

[Power Apps Test Engine overview (preview)](overview.md)   
[Power Apps Test Engine YAML format (preview)](yaml.md)   

[!INCLUDE [footer-banner](../../includes/footer-banner.md)]

