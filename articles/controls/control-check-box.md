<properties
    pageTitle="Check-box control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the check-box control"
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

# Check-box control in PowerApps #
[AZURE.INCLUDE [control-summary-check-box](../../includes/control-summary-check-box.md)]

## Description ##
The user can specify a Boolean value by using this familiar control, which has been used in GUIs for decades.

## Key properties ##

[AZURE.INCLUDE [short-text](../../includes/short-text.md)]

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-checkboxbackgroundfill](../../includes/short-checkboxbackgroundfill.md)]

[AZURE.INCLUDE [short-checkboxbordercolor](../../includes/short-checkboxbordercolor.md)]

[AZURE.INCLUDE [short-checkboxsize](../../includes/short-checkboxsize.md)]

[AZURE.INCLUDE [short-checkmarkfill](../../includes/short-checkmarkfill.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

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

[AZURE.INCLUDE [short-oncheck](../../includes/short-oncheck.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-onuncheck](../../includes/short-onuncheck.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedcolor](../../includes/short-pressedcolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-strikethrough](../../includes/short-strikethrough.md)]

[AZURE.INCLUDE [short-text](../../includes/short-text.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-underline](../../includes/short-underline.md)]

[AZURE.INCLUDE [short-valid](../../includes/short-valid.md)]

[AZURE.INCLUDE [short-verticalalign](../../includes/short-verticalalign.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**If**( *Condition*, *Result* )](function-if.md)

## Example ##
1. Add a check box, name it **chkReserve**, and set its **Text** property to show **Reserve now**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a date picker, and set its **Visible** property to this formula:
<br>**If(chkReserve.Value = true, true)**

	Want more information about the [**If** function](function-if.md) or [other functions](formula-reference.md)?

1. Press F5, select **chkReserve**, and then clear it.

	The date picker appears when **chkReserve** is selected but not when it's cleared.

1. To return to the default workspace, press Esc.
