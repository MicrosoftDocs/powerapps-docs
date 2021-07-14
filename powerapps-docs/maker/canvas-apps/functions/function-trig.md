---
title: Acos, Acot, Asin, Atan, Atan2, Cos, Cot, Degrees, Pi, Radians, Sin, and Tan functions in Power Apps
description: Reference information including syntax and examples for the Acos, Acot, Asin, Atan, Atan2, Cos, Cot, Degrees, Pi, Radians, Sin, and Tan functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 09/13/2016
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Acos, Acot, Asin, Atan, Atan2, Cos, Cot, Degrees, Pi, Radians, Sin, and Tan functions in Power Apps
Calculates trigonometric values.

## Description
### Primary functions
The **Cos** function returns the cosine of its argument, an angle specified in radians.

The **Cot** function returns the cotangent of its argument, an angle specified in radians.

The **Sin** function returns the sine of its argument, an angle specified in radians.

The **Tan** function returns the tangent of its argument, an angle specified in radians.

### Inverse functions
The **Acos** function returns the arccosine, or inverse cosine, of its argument. The arccosine is the angle whose cosine is the argument.  The returned angle is given in radians in the range 0 (zero) to &pi;.

The **Acot** function returns the principal value of the arccotangent, or inverse cotangent, of its argument.  The returned angle is given in radians in the range 0 (zero) to &pi;.

The **Asin** function returns the arcsine, or inverse sine, of its argument. The arcsine is the angle whose sine is the argument.  The returned angle is given in radians in the range -&pi;/2 to &pi;/2.

The **Atan** function returns the arctangent, or inverse tangent, of its argument. The arctangent is the angle whose tangent is the argument. The returned angle is given in radians in the range -&pi;/2 to &pi;/2.

The **Atan2** function returns the arctangent, or inverse tangent, of the specified *x* and *y* coordinates as arguments. The arctangent is the angle from the *x*-axis to a line that contains the origin (0, 0) and a point with coordinates (*x*, *y*). The angle is given in radians between -&pi; and &pi;, excluding -&pi;.  A positive result represents a counterclockwise angle from the *x*-axis; a negative result represents a clockwise angle.  **Atan2(&nbsp;*a*,&nbsp;*b*&nbsp;)** equals **Atan(&nbsp;*b*/*a*&nbsp;)**, except that ***a*** can equal 0 (zero) with the **Atan2** function.

### Helper functions
The **Degrees** function converts radians to degrees.  &pi; radians equals 180 degrees.

The **Pi** function returns the transcendental number &pi;, which begins 3.141592...

The **Radians** function converts degrees to radians.  

### Notes
If you pass a single number to these functions, the return value is a single result.  If you pass a single-column [table](../working-with-tables.md) that contains numbers, the return value is a single-column table of results, one result for each record in the argument's table. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.  

If an argument would result in an undefined value, the result is *blank*.  This can happen, for example, when using inverse functions with arguments that are out of range.

## Syntax
### Primary Functions
**Cos**( *Radians* )<br>**Cot**( *Radians* )<br>**Sin**( *Radians* )<br>**Tan**( *Radians* )

* *Radians* - Required. Angle to operate on.

**Cos**( *SingleColumnTable* )<br>**Cot**( *SingleColumnTable* )<br>**Sin**( *SingleColumnTable* )<br>**Tan**( *SingleColumnTable* )

* *SingleColumnTable* - Required. A single-column table of angles to operate on.

### Inverse Functions
**Acos**( *Number* )<br>**Acot**( *Number* )<br>**Asin**( *Number* )<br>**Atan**( *Number* )

* *Number* - Required. Number to operate on.

**Acos**( *SingleColumnTable* )<br>**Acot**( *SingleColumnTable* )<br>**Asin**( *SingleColumnTable* )<br>**Atan**( *SingleColumnTable* )

* *SingleColumnTable* - Required. A single-column table of numbers to operate on.

**Atan2**( *X*, *Y* )

* *X* - Required.  *X*-axis coordinate.
* *Y* - Required.  *Y*-axis coordinate.

### Helper Functions
**Degrees**( *Radians* )

* *Radians* - Required.  Angle in radians to convert to degrees.

**Pi**()

**Radians**( *Degrees* )

* *Degrees* - Required.  Angle in degrees to convert to radians.

## Examples
### Single number

| Formula | Description | Result |
| --- | --- | --- |
| **Cos(&nbsp;1.047197&nbsp;)** |Returns the cosine of 1.047197 radians or 60 degrees. |0.5 |
| **Cot(&nbsp;Pi()/4&nbsp;)** |Returns the cotangent of 0.785398... radians or 45 degrees. |1 |
| **Sin(&nbsp;Pi()/2&nbsp;)** |Returns the sine of 1.570796... radians or 90 degrees. |1 |
| **Tan(&nbsp;Radians(60)&nbsp;)** |Returns the tangent of 1.047197... radians or 60 degrees. |1.732050... |
| **Acos(&nbsp;0.5&nbsp;)** |Returns the arccosine of 0.5, in radians. |1.047197... |
| **Acot(&nbsp;1&nbsp;)** |Returns the arccotangent of 1, in radians. |0.785398... |
| **Asin(&nbsp;1&nbsp;)** |Returns the arcsine of 1, in radians. |1.570796... |
| **Atan(&nbsp;1.732050&nbsp;)** |Returns the arctangent of 1.732050, in radians. |1.047197... |
| **Atan2(&nbsp;5,&nbsp;3&nbsp;)** |Returns the arctangent of the angle from the *x*-axis of the line that contains the origin (0,0) and the coordinate (5,3), which is approximately 31 degrees. |0.540419... |
| **Atan2(&nbsp;4,&nbsp;4&nbsp;)** |Returns the arctangent of the angle from the *x*-axis of the line that contains the origin (0,0) and the coordinate (4,4), which is exactly &pi;/4 radians or 45 degrees. |0.785398... |
| **Degrees(&nbsp;1.047197&nbsp;)** |Returns the equivalent number of degrees for 1.047197 radians. |60 |
| **Pi()** |Returns the transcendental number &pi;. |3.141592... |
| **Radians(&nbsp;15&nbsp;)** |Returns the equivalent number of radians for 15 degrees. |0.261799... |

### Single-column table
The examples in this section use a [data source](../working-with-data-sources.md) that's named **ValueTable** and that contains the following data.  The last record in the table is &pi;/2 radians or 90 degrees.

![List of values.](media/function-trig/values.png)

| Formula | Description | Result |
| --- | --- | --- |
| **Cos(&nbsp;ValueTable&nbsp;)** |Returns the cosine of each number in the table. | ![Cos.](media/function-trig/values-cos.png) |
| **Cot(&nbsp;ValueTable&nbsp;)** |Returns the cotangent of each number in the table. | ![Cot.](media/function-trig/values-cot.png) |
| **Sin(&nbsp;ValueTable&nbsp;)** |Returns the sine of each number in the table. | ![Sin.](media/function-trig/values-sin.png) |
| **Tan(&nbsp;ValueTable&nbsp;)** |Returns the tangent of each number in the table. | ![Tan.](media/function-trig/values-tan.png) |
| **Acos(&nbsp;ValueTable&nbsp;)** |Returns the arccosine of each number in the table. | ![Acos.](media/function-trig/values-acos.png) |
| **Acot(&nbsp;ValueTable&nbsp;)** |Returns the arccotangent of each number in the table. | ![Acot.](media/function-trig/values-acot.png) |
| **Asin(&nbsp;ValueTable&nbsp;)** |Returns the arcsine of each number in the table. | ![Asin.](media/function-trig/values-asin.png) |
| **Atan(&nbsp;ValueTable&nbsp;)** |Returns the arctangent of each number in the table. | ![Atan.](media/function-trig/values-atan.png) |
| **Degrees(&nbsp;ValueTable&nbsp;)** |Returns the equivalent number of degrees for each number in the table, assumed to be angles in radians. | ![Degrees.](media/function-trig/values-degrees.png) |
| **Radians(&nbsp;ValueTable&nbsp;)** |Returns the equivalent number of radians for each number in the table, assumed to be angles in degrees. | ![Radians.](media/function-trig/values-radians.png) |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]