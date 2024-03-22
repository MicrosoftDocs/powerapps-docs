---
title: Power Fx and cards overview
description: Learn about Power FX and how it's used to add business logic in cards for Microsoft Power Apps.
ms.date: 3/22/2024
ms.topic: overview
author: sericks007
ms.author: sericks
ms.reviewer: 
ms.custom: 
ms.collection: 

---

# Power Fx and cards overview

[Power Fx](/power-platform/power-fx/overview) is a low-code programming language available across the Power Platform, including in Power Apps cards. Cards can calculate values, perform tasks, and respond to user input using formulas expressed in Power Fx. Power Fx expressions can also update variables and data sources. Expressions can be combined to create complex formulas that can handle advanced business logic.

## Power Fx documentation

The [Power Fx documentation](/power-platform/power-fx/overview) is the primary source of information about Power Fx. When you're working with cards, you'll find the following articles especially helpful:

- [Expression grammar](/power-platform/power-fx/expression-grammar)
- [Operators](/power-platform/power-fx/operators)
- [Variables](/power-platform/power-fx/variables)
- [Formula reference](/power-platform/power-fx/formula)

For more information on Power Fx formulas that work in cards, see [Formula reference for Cards](/power-platform/power-fx/formula-reference-cards).

> [!Important]
> [Defaults](/power-platform/power-fx/reference/function-defaults) is not support. Instead use [Collect](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect), for example, instead of `Patch(account, Defaults(account), {"Account Name": "Example Account"})` use `Collect(account, {"Account Name": "Example Account"})`.

### Large tables (delegation)

Working with large data sets in cards can impact performance. Take heed of delegation warnings. Learn more about [delegation](/power-apps/maker/canvas-apps/delegation-overview).

Today, cards supports delegating the following functions:

- LookUp

### Dataverse types

Cards do not support Image, URL, File, or ManagedProperty column types yet.
