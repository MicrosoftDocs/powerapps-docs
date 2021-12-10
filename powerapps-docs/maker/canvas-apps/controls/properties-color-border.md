---
title: Color and border properties in Power Apps
description: Reference information about the color and border properties in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 09/01/2021
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
  - gregli-msft
---
# Color and border properties in Power Apps

## Overview

Configure the style of a control based on how the user interacts with it.

You can specify colors in many ways:

- [**Color**](../functions/function-colors.md) enumeration: Specify color names from cascading style sheets, as in these examples:

  - **Color.Red**
  - **Color.Indigo**

- [**ColorValue**](../functions/function-colors.md) function: Specify text strings such as color names from cascading style sheets and hex-code notation (**#**), as in these examples:

  - **ColorValue( "AliceBlue" )**
  - **ColorValue( "#ff00ff" )**

- [**ColorFade**](../functions/function-colors.md) function: Specify how faded a color is, from fully black (-100%) to fully white (100%), as in this example:

  - **ColorFade( Color.Red, 50% )**

- [**RGBA**](../functions/function-colors.md) function: Specify the red, green, and blue components of a color from 0 to 255, and specify an alpha channel from 0% (fully transparent) to 100% (fully opaque), as in this example:

  - **RGBA( 255, 0, 255, 25% )**

Color properties can also reference other color properties. For example, **Label.PressedColor** may be set to the formula **Label1.Color**, automatically cascading a change from one property to another.

## Normal

These properties are in effect normally, when the user is not interacting with the control.

**BorderColor** – The color of a control's border.

- Applies to **[Add picture](control-add-picture.md)**, **[Audio](control-audio-video.md)**, **[Button](control-button.md)**, **[Camera](control-camera.md)**, **[Card](control-card.md)**, **[Check box](control-check-box.md)**, **[Column chart](control-column-line-chart.md)**, **[Date Picker](control-date-picker.md)**, **[Display form](control-form-detail.md)**, **[Drop down](control-drop-down.md)**, **[Edit form](control-form-detail.md)**, **[Export](control-export-import.md)**, **[Gallery](control-gallery.md)**, **[HTML text](control-html-text.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[Line chart](control-column-line-chart.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pen input](control-pen-input.md)**, **[Pie chart](control-pie-chart.md)**, **[Radio](control-radio.md)**, **[Rating](control-rating.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](control-audio-video.md)** controls.

**BorderStyle** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

- Applies to **[Add picture](control-add-picture.md)**, **[Audio](control-audio-video.md)**, **[Button](control-button.md)**, **[Camera](control-camera.md)**, **[Card](control-card.md)**, **[Check box](control-check-box.md)**, **[Column chart](control-column-line-chart.md)**, **[Date Picker](control-date-picker.md)**, **[Display form](control-form-detail.md)**, **[Drop down](control-drop-down.md)**, **[Edit form](control-form-detail.md)**, **[Export](control-export-import.md)**, **[Gallery](control-gallery.md)**, **[HTML text](control-html-text.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[Line chart](control-column-line-chart.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pen input](control-pen-input.md)**, **[Pie chart](control-pie-chart.md)**, **[Radio](control-radio.md)**, **[Rating](control-rating.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](control-audio-video.md)** controls.

**BorderThickness** – The thickness of a control's border.

- Applies to **[Add picture](control-add-picture.md)**, **[Audio](control-audio-video.md)**, **[Button](control-button.md)**, **[Camera](control-camera.md)**, **[Card](control-card.md)**, **[Check box](control-check-box.md)**, **[Column chart](control-column-line-chart.md)**, **[Date Picker](control-date-picker.md)**, **[Display form](control-form-detail.md)**, **[Drop down](control-drop-down.md)**, **[Edit form](control-form-detail.md)**, **[Export](control-export-import.md)**, **[Gallery](control-gallery.md)**, **[HTML text](control-html-text.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[Line chart](control-column-line-chart.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pen input](control-pen-input.md)**, **[Pie chart](control-pie-chart.md)**, **[Radio](control-radio.md)**, **[Rating](control-rating.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](control-audio-video.md)** controls.

**Color** – The color of text in a control.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Column chart](control-column-line-chart.md)**, **[Date Picker](control-date-picker.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[HTML text](control-html-text.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[Line chart](control-column-line-chart.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Pen input](control-pen-input.md)**, **[Pie chart](control-pie-chart.md)**, **[Radio](control-radio.md)**, **[Text input](control-text-input.md)**, and **[Timer](control-timer.md)** controls.

**Fill** – The background color of a control.

- Applies to **[Add picture](control-add-picture.md)**, **[Audio](control-audio-video.md)**, **[Button](control-button.md)**, **[Card](control-card.md)**, **[Check box](control-check-box.md)**, **[Date Picker](control-date-picker.md)**, **[Display form](control-form-detail.md)**, **[Drop down](control-drop-down.md)**, **[Edit form](control-form-detail.md)**, **[Export](control-export-import.md)**, **[Gallery](control-gallery.md)**, **[HTML text](control-html-text.md)**, **[Icon](control-shapes-icons.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pen input](control-pen-input.md)**, **[Radio](control-radio.md)**, **[Rating](control-rating.md)**, **[Screen](control-screen.md)**, **[Shape](control-shapes-icons.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](control-audio-video.md)** controls.

## Focused

These properties are in effect when the control is focused.

**FocusedBorderColor** – The color of a control's border when it has focus.

**FocusedBorderThickness** – The thickness of a control's border when it has focus.

- These properties apply to **[Add picture](control-add-picture.md)**, **[Attachments](control-attachments.md)**, **[Audio](control-audio-video.md)**, **[Button](control-button.md)**, **[Camera](control-camera.md)**, **[Check box](control-check-box.md)**, **[Combo box](control-combo-box.md)**, **[Date Picker](control-date-picker.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[Gallery](control-gallery.md)**, **[Icon](control-shapes-icons.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Radio](control-radio.md)**, **[Rating](control-rating.md)**, **[Shape](control-shapes-icons.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](control-audio-video.md)** controls.

## Disabled

These properties are in effect when the control is disabled.  A control can be disabled if the **[Disabled](properties-core.md)** property is set to *true*.

**DisabledBorderColor** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Column chart](control-column-line-chart.md)**, **[Date Picker](control-date-picker.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[HTML text](control-html-text.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[Line chart](control-column-line-chart.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pie chart](control-pie-chart.md)**, **[Radio](control-radio.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, and **[Toggle](control-toggle.md)** controls.

**DisabledColor** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Date Picker](control-date-picker.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Radio](control-radio.md)**, **[Text input](control-text-input.md)**, and **[Timer](control-timer.md)** controls.

**DisabledFill** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Date Picker](control-date-picker.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[HTML text](control-html-text.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Radio](control-radio.md)**, **[Text input](control-text-input.md)**, and **[Timer](control-timer.md)** controls.

## Hover

These properties are in effect when the user hovers over the control with a mouse.

**HoverBorderColor** – The color of a control's border when the user keeps the mouse pointer on that control.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Column chart](control-column-line-chart.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[HTML text](control-html-text.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[Line chart](control-column-line-chart.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pie chart](control-pie-chart.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, and **[Toggle](control-toggle.md)** controls.

**HoverColor** – The color of the text in a control when the user keeps the mouse pointer on it.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Radio](control-radio.md)**, **[Text input](control-text-input.md)**, and **[Timer](control-timer.md)** controls.

**HoverFill** – The background color of a control when the user keeps the mouse pointer on it.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[Icon](control-shapes-icons.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Radio](control-radio.md)**, **[Shape](control-shapes-icons.md)**, **[Text input](control-text-input.md)**, and **[Timer](control-timer.md)** controls.

## Pressed

These properties are in effect when a button or image control is pressed.

**PressedBorderColor** – The color of a control's border when the user taps or clicks that control.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Column chart](control-column-line-chart.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[Icon](control-shapes-icons.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[Line chart](control-column-line-chart.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pie chart](control-pie-chart.md)**, **[Shape](control-shapes-icons.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, and **[Toggle](control-toggle.md)** controls.

**PressedColor** – The color of text in a control when the user taps or clicks that control.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Radio](control-radio.md)**, **[Text input](control-text-input.md)**, and **[Timer](control-timer.md)** controls.

**PressedFill** – The background color of a control when the user taps or clicks that control.

- Applies to **[Add picture](control-add-picture.md)**, **[Button](control-button.md)**, **[Check box](control-check-box.md)**, **[Drop down](control-drop-down.md)**, **[Export](control-export-import.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[Radio](control-radio.md)**, **[Text input](control-text-input.md)**, and **[Timer](control-timer.md)** controls.

## Selection

These properties are in effect when the user selects an item in a control.

**SelectionColor** – The text color of a selected item or items in a list or the color of the selection tool in a pen control.

- Applies to **[Drop down](control-drop-down.md)**, **[List Box](control-list-box.md)**, and **[Pen input](control-pen-input.md)** controls.

**SelectionFill** – The background color of a selected item or items in a list or a selected area of a pen control.

- Applies to **[Drop down](control-drop-down.md)** and **[List Box](control-list-box.md)** controls.

## Order of color

A control can be in multiple states.  For example: focused and hovered.  Only one color is used, in this order:

1. Disabled
1. Pressed
1. Hover
1. Focus 
1. Normal

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
