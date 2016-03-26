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

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-max](../../includes/short-max.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-max](../../includes/short-max.md)]

[AZURE.INCLUDE [short-onchange](../../includes/short-onchange.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-ratingfill](../../includes/short-ratingfill.md)]

[AZURE.INCLUDE [short-readonly](../../includes/short-readonly.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-showvalue](../../includes/short-showvalue.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-valid](../../includes/short-valid.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

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
