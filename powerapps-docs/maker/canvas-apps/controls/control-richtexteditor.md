---
title: 'Rich text editor control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Rich text editor control
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/24/2018
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Rich text editor control (experimental) in PowerApps
An experimental  control that allows end users to format text inside a WYSIWYG editing area.  Output format is HTML.

## Description
The **Rich text editor** control provides the app user a WYSIWYG editing area for formatting text.  Control's input and output format is HTML.

Control allows copied rich text (i.e from web browser or Word) to be pasted into the control.  

Control's intended use is to format text and does not guarantee to preserve the integrity of the input HTML.  All script, style, object and other potentially compromising tags will be removed by the editor.  This means that if rich text was created outside of PowerApps, it may not look the same as in the product where it was created.

Currently supported features include:
- Bold, Italic, Underline
- Text color, highlight Color
- Text Size
- Numbered lists, bullet lists
- Hyperlinks
- Clear formatting

To use the control inside a form, select the "Edit multi-line text" card, and customize it by inserting the RTE control.

## Limitations
The current version of the control is experimental due to the following temporary limitations:
- Control has limited features for formatting text.  

- The control is primarily targeted for use in browsers on large screens.  Using the control on a mobile phone can be a frustrating experience.

- Known issues in the authoring  experience when using the Windows studio or Microsoft Edge browser.  Current recommendation is to use web studio in Chrome.


## Key properties
**[Default](properties-core.md)** – Input property for the initial text value shown in editor.

**HtmlText** – Output property for the resulting rich text in HTML format.



## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of the attachments.

**[DisplayMode](properties-core.md)** – Whether the control allows adding and deleting files (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control is visible or hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or screen, if no parent container).
