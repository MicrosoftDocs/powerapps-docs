---
title: Use the Fluent UI controls | Microsoft Docs
description: Learn about the new Fluent UI Framework controls in Power Apps.
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: tapanm
ms.reviewer: 
---

# Use the Fluent UI controls

Creating apps that look great in Teams will be easier with our new components. Built on [Fluent UI framework](https://www.microsoft.com/design/fluent/#/), the new components will look great with Teams styles and will automatically adjust to the current Teams theme. The new controls are: Button, Check box, Combo box, Date picker, Label, Radio group, Rating, Slider, Text box, and Toggle.

Let’s take a look at each Fluent UI control and the most useful properties. For a complete list of controls and properties in Power Apps, go to [Controls and
properties in Power Apps](https://docs.microsoft.com/powerapps/maker/canvas-apps/reference-properties).

## Button

A control that the user can select to interact with the app.

![Button control](media/fluent-button.png)

### Description

Configure the OnSelect property of a Button control to run one or more formulas when the user selects the control.

### Key properties

*ButtonType* – The style of button to show, Default, or Primary. Default value: **Standard**.

*OnSelect* – How the app responds when the user selects a control.

*Text* – Text that appears on a control or that the user types into a control.

## Check box

A control that the user can select or clear to set its value to **true** or
**false**.

![Check box control](media/fluent-check-box.png)

### Description

The user can specify a Boolean value by using this familiar control, which has
been widely used in the user interface.

### Key properties

*Box side* – The side of the control that the check box is displayed.

*Label* – Text that appears on a control.

*Value* – The value of an input control.

## Combo box

A control that allows users to make selections from provided choices. Supports
search and multiple selections.

![Combo box control](media/fluent-combo-box.png)

### Description

A Combo box control allows you to search for items you'll select. The search
is done server-side on the *SearchField* property so performance is not
affected by large data sources.

Single or multi-select mode is configured via the *SelectMultiple* property.

### Key properties

*Items* – The source of data from which selections can be made.

*DefaultSelectedItems* – The initial selected item(s) before the user interacts with the control.

*SelectMultiple* – Whether the user can select a single item or multiple items.

*IsSearchable* – Whether the user can search for items before selecting.

## Date picker

A control that the user can select to specify a date.

![Date picker control](media/fluent-date-picker.png)

### Description

If you add a **Date Picker** control instead of a **Text input** control, you
help ensure that the user specifies a date in the correct format.

### Key properties

*Value* – The date currently selected in a date control. This date is
represented in local time.

*Format* – The text format in which the control shows the date and the user
specifies the date. You can set this property to ShortDate (default) or LongDate to format dates based on the Language property of this control. You can also set this property to an expression, such as yyyy/mm/dd if you want the same format independent of the language. For example:

-   The control shows "12/31/2017" if the user selects the last day of
    2017, the Format property is set to ShortDate, and the Language property is
    set to "en-us".

-   The control shows "dimanche 31 December 2017" if the user selects the
    last day of 2017, the Format property is set to LongDate, and the Language
    property is set to "fr-fr".

## Label

A box that shows data such as text, numbers, dates, or currency.

![Label control](media/fluent-label.png)

### Description

A label shows data that you specify as a literal string of text or as a formula that evaluates to a string of text. Labels often appear outside of any other control (such as a banner that identifies a screen), as a label that identifies another control (such as a rating or audio control), or in a gallery to show a specific type of information about an item.

### Key properties

*Color* – The color of text in a control.

*Font* – The name of the family of fonts in which text appears.

*Text* – The text that appears on a control.

## Radio group

An input control that shows multiple options, of which users can select only one at a time.

![Radio group control](media/fluent-radio-group.png)

### Description

A Radio group control, a standard HTML input control, is best used with only a
few, mutually exclusive options.

### Key properties

*Items* – The source of data that appears in a control such as a gallery, a
list, or a chart.

*Selected* – The data record that represents the selected item.

## Rating

A control with which users can indicate a value between 0 and a maximum number
that you specify.

![Rating control](media/fluent-rating.png)

### Description

In this control, the user can indicate, for example, how much they liked
something by selecting a certain number of stars.

### Key properties

*Value* – The initial value of a control before it's changed by the user.

*Max* – The maximum value to which the user can set a slider or a rating.

## Slider

A control with which the user can specify a value by dragging a handle.

![Slider control](media/fluent-slider.png)

### Description

The user can indicate a value, between a minimum and a maximum value that you
specify, by dragging the handle of a slider left-right or up-down, depending on the direction that you choose.

### Key properties

*Max* – The maximum value to which the user can set a slider or a rating.

*Min* – The minimum value to which the user can set a slider.

*Value* – The value of an input control.

*Layout* – Whether a control is displayed horizontally or vertically.

*Show value* – Whether a control should display the value.

## Text box

A box in which the user can type text, numbers, and other data.

![Text box control](media/fluent-text-box.png)

### Description

The user can specify data by typing into a text box control. Depending on how
you configure the app, that data might be added to a data source, used to
calculate a temporary value, or incorporated in some other way.

### Key properties

*Font* – The name of the family of fonts in which text appears.

*Text* – Text that appears on a control or that the user types into a control.

## Toggle

A control that the user can turn on or off by moving its handle.

![Toggle control](media/fluent-toggle.png)

### Description

A Toggle is designed for modern user interface but behaves the same way as a check box.

### Key properties

*Value* – The value of an input control.

*OffText* – The text of the off state.

*OnText* – The text of the on state.

### See also

- [Create additional apps](create-additional-apps.md)
- [Understand Power Apps Studio](understand-power-apps-studio.md)
