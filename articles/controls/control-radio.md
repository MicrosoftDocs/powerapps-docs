<properties
    pageTitle="Radio-button control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the radio-button control"
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

# Radio-button control in PowerApps #
[AZURE.INCLUDE [control-summary-radio](../../includes/control-summary-radio.md)]

## Description ##
A radio-button control, with which users have decades of experience, is best used with only a few options that are mutually exclusive.

## Key properties ##

[AZURE.INCLUDE [long-items](../../includes/long-items.md)]

[AZURE.INCLUDE [long-default](../../includes/long-default.md)]

[AZURE.INCLUDE [long-reset](../../includes/long-reset.md)]

## All properties ##
[AZURE.INCLUDE [short-align](../../includes/short-align.md)]

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

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

[AZURE.INCLUDE [short-hovercolor](../../includes/short-hovercolor.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-italic](../../includes/short-italic.md)]

[AZURE.INCLUDE [short-items](../../includes/short-items.md)]

[AZURE.INCLUDE [short-lineheight](../../includes/short-lineheight.md)]

[AZURE.INCLUDE [short-onchange](../../includes/short-onchange.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-pressedcolor](../../includes/short-pressedcolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-radiobackgroundfill](../../includes/short-radiobackgroundfill.md)]

[AZURE.INCLUDE [short-radiobordercolor](../../includes/short-radiobordercolor.md)]

[AZURE.INCLUDE [short-radioselectionfill](../../includes/short-radioselectionfill.md)]

[AZURE.INCLUDE [short-radiosize](../../includes/short-radiosize.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-strikethrough](../../includes/short-strikethrough.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-underline](../../includes/short-underline.md)]

[AZURE.INCLUDE [short-valid](../../includes/short-valid.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Distinct**( *DataSource*, *ColumnName* )](function-distinct.md)

## Example ##
1. Add a radio-button control, name it **Pricing**, and set its **Items** property to this formula:
<br>**["Standard", "Premium"]**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a text box, move it below the **Pricing** list, and set its **Text** property to this formula:
<br>**If("Premium" in Pricing.Selected.Value, "$200 per day", "$150 per day")**

	Want more information about the [**If** function](function-if.md) or [other functions](formula-reference.md)?

1. Press F5, and then select either option in the **Pricing** list.

	The text box shows the appropriate text for your selection.

1. (optional) Select the other option to confirm that the text changes appropriately.

1. To return to the default workspace, press Esc.
