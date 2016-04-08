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
[AZURE.INCLUDE [control-summary-date-picker](../../includes/control-summary-date-picker.md)]

## Description ##
If you add a **Date Picker** control instead of a **Text input** control, you help ensure that the user specifies a date in the correct format.

## Key properties ##

[AZURE.INCLUDE [short-startyear](../../includes/short-startyear.md)]

[AZURE.INCLUDE [short-endyear](../../includes/short-endyear.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledcolor](../../includes/short-disabledcolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-endyear](../../includes/short-endyear.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-fontweight](../../includes/short-fontweight.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-italic](../../includes/short-italic.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-startyear](../../includes/short-startyear.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Year**( *DateTimeValue* )](function-datetime-parts.md)

## Example ##
1. Add a **Date Picker** control, and name it **Deadline**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a **Text Box** control, and set its **Items** property to this formula:
<br>**DateDiff(Today(), Deadline.SelectedDate) & " days to go!"**

	Want more information about the [**DateDiff** function](function-dateadd-datediff.md) or [other functions](formula-reference.md)?

1. Press F5, choose a date in **Deadline**, and then click or tap **OK**.

	The **Text Box** control shows the number of days between today and the date that you chose.

1. To return to the default workspace, press Esc.
