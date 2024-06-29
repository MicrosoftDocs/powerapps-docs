---
title: Work with Dataverse formula column data types
description: Learn how to create and use dirrent data types in formula columns in Microsoft Dataverse.
author: sanjeevgoyalmsft
reviewer: mattp123
ms.topic: how-to
ms.custom: 
ms.date: 06/28/2024
ms.subservice: teams
ms.author: dikamath
ms.reviewer: matp
ms.collection: bap-ai-copilot
contributors:
  - mattp123
  - sanjeevgoyalmsft
  - neerajatmsft
---

## Create a decimal formula column

Create a formula column that returns a decimal number.

1. When you create a column, enter the following information:
   - A **Display name** for the column.
   - Optionally, enter a **Description** of the column.
1. For **Data type** select ***fx* Formula**.
1. Enter a formula that returns a numeric value in the **Formula** bar.
   This example creates a formula column called *Total Amount*. The *Price Per Unit* column is of decimal data type.
   :::image type="content" source="media/formula-columns-decimal-fd.png" alt-text="Screenshot of a create a new formula column pane for use with a decimal number.":::
1. Expand **Advanced options**, select **Decimal** as the **Formula data type**, and then set the required number of decimal places.
  :::image type="content" source="media/formula-columns-decimal-adv-options.png" alt-text="Screenshot of a decimal formula column definition.":::
1. Select **Save**.

## Create a whole number formula column

Create a formula column that returns a whole number.

1. When you create a column, enter the following information:
   - A **Display name** for the column.
   - Optionally, enter a **Description** of the column.
1. For **Data type** select ***fx* Formula**.
1. Enter a formula that returns a numeric value in the **Formula** bar.
   This example creates a formula column called *Number of Units*. *Total Price* and *Price Per Unit* columns are of decimal data type.
   :::image type="content" source="media/formula-columns-wholenum-fd.png" alt-text="Screenshot of a create a new formula column pane for use with a whole number..":::
1. Expand **Advanced options**, and select **Whole number** as the **Formula data type** and set the required format for whole number column.
  :::image type="content" source="media/formula-columns-wholenum-adv-options.png" alt-text="Screenshot of a whole number formula column definition.":::
1. Select **Save**.

## Create a floating point number formula column

Create a formula column that returns float.

1. When you create a column, enter the following information:
   - A **Display name** for the column.
   - Optionally, enter a **Description** of the column.
1. For **Data type** select ***fx* Formula**.
1. Enter a formula that returns a float value in the **Formula** bar.
   This example creates a formula column called *TestFloat* that uses a ```Float``` function.
   :::image type="content" source="media/formula-columns-float-fd.png" alt-text="Screenshot of a creating float formula column.":::
1. Expand **Advanced options**, and set the required required number of decimal places for float column.
1. Select **Save**.

### Guidelines for creating floating point number formula columns
1. Floating point numbers store an extremely close approximation of the value. It is usually used for storing scientific number values.
2. If at least one operand involved in the arithmetic operation is of Float data type, then result of that formula is of Float type. 
	For e.g., ```1 + 2 + Float(1)``` is of Float type as there is an operand ```Float(1)``` of type Float.
3. A  function that returns numeric value, will yield a result of float type if the first argument provided to the function is of the float type, else it yields the result of Decimal type.
  For e.g., ```Sum(1, 2, Float(1))``` is of Decimal type, whereas ```Sum(Float(1), 1, 2)``` is of Float type.
4. Functions - ```Float```, ```Sqrt```, ```Ln```, ```Power```, ```Exp``` and ```^``` operator returns a Float value.
5. Float data type supports a maximum precision of 5.

## Create a choice formula column
Either global choices or local choice of other simple choice column can be used in result of ```If``` or ```Switch``` to create a choice formula column.

### Using Global Choice
1. Create a global option set. This example creates a global choice called *Color* -
   :::image type="content" source="media/global-choice-def.png" alt-text="Screenshot of a global choice.":::
2. Create formula column using global choice. This example creates a formula column *Color Column* using global choice *Color* created from above step.
   :::image type="content" source="media/formula-columns-global-choice-fd.png" alt-text="Screenshot of a creating global choice formula column.":::

### Using local choice from other simple choice column
1. Create a simple choice column. This example creates a *Simple Color* choice column on *Account* entity.
   :::image type="content" source="media/local-choice-def.png" alt-text="Screenshot of a creating a simple choice column.":::
2. Create formula column on same entity as simple choice column using it's local choice in formula.This example creates a formula column *Color Column 2* on the *Account* entity using local choice column created from above step.
   :::image type="content" source="media/formula-columns-local-choice-fd.png" alt-text="Screenshot of a creating local choice formula column.":::

### Guidelines for working with choices in formula columns
1. Related entity choice column's local choices cannot be used as result type in choice formula columns.
2. Choices used as result in choice formula columns should be from single choice.
3. Choice used by a formula column cannot be updated to use a different choice.
4. OptionSetValue type cannot be passed to String Functions. Value(OptionSetValue) can be used to get numeric value of a choice.
5. Local choice column or global choice cannot be deleted if any formula column is dependent on them.

## See also

[Using the right type of number](types-of-fields.md#using-the-right-type-of-number)  <br />

[Fx Formula Columns](formula-columns.md)

[Microsoft Power Fx overview](/power-platform/power-fx/overview)

[Formula, calculated, and rollup columns using code](../../developer/data-platform/calculated-rollup-attributes.md)
