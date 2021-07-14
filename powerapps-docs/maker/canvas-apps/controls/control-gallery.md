---
title: Gallery control in Power Apps
description: Learn about the details, properties and examples of the gallery control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/11/2021
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType:
  - maker
search.app:
  - PowerApps
---
# Gallery control in Power Apps

A control that contains other controls and shows a set of data.

## Description

A **Gallery** control can show multiple records from a data source, and each record can contain multiple types of data. For example, use a **Gallery** control to show multiple contacts with each item showing contact information that includes a name, an address, and a phone number for each contact.

Each data field appears in a separate control within the **Gallery** control. And you can configure those controls in its template. The template appears as the first item inside the gallery:

- On the left edge of a **Gallery** control in horizontal/landscape orientation.
- And at the top of a **Gallery** control in vertical/portrait orientation. 

Any changes that you make in the template are reflected throughout the **Gallery** control.

Predefined templates for showing images and text in a gallery are available, and a gallery for variable-height items.

## Limitations

If a user scrolls the **Flexible height** gallery control before all items are loaded, the item that's currently in view may be pushed down and out of view when the data loading is finished. To avoid this issue, use a standard **Gallery** control instead of the **Flexible height** variant.

## Key properties

[Default](properties-core.md) – The item or record from the data source to be selected in the gallery when the app starts up.

[Items](properties-core.md) – The source of data that appears in a control such as a gallery, a list, or a chart.

**Selected** – The selected item.

## Additional properties

[AccessibleLabel](properties-accessibility.md) – Label of the gallery (not the items it contains) for screen readers. Should describe what the list of items are.

**AllItems** – All items in a gallery, including additional control values that are a part of the gallery's template.

[BorderColor](properties-color-border.md) – The color of a control's border.

[BorderStyle](properties-color-border.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

[BorderThickness](properties-color-border.md) – The thickness of a control's border.

**DelayItemLoading** - Delay loading of items (rows) until after the screen first loads.

[DisplayMode](properties-core.md) – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

[Fill](properties-color-border.md) – The background color of a control.

[Height](properties-size-location.md) – The distance between a control's top and bottom edges.

**ItemAccessibleLabel** – Label of each gallery item for screen readers. Should describe what each item is.

**LoadingSpinner** (**None**, **Controls** or **Data**) - When None, spinner will not be shown. When Controls | Data, spinner will be shown when a render pass occurs that results in visible empty rows.

**LoadingSpinnerColor** - The fill color of the loading spinner.  Default is set to BorderColor.

**NavigationStep** – How far a gallery scrolls if its **ShowNavigation** property is set to **true** and the user selects a navigation arrow at either end of that gallery.

**Selectable** – Whether gallery items can be selected. When set to **true**, screen readers identify the gallery as a selectable list. And you select an item by selecting it. When set to **false**, screen readers identify the gallery as a regular list, and selecting an item doesn't select it.

**ShowNavigation** – Whether an arrow appears at each end of a gallery so that a user can scroll through the items in the gallery by selecting an arrow.

**ShowScrollbar** – Whether a scrollbar appears when the user hovers over a gallery.

**TemplateFill** – The background color of a gallery.

**TemplatePadding** – The distance between items in a gallery.

**TemplateSize** – The height of the template for a gallery in vertical/portrait orientation. Or the width of the template for a gallery in horizontal/landscape orientation.

**Transition** – The visual effect (**Pop**, **Push**, or **None**) when the user hovers over an item in a gallery.

[Visible](properties-core.md) – Whether a control appears or is hidden.

[Width](properties-size-location.md) – The distance between a control's left and right edges.

**WrapCount** – Number of items shown per row or column based on horizontal or vertical layout.

[X](properties-size-location.md) – The distance between the left edge of a control and the left edge of its parent container or screen.

[Y](properties-size-location.md) – The distance between the top edge of a control and the top edge of the parent container or screen.

## Related functions

[Filter( *DataSource*, *Formula* )](../functions/function-filter-lookup.md)

[Reset( *Control* )](../functions/function-reset.md) - Resets your gallery back to its initial state. Initial state includes scrolling to the first item and selecting the first item or default if present. 

  > [!NOTE]
  > **Reset** control does not recursively reset all the children of the gallery.

## Examples

### Show and filter data

- [Show text](control-text-box.md#show-data-in-a-gallery)
- [Show images](control-image.md#show-a-set-of-images-from-a-data-source)
- [Filter data by selecting a list option](control-drop-down.md#examples)
- [Filter data by adjusting a slider](control-slider.md#example)

### Get data from the user

- [Get text](control-text-input.md#collect-data)
- [Get images](control-add-picture.md#add-images-to-an-image-gallery-control)
- [Get photos](control-camera.md#examples)
- [Get sounds](control-microphone.md#examples)
- [Get drawings](control-pen-input.md#create-a-set-of-images)

## Accessibility guidelines

### Color contrast

If clicking anywhere in a gallery item is meant to select it, there must be adequate color contrast between:

- [BorderColor](properties-color-border.md) and the color outside the gallery (if there is a border).
- [Fill](properties-color-border.md) and the color outside the gallery (if there's no border).

### Screen reader support

- [AccessibleLabel](properties-accessibility.md) must be present.

    > [!NOTE]
    > Screen readers will announce when items in the gallery change. The **AccessibleLabel** is also mentioned. This gives context to the announcement and is even more important when there are multiple galleries on the same screen.

- When a gallery item contains multiple controls, use **ItemAccessibleLabel** to show the contents of gallery items.

- Set the value of **Selectable** to **true** if you want users to select a gallery item. Otherwise, set that value to **false**.

- When a gallery item contains multiple controls, use **ItemAccessibleLabel** to provide a summary of the gallery item's contents.

- **Selectable** should be set appropriately, depending on whether users are meant to select a gallery item.

### Keyboard support

- Consider setting **ShowScrollbar** to **true**. On most touch screen devices, the scrollbar won't show until scrolling begins.
- If clicking anywhere in a gallery item is meant to select it, there must also be way for keyboard users to select the gallery item. For example, adding a [Button](control-button.md) that has its **OnSelect** property set to **Select(Parent)**.

    > [!NOTE]
  > Controls outside the gallery are not considered in the keyboard navigation order within the gallery. [TabIndex](properties-accessibility.md) controls inside a gallery are scoped. See [accessibility properties](properties-accessibility.md) to learn more.

### See also

[Use DelayItemLoading and Loading spinner to improve performance in Gallery](../performance-tips.md#use-delayitemloading-and-loading-spinner-to-improve-performance-in-gallery)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]