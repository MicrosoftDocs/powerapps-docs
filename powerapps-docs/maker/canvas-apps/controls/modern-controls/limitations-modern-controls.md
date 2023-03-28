---
title: Limitations of modern controls in canvas apps
description: Learn about limitations and known issue of modern controls in canvas apps.
author: yogeshgupta698

ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur-msft
ms.date: 03/22/2023
ms.subservice: canvas-maker
ms.author: yogupt


search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - mduelae
  - yogeshgupta698
---

# Limitations of modern controls in canvas apps
[This article is pre-release document and is subject to change.]

There are few current limitations & known issues which Microsoft is working towards:

1. For the modern controls, if add items through an array such as PowerFx bar or advance properties. Then, you will need to additionally select “Value” field from the properties panel.

> [!div class="mx-imgBorder"]
   > ![List in items](media/array-list.png)

> [!div class="mx-imgBorder"]
   > ![Enable value field](media/select-value-field.png)

2. While updating properties of controls in property panel, some of the property value updates in format of:
  ‘PowerApps.CoreControls.<Control name>.<Property name>’.<Value>
  This is a valid format, or you can update to value only. Both approaches will work for configuration of the control.
  
3. The property sets for new controls are different than property sets of original controls. Not all scenarios are supported on new controls yet and we will ship consistent improvements to enable new scenarios.
  
4. The modern controls don’t have support right now for properties to show up in command bar too. We currently only support property value updates through property panel.
  
5. All app checker rules like accessibility and formulas, don’t run on modern controls currently. The support will come soon as the feature develops.



### See also

[Overview of modern controls in canvas apps](overview-modern-controls.md)


