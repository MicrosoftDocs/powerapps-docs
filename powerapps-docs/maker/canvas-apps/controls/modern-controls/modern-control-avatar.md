---
title: "Avatar Modern Control in Canvas Apps: Properties and Examples"
description: "Discover how to use the Avatar modern control in Power Apps canvas apps. Learn key properties, presence badges, styling options, and examples to represent users and entities."
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 08/24/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
search.audienceType:
  - maker
contributors:
  - jasongre
  - yogeshgupta698
---

# Avatar modern control in canvas apps

A control that shows a visual representation of a user, team, or entity, with an optional presence badge.

## Description

Use the **Avatar** modern control to visually represent a user, team, or entity. The control displays the image supplied in **Image**, falls back to initials derived from **Name**, and shows a generic person icon when neither value is available. You can also show a presence badge and, in the updated version, make the avatar respond to selection. Key properties for this control are **Name**, **Image**, and **Badge**.

> [!NOTE]
> This article describes the updated Avatar modern control. For information about what changed from the previous version, see [Recent updates](#recent-updates).

## General

**Name** – The name of the person or entity. The control uses this value to determine the initials that appear when there's no image, and for accessibility. The default is `User().FullName`.

**Image** – The visual representation for the person or entity. Accepts image URLs, data URIs, and Power Apps image references. The default is `User().Image`.

**Badge** – A small visual decoration added to convey the status of the person or entity. Accepts `PresenceBadge` enum values. Use a blank value when no badge should appear.

| Value | Description |
|-------|-------------|
| `PresenceBadge.Available` | The person is available. |
| `PresenceBadge.Busy` | The person is busy. |
| `PresenceBadge.DoNotDisturb` | The person doesn't want to be disturbed. |
| `PresenceBadge.Away` | The person is away. |
| `PresenceBadge.Offline` | The person is offline. |
| `PresenceBadge.OutOfOffice` | The person is out of office. |
| `PresenceBadge.Unknown` | The status is unknown. |

**Visible** – Whether the control appears or is hidden.

## Behavior

**OnSelect** – Actions to perform when the user selects the avatar. When this property contains an active formula, the avatar becomes interactive and renders with button semantics, so it responds to Enter or Space while it has keyboard focus. When the property is blank, the avatar is display-only.

**DisplayMode** – Whether the control allows interaction (**Edit**), only displays content (**View**), or is disabled (**Disabled**). When **Disabled** and **OnSelect** is set, the avatar is dimmed and **OnSelect** doesn't fire.

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **64**.

**Height** – Distance between the control's top and bottom edges. Default is **64**.

## Style and theme

**Shape** – Whether the avatar appears with a circular or square shape. Accepts `AvatarShape` enum values: `AvatarShape.Circular` (default) or `AvatarShape.Square`.

**Appearance** – An avatar can have portions of itself styled for greater emphasis or to be subtle. The following options are available:

- **Brand**: Uses the modern theme to style the avatar. Use the **BasePaletteColor** property to override this color scheme.
- **Neutral**: Uses a grayscale for the initials background to provide a subtle appearance.
- **Colorful**: Uses a color from a predefined set of colors, based on a hash of the provided **Name**.

**BasePaletteColor** – The color palette applied to a control. This property impacts all surfaces of the control that render a theme color. If the value is null or zero, the color is driven by the selected Fluent theme.

**Font** – The name of the family of fonts in which the initials appear.

**Size** – The font size of the initials. If the value is null or zero, the font size is driven by the avatar dimensions.

**Color** – The color of the initials. If not set, the control chooses a contrasting color based on **Appearance**.

**FontWeight** – The weight of the initials. Accepts `FontWeight` enum values: `FontWeight.Bold`, `FontWeight.Semibold`, `FontWeight.Normal` (default), or `FontWeight.Lighter`.

**Italic** – Whether the initials appear in italic style.

**Underline** – Whether a line appears under the initials.

**Strikethrough** – Whether a line appears through the initials.

## Additional properties

**AccessibleLabel** – Label read by screen readers. When not set, the control uses the **Name** value. When **OnSelect** is set, describe the action, for example `"Open profile for " & User().FullName`.

**Tooltip** – Explanatory text that appears when the user hovers over the control.

**ContentLanguage** – The display language for the control content, if different from the app language.

## Example

The following YAML example shows the current user's avatar with a presence badge, and a second avatar that opens a profile screen when selected:

```yaml
- CurrentUserAvatar:
    Control: ModernAvatar@1.0.0
    Properties:
      Name: =User().FullName
      Image: =User().Image
      Badge: =PresenceBadge.Available
      Shape: =AvatarShape.Circular
      Appearance: ="Brand"
      Tooltip: =User().FullName
      Width: =64
      Height: =64

- EmployeeAvatar:
    Control: ModernAvatar@1.0.0
    Properties:
      Name: =ThisItem.FullName
      Image: =ThisItem.Photo
      Badge: =PresenceBadge.Away
      Shape: =AvatarShape.Square
      Appearance: ="Colorful"
      AccessibleLabel: ="Open profile for " & ThisItem.FullName
      OnSelect: =Navigate(ProfileScreen)
      Width: =48
      Height: =48
```

## Recent updates

The updated version of the **Avatar** modern control includes the following improvements and behavior changes.

### Property renames

The following properties are renamed. Update any formulas in your app that reference the old property names.

| Previous property | New property |
|---|---|
| `FontSize` | `Size` |
| `FontColor` | `Color` |
| `FontItalic` | `Italic` |
| `FontUnderline` | `Underline` |
| `FontStrikethrough` | `Strikethrough` |

### Removed properties

| Removed property | Notes |
|---|---|
| `Out of office` | Removed. Use `Badge = PresenceBadge.OutOfOffice` to show the out-of-office presence instead. |

### Bug fixes and improvements

- **Updated enums**: `Badge` and `Shape` now use typed Power Fx enums (`PresenceBadge` and `AvatarShape`) instead of string values, improving IntelliSense and reducing formula errors. `FontWeight` uses the `FontWeight` enum.
- **OnSelect support**: The avatar can now trigger actions when selected. When `OnSelect` is set, the control renders with button semantics and is fully accessible via keyboard and screen readers.
- **Tooltip support**: New `Tooltip` property shows explanatory text on hover.
- **Full font control**: Font properties are now consistent with other modern controls. Use `Font`, `Size`, `Color`, `Italic`, `Underline`, and `Strikethrough`.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Recent updates to modern controls](modern-control-updates.md)
- [Size and location properties](../properties-size-location.md)
