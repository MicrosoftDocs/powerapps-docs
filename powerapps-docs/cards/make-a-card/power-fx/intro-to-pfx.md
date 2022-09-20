---
title: Power Fx and cards overview (Preview)
description: Learn about Power FX and how it's used to add business logic in Microsoft Power Apps cards.
ms.date: 09/20/2022
ms.topic: overview
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Power Fx and cards overview (Preview)

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

- Device sensor formulas (**Acceleration**, **App**, **Compass**, **Connection**, and **Location**) don't work.
- **SaveData**, **LoadData**, and **ClearData** don't work.
- Form-related formulas (**EditForm**, **NewForm**, **SubmitForm**, **ResetForm**, and **ViewForm**) don't work.
- **Update** and **UpdateIf** don't work.
- **Collect**, **Patch**, and **Remove** work in variables and Dataverse tables only.
- **Set** requires the variable to exist and the variable type to match what you're trying to set it to.
