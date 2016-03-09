<properties
    pageTitle="Export and import controls: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the export and import controls"
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

# Export and import controls in PowerApps #
[AZURE.INCLUDE [control-summary-export-import](../../includes/control-summary-export-import.md)]

## Description ##
If you want to create more than one app that uses the same data but not share that data outside those apps, you can export it and import it by using the export and import controls. When you export data, you create a compressed file that you can copy to another machine, but you can't read it in any program other than PowerApps.

## Key properties ##
[AZURE.INCLUDE [short-data](../../includes/short-data.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

## All properties ##

[AZURE.INCLUDE [short-align](../../includes/short-align.md)]

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-data](../../includes/short-data.md)]

- The **Data** property is available for the export control but not the import control.

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

[AZURE.INCLUDE [short-padding](../../includes/short-padding.md)]

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

[AZURE.INCLUDE [short-underline](../../includes/short-underline.md)]

[AZURE.INCLUDE [short-verticalalign](../../includes/short-verticalalign.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Example ##
1. Add a button, and set its **OnSelect** property to this formula:
<br>**ClearCollect(Products, {Name:"Europa", Price:"10.99"}, {Name:"Ganymede", Price:"12.49"}, {Name:"Callisto", Price:"11.79"})**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

	Want more information about the [**ClearCollect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Press F5, select the button, and then press Esc.

1. Add an export control, and set its **Data** property to **Products**.

1. Press F5, select the export control, and then specify the name of the file into which you want to export the data.

1. Select **Save**, then press Esc to return to the default workspace.

1. In a new or existing app, add an import control, name it **MyData**, and set its **OnSelect** property to this formula:<br>
**Collect(ImportedProducts, MyData.Data)**

1. Press F5, select the file that you exported, and then select **Open**.

1. Press Esc, select **Collections** on the **File** menu, and confirm that the new app has the data that you exported.
