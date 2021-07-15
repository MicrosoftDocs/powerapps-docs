---
title: And, Or, and Not functions in Power Apps
description: Reference information including syntax and examples for the And, Or, and Not functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 05/23/2019
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# And, Or, and Not functions in Power Apps

Boolean logic functions, commonly used to manipulate the results of comparisons and tests.

## Description

The **And** function returns **true** if all of its arguments are **true**.

The **Or** function returns **true** if any of its arguments are **true**.

The **Not** function returns **true** if its argument is **false**; it returns **false** if its argument is **true**.

These functions work the same way as they do in Excel. You can also use [operators](operators.md) to perform these same operations, using either Visual Basic or JavaScript syntax:

| Function notation | Visual Basic operator notation | JavaScript operator notation |
| -------------|------------|--------|
| **And( x, y )** | **x And y** | **x && y** |
| **Or( x, y )** | **x Or y** | **x &#124;&#124; y** |
| **Not( x )** | **Not x** | **! x** |

These functions work with logical values. You can't pass them a number or a string directly; instead, you must make a comparison or a test. For example, this logical formula **x > 1** evaluates to the Boolean value **true** if **x** is greater than **1**. If **x** is less than **1**, the formula evaluates to **false**.

## Syntax

**And**( *LogicalFormula1*, *LogicalFormula2* [, *LogicalFormula3*, ... ] )<br>
**Or**( *LogicalFormula1*, *LogicalFormula2* [, *LogicalFormula3*, ... ] )<br>
**Not**( *LogicalFormula* )

- *LogicalFormula(s)* - Required.  Logical formulas to evaluate and operate on.

## Examples

The examples in this section use these global variables:

- **a** = *false*
- **b** = *true*
- **x** = 10
- **y** = 100
- **s** = "Hello World"

To create these global variables in an app, insert a [**Button**](../controls/control-button.md) control, and set its **OnSelect** property to this formula:

```powerapps-dot
Set( a, false ); Set( b, true ); Set( x, 10 ); Set( y, 100 ); Set( s, "Hello World" )
```

Select the button (by clicking it while you hold down the Alt key), and then set the **Text** property of a [**Label**](../controls/control-text-box.md) control to a formula in the first column of the next table.

| Formula | Description | Result |
|---------|-------------|--------|
| **And( a, b )** | Tests the values of **a** and **b**.  One of the arguments is *false*, so the function returns *false*. | *false* |
| **a And b** | Same as the previous example, using Visual Basic notation. | *false* |
| **a && b** | Same as the previous example, using JavaScript notation. | *false* |
| **Or( a, b )** | Tests the values of **a** and **b**. One of the arguments is *true*, so the function returns *true*. | *true* |
| **a Or b** | Same as the previous example, using Visual Basic notation. | *true* |
| **a &#124;&#124; b** | Same as the previous example, using JavaScript notation. | *true* |
| **Not( a )** | Tests the value of **a**. The argument is *false*, so the function returns the opposite result. | *true* |
| **Not a** | Same as the previous example, using Visual Basic notation. | *true* |
| **! a** | Same as the previous example, using JavaScript notation. | *true* |
| **Len(&nbsp;s&nbsp;)&nbsp;<&nbsp;20 And&nbsp;Not&nbsp;IsBlank(&nbsp;s&nbsp;)** | Tests whether the length of **s** is less than 20 and whether it isn't a **blank** value. The length is less than 20, and the value isn't blank. Therefore, the result is *true*. | *true* |
| **Or(&nbsp;Len(&nbsp;s&nbsp;)&nbsp;<&nbsp;10, x&nbsp;<&nbsp;100, y&nbsp;<&nbsp;100&nbsp;)** | Tests whether the length of **s** is less than 10, whether **x** is less than 100, and whether **y** is less than 100. The first and third arguments are false, but the second one is true. Therefore, the function returns *true*. | *true* |
| **Not IsBlank(&nbsp;s&nbsp;)** | Tests whether **s** is *blank*, which returns *false*. **Not** returns the opposite of this result, which is *true*. | *true* |

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]