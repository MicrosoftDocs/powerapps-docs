---
title: Work with Dataverse formula column data types
description: Learn how to create and use decimal, whole number, float, and choice data types in formula columns.
author: sanjeevgoyalmsft
reviewer: mattp123
ms.topic: how-to
ms.custom: 
ms.date: 08/16/2024
ms.subservice: teams
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
1. Select the **Columns** area, and then select **New column**, and then select the data type and enter the Power Fx formula to create any of the following:

   - [Create a decimal formula column](#create-a-decimal-formula-column)
   - [Create a whole number formula column](#create-a-whole-number-formula-column)
   - [Create a floating point number formula column](#create-a-floating-point-number-formula-column)
   - [Create a choice formula column](#create-a-choice-formula-column)

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
1. Expand **Advanced options**, and set the required number of decimal places.
1. Select **Save**.

### Guidelines for creating floating point number formula columns

- Floating point numbers store an extremely close approximation of a value. Floats are typically used for storing scientific numeric values.
- If an operand involved in an arithmetic operation is of float type, then the result of the formula is of float type. For example:
   - ```1 + 2 + Float(1)``` as it uses a float type operand - ```Float(1)```.
- A numeric function returns a float value when the first parameter provided to the function is of float type. Otherwise, the function returns a decimal value. For example:
  - ```Sum(1, 2, Float(1))``` is of decimal type and ```Sum(Float(1), 1, 2)``` is of float type.
- ```Float```, ```Sqrt```, ```Ln```, ```Power```, ```Exp``` functions and the ```^``` operator return a float value.
- Float formula columns support a maximum precision of 5.

## Create a choice formula column

To create a choice formula column, either global choice or local choice of a simple choice column can be used as a result in ```If``` or ```Switch``` functions.

### Using global choice

1. Create a [global choice](custom-picklists.md). This example creates a global choice with a **Display name** that's *Color*.
1. Add the following **Choices**:
   - **Label**: *Red* **Value**: '*858,170,0000*'
   - **Label**: *Pink* **Value**: *858,170,001*
   - **Label**: *Yellow* **Value**: 858,170,002
   - **Label**: *Blue* **Value**: *858,170,003*
   :::image type="content" source="media/global-choice-def.png" alt-text="Screenshot of a global choice.":::
1. Create a formula column using the global choice. This example creates a formula column *Color Column* using the global choice *Color* created from the previous step.
   :::image type="content" source="media/formula-columns-global-choice-fd.png" alt-text="Screenshot of a creating global choice formula column.":::
1. Select **Save**. Notice that the column created is of data type **Choice fx**.

### Using local choice from a simple choice column

1. Create a simple choice column. This example creates a *Simple Color* choice column on the *Account* table.
   :::image type="content" source="media/local-choice-def.png" alt-text="Screenshot of a creating a simple choice column.":::
2. Create formula column on the same entity as simple choice column using simple choice column's local choice in the formula. This example creates a formula column *Color Column 2* on *Account* entity using local choice column created from the previous step.
   :::image type="content" source="media/formula-columns-local-choice-fd.png" alt-text="Screenshot of a creating local choice formula column.":::

### Guidelines for working with choices in formula columns

- Local choices of a related table's simple choice column can't be used as result type in formula columns.
- Options from the same choice column should be used for all result arguments in choice formula columns.
- A choice used by a formula column can't be updated.
- Options of a choice can't be passed as an argument to string functions. Value function can be used to return numeric a value of an option.
- A formula column's dependent local choice column or global choice can't be deleted.

## See also

[Using the right type of number](types-of-fields.md#using-the-right-type-of-number)  <br />

[Fx Formula Columns](formula-columns.md)

[Microsoft Power Fx overview](/power-platform/power-fx/overview)

[Formula, calculated, and rollup columns using code](../../developer/data-platform/calculated-rollup-attributes.md)
