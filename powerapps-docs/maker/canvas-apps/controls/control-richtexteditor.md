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
Allows end users to format text inside a WYSIWYG editing area. Output format is HTML.

## Description
The **Rich text editor** control provides the app user a WYSIWYG editing area for formatting text.

Although the input and output format is HTML, the control is not a HTML editor. All script, style, object, and unsupported HTML elements and attributes are removed by the editor.

Currently supported features include:
- Bold, italic, and underline
- Text and highlight color
- Text size
- Numbered and bulleted lists
- Hyperlinks
- Clear formatting

To use the control inside a form, select the **Edit multi-line text** card, and customize it by inserting the RTE control.

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

### Appearance isn't guaranteed when working with other products
When rich text is used across different products, it may not look exactly the same.

- Users can paste rich text from web pages, Microsoft Word, and other apps. However, the appearance may differ depending on the capabilities of the device, browser, and external source. 
- Similarly, if rich text is created outside of canvas apps, it may look slightly different because built-in styles of the other app aren't present.
- If the canvas app is embedded in another app, the host app may override the styles of the rich text. For example, when a canvas app is used as a [custom page](../../model-driven-apps/model-app-page-overview.md) in a model-driven app, the host app removes list styles. Bulleted lists appear without bullet points in a custom app.

A different appearance can be desirable if rich text should adapt to the product where it's shown. For example, the primary font could be different in another product. Or the text color should be different when the user enables dark mode. For consistent appearance, compose rich text and display it in canvas apps only.

### Pasted images may not appear consistently
A pasted image may appear in a browser but not in a mobile app. Or it may appear intermittently or not at all. These are signs that the pasted image is not supported because of:

- Cross-Origin Resource Sharing (CORS). The image host blocks the image from loading on Power Apps.
- Authentication. The image is not publicly accessible and can only be accessed after logging into the image host.
- Image format support. Common image formats like jpg and png are supported but less common types may not be supported by the browser or device.

Images in rich text can be represented differently. Some browsers or devices copy the image as raw image data while others may copy the image's URL which may not be accessible for the reasons above.

> [!TIP]
>  Use a screen clipping or screenshot tool to copy and paste images for the best experience.

### When editing an app, Alt key doesn't allow interaction with the control
In [Power Apps Studio](../power-apps-studio.md), the keyboard shortcut of [Alt key for quick interaction](../keyboard-shortcuts#alternate-behavior.md) doesn't work. You can only interact with the rich text editor when [previewing the app](../power-apps-studio#preview.md).

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
