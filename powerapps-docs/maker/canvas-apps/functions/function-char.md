---
title: Char function | Microsoft Docs
description: Reference information for the Char function in PowerApps, including syntax and examples
documentationcenter: na
author: gregli-msft
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.component: canvas
ms.date: 11/07/2015
ms.author: gregli

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

