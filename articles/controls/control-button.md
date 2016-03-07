<properties
    pageTitle="Button control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the button control"
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
   ms.date="02/29/2016"
   ms.author="anneta"/>

# Button control in PowerApps #
[AZURE.INCLUDE [control-summary-button](../../includes/control-summary-button.md)]

## Description ##
Configure the **OnSelect** property of a **Button** control to run one or more formulas when the user clicks or taps the control.

## Key properties ##

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-text](../../includes/short-text.md)]

## All properties ##

[AZURE.INCLUDE [short-align](../../includes/short-align.md)]

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledcolor](../../includes/short-disabledcolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-fontweight](../../includes/short-fontweight.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-hovercolor](../../includes/short-hovercolor.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-italic](../../includes/short-italic.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedcolor](../../includes/short-pressedcolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-radiusbottomleft](../../includes/short-radiusbottomleft.md)]

[AZURE.INCLUDE [short-radiusbottomright](../../includes/short-radiusbottomright.md)]

[AZURE.INCLUDE [short-radiustopleft](../../includes/short-radiustopleft.md)]

[AZURE.INCLUDE [short-radiustopright](../../includes/short-radiustopright.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-strikethrough](../../includes/short-strikethrough.md)]

[AZURE.INCLUDE [short-text](../../includes/short-text.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-underline](../../includes/short-underline.md)]

[AZURE.INCLUDE [short-verticalalign](../../includes/short-verticalalign.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Navigate**( *ScreenName*, *ScreenTransitionValue* )](function-navigate.md)

## Example ##
1. Add a **Text input** control, and name it **Source**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a **Button**, set its **Text** property to show **Add**, and set its **OnSelect** property to this formula:<br>
**UpdateContext({Total:Total + Value(Source.Text)})**

	Want more information about the [**UpdateContext** function](function-updatecontext.md) or [other functions](formula-reference.md)?

1. Add a **Text box** control, set its **Text** property to **Total** (no quotation marks), and then press F5.

1. Type a number in **Source**, and then click or tap **Add**.

	The **Text box** shows the number that you typed.

1. Repeat the previous step one or more times.

	The **Text box** shows the sum of the numbers that you typed.

1. To return to the default workspace, press Esc.
