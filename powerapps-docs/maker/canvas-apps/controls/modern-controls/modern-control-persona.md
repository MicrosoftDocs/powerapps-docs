---
title: "Persona Modern Control in Canvas Apps: Properties and Examples"
description: "Discover how to use the Persona modern control in Power Apps canvas apps. Learn its identity, presence, layout, styling, accessibility behavior, and examples."
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 09/24/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
ai-usage: ai-generated
search.audienceType:
  - maker
contributors:
  - yogeshgupta698
---

# Persona modern control in canvas apps (Preview)

The **Persona** modern control displays a person's identity, profile image, supporting details, and presence in a canvas app.

> [!IMPORTANT]
> The Persona modern control is a preview feature. Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Description

Use the **Persona** control to display one person or entity. The control combines an avatar with up to three text lines and an optional presence badge. It displays **Image** when available and otherwise derives initials from **Name**. The control becomes interactive only when **OnSelect** contains a formula. Key properties are **Name**, **Caption**, **Details**, **Image**, and **Presence**.

Persona is a new control. Studio doesn't offer an upgrade action from another control.

## General

**Name** – The primary text line and the name used to derive avatar initials. The default is `User().FullName`.

**Caption** – The secondary text line. The default is `User().Email`.

**Details** – The third text line. The default is blank.

**Image** – The image displayed in the avatar. The default is `User().Image`. When the image is blank or unavailable, the avatar displays initials derived from **Name**.

**Presence** – The presence badge displayed on the avatar. Accepts `PresenceBadge` enum values:

| Value | Description |
|---|---|
| `PresenceBadge.Available` | Available status. |
| `PresenceBadge.Away` | Away status. |
| `PresenceBadge.Busy` | Busy status. |
| `PresenceBadge.'Do not disturb'` | Do-not-disturb status. |
| `PresenceBadge.Offline` | Offline status. |
| `PresenceBadge.'Out of office'` | Out-of-office status. |
| `PresenceBadge.Blocked` | Blocked status. |
| `PresenceBadge.Unknown` | Unknown status. |
| `PresenceBadge.None` | Hides the presence badge. Default. |

**OutOfOffice** – Whether the presence badge also indicates that the person is out of office. The default is `false`. This property has no visible effect when **Presence** is `PresenceBadge.None`.

**Visible** – Whether the control appears or is hidden.

## Behavior

**OnSelect** – Actions to perform when the user selects the Persona. When this property contains an active formula, the control uses button semantics and responds to Enter or Space while it has keyboard focus. When the property is blank, Persona is display-only.

**DisplayMode** – Whether the control allows interaction (**Edit**), only displays content (**View**), or is disabled (**Disabled**). When the control isn't interactive, **OnSelect** doesn't fire.

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. The default is **220**.

**Height** – Distance between the control's top and bottom edges. The default is **69**.

**Align** – The horizontal placement of the assembled avatar and text block within the control. Accepts `Align.Left` (default), `Align.Center`, `Align.Right`, or `Align.Justify`.

**VerticalAlign** – The vertical placement of the assembled avatar and text block. Accepts `VerticalAlign.Top`, `VerticalAlign.Middle` (default), or `VerticalAlign.Bottom`.

**TextPosition** – The position of the text block relative to the avatar. Accepts `PersonaTextPosition` enum values:

| Value | Description |
|---|---|
| `PersonaTextPosition.After` | Places text after the avatar. Default. |
| `PersonaTextPosition.Before` | Places text before the avatar. |
| `PersonaTextPosition.Below` | Places text below the avatar. |

**TextAlignment** – The alignment of the text lines relative to the avatar. Accepts `PersonaTextAlignment.Start` (default) or `PersonaTextAlignment.Center`.

**PaddingTop**, **PaddingRight**, **PaddingBottom**, **PaddingLeft** – The distance between the Persona content and each edge of the control.

## Style and theme

**Appearance** – The avatar color used when initials are displayed. Accepts `AvatarColor` enum values. The default is `AvatarColor.Brand`.

Available values are `Brand`, `DarkRed`, `Cranberry`, `Red`, `Pumpkin`, `Peach`, `Marigold`, `Gold`, `Brass`, `Brown`, `Forest`, `Seafoam`, `DarkGreen`, `LightTeal`, `Teal`, `Steel`, `Blue`, `RoyalBlue`, `Cornflower`, `Navy`, `Lavender`, `Purple`, `Grape`, `Lilac`, `Pink`, `Magenta`, `Plum`, `Beige`, `Mink`, `Platinum`, and `Anchor`. Use the `AvatarColor` prefix, for example `AvatarColor.Cornflower`.

**Shape** – The shape of the avatar. Accepts `AvatarShape.Circular` (default) or `AvatarShape.Square`.

**BasePaletteColor** – The base color used to derive the avatar palette when **Appearance** is `AvatarColor.Brand`.

**Font** – The font family used by the text lines and avatar initials.

**Size** – The inherited base font size. The default is **0**, which lets the control use its default text sizes.

**Color** – The inherited base text color. An individual line's color property overrides this value.

**NameColor**, **CaptionColor**, **DetailsColor** – The color of each text line. When blank, the line inherits **Color**.

**NameSize** – The font size of **Name**. The default is **16**.

**CaptionSize** – The font size of **Caption**. The default is **14**.

**DetailsSize** – The font size of **Details**. The default is **12**.

**FontWeight** – The weight of all three text lines. Accepts `FontWeight.Bold`, `FontWeight.Semibold`, `FontWeight.Normal`, or `FontWeight.Lighter`.

**Italic**, **Underline**, **Strikethrough** – Whether the text lines use the corresponding font style.

**LineHeight** – The line-height multiplier for the stacked text lines. When blank or `0`, the control derives line height from the font size.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border.

**BorderThickness** – The thickness of the control's border.

**RadiusTopLeft**, **RadiusTopRight**, **RadiusBottomLeft**, **RadiusBottomRight** – The radius of each corner of the control.

## Additional properties

**AccessibleLabel** – A label that screen readers read. When you leave it blank, the control derives a label from the visible text and presence status. For an interactive Persona, provide a label that describes the action.

**Tooltip** – Explanatory text shown on hover or focus. When text is truncated and no authored tooltip is present, the control can expose the full text in a tooltip.

**ContentLanguage** – The display language for the Persona content, if different from the app language.

## Accessibility

- A display-only Persona exposes image or group semantics instead of button semantics.
- A Persona with **OnSelect** uses button semantics and supports Enter and Space.
- The accessible label can include the visible identity text and localized presence status.
- Presence changes aren't announced as live-region updates, so routine status changes don't interrupt a screen reader.

## Example

The following self-contained YAML example displays a team member without requiring a connector, data source, variable, or another control:

```yaml
- TeamMemberPersona:
    Control: ModernPersona@1.2.0
    Properties:
      Name: ="Adele Vance"
      Caption: ="Product manager"
      Details: ="Available for review"
      Image: =Blank()
      Presence: =PresenceBadge.Available
      OutOfOffice: =false
      Appearance: =AvatarColor.Cornflower
      Shape: =AvatarShape.Circular
      TextPosition: =PersonaTextPosition.After
      TextAlignment: =PersonaTextAlignment.Start
      AccessibleLabel: ="Adele Vance, Product manager, available"
      Tooltip: ="Open Adele Vance's profile"
      OnSelect: =Notify("Adele Vance selected", NotificationType.Information)
```

## Limitations

- Persona displays a single identity. Use a gallery or an Avatar Group control to display multiple people.
- **Presence** and **OutOfOffice** are formula-driven display values. The control doesn't retrieve live presence from Microsoft Teams or Microsoft Graph.
- The control doesn't expose a selected person or another primary output because it doesn't own selection or editing state.
- Persona has no automatic upgrade path from another control.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Modern controls and properties](modern-controls-reference.md)
- [Size and location properties](../properties-size-location.md)
