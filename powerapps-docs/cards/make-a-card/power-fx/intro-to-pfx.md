---
title: Power Fx and cards overview (preview)
description: Learn about Power FX and how it's used to add business logic in cards for Microsoft Power Apps.
ms.date: 09/20/2022
ms.topic: overview
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Power Fx and cards overview (preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

[Power Fx](/power-platform/power-fx/overview) is a low-code programming language available across the Power Platform, including in Power Apps cards. Cards can calculate values, perform tasks, and respond to user input using formulas expressed in Power Fx. Power Fx expressions can also update variables and data sources. Expressions can be combined to create complex formulas that can handle advanced business logic.

## Power Fx documentation

The [Power Fx documentation](/power-platform/power-fx/overview) is the main source of information about Power Fx. When you're working with cards, you'll find the following articles especially helpful:

- [Expression grammar](/power-platform/power-fx/expression-grammar)
- [Operators](/power-platform/power-fx/operators)
- [Variables](/power-platform/power-fx/variables)
- [Formula reference](/power-platform/power-fx/formula-reference)

## Known limitations of using Power Fx in cards

The following Power Fx formulas don't work in cards or work with limitations:

- [**Set**](/power-platform/power-fx/reference/function-set) and [**Collect**](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect) requires the variable to exist and the variable type to match what you're trying to set it to.
- [**Collect**](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect), [**Patch**](/power-platform/power-fx/reference/function-patch), and [**Remove**](/power-platform/power-fx/reference/function-remove-removeif#remove-function) work with variables and Dataverse tables only.
- [**Defaults**](/power-platform/power-fx/reference/function-defaults) is not supported, instead use [**Collect**](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect). For example, instead of `Patch(account, Defaults(account), {"Account Name": "Example Account"})` do `Collect(account, {"Account Name": "Example Account"})`.
- [**User()**](/power-platform/power-fx/reference/function-user) is not supported yet, instead use **Viewer**, which has a subset of information about the user viewing the card.
- [**Clear**](/power-platform/power-fx/reference/function-clear-collect-clearcollect#clear) and [**ClearCollect**](/power-platform/power-fx/reference/function-clear-collect-clearcollect#clearcollect) are not supported yet
- [**Update**](/power-platform/power-fx/reference/function-update-updateif#update-function) and [**UpdateIf**](/power-platform/power-fx/reference/function-update-updateif#updateif-function) are not supported yet
- Device sensor formulas ([**Acceleration**, **App**, **Compass**, **Connection**, and **Location**](/power-platform/power-fx/reference/signals)) don't work.
- [**SaveData**, **LoadData**, and **ClearData**](/power-platform/power-fx/reference/function-savedata-loaddata) don't work.
- Form-related formulas ([**EditForm**, **NewForm**, **SubmitForm**, **ResetForm**, and **ViewForm**](/power-platform/power-fx/reference/function-form)) don't work.
