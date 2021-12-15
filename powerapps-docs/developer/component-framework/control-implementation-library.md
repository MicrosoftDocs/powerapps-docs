---
title: Component implementation library | Microsoft Docs
description: Create code components using JavaScript or TypeScript
keywords:
ms.subservice: pcf
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5d100dc3-bd82-4b45-964c-d90eaebc0735
---

# Component implementation library

Implementing the component library is one of the key steps when you're developing code components using Power Apps component framework. Developers can implement component library using TypeScript.

Each code component must have a library that includes the definition of a function, which returns an object that implements the methods described in the code component interface. 

The object implements the following methods:

- [init](reference/control/init.md) (Required)
- [updateView](reference/control/updateview.md) (Required)
- [getOutputs](reference/control/getoutputs.md) (Optional)
- [destroy](reference/control/destroy.md) (Required)

These methods control the lifecycle of the code component.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]