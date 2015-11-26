<properties
	pageTitle="PowerApps: Round, RoundDown, and RoundUp functions"
	description="Reference information for the Round, RoundDown, and RoundUp functions in PowerApps, including syntax and examples"
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

# Round, RoundDown, and RoundUp functions in PowerApps #

Rounds a number.

## Description ##

The **Round**, **RoundDown**, and **RoundUp** functions round a number to the specified number of decimal places:

- **Round** rounds up if the next digit is a 5 is higher, and rounds down otherwise.
- **RoundDown** always rounds down to the previous lower number.
- **RoundUp** always rounds up to the next higher number.

If you pass a single number, the return value is the rounded version of that number.  If you pass a single-column [table](working-with-tables.md) that contains numbers, the return value is a single-column table of rounded numbers. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.

## Syntax ##

**Round**( *Number*, *DecimalPlaces* )<br>**[Upper](function-lower-upper-proper.md)**( *Number*, *DecimalPlaces* )<br>**[Proper](function-lower-upper-proper.md)**( *Number*, *DecimalPlaces* )

- *Number* - Required. The number to round.
- *DecimalPlaces* - Required.  The number of places to the right of the decimal point to round to.  Use 0 to round to a whole number.  

