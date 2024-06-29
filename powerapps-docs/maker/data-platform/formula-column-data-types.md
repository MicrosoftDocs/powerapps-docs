---
title: Work with Dataverse formula column data types
description: Learn how to create and use different data types in formula columns.
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
# Formula column data types

## Create a decimal formula column

Create a formula column that returns a decimal number.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a numeric value in the **Formula** bar.
   This example creates a formula column called *Total Amount*. The *Price Per Unit* column is of decimal data type.
   :::image type="content" source="media/formula-columns-decimal-fd.png" alt-text="Screenshot of a create a new formula column pane for use with a decimal number.":::
1. Expand **Advanced options**, select **Decimal** as the **Formula data type**, and then set the required number of decimal places.
  :::image type="content" source="media/formula-columns-decimal-adv-options.png" alt-text="Screenshot of a decimal formula column definition.":::
1. Select **Save**.

## Create a whole number formula column

Create a formula column that returns a whole number.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a numeric value in the **Formula** bar.
   This example creates a formula column called *Number of Units*. *Total Price* and *Price Per Unit* columns are of decimal data type.
   :::image type="content" source="media/formula-columns-wholenum-fd.png" alt-text="Screenshot of a create a new formula column pane for use with a whole number..":::
1. Expand **Advanced options**, and select **Whole number** as the **Formula data type** and set the required format for whole number column.
  :::image type="content" source="media/formula-columns-wholenum-adv-options.png" alt-text="Screenshot of a whole number formula column definition.":::
1. Select **Save**.

## Create a floating point number formula column

Create a formula column that returns float.

1. Select **Data type** as ***fx* Formula**.
1. Enter a formula that returns a floating point number in the **Formula** bar.
   This example creates a formula column called *TestFloat*.
   :::image type="content" source="media/formula-columns-float-fd.png" alt-text="Screenshot of a creating float formula column.":::
1. Expand **Advanced options**, and set the required required number of decimal places.
1. Select **Save**.

### Guidelines for creating floating point number formula columns
1. Floating point numbers store an extremely close approximation of a value. It is usually used for storing scientific numeric values.
2. If one of the operand involved in an arithmetic operation is of float type, then result of the formula will be float type. 
   E.g., ```1 + 2 + Float(1)``` as it uses a float type operand - ```Float(1)```.
3. A numeric function returns float value if first parameter provided to the function is of float type, else the function returns a decimal value.
   E.g., ```Sum(1, 2, Float(1))``` is of decimal type and ```Sum(Float(1), 1, 2)``` is of float type.
4. ```Float```, ```Sqrt```, ```Ln```, ```Power```, ```Exp``` functions and ```^``` operator returns a float value.
5. Float formula columns support a maximum precision of 5.

## Create a choice formula column
To create a choice formula column, either global choice or local choice of a simple choice column can be used as a result in ```If``` or ```Switch``` functions.

### Using global choice
1. Create a global choice. This example creates a global choice called *Color*.
   :::image type="content" source="media/global-choice-def.png" alt-text="Screenshot of a global choice.":::
2. Create a formula column using global choice. This example creates a formula column *Color Column* using global choice *Color* created from above step.
   :::image type="content" source="media/formula-columns-global-choice-fd.png" alt-text="Screenshot of a creating global choice formula column.":::

### Using local choice from a simple choice column
1. Create a simple choice column. This example creates a *Simple Color* choice column on *Account* entity.
   :::image type="content" source="media/local-choice-def.png" alt-text="Screenshot of a creating a simple choice column.":::
2. Create formula column on the same entity as simple choice column using simple choice column's local choice in the formula. This example creates a formula column *Color Column 2* on *Account* entity using local choice column created from the above step.
   :::image type="content" source="media/formula-columns-local-choice-fd.png" alt-text="Screenshot of a creating local choice formula column.":::

### Guidelines for working with choices in formula columns
1. Local choices of related entity's simple choice column cannot be used as result type in formula columns.
2. Options from same option set should be used for all result arguments in choice formula columns.
3. A choice used by a formula column cannot be updated.
4. Options of a choice cannot be passed as an argument to string functions. Value function can be used to return numeric value of an option.
5. Formula columnn's dependent local choice column or global choice cannot be deleted.

## See also

[Using the right type of number](types-of-fields.md#using-the-right-type-of-number)  <br />

[Fx Formula Columns](formula-columns.md)

[Microsoft Power Fx overview](/power-platform/power-fx/overview)

[Formula, calculated, and rollup columns using code](../../developer/data-platform/calculated-rollup-attributes.md)
