---
title: 'Screen control: reference | Microsoft Docs'
description: Information, including properties and examples, about a Screen control
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/25/2016
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Screen control in PowerApps

A UI element that contains one or more other controls in an app.

## Description

Most apps have multiple **Screen** controls that contain **[Label](control-text-box.md)** controls, **[Button](control-button.md)** controls, and other controls that show data and support navigation. For information about how to add a screen, reorder screens, and configure navigation, review [Add a screen](../add-screen-context-variables.md).

## Key properties

**[BackgroundImage](properties-visual.md)** – The name of an image file that appears in the background of a screen.

**[Fill](properties-color-border.md)** – The background color of a control.

## Additional properties

**[ImagePosition](properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

**OnHidden** – The behavior of an app when the user navigates away from a screen.

**OnVisible** – The behavior of an app when the user navigates to a screen.

**OnStart** – The behavior of the app when the user opens the app.

- The formula to which this property is set runs before the first screen of the app appears. Call the [**Navigate**](../functions/function-navigate.md) function to change which screen appears first when the app starts.
- You can't set [context variables](../working-with-variables.md) with the [**UpdateContext**](../functions/function-updatecontext.md) function because no screen has appeared yet. However, you can pass context variables in the **Navigate** function and create and fill a [collection](../working-with-variables.md) by using the [**Collect**](../functions/function-clear-collect-clearcollect.md) function.
- When you update an app, the formula to which this property is set runs when the app is loaded into PowerApps Studio. To see the impact of changing this property, you'll need to save, close, and reload your app.
- The **OnStart** property is actually a property of the app, not the screen. For editing convenience, you view and modify it as a property on the first screen of your app. If you remove the first screen or reorder screens, this property may become hard to find. In this case, save, close, and reload your app, and the property will reappear as a property of the first screen.

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
