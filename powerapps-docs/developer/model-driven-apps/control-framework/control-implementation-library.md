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

Custom controls are implemented as JavaScript objects that implements a specific interface. This interface requires the control to implement [init](reference/control/init.md), [updateView](reference/control/updateview.md), [destroy](reference/control/destroy.md) and [getOutputs](reference/control/getoutputs.md) methods that will be called by the Mode1-driven Apps. 

Custom controls can be implemented using `JavaScript` or `TypeScript`. You need to transpile into `JavaScript` if you wish to implement the custom logic in `TypeScript` and add a reference to it in the manifest file.

> [!NOTE]
> Custom controls are supported only on **Unified Interface**. 
