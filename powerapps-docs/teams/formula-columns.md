---
title: Work with Dataverse for Teams formula table columns | Microsoft Docs
description: Explains how to create and use formula table columns in Dataverse for Teams.
author: revachauhan
reviewer: mattp123
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/09/2021
ms.subservice: teams
ms.author: rechauha
ms.reviewer: matp
contributors:
  - mattp123
---

# Work with formula table columns (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)] More information: [Power Apps preview program](/power-platform/admin/preview-environments)

Formula columns are a data type in Microsoft Dataverse for Teams that are built on Power Fx. You can add a formula column to a table in real time. The Dataverse table stores the logic and gives you the values during fetch operations. This means you can create the formula and compute the values as you read. Formula columns use a syntax that's similar to Office Excel. As you enter the formula, Intellisense helps you with recommendations for formula, syntax, and errors.

> [!NOTE]
> - Currently, formula columns are only available with Dataverse for Teams environments.
> - Formula columns can be added as a calculated field. Currently, formula columns can't be used in roll-up fields or with plugins.

## Add a formula column

1. On the **Build** tab, select **See all**, and then expand **Tables**.
1. From the list of tables in Power Apps app for Teams, select the table you want.
1. Select **Add column** or select **Edit data** > **Add column**. When you select **Edit data**, you can also select **+** next to the row where you want to add the formula column.
1. In the **Add new column** pane: 
   - Enter a **Name** for the column, such as *Total price*.
   - Select **Formula** as the **Type**.
   - Enter the formula in the **Expression** box. In this example, the *Price* column (Decimal data type) is multiplied by the *Number of units* column (Number data type).  Select **Create**.
   :::image type="content" source="media/create-formula-column.png" alt-text="Create a formula column":::

When you create a record, the formula column executes the formula and displays the data for the record. If the formula column value for a record doesn't update, select **Refresh** on the command bar to execute the formula.

:::image type="content" source="media/record-example-formula-column.png" alt-text="Example record with a formula column":::

## Data types

The following data types can be displayed in a formula column:

- Text
- Decimal Number
- Yes/No (boolean)
- Date

> [!NOTE]
> The Currency data type is not currently supported.

## Function types

The following function types are supported with the formulas used in a formula column:

- Decimal
- String
- Boolean
- Option Set
- DateTime (User Local)
- DateTime (Date Only)
- DateTime (TZI)
- Currency
- Whole Number
- Float

## Operators

These  operators are supported with the formulas used in a formula column: <br />
+, -, *, /, %, ^, in, exactin, &

## Available functions 

The following scalar functions are available with formula columns.

:::row:::
   :::column span="":::
      Abs
   :::column-end:::
   :::column span="":::
      And
   :::column-end:::
   :::column span="":::
      Average
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Blank
   :::column-end:::
   :::column span="":::
      Char
   :::column-end:::
   :::column span="":::
      Concatenate
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      DateTimeValue
   :::column-end:::
   :::column span="":::
      DateValue
   :::column-end:::
   :::column span="":::
      Day
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      EndsWith
   :::column-end:::
   :::column span="":::
      Exp
   :::column-end:::
   :::column span="":::
      Hour
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      If
   :::column-end:::
   :::column span="":::
      IfError
   :::column-end:::
   :::column span="":::
      IsBlank
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      IsError
   :::column-end:::
   :::column span="":::
      IsToday
   :::column-end:::
   :::column span="":::
      ISOWeekNum
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Left
   :::column-end:::
   :::column span="":::
      Len
   :::column-end:::
   :::column span="":::
      Ln
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Lower
   :::column-end:::
   :::column span="":::
      Max
   :::column-end:::
   :::column span="":::
      Mid
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Min
   :::column-end:::
   :::column span="":::
      Minute
   :::column-end:::
   :::column span="":::
      Mod
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Month
   :::column-end:::
   :::column span="":::
      Not
   :::column-end:::
   :::column span="":::
      Now
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Or
   :::column-end:::
   :::column span="":::
      Power
   :::column-end:::
   :::column span="":::
      Replace
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Right
   :::column-end:::
   :::column span="":::
      Round
   :::column-end:::
   :::column span="":::
      RoundDown
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      RoundUp
   :::column-end:::
   :::column span="":::
      Second
   :::column-end:::
   :::column span="":::
      Sqrt
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      StartsWith
   :::column-end:::
   :::column span="":::
      Substitute
   :::column-end:::
   :::column span="":::
      Sum
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Switch
   :::column-end:::
   :::column span="":::
      Text
   :::column-end:::
   :::column span="":::
      TimeZoneOffset
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Today
   :::column-end:::
   :::column span="":::
      Trim
   :::column-end:::
   :::column span="":::
      Trunc
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      TrimEnds
   :::column-end:::
   :::column span="":::
      Upper
   :::column-end:::
   :::column span="":::
      Value
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Weekday
   :::column-end:::
   :::column span="":::
      WeekNum
   :::column-end:::
   :::column span="":::
      Year
   :::column-end:::
:::row-end:::

### See also

[Work with table columns](table-columns.md) <br />
[Formula reference for Power Apps](../maker/canvas-apps/formula-reference.md)
