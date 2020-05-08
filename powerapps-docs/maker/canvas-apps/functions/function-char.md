---
title: Char function | Microsoft Docs
description: Reference information for the Char function in Power Apps, including syntax and examples
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/01/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Char function in Power Apps

Translates a character code into a string.

## Description

The **Char** function translates a number into a string with the corresponding ASCII character.

## Syntax

**Char**( *CharacterCode* )

- *CharacterCode* - Required. ASCII character code to translate.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **Char( 65 )** |Returns the character that corresponds to ASCII code 65. |"A" |
| **Char( 105 )** |Returns the character that corresponds to ASCII code 105. |"i" |
| **Char( 35 )** |Returns the character that corresponds to ASCII code 35. |"#" |

### Display a character map

1. On an empty screen in a tablet app, add a [**Gallery**](../controls/control-gallery.md) control with a **Blank Horizontal** layout, and then set these properties:

    - **Items**: `[0,1,2,3,4,5,6,7]`
    - **Width**: 800
    - **Height**: 500
    - **TemplateSize**: 100
    - **TemplatePadding**: 0

1. Inside that gallery, add a **Gallery** control with a **Blank Vertical** layout, and then set these properties:

    - **Items**: `ForAll( [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], Value + ThisItem.Value * 16 )`
    - **Width**: 100
    - **Height**: 500
    - **TemplateSize**: 30
    - **TemplatePadding**: 0

    The value of the **Items** property multiplies 16 by the column number provided by the Value column of the **Items** property from the first gallery (0-7 in `ThisItem.Value`). The formula then adds the result to one of the row numbers from the second gallery (0-15 in the record scope that the [**ForAll**](function-forall.md) function provides).

1. Inside the second (vertical) gallery, add a **Label** control, and set these properties:

    - **Text**: `ThisItem.Value`
    - **Width**: 50

1. Inside the second (vertical) gallery, add another **Label** control, and set these properties:

    - **Text**: `Char( ThisItem.Value )`
    - **Width**: 50
    - **X**: 50

You've created a chart of the first 128 ASCII characters. Characters that appear as a small square can't be printed.

![First 128 ASCII characters](media/function-char/chart-lower.png)

To show the extended ASCII characters, set the **Items** property of the second gallery to this formula, which adds 128 to each character value:

`ForAll( [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], Value + ThisItem.Value * 16 + 128)`

![Extended ASCII characters](media/function-char/chart-higher.png)

To show the characters in a different font, set the **Font** property of the second label to a value such as **'Dancing Script'**.

![Dancing Script](media/function-char/chart-higher-dancing-script.png)
