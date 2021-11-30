---
title: Find function in Power Apps
description: Reference information including syntax and examples for the Find function in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/07/2015
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - tapanm-msft
---
# Find function in Power Apps
Finds a string of text, if it exists, within another string.

## Description
The **Find** function looks for a string within another string and is case sensitive. To ignore case, first use the **[Lower](function-lower-upper-proper.md)** function on the arguments.

**Find** returns the starting position of the string that was found.  Position 1 is the first character of the string. **Find** returns *blank* if the string in which you're searching doesn't contain the string for which you're searching.

## Syntax
**Find**( *FindString*, *WithinString* [, *StartingPosition* ] )

* *FindString* - Required.  The string to find.
* *WithinString* - Required.  The string to search within.
* *StartingPosition* - Optional.  The starting position to start searching.  Position 1 is the first character.



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]