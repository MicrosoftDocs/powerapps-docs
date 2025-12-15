---
title: Copilot answer modern control in Power Apps
description: Learn about the details, properties, and examples of the Copilot answer modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 12/15/2025
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  
---
# Copilot answer modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A control that makers can use to add predefined questions that end users can use to get generated answers.

> [!IMPORTANT]
> Starting February 2, 2026, adding the Copilot control to new canvas apps will be discontinued. Existing apps with this control will remain functional for a limited time but will eventually no longer be supported.

> [!NOTE]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - App Copilot for canvas apps is currently rolling out and might not yet be available in your region.

## Description

Makers can use the Copilot answer control to set predefined questions that end users can use to get generative answers with a single click. The control is optimized for mobile users and is powered by Microsoft Copilot.

## Key properties

**Data source (Items)** – The Copilot answer control only supports Dataverse as the data source. The answer to the question comes from the Dataverse table that you select.

**Views** – A user can select any of the views that are available in the data source.  

**Fields** - Default list of fields available for the table. Users can select **Edit** to see the list of fields. They can also add or modify the fields based on their requirements.  

**Title** – A label that is displayed at the top of the Copilot answer control.  

**Question for Copilot** – This is the question a maker asks the Copilot answer control. The question is used as the prompt to generate a response that is displayed by the answer control that's based on the selected **Data source** property.


## Additional properties

**Show answer** – Should the Copilot answer control answer a question when the user clicks on the ‘Arrow’ icon (After sending) or as soon as the control loads when the question is defined in the properties window (Immediate).

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**Position** - Whether a control appears or is hidden.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas
