---
title: Progress bar modern control in Power Apps
description: Learn about the details, properties and examples of the progress bar modern control in Power Apps.
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
# Progress bar modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

Displays the progress, can be configured as determinate showcasing exact progress or indeterminate for ongoing progress.

## Description
The progress bar can be configured to show various states of progress in the apps. This versatile control can be used to inform users on their progress as they work on the app or can be used to show loading scenarios. 

## Key properties
**Thickness** – The thickness of the progress bar. 

**Shape** – The shape of the bar and track. The shape property affects the corners of the bar. 

**Indeterminate** – Set the bar to determinate or indeterminate.

**Color** – The color prop can be used to indicate a "brand" state (default), "error" state (red), "warning" state (orange), or "success" state (green).

**Base palette color** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. This property is on in effect if the **Color** property has a value of **None**.  

**Value** – A decimal number between 0 and 'max', which specifies how much of the task has been completed. Only applicable for determinate state.

**Max** - The maximum value, which indicates the task is complete. The ProgressBar bar will be full when value equals max. This is useful for instances where you want to show capacity, or how much of a total has been uploaded/downloaded.


## Additional properties
**Accessible label** – Label for screen readers.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas.





