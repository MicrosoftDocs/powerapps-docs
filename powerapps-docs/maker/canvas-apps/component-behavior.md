---
title: Component behavior property | Microsoft Docs
description: Component behavior property explained
author: yifwang
ms.service: powerapps
ms.topic: article
ms.date: 05/24/2019
ms.author: yifwang
search.audienceType:
  - maker
search.app:
  - PowerApps
---

# Component behavior property

> [!IMPORTANT]
> This feature is still experimental and disabled by default. For more information, see [Experimental and preview features](working-with-experimental.md).

Behavior properties rise events when the trigger action have been performed. For example 

## OnReset ##

For scenarios that have a need to invoke a behavior whenever the component is reset, you can set formulas to **OnReset** property of the component master. For examples, to perform initialization, to clear input, and to reset values. While editing a component, you can set its OnReset behavior property to a formula that will run when the component is reset. Select the component, and then select OnReset in the formula bar and enter a formula. 

![OnReset example](./media/component-behavior/example-onreset.png)

To trigger OnReset, set an action to reset the component instance in the app. 

![OnReset button](./media/component-behavior/reset-button.png)
