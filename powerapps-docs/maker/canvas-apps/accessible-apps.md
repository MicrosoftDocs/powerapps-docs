---
title: Creating Accessible Apps | Microsoft Docs
description: How to make apps accessible for people with disabilities
services: ''
suite: powerapps
documentationcenter: na
author: fikaradz
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 04/03/2018
ms.author: fikaradz

---
# Creating accessible apps
An accessible app will allow users with vision, hearing and other impairments to successfully use the app.  In addition to being a requirement for many governments and organizations, following the below guidelines increases usability for all users, regardless of their abilities.

### Layout and color
Common sense and uncomplicated design helps apps be more accessible to all users.  When doing heavy customization of apps take note of the below suggestions.  PowerApps themes are by default accessible.
- Ensure all elements are clearly visible and text is of sufficient size.  All content must be easily read and understood by the naked eye.
- Avoid using the visibility property of items to bring an element into view.  If you need to show something conditionally, create the content in a new screen and navigate to it and back.
- Ensure input elements are labeled on the screen. **[AccessibilityLabel](properties-accessibility.md)** property defines what the screen reader will announce.
- If customizing colors, ensure the contrast of text:background is 4.5:1 or greater.  Software tools that assist this process are readily available.
- Ensure layout follows a logical flow when read top-bottom, left to right.


### Keyboard support
When testing your app's accessibility, ensure the app can be used with the keyboard only, the accessibility modes on iOS and Android, as well as navigated successfully with the screen reader enabled.

For keyboard navigation (with or without the screen reader) test for the following:
- Ensure that a logical order is followed when using the TAB key to navigate to input fields by setting each control's **[TabIndex](properties-accessibility.md)** property.
- Label, Image, Icon, Shape - if they are interactive elementes (i.e.buttons) set TabIndex to 0; if they are decorative elements or text, set TabIndex to -1.
- Avoid setting tab index higher than zero.

### Screen reader support
The following software combinations are the supported recommendations for consuming PowerApps with a screen reader:

- **Windows**: Edge / Narrator
- **macOS**: Safari / VoiceOver
- **Android**: PowerApps app / Talkback
- **iOS**: PowerApps app / VoiceOver

To ensure a satisfying experience with the screen reader it is recommended to:

- Ensure all input controls have the **[AccessibilityLabel](properties-accessibility.md)** property set.
- For images set **[AccessibilityLabel](properties-accessibility.md)** to an appropriate description.
  - If a picture is not used as a button or a link (i.e. icon is there just for the decoration) and should not be read by the screen reader, make sure the **[AccessibilityLabel](properties-accessibility.md)** is empty or not set.
  - If a picture or an icon is used as a button, then set **[TabIndex](properties-accessibility.md)** to 0 and **[AccessibilityLabel](properties-accessibility.md)** to the link description.


### Multimedia
Ensure all videos are captioned and that a transcript of all audio recordings is available to the user.
- **Video** control suppports closed caption  in WebVTT format via the **ClosedCaptionsUrl** property.

Note that with the screen reader enabled, **Timer** does not announce button text, but how much time has passed.  Announcements can't be turned off, even if timer is hidden with low opacity.

### Working with signatures
If you have a signature field that uses the PenInput control you need to enable an alternative method of signature input.  The recommended way is to show a TextInput control where a user can type their name.  Ensure the signing instructions are placed in the **[AccessibilityLabel](properties-accessibility.md)** property and the control is placed close to the Pen input - to the right of it or immediately below.

### Limitations
- Cannot assign custom roles to controls.
- Cannot have dynamic notifications to screen readers
- No good way to group controls. Data cards or Gallery is a workaround.

Related:
**[Accessibility properties](properties-accessibility.md)**
