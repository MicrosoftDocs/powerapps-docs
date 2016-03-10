<properties
    pageTitle="Toggle control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the toggle control"
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

# Toggle control in PowerApps #
[AZURE.INCLUDE [control-summary-toggle](../../includes/control-summary-toggle.md)]

## Description ##
A toggle is designed for recent GUIs but behaves the same way as a check box.

## Key properties ##

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-oncheck](../../includes/short-oncheck.md)]

[AZURE.INCLUDE [short-onuncheck](../../includes/short-onuncheck.md)]

## All properties ##
[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-handlefill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-onchange](../../includes/short-onchange.md)]

[AZURE.INCLUDE [short-oncheck](../../includes/short-oncheck.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-onuncheck](../../includes/short-onuncheck.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-railfill](../../includes/short-railfill.md)]

[AZURE.INCLUDE [short-railhoverfill](../../includes/short-railhoverfill.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-valid](../../includes/short-valid.md)]

[AZURE.INCLUDE [short-valuefill](../../includes/short-valuefill.md)]

[AZURE.INCLUDE [short-valuehoverfill](../../includes/short-valuehoverfill.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**If**( *Condition*, *Result* )](function-if.md)

## Example ##
1. Add a toggle, and name it **MemberDiscount**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a text box, and set its **Text** property to this formula:
<br>**If(MemberDiscount.Value = true, "Price: $75", "Price: $100")**

	Want more information about the [**If** function](function-if.md) or [other functions](formula-reference.md)?

1. Press F5, and change the value of **MemberDiscount**.

	The text box shows a different price, depending on whether **MemberDiscount** is on or off.

1. To return to the default workspace, press Esc.
