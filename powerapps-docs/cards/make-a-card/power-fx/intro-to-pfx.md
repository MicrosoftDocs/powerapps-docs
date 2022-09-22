---
title: Introduction to Power Fx (Preview)
description: Learn about Power FX and how it's used in cards to add business logic.
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Introduction to Power Fx (Preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

[Power Fx](/power-platform/power-fx/overview) is a low-code programming language available across the Power Platform, including cards. Cards can calculate values, perform other tasks, and respond to user input using [formulas](/power-platform/power-fx/formula-reference) expressed with Power Fx.

For example, a formula might determine what happens when a user selects a button or enters text into a text input. Formulas can also be used to update variables and data sources. Expressions can be combined to create complex formulas that can handle advanced business logic.

## Power Fx documentation

The [Power Fx documentation](/power-platform/power-fx/overview) is the main source for information about Power Fx. Makers and developers working with cards will find the following articles helpful:

- [Expression grammar](/power-platform/power-fx/expression-grammar)
- [Operators](/power-platform/power-fx/operators)
- [Variables](/power-platform/power-fx/variables)
- [Formula reference](/power-platform/power-fx/formula-reference)

## Known Power Fx limitations with cards

There are some known limitations with cards and Power Fx. These include:

- All device sensor formulas don't work (**Acceleration**, **App**, **Compass**, **Connection**, and **Location**).
- **SaveData**, **LoadData**, and **ClearData** don't work.
- Form-related formulas don't work (**EditForm**, **NewForm**, **SubmitForm**, **ResetForm**, and **ViewForm**).
- **Collect**, **Patch**, and **Remove** only work for variables and Dataverse tables.
- **Update** and **UpdateIf** don't work.
- **Set** requires the type of the variable to match what you are trying to set it to and requires the variable to be already created using the variable creation.
