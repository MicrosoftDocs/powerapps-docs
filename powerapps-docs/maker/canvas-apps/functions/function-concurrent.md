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
The **Concurrent** function evaluates multiple formulas at the same time.  Normally multiple formulas are evaluated by chaining them together with the [*;*](operators.md) (or [*;;*](operators.md)) operator which evaluates each sequentially in order.  The result of performing operations concurrently versus sequentially is the same; the only difference is the amount of elapsed wall time the user will need to wait.

Use **Concurrent** to improve performance when loading data in the [**OnStart**](../controls/control-screen.md) of your app.  Rather than waiting for each data call to finish before starting the next and incurring the network latency cost over and over, you can start the data calls at the same time and overlap the network latency.  Performing multiple data operations concurrently is often done by web browsers for greater performance.  

The order in which formulas within the **Concurrent** begin and end evaluation is unpredictable.  Formulas within the **Concurrent** should not contain dependencies on other formulas within the same **Concurrent**.  From within, it is safe to take dependencies on formulas outside the **Concurrent** as they will complete before the **Concurrent** begins.  It is also safe for formulas after the **Concurrent** to take dependencies on formulas within as they will all complete before the **Concurrent** finishes and moves on to the next formula in a chain (using the **;** or **;;** operator).  Watch out for subtle order dependencies if you are calling service methods that have side effects.

If any of the formulas within the **Concurrent** results in an error, the first error encountered is returned.  If all formulas are successful, *true* is returned.

**Concurrent** can only be used in [behavior formulas](../working-with-formulas-in-depth.md).

## Syntax
**Concurrent**( *Formula1*, *Formula2* [, ...] )

* *Formula(s)* – Required. Formulas to evaluate concurrently.  At least two formulas must be supplied.

## Examples

1. Create a new app.

2. Add four different data sources from the Common Data Service for apps, SQL Server, or SharePoint.  In this example, we are using four tables from the [sample Adventure Works database on SQL Azure](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-get-started-portal).

2. Add a **[Button](../controls/button.md)** control, and set its **OnSelect** property to this formula:

	**ClearCollect( Product, '[SalesLT].[Product]' ); 
	ClearCollect( Customer, '[SalesLT].[Customer]' ); 
	ClearCollect( SalesOrderDetail, '[SalesLT].[SalesOrderDetail]' ); 
	ClearCollect( SalesOrderHeader, '[SalesLT].[SalesOrderHeader]' )**

3. Both [Microsoft Edge](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/network) and [Google Chrome](https://developers.google.com/web/tools/chrome-devtools/network-performance/) offer developer tools to monitor network traffic while your app is running.  Turn this on in your browser.  You may want to also turn on network throttling to exaggerate the effects of this comparison.  

4. Press the button.  Watch the network traffic.  You will see four requests performed in series similar to this:

	![Time graph of four network requests, one starting after the last, covering the entire span of time](media/function-concurrent/chained-network.png)

5. Save and close the app.  As data is cached by PowerApps, hitting the button again will not necessarily cause four new requests.  Each time you want to test the performance again, you will need to close and reopen your app.  If you turned on network throttling, you may want to turn it off until you are ready for another test.

1. Add a second **[Button](../controls/button.md)** control, and set its **OnSelect** property to this formula:

	**Concurrent( 
	&nbsp;&nbsp;&nbsp;&nbsp;ClearCollect( Product, '[SalesLT].[Product]' ), 
	&nbsp;&nbsp;&nbsp;&nbsp;ClearCollect( Customer, '[SalesLT].[Customer]' ), 
	&nbsp;&nbsp;&nbsp;&nbsp;ClearCollect( SalesOrderDetail, '[SalesLT].[SalesOrderDetail]' ), 
	&nbsp;&nbsp;&nbsp;&nbsp;ClearCollect( SalesOrderHeader, '[SalesLT].[SalesOrderHeader]' ) 
	)**

	Note that these are the same **ClearCollect** calls as with the first button, but they are wrapped in a Concurrent function and separated by commas.

2. Clear the network monitor in the browser.  If you were using network throttling before, turn it on again now.

3. Press the second button.   Watch the network traffic.  You will see four requests performed concurrently similar to this:

	![Time graph of four network requests, all four starting together, covering about half of the span of time](media/function-concurrent/concurrent-network.png)

	These two network graphs are on the same scale.  Using **Concurrent** the wall time required to perform these four operations is about half of what it was for the sequential chaining operator. 

5. Save and close the app.   