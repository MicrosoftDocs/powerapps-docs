---
title: Component implementation library | Microsoft Docs
description: Create code components using JavaScript or TypeScript
keywords:
ms.subservice: pcf
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
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