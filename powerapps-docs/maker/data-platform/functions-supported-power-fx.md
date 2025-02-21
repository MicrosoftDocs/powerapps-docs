---
title: "Supported functions in Microsoft Dataverse"
description: "Find out what Power Fx operators, variables, and formulas are supported with Dataverse"
ms.custom: ""
ms.date: 02/03/2025
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "paulliew"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "paulliew"
search.audienceType: 
  - maker
---
# Supported functions

Functions in Microsoft Dataverse can add business logic to your apps using the Power Fx expression language and you can quickly build rich workflows without any code. Functions support many of the Power Fx operators, variables, and formulas.

The following table lists the Power Fx formulas that work with functions in Dataverse but have limitations or don’t work but have an alternative for use with functions.

| Power Fx formula or operation    | Supported in functions? | Limitation or work around                                                                                     |
|---------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------|
| `Collect`                   | Yes                     | Requires the variable to exist and the variable type to match what you’re trying to set it to.                 |
| `Defaults`                  | No                      | Use `Collect` instead of `Patch`. For example, instead of `Patch(account, Defaults(account), {"Account Name": "Example Account"})`, use `Collect(account, {"Account Name": "Example Account"})`. |
| Add tables in the UI      | Yes                     | For example, in order for the expression to `Collect(Accounts, {... })`, the accounts table needs to be added in the UI. This helps with intellisense. |
| Accessing fields in formula| Yes                     | No implicit scope for accessing fields. Instead of saying `Field2`, say `NewRecord.Field2`. This applies to `Set` as well: `Set(NewRecord.Field1, OldRecord.Field2*10)`. |
| `With()`                  | Yes              | Functions don't support contexts, named formulas, or variables. `With()` can be used to create aliases and factor the expressions. |
| Access Dataverse tables   | Yes              | Functions can read and write to Dataverse tables. This includes `Collect()`, `Patch()`, `Filter()`, and `LookUp()`. Delegation operations are supported, and a warning is issued if an expression can't be delegated. These operations run directly against the function’s `IOrganizationService` (not the current table) and directly operate on the database. Functions run in the transaction context. |

## Power Fx functions not supported

The following Power Fx function aren't currently supported with functions in Dataverse.

:::row:::
   :::column span="":::
      ClearCollect
   :::column-end:::
   :::column span="":::
      Update
   :::column-end:::
   :::column span="":::
      UpdateIf
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Concurrent
   :::column-end:::
   :::column span="":::
      SetFocus
   :::column-end:::
   :::column span="":::
      IsType
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Download
   :::column-end:::
   :::column span="":::
      RemoveIf
   :::column-end:::
   :::column span="":::
      GroupBy
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      SetProperty
   :::column-end:::
   :::column span="":::
      Search
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
      As
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Calendar
   :::column-end:::
   :::column span="":::
      Choices
   :::column-end:::
   :::column span="":::
      Clock
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Select
   :::column-end:::
   :::column span="":::
      Notify
   :::column-end:::
   :::column span="":::
      HashTags
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      ISOWeekNum
   :::column-end:::
   :::column span="":::
      SaveData, LoadData, and ClearData
   :::column-end:::
   :::column span="":::
      Form-related formulas (EditForm, NewForm, SubmitForm, ResetForm, and ViewForm)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="3":::
      Device sensor formulas (Acceleration, App, Compass, Connection, and Location)
   :::column-end:::
:::row-end:::

For more information about Power Fx, go to these articles:

- [Expression grammar](/power-platform/power-fx/expression-grammar)
- [Operators](/power-platform/power-fx/operators)
- [Variables](/power-platform/power-fx/variables)
- [Formula reference](/power-platform/power-fx/formula-reference)

 