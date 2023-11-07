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
contributors:
  - mduelae
  - yogeshgupta698
---

# Limitations of modern controls in canvas apps (preview)

[This article is pre-release document and is subject to change.]

In this article, learn about the general limitations of the modern controls used in canvas apps. 

1. While updating properties of controls in property panel, some of the property value updates in format of:

    `PowerApps.CoreControls.<Control name>.<Property name>`  `.<Value>`
  
     This is a valid format, or you can update to value only. Both approaches work for configuration of the control.

2. The property sets for new controls are different than property sets of original controls. Not all scenarios are supported on new controls. We're consistently trying to make improvements for new scenarios.
  
3. The modern controls don’t have support for properties that show up in command bar. Currently we only support property value updated through the property panel.
  
4. Not all app checker rules such as accessibility and formulas run on modern controls currently. We offer support when the feature matures.

5. Test Studio and Test engine compatibility with modern controls is under development and modern controls aren't fully supported on these tools.



### See also

[Overview of modern controls in canvas apps](overview-modern-controls.md)


