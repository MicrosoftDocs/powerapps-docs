---
title: Avatar Group modern control in canvas apps (preview) - Power Apps
description: Display a group of people or entities with the modern Avatar Group control in Power Apps canvas apps. Configure item fields, overflow, presence, and selection.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 11/02/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
ai-usage: ai-generated
search.audienceType:
  - maker
---

# Avatar Group modern control in canvas apps (preview)

Display several people or entities as avatars, with an overflow list for items that don't fit.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Description

Use **Avatar Group** to show team members, reviewers, or record owners in a compact space. Bind **Items** to a table, then map its columns with the **ItemName**, **ItemImage**, and other per-item properties. You can overlap the avatars or spread them out, show presence badges, and respond when a user selects a person.

The control doesn't look up people or presence automatically. Supply the names, images, and status values through your formulas.

## General

Use these properties to supply the records and map their fields.

| Property | Description |
| --- | --- |
| **Items** | The table of people or entities to display. Its column names aren't fixed; map your columns with the per-item properties. |
| **ItemName** | The name for each avatar. The default is `ThisItem.name`. The name supplies initials when no image or explicit initials are available. |
| **ItemImage** | A string containing the image reference for each avatar. The default is `ThisItem.image`. A blank or unresolved image falls back to initials or a generic avatar. |
| **ItemInitials** | Optional initials to use instead of deriving them from the name. The default is an empty string. |
| **ItemPresence** | A string representing each person's status. The default is `ThisItem.presence`. For more values, see [Presence values](#presence-values). |
| **ItemColor** | An optional named avatar color, such as `"red"`, `"blue"`, or `"gold"`. The default is `ThisItem.color`. A blank or unsupported value uses **Appearance**. This property accepts a string, not a Power Fx color value. |
| **ItemTooltip** | Tooltip text for each item. The default is `ThisItem.name`. |
| **Default** | An optional record from **Items** to select initially. Selection isn't required. |
| **Visible** | Whether the control appears or is hidden. |

The six **Item** properties evaluate in the scope of each record. For example, set **ItemName** to `ThisItem.DisplayName` when your table has a `DisplayName` column. Map every field you use; the control doesn't search other columns for a missing name.

### Presence values

Set **ShowPresence** to `true` to display badges. **ItemPresence** accepts the following strings:

| Value | Meaning |
| --- | --- |
| `"available"` | Available. |
| `"away"` | Away. |
| `"busy"` | Busy. |
| `"do-not-disturb"` | Do not disturb. |
| `"offline"` | Offline. |
| `"out-of-office"` | Out of office. |
| `"blocked"` | Blocked. |
| `"unknown"` | Unknown status. |

A blank or unsupported value displays no badge. Unlike the standalone Persona control's **Presence** property, **ItemPresence** is a string property, not a `PresenceBadge` enum property.

## Behavior and output

Use selection to identify a person and trigger an action.

| Property | Description |
| --- | --- |
| **Selected** | Output record for the selected item. It retains the columns from **Items**. For example, read `TeamAvatars.Selected.DisplayName`. |
| **OnSelect** | Optional actions to run when a user selects an avatar, including an item in the overflow list. Selection works in **Edit** mode even when this formula is blank. |
| **OnChange** | Actions to run when the control reports selection. For user activation, **Selected** updates first, followed by **OnSelect**, if configured, and then **OnChange**. Don't assume that activating the selected item again is ignored. |
| **DisplayMode** | `DisplayMode.Edit` allows selection and opening overflow. `DisplayMode.View` displays the group without selection or opening overflow. `DisplayMode.Disabled` prevents interaction and uses disabled styling. |

Use either **OnSelect** or **OnChange** for an action that should run once per activation, rather than putting the same action in both.

## Layout and style

Configure how the group fits into your screen.

| Property | Description |
| --- | --- |
| **Layout** | `AvatarGroupLayout.Stack` overlaps avatars and is the default. `AvatarGroupLayout.Spread` separates them. |
| **MaxInlineItems** | Maximum number of avatars to display before overflow. The default is `5`. Available width can reduce the number displayed. The overflow button doesn't count toward this maximum. |
| **AvatarSize** | Requested avatar diameter. The default is `32`, or `48` for phone layouts. Supported sizes are 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 72, 96, 120, and 128. Other values within this range round down to a supported size. |
| **Gap** | Space in pixels between avatars in `AvatarGroupLayout.Spread`. Leave it blank for automatic spacing based on **AvatarSize**, or set a nonnegative number, including `0`. It doesn't change overlap in `AvatarGroupLayout.Stack`. |
| **Shape** | `AvatarShape.Circular` (default), `AvatarShape.Rounded`, or `AvatarShape.Square`. |
| **Appearance** | Default avatar color, using the `AvatarColor` enum. Examples include `AvatarColor.Brand` (default), `AvatarColor.Red`, and `AvatarColor.Blue`. A valid **ItemColor** overrides it for that item. |
| **BasePaletteColor** | Customizes avatars that use the Brand appearance. Explicit named item colors keep their own colors. |
| **ShowPresence** | Whether to show each item's valid presence badge. The default is `true`. |
| **OverflowIndicator** | `AvatarGroupOverflowIndicator.Count` (default) displays a count. `AvatarGroupOverflowIndicator.Icon` displays an icon. `AvatarGroupOverflowIndicator.Auto` uses an icon below avatar size 24 and a count at larger sizes. |
| **PaddingTop**, **PaddingRight**, **PaddingBottom**, **PaddingLeft** | Space around the group. Blank horizontal padding doesn't add implicit space. New phone instances use `0` for top and bottom padding and `8` for left and right padding. |
| **BorderColor**, **BorderStyle**, **BorderThickness** | Color, style, and thickness of the group's outer border. Set the style and thickness to show a border. |
| **RadiusTopLeft**, **RadiusTopRight**, **RadiusBottomLeft**, **RadiusBottomRight** | Corner radii of the group's outer frame. Use **Shape**, not these properties, to change individual avatars. |

The overflow list shows additional items in pages of up to 20 records.

## Size, position, and accessibility

Set **X**, **Y**, **Width**, and **Height** to position and size the control. The default desktop dimensions are 300 × 64; the phone defaults are 224 × 48. Increasing the control's width can make more avatars fit, up to **MaxInlineItems**. In Spread layout, increasing **Gap** can move more avatars into overflow.

**AccessibleLabel** – A screen-reader label describing the group, such as `"Project reviewers"`.

**OverflowButtonLabel** – Optional screen-reader label for the overflow button, such as `"Show more reviewers"`.

**Tooltip** – Explanatory text for the group. Use **ItemTooltip** for individual people.

**ContentLanguage** – The language of the control's content, if different from the app language.

## Example

This example defines its own table of seven people, so it doesn't require a data connection, collection, or another control. It maps all six per-item fields, shows up to two avatars inline, and displays the selected person's name in a notification.

Use the following YAML in a canvas app that supports `ModernAvatarGroup@1.3.0`:

```yaml
- TeamAvatars:
    Control: ModernAvatarGroup@1.3.0
    Properties:
      Items: |-
        =Table(
            {DisplayName: "Malik Johnson", Photo: "", Initials: "MJ", Status: "available", AvatarColorName: "blue", Hint: "Project owner"},
            {DisplayName: "Sam Cantrell", Photo: "", Initials: "SC", Status: "busy", AvatarColorName: "gold", Hint: "Reviewer"},
            {DisplayName: "Maria Sullivan", Photo: "", Initials: "MS", Status: "away", AvatarColorName: "", Hint: "Reviewer"},
            {DisplayName: "Henry Ross", Photo: "", Initials: "HR", Status: "do-not-disturb", AvatarColorName: "red", Hint: "Contributor"},
            {DisplayName: "Quinn Santiago", Photo: "", Initials: "QS", Status: "offline", AvatarColorName: "pink", Hint: "Contributor"},
            {DisplayName: "Darius Franklin", Photo: "", Initials: "DF", Status: "available", AvatarColorName: "forest", Hint: "Reviewer"},
            {DisplayName: "Hannah Jarvis", Photo: "", Initials: "HJ", Status: "busy", AvatarColorName: "purple", Hint: "Reviewer"}
        )
      ItemName: =ThisItem.DisplayName
      ItemImage: =ThisItem.Photo
      ItemInitials: =ThisItem.Initials
      ItemPresence: =ThisItem.Status
      ItemColor: =ThisItem.AvatarColorName
      ItemTooltip: =ThisItem.Hint
      Layout: =AvatarGroupLayout.Stack
      MaxInlineItems: =2
      AvatarSize: =40
      Shape: =AvatarShape.Circular
      Appearance: =AvatarColor.Brand
      ShowPresence: =true
      OverflowIndicator: =AvatarGroupOverflowIndicator.Count
      AccessibleLabel: ="Project reviewers"
      OverflowButtonLabel: ="Show more reviewers"
      DisplayMode: =DisplayMode.Edit
      Width: =300
      Height: =64
      OnSelect: =Notify(Self.Selected.DisplayName, NotificationType.Information)
```

Run the app, select an avatar, and confirm the notification uses that person's name. Open the overflow button to select one of the remaining people. Change **Layout** to `AvatarGroupLayout.Spread` to compare the layouts.

## Limitations

- The control supports one selected record, not multiple selection.
- **View** and **Disabled** modes don't open the overflow list. Don't use overflow as the only way to expose essential information in a read-only screen.
- Presence reflects the values your app supplies; the control doesn't establish a live presence connection.

## Related information

- [Avatar modern control](modern-control-avatar.md).
- [Persona modern control](modern-control-persona.md).
- [Modern controls overview](overview-modern-controls.md).
- [Size and location properties](../properties-size-location.md).
