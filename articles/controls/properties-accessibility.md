<properties
    pageTitle="Accessibility properties | Microsoft PowerApps"
    description="Reference information about properties such as TabIndex, Tooltip"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="fikaradz"
    manager="anneta"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="01/26/2017"
   ms.author="anneta"/>

# Accessibility properties in PowerApps #

## Overview ##
Configuration of properties that aid alternative ways of interaction with controls suitable for visually impaired users.

## Properties ##

**Tooltip** – Explanatory text that appears when the user hovers over a control.  Text is used by Aria labels that aid screen readers.

- Applies to **[Audio](control-audio-video.md)**, **[Button](control-button.md)**, **[Camera](control-camera.md)**, **[Check box](control-check-box.md)**, **[Drop down](control-drop-down.md)**, **[HTML text](control-html-text.md)**, **[Image](control-image.md)**, **[Label](control-text-box.md)**, **[List Box](control-list-box.md)**, **[Microphone](control-microphone.md)**, **[PDF viewer](control-pdf-viewer.md)**, **[Pen input](control-pen-input.md)**, **[Radio](control-radio.md)**, **[Rating](control-rating.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, **[Timer](control-timer.md)**, **[Toggle](control-toggle.md)**, and **[Video](control-audio-video.md)** controls.


**TabIndex** –  Customizes the tab order of controls at runtime.

Default value of zero specifies default tab order, based on control's XY coordinate.  Setting a value higher than zero will move the control's tab order ahead of all controls with the default values.  A control with TabIndex value of 2 will precede one with TabIndex of 3 or higher when tabbed.

Note that containers such as Form and Gallery controls will always tab through all elements of the container before proceeding to controls outside of the container.  The container's tab order is that of the lowest value TabIndex of a child control.

Setting TabIndex to -1 will disable tab access to the control; in case of Images, Icons and Shapes, they will also be invisible to the screen reader.

- Applies to **[Button](control-button.md)**, **[Date Picker](control-date-picker.md)**,  **[Drop down](control-drop-down.md)**, **[Image](control-image.md)**, **[Import](control-export-import.md)**, **[List Box](control-list-box.md)**, **[Radio](control-radio.md)**, **[Rating](control-rating.md)**, **[Slider](control-slider.md)**, **[Text input](control-text-input.md)**, and  **[Toggle](control-toggle.md)** controls.
