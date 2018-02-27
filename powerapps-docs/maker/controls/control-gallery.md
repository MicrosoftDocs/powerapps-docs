---
title: 'Gallery control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Gallery control
services: ''
suite: powerapps
documentationcenter: na
author: RickSaling
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 05/25/2017
ms.author: sharik

---
# Gallery control in PowerApps
A control that contains other controls and shows a set of data.

## Description
A **Gallery** control can show multiple records from a data source, and each record can contain multiple types of data. For example, a **Gallery** control can show multiple contacts with each item showing contact information that includes a name, an address, and a phone number for each contact. Each data field appears in a separate control within the **Gallery** control, and you can configure those controls in its template. The template appears as the first item inside the gallery, on the left edge of a **Gallery** control in horizontal/landscape orientation and at the top of a **Gallery** control in vertical/portrait orientation. Any changes that you make in the template are reflected throughout the **Gallery** control.

Predefined Gallery templates for showing images, text as well as a gallery with variable height items are available.

## Key properties
**[Default](../../controls/properties-core.md)** – The item or record from the data source to be selected in the gallery when the app starts up.

**[Items](../../controls/properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

**Selected** – The selected item.

## Additional properties
**AllItems** – All items in a gallery, including additional control values that are a part of the gallery's template.

**[BorderColor](../../controls/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../../controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../../controls/properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](../../controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Fill](../../controls/properties-color-border.md)** – The background color of a control.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**Layout** – Whether the user scrolls through a gallery or adjusts a slider top to bottom (**Vertical**) or left to right (**Horizontal**).

**NavigationStep** – How far a gallery scrolls if its **ShowNavigation** property is set to **true** and the user selects a navigation arrow at either end of that gallery.

**ShowNavigation** – Whether an arrow appears at each end of a gallery so that a user can scroll through the items in the gallery by clicking or tapping an arrow.

**ShowScrollbar** – Whether a scrollbar appears when the user hovers over a gallery.

**Snap** – Whether, when a user scrolls through a gallery, it automatically snaps so that the next item appears in full.

**TemplateFill** – The background color of a gallery.

**TemplatePadding** – The distance between items in a gallery.

**TemplateSize** – The height of the template for a gallery in vertical/portrait orientation or the width of the template for a gallery in horizontal/landscape orientation.

**Transition** – The visual effect (**Pop**, **Push**, or **None**) when the user hovers over an item in a gallery.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**WrapCount** – Number of items shown per row or column based on horizontal or vertical layout.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Filter**( *DataSource*, *Formula* )](../../functions/function-filter-lookup.md)

## Examples
### Show and filter data
* [Show text](control-text-box.md#show-data-in-a-gallery)
* [Show images](control-image.md#show-a-set-of-images-from-a-data-source)
* [Filter data by selecting a list option](control-drop-down.md#example)
* [Filter data by adjusting a slider](control-slider.md#example)

### Get data from the user
* [Get text](control-text-input.md#collect-data)
* [Get images](control-add-picture.md#add-images-to-an-image-gallery-control)
* [Get photos](control-camera.md#example)
* [Get sounds](control-microphone.md#example)
* [Get drawings](control-pen-input.md#create-a-set-of-images)

