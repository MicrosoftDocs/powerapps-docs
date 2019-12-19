---
title: SetProperty function | Microsoft Docs
description: Reference information, including syntax, for the SetProperty function in Power Apps Test Studio
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 12/19/2018
ms.author: aheneay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# SetProperty function in Power Apps Test Studio

The SetProperty function simulates interactions with input controls as if the user had entered or set a value on the control. The following properties can be set using the SetProperty function.

## Syntax

*Select(Control Property, value)*

- *Control Property* – Required. The control property to set on behalf of the user.
- *Value* – Required. The value of the property to set on behalf of the user. 

## Examples

| Control	| Property	| Example expression
| :- | :- | :-
| TextInput	| Text	| ```SetProperty(TextInput1.Text, "Sample text")```
| RichTextEditor	| HtmlText	| ```SetProperty(RichTextEditor1.HtmlText, "<p>Sample text</p>")```
| Toggle	| Value	| ```SetProperty(Toggle1.Value, false)```
| Checkbox	| Value	| ```SetProperty(Checkbox1.Value, false)```
| Slider	| Value	| ```SetProperty(Slider1.Value, 10)```
| Rating	| Value	| ```SetProperty(Rating1.Value, 5)```
| DatePicker	| SelectedDate	| ```SetProperty(DatePicker1.SelectedDate, Date(2020,3,10))```
| Radio	| Selected	| ```SetProperty(Radio1.Selected, "Yes")```
| Radio | SelectedText | ```SetProperty(Radio1.SelectedText, "Yes")```
| Dropdown | Selected | ```SetProperty(Dropdown1.Selected, {Value:"Sample Value"})```
| Dropdown | SelectedText | ```SetProperty(Dropdown1.SelectedText, {Value:"value"})```
| Combobox | Selected | ```SetProperty(Dropdown1.Selected, {Value:"Sample Value"})```
| Combobox | SelectedItems | ```SetProperty(ComboBox1.SelectedItems, Table({Value:"Sample Value"},({Value:"Sample Value"}))```
| ListBox | Selected | ```SetProperty(Listbox1.Selected, {'Value':"Sample Value"})```
| ListBox | SelectedText | ```SetProperty(Listbox1. SelectedText, {'Value':"Sample text"})```
| ListBox | SelectedItems | ```SetProperty(Listbox1.SelectedItems, Table({Value:"Sample value"},({Value:"Sample value"}))```
| ListBox | SelectedItemsText | ```SetProperty(Listbox1.SelectedItemsText, Table({Value:"Sample value"},({Value:"Sample value"}))```

