---
title: 'PDF viewer control: reference | Microsoft Docs'
description: Information, including properties and examples, about the PDF viewer control
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
ms.date: 10/25/2016
ms.author: fikaradz

---
# PDF viewer control in PowerApps
A control that shows the content of a PDF file.

## Description
Show text, graphics, and other content in a PDF file by adding this type of control and setting its **Document** property to the URL, enclosed in double quotation marks, of the file that you want to show.

## Limitations
Note that due to the security architecture of PowerApps, PDF Viewer only supports HTTPS links and not HTTP.  
If the PDF document resides on a server with restrictive CORS settings, you may not be able to view it within your app.  In case the document cannot be opened in PowerApps, the option to open the document in an external browser is presented to the end user.

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

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnStateChange** – How an app responds when the state of the control changes.

**[PaddingBottom](../../controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../../controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../../controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../../controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**Page** – The number of the page that you want to show.

**PageCount** – The number of pages in a document.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Zoom** – The percentage by which an image from a camera is magnified or the view of a file in a PDF viewer.

## Example
* Add a **PDF viewer** control, and set its **Document** property to the URL, enclosed in double quotation marks, of a PDF file as in this example:<br>
  **"http://www.who.int/gho/publications/world_health_statistics/EN_WHS2015_TOC.pdf?ua=1"**

    The control shows the PDF file.

    Don't know how to [add and configure a control](../add-configure-controls.md)?
