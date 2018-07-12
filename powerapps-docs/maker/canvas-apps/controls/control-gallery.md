---
title: 'Gallery control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Gallery control
documentationcenter: na
author: fikaradz
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.component: canvas
ms.date: 05/25/2017
ms.author: sharik

---
# Gallery control in PowerApps
A control that contains other controls and shows a set of data.

## Description
A **Gallery** control can show multiple records from a data source, and each record can contain multiple types of data. For example, a **Gallery** control can show multiple contacts with each item showing contact information that includes a name, an address, and a phone number for each contact. Each data field appears in a separate control within the **Gallery** control, and you can configure those controls in its template. The template appears as the first item inside the gallery, on the left edge of a **Gallery** control in horizontal/landscape orientation and at the top of a **Gallery** control in vertical/portrait orientation. Any changes that you make in the template are reflected throughout the **Gallery** control.

Predefined Gallery templates for showing images, text as well as a gallery with variable height items are available.

## Key properties
**[Default](properties-core.md)** – The item or record from the data source to be selected in the gallery when the app starts up.

**[Items](properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

**Selected** – The selected item.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe what the list of items are.

**AllItems** – All items in a gallery, including additional control values that are a part of the gallery's template.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**Layout** – Whether the user scrolls through a gallery or adjusts a slider top to bottom (**Vertical**) or left to right (**Horizontal**).

**NavigationStep** – How far a gallery scrolls if its **ShowNavigation** property is set to **true** and the user selects a navigation arrow at either end of that gallery.

**ShowNavigation** – Whether an arrow appears at each end of a gallery so that a user can scroll through the items in the gallery by clicking or tapping an arrow.

**ShowScrollbar** – Whether a scrollbar appears when the user hovers over a gallery.

**Snap** – Whether, when a user scrolls through a gallery, it automatically snaps so that the next item appears in full.

**TemplateFill** – The background color of a gallery.

**TemplatePadding** – The distance between items in a gallery.

**TemplateSize** – The height of the template for a gallery in vertical/portrait orientation or the width of the template for a gallery in horizontal/landscape orientation.

**Transition** – The visual effect (**Pop**, **Push**, or **None**) when the user hovers over an item in a gallery.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**WrapCount** – Number of items shown per row or column based on horizontal or vertical layout.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Filter**( *DataSource*, *Formula* )](../functions/function-filter-lookup.md)

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


## Accessibility guidelines
### Color contrast
If clicking anywhere in a gallery item is meant to select it, there must be adequate color contrast between:
* **[BorderColor](properties-color-border.md)** and the color outside the gallery (if there is a border)
* **[Fill](properties-color-border.md)** and the color outside the gallery (if there is no border)

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

    > [!NOTE]
  > Screen readers will annnouce when items in the gallery change. The **AccessibleLabel** is also mentioned. This gives context to the announcement and is even more important when there are multiple galleries on the same screen.

### Keyboard support
* Consider setting **ShowScrollbar** to **true**. On most touch screen devices, the scrollbar will not show until scrolling begins.
* If clicking anywhere in a gallery item is meant to select it, there must also be way for keyboard users to select the gallery item. For example, adding a **[Button](control-button.md)** that has its **OnSelect** property set to **Select(Parent)**.

    > [!NOTE]
  > Controls outside the gallery are not considered in the keyboard navigation order within the gallery. **[TabIndex](properties-accessibility.md)** of controls inside a gallery are scoped. See [accessibility properties](properties-accessibility.md) to learn more.
