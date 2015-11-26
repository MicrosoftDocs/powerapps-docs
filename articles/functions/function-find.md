<properties
	pageTitle="PowerApps: Find function"
	description="Reference information for the Find function in PowerApps, including syntax and examples"
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

# Find function in PowerApps #

Finds a string within another string.

## Description ##

The **Find** function looks for a string within another string.

**Find** is case sensitive.  To perform a case insensitive search, first use the **[Lower](function-lower-upper-proper.md)** function on the arguments.

**Find** returns the starting position of the string that was found.  Position 1 is the first character of the string.  **Find** will return *blank* if no match was found.

## Syntax ##

**Find**( *FindString*, *WithinString* [, *StartingPosition* ] )

- *FindString* - Required.  The string to find.
- *WithinString* - Required.  The string to search within.
- *StartingPosition* - Optional.  The starting position to start searching.  Position 1 is the first character.

