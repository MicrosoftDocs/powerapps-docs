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

**Type** – Primary and Secondary. Primary emphasizes the button as a primary action. Secondary gives emphasis to the button in such a way that it indicates a secondary action.

**Display mode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

## Adding icon to button control
Button control is now enhanced to support subset of fluent icons. We have introduced below properties:

**Icon** - Allows the inclusion of Fluent icons within the button for visual enhancement. In properties panel, you can select the icon through dropdown menu showcasing available icons:
> [!div class="mx-imgBorder"]
> ![List of icons](media/Icons-List.png)

**Layout** - Defines the positioning of the icon in relation to the text on the button or no icon at all.

**Icon Rotation** - Provides the ability to rotate the icon to a desired orientation.

**Icon Style** - Provides option for icon to be rendered in filled or outline state.

## Additional properties
**Accessible label** – Label for screen readers.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas.











