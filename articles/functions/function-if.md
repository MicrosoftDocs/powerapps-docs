<properties
	pageTitle="PowerApps: If function"
	description="Reference information for the If function in PowerApps, including syntax and examples"
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

# If function in PowerApps #

Returns one value if a condition is true, and another value if not. 

## Description ##

The **If** function tests conditions until a **true** result is found.  The corresponding value is then returned as the result of the function.  

If an odd number of arguments are provided, the value of the last argument is returned if no conditions are satisfied.  *Blank* is returned if an even number arguments are provided.  

## Syntax ##

**If**( *Condition*, *Result* [, *ElseResult* ] )<br>**If**( *Condition1*, *Result1* [, *Condition2*, *Result2*, ... [ , *ElseResult* ] ] )

- *Condition(s)* - Required.  Conditions to test for **true**.
- *Result(s)* - Required.  The corresponding value to return for a condition that is satisfied.
- *ElseResult* - Optional.  The value to return if no conditions are satisfied.  If not specified, *blank* is returned.

