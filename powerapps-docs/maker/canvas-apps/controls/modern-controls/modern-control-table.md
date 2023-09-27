---
title: Table control in Power Apps
description: Learn about the details, properties, and examples of the modern Table control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 8/31/2023
ms.subservice: canvas-maker
ms.author: jasongre


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - jasongre
  
---
# Table modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A control that shows a set of data in a tabular or list format.

## Description
The **Table** control is a modern responsive control that shows a set of data in a tabular or list format. The tabular format includes column headings for each displayed field and a footer that provides details about the dataset such as the record count. The list format presents the data in a single column and has three fields for each row. As an app maker, you have full control over what fields are added to the control including the order. Although all added fields are visible in the tabular format, only the initial three fields appear in the narrower list format.

Similar to the **Gallery** and **Data** table controls, the **Table** maintains a **Selected** property that points to the selected row that can be used to link the **Table** control to other controls.

## Supported capabilities
- Data in a **Table** control is read-only.
- The tabular format offers a modern data browsing experience with infinite scroll, eliminating the need for paging buttons.
- The **Table** control only supports linking to Microsoft Dataverse tables.
- When you connect a **Table** control to a compatible connector such as Microsoft Dataverse, a predefined set of fields are displayed by default. You can also display or hide other fields based on your needs.
- The **Table** control can automatically switch between tabular and list formats. You can manually manage this behavior using the **Reflow** property.
- When you run your app, you can adjust column width in the **Table** control. However, your changes aren't saveontrol while you run the app. Your changes aren't saved.

### Unsupported capabilities
Currently, the listed capabilities aren't supported. However, since the **Table** control is still evolving, check back for any updates.

* You can't link to other connectors.
* Customize the style of the **Table** or modify individual columns.


## Key properties
**[Items](../properties-core.md)** - The source of data for the items that appear in the table. 

**Reflow behavior** - The default responsive behavior of the table. **Reflow** means the table displays in tabular form when the control is 480 or more pixels wide and transitions to a list format in narrower conditions. **GridOnly** (or **ListOnly**) means the table always displays in a tabular (or list) format regardless of the control width, and you can use Power Fx formulas to create your own breakpoints for defining the responsive behavior of the table.

**Selected** – The selected row in the **Table** control.

## Additional properties
**Allow range selection** – Whether users can select a portion of the table to copy its values. Default is Yes.

**[Visible](../properties-core.md)** - Whether a control appears or is hidden.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas.











