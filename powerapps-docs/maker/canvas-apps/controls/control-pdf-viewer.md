---
title: PDF viewer control (experimental) in Power Apps
description: Learn about the details, properties and examples of the PDF viewer control in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 04/10/2020
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---
# PDF viewer control (experimental) in Power Apps
An experimental control that shows the content of a PDF file.

## Description
Show text, graphics, and other content in a PDF file by adding this type of control and setting its **Document** property to the URL, enclosed in double quotation marks, of the file that you want to show.

## Limitations
1. The security architecture of Power Apps requires the PDF Viewer to support only HTTPS links, not HTTP.  

2. The **Document** property must link directly to the PDF file. Server redirects or HTML views of the document aren't supported.

3. The server that hosts the document must not require authentication.

4. You may not be able to view a PDF document in your app if the document resides on a server that has restrictive cross-origin resource sharing (CORS) settings. To resolve this issue, the server that hosts PDF documents must permit cross-origin requests from powerapps.com.

5. Some download managers (for example Internet Download Manager) will try to download the PDF file instead of allowing PowerApps to display the file. To avoid the issue, ether disable your download manager or adjust the relevent settings to avoid detection of PDF files.

App users can work around these limitations by opening PDF documents in an external browser, as prompted if the control can't open a document. This option is also available in the control menu for all external documents.

## Key properties
**Document** – The URL, enclosed in double-quotation marks, of a PDF file.

## Additional properties
**ActualZoom** – The actual zoom of the control, which may differ from the zoom requested with the **Zoom** property.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**CurrentFindText** – The current search term that is in use.

**CurrentPage** – The number of the page in a PDF file that is actually being shown.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**FindNext** – Finds the next instance of **FindText** in the document.

**FindPrevious** – Finds the previous instance of **FindText** in the document.

**FindText** – The search term to look for in the document.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**OnStateChange** – Actions to perform when the state of the control changes.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**Page** – The number of the page that you want to show.

**PageCount** – The number of pages in a document.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Zoom** – The percentage by which an image from a camera is magnified or the view of a file in a PDF viewer.

## Example

Add a **PDF viewer** control, and set its **Document** property to the URL, enclosed in double quotation marks, of a PDF file as in this example:

  **"https://blog.mozilla.org/security/files/2015/05/HTTPS-FAQ.pdf"**

The control shows the PDF file.

Don't know how to [add and configure a control](../add-configure-controls.md)?

## Accessibility guidelines

Not all accessibility features of PDF documents are supported because the **PDF viewer** is still in the experimental stage. Therefore, **ShowControls** should be set to **true** to allow users to open the document in an external application.

Learn how to create accessible PDF documents with the [WCAG 2.0](https://www.w3.org/TR/WCAG-TECHS/pdf.html) and [PDF/UA](https://www.pdfa.org/pdfua-the-iso-standard-for-universal-accessibility/) standards.

### Screen reader support
* Consider adding a heading using a **[Label](control-text-box.md)**, if the PDF document does not have a title. The heading can be positioned immediately before the **PDF viewer**.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
