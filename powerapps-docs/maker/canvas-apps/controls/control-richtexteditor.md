---
title: Rich text editor control in Power Apps
description: Learn about the details, properties, and examples of the Rich text editor control in Power Apps.
author: yogeshgupta698
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 04/17/2024
ms.subservice: canvas-maker
ms.author: yogupt
search.audienceType:
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  - tahoon-ms
---
# Rich text editor control in Power Apps
Allows end users to format text inside a WYSIWYG editing area.  Output format is HTML.

## Description
The **Rich text editor** control provides the app user a WYSIWYG editing area for formatting text.  Control's input and output format is HTML.

Control allows copied rich text (i.e from web browser or Word) to be pasted into the control.

Control's intended use is to format text and doesn't guarantee to preserve the integrity of the input HTML.  All script, style, object, and other potentially compromising tags will be removed by the editor.  This means that if rich text was created outside of Power Apps, it may not look the same as in the product where it was created.

Currently supported features include:
- Bold, Italic, Underline
- Text color, highlight Color
- Text Size
- Numbered lists, bullet lists
- Hyperlinks
- Clear formatting

To use the control inside a form, select the **Edit multi-line tex** card, and customize it by inserting the RTE control.

## Key properties
**[Default](properties-core.md)** – Input property for the initial text value shown in editor.

**HtmlText** – Output property for the resulting rich text in HTML format.


## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of the attachments.

**[DisplayMode](properties-core.md)** – Whether the control allows adding and deleting files (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**EnableSpellCheck** – Whether the browser spell checker is enabled. This functionality will provide spell checking only in the default language of the browser.  Power Apps for Windows doesn't support this property.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control is visible or hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (or screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (or screen, if no parent container).


## Accessibility guidelines
### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.

> [!TIP]
> Use **Alt+0** while the editor is focused to learn about other keyboard shortcuts.

> [!NOTE]
> When the toolbar is focused, **Tab** and **Shift+Tab** keys will navigate between toolbar groups. But you can't cycle back from the last group to the first group and vice versa.

## Limitations

You can only interact with the rich text editor control in Power Apps Studio when using the preview mode.

Pasting images in the rich text editor has the following limitations:
- Cross-Origin Resource Sharing (CORS)
- Authentication
- Image format support in browser
- Type of image (inline vs URL)
- When inserting an image, don't expect it to be automatically stored with the bound data source. A possible solution is to implement additional logic that uploads images from the rich text editor to the data source, processes the response, and then pastes it back into the original field. It's also important to understand that different programs may represent copied images in various ways.

> [!NOTE]
> Browsers represent image data differently, some browsers will capture the image as raw image data while others may get a reference to a URL which may not be accessible after pasting.

> [!TIP]
>  Using a screen clipping or screen shotting tool to copy / paste images will provide the best experience.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
