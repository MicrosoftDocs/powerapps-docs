---
title: Button modern control in Power Apps
description: Learn about the details, properties and examples of the button modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 3/23/2023
ms.subservice: canvas-maker
ms.author: yogupt


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  
---
# Button modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A control that the user can select to interact with the app.

## Description
With the modern button you can set a button to be primary or secondary. Configure the **[OnSelect](../properties-core.md)** property of a **Button** control to run one or more formulas when the user selects the control. As a design pattern, we recommend always placing the primary button on the left, the secondary button to the right of it.

## Key properties
**[OnSelect](../properties-core.md)** – Actions to perform when the user taps or clicks a control.

**[Text](../properties-core.md)** – Text that appears on a component.

**Base palette color** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color.  

**Type** – Primary and Secondary. Primary emphasizes the button as a primary action. Secondary gives emphasis to the button in such a way that it indicates a secondary action.

**Display mode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

## Additional properties
**Accessible label** – Label for screen readers.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas.











