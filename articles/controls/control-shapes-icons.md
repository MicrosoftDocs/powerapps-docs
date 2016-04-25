<properties
    pageTitle="Shape controls and icon controls: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about shape controls and icon controls"
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
   ms.date="03/11/2016"
   ms.author="anneta"/>

# Shape controls and icon controls in PowerApps #
[AZURE.INCLUDE [control-summary-shapes-icons](../../includes/control-summary-shapes-icons.md)]

## Description ##
These controls include arrows, geometric shapes, action icons, and symbols for which you can configure properties such as fill, size, and location. You can also configure their **OnSelect** property so that the app responds if the user clicks or taps the control.

## Key properties ##

[**Fill**](properties\properties-color-border.md) – The background color of a control.

[**OnSelect**](properties\properties-core.md) – How the app responds when the user taps or clicks a control.

## Additional properties ##

[**Disabled**](properties\properties-core.md) – Whether the user can interact with the control.

[**Height**](properties\properties-size-location.md) – The distance between a control's top and bottom edges.

[**HoverFill**](properties\properties-color-border.md) – The background color of a control when the user keeps the mouse pointer on it.

[**PressedBorderColor**](properties\properties-color-border.md) – The color of a control's border when the user taps or clicks that control.

[**Visible**](properties\properties-core.md) – Whether a control appears or is hidden.

[**Width**](properties\properties-size-location.md) – The distance between a control's left and right edges.

[**X**](properties\properties-size-location.md) – The distance between the left edge of a control and the left edge of the screen.

[**Y**](properties\properties-size-location.md) – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Navigate**( *ScreenName*, *ScreenTransition* )](function-navigate.md)

## Example ##
1. Name the default **Screen** control **Target**, add a **Text box** control, and set its **Text** property to show **Target**.

	Don't know how to [add and configure a control](add-configure-controls.md)?

1. Add a **Screen** control, and name it **Source**.

1. In **Source**, add a **Shape** control, and set its **OnSelect** property to this formula:
<br>**Navigate(Target, ScreenTransition.Fade)**

1. Press F5, and then click or tap the **Shape** control.

	The **Target** screen appears.

1. (optional) Press Esc to return to the default workspace, add a **Shape** control to **Target**, and set the **OnSelect** property of the **Shape** control to this formula:
<br>**Navigate(Source, ScreenTransition.Fade)**
