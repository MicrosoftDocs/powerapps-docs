<properties
   pageTitle="Build a formula in PowerApps"
   description="In PowerApps, you can use the operators and functions that this topic describes."
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
   ms.date="10/23/2015"
   ms.author="gregli"/>

# Formula reference #

Functions and signals are the building blocks of formulas, listed below.  

Reference information is also available for:

- [Operators](functions/operators.md)
- [Control Properties]((reference-properties.md)
- "Working with ..." guides:
	- [Formulas](working-with-formulas.md)
	- [Tables](functions/working-with-tables.md)
	- [Data Sources](functions/working-with-data-sources.md)
	- [Variables](functions/working-with-variables.md)

## A ##

[Abs](functions/function-numericals.md) Absolute value of a number.  


[Acceleration](functions/sensors.md) Reads the acceleration sensor in your device.

[AddColumns](functions/function-table-shaping.md) Returns a table with columns added. 

[And](functions/function-logicals.md) Boolean logic AND.  Returns **true** if all arguments are **true**.  You can also use the **&&** operator.

[App](functions/sensors.md) Returns information about the currently running app, such as which screen is currently displayed.

[Average](functions/function-aggregates.md) Calculates the average of a table expression or set of arguments. 

## B ##

[Back](functions/function-navigate.md) Displays the previous screen.  

## C ##

[Char](functions/function-char.md) Translates a character code into a string.  *Coming Soon.*

[Clear](functions/function-clear-collect-clearcollect.md) Deletes all data from a collection.

[ClearCollect](functions/function-clear-collect-clearcollect.md) Deletes all data from a collection and then adds a set of records.

[Collect](functions/function-clear-collect-clearcollect.md) Creates collections and adds data to a data source.

[ColorFade](functions/function-colors.md) Fades a color value.  *Coming Soon.*

[ColorValue](functions/function-colors.md) Translates a CSS color name to a color value.  *Coming Soon.*

[Compass](functions/sensors.md) Returns your compass heading.

[Concat](functions/function-concatenate.md) Concatenates strings in a data source.  *Coming Soon.*

<!-- TODO: Rename concat -->

[Concatenate](functions/function-concatenate.md) Concatenates strings.  *Coming Soon.*


[Connection](functions/sensors.md) Returns information about your network connection.

[Count](functions/function-table-counts.md) Counts table records that contain numbers. 

[CountA](functions/function-table-counts.md) Counts table records that are not empty.

[CountIf](functions/function-table-counts.md) Counts table records that satisfy a condition.  

[CountRows](functions/function-table-counts.md) Counts table records.   

## D ##

[Date](functions/function-date.md) Returns a date/time value, based on Year, Month, and Day values.  *Coming Soon.*

[DateAdd](functions/function-dateadd-datediff.md) Add days, months, quarters, or years to a date/time value. *Coming Soon.*

[DateDiff](functions/function-dateadd-datediff.md) Subract two date values, the result in days, months, quarters, or years. *Coming Soon.*

[DateTimeValue](functions/function-date.md) Converts a date and time string to a date/time value. *Coming Soon.*

[DateValue](functions/function-date.md) Converts a date only string to a date/time value. *Coming Soon.*

[DataSourceInfo](functions/function-datasourceinfo.md) Provides information about a data source.

[Day](functions/function-datetime-parts.md) Retrieves the day portion of a date/time value.  *Coming Soon.*

[Disable](functions/function-enable-disable.md) Disables a signal, such as **Location** (GPS). *Coming Soon.*

[Distinct](functions/function-distinct.md) Returns the non-duplicate values of an expression evaluated across a table.  *Coming Soon.*

[DropColumns](functions/function-table-shaping.md) Returns a table with columns removed.

[Defaults](functions/function-defaults.md) Returns the default values for a data source.

## E ##

[Enable](functions/function-enable-disable.md) Enables a signal, such as **Location** (GPS). *Coming Soon.*

[Errors](functions/function-errors.md) Provides error information for previous changes to a data source.

[EncodeUrl](functions/function-encodeurl.md) Encodes special characters using URL encoding. *Coming Soon.*

## F ##

[Filter](functions/function-filter-lookup.md) Returns a filtered table based on a criteria.

[Find](functions/function-find.md) Checks if one string appears within another and returns the location. *Coming Soon.*

[First](functions/function-first-last.md) Returns the first record of a table.

[FirstN](functions/function-first-last.md) Returns the first N records of a table.

## G ##

[GrounBy](functions/function-groupby.md) Returns a table with records grouped together.  *Coming Soon.*

## H ##

[HashTags](functions/function-hashtags.md) Retrieves the set of hashtags (#strings) that appear in a string. *Coming Soon.*

[Hour](functions/function-datetime-parts.md) Retrieves the hour portion of a date/time value.  *Coming Soon.*

## I ##

[If](functions/function-if.md) Conditional logic: return one value if a condition is true and another value if it's false. *Coming Soon.*

[IsBlank](functions/function-isblank-isempty.md) Checks for a blank value. *Coming Soon.*

[IsEmpty](functions/function-isblank-isempty.md) Checks for an empty table. *Coming Soon.*

[IsNumeric](functions/function-isblank-isempty.md) Checks for a numeric value. *Coming Soon.*

[IsToday](functions/function-isblank-isempty.md) Checks if a date/time value is sometime today. *Coming Soon.*

## L ##

[Language](functions/function-language.md) Language.  *Coming Soon.*

[Last](functions/function-first-last.md) Returns the last record of a table.

[LastN](functions/function-first-last.md) Returns the last set of records (N records) of a table.

[Launch](functions/function-launch.md) Launches a URL, often used to open a web page. *Coming Soon.*

[Left](functions/function-left-mid-right.md) Returns the left portion of a string. *Coming Soon.*

[Len](functions/function-len.md) Returns the length of a string. *Coming Soon.*

[LoadData](functions/functions-loaddata-savedata.md) Loads a collection from app private storage. *Coming Soon.*


[Location](functions/sensors.md) Returns your location as a map coordinate, using the Global Positioning System (GPS) and other information.

[LookUp](functions/functions-filter-lookup) Looks up a single record in a table based on a criteria. 

[Lower](functions/function-lower-upper-proper.md) Converts letters in a string of text to all lowercase.

## M ##

[Max](functions/function-aggregates.md) Maximum value of a table expression or set of arguments.

[Mid](functions/function-left-mid-right.md) Returns the middle portion of a string. *Coming Soon.*

[Min](functions/function-aggregates.md) Minimum value of a table expression or set of arguments.

[Minute](functions/function-datetime-parts.md) Retrieves the minute portion of a date/time value.  *Coming Soon.*

[Mod](functions/function-mod.md) Returns the remainder after a number is divided by a divisor. *Coming Soon.*

[Month](functions/function-datetime-parts.md) Retrieves the minute portion of a date/time value.  *Coming Soon.*

## N ##

[Navigate](functions/function-navigate.md) Changes which screen is displayed.

[Not](functions/function-logicals.md) Boolean logic NOT.  Returns **true** if its argument is **false**, and **false** if its argument is **true**.  You can also use the **!** operator.

[Now](functions/function-now-today.md) Returns the current date/time value.

## O ##

[Or](functions/function-logicals.md) Boolean logic OR.  Returns **true** if any of its arguments are **true**.  You can also use the **||** operator.

## P ##

[Param](functions/function-params.md) Param. *Coming Soon.*

[Patch](functions/function-patch.md) Modifies or creates a record in a data source, or merges records outside of a data source.

[PlainText](functions/function-plaintext.md) Removes HTML and XML tags from a string. *Coming Soon.*

[Proper](functions/function-lower-upper-proper.md) Converts letters in a string of text to proper case (first letter of each word is uppercase, the rest are lowercase).

## R ##

[Rand](functions/function-rand.md) Returns a random number. *Coming Soon.*

[Refresh](functions/function-refesh.md) Refreshes the records of a data source.

[Remove](functions/function-remove-removeif.md) Removes specific records from a data source.

[RemoveIf](functions/function-remove-removeif.md) Removes records from a data source based on a condition.

[RenameColumns](functions/function-table-shaping.md) Renames columns of a table.

[Replace](functions/function-replace-substitute.md) Replaces part of a string with another string. *Coming Soon.*

[Revert](functions/function-revert.md) Reloads and clears errors for the records of a data source.

[RGBA](functions/function-colors.md) Returns a color value for a set of red, green, blue, and alpha components. *Coming Soon.*

[Right](functions/function-left-mid-right.md) Returns the right portion of a string. *Coming Soon.*

[Round](functions/function-round-rounddown-roundup.md) Rounds to the closest number. *Coming Soon.*

[RoundDown](functions/function-round-rounddown-roundup.md) Rounds down to the largest previous number. *Coming Soon.*

[RoundUp](functions/function-round-rounddown-roundup.md) Rounds up to the smallest next number. *Coming Soon.*

## S ##

[SaveData](functions/functions-loaddata-savedata.md) Saves a collection to app private storage. *Coming Soon.*

[Second](functions/function-datetime-parts.md) Retrieves the second portion of a date/time value.  *Coming Soon.*

[ShowColumns](functions/function-table-shaping.md) Returns a table with only selected columns.

[Shuffle](functions/function-shuffle.md) Returns a randomly shuffled version of a table.  *Coming Soon.*

[Sort](functions/function-sort.md) Returns a sorted table.

[Sqrt](functions/function-numericals.md) Returns a square root of a number.  

[StdevP](functions/function-statistical.md) Returns the standard deviation of its arguments.  *Coming Soon.*

[Substitute](functions/function-replace-substitute.md) Replaces part of a string with another string. *Coming Soon.*

[Sum](functions/function-aggregates.md) Calculates the sum of a table expression or set of arguments.  

## T ##

[Table](functions/function-table.md) Creates a temporary table.  *Coming Soon.*

[Text](functions/function-text.md) Formats a number as a string. *Coming Soon.*

[Time](functions/function-date.md) Returns a date/time value, based on Hour, Minute, and Second values.  *Coming Soon.*

[TimeValue](functions/function-date.md) Converts a time only string to a date/time value. *Coming Soon.*

[Today](functions/function-now-today.md) Returns the current date/time value. *Coming Soon.*

[Trim](functions/function-trim.md) Strips spaces from both ends of a string.  *Coming Soon.*

## U ##

[Ungroup](functions/function-group-ungroup.md) Removed a grouping. *Coming Soon.*

[Update](functions/function-update.md) Replaces a record in a data source.

[UpdateContext](functions/function-updatecontext.md) Creates or updates context variables of the current screen.

[UpdateIf](functions/function-update-updateif.md) Modifies a set of records in a data source based on a condition.

[Upper](functions/function-lower-upper-proper.md) Converts letters in a string of text to all uppercase.

[User](functions/function-user.md) Returns information about the current user. *Coming Soon.*

## V ##

[Value](functions/function-value.md) Converts a string to a number. *Coming Soon.*

[Validate](functions/function-validate.md) Checks whether the value of a single column or a complete record is valid for a data source.

[VarP](functions/function-statistical.md) Returns the variance of its arguments.  *Coming Soon.*

## Y ##

[Year](functions/function-datetime-parts.md) Retrieves the year portion of a date/time value.  *Coming Soon.*
