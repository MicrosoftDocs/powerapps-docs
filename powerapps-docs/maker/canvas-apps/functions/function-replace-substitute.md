---
title: Replace and Substitute functions | Microsoft Docs
description: Reference information, including syntax, for the Replace and Substitute functions in PowerApps
author: gregli-msft
manager: kvivek

ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2015
ms.author: gregli

---
# Replace and Substitute functions in PowerApps
Replace a portion of a string of text with another string.

## Description
The **Replace** function identifies the text to replace by starting position and length.  

The **Substitute** function identifies the text to replace by matching a string.  If more than one match is found, you can control which one is replaced.

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
* *InstanceNumber* - Optional. By default, the first instance of *OldString* is replaced. If *String* contains more than one instance, you can specify which instance to replace.

**Replace**( *SingleColumnTable*, *StartingPosition*, *NumberOfCharacters*, *NewString* )

* *SingleColumnTable* - Required. A single-column table of strings to operate on.
* *StartingPosition* - Required.  Character position to start the replacement.  The first character of each string in the table is at position 1.
* *NumberOfCharacters* - Required.  The number of characters to replace in each string.
* *NewString* - Required.  The replacement string. The number of characters in this argument can differ from the *NumberOfCharacters* argument.

**Substitute**( *SingleColumnTable*, *OldString*, *NewString* [, *InstanceNumber* ] )

* *SingleColumnTable* - Required. A single-column table of strings to operate on.
* *OldString* - Required.  The string to replace.
* *NewString* - Required.  The replacement string. *OldString* and *NewString* can have different lengths.
* *InstanceNumber* - Optional. By default, the first instance of *OldString* is replaced. If the table contains more than one instance, you can specify which instance to replace.

