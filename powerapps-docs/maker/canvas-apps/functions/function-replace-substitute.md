---
title: Replace and Substitute functions | Microsoft Docs
description: Reference information, including syntax, for the Replace and Substitute functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 12/02/2018
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Replace and Substitute functions in PowerApps
Replace a portion of a string of text with another string.

## Description
The **Replace** function identifies the text to replace by starting position and length.  

The **Substitute** function identifies the text to replace by matching a string.  If more than one match is found, you can replace all of them or select one to be replaced.

If you pass a single string, the return value is the modified string.  If you pass a single-column [table](../working-with-tables.md) that contains strings, the return value is a single-column table of modified strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.

## Syntax
**Replace**( *String*, *StartingPosition*, *NumberOfCharacters*, *NewString* )

* *String* - Required. The string to operate on.
* *StartingPosition* - Required.  Character position to start the replacement. The first character of *String* is at position 1.
* *NumberOfCharacters* - Required.  The number of characters to replace in *String*.
* *NewString* - Required.  The replacement string. The number of characters in this argument can differ from the *NumberOfCharacters* argument.

**Substitute**( *String*, *OldString*, *NewString* [, *InstanceNumber* ] )

* *String* - Required. The string to operate on.
* *OldString* - Required.  The string to replace.
* *NewString* - Required.  The replacement string. *OldString* and *NewString* can have different lengths.
* *InstanceNumber* - Optional. All instances of *OldString* are replaced if this argument is not provided. Use this argument to select one specific instance to be replaced.

**Replace**( *SingleColumnTable*, *StartingPosition*, *NumberOfCharacters*, *NewString* )

* *SingleColumnTable* - Required. A single-column table of strings to operate on.
* *StartingPosition* - Required.  Character position to start the replacement.  The first character of each string in the table is at position 1.
* *NumberOfCharacters* - Required.  The number of characters to replace in each string.
* *NewString* - Required.  The replacement string. The number of characters in this argument can differ from the *NumberOfCharacters* argument.

**Substitute**( *SingleColumnTable*, *OldString*, *NewString* [, *InstanceNumber* ] )

* *SingleColumnTable* - Required. A single-column table of strings to operate on.
* *OldString* - Required.  The string to replace.
* *NewString* - Required.  The replacement string. *OldString* and *NewString* can have different lengths.
* *InstanceNumber* - Optional. All instances of *OldString* are replaced if this argument is not provided. Use this argument to select one specific instance to be replaced.

## Examples

| Formula | Description | Result |
|---------|-------------|--------|
| **Replace( "abcdefghijk", 6, 5, "*" )** | Replaces five characters in "abcdefghijk" with a single "*" character, starting with the sixth character ("f"). | "abcde*k" |
| **Replace( "2019", 3, 2, "20" )** | Replaces the last two digits of "2019" with "20". | "2020" |
| **Replace( "123456", 1, 3, "@" )** | Replaces the first three characters of 123456 with a single "@" character. | "@456" |
| **Replace( <br>[ "Quarter 1, 2018",<br>"Quarter 2, 2011",<br>"Quarter 4, 2019" ],<br>9,  1, "3" )** | Replaces the ninth character in each of the records in the single column table with "3". | [ "Quarter 3, 2018",<br>"Quarter 3, 2011",<br>"Quarter 3, 2019" ] | 

| Formula | Description | Result |
|---------|-------------|--------|
| **Substitute( "Sales Data", "Sales", "Cost"** | Substitutes the string "Cost" for "Sales". | "Cost Data" | 
| **Substitute( "Quarter 1, 2018", "1", "2", 1 )** | Substitutes only the first instance of "1" with "2". |  "Quarter 2, 2018" |
| **Substitute( "Quarter 1, 2011", "1", "2", 3 )** | Substitutes only the third instance of "1" with "2". | "Quarter 1, 2012" |
| **Substitute( "Quarter 1, 2011", "1", "2" )** | Substitutes all instances of "1" with "2". | "Quarter 2, 2022" |
| **Substitute( <br>[ "Qtr 1, 2018",<br>"Quarter 1, 2011",<br>"Q1, 2019" ],<br>"1", "3", 1 )** | Substitutes only the first instance of "1" in each of the records in the single column table with "3". | [ "Qtr 3, 2018",<br>"Quarter 3, 2011",<br>"Q3, 2019" ] |
  
 


