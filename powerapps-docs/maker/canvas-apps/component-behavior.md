---
title: Behavior formulas for components | Microsoft Docs
description: Trigger an app to perform one or more tasks when a component-based action occurs.
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

# Behavior formulas for components

> [!IMPORTANT]
> This feature is still experimental and disabled by default. For more information, see [Experimental and preview features](working-with-experimental.md).

Specify one or more [behavior formulas](working-with-formulas-in-depth.md) that run when an event triggers a change in a component. For example, set a component's **OnReset** property to one or more formulas that perform initialization, clear input, and reset values when the **Reset** function runs on that component.

## OnReset ##

Create a blank app for tablets, and then add a 

With a component selected, select **OnReset** in the drop-down list of properties (on the right side of the formula bar), and then enter one or more formulas.

![OnReset example](./media/component-behavior/example-onreset.png)

To trigger **OnReset**, set an action to reset the component instance in the app. 

![OnReset button](./media/component-behavior/reset-button.png)
