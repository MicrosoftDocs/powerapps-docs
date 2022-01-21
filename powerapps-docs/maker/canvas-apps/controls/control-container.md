---
title: Container control in Power Apps
description: Learn about the details, properties and examples of the container control in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.component: canvas
ms.date: 02/12/2021
ms.subservice: canvas-maker
ms.author: chmoncay
ms.reviewer: tapanm-msft
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - chmoncay
  - tahoon-ms
  - tapanm-msft
---
# Container control in Power Apps

Provides the ability to create hierarchy.

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

- Containers don't work within forms.
- You cannot add tables to the layout containers.

## Frequently asked questions

### What is the difference between a container and a group?

The authoring group is a lightweight concept used for moving around controls and bulk editing similar properties of controls within the group. The authoring group doesn't affect the layout of the app.

The container control previously shipped in experimental as a replacement for the authoring group renamed as the enhanced group. It was renamed to the container control as there's value in both a lightweight authoring group and a structured container control with additional properties.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]