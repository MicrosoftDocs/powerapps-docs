---
title: Core properties | Microsoft Docs
description: Reference information about the Disabled, Visible, and ReadOnly properties
services: ''
suite: powerapps
documentationcenter: na
author: gregli-msft
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/25/2016
ms.author: gregli

---
# Core properties in PowerApps
Configure whether the user can see and interact with a control.

### Properties
**Default** – The initial value of a control before it is changed by the user.

* Applies to **[Card](../maker/controls/control-card.md)**, **[Check box](../maker/controls/control-check-box.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[Gallery](../maker/controls/control-gallery.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Rating](../maker/controls/control-rating.md)**, **[Slider](../maker/controls/control-slider.md)**, **[Text input](../maker/controls/control-text-input.md)**, and **[Toggle](control-toggle.md)** controls.

**DelayOutput** – Set to true to delay action during text input.

* Applies to  **[Text input](../maker/controls/control-text-input.md)**, **[Card](../maker/controls/control-card.md)**

**DisplayMode** – Values can be **Edit, View,** or **Disabled**. Configures whether the control allows user input (**Edit**), only displays data (**View**) or is disabled (**Disabled**).  In **View** mode, input controls such as **[Text input](../maker/controls/control-text-input.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[Date Picker](../maker/controls/control-date-picker.md)** will only display the text value and will not render any interactive elements or decorations.  This makes them suitable to be displayed in Forms or as readable output.

* Applies to **[Add picture](../maker/controls/control-add-picture.md)**, **[Audio](../maker/controls/control-audio-video.md)**, **[Button](../maker/controls/control-button.md)**, **[Camera](../maker/controls/control-camera.md)**, **[Check box](../maker/controls/control-check-box.md)**, **[Column chart](../maker/controls/control-column-line-chart.md)**, **[Date Picker](../maker/controls/control-date-picker.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[Export](../maker/controls/control-export-import.md)**, **[Gallery](../maker/controls/control-gallery.md)**, **[HTML text](../maker/controls/control-html-text.md)**, **[Icon](../maker/controls/control-shapes-icons.md)**, **[Image](../maker/controls/control-image.md)**, **[Import](../maker/controls/control-export-import.md)**, **[Label](../maker/controls/control-text-box.md)**, **[Line chart](../maker/controls/control-column-line-chart.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Microphone](../maker/controls/control-microphone.md)**, **[PDF viewer](../maker/controls/control-pdf-viewer.md)**, **[Pen input](../maker/controls/control-pen-input.md)**, **[Pie chart](../maker/controls/control-pie-chart.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Rating](../maker/controls/control-rating.md)**, **[Shape](../maker/controls/control-shapes-icons.md)**, **[Slider](../maker/controls/control-slider.md)**, **[Text input](../maker/controls/control-text-input.md)**, **[Timer](../maker/controls/control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](../maker/controls/control-audio-video.md)** controls.

**Items** – The source of data that appears in a control such as a gallery, a list, or a chart.

* Applies to **[Column chart](../maker/controls/control-column-line-chart.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[Gallery](../maker/controls/control-gallery.md)**, **[Line chart](../maker/controls/control-column-line-chart.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Pie chart](../maker/controls/control-pie-chart.md)**, and **[Radio](../maker/controls/control-radio.md)** controls.

**OnChange** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

* Applies to **[Add picture](../maker/controls/control-add-picture.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Rating](../maker/controls/control-rating.md)**, **[Slider](../maker/controls/control-slider.md)**, **[Text input](../maker/controls/control-text-input.md)**, and **[Toggle](control-toggle.md)** controls.

**OnSelect** – How the app responds when the user taps or clicks a control.

* Applies to **[Add picture](../maker/controls/control-add-picture.md)**, **[Button](../maker/controls/control-button.md)**, **[Camera](../maker/controls/control-camera.md)**, **[Check box](../maker/controls/control-check-box.md)**, **[Column chart](../maker/controls/control-column-line-chart.md)**, **[Date Picker](../maker/controls/control-date-picker.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[Export](../maker/controls/control-export-import.md)**, **[HTML text](../maker/controls/control-html-text.md)**, **[Icon](../maker/controls/control-shapes-icons.md)**, **[Image](../maker/controls/control-image.md)**, **[Import](../maker/controls/control-export-import.md)**, **[Label](../maker/controls/control-text-box.md)**, **[Line chart](../maker/controls/control-column-line-chart.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Microphone](../maker/controls/control-microphone.md)**, **[PDF viewer](../maker/controls/control-pdf-viewer.md)**, **[Pen input](../maker/controls/control-pen-input.md)**, **[Pie chart](../maker/controls/control-pie-chart.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Rating](../maker/controls/control-rating.md)**, **[Shape](../maker/controls/control-shapes-icons.md)**, **[Slider](../maker/controls/control-slider.md)**, **[Text input](../maker/controls/control-text-input.md)**, **[Timer](../maker/controls/control-timer.md)**, and **[Toggle](control-toggle.md)** controls.

**Reset** – Whether a control reverts to its default value.  Also see the **[Reset](../functions/function-reset.md)** function.

* Applies to **[Audio](../maker/controls/control-audio-video.md)**, **[Check box](../maker/controls/control-check-box.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Microphone](../maker/controls/control-microphone.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Rating](../maker/controls/control-rating.md)**, **[Slider](../maker/controls/control-slider.md)**, **[Text input](../maker/controls/control-text-input.md)**, **[Timer](../maker/controls/control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](../maker/controls/control-audio-video.md)** controls.

**Text** – Text that appears on a control or that the user types into a control.

* Applies to **[Add picture](../maker/controls/control-add-picture.md)**, **[Button](../maker/controls/control-button.md)**, **[Check box](../maker/controls/control-check-box.md)**, **[Export](../maker/controls/control-export-import.md)**, **[Import](../maker/controls/control-export-import.md)**, **[Label](../maker/controls/control-text-box.md)**, **[Text input](../maker/controls/control-text-input.md)**, and **[Timer](../maker/controls/control-timer.md)** controls.

**Tooltip** – Explanatory text that appears when the user hovers over a control.

* Applies to **[Audio](../maker/controls/control-audio-video.md)**, **[Button](../maker/controls/control-button.md)**, **[Camera](../maker/controls/control-camera.md)**, **[Check box](../maker/controls/control-check-box.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[HTML text](../maker/controls/control-html-text.md)**, **[Image](../maker/controls/control-image.md)**, **[Label](../maker/controls/control-text-box.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Microphone](../maker/controls/control-microphone.md)**, **[PDF viewer](../maker/controls/control-pdf-viewer.md)**, **[Pen input](../maker/controls/control-pen-input.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Rating](../maker/controls/control-rating.md)**, **[Slider](../maker/controls/control-slider.md)**, **[Text input](../maker/controls/control-text-input.md)**, **[Timer](../maker/controls/control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](../maker/controls/control-audio-video.md)** controls.

**Value** – The value of an input control.

* Applies to **[Check box](../maker/controls/control-check-box.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Slider](../maker/controls/control-slider.md)**, and **[Toggle](control-toggle.md)** controls.

**Visible** – Whether a control appears or is hidden.

* Applies to **[Add picture](../maker/controls/control-add-picture.md)**, **[Audio](../maker/controls/control-audio-video.md)**, **[Button](../maker/controls/control-button.md)**, **[Camera](../maker/controls/control-camera.md)**, **[Card](../maker/controls/control-card.md)**, **[Check box](../maker/controls/control-check-box.md)**, **[Column chart](../maker/controls/control-column-line-chart.md)**, **[Date Picker](../maker/controls/control-date-picker.md)**, **[Display form](../maker/controls/control-form-detail.md)**, **[Drop down](../maker/controls/control-drop-down.md)**, **[Edit form](../maker/controls/control-form-detail.md)**, **[Export](../maker/controls/control-export-import.md)**, **[Gallery](../maker/controls/control-gallery.md)**, **[HTML text](../maker/controls/control-html-text.md)**, **[Icon](../maker/controls/control-shapes-icons.md)**, **[Image](../maker/controls/control-image.md)**, **[Import](../maker/controls/control-export-import.md)**, **[Label](../maker/controls/control-text-box.md)**, **[Line chart](../maker/controls/control-column-line-chart.md)**, **[List Box](../maker/controls/control-list-box.md)**, **[Microphone](../maker/controls/control-microphone.md)**, **[PDF viewer](../maker/controls/control-pdf-viewer.md)**, **[Pen input](../maker/controls/control-pen-input.md)**, **[Pie chart](../maker/controls/control-pie-chart.md)**, **[Radio](../maker/controls/control-radio.md)**, **[Rating](../maker/controls/control-rating.md)**, **[Shape](../maker/controls/control-shapes-icons.md)**, **[Slider](../maker/controls/control-slider.md)**, **[Text input](../maker/controls/control-text-input.md)**, **[Timer](../maker/controls/control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](../maker/controls/control-audio-video.md)** controls.

