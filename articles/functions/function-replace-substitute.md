<properties
	pageTitle="PowerApps: Replace and Substitute functions"
	description="Reference information for the Replace and Substitute functions in PowerApps, including syntax and examples"
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

# Replace and Substitute function in PowerApps #

Replace a portion of one string with another string.

## Description ##

The **Replace** function identifies the text to replace by starting position and length.  

The **Substitute** function identifies the text to replace by matching a string.

If you pass a single string, the return value is the modified string.  If you pass a single-column [table](working-with-tables.md) that contains strings, the return value is a single-column table of modified strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.

## Syntax ##

**Replace**( *String*, *StartingPosition*, *NumberOfCharacters*, *NewString* )

- *String* - Required. The string to operate on.
- *StartingPosition* - Required.  Character position to begin the replacement.  The first character of the string is at position 1.
- *NumberOfCharacters* - Required.  The number of characters to replace.
- *NewString* - Required.  The replacement string.  The replacement string does not need to be the same length as what it is replacing.

**Substitute**( *String*, *OldString*, *NewString* [, *InstanceNumber" ] )

- *String* - Required. The string to operate on.
- *OldString* - Required.  The string to be replaced.
- *NewString* - Required.  The replacement string.  The length of this string does not need to be the same as what it is replacing.
- *InstanceNumber* - Optional. By default, the first time a match is found for *OldString* it is replaced. you can specify which instance is to be replaced if there are more than one instance of *OldString* within *String*.

**Replace**( *SingleColumnTable*, *StartingPosition*, *NumberOfCharacters*, *NewString* )

- *SingleColumnTable* - Required. A single-column table of strings to operate on.
- *StartingPosition* - Required.  Character position to begin the replacement.  The first character of the string is at position 1.
- *NumberOfCharacters* - Required.  The number of characters to replace.
- *NewString* - Required.  The replacement string.  The replacement string does not need to be the same length as what it is replacing.

**Substitute**( *SingleColumnTable*, *OldString*, *NewString* [, *InstanceNumber* ] )

- *SingleColumnTable* - Required. A single-column table of strings to operate on.
- *OldString* - Required.  The string to be replaced.
- *NewString* - Required.  The replacement string.  The length of this string does not need to be the same as what it is replacing.
- *InstanceNumber* - Optional. By default, the first time a match is found for *OldString* it is replaced. you can specify which instance is to be replaced if there are more than one instance of *OldString* within *String*.

<!-- need more examples, including tables -->
