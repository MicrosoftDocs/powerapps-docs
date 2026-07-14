---
title: Work with Dataverse for Teams formula table columns | Microsoft Docs
description: Explains how to create and use formula table columns in Dataverse for Teams.
author: MicroSri
reviewer: mattp123
ms.topic: how-to
ms.custom: 
ms.date: 01/24/2022
ms.subservice: teams
ms.author: matp
ms.reviewer: matp
contributors:
  - mattp123
---

# Work with formula table columns (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)] More information: [Power Apps preview program](/power-platform/admin/preview-environments)

Formula columns are a data type in Microsoft Dataverse for Teams that are built on Power Fx. You can add a formula column to a table in real time. The Dataverse table stores the logic and gives you the values during fetch operations. Formula columns use the Power Fx syntax that's similar to Office Excel. As you enter the formula, Intellisense helps you with recommendations for formula, syntax, and errors.

> [!NOTE]
> Formula columns can be added as a calculated field. Currently, formula columns can't be used in roll-up fields or with plugins.

## Add a formula column

1. On the **Build** tab, select **See all**, and then expand **Tables**.
1. From the list of tables in Power Apps app for Teams, select the table you want.
1. Select **Add column** or select **Edit data** > **Add column**. When you select **Edit data**, you can also select **+** on the column where you want to add the formula column.
1. In the **Add new column** pane: 
   - Enter a **Name** for the column, such as *Total price*.
   - Select **Formula** as the **Type**.
   - Enter the formula in the **Expression** box. In this example, the *Price* column (Decimal data type) is multiplied by the *Number of units* column (Number data type).  Select **Create**.
   :::image type="content" source="media/create-formula-column.png" alt-text="Create a formula column":::

When you create a record, the formula column executes the formula and displays the data for the record. If the formula column value for a record doesn't update, select **Refresh** on the command bar to execute the formula.

:::image type="content" source="media/record-example-formula-column.png" alt-text="Example record with a formula column":::

Notice that the column type is determined by the formula. You can change the formula after you’ve created it if it doesn’t change the column type. For example, the formula *price * discount* creates a column type of number, whereas the formula *First & “ “ & Last* creates a column type of string. You can change a *price * discount* formula to  *price * (discount +10%)* because that doesn’t change the column type. However, once saved, you can’t change the *price * discount* formula to  *Text(price * discount)* because that would require changing the column type to string.

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
- DateTime (TZI)
- DateTime (User local) (limited to comparisons with other user local values and the DateAdd function)
- DateTime (Date only) (limited to comparisons with other date-only values, and the DateAdd function)
- Currency
- Whole Number, promoted to Decimal

## Operators

These operators are supported with the formulas used in a formula column: <br>
+, -, \*, /, %, ^, in, exactin, &

More information: [Operators in Power Apps](../maker/canvas-apps/functions/operators.md)

## Available functions 

The following scalar functions are available with formula columns.

:::row:::
   :::column span="":::
      [Abs](../maker/canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [And](../maker/canvas-apps/functions/function-logicals.md)
   :::column-end:::
   :::column span="":::
      [Average](../maker/canvas-apps/functions/function-aggregates.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Blank](../maker/canvas-apps/functions/function-isblank-isempty.md)
   :::column-end:::
   :::column span="":::
      [Char](../maker/canvas-apps/functions/function-char.md)
   :::column-end:::
   :::column span="":::
      [Concatenate](../maker/canvas-apps/functions/function-concatenate.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [DateAdd](../maker/canvas-apps/functions/function-dateadd-datediff.md)
   :::column-end:::
   :::column span="":::
      [DateDiff](../maker/canvas-apps/functions/function-dateadd-datediff.md)
   :::column-end:::
   :::column span="":::
      [Day](../maker/canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [EndsWith](../maker/canvas-apps/functions/function-startswith.md)
   :::column-end:::
   :::column span="":::
      [Exp](../maker/canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Hour](../maker/canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [If](../maker/canvas-apps/functions/function-if.md)
   :::column-end:::
   :::column span="":::
      [IfError](../maker/canvas-apps/functions/function-iferror.md)
   :::column-end:::
   :::column span="":::
      [Int](../maker/canvas-apps/functions/function-round.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [IsBlank](../maker/canvas-apps/functions/function-isblank-isempty.md)
   :::column-end:::
   :::column span="":::
      [IsError](../maker/canvas-apps/functions/function-iferror.md)
   :::column-end:::
   :::column span="":::
      [ISOWeekNum](../maker/canvas-apps/functions/function-weeknum.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [IsUTCToday](../maker/canvas-apps/functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Left](../maker/canvas-apps/functions/function-left-mid-right.md)
   :::column-end:::
   :::column span="":::
      [Len](../maker/canvas-apps/functions/function-len.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Ln](../maker/canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Lower](../maker/canvas-apps/functions/function-lower-upper-proper.md)
   :::column-end:::
   :::column span="":::
      [Max](../maker/canvas-apps/functions/function-aggregates.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Mid](../maker/canvas-apps/functions/function-left-mid-right.md)
   :::column-end:::
   :::column span="":::
      [Min](../maker/canvas-apps/functions/function-aggregates.md)
   :::column-end:::
   :::column span="":::
      [Minute](../maker/canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Mod](../maker/canvas-apps/functions/function-mod.md)
   :::column-end:::
   :::column span="":::
      [Month](../maker/canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Not](../maker/canvas-apps/functions/function-logicals.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Or](../maker/canvas-apps/functions/function-logicals.md)
   :::column-end:::
   :::column span="":::
      [Power](../maker/canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Replace](../maker/canvas-apps/functions/function-replace-substitute.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Right](../maker/canvas-apps/functions/function-left-mid-right.md)
   :::column-end:::
   :::column span="":::
      [Round](../maker/canvas-apps/functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [RoundDown](../maker/canvas-apps/functions/function-round.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [RoundUp](../maker/canvas-apps/functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [Second](../maker/canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Sqrt](../maker/canvas-apps/functions/function-numericals.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [StartsWith](../maker/canvas-apps/functions/function-startswith.md)
   :::column-end:::
   :::column span="":::
      [Substitute](../maker/canvas-apps/functions/function-replace-substitute.md)
   :::column-end:::
   :::column span="":::
      [Sum](../maker/canvas-apps/functions/function-aggregates.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Switch](../maker/canvas-apps/functions/function-if.md)
   :::column-end:::
   :::column span="":::
      [Text](../maker/canvas-apps/functions/function-text.md) \*
   :::column-end:::
   :::column span="":::
      [Trim](../maker/canvas-apps/functions/function-trim.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Trunc](../maker/canvas-apps/functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [TrimEnds](../maker/canvas-apps/functions/function-trim.md)
   :::column-end:::
   :::column span="":::
      [Upper](../maker/canvas-apps/functions/function-lower-upper-proper.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [UTCNow](../maker/canvas-apps/functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [UTCToday](../maker/canvas-apps/functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Value](../maker/canvas-apps/functions/function-value.md) \*
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Weekday](../maker/canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [WeekNum](../maker/canvas-apps/functions/function-weeknum.md)
   :::column-end:::
   :::column span="":::
      [Year](../maker/canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::

\* The **Text** and **Value** functions only work with whole numbers, where no decimal separator is involved. Since the decimal separator varies across locales, and the formula columns are evaluated without locale knowledge, there's no way to properly interpret or generate the decimal separator.

### See also

[Work with table columns](table-columns.md) <br />
[Formula reference for Power Apps](../maker/canvas-apps/formula-reference.md)
