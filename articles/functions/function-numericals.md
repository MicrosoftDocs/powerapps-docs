<properties
	pageTitle="PowerApps: Abs and Sqrt functions"
	description="Reference information for the Abs and Sqrt functions in PowerApps, including syntax and examples"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# Abs and Sqrt functions in PowerApps #

Numerical functions.

## Description ##

The **Abs** function returns the non-negative value of its argument.  If a number is negative, **Abs** returns the positive equivalent.

The **Sqrt** function returns the number, that when multiplied by itself, equals its argument.

If you pass a single number, the return value is the converted version of that string.  If you pass a single-column [table](working-with-tables.md) that contains numbers, the return value is a single-column table of answers. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.  

## Syntax ##

**Abs**( *Number* )<br>**Sqrt**( *Number* )

- *Number* - Required. Number to be operated on.

**Abs**( *SingleColumnTable* )<br>**Sqrt**( *SingleColumnTable* )

- *Number* - Required. A single-column table of numbers to operate on.

## Examples ##

### Single number ###

| Formula | Description | Result |
|---------|-------------|--------|
| **Abs( -55 )** | Returns the number without the negative sign. | 55 |
| **Sqrt( 9 )** | Returns the number, that when multiplied by itself, results in 9. | 3 |

### Single-column table
The examples in this section use this [data source](working-with-data-sources.md), named **ValueTable**:

![](media/function-numericals/values.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Abs( ValueTable )** | Returns the absolute values of each number in the table. | <style> img { max-width: none } </style> ![](media/function-numericals/values-abs.png) |
| **Sqrt( ValueTable )** | Returns the square root of each number in the table | ![](media/function-numericals/values-sqrt.png) |

### Step-by-step example ###

1.Add an input-text control, and name it Source.

2.Add a label, and set its Text property to this function:

- **Sqrt( Value( Source!Text ) )**

3.Type a number into the input-text control, and confirm that the label shows the square root of the number that you typed.
