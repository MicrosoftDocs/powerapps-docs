---
title: Control implementation library | Microsoft Docs
description: Create custom controls using JavaScript or TypeScript
keywords:
ms.author: nabuthuk
manager: 
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5d100dc3-bd82-4b45-964c-d90eaebc0735
---

Implementing the control library is one of the key component when your developing custom controls using **PowerApps Control Framework**. Developers can implement control library using `JavaScript` and `TypeScript`. You need to transpile into `JavaScript` if you wish to implement the custom logic in `TypeScript` and add a reference to it in the manifest file.

Custom controls are implemented as `JavaScript` objects that implements a specific interface. This interface requires the control to implement the methods that will be called by the Model-driven apps.

Each custom control must have one JavaScript library that includes the definition of a function which will return an object that implements the methods described in the custom control interface. 
The object can implement the following methods:

- [init](reference/control/init.md) (Required)
- [updateView](reference/control/updateview.md) (Required)
- [getOutputs](reference/control/getoutputs.md) (Optional)
- [destroy](reference/control/destroy.md) (Required)

These methods control the life cycle of the custom control. 


