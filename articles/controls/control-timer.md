<properties
    pageTitle="Timer control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the timer control"
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

# Timer control in PowerApps #
[AZURE.INCLUDE [control-summary-timer](../../includes/control-summary-timer.md)]

## Description ##
Timers can, for example, determine how long a control appears or change other properties of a control after a certain amount of time has passed.

## Key properties ##

[AZURE.INCLUDE [short-duration](../../includes/short-duration.md)]

[AZURE.INCLUDE [short-ontimerend](../../includes/short-ontimerend.md)]

[AZURE.INCLUDE [short-repeat](../../includes/short-repeat.md)]

## All properties ##

[AZURE.INCLUDE [short-align](../../includes/short-align.md)]

[AZURE.INCLUDE [short-autopause](../../includes/short-autopause.md)]

[AZURE.INCLUDE [short-autostart](../../includes/short-autostart.md)]

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledcolor](../../includes/short-disabledcolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-duration](../../includes/short-duration.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-fontweight](../../includes/short-fontweight.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-hovercolor](../../includes/short-hovercolor.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-italic](../../includes/short-italic.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-ontimerend](../../includes/short-ontimerend.md)]

[AZURE.INCLUDE [short-ontimerstart](../../includes/short-ontimerstart.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedcolor](../../includes/short-pressedcolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-repeat](../../includes/short-repeat.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-start](../../includes/short-start.md)]

[AZURE.INCLUDE [short-strikethrough](../../includes/short-strikethrough.md)]

[AZURE.INCLUDE [short-text](../../includes/short-text.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-underline](../../includes/short-underline.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Refresh**( *DataSource* )](function-refresh.md)

## Examples ##
### Show a countdown ###
1. Add a timer, and name it **Countdown**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Set the timer's **Duration** property to **10000** and its **Repeat** and **Autostart** properties to **true**.

1. (optional) Make the timer easier to read by setting its **Height** property to **160**, its **Width** property to **600**, and its **Size** property to **60**.

1. Add a text box, and set its **Text** property to this formula:
<br>**"Number of seconds remaining: " & RoundUp(10-Countdown.Value/1000, 0)**

	Want more information about the [**RoundUp** function](function-round.md) or [other functions](formula-reference.md)?

	The text box shows how many seconds remain before the timer restarts.

1. (optional) Set the timer's **Visible** property to **false**.

### Animate a control ###
1. Add a timer, and name it **FadeIn**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Set the timer's **Duration** property to **5000** and its **Repeat** and **Autostart** properties to **true**.

1. (optional) Make the timer easier to read by setting its **Height** property to **160**, its **Width** property to **600**, and its **Size** property to **60**.

1. Add a text box, set its **Text** property to show **Welcome!** and set its **Color** property to this formula:
<br>**ColorFade(Color.BlueViolet, FadeIn.Value/5000)**

	Want more information about the [**ColorFade** function](function-colors.md) or [other functions](formula-reference.md)?

	The text in the text box fades to white, returns to full intensity, and repeats the process.

1. (optional) Set the timer's **Visible** property to **false**.
