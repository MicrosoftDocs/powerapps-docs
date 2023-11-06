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
# Progress bar modern control in Power Apps

Displays the progress, can be configured as determinate showcasing exact progress or indeterminate for ongoing progress.

## Description
The progress bar can be configured to show various states of progress in the apps. This versatile control can be used to inform users on their progress as they work on the app or can be used to show loading scenarios. 

## Key properties

**[OnChange](../properties-core.md)** – Actions to perform when the value of control gets updated.

**Value** – Number between 0 and 'max', which specifies how much of the task has been completed. Only applicable for determinate state.

**Max** - The maximum value, which indicates the task is complete. The ProgressBar bar will be full when value equals max. This is useful for instances where you want to show capacity, or how much of a total has been uploaded/downloaded.

**Thickness** – The thickness of the progress bar. Current options are only medium and large.

**Shape** – The shape of the bar and track. The shape property affects the corners of the bar. 

**Indeterminate** – Set the bar to determinate or indeterminate.

**ProgressColor** – For determinate state only, the color prop can be used to indicate a "brand" state (default), "error" state (red), "warning" state (orange), or "success" state (green). For indeterminate state, ProgressColor falls back to BasePaletteColor regardless of selected color.

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by selected Fluent theme.

## Additional properties
**Accessible label** – Label for screen readers.

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**Visible** - Whether a control appears or is hidden.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas.





