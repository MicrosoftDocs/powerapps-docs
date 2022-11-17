---
title: Power Fx and cards overview (preview)
description: Learn about Power FX and how it's used to add business logic in cards for Microsoft Power Apps.
ms.date: 11/17/2022
ms.topic: overview
author: sericks007
ms.author: sericks
manager: tapanm-MSFT
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

The table below contains the Power Fx formulas don't work in cards or work with limitations. All other functions are fully supported.

| Power Fx formula | Supported in cards | Limitations and suggestions |
|---------|:---:|:------------------:|
| [Set](/power-platform/power-fx/reference/function-set) | Yes | Requires the variable to exist and the variable type to match what you're trying to set it to. |
| [Collect](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect) | Yes | Requires the variable to exist and the variable type to match what you're trying to set it to. |
| [Defaults](/power-platform/power-fx/reference/function-defaults) | No | Use [Collect](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect) instead, for example, instead of `Patch(account, Defaults(account), {"Account Name": "Example Account"})` use `Collect(account, {"Account Name": "Example Account"})`. |
| [User()](/power-platform/power-fx/reference/function-user) | No | Instead use **Viewer**, which has a subset of information about the user viewing the card. |
| [Clear](/power-platform/power-fx/reference/function-clear-collect-clearcollect#clear) | No |  |
| [ClearCollect](/power-platform/power-fx/reference/function-clear-collect-clearcollect#clearcollect) | No | |
| [Update](/power-platform/power-fx/reference/function-update-updateif#update-function) | No | |
| [UpdateIf](/power-platform/power-fx/reference/function-update-updateif#updateif-function) | No | |
| Device sensor formulas ([Acceleration, App, Compass, Connection, and Location](/power-platform/power-fx/reference/signals)) | No | |
| [SaveData, LoadData, and ClearData](/power-platform/power-fx/reference/function-savedata-loaddata) | No | |
| Form-related formulas ([EditForm, NewForm, SubmitForm, ResetForm, and ViewForm](/power-platform/power-fx/reference/function-form)) | No | |
| AddColumns | No | |
| Concurrent | No | |
| DropColumns | No | |
| EncodeUrl | No | |
| IsEmpty | No | |
| IsMatch | No | |
| IsType | No | |
| JSON | No | |
| Match | No | |
| PlainText | No | |
| RemoveIf | No | |
| SortByColumns | No | |
| Update | No | |
| UpdateIf | No | |
| AsType | No | |
| Distinct | No | |
| exactin | No | |
| GroupBy | No | |
| in | No | |
| RenameColumns | No | |
| Search | No | |
| ShowColumns | No | |
| UTCNow | No | |
| UTCToday | No | |
| Validate | No | |
| Weekday | No | |
| As | No | |
| Calendar | No | |
| Choices | No | |
| Clock | No | |
| ColorFade | No | |
| ColorValue | No | |
| Errors | No | |
| HashTags | No | |
| ISOWeekNum | No | |
| Language | No | |
| MatchAll | No | |
| Refresh | No | |
| RGBA | No | |
| WeekNum | No | |
| Notify | No | |
| Select | No | |
| SetProperty | No | |
| Download | No | |
| SetFocus | No | |
