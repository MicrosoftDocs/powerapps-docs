---
title: Power Fx and cards overview
description: Learn about Power Fx and how it's used to add business logic in cards for Microsoft Power Apps.
ms.date: 3/22/2024
ms.topic: overview
author: mduelae
ms.author: mkaur
ms.reviewer: 
ms.custom: 
ms.collection: 

---

# Power Fx and cards overview

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

[Power Fx](/power-platform/power-fx/overview) is a low-code programming language available across the Power Platform, including in Power Apps cards. Cards can calculate values, perform tasks, and respond to user input using formulas expressed in Power Fx. Power Fx expressions can also update variables and data sources. Expressions can be combined to create complex formulas that can handle advanced business logic.

## Power Fx documentation

For more information on Power Fx formulas that work in cards, see [Formula reference for Cards](/power-platform/power-fx/formula-reference-cards). When you're working with cards, you'll also find the following articles especially helpful:

- [Expression grammar](/power-platform/power-fx/expression-grammar)
- [Operators](/power-platform/power-fx/operators)
- [Variables](/power-platform/power-fx/variables)
- [Formula reference](/power-platform/power-fx/formula-reference)

For more information on Power Fx formulas that work in cards, see [Formula reference for Cards](/power-platform/power-fx/formula-reference-cards).

> [!Important]
> [Defaults](/power-platform/power-fx/reference/function-defaults) isn't supported. Instead use [Collect](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect), for example, instead of `Patch(account, Defaults(account), {"Account Name": "Example Account"})` use `Collect(account, {"Account Name": "Example Account"})`.

### Large tables (delegation)

Working with large data sets in cards can impact performance. Take heed of delegation warnings. Learn more about [delegation](/power-apps/maker/canvas-apps/delegation-overview).

Cards supports delegating the following functions:

- LookUp

### Dataverse types

Cards don't support Image, URL, File, or ManagedProperty column types yet.
