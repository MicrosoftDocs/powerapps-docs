---
title: Replace and Substitute functions in Power Apps
description: Reference information including syntax and examples for the Replace and Substitute functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 12/02/2018
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Replace and Substitute functions in Power Apps
Replace a portion of a string of text with another string.

## Description
The **Replace** function identifies the text to replace by starting position and length.  

The **Substitute** function identifies the text to replace by matching a string. If more than one match is found, you can replace all of them or specify one to replace.

If you pass a single string, the return value is the modified string. If you pass a single-column [table](../working-with-tables.md) that contains strings, the return value is a single-column table of modified strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.

## Syntax
**Replace**( *String*, *StartingPosition*, *NumberOfCharacters*, *NewString* )

* *String* - Required. The string to operate on.
* *StartingPosition* - Required. Character position to start the replacement. The first character of *String* is at position 1.
* *NumberOfCharacters* - Required. The number of characters to replace in *String*.
* *NewString* - Required. The replacement string. The number of characters in this argument can differ from the *NumberOfCharacters* argument.

**Substitute**( *String*, *OldString*, *NewString* [, *InstanceNumber* ] )

* *String* - Required. The string to operate on.
* *OldString* - Required. The string to replace.
* *NewString* - Required. The replacement string. *OldString* and *NewString* can have different lengths.
* *InstanceNumber* - Optional. Use this argument to specify which instance of *OldString* to replace if *String* contains more than one instance. If you don't specify this argument, all instances will be replaced.

**Replace**( *SingleColumnTable*, *StartingPosition*, *NumberOfCharacters*, *NewString* )

* *SingleColumnTable* - Required. A single-column table of strings to operate on.
* *StartingPosition* - Required. Character position to start the replacement.  The first character of each string in the table is at position 1.
* *NumberOfCharacters* - Required. The number of characters to replace in each string.
* *NewString* - Required.  The replacement string. The number of characters in this argument can differ from the *NumberOfCharacters* argument.

**Substitute**( *SingleColumnTable*, *OldString*, *NewString* [, *InstanceNumber* ] )

* *SingleColumnTable* - Required. A single-column table of strings to operate on.
* *OldString* - Required.  The string to replace.
* *NewString* - Required.  The replacement string. *OldString* and *NewString* can have different lengths.
* *InstanceNumber* - Optional. Use this argument to specify which instance of *OldString* to replace if *String* contains more than one instance. If you don't specify this argument, all instances will be replaced.

## Examples

| Formula | Description | Result |
|---------|-------------|--------|
| **Replace( "abcdefghijk",&nbsp;6,&nbsp;5,&nbsp;"*" )** | Replaces five characters in "abcdefghijk" with a single "*" character, starting with the sixth character ("f"). | "abcde*k" |
| **Replace(&nbsp;"2019",&nbsp;3,&nbsp;2,&nbsp;"20"&nbsp;)** | Replaces the last two characters of "2019" with "20". | "2020" |
| **Replace(&nbsp;"123456",&nbsp;1,&nbsp;3,&nbsp;"_"&nbsp;)** | Replaces the first three characters of "123456" with a single "_" character. | "_456" | 
| **Substitute(&nbsp;"Sales&nbsp;Data",&nbsp;"Sales",&nbsp;"Cost"&nbsp;)** | Substitutes the string "Cost" for "Sales". | "Cost Data" | 
| **Substitute( "Quarter&nbsp;1,&nbsp;2018", "1", "2", 1 )** | Substitutes only the first instance of "1" with "2" because the fourth argument (*InstanceNumber*) is provided with a 1. |  "Quarter 2, 2018" |
| **Substitute( "Quarter&nbsp;1,&nbsp;2011", "1", "2", 3 )** | Substitutes only the third instance of "1" with "2" because the fourth argument (*InstanceNumber*) is provided with a 3. | "Quarter 1, 2012" |
| **Substitute( "Quarter&nbsp;1,&nbsp;2011", "1", "2" )** | Substitutes all instances of "1" with "2" because the fourth argument (*InstanceNumber*) isn't provided. | "Quarter 2, 2022" |
| **Replace(<br>[&nbsp;"Quarter&nbsp;1,&nbsp;2018",<br>"Quarter&nbsp;2,&nbsp;2011",<br>"Quarter&nbsp;4,&nbsp;2019" ],<br>9,  1, "3" )** | Replaces the ninth character in each record of the single-column table with "3". | [&nbsp;"Quarter&nbsp;3,&nbsp;2018",<br>"Quarter&nbsp;3,&nbsp;2011",<br>"Quarter&nbsp;3,&nbsp;2019"&nbsp;] |
| **Substitute( <br>[&nbsp;"Qtr&nbsp;1,&nbsp;2018",<br>"Quarter&nbsp;1,&nbsp;2011",<br>"Q1,&nbsp;2019"&nbsp;],<br>"1", "3", 1 )** | Because the fourth argument (*InstanceNumber*) is provided with a value of 1, substitutes only the first instance of "1" in each record of the single-column table with "3". | [&nbsp;"Qtr&nbsp;3,&nbsp;2018",<br>"Quarter&nbsp;3,&nbsp;2011",<br>"Q3,&nbsp;2019"&nbsp;] |
| **Substitute( <br>[&nbsp;"Qtr&nbsp;1,&nbsp;2018",<br>"Quarter&nbsp;1,&nbsp;2011",<br>"Q1,&nbsp;2019"&nbsp;],<br>"1", "3" )** | Because the fourth argument (*InstanceNumber*) isn't provided, substitutes all instances of "1" in each record of the single-column table with "3". | [&nbsp;"Qtr&nbsp;3,&nbsp;2038",<br>"Quarter&nbsp;3,&nbsp;2033",<br>"Q3,&nbsp;2039"&nbsp;] |  
 




[!INCLUDE[footer-include](../../../includes/footer-banner.md)]