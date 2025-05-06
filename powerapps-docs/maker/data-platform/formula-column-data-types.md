---
title: Work with Dataverse formula column data types
description: Learn how to create and use decimal, whole number, float, and choice data types in formula columns.
author: sanjeevgoyalmsft
reviewer: mattp123
ms.topic: how-to
ms.custom: 
ms.date: 01/06/2025
ms.subservice: dataverse-maker
ms.author: dikamath
ms.reviewer: matp
ms.collection: bap-ai-copilot
ai-usage: ai-assisted
contributors:
  - mattp123
  - sanjeevgoyalmsft
  - neerajatmsft
---
# Create formula columns with decimal, whole number, float, and choice data types

This article provides guidance on creating and using different data types in Microsoft Dataverse formula columns, such as decimal, whole number, floating point, and choice columns. It outlines steps starting with selecting **fx Formula** as the data type and entering a numeric value-returning formula in the formula bar.

## Start by creating a column for a table

1. Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Tables**, and then select the table where you want to add a formula column. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the **Columns** area, select **New column**, and then select the data type and enter the Power Fx formula. Depending on the formula you enter, you can create any of the following:

   - [Decimal formula column](#create-a-decimal-formula-column)
   - [Whole number formula column](#create-a-whole-number-formula-column)
   - [Floating point number formula column](#create-a-floating-point-number-formula-column)
   - [Choice formula column](#create-a-choice-formula-column)

## Create a decimal formula column

Create a formula column that returns a decimal number.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a numeric value in the **Formula** bar.
   This example creates a formula column called *Total Amount*. The *Price Per Unit* column is of decimal data type.
   :::image type="content" source="media/formula-columns-decimal-fd.png" alt-text="Screenshot of a create a new formula column pane for use with a decimal number using 'Price Per Unit' * 150.":::
1. Expand **Advanced options**, and then set the required number of decimal places.
  :::image type="content" source="media/formula-columns-decimal-adv-options.png" alt-text="Screenshot of a decimal formula column definition.":::
1. Select **Save**. By default, **Formula data type** is set to **Decimal** and a decimal formula field is created.

## Create a whole number formula column

Create a formula column that returns a whole number.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a numeric value in the **Formula** bar.
   This example creates a formula column called *Number of Units*. *Total Price* and *Price Per Unit* columns are of decimal data type.
   :::image type="content" source="media/formula-columns-wholenum-fd.png" alt-text="Screenshot of a create a new formula column pane for use with a whole number.":::
1. Expand **Advanced options**, and select **Whole number** as the **Formula data type** and set the required format for whole number column.
  :::image type="content" source="media/formula-columns-wholenum-adv-options.png" alt-text="Screenshot of a whole number formula column definition using 'Total Price' / 'Price Per Unit'.":::
1. Select **Save**.

## Create a floating point number formula column

Create a formula column that returns float.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a floating point number in the **Formula** bar.
Enter a formula that returns a floating point number in the **Formula** bar. This example creates a formula column called *Total Price*. *Weight* is a simple float column and *Price Per Gm* is a simple decimal column.
:::image type="content" source="media/formula-columns-float-fd.png" alt-text="Screenshot of a creating float formula column":::
1. Expand **Advanced options**, and set the required number of decimal places.
1. Select **Save**.

### Guidelines for creating floating point number formula columns

- If an operand involved in an arithmetic operation is of float type, then the result of the formula is of float type. For example:
   - ```1 + 2 + Float(1)``` as it uses a float type operand - ```Float(1)```.
- A numeric function returns a float value when the first parameter provided to the function is of float type. Otherwise, the function returns a decimal value. For example:
  - ```Sum(1, 2, Float(1))``` is of decimal type and ```Sum(Float(1), 1, 2)``` is of float type.
- ```Float```, ```Sqrt```, ```Ln```, ```Power```, ```Exp``` functions and the ```^``` operator return a float value.

## Create a choice formula column

To create a choice formula column, either global choice or local choice of a simple choice column can be used as result.

### Using global choice

Create a global choice. This example creates a global choice called *Task Priority*.

:::image type="content" source="media/global-choice-def.png" alt-text="Screenshot of a global choice.":::

Create a formula column that returns a choice using a global choice.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a choice value in the **Formula** bar.
   This example creates a formula column *Priority* using global choice *Task Priority*.
   :::image type="content" source="media/formula-columns-global-choice-fd.png" alt-text="Screenshot of a creating global choice formula column.":::
1. Select **Save**.  Notice that the column created is of data type **Choice fx**.

### Using local choice from a simple choice column

Create a simple choice column. This example creates a *Task Priority* simple choice column for the account table.

:::image type="content" source="media/local-choice-def.png" alt-text="Screenshot of a creating a simple choice column.":::

Create a formula column that returns choice using a local choice of a simple choice column.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a choice value in the **Formula** bar.
   This example creates a formula column *Priority* on *Account* entity using local choice of a choice column *Task Priority* for the account table.
   :::image type="content" source="media/formula-columns-local-choice-fd.png" alt-text="Screenshot of a creating local choice formula column.":::
1. Select **Save**.

### Guidelines for working with choices in formula columns

- Local choices of related table's simple choice column can't be used as a result type in formula columns.
- Options from the same option set should be used for all result arguments in choice formula columns.
- A choice used by a formula column can't be updated.
- Options of a choice can't be passed as an argument to string functions. Value function can be used to return the numeric value of an option.
- Formula column's dependent local choice column or global choice can't be deleted.
- For using a related table local choices (optionset) column's options in the formula column definition, first use choice and then use options of that local choice.
  
  For example, a choice column named *Color* on the **Contact** table.
  :::image type="content" source="../model-driven-apps/media/choice-column-sample1.png" alt-text="Choice column for related contact table named color.":::
  The choice column has options Red, Yellow, and Green.
  :::image type="content" source="../model-driven-apps/media/choice-column-sample2.png" alt-text="Choice column with options red, yellow, and green.":::
  For a formula column on the account table using the *Color* choice column, the formula appears like this:
  
  **Recommended** - `If(ParentAccount.Color == 'Color (Accounts)'.Red, 1, 2)`
  
  **Not Recommended** - `If( 'Color (Accounts)'.Red == ParentAccount.Color, 1, 2)`
  :::image type="content" source="../model-driven-apps/media/choice-column-sample3.png" alt-text="Formula for choice column":::

## See also

[Using the right type of number](types-of-fields.md#using-the-right-type-of-number)  <br />

[Fx Formula Columns](formula-columns.md)

[Microsoft Power Fx overview](/power-platform/power-fx/overview)

[Formula, calculated, and rollup columns using code](../../developer/data-platform/calculated-rollup-attributes.md)

[Create formula columns with decimal (video)](https://youtu.be/NmpPG0_sPX0?feature=shared)
