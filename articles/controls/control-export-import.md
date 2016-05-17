<properties
    pageTitle="Export control and Import control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Export control and the Import control"
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

# Export control and Import control in PowerApps #
Controls for exporting data to a local file and then importing that data into another app in PowerApps.

## Description ##
If you want to create more than one app that uses the same data but not share that data outside those apps, you can export it and import it by using an **Export** control and an **Import** control. When you export data, you create a compressed file that you can copy to another machine, but you can't read it in any program other than PowerApps.

## Key properties ##
**Data** – The name of a collection that you want to export to a local file.

- The **Data** property is available for an **Export** control but not an **Import** control.

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

## Additional properties ##

**[Align](../properties/properties-text.md)** – The location of text in relation to the horizontal center of its control.

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**[Color](../properties/properties-color-border.md)** – The color of text in a control.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](../properties/properties-color-border.md)** – The color of a control's border if the control's **[Disabled](../properties/properties-core.md)** property is set to **true**.

**[DisabledColor](../properties/properties-color-border.md)** – The color of text in a control if its **[Disabled](../properties/properties-core.md)** property is set to **true**.

**[DisabledFill](../properties/properties-color-border.md)** – The background color of a control if its **[Disabled](../properties/properties-core.md)** property is set to **true**.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Font](../properties/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../properties/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](../properties/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](../properties/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](../properties/properties-text.md)** – Whether the text in a control is italic.

**[Padding](../properties/properties-size-location.md)** – The distance between the text on an import or export button and the edges of that button.

**[PressedBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../properties/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../properties/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[RadiusBottomLeft](../properties/properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.

**[RadiusBottomRight](../properties/properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.

**[RadiusTopLeft](../properties/properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.

**[RadiusTopRight](../properties/properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.

**[Size](../properties/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](../properties/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[Text](../properties/properties-core.md)** – Text that appears on a control or that the user types into a control.

**[Underline](../properties/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](../properties/properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Example ##
1. Add a **[Button](control-button.md)** control, and set its **[OnSelect](../properties/properties-core.md)** property to this formula:
<br>**ClearCollect(Products, {Name:"Europa", Price:"10.99"}, {Name:"Ganymede", Price:"12.49"}, {Name:"Callisto", Price:"11.79"})**

	Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

	Want more information about the **[ClearCollect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?

1. Press F5, click or tap the **[Button](control-button.md)** control, and then press Esc.

1. Add an **Export** control, and set its **Data** property to **Products**.

1. Press F5, click or tap the **Export** control, and then specify the name of the file into which you want to export the data.

1. Click or tap **Save**, then press Esc to return to the default workspace.

1. In a new or existing app, add an **Import** control, name it **MyData**, and set its **[OnSelect](../properties/properties-core.md)** property to this formula:<br>
**Collect(ImportedProducts, MyData.Data)**

1. Press F5, click or tap **MyData**, click or tap the file that you exported, and then click or tap **Open**.

1. Press Esc, click or tap **Collections** on the **File** menu, and confirm that the current app has the data that you exported.
