---
title: Best practices for using the Gallery control in canvas apps
description: Learn best practices and recommendations for configuring gallery controls correctly in canvas apps to avoid unexpected behavior and improve performance.
author: tahoon-ms

ms.topic: best-practice
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/11/2025
ms.subservice: canvas-maker
ms.author: tahoon
search.audienceType: 
  - maker
---
# Best practices for using the Gallery control in canvas apps

The **[Gallery](controls/control-gallery.md)** is the only control in canvas apps that can create other controls. It has its own [scope](/troubleshoot/power-platform/power-apps/isolate-and-troubleshoot-common-issues/isolate-canvas-app-issues#try-a-different-app-structure). These advanced features can lead to unexpected behavior when the **Gallery** isn't configured correctly. This article covers best practices and recommendations when you work with **Gallery** controls.

> [!TIP]
> Consider using [modern controls](controls/modern-controls/overview-modern-controls.md) in your gallery items where possible. Modern controls are designed to minimize common pitfalls like unintended `OnChange` triggers and provide better accessibility and styling options. You can also use [Copilot in Power Apps](ai-overview.md) to generate a gallery layout and data connection automatically.

## Don't change gallery items from within the gallery

It's easy to create unstable behavior if `OnChange` or `OnSelect` of child controls modifies the **Items** of the parent gallery. For example, a **Text input** in a gallery can have its `OnChange` property set to:

```power-fx
Patch(GalleryData, ThisItem, {Name: TextInput.Text})
``` 

This is usually fine. Most controls only trigger `OnChange` when users change their value directly. However, the following controls can cause issues because they also trigger `OnChange` when the *system* changes their value:

* **[Combo box](controls/control-combo-box.md)**
* **[Date picker](controls/control-date-picker.md)**
* **[Slider](controls/control-slider.md)**
* **[Toggle](controls/control-toggle.md)**

For example, when `ComboBox.DefaultSelectedItems` changes, it triggers `OnChange`. Consider a **Combo box** in a **Gallery** with `DefaultSelectedItems` set to `First(ThisItem.A)` and its `OnChange` property set to:

```power-fx
UpdateIf(GalleryData, Name = ThisItem.Name, {
    A: Table({
        B: First(Self.SelectedItems).B
    })
})
```

This expression updates a record in the gallery's data source that matches the current item's name, replacing the `A` column with a new table.

This causes an infinite loop. When the user changes the **Combo box** value, `OnChange` fires, which updates `GalleryData`, which changes `DefaultSelectedItems` (because `First(ThisItem.A)` refers to a new table), which triggers `OnChange` again—and so on.

To avoid infinite loops, use [modern controls](controls/modern-controls/overview-modern-controls.md) or other controls that don't trigger `OnChange` when their data changes.

### Slow performance from patching items

Even if you avoid unwanted loops, [patching](/power-platform/power-fx/reference/function-patch) or [updating](/power-platform/power-fx/reference/function-update-updateif) **Gallery** items can be slow if the gallery has many items. The **Gallery** doesn't just update the rows associated with the changed records—in some cases, it reloads all items. This happens because of the loosely structured nature of data sources, which makes it hard for the **Gallery** to determine whether a single record or the entire data source changed.

## Gallery.Selected can change unexpectedly

The **Selected** property of the **Gallery** is a moving target. It can change without user interaction when any of the following occur:

* **Gallery.Default** changes
* **Gallery.Items** changes
* Data sources are refreshed or updated

If you want a stable copy of the item the user selected, store it in a variable. For example, set the **OnSelect** property of the **Gallery** to:

```power-fx
Set(CurrentItem, Self.Selected)
```

Then use `CurrentItem` elsewhere in the app to refer to the most recently user-selected item, rather than the system-updated **Selected** property.

## Don't use Gallery.Selected in a child control's event

The **Selected** property of the **Gallery** changes when a user selects an item. However, this event isn't synchronized with child control events. Referring to `Gallery.Selected` in a child control's events can lead to unexpected results.

For example, when a user selects a **Checkbox** in a **Gallery**, the following events occur in an unspecified order:

* `Checkbox.OnSelect`
* `Checkbox.OnCheck`
* `Gallery.Selected` changes to the newly selected row

Because the order of these events isn't fixed, using `Gallery.Selected` in `Checkbox.OnSelect` might still refer to the previously selected row.

To avoid timing issues, don't use `Gallery.Selected` in child control events. If you must respond to changes in `Gallery.Selected`, use the **Gallery**'s own `OnSelect` event.

## Ensure that the Gallery knows the schema of its items

Setting `Gallery.Items` to a variable or the output of a [Canvas component](create-component.md) can produce unexpected results, depending on when the variable is set or changed.

**Galleries** must know the schema of their **Items** when the app loads. A schema (also called a *shape*) defines the name and type of columns in a data source. For example, this table:

```power-fx
[{A: "abc", B: 123}, {A: "def", B: 456}]
```

has a schema with a text column `A` and a number column `B`.

Most of the time, the **Gallery** can infer the schema from the data source and expressions used in the app. However, if the **Items** property is set to the output of a **Canvas component** or **[Import](controls/control-export-import.md)** control, the **Gallery** can't determine its schema at load time&mdash;the output table might not be available yet, and the schema might change. The **Gallery** won't render any items when it doesn't know its schema.

The same issue can occur when **Items** is set to a variable that isn't initialized when the app loads.

As a workaround, hint the expected schema to the **Gallery** using a variable. Set **App.OnStart** to:

```power-fx
If(false, Set(GalleryData, [{A: "abc", B: 123}]), Set(GalleryData, []))
```

This lets the system infer the schema of `GalleryData`. Set the **Items** property of the **Gallery** to `GalleryData`, then update it to the actual data source as needed.

## Don't assume AllItems contains all items of its dataset

The [**AllItems** property](controls/control-gallery.md#additional-properties) contains the items currently loaded into the visible area of the gallery&mdash;not all items in **Items**. **AllItems** can change as the user scrolls to load more items. Typically, this property is used to access values of child controls that the user is currently interacting with, which guarantees those items are loaded.

Don't refer to an item in **AllItems** if you're not sure whether the user has scrolled to that item.

Similarly, [**AllItemsCount**](controls/control-gallery.md#additional-properties) is the count of items loaded into view, not the total record count in **Items**. To get the total number of records in **Items**, use `CountRows(<expression used for Items property>)`.

## Next steps

- [Add a gallery to show a list of items](add-gallery.md)
- [Understand gallery dynamic sizing](gallery-dynamic-sizing.md)
- [Isolate issues in canvas apps](/troubleshoot/power-platform/power-apps/isolate-and-troubleshoot-common-issues/isolate-canvas-app-issues)
- [Overview of modern controls in canvas apps](controls/modern-controls/overview-modern-controls.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]