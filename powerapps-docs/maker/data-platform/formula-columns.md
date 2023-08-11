---
title: Work with Dataverse formula columns
description: Learn how to create and use formula columns in Microsoft Dataverse.
author: matp
reviewer: mattp123
ms.topic: how-to
ms.custom: 
ms.date: 07/25/2023
ms.subservice: teams
ms.author: dikamath
ms.reviewer: matp
contributors:
  - mattp123
---

# Work with formula columns (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Formula columns are columns that display a calculated value in a Microsoft Dataverse table. Formulas use [Power Fx](/power-platform/power-fx/overview), a powerful but human-friendly programming language. Build a formula in a Dataverse formula column the same way you would build a formula in Microsoft Excel. As you type, Intellisense suggests functions and syntax, and even helps you fix errors.

> [!NOTE]
> Formula columns can be added as a calculated field. Currently, formula columns can't be used in roll-up fields or with plugins.

## Add a formula column

1. Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Tables**, and then select the table where you want to add a formula column. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the **Columns** area, and then select **New column**.
1. Enter the following information:

   - A **Display name** for the column.
   - Optionally, enter a **Description** of the column.
   - In **Data type**, select ***fx* Formula**.
   - Enter the formula in the **Formula** box.
   - Select **Searchable** if you want this column to be available in views, charts, dashboards and Advanced Find.
   - **Advanced options**:
     - If the formula entered evaluates to a decimal value, expand **Advanced options** to change the number of points of precision, between 0 and 10. The default value is 2.
5. Select **Save**.

The following example creates a formula column called *Total price*. The *Number of units* column is a whole number data type. The *Price* column is a decimal data type.

:::image type="content" source="media/create-formula-column-dataverse.png" alt-text="Screenshot of a formula column definition.":::

The formula column displays the result of *Price* multiplied by *Number of units*.

:::image type="content" source="media/record-in-app-formula-column.png" alt-text="Screenshot of a record with a formula column.":::

The formula that you enter determines the column type. You can't change a column type after the column is created. That means you can change the formula after you’ve created the column only if it doesn’t change the column type.

For example, the formula *price * discount* creates a column type of number. You can change *price * discount* to  *price * (discount + 10%)* because that doesn’t change the column type. However, you can’t change *price * discount* to  *Text(price * discount)* because that would require changing the column type to string.

## Operators

You can use the following operators in a formula column:  
+, -, \*, /, %, in, exactin, &

For more information, go to [Operators in Power Apps](../canvas-apps/functions/operators.md).

## Data types

You can display the following data types in a formula column:

- Text
- Decimal number
- Yes/No (boolean)
- Datetime

The currency and date data types aren't currently supported.

## Function types

You can use the following function types in a formula column:

- Decimal
- String
- Boolean
- Option Set
- DateTime (TZI)
- DateTime (User local) (limited to comparisons with other user local values DateAdd, and DateDiff functions)
- DateTime (Date only) (limited to comparisons with other date-only values, DateAdd, and DateDiff functions)
- Currency
- Whole Number, promoted to Decimal

## Functions

You can use the following scalar functions in a formula column:

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
      [Value](../canvas-apps/functions/function-value.md) \*
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
      [Year](../canvas-apps/functions/function-datetime-parts.md)
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
      [WeekNum](../canvas-apps/functions/function-weeknum.md)
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
      [Weekday](../canvas-apps/functions/function-datetime-parts.md)
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

   :::column-end:::
:::row-end:::

\* The **Text** and **Value** functions only work with whole numbers, where no decimal separator is involved. The decimal separator varies across locales. Since formula columns are evaluated without locale knowledge, there's no way to properly interpret or generate the decimal separator.

### Function example

|Description  |Example  |
|---------|---------|
|Retrieve a date value.  |  `DateAdd(UTCNow(),-1,TimeUnit.Years)`   |


### See also

[Types of columns](types-of-fields.md)  
[Microsoft Power Fx overview](/power-platform/power-fx/overview)
