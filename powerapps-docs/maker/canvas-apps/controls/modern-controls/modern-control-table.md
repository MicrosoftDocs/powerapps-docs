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
# Table control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A control that shows a set of data in a tabular or list format.

## Description
The **Table** control is a modern responsiveness control that shows a set of data in a tabular or list format. The tabular format includes column headings for each displayed field and a footer that provides details about the dataset such as the record count. The list format presents the data in a single column and has three fields for each row. As an app maker, you have full control over what fields are added to the control including the order. Although all added fields are visible in the tabular format, only the initial three fields appear in the narrower list format.

Similar to the **Gallery** and **Data** table controls, the **Table** maintains a **Selected** property that points to the selected row which can be used to link the **Table** control to other controls.

## Supported capabilities
- Data in a **Table** control is read-only.
- Modern data browsing experience for the tabular format via infinite scroll (i.e. no paging buttons).
- The **Table** control only currently supports linking to Microsoft Dataverse entities. 
- A set of default fields appear in the **Table** control when you link it to a connector that has implemented this capability, such as the Microsoft Dataverse. You can then show or hide these fields and others as necessary.
- Automatic responsiveness behavior of the **Table** between the tabular and list formats. Use the **Reflow** property to manually control this behavior. 
- Adjust column widths in the **Table** control while you run the app, though your changes aren't saved.

### Unsupported capabilities
* Support for linking to other connectors.
* Customize the styling of the **Table** or individual columns.

## Key properties
**[Items](../properties-core.md)** - The source of data for the items that appear in the table. 

**Reflow behavior** - The default responsiveness behavior of the Table. **Reflow** means the Table displays in tabular form when the control is 480 or more pixels wide and transitions to a list format in narrower conditions. **GridOnly** (or **ListOnly**) mean the Table always displays in a tabular (or list) format regardless of the control width and can use Power Fx formula to create your own breakpoints for defining the responsiveness behavior of the Table.  

**Selected** – The selected row in the **Table** control.

## Additional properties
**Allow range selection** – Whether users can select a portion of the Table to copy its values. Default is Yes.

**[Visible](../properties-core.md)** - Whether a control appears or is hidden

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas.











