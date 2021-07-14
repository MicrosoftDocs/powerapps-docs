---
title: Screen control in Power Apps
description: Learn about the details, properties and examples of the screen control in Power Apps.
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 09/14/2019
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Screen control in Power Apps

A UI element that contains one or more other controls in an app.

## Description

Most apps have multiple **Screen** controls that contain **[Label](control-text-box.md)** controls, **[Button](control-button.md)** controls, and other controls that show data and support navigation. For information about how to add a screen, reorder screens, and configure navigation, review [Add a screen](../add-screen-context-variables.md).

## Key properties

**[BackgroundImage](properties-visual.md)** – The name of an image file that appears in the background of a screen.

**[Fill](properties-color-border.md)** – The background color of a control.

## Additional properties

**Height** - The height of the screen. If the app is responsive ([**Scale to fit**](../set-aspect-ratio-portrait-landscape.md#change-screen-size-and-orientation) is **Off**) and the device on which the app is running is shorter than this property, the screen can scroll vertically.

**[ImagePosition](properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

**LoadingSpinner** (**None**, **Controls** or **Data**) - When None, spinner will not be shown. When Controls | Data, will show  spinner until all child controls at the screen level are visible. **Note. Nested controls are not considered.**

**LoadingSpinnerColor** - The fill color of the loading spinner.

**Name** - The name of the screen.

**OnHidden** – The behavior of an app when the user navigates away from a screen.

**OnVisible** – The behavior of an app when the user navigates to a screen.  Use this property to set up variables and preload data used by the screen.  Use the [**App.OnStart**](../functions/object-app.md#onstart-property) property for set up once when the app is started.

**Orientation** - The orientation of the screen. If its **Width** is greater than its **Height**, the orientation will be **Layout.Horizontal**; otherwise, it will be **Layout.Vertical**.

**Size** - A positive integer that classifies the size of the screen. The classification is determined by comparing the screen's **Width** property to the values in the [**App.SizeBreakpoints**](../functions/signals.md) property. The **ScreenSize** type consists of four values (**Small**, **Medium**, **Large**, and **ExtraLarge**) that correspond to the integers 1 through 4.

**Width** - The width of the screen. If the app is responsive ([**Scale to fit**](../set-aspect-ratio-portrait-landscape.md#change-screen-size-and-orientation) is **Off**) and the device on which the app is running is narrower than this property, the screen can scroll horizontally.

## Related functions

[**Distinct**( *DataSource*, *ColumnName* )](../functions/function-distinct.md)

## Example

1. Add a **[Radio](control-radio.md)** control, name it **ScreenFills**, and set its **[Items](properties-core.md)** property to this value:

    `["Red", "Green"]`

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Name the default **Screen** control **Source**, add another **Screen** control, and name it **Target**.

1. In **Source**, add a **[Shape](control-shapes-icons.md)** control (such as an arrow), and set its **[OnSelect](properties-core.md)** property to this formula:

    `Navigate(Target, ScreenTransition.Fade)`

    Want more information about the **[Navigate](../functions/function-navigate.md)** function or [other functions](../formula-reference.md)?

1. In **Target**, add a **[Shape](control-shapes-icons.md)** control (such as an arrow), and set its **[OnSelect](properties-core.md)** property to this formula:

    `Navigate(Source, ScreenTransition.Fade)`

1. Set the **[Fill](properties-color-border.md)** property of **Target** to this formula:

    `If("Red" in ScreenFills.Selected.Value, RGBA(255, 0, 0, 1), RGBA(54, 176, 75, 1))`

1. Select the **Source** screen and then, while holding down the Alt key, select either option in the **[Radio](control-radio.md)** control, and then select the **[Shape](control-shapes-icons.md)** control.

    **Target** appears in the color that you selected.

1. In **Target**, select the **[Shape](control-shapes-icons.md)** control to return to **Source**.

1. (optional) Select the other option in the **[Radio](control-radio.md)** control, and then select the **[Shape](control-shapes-icons.md)** control to confirm that **Target** appears in the other color.

1. (optional) Reorder the screens by hovering over **Target** in the left navigation bar, selecting the ellipsis that appears, and then selecting **Move up**.

    **Target** appears first when the user opens the app.

## Accessibility guidelines

### Color contrast

When the **Screen** is the effective background for text, there must be adequate color contrast between:

- **[Fill](properties-color-border.md)** and text
- **[BackgroundImage](properties-visual.md)** and text (if applicable)

For example, if a **Screen** contains a **[Label](control-text-box.md)** and the label has transparent fill, then the screen's **[Fill](properties-color-border.md)** effectively becomes the background color for the label.

In addition to text, consider checking color contrast with essential graphical objects like the star images in a **[Rating](control-rating.md)** control.

### Screen reader support

- There must be a meaningful name for each **Screen**. The screen name can be viewed and edited in the same way as other controls: in the tree view of the controls pane or in the header of the properties pane.

    > [!NOTE]
  > When a new **Screen** is loaded, screen readers will announce its name.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]