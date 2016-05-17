<properties
    pageTitle="Date Picker control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Date Picker control"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="03/09/2016"
   ms.author="anneta"/>

# Date Picker control in PowerApps #
A control that the user can click or tap to specify a date.

## Description ##
If you add a **Date Picker** control instead of a **[Text input](control-text-input.md)** control, you help ensure that the user specifies a date in the correct format.

## Key properties ##

**DefaultDate** – The initial value of a date control before it is changed by the user.

**SelectedDate** – The date currently selected in a date control.

## Additional properties ##

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**[Color](../properties/properties-color-border.md)** – The color of text in a control.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](../properties/properties-color-border.md)** – The color of a control's border if the control's **[Disabled](../properties/properties-core.md)** property is set to **true**.

**[DisabledColor](../properties/properties-color-border.md)** – The color of text in a control if its **[Disabled](../properties/properties-core.md)** property is set to **true**.

**[DisabledFill](../properties/properties-color-border.md)** – The background color of a control if its **[Disabled](../properties/properties-core.md)** property is set to **true**.

**EndYear** – The latest year to which the user can set value of a date-picker control.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Font](../properties/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../properties/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[Italic](../properties/properties-text.md)** – Whether the text in a control is italic.

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](../properties/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../properties/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../properties/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../properties/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[Size](../properties/properties-text.md)** – The font size of the text that appears on a control.

**StartYear** – The earliest year to which the user can set the value of a date-picker control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Year**( *DateTimeValue* )](../functions/function-datetime-parts.md)

## Example ##
1. Add a **Date Picker** control, and name it **Deadline**.

	Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add a **[Text Box](control-text-box.md)** control, and set its **[Items](../properties/properties-core.md)** property to this formula:
<br>**DateDiff(Today(), Deadline.SelectedDate) & " days to go!"**

	Want more information about the **[DateDiff](../functions/function-dateadd-datediff.md)** function or [other functions](../formula-reference.md)?

1. Press F5, choose a date in **Deadline**, and then click or tap **OK**.

	The **[Text Box](control-text-box.md)** control shows the number of days between today and the date that you chose.

1. To return to the default workspace, press Esc.
