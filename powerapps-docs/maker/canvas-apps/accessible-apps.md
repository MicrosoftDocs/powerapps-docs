---
title: Create accessible canvas apps
description: How to make canvas apps accessible for people with disabilities
author: chmoncay
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/18/2021
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - chmoncay
  - tahoon-ms
  - tapanm-msft
---
# Create accessible canvas apps

An accessible canvas app will allow users with vision, hearing, and other impairments to successfully use the app.  In addition to being a requirement for many governments and organizations, following the below guidelines increases usability for all users, regardless of their abilities.

Use the **[Accessibility Checker](accessibility-checker.md)** to help review potential accessibility issues in your app. 

## Layout and color
Common sense and uncomplicated design helps apps be more accessible to all users.  When doing heavy customization of apps take note of the below suggestions. Power Apps themes are designed to meet accessibility standards.
- Ensure all elements are clearly visible and text is of sufficient size.  All content must be easily read and understood by the naked eye.
- Avoid using the visibility property of items to bring an element into view.  If you need to show something conditionally, create the content in a new screen and navigate to it and back.
- Ensure input elements are labeled on the screen. **[AccessibleLabel](controls/properties-accessibility.md)** property defines what the screen reader will announce.
- If customizing colors, ensure the contrast ratio of text to background is 4.5:1 or greater.  Software tools that assist this process are readily available.
- Ensure layout follows a logical flow when read top-bottom, left to right.

## Keyboard support
When testing your app's accessibility, ensure the app can be used with the keyboard only, the accessibility modes on iOS and Android, and keyboard-based screen readers.

For keyboard navigation (with or without the screen reader), ensure that a logical order is followed when using the TAB key to navigate to input fields by setting each control's **[TabIndex](controls/properties-accessibility.md)** property:
- Label, Image, Icon, Shape controls - if they represent interactive elements (i.e.buttons) set TabIndex to 0; if they are decorative elements or text, set TabIndex to -1.
- Avoid setting tab index higher than zero.

## Screen reader support
The following software combinations are the supported recommendations for consuming Power Apps with a screen reader:

- **Windows**: Microsoft Edge / Narrator
- **macOS**: Safari / VoiceOver
- **Android**: Power Apps app / Talkback
- **iOS**: Power Apps app / VoiceOver

To ensure a satisfying experience with the screen reader it is recommended to:

- Ensure all input controls have the **[AccessibleLabel](controls/properties-accessibility.md)** property set.
- For images set **[AccessibleLabel](controls/properties-accessibility.md)** to an appropriate description.
  - If a picture is not used as a button or a link (i.e. icon is there just for the decoration) and should not be read by the screen reader, make sure the **[AccessibleLabel](controls/properties-accessibility.md)** is empty or not set.
  - If a picture or an icon is used as a button, then set **[TabIndex](controls/properties-accessibility.md)** to 0 and **[AccessibleLabel](controls/properties-accessibility.md)** to the link description.

## Control type and structure
Using the right controls and grouping them will help screen reader users understand the structure of the app.

- Include at least one heading on each screen of the app. You can create headings by setting the **Role** property of a **[Label](controls/control-text-box.md)**.
- Use a **[Button](controls/control-button.md)** instead of a **[Label](controls/control-text-box.md)** for interactive text.
- Group related content in **[Containers](controls/control-container.md)**.
- Be aware of [unsupported design patterns](accessible-apps-limitations.md).

## Multimedia
Ensure all videos are captioned and a transcript of all audio recordings is available to the user.  **Video** control supports closed captions  in WebVTT format via the **ClosedCaptionsUrl** property.

With the screen reader enabled, **Timer** does not announce button text, but how much time has passed.  Announcements can't be turned off, even if timer is hidden with low opacity.

## Working with signatures
If you have a signature field that uses the PenInput control, you need to enable an alternative method of signature input.  The recommended way is to show a TextInput control where a user can type their name.  Ensure the signing instructions are placed in the **[AccessibleLabel](controls/properties-accessibility.md)** property and the control is placed close to the Pen input - to the right or immediately below.

## Next steps

[Accessible app structure](accessible-apps-structure.md)

### See also

- [Accessible colors in Power Apps](accessible-apps-color.md)
- [Show or hide content from assistive technologies for canvas apps](accessible-apps-content-visibility.md)
- [Announce dynamic changes with live regions for canvas apps](accessible-apps-live-regions.md)
- [Use the Accessibility checker](accessibility-checker.md)
- [Accessibility limitations in canvas apps](accessible-apps-limitations.md)
- [Accessibility properties](controls/properties-accessibility.md)
