---
title: Container control in Power Apps
description: Learn about the details, properties and examples of the container control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.component: canvas
ms.date: 06/01/2022
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur-msft
search.audienceType: 
  - maker
contributors:
  - yogeshgupta698
  - tahoon-ms
  - mduelae
---
# Container control in Power Apps

Groups logically-related controls to create hierarchies.

## Description

The container can hold a set of controls and has its own properties.

You can start with inserting a blank container. And then, customize it by adding controls to it, resizing it, moving it, hiding it, and making other changes. You can also start with a number of controls, select them and add using tree view.

## Limitations

- Containers don't work within forms.
- The following controls are not supported within a container:
    - [Data table](control-data-table.md)
    - [PDF viewer](control-pdf-viewer.md)
    - [Web barcode scanner](control-barcodescanner.md)

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


## Frequently asked questions

### What is the difference between a container and a group?

When editing an app, you can select controls and group them using Ctrl + G or the context menu. You can modify common properties of controls within the group. Groups are an aid for app making. They don't have properties of their own and don't affect the layout of the app.

In contrast, containers are actual controls with their own properties like **Width** and **BorderColor**. Containers affect app layout and help screen reader users understand the structure of the app.

While you can add any controls in a group, you should only add logically-related controls in a container. For example, [controls in a tile should be placed in containers](../accessible-apps-structure.md#logical-control-order).


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
