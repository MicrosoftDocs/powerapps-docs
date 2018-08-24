---
title: Char function | Microsoft Docs
description: Reference information for the Char function in PowerApps, including syntax and examples
dauthor: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Char function in PowerApps
Translates a character code into a string.

## Description
The **Char** function returns a string that contains the appropriate ASCII character for your platform.

## Syntax
**Char**( *CharacterCode* )

* *CharacterCode* - Required. ASCII character code to translate.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **Char( 65 )** |Returns the character that corresponds to ASCII code 65. |A |
| **Char( 105 )** |Returns the character that corresponds to ASCII code 105. |i |
| **Char( 35 )** |Returns the character that corresponds to ASCII code 35. |# |

