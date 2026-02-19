---
title: Link modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Link modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 02/18/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Link modern control in canvas apps

A clickable hyperlink control that navigates users to web URLs or triggers custom actions.

## Description

Use the **Link** control to create clickable hyperlinks in your canvas app. The control supports navigation to external websites, formatted text display, and customizable styling to match your app's design. Key properties for this control are **Text**, **Url**, and **Type**.

> [!NOTE]
> This article describes the Link modern control. For information about migrating from the previous version, see [Migrate to the Link modern control](link-migration.md).

> [!IMPORTANT]
> **Security:** The Link control validates the **Url** property to prevent cross-site scripting (XSS) attacks. URLs using the `javascript:` scheme or other unsafe protocols are blocked and will not navigate. Always use standard `https://` or `http://` URLs.

## General

**Text** – The display text shown for the hyperlink. This is the text users see and click on. Can be different from the actual URL.

**Url** – The web address to navigate to when the link is clicked. Must be a valid URL using `http://`, `https://`, or other safe protocols. URLs using `javascript:` or other unsafe schemes are blocked for security.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**Wrap** – Whether the text wraps to the next line when it exceeds the control width. When `true`, text wraps to multiple lines. When `false`, text is clipped or continues on a single line. Default is **true**.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **Edit** mode, the link is clickable. In **View** mode, it displays as text without being clickable.

## Size and position

**Align** – The horizontal alignment of text within the control. Accepts `Align` enum values:

| Value | Description |
|-------|-------------|
| `Align.Left` | Aligns text to the left edge (default) |
| `Align.Center` | Centers text horizontally |
| `Align.Right` | Aligns text to the right edge |
| `Align.Justify` | Stretches text to fill the full width |

**VerticalAlign** – The vertical alignment of text within the control. Accepts `VerticalAlign` enum values:

| Value | Description |
|-------|-------------|
| `VerticalAlign.Top` | Aligns text to the top |
| `VerticalAlign.Middle` | Centers text vertically (default) |
| `VerticalAlign.Bottom` | Aligns text to the bottom |

**AutoHeight** – Whether the control automatically increases its height when the text content exceeds the visible area.

**X** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**Y** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **150**.

**Height** – Distance between the control's top and bottom edges. Default is **32**.

**PaddingTop** – Distance between the text and the top edge of the control. Default is **5**.

**PaddingBottom** – Distance between the text and the bottom edge of the control. Default is **5**.

**PaddingLeft** – Distance between the text and the left edge of the control. Default is **5**.

**PaddingRight** – Distance between the text and the right edge of the control. Default is **5**.

## Style and theme

**Type** – The visual style of the link. Accepts `LinkAppearance` enum values:

| Value | Description |
|-------|-------------|
| `LinkAppearance.Default` | Standard link appearance with theme color (default) |
| `LinkAppearance.Subtle` | Subtle appearance with lighter styling |

**BasePaletteColor** – The base color used by the theme to generate the control's color palette. Changes this property to apply a different theme color to the control.

**Font** – The name of the font family in which text appears.

**Size** – The font size of the text, in points. Default is **15**.

**Color** – The color of the link text in the control.

**FontWeight** – The weight (thickness) of the text. Accepts `FontWeight` enum values:

| Value | Description |
|-------|-------------|
| `FontWeight.Bold` | Bold text |
| `FontWeight.Semibold` | Semibold text |
| `FontWeight.Normal` | Normal weight (default) |
| `FontWeight.Lighter` | Lighter weight |

**Italic** – Whether the text appears in italic style.

**Underline** – Whether a line appears under the text. Links typically have underlines by default.

**Strikethrough** – Whether a line appears through the middle of the text.

**Fill** – The background fill color of the control.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border. Accepts `BorderStyle` enum values: `BorderStyle.Solid`, `BorderStyle.Dashed`, `BorderStyle.Dotted`, or `BorderStyle.None`.

**BorderThickness** – The thickness of the control's border in pixels.

**RadiusTopLeft** – The corner radius for the top-left corner of the control.

**RadiusTopRight** – The corner radius for the top-right corner of the control.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of the control.

**RadiusBottomRight** – The corner radius for the bottom-right corner of the control.

## Accessibility

**AccessibleLabel** – A label for screen readers to announce what the link leads to. Should describe the destination or purpose of the link, not just "link".

**ContentLanguage** – The language used for the link text. Inherits from app settings if not specified.

## Example

The following YAML example shows link controls with different styling options:

```yaml
- DocumentationLink:
    Control: ModernLink@1.0.0
    Properties:
      Text: ="View Documentation"
      Url: ="https://docs.microsoft.com/powerapps"
      Type: =LinkAppearance.Default
      Size: =16
      FontWeight: =FontWeight.Semibold
      X: =40
      Y: =100
      Width: =200
      Height: =32

- SupportLink:
    Control: ModernLink@1.0.0
    Properties:
      Text: ="Contact Support"
      Url: ="https://support.microsoft.com"
      Type: =LinkAppearance.Subtle
      Size: =14
      X: =40
      Y: =150
      Width: =200
      Height: =32

- TermsLink:
    Control: ModernLink@1.0.0
    Properties:
      Text: ="Terms and Conditions"
      Url: ="https://company.com/terms"
      Type: =LinkAppearance.Subtle
      Size: =12
      Wrap: =false
      X: =40
      Y: =200
      Width: =150
      Height: =32
```

## What's new in this version

This new Link modern control includes the following improvements:

- **URL security validation**: The **Url** property now validates and sanitizes URLs to prevent XSS injection attacks. Direct `javascript:` URIs and other unsafe URLs are blocked, protecting your app and users from security vulnerabilities.
- **Font weight fixed**: The **FontWeight** property now correctly applies font weight changes. Previously, changes to this property were not reflected visually.
- **Wrap behavior fixed**: The **Wrap** property now correctly controls text wrapping. Previously, changing this property did not update the text display.
- **URL preview in edit mode**: When placing your cursor on the link control in edit mode, the URL is now properly displayed. This makes it easier to verify link destinations during app development.
- **Alt+Click to open**: In edit mode, you can now Alt+Click the link to open it in a browser. This allows you to test links without leaving the editor.
- **Simplified property organization**: Properties are now logically organized into **Data** and **Design** sections for better discoverability in the Advanced panel.
- **Default padding**: All padding properties now default to **5** pixels for consistent spacing.
- **LinkAppearance enum**: The **Type** property now uses the `LinkAppearance` enum with `Default` and `Subtle` options for clearer styling choices.

## Best practices

- **Clear link text**: Use descriptive text that tells users where the link leads. Avoid generic text like "click here" or "link".
- **Accessible labels**: Always provide descriptive **AccessibleLabel** text for screen readers that explains the link's destination.
- **URL validation**: Only use standard `https://` or `http://` URLs. The control blocks unsafe protocols for security.
- **Visual differentiation**: Use the **Type**, **Color**, or **Underline** properties to make links visually distinct from regular text.
- **Test navigation**: Use Alt+Click in edit mode to test that links navigate to the correct destinations.
- **Mobile tap targets**: Ensure links are large enough to tap easily on mobile devices (minimum 32x32 pixels height).

## Limitations

- The control blocks URLs using `javascript:` or other unsafe protocols for security reasons.
- Color changes for **LinkAppearance.Subtle** type may not apply correctly in the current version (being fixed).

## See also

- [Migrate to the Link modern control](link-migration.md)
- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
