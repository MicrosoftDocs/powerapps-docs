---
title: Card modern control control in Power Apps
description: Learn about the details, properties, and examples of the card modern control in Power Apps.
author: yogeshgupta698 

ms.topic: reference
ms.component: canvas
ms.date: 1/13/2025
ms.subservice: canvas-maker
ms.author: yogupt


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - yogupt
     
---

# Card modern control (preview)

Cards help makers create clean, responsive object summaries such as contact tiles, document previews, or product listings in either horizontal or vertical orientation.

## Description
Use a Card when you want to show a concise overview of an item with optional imagery and text.  
The control adapts its layout to the sections a maker chooses to configure, enabling consistent patterns without requiring multiple independent controls.

## General

**Direction** – Determines whether the card layout is vertical or horizontal

**Title** – Header title text displayed at the top of the card  

**Subtitle** – Supplemental text displayed under or beside the title in the header 

**Description** – Description text displayed below the header of the card  

**Image** – Main preview image for the card  

**ImageAltText** – Alt text for the preview image for accessibility  

**HeaderImage** – Small avatar or icon displayed in the header with the title and subtitle  

**HeaderImageAltText** – Alt text for the header image  

**ImagePosition** – Determines whether the preview image appears before or after the header section  

## Behavior

**OnSelect** – Action triggered when the card is selected by the user  

**DisplayMode** – Controls whether the card is interactive, view‑only, or disabled  

**Visible** – Shows or hides the card  

## Style and theme

**Radius** – Controls corner roundness of the card container  

**DropShadow** – Defines the shadow style applied to the card  

## Size and position

**X, Y** – Position of the control on the canvas  

**Width, Height** – Dimensions of the control  

## Examples

Below are three example Card configurations you can copy and paste directly into your app configuration.

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
      Image: =
      LayoutDirection: =LayoutDirection.Horizontal
      Width: =300
      X: =40
      Y: =40
```

### **Vertical card with header on top***
```yaml
- VerticalCardwithHeaderOnTop:
    Control: ModernCard@1.0.0
    Properties:
      HeaderImage: =
      Height: =240
      ImagePlacement: =ImagePlacement.AfterHeader
      Subtitle: ="This is subtitle which can take whole of single line."
      Title: ="Title for the card"
      Width: =350
      X: =40
      Y: =40
```
