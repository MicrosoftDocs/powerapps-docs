---
title:  Best practices and recommendations when working with gallery in canvas apps
description: Best practices and recommendations when working with gallery in canvas apps.
author: tahoon-ms

ms.topic: best-practice
ms.custom: canvas
ms.date: 11/15/2023
ms.subservice: canvas-maker
ms.author: tahoon
search.audienceType: 
  - maker
---
# Best practices and recommendations

The **[Gallery](controls/control-gallery.md)** is the only control that can create other controls. It has its own [scope](/troubleshoot/power-platform/power-apps/isolate-and-troubleshoot-common-issues/isolate-canvas-app-issues#try-a-different-app-structure). These advanced features can lead to unexpected behavior if the **Gallery** isn't configured correctly. This article covers best practices and recommendations when you're working with **Galleries**.

## Don't change gallery items from within the gallery

It's easy to create unstable behavior if `OnChange` or `OnSelect` of child controls modifies the **Items** of the parent gallery. For example, a **Text input** in a gallery can have its `OnChange` property set to:

```power-fx
Patch(GalleryData, ThisItem, {Name: TextInput.Text})
``` 

This is usually fine. Most controls will only trigger `OnChange` when users change their value directly. However, these controls can cause issues because they also trigger OnChange when the system changes their value:

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

This expression updates a record in the gallery's data source that matches the current item's name. The change is to replace the `A` column of the record with a new table.

This causes an infinite loop. When the user changes the value of the **Combo box**, `OnChange` is triggered, which updates `GalleryData`, which changes `DefaultSelectedItems` (because `First(ThisItem.A)` refers to a new table), which triggers `OnChange` again, and so on.

To avoid infinite loops, you can use [modern controls](controls/modern-controls/overview-modern-controls.md) or other controls that don't trigger `OnChange` when their data changes.

### Slow performance from patching items

Even if you avoid unwanted loops, [patching](/power-platform/power-fx/reference/function-patch) or [updating](/power-platform/power-fx/reference/function-update-updateif) **Gallery** items can be slow if the **Gallery** has many items. The **Gallery** doesn't just update the rows associated with the changed records. In some cases, it reloads all items. This is because of the loosely structured nature of data sources. It can be difficult for the **Gallery** to know whether just a single record changed or the entire data source changed.

## Gallery.Selected can change unexpectedly

The **Selected** property of the **Gallery** is a moving target. It can change without user interaction when:

* **Gallery.Default** changes
* **Gallery.Items** changes
* Refreshing or updating data sources

This might not be desirable for your scenario. If you want a stable copy of the item that is selected by the user, consider storing it in a variable. For example, set the **OnSelect** property of the **Gallery** to a global variable `CurrentItem`:

```power-fx
Set(CurrentItem, Self.Selected)
```

You can then use `CurrentItem` in other parts of the app to refer to the most recent item selected by the user rather than by the system.

## Don't use Gallery.Selected in a child control's event

The **Selected** property of the **Gallery** changes when a user selects an item. However, this event isn't related to events of child controls. Referring to `Gallery.Selected` in a child control's events can lead to unexpected results.

For example, when a user selects a **Checkbox** in a **Gallery**, the following events occur:

* `Checkbox.OnSelect`
* `Checkbox.OnCheck`
* `Gallery.Selected` changes to the newly clicked row

The order of these events isn't fixed. This is a problem if `Checkbox.OnSelect` is set to:

```power-fx
Notify(Gallery.Selected.Name)
```

`Gallery.Selected` might still be referring to the previously selected row when `Checkbox.OnSelect` is executed.

To avoid timing issues, don't use `Gallery.Selected` in events. If you must, use `Gallery.OnSelect` to respond to changes to `Gallery.Selected`.

## Ensure that the Gallery knows the schema of its items

Setting `Gallery.Items` to a variable or output of a [Canvas component](create-component.md) can give unexpected results, depending on when the variable is set or changed.

**Galleries** need to know the schema of its **Items** when the app loads. A schema, also known as shape, is the name and type of columns in a data source. Consider this table:

```power-fx
[{A: "abc", B: 123}, {A: "def", B: 456}]
```

Its schema consists of a text column `A` and a number column `B`.

Most of the time, the **Gallery** can guess the schema of its **Items** from the data source and expressions used in the app. But if the **Items** property is set to the output of a **Canvas component** or **[Import](controls/control-export-import.md)** control, the **Gallery** can't determine its schema. The output table from these controls might not be available when the app loads and the schema might even change. The **Gallery** won't render any items when it doesn't know its schema.

The same issue might happen when **Items** is set to a variable that's not initialized when the app loads.

As a workaround, you can hint the expected schema to the Gallery with a variable. Set **App.OnStart** to:

```power-fx
If(false, Set(GalleryData, [{A: "abc", B: 123}]), Set(GalleryData, []))
```

This lets the system know the schema of the `GalleryData` table. Then, you can use `GalleryData` as the **Items** property of the **Gallery**. Change it to the actual data source when needed.

## Don't assume AllItems contains all items of its dataset
The [**AllItems** property](controls/control-gallery.md#additional-properties) are the items that are loaded into view in a gallery. It's not all items in **Items**. **AllItems** can change when the user scrolls the gallery to load more items. Typically, this property is used to get values of child controls when the user is interacting with them. Hence, **AllItems** is guaranteed to have loaded that item and it's safe to refer to it. Don't refer to an item in **AllItems** if you're not sure whether the user has seen it.

Similarly, [**AllItemsCount**](controls/control-gallery.md#additional-properties) is the number of items that are loaded into view in the gallery. It's not the total number of records in **Items**. To get the total records in **Items**, use `CountRows(<expression used for Items property>)`.

## Next steps
[Isolate issues in canvas apps](/troubleshoot/power-platform/power-apps/isolate-and-troubleshoot-common-issues/isolate-canvas-app-issues)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
