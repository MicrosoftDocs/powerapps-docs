---
title: Low-code plug-ins Power Fx
description: Supported Power Fx expressions for use with Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 08/02/2024
ms.custom: template-how-to
---
# Low-code plug-ins Power Fx (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Low-code plug-ins can add business logic to your apps using the Power Fx expression language and directly integrate with Dataverse business data and external data through Power Platform connectors. With low-code plug-ins, you can quickly build rich workflows without any code.

> [!IMPORTANT]
>
>- Instant low-code plug-ins are deprioritized and aren't being delivered as a feature. Instant low-code plug-ins are replaced with functions. More information: [Functions in Microsoft Dataverse (preview)](functions-overview.md)
> - This is an preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Low-code plug-ins support many of the Power Fx operators, variables, and formulas. For more information about Power Fx, go to these articles:

- [Expression grammar](/power-platform/power-fx/expression-grammar)
- [Operators](/power-platform/power-fx/operators)
- [Variables](/power-platform/power-fx/variables)
- [Formula reference](/power-platform/power-fx/formula-reference)

The following table lists the Power Fx formulas that work but have limitations or don’t work but have an alternative for use with low-code plug-ins.

|Power Fx formula  |Supported in plug-ins?  | Limitation or work around   |
|---------|---------|---------|
|Collect     | Yes        | Requires the variable to exist and the variable type to match what you’re trying to set it to.    |
|Defaults     |  No       | Use Collect instead. For example, instead of *Patch(account, Defaults(account), {“Account Name”: “Example Account”})* use `Collect(account, {“Account Name”: “Example Account”})`.    |

## Power Fx formulas supported

For information about the formulas supported with low-code plug-ins, go to [Formula reference- Dataverse plug-ins](/power-platform/power-fx/formula-reference-plug-ins).

Formulas *not currently supported* with low-code plug-ins

:::row:::
   :::column span="":::
      Clear
   :::column-end:::
   :::column span="":::
      ClearCollect
   :::column-end:::
   :::column span="":::
      Update
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      UpdateIf
   :::column-end:::
   :::column span="":::
      SortByColumns
   :::column-end:::
   :::column span="":::
      Concurrent
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      DropColumns
   :::column-end:::
   :::column span="":::
      AddColumns
   :::column-end:::
   :::column span="":::
      IsEmpty
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      SetFocus
   :::column-end:::
   :::column span="":::
      IsType
   :::column-end:::
   :::column span="":::
      JSON
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Download
   :::column-end:::
   :::column span="":::
      PlainText
   :::column-end:::
   :::column span="":::
     RemoveIf
   :::column-end:::
:::row-end:::
:::row:::
:::row-end:::
:::row:::
   :::column span="":::
      GroupBy
   :::column-end:::
   :::column span="":::
      SetProperty
   :::column-end:::
   :::column span="":::
      RenameColumns
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Search
   :::column-end:::
   :::column span="":::
      ShowColumns
   :::column-end:::
   :::column span="":::
      UTCNow
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      UTCToday
   :::column-end:::
   :::column span="":::
      Validate
   :::column-end:::
   :::column span="":::
      Weekday
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      As
   :::column-end:::
   :::column span="":::
      Calendar
   :::column-end:::
   :::column span="":::
      Choices
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Clock
   :::column-end:::
   :::column span="":::
      Select
   :::column-end:::
   :::column span="":::
      Notify
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Errors
   :::column-end:::
   :::column span="":::
      HashTags
   :::column-end:::
   :::column span="":::
      ISOWeekNum 
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      WeekNum
   :::column-end:::
   :::column span="":::
      Refresh
   :::column-end:::
   :::column span="":::
      SaveData, LoadData, and ClearData
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Form-related formulas (EditForm, NewForm, SubmitForm, ResetForm, and ViewForm)
   :::column-end:::
   :::column span="":::
      Device sensor formulas (Acceleration, App, Compass, Connection, and Location)
   :::column-end:::
   :::column span="":::
      <!--empty-->
   :::column-end:::
:::row-end:::

## See also

[Use Dataverse low-code plug-ins (preview)](low-code-plug-ins.md)
