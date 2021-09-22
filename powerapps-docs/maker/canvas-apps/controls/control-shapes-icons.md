---
title: Shape and Icon controls in Power Apps
description: Learn about the details, properties and examples of the Shape and Icon controls in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/25/2016
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---
# Shape and Icon controls in Power Apps
Graphics for which you can configure appearance and behavior properties.

## Description
These controls include arrows, geometric shapes, action icons, and symbols for which you can configure properties such as fill, size, and location. You can also configure their **[OnSelect](properties-core.md)** property so that the app responds if the user selects the control.

## Key properties (icons and shapes)
**[Fill](properties-color-border.md)** – The background color of a control.

**[OnSelect](properties-core.md)** – Actions to perform when the user selects a control.

## Key properties (icons only)

**Icon** - The type of icon to display (for example, **ArrowDown** or **ShoppingCart**). 

**Rotation** - The number of degrees to rotate the icon. 

**Color** - The color of the icon by name or RGBA values.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user selects that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user selects that control.

**[TabIndex](properties-accessibility.md)** – Keyboard-navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions

[**Navigate**( *ScreenName*, *ScreenTransition* )](../functions/function-navigate.md)

## Example

1. Name the default **[Screen](control-screen.md)** control **Target**, add a **[Label](control-text-box.md)** control, and set its **[Text](properties-core.md)** property to show **Target**.

    Don't know how to [add and configure a control](../add-configure-controls.md)?

1. Add a **[Screen](control-screen.md)** control, and name it **Source**.

1. In **Source**, add a **Shape** control, and set its **[OnSelect](properties-core.md)** property to this formula:

  `Navigate(Target, ScreenTransition.Fade)`
  
1. Press F5, and then select the **Shape** control.

    The **Target** screen appears.

1. (optional) Press Esc to return to the default workspace, add a **Shape** control to **Target**, and set the **[OnSelect](properties-core.md)** property of the **Shape** control to this formula:

  `Navigate(Source, ScreenTransition.Fade)`

## Accessibility guidelines

### Color contrast

The following applies only to graphics that are used as buttons or are otherwise not just for decoration.

For icons:
- **[Color](properties-color-border.md)** and **[Fill](properties-color-border.md)**
- Other [standard color contrast requirements](../accessible-apps-color.md) apply (if used as a button)

For shapes with borders:
- **[BorderColor](properties-color-border.md)** and the color outside the control
- **[FocusedBorderColor](properties-color-border.md)** and the color outside the control (if used as a button)

For shapes without borders:
- **[Fill](properties-color-border.md)** and the color outside the control
- **[PressedFill](properties-color-border.md)** and the color outside the control (if used as a button)
- **[HoverFill](properties-color-border.md)** and the color outside the control (if used as a button)

### Screen-reader support
- **[AccessibleLabel](properties-accessibility.md)** must be set for important graphics.

- If the graphic is for decoration or provides redundant information, leave **[AccessibleLabel](properties-accessibility.md)** empty or set it to the empty string **""** . Screen readers will ignore these graphics.

For example, you might place a **Lock** icon next to a **[Label](control-text-box.md)** that says **This form cannot be modified**. You don't need an **[AccessibleLabel](properties-accessibility.md)** for the icon because the **Label** already explains its meaning.

> [!IMPORTANT]
> When **[TabIndex](properties-accessibility.md)** is zero or greater, the icon or shape becomes a button. Its appearance doesn't change, but screen readers will treat it as a button. They will not ignore the control, even if **AccessibleLabel** is empty. When **[TabIndex](properties-accessibility.md)** is less than zero, screen readers treat the icon or shape as an image.

### Keyboard support
- **[TabIndex](properties-accessibility.md)** must be zero or greater if the graphic is used as a button. Keyboard users can then navigate to it.

- Focus indicators must be clearly visible if the graphic is used as a button. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this result.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]