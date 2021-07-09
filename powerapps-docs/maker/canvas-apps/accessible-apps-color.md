---
title: Accessible colors for canvas apps
description: Color-contrast guidelines for canvas apps in Power Apps
author: tahoon-ms
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/19/2021
ms.author: tahoon
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tahoon-ms
  - tapanm-msft
  - chmoncay
---
# Accessible colors for canvas apps

Colors used in a canvas app should be accessible to color-blind and low-vision users. All Power Apps themes are accessible by default. When modifying colors used in an app, follow these guidelines to ensure that they remain accessible. There are several tools available online which can help you identify color contrast issues.

## Minimum contrast for text
* Text and its background must have a contrast ratio of at least 4.5:1
* Large text must have a contrast ratio of at least 3:1
* Disabled text has no contrast requirements

In practical terms, all interactive controls must have adequate color contrast between:
* **[Color](controls/properties-color-border.md)** and **[Fill](controls/properties-color-border.md)**
* **[PressedColor](controls/properties-color-border.md)** and **[PressedFill](controls/properties-color-border.md)**
* **[HoverColor](controls/properties-color-border.md)** and **[HoverFill](controls/properties-color-border.md)**

## Minimum contrast for non-text
* Non-text components, such as icons and borders, must have a contrast ratio of at least 3:1 with the colors outside of them.
* Disabled and decorative components have no contrast requirements.

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

[Show or hide content from assistive technologies for canvas apps](accessible-apps-content-visibility.md)

### See also

- [Create accessible apps](accessible-apps.md)
- [Accessible app structure](accessible-apps-structure.md)
- [Announce dynamic changes with live regions for canvas apps](accessible-apps-live-regions.md)
- [Use the Accessibility checker](accessibility-checker.md)
- [Accessibility limitations in canvas apps](accessible-apps-limitations.md)
- [Accessibility properties](controls/properties-accessibility.md)
