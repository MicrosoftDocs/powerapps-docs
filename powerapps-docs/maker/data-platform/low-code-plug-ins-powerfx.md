---
title: Low-code plug-ins Power Fx
description: Supported Power Fx expressions for use with Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 05/18/2023
ms.custom: template-how-to
---
# Low-code plug-ins Power Fx (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Low-code plug-ins can add business logic to your apps using the Power Fx expression language and directly integrate with Dataverse business data and external data through Power Platform connectors. With low-code plug-ins, you can quickly build rich workflows without any code.

> [!IMPORTANT]
> This is a preview feature.

The following table lists the Power Fx formulas that have limitations or don’t work with low-code plug-ins. Power Fx formulas not listed here are supported.

|Power Fx formula  |Supported in plug-ins?  | Limitation or work around   |
|---------|---------|---------|
|Set     |  Yes      | Requires the variable to exist (as bound table row property) and the variable type to match what you’re trying to set it to. <br /> For an automated action, update the associated row’s values by passing `ThisRecord` as the first argument (referring to the row that triggered the data event), then the desired column updates in the second object parameter, such as `Set( ThisRecord, { Description: “Updated description text” } );`  |
|Collect     | Yes        | Requires the variable to exist and the variable type to match what you’re trying to set it to.    |
|Defaults     |  No       | Use Collect instead. For example, instead of *Patch(account, Defaults(account), {“Account Name”: “Example Account”})* use `Collect(account, {“Account Name”: “Example Account”})`.    |
|User()     | No        | Instead use Viewer, which has a subset of information about the user who invoked the action (both instant and automated).    |
|Clear     | No        |     |
|ClearCollect    |  No       |     |
|Update     |  No       |     |
|UpdateIf    |  No       |     |
|Device sensor formulas (Acceleration, App, Compass, Connection, and Location)    |   No      |     |
|SaveData, LoadData, and ClearData     |   No      |     |
|Form-related formulas (EditForm, NewForm, SubmitForm, ResetForm, and ViewForm)     |  No       |     |
|AddColumns     | No        |     |
|Concurrent     |  No       |     |
|DropColumns     | No        |     |
|EncodeUrl   |  No       |     |
|IsEmpty    |  No       |     |
|IsMatch     |  No       |     |
|IsType    |  No       |     |
|JSON     |  No       |     |
|Match    |  No       |     |
|PlainText    |  No       |     |
|RemoveIf     |  No       |     |
|SortByColumns     |  No       |     |
|Update    |  No       |     |
|UpdateIf    |  No       |     |
|AsType   |   No      |     |
|Distinct    |  No       |     |
|exactin     |  No       |     |
|GroupBy     |    No     |     |
|in    |     No    |     |
|RenameColumns      |  No         |       |
| Search     |   No        |       |
| ShowColumns     |   No        |       |
| UTCNow     |   No        |       |
|UTCToday     |   No        |       |
| Validate     |   No        |       |
| Weekday     |  No         |       |
| As     |   No        |       |
| Calendar     |  No         |       |
| Choices     |   No        |       |
| Clock     |  No         |       |
| ColorFade     |   No        |       |
| ColorValue     |  No         |       |
| Errors     |   No        |       |
| HashTags     |  No         |       |
| ISOWeekNum     |  No         |       |
| Language     |  No         |       |
| MatchAll     |  No         |       |
| Refresh     |  No         |       |
| RGBA     |  No         |       |
| WeekNum     | No          |       |
| Notify     |  No         |       |
| Select     |  No         |       |
| SetProperty     |  No         |       |
| Download     |  No         |       |
| SetFocus     |  No         |       |

## See also

The Power Fx documentation is the primary source of information about Power Fx. When you’re working with actions, you’ll find the following articles helpful:

- [Expression grammar](/power-platform/power-fx/expression-grammar)
- [Operators](/power-platform/power-fx/operators)
- [Variables](/power-platform/power-fx/variables)
- [Formula reference](/power-platform/power-fx/formula-reference)