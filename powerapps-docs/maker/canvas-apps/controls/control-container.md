---
title: 'Container control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Container control
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.component: canvas
ms.date: 05/01/2020
ms.author: emcoope
ms.reviewer: tapanm-msft
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Container control in Power Apps (experimental)
Provides the ability to create hierarchy.

> [!IMPORTANT]
> This is an experimental feature. Experimental features can radically change or completely disappear at any time.
> For more information, read [Understand experimental and preview features in Power Apps](https://docs.microsoft.com/powerapps/maker/canvas-apps/working-with-experimental-preview).

## Description
 The container can hold a set of controls and has its own properties.

You can start with inserting a blank container. And then, customize it by adding controls to it, resizing it, moving it, hiding it, and making other changes. You can also start with a number of controls, select them and add using tree view.

## Properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen, if no parent container). 

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen, if no parent container). 


## Known limitations

Containers don't work within forms.

## Frequently asked questions

### What is the difference between a container and a group?

The authoring group is a lightweight concept used for moving around controls and bulk editing similar properties of controls within the group. The authoring group doesn't affect the layout of the app.

The container control previously shipped in experimental as a replacement for the authoring group renamed as the enhanced group. It was renamed to the container control as there's value in both a lightweight authoring group and a structured container control with additional properties.
