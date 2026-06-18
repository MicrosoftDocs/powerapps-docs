---
title: Card modern control in Power Apps
description: Learn about the details, properties, and examples of the card modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.component: canvas
ms.date: 06/12/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - yogupt

---

# Card modern control

Cards help makers create clean, responsive object summaries such as contact tiles, document previews, or product listings in either horizontal or vertical orientation.

## Description

Use a Card when you want to show a concise overview of an item with optional imagery and text.
The control adapts its layout to the sections a maker chooses to configure, enabling consistent patterns without requiring multiple independent controls.

## General

**Direction** – Determines whether the card layout is vertical or horizontal

**Title** – Header title text displayed on the card

**Subtitle** – Supplemental text displayed under or beside the title in the header

**Description** – Description text displayed below the header of the card

**Image** – Main preview image for the card

**ImageAltText** – Alt text for the preview image for accessibility

**HeaderImage** – Small avatar or icon displayed in the header with the title and subtitle

**HeaderImageAltText** – Alt text for the header image

**ImagePosition** – Determines whether the preview image appears before or after the header section

## Behavior

**OnSelect** – Action triggered when the user selects the card

**DisplayMode** – Controls whether the card is interactive, view‑only, or disabled

**Visible** – Shows or hides the card

## Style and theme

**Fill** – The background fill color of the card. When set, text colors automatically adjust for contrast unless explicitly overridden.

**Radius** – Controls corner roundness of the card container

**DropShadow** – Defines the shadow style applied to the card

**TitleColor** – The font color of the title text. Overrides auto-contrast when explicitly set.

**SubtitleColor** – The font color of the subtitle text. Overrides auto-contrast when explicitly set.

**DescriptionColor** – The font color of the description text. Overrides auto-contrast when explicitly set.

**TitleSize** – The font size of the title text, in points.

**SubtitleSize** – The font size of the subtitle text, in points.

**DescriptionSize** – The font size of the description text, in points.

> [!NOTE]
> When you set a **Fill** color without explicitly setting text colors, the card automatically adjusts text to contrast with the background (black or white based on luminance). If you set an explicit color property such as **TitleColor**, it overrides the auto-contrast behavior for that text slot.

## Size and position

**X, Y** – Position of the control on the canvas

**Width, Height** – Dimensions of the control

## Examples

The following examples show three Card configurations you can copy and paste directly into your app configuration.

### **Vertical card with description**
```yaml
- VerticalCardwithDescription:
    Control: ModernCard@1.0.0
    Properties:
      Description: ="This is a sample description"
      Height: =240
      Width: =329
      X: =50
      Y: =45
```

### **Horizontal card with long description and no image**
```yaml
- HorizontalCardwithLongDescriptionNoImage:
    Control: ModernCard@1.0.0
    Properties:
      Description: ="This is a long description text. It provides a rich, narrative overview designed to help users understand the purpose, value, and key capabilities of the experience. This section typically expands beyond a short summary by offering contextual background, explaining how the feature solves real user problems, and detailing what makes it uniquely impactful."
      Height: =240
      Image: =Blank()
      LayoutDirection: =LayoutDirection.Horizontal
      Width: =300
      X: =40
      Y: =40
```

### **Vertical card with header on top**
```yaml
- VerticalCardwithHeaderOnTop:
    Control: ModernCard@1.0.0
    Properties:
      HeaderImage: =Blank()
      Height: =240
      ImagePlacement: =ImagePlacement.AfterHeader
      Subtitle: ="This is subtitle which can take whole of single line."
      Title: ="Title for the card"
      Width: =350
      X: =40
      Y: =40
```

### **Card with custom text styling**
```yaml
- StyledCard:
    Control: ModernCard@1.0.0
    Properties:
      Title: ="Featured Product"
      Subtitle: ="Limited time offer"
      Description: ="High quality item with premium features."
      Fill: =RGBA(0, 51, 102, 1)
      TitleColor: =RGBA(255, 255, 255, 1)
      SubtitleColor: =RGBA(200, 220, 255, 1)
      DescriptionColor: =RGBA(180, 200, 230, 1)
      TitleSize: =18
      SubtitleSize: =14
      DescriptionSize: =12
      Height: =240
      Width: =350
      X: =40
      Y: =40
```