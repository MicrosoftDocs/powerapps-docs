---
title: 'Shape controls and icon controls: reference | Microsoft Docs'
description: Information, including properties and examples, about shape controls and icon controls
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/25/2016
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Shape controls and Icon controls in PowerApps
Graphics for which you can configure appearance and behavior properties.

## Description
These controls include arrows, geometric shapes, action icons, and symbols for which you can configure properties such as fill, size, and location. You can also configure their **[OnSelect](properties-core.md)** property so that the app responds if the user clicks or taps the control.

## Key properties
**[Fill](properties-color-border.md)** – The background color of a control.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions

[**Navigate**( *ScreenName*, *ScreenTransition* )](../functions/function-navigate.md)

## Example

1. Name the default **[Screen](control-screen.md)** control **Target**, add a **[Label](control-text-box.md)** control, and set its **[Text](properties-core.md)** property to show **Target**.

    Don't know how to [add and configure a control](../add-configure-controls.md)?

2. Add a **[Screen](control-screen.md)** control, and name it **Source**.
3. In **Source**, add a **Shape** control, and set its **[OnSelect](properties-core.md)** property to this formula:<br>**Navigate(Target, ScreenTransition.Fade)**
4. Press F5, and then click or tap the **Shape** control.

    The **Target** screen appears.

5. (optional) Press Esc to return to the default workspace, add a **Shape** control to **Target**, and set the **[OnSelect](properties-core.md)** property of the **Shape** control to this formula:
   <br>**Navigate(Source, ScreenTransition.Fade)**


## Accessibility guidelines

### Color contrast

The following applies only to graphics that are used as buttons or are otherwise not just for decoration.

For icons:
* **[Color](properties-color-border.md)** and **[Fill](properties-color-border.md)**
* Other [standard color contrast requirements](../accessible-apps-color.md) apply (if used as a button)

For shapes with borders:
* **[BorderColor](properties-color-border.md)** and the color outside the control
* **[FocusedBorderColor](properties-color-border.md)** and the color outside the control (if used as a button)

For shapes without borders:
* **[Fill](properties-color-border.md)** and the color outside the control
* **[PressedFill](properties-color-border.md)** and the color outside the control (if used as a button)
* **[HoverFill](properties-color-border.md)** and the color outside the control (if used as a button)

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present, if the graphic is used as a button or is otherwise not just for decoration.
* **[AccessibleLabel](properties-accessibility.md)** must be empty or the empty string **""**, if the graphic is purely for decoration. This causes screen readers to ignore the graphic.
* **[AccessibleLabel](properties-accessibility.md)** can be empty or the empty string **""**, if the graphic provides redundant information.

    For example, a **Settings** icon with its **[AccessibleLabel](properties-accessibility.md)** set to **Settings**. This icon is not used as a button. It is next to a **[Label](control-text-box.md)** that also says **Settings**. Screen readers will read the icon as **Settings**, and the label as **Settings** again. This is unnecessarily verbose. In this case, the icon does not need an **[AccessibleLabel](properties-accessibility.md)**.

    > [!IMPORTANT]
    > Screen readers will always read icons or shapes that have **[TabIndex](properties-accessibility.md)** of zero or greater, even if **[AccessibleLabel](properties-accessibility.md)** is empty. This is because they are rendered as buttons. If no **[AccessibleLabel](properties-accessibility.md)** is provided, screen readers will simply read the graphic as **button**.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater, if the graphic is used as a button. This allows keyboard users to navigate to it.
* Focus indicators must be clearly visible, if the graphic is used as a button. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.

    > [!NOTE]
  > When **[TabIndex](properties-accessibility.md)** is zero or greater, the icon or shape is rendered as a button. There is no change to the visual appearance, but screen readers will correctly identify the image as a button. When **[TabIndex](properties-accessibility.md)** is less than zero, the icon or shape is identified as an image.
