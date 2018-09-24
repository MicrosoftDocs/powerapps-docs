---
title: Accessible colors in canvas apps | Microsoft Docs
description: Color-contrast guidelines for canvas apps in PowerApps
author: tahoon
manager: kvivek
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer: anneta
ms.date: 04/23/2018
ms.author: tahoon
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Accessible colors for canvas apps in PowerApps
Colors used in a canvas app should be accessible to color-blind and low-vision users. All PowerApps themes are accessible by default. When modifying colors used in an app, follow these guidelines to ensure that they remain accessible. There are several tools available online which can help you identify color contrast issues.

## Minimum contrast for text
* Text and its background must have a contrast ratio of at least 4.5:1
* Large text must have a contrast ratio of at least 3:1
* Disabled text has no contrast requirements

In practical terms, all interactive controls must have adequate color contrast between:
* **[Color](controls/properties-color-border.md)** and **[Fill](controls/properties-color-border.md)**
* **[PressedColor](controls/properties-color-border.md)** and **[PressedFill](controls/properties-color-border.md)**
* **[HoverColor](controls/properties-color-border.md)** and **[HoverFill](controls/properties-color-border.md)**

## Minimum contrast for non-text

> [!NOTE]
> In the [WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html) standard, contrast requirements only applies to text. For greater accessibility, consider the upcoming [WCAG 2.1 contrast guidelines](https://www.w3.org/TR/WCAG21/#non-text-contrast) for essential user interface components like icon buttons. A minimum ratio of 3:1 is recommended for these components. The guidelines descibed in this section are **optional** for WCAG 2.0 compliance.

### User interface components
All interactive controls must have adequate color contrast between:
* **[FocusedBorderColor](controls/properties-color-border.md)** and color outside the control

Additional color contrast checks apply for controls where the entire area is interactive or informative. For example, a **[Button](controls/control-button.md)** or an **[Icon](controls/control-shapes-icons.md)** used as a button. This ensures that the boundaries of the control are clear and users know where they can click or tap.

If there is a border for such controls, there should be adequate color contrast between:
* **[BorderColor](controls/properties-color-border.md)** and color outside the control
* **[PressedBorderColor](controls/properties-color-border.md)** and color outside the control
* **[HoverBorderColor](controls/properties-color-border.md)** and color outside the control

If there is no border, there should be adequate color contrast between:
* **[Fill](controls/properties-color-border.md)** and color outside the control
* **[PressedFill](controls/properties-color-border.md)** and color outside the control
* **[HoverFill](controls/properties-color-border.md)** and color outside the control

### Graphical objects
If an image conveys important information, consider checking it for contrast issues. This applies to controls where an image can be shown: **[Audio](controls/control-audio-video.md)**, **[Image](controls/control-image.md)**, **[Microphone](controls/control-microphone.md)**, and **[Video](controls/control-audio-video.md)**.

For video content, consider checking it for contrast issues. Alternatively or additionally, provide [closed captions](controls/control-audio-video.md) that describe the video.

## Provide other visual cues
Ensure that the app does not convey information with just color. For example, users with red-green color blindness will not be able to distinguish a red error message from a green success message.

Additional cues like an **[Icon](controls/control-shapes-icons.md)** or text styles like **[Italic](controls/properties-text.md)** and **[Underline](controls/properties-text.md)** can help convey meaning.

## Next steps
Learn about [accessibility properties](controls/properties-accessibility.md) in PowerApps controls and try [using the Accessibility checker](accessibility-checker.md).
