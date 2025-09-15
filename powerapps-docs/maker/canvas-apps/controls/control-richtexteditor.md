---
title: Rich text editor control in Power Apps
description: Learn about the details, properties, and examples of the Rich text editor control in Power Apps.
author: yogeshgupta698
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 09/15/2025
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
Let users format text in a WYSIWYG editing area. The output format is HTML.

## Description
The **Rich text editor** control lets the app user format text in a WYSIWYG editing area.

The input and output format is HTML, but the control isn't an HTML editor. The editor removes script, style, object, and unsupported HTML elements and attributes.

Supported features include:
- Bold, italic, and underline
- Text and highlight color
- Text size
- Numbered and bulleted lists
- Hyperlinks
- Clear formatting

To use the control in a form, select the **Edit multi-line text** card, then customize it by inserting the RTE control.

## Key properties
**[Default](properties-core.md)** – Input property for the initial text value shown in the editor

**HtmlText** – Output property for the resulting rich text in HTML format


## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of the attachments.

**[DisplayMode](properties-core.md)** – Whether the control lets you add and delete files (**Edit**), only shows data (**View**), or is disabled (**Disabled**).

**EnableSpellCheck** – Whether the browser spell checker is enabled. This feature only checks spelling in the browser's default language. Power Apps for Windows doesn't support this property.

**[Height](properties-size-location.md)** – The distance from the control's top edge to its bottom edge.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control is visible or hidden.

**[Width](properties-size-location.md)** – The distance from the control's left edge to its right edge.

**[X](properties-size-location.md)** – The distance from the control's left edge to the left edge of its parent container, or the screen if there's no parent container.

**[Y](properties-size-location.md)** – The distance from the control's top edge to the top edge of its parent container, or the screen if there's no parent container.


## Accessibility guidelines
### Screen reader support
* Make sure **[AccessibleLabel](properties-accessibility.md)** is present.

### Keyboard support
* Set **[TabIndex](properties-accessibility.md)** to zero or greater so keyboard users can navigate to it.

> [!TIP]
> Select <kbd>Alt</kbd>+<kbd>0</kbd> while the editor is focused to learn about other keyboard shortcuts.

> [!NOTE]
> When the toolbar is focused, select <kbd>Tab</kbd> or <kbd>Shift</kbd>+<kbd>Tab</kbd> to move between toolbar groups. You can't cycle back from the last group to the first group or vice versa.

## Limitations

### Appearance isn't guaranteed when working with other products
When you use rich text across different products, it might not look exactly the same.

- You can paste rich text from web pages, Microsoft Word, and other apps. However, the appearance might differ depending on the capabilities of the device, browser, and external source.
- Similarly, if you create rich text outside of canvas apps, it might look slightly different because built-in styles of the other app aren't present.
- If you embed the canvas app in another app, the host app might override the styles of the rich text. For example, when you use a canvas app as a [custom page](../../model-driven-apps/model-app-page-overview.md) in a model-driven app, the host app removes list styles. Bulleted lists don't show bullet points in a custom page.

Sometimes, you might want rich text to display differently based on where it's shown. For example, the primary font might be different in another product, or the text color might change when the user enables dark mode. For a consistent display, compose and show rich text in canvas apps only.

### Pasted images may not appear consistently
A pasted image might appear in a browser but not in a mobile app. Or it might appear intermittently or not at all. These are signs that the pasted image isn't supported because of:

- Cross-Origin Resource Sharing (CORS). The image host blocks the image from loading on Power Apps.
- Authentication. The image isn't publicly accessible and can only be accessed after you sign in to the image host.
- Image format support. Common image formats like jpg and png are supported, but less common types might not be supported by the browser or device.

Browsers or devices can represent images in rich text differently. Some copy the image as raw data, while others might simply reference the image's URL. Image URLs might not be accessible for the reasons above.

> [!TIP]
>  Use a screen clipping or screenshot tool to copy and paste images for the best results.

### When editing an app, Alt key doesn't allow interaction with the control
In [Power Apps Studio](../power-apps-studio.md), pressing [Alt key for quick interaction](../keyboard-shortcuts.md#alternate-behavior) doesn't work. You can only interact with the rich text editor when [previewing the app](../power-apps-studio.md#preview).

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
