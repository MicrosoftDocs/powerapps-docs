---
title: Concurrent function | Microsoft Docs
description: Reference information, including syntax, for the Concurrent function in PowerApps
author: gregli-msft

ms.service: powerapps
ms.topic: reference
ms.component: canvas
ms.date: 06/12/2018
ms.author: gregli

---
# Concurrent function in PowerApps
Evaluates multiple formulas concurrently with one another.

## Description
The **Concurrent** function evaluates multiple formulas at the same time.  Normally multiple formulas are evaluated by chaining them together with the *;* (or *;;*) operator which evaluates them in order.

Use **Concurrent** to improve performance when loading data in the [**OnStart**](../controls/control-screen.md) of the app.  Rather than waiting for each data call to finish before starting the next and waiting for network latency over and over, you can start the data calls at the same time and overlap the network latency.  Performing multiple data operations concurrently is often done by web browsers for this reason.  

The order in which formulas within the **Concurrent** begin and end evaluation is unpredictable.  Formulas within the **Concurrent** should not contain dependencies on other formulas within the same **Concurrent**.  From within, it is safe to take dependencies on formulas outside the **Concurrent** as they will complete before the **Concurrent** begins.  It is also safe for formulas after the **Concurrent** to take dependencies on formulas within as they will all complete before the **Concurrent** finishes and moves on to the next formula in a chain (using the **;** or **;;** operator).  

If any of the formulas within the **Concurrent** results in an error, the first error encountered is returned.  If all formulas are successful, *true* is returned.

## Syntax
**Concurrent**( *Formula1*, *Formula2* [, ...] )

* *Formula(s)* – Required. Formulas to evaluate concurrently.  At least two formulas must be supplied.

## Examples



#### Display a different random number as user input changes
1. Add a **[Slider](../controls/control-slider.md)** control, and rename it **Slider1** if it has a different name.

1. Add a **[Label](../controls/control-text-box.md)** control, and set its **Text** property to this formula:

    **Slider1.Value + Rand()**

    The label shows **50** (the default value for the slider) plus a random decimal:

    ![A screen displaying a label control with 50.741](media/function-rand/rand-slider-1.png)

1. While holding down the Alt key, change the value of the slider.

    Every time you change the value of the slider, the decimal portion of the label shows a different random number:

    ![Four screens displaying a label control with four different random decimal values for each of four different slider settings 70.899, 84.667, 90.134, 99.690](media/function-rand/rand-slider-results.png)

#### Create a table of random numbers
1. Add a **[Button](../controls/control-button.md)** control, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:

    **ClearCollect( RandomNumbers, ForAll( [ 1, 2, 3, 4, 5 ], Rand() ))**

    This formula creates a single-column table that's used to iterate five times, resulting in five random numbers.

1. Add a **[Data table](../controls/control-data-table.md)**, set its **Items** property to **RandomNumbers**, and show the **Value** field.

    ![A screen showing a data table with five different decimal values 0.857, 0.105, 0.979, 0.167, 0.814](media/function-rand/set-show-data.png)

1. While holding down the Alt key, select the button by clicking or tapping it.

    The data table shows five random decimal numbers:

    ![A screen showing a data table with five different decimal values 0.857, 0.105, 0.979, 0.167, 0.814](media/function-rand/rand-collection-1.png)

1. Select the button again to show a different list of random numbers:

    ![The same screen showing a data table with a new set of five different decimal values 0.414, 0.128, 0.860, 0.303, 0.568](media/function-rand/rand-collection-2.png)

To generate a single random number instead of a table, use **Set( RandomNumber, Rand() )**.
