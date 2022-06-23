---
title: Work with Dataverse formula table columns | Microsoft Docs
description: Explains how to create and use formula table columns in Dataverse.
author: matp
reviewer: mattp123
ms.topic: how-to
ms.custom: 
ms.date: 06/23/2022
ms.subservice: teams
ms.author: dikamath
ms.reviewer: matp
contributors:
  - mattp123
---
# Work with formula columns (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Formula columns are a data type in Microsoft Dataverse that are built on Power Fx. You can add a formula column to a table in real time. The table stores the logic and gives you the values during fetch operations. Formula columns use the Power Fx syntax that's similar to Office Excel. As you enter the formula, Intellisense helps you with recommendations for formula, syntax, and errors.

> [!NOTE]
> Formula columns can be added as a calculated field. Currently, formula columns can't be used in roll-up fields or with plugins.

## Add a formula column

1. Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Go to **Dataverse** > **Tables**, and then open the table you want where you want to add a formula column.
1. Select the **Columns** area, and then select **New column**.
1. In the **New column** pane:
   - Enter a **Display name** for the column, such as *Total price*.
   - Optionally, enter a description for the column.
   - Select **Formula** as the **Data type**.
   - Enter the formula in the **Expression** box. In this example, *Price* is a custom column with a decimal data type that is multiplied by the *Number of units*, a custom column with a whole number data type.  Select **Create**.
   :::image type="content" source="media/create-formula-column-dataverse.png" alt-text="Create a formula column":::

When you create a record in a model-driven app, the formula column executes upon save and displays the data for the record in the column.

:::image type="content" source="media/record-in-app-formula-column.png" alt-text="Example record with a formula column":::

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

More information: [Operators in Power Apps](../canvas-apps/functions/operators.md)

## Available functions 

The following scalar functions are available with formula columns.

:::row:::
   :::column span="":::
      [Abs](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [And](../canvas-apps/functions/function-logicals.md)
   :::column-end:::
   :::column span="":::
      [Average](../canvas-apps/functions/function-aggregates.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Blank](../canvas-apps/functions/function-isblank-isempty.md)
   :::column-end:::
   :::column span="":::
      [Char](../canvas-apps/functions/function-char.md)
   :::column-end:::
   :::column span="":::
      [Concatenate](../canvas-apps/functions/function-concatenate.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [DateAdd](../canvas-apps/functions/function-dateadd-datediff.md)
   :::column-end:::
   :::column span="":::
      [DateDiff](../canvas-apps/functions/function-dateadd-datediff.md)
   :::column-end:::
   :::column span="":::
      [Day](../canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [EndsWith](../canvas-apps/functions/function-startswith.md)
   :::column-end:::
   :::column span="":::
      [Exp](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Hour](../canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [If](../canvas-apps/functions/function-if.md)
   :::column-end:::
   :::column span="":::
      [IfError](../canvas-apps/functions/function-iferror.md)
   :::column-end:::
   :::column span="":::
      [Int](../canvas-apps/functions/function-round.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [IsBlank](../canvas-apps/functions/function-isblank-isempty.md)
   :::column-end:::
   :::column span="":::
      [IsError](../canvas-apps/functions/function-iferror.md)
   :::column-end:::
   :::column span="":::
      [ISOWeekNum](../canvas-apps/functions/function-weeknum.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [IsUTCToday](../canvas-apps/functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Left](../canvas-apps/functions/function-left-mid-right.md)
   :::column-end:::
   :::column span="":::
      [Len](../canvas-apps/functions/function-len.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Ln](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Lower](../canvas-apps/functions/function-lower-upper-proper.md)
   :::column-end:::
   :::column span="":::
      [Max](../canvas-apps/functions/function-aggregates.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Mid](../canvas-apps/functions/function-left-mid-right.md)
   :::column-end:::
   :::column span="":::
      [Min](../canvas-apps/functions/function-aggregates.md)
   :::column-end:::
   :::column span="":::
      [Minute](../canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Mod](../canvas-apps/functions/function-mod.md)
   :::column-end:::
   :::column span="":::
      [Month](../canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Not](../canvas-apps/functions/function-logicals.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Or](../canvas-apps/functions/function-logicals.md)
   :::column-end:::
   :::column span="":::
      [Power](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Replace](../canvas-apps/functions/function-replace-substitute.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Right](../canvas-apps/functions/function-left-mid-right.md)
   :::column-end:::
   :::column span="":::
      [Round](../canvas-apps/functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [RoundDown](../canvas-apps/functions/function-round.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [RoundUp](../canvas-apps/functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [Second](../canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Sqrt](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [StartsWith](../canvas-apps/functions/function-startswith.md)
   :::column-end:::
   :::column span="":::
      [Substitute](../canvas-apps/functions/function-replace-substitute.md)
   :::column-end:::
   :::column span="":::
      [Sum](../canvas-apps/functions/function-aggregates.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Switch](../canvas-apps/functions/function-if.md)
   :::column-end:::
   :::column span="":::
      [Text](../canvas-apps/functions/function-text.md) \*
   :::column-end:::
   :::column span="":::
      [Trim](../canvas-apps/functions/function-trim.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Trunc](../canvas-apps/functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [TrimEnds](../canvas-apps/functions/function-trim.md)
   :::column-end:::
   :::column span="":::
      [Upper](../canvas-apps/functions/function-lower-upper-proper.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [UTCNow](../canvas-apps/functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [UTCToday](../canvas-apps/functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Value](../canvas-apps/functions/function-value.md) \*
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Weekday](../canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [WeekNum](../canvas-apps/functions/function-weeknum.md)
   :::column-end:::
   :::column span="":::
      [Year](../canvas-apps/functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::

\* The **Text** and **Value** functions only work with whole numbers, where no decimal separator is involved. Since the decimal separator varies across locales, and the formula columns are evaluated without locale knowledge, there's no way to properly interpret or generate the decimal separator.

### See also

[Types of columns](types-of-fields.md)