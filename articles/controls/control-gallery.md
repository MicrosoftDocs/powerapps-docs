<properties
    pageTitle="Gallery control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Gallery control"
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
   ms.date="03/10/2016"
   ms.author="anneta"/>

# Gallery control in PowerApps #
A control that contains other controls and shows a set of data.

## Description ##
A **Gallery** control can show records from a data source, and each record can contain multiple types of data. For example, a **Gallery** control can show contact information that includes a name, an address, and a phone number for each contact. Each type of information appears in a separate control within the **Gallery** control, and you configure those controls in its template. The template appears on the left edge of a **Gallery** control in horizontal/landscape orientation and at the top of a **Gallery** control in vertical/portrait orientation. Any changes that you make in the template are reflected throughout the **Gallery** control.

## Key properties ##

**[Default](../properties/properties-core.md)** – The initial value of a control before it is changed by the user.

**[Items](../properties/properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

**Selected** – The selected item.

## Additional properties ##

**AllItems** – All items in a gallery, including additional control values that are a part of the gallery's template.

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**Direction** – Whether the first item in a gallery in landscape orientation appears near the left or right edge.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**Layout** – Whether the user scrolls through a gallery or adjusts a slider top to bottom (**Vertical**) or left to right (**Horizontal**).

**NavigationStep** – How far a gallery scrolls if its **ShowNavigation** property is set to **true** and the user selects a navigation arrow at either end of that gallery.

**ShowNavigation** – Whether an arrow appears at each end of a gallery so that a user can scroll through the items in the gallery by clicking or tapping an arrow.

**ShowScrollbar** – Whether a scrollbar appears when the user hovers over a gallery.

**Snap** – Whether, when a user scrolls through a gallery, it automatically snaps so that the next item appears in full.

**TemplateFill** – The background color of a gallery.

**TemplatePadding** – The distance between items in a gallery.

**TemplateSize** – The height of the template for a gallery in vertical/portrait orientation or the width of the template for a gallery in horizontal/landscape orientation.

**Transition** – The visual effect (**Pop**, **Push**, or **None**) when the user hovers over an item in a gallery.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**WrapCount** – How many records appear in each item of a gallery.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Filter**( *DataSource*, *Formula* )](../functions/function-filter-lookup.md)

## Examples ##
### Show and filter data ###
- [Show text](control-text-box.md#show-data-in-a-gallery)
- [Show images](control-image.md#show-a-set-of-images-from-a-data-source)
- [Filter data by selecting a list option](control-drop-down.md#example)
- [Filter data by adjusting a slider](control-slider.md#example)

### Get data from the user ###
- [Get text](control-text-input.md#collect-data)
- [Get images](control-add-picture.md#add-images-to-an-image-gallery-control)
- [Get photos](control-camera.md#example)
- [Get sounds](control-microphone.md#example)
- [Get drawings](control-pen-input.md#create-a-set-of-images)
