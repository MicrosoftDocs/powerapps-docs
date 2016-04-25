<properties
    pageTitle="Rating control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Rating control"
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

# Rating control in PowerApps #
[AZURE.INCLUDE [control-summary-rating](../../includes/control-summary-rating.md)]

## Description ##
In this control, the user can indicate, for example, how much they liked something by selecting a certain number of stars.

## Key properties ##

[**Default**](properties\properties-core.md) – The initial value of a control before it is changed by the user.

**Max** – The maximum value to which the user can set a slider or a rating.

## Additional properties ##

[**BorderColor**](properties\properties-color-border.md) – The color of a control's border.

[**BorderStyle**](properties\properties-size-location.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

[**BorderThickness**](properties\properties-size-location.md) – The thickness of a control's border.

[**Disabled**](properties\properties-core.md) – Whether the user can interact with the control.

[**Fill**](properties\properties-color-border.md) – The background color of a control.

[**Height**](properties\properties-size-location.md) – The distance between a control's top and bottom edges.

[**OnChange**](properties\properties-core.md) – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

[**OnSelect**](properties\properties-core.md) – How the app responds when the user taps or clicks a control.

**RatingFill** – The color of the stars in a rating control.

**ReadOnly** – Whether a user can change the value of a slider or rating control.

[**Reset**](properties\properties-core.md) – Whether a control reverts to its default value.

**ShowValue** – Whether a slider's or rating's value appears as the user changes that value or hovers over the control.

[**Tooltip**](properties\properties-core.md) – Explanatory text that appears when the user hovers over a control.

[**Visible**](properties\properties-core.md) – Whether a control appears or is hidden.

[**Width**](properties\properties-size-location.md) – The distance between a control's left and right edges.

[**X**](properties\properties-size-location.md) – The distance between the left edge of a control and the left edge of the screen.

[**Y**](properties\properties-size-location.md) – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Average**( *Value1*, *Value2,* ... )](function-aggregates.md)

## Example ##
1. Add a **Rating** control, and name it **Quantitative**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a **Text input** control, name it **Qualitative**, and move it below the **Rating** control.

1. Set the **Default** property of the **Text input** control to **""**, and set its **HintText** to this formula:
<br>**If(Quantitative.Value > 3, "What did you especially like?", "How might we do better?")**

	Want more information about the [**If** function](function-if.md) or [other functions](formula-reference.md)?

1. Press F5, and then click or tap either four or five stars in the **Rating** control.

	The hint text in the **Text input** control changes to reflect the high rating.

1. Click or tap fewer than four stars in **Quantitative**.

	The hint text in the **Text input** control changes to reflect the low rating.

1. To return to the default workspace, press Esc.
