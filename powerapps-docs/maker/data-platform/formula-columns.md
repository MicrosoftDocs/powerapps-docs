---
title: Work with Dataverse formula columns
description: Learn how to create and use formula columns in Microsoft Dataverse.
author: sanjeevgoyalmsft
reviewer: mattp123
ms.topic: how-to
ms.custom: needs-feature-review
ms.date: 06/23/2025
ms.update-cycle: 180-days
ms.subservice: dataverse-maker
ms.author: sriknair
ms.reviewer: matp
ms.collection: bap-ai-copilot
contributors:
  - mattp123
  - sanjeevgoyalmsft
  - JimDaly
  - neerajatmsft
---
# Work with formula columns

Formula columns are columns that display a calculated value in a Microsoft Dataverse table. Formulas use [Power Fx](/power-platform/power-fx/overview), a powerful but human-friendly programming language. Build a formula in a Dataverse formula column the same way you would build a formula in Microsoft Excel. As you type, Intellisense suggests functions and syntax, and even helps you fix errors.

## Add a formula column

1. Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Tables**, and then select the table where you want to add a formula column. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the **Columns** area, and then select **New column**.
1. Enter the following information:
   - A **Display name** for the column.
   - Optionally, enter a **Description** of the column.
1. For **Data type** select ***fx* Formula**.
1. Type the formula or use formula suggestions:

   # [Type a formula](#tab/type-or-paste)

   Enter the Power Fx formula in the **Formula** box. More information: [Type a formula](#type-a-formula-1)

   # [Get formula suggestions (preview)](#tab/natural-language)

   [!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]
   a. Select the up and down arrows, and then select **Get formula suggestions**.<br />
       :::image type="content" source="media/formula-suggestions-selector.png" alt-text="Select the formula suggestions selector":::
   b. Type your question, such as *what is the Price times Quantity*, in the **Get formula suggestions** box. More information: [Get formula suggestions (preview)](#get-formula-suggestions-preview-1)

---

7. Select additional properties:
   - Select **Searchable** if you want this column to be available in views, charts, dashboards, and Advanced Find.
   - **Advanced options**:
     - If the formula evaluates to a decimal value, expand **Advanced options** to change the number of points of precision, between 0 and 10. The default value is 2.
8. Select **Save**.

### Type a formula

The following example creates a formula column called *Total price*. The *Number of units* column is a whole number data type. The *Price* column is a decimal data type.

:::image type="content" source="media/create-formula-column-dataverse.png" alt-text="Screenshot of a formula column definition.":::

The formula column displays the result of *Price* multiplied by *Number of units*.

:::image type="content" source="media/record-in-app-formula-column.png" alt-text="Screenshot of a record with a formula column.":::

The formula that you enter determines the column type. You can't change a column type after the column is created. That means you can change the formula after you create the column only when it doesn't change the column type.

For example, the formula *price * discount* creates a column type of number. You can change *price * discount* to  *price * (discount + 10%)* because that doesn't change the column type. However, you can't change *price * discount* to  *Text(price * discount)* because that would require changing the column type to string.

### Get formula suggestions (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Describe what you want the formula to do and get AI generated results. Formula suggestions accept your natural language input to interpret and suggest a Power Fx formula using GPT-based AI model.

> [!IMPORTANT]
> This is a preview feature available only in US regions only.
>
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
>
> Currently, formula suggestions that reference a single table are supported. Formula suggestions that reference a column on a related table aren't supported.

#### Prerequisites

To enable this feature, you must enable the **AI suggestions for formula columns** environment setting. More information: [AI suggestions for formula columns](/power-platform/admin/settings-features#ai-suggestions-for-formula-columns)

#### Example natural language input

Imagine there's a **Customer rating** column that shows their rating by account.
:::image type="content" source="media/customer-rating-column.png" alt-text="Example customer rating column":::

In the **Get formula suggestions** box enter the formula in natural language, such as *If the rating on the rating column is equal or greater than 5 then indicate as Good and if less than 5 indicate as Average and if value is blank or zero then display as Bad*, and then select the arrow button (enter).

Then copy the **Suggested Formula**.
:::image type="content" source="media/suggested-formula.png" alt-text="Suggested formula":::

And paste it into the **Type a formula** box. Select **Save**.
:::image type="content" source="media/paste-formula.png" alt-text="Paste formula into Type a formula box.":::

Here's how the formula appears when pasted.

```powerappsfl
Switch(
    ThisRecord.'Customer Rating',
    Blank(), "Bad",
    0, "Bad",
    1, "Average",
    2, "Average",
    3, "Average",
    4, "Average",
    5, "Good",
    6, "Good",
    7, "Good",
    8, "Good",
    9, "Good",
    10, "Good"
)
```

Check the computed **Rating Description** formula column, which appears like this.
 
:::image type="content" source="media/formula-suggestions-results.png" alt-text="Check the results for the formula column":::

#### Responsible AI

For information about responsible AI, go to these resources:

- [FAQ for building apps and tables through conversation](../common/faqs-build-apps-conversation.md)
- [FAQ about using AI responsibly in Power Apps](../common/responsible-ai-overview.md)

## Operators

You can use the following operators in a formula column:  
+, -, \*, /, %, in, exactin, &

For more information, go to [Operators in Power Apps](../canvas-apps/functions/operators.md).

## Data types

You can display the following data types in a formula column:

- Text
- [Decimal Number](formula-column-data-types.md#create-a-decimal-formula-column)
- [Whole Number](formula-column-data-types.md#create-a-whole-number-formula-column)
- [Float](formula-column-data-types.md#create-a-floating-point-number-formula-column)
- Boolean Choice (Yes/No)
- [Choice](formula-column-data-types.md#create-a-choice-formula-column) (formerly option sets)
- Datetime

More information: [Create formula columns with decimal, whole number, float, and choice data types](formula-column-data-types.md)\

The currency data type isn't currently supported.

## Function types

You can use the following function types in a formula column:

- Decimal
- String
- Boolean
- Choice
- DateTime (TZI)
- DateTime (User local) (limited to comparisons with other user local values DateAdd, and DateDiff functions)
- DateTime (Date only) (limited to comparisons with other date-only values, DateAdd, and DateDiff functions)
- Currency
- Whole Number

## Functions

For the scalar functions you can use in a formula column, go to [Formula reference - Dataverse formula columns](/power-platform/power-fx/formula-reference-formula-columns).
<!--
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
      [Now](../canvas-apps/functions/function-now-today-istoday.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Error](../canvas-apps/functions/function-iferror.md)
   :::column-end:::
   :::column span="":::
     [Decimal](../canvas-apps/functions/function-value.md) \*
   :::column-end:::
   :::column span="":::
     [Float](../canvas-apps/functions/function-value.md) \*
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Sqrt](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
     [Ln](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
     [Power](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Exp](../canvas-apps/functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
   :::column-end:::
   :::column span="":::
   :::column-end:::
:::row-end::: -->

\* The **Text** and **Value** functions only work with whole numbers, where no decimal separator is involved. The decimal separator varies across locales. Since formula columns are evaluated without locale knowledge, there's no way to properly interpret or generate the decimal separator.

\* **StartOfWeek** argument isn't supported for the **WeekNum** and **Weekday** functions in formula columns.

### Function example

|Description  |Example  |
|---------|---------|
|Retrieve a date value.  |  `DateAdd(UTCNow(),-1,TimeUnit.Years)`   |

## Guidelines and limitations

This section describes guidelines and the known limitations with formula columns in Dataverse.

### Currency fields usage validations

- Formula columns don't support using a related table currency column in the formula, such as in this example.
   :::image type="content" source="media/formula-column-currency.png" alt-text="Formula column with unsupported formula of Account.Annual Revenue":::
- Direct use of currency columns and exchange rate in the formula is currently unsupported. The use of currency and exchange rate columns is achieved through the `Decimal` function, such as `Decimal(currency column)` or `Decimal(exchange rate)`. The `Decimal` function makes sure the output is within the accepted range. If the currency or exchange rate column value exceeds the accepted range, then the formula returns null.
- Base currency columns aren't supported in the formula column expressions because they're system columns used for reporting purpose. If you want a similar result, you can use a currency column type along with an exchange rate column combination as `CurrencyField_Base = (CurrencyField / ExchangeRate)`.

### Date time columns usage validations

- Behavior of date time formula columns can only be updated when it isn't used in another formula column.
- For date time formula columns, while using the `DateDiff` function, make sure that:
  - User local behavior column can't be compared or used  with a `DateTime(TZI)/DateOnly` behavior column.
  - User local behavior columns can only be compared or used with another user local behavior column.
  - `DateTime(TZI)` behavior columns can be compared or used in `DateDiff` functions with another `DateTime(TZI)/DateOnly` behavior column.
  - `DateOnly` behavior columns can be compared or used in DateDiff function with another `DateTime(TZI)/DateOnly` behavior column.
  :::image type="content" source="media/formula-column-datetime.png" alt-text="Unsupported date time configuration with a formula column":::
- Date time columns and date time functions `UTCNow()`, `Now()` can't be passed as a parameter to string functions.
  :::image type="content" source="media/formula-column-date-time-arg.png" alt-text="Formula column with unsupported date time parameter passed in formula":::

### Formula column usage in rollup fields

- A *simple formula column* is where the formula uses columns from the same record or uses hard coded values. For rollup columns, formula columns must be simple formula columns, such as this example rollup column.
   :::image type="content" source="media/formula-column-rollup1.png" alt-text="Example simple formula column for a rollup column":::
   :::image type="content" source="media/formula-column-rollup2.png" alt-text="Example rollup column configuration":::
- A formula column, which is dependent on time bound functions `UTCNow()` and `UTCToday()` can't be used in a rollup field.

### Power Fx text function recommendations

- Formula columns don't support `Text()` functions with a single argument of type Number. Number can be whole, decimal, or currency.
   :::image type="content" source="media/formula-column-number.png" alt-text="Formula column with unsupported text function with a number argument":::  
- Formula columns don't support using numbers in the following configurations:
  - In string functions. These are string functions placed wherever a text argument is expected: Upper, Lower, Left, Right, Concatenate, Mid, Len, StartsWith, EndsWith, TrimEnds, Trim, Substitute, and Replace.
  - In the implicit formulas, such as `12 & "foo"`, or `12 & 34`, or `"foo" & 12`.
  - Internal number to text coercion isn't supported. We recommend using `Text(Number, Format)` to convert a number to text. In the case where a `String` argument is passed in a `Text` function then the `Format` argument isn't supported.
  - Here's an example using the `Text` function to convert a number to text and append a string to it:

   ```powerappsfl
   Concatenate(Text(123,"#"),"ab")
   Text(123,"#") & "foo"
   ```
- Locale-specific formatting tokens such as "." and "," aren't supported in formula columns.
  :::image type="content" source="media/formula-column-locale-specific-arg.png" alt-text="Unsupported locale-specific formatting token passed as parameter to Text function in formula":::

### Range validations on formula columns

- You can't set the **Minimum value** or **Maximum value** properties of a formula column.
- All internal computations should lie within the Dataverse range for decimal type formula columns (-100000000000 to 100000000000).
- A hard coded literal value entered in the formula bar should lie within the Dataverse range.  
- If there's a numeric column that's null then it's considered 0 in the intermediate operation. For example, `a+b+c and If a = null, b=2, c=3` then formula column gives `0 + 2 + 3 = 5`.
  - This behavior is different from calculated columns in this case because calculated columns give `null + 2 + 3 = null`.

### General validations on formula columns

- Formula columns can reference other formula columns, but a formula column can't reference itself.
- Formula columns don't support cyclic chains, such as `F1 = F2 + 10, F2 = F1 * 2`.
- Maximum formula expression length in formula columns is 1,000 characters.
- The maximum depth allowed in formula columns is 10. *Depth* is defined as the chain of formula columns referring to other formula or rollup columns.  
  - For example, `table E1, F1 =  1*2, table E2, F2 - E1*2`. In this example, the depth of F2 is 1.
- In model-driven apps, sorting is disabled on:
  - A formula column that contains a column of a related table.
  - A formula column that contains a logical column (for example, address column).
  - A formula column that contains another calculated or formula column.
  - A formula column that uses time-bound function `UTCNow()`.
- Columns of type Whole Number with format Language, Duration, Time Zone aren't supported in formula columns.
- Columns of type String with format Email, Text Area, Ticker Symbol, URL aren't supported in formula columns.
- Formula columns don't display values when the app is in mobile offline mode.
- You can't trigger workflows or plug-ins on formula columns.
- We don't recommend using calculated columns in formula columns and vice versa.
- Duplicate detection rules aren't triggered on formula columns.
- The `Now` function can be used with formula columns. `Now()` has user local behavior and `UTCNow()` has time zone independent behavior.
- You can set the precision property for decimal columns.
- Default formula data type value is set to **Decimal** for numeric value returning formulas.
- Updating whole number formula column's format isn't supported.

### Formula columns of data types that can't be produced

- Currency

## See also

[Types of columns](types-of-fields.md)  <br />

[Microsoft Power Fx overview](/power-platform/power-fx/overview)

[Formula, calculated, and rollup columns using code](../../developer/data-platform/calculated-rollup-attributes.md)
