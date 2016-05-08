<properties
    pageTitle="Pen input control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Pen input control"
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

# Pen input control in PowerApps #
A control in which the user can draw, erase, and highlight areas of an image.

## Description ##
The user can use this control like a whiteboard, drawing diagrams and writing words that can be converted to typed text.

## Key properties ##

**[Color](../properties/properties-color-border.md)** – The color of text in a control.

**Mode** – The control is in **Draw**, **Erase**, or **Select** mode.

## Additional properties ##

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**Input** – Input.

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[SelectionColor](../properties/properties-color-border.md)** – The text color of a selected item or items in a list or the color of the selection tool in a pen control.

**SelectionThickness** – The thickness of the selection tool for a pen-input control.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.

**[Size](../properties/properties-text.md)** – The font size of the text that appears on a control.

**[Tooltip](../properties/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Collect**( *CollectionName*, *DatatoCollect* )](function-clear-collect-clearcollect.md)

## Example ##

### Create a set of images ###
1. Add a **Pen input** control, name it **MyDoodles**, and set its **ShowControls** property to **true**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a **Button** control, move it below **MyDoodles**, and set the **Text** property of the **Button** control to show **Add**.

1. Set the **OnSelect** property of the **Button** control to this formula:<br>
**Collect(Doodles, {Sketch:MyDoodles.Image})**

1. Add an **Image gallery** control, move it below the **Button** control, and shrink the width of the **Image gallery** control until it shows three items.

1. Set the **Items** property of the **Image gallery** control to **Doodles**, and then  press F5.

1. Draw an image in **MyDoodles**, and then click or tap the **Button** control.

	The image that you drew appears in the **Image gallery** control.

1. (optional) In the **Pen input** control, click or tap the icon to clear the image that you drew, draw another image, and then click or tap the **Button** control.

1. In the **Image gallery** control, set the **OnSelect** property of the **Image** control to this formula:<br>
**Remove(Doodles, ThisItem)**

1. Remove a drawing by clicking or tapping it in the **Image gallery** control.

Use the [**SaveData** function](function-savedata-loaddata.md) to save your drawings locally or the [**Patch** function](function-patch.md) to save them to a data source.
