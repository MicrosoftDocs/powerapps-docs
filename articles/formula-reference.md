<properties
   pageTitle="Build a formula | Microsoft PowerApps"
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

Functions and [signals](functions/signals.md), listed below, are the building blocks of formulas.  

Reference information is also available for:

- [Operators](functions/operators.md)
- [Control properties](reference-properties.md)
- "Working with ..." guides:
	- [Formulas](working-with-formulas.md)
	- [Tables](functions/working-with-tables.md)
	- [Data sources](functions/working-with-data-sources.md)
	- [Variables](functions/working-with-variables.md)

## A ##

**[Abs](functions/function-numericals.md)** Absolute value of a number.  

**[Acceleration](functions/signals.md)** Reads the acceleration sensor in your device.

**[AddColumns](functions/function-table-shaping.md)** Returns a table with [columns](functions/working-with-tables.md#columns) added.

**[And](functions/function-logicals.md)** Boolean logic AND.  Returns **true** if all arguments are **true**.  You can also use the **&&** operator.

**[App](functions/signals.md)** Returns information about the currently running app, such as which screen is currently displayed.

**[Average](functions/function-aggregates.md)** Calculates the average of a table expression or set of arguments.

## B ##

**[Back](functions/function-navigate.md)** Displays the previous screen.  

## C ##

**[Char](functions/function-char.md)** Translates a character code into a string.

**[Clear](functions/function-clear-collect-clearcollect.md)** Deletes all data from a [collection](functions/working-with-data-sources.md#collections).

**[ClearCollect](functions/function-clear-collect-clearcollect.md)** Deletes all data from a collection and then adds a set of [records](functions/working-with-tables.md#records).

**[Collect](functions/function-clear-collect-clearcollect.md)** Creates collections and adds data to a data source.

**[Color](functions/function-colors.md)** Built in color values.

**[ColorFade](functions/function-colors.md)** Fades a color value.

**[ColorValue](functions/function-colors.md)** Translates a CSS color name or hex code to a color value.  

**[Compass](functions/signals.md)** Returns your compass heading.

**[Concat](functions/function-concatenate.md)** Concatenates strings in a data source.  

<!-- TODO: Rename concat -->

**[Concatenate](functions/function-concatenate.md)** Concatenates strings.

**[Connection](functions/signals.md)** Returns information about your network connection.

**[Count](functions/function-table-counts.md)** Counts table records that contain numbers.

**[CountA](functions/function-table-counts.md)** Counts table records that aren't [empty](functions/function-isblank-isempty.md).

**[CountIf](functions/function-table-counts.md)** Counts table records that satisfy a condition.  

**[CountRows](functions/function-table-counts.md)** Counts table records.   

## D ##

**[Date](functions/function-date-time.md)** Returns a date/time value, based on Year, Month, and Day values.  

**[DateAdd](functions/function-dateadd-datediff.md)** Add days, months, quarters, or years to a date/time value.

**[DateDiff](functions/function-dateadd-datediff.md)** Subtracts two date values, and shows the result in days, months, quarters, or years.

**[DateTimeValue](functions/function-datevalue-timevalue.md)** Converts a date and time string to a date/time value.

**[DateValue](functions/function-datevalue-timevalue.md)** Converts a date-only string to a date/time value.

**[DataSourceInfo](functions/function-datasourceinfo.md)** Provides information about a data source.

**[Day](functions/function-datetime-parts.md)** Retrieves the day portion of a date/time value.  

**Disable** Disables a signal, such as **[Location](functions/signals.md)** (GPS). *Coming Soon.*

**Distinct** Returns the non-duplicate values of an expression evaluated across a table.  *Coming Soon.*

**[DropColumns](functions/function-table-shaping.md)** Returns a table with columns removed.

**[Defaults](functions/function-defaults.md)** Returns the default values for a data source.

## E ##

**Enable** Enables a signal, such as **[Location](functions/signals.md)** (GPS). *Coming Soon.*

**[Errors](functions/function-errors.md)** Provides error information for previous changes to a data source.

**EncodeUrl** Encodes special characters using URL encoding. *Coming Soon.*

## F ##

**[Filter](functions/function-filter-lookup.md)** Returns a filtered table based on one or more criteria.

**Find** Checks if one string appears within another and returns the location. *Coming Soon.*

**[First](functions/function-first-last.md)** Returns the first record of a table.

**[FirstN](functions/function-first-last.md)** Returns the first N records of a table.

## G ##

**GroupBy** Returns a table with records grouped together.  *Coming Soon.*

## H ##

**HashTags** Retrieves the set of hashtags (#strings) that appear in a string. *Coming Soon.*

**[Hour](functions/function-datetime-parts.md)** Retrieves the hour portion of a date/time value.

## I ##

**If** Conditional logic: returns one value if a condition is true and another value if it's false. *Coming Soon.*

**[IsBlank](functions/function-isblank-isempty.md)** Checks for a [blank](functions/function-isblank-isempty.md) value.

**[IsEmpty](functions/function-isblank-isempty.md)** Checks for an empty table.

**IsNumeric** Checks for a numeric value. *Coming Soon.*

**IsToday** Checks if a date/time value is sometime today. *Coming Soon.*

## L ##

**Language** Language.  *Coming Soon.*

**[Last](functions/function-first-last.md)** Returns the last record of a table.

**[LastN](functions/function-first-last.md)** Returns the last set of records (N records) of a table.

**Launch** Launches a URL, often used to open a webpage. *Coming Soon.*

**Left** Returns the left portion of a string. *Coming Soon.*

**Len** Returns the length of a string. *Coming Soon.*

**LoadData** Loads a collection from PowerApps private storage. *Coming Soon.*

**[Location](functions/signals.md)** Returns your location as a map coordinate, using the Global Positioning System (GPS) and other information.

**[LookUp](functions/function-filter-lookup.md)** Looks up a single record in a table based on one or more criteria.

**[Lower](functions/function-lower-upper-proper.md)** Converts letters in a string of text to all lowercase.

## M ##

**[Max](functions/function-aggregates.md)** Maximum value of a table expression or a set of arguments.

**Mid** Returns the middle portion of a string. *Coming Soon.*

**[Min](functions/function-aggregates.md)** Minimum value of a table expression or a set of arguments.

**[Minute](functions/function-datetime-parts.md)** Retrieves the minute portion of a date/time value.  

**Mod** Returns the remainder after a number is divided by a divisor. *Coming Soon.*

**[Month](functions/function-datetime-parts.md)** Retrieves the month portion of a date/time value.

## N ##

**[Navigate](functions/function-navigate.md)** Changes which screen is displayed.

**[Not](functions/function-logicals.md)** Boolean logic NOT.  Returns **true** if its argument is **false**, and **false** if its argument is **true**.  You can also use the **!** operator.

**Now** Returns the current date/time value.

## O ##

**[Or](functions/function-logicals.md)** Boolean logic OR.  Returns **true** if any of its arguments are **true**.  You can also use the **||** operator.

## P ##

**Param** Param. *Coming Soon.*

**[Patch](functions/function-patch.md)** Modifies or creates a record in a data source, or merges records outside of a data source.

**PlainText** Removes HTML and XML tags from a string. *Coming Soon.*

**[Proper](functions/function-lower-upper-proper.md)** Converts letters in a string of text to proper case. (The first letter of each word is uppercase, and the rest are lowercase.)

## R ##

**Rand** Returns a random number. *Coming Soon.*

**[Refresh](functions/function-refresh.md)** Refreshes the records of a data source.

**[Remove](functions/function-remove-removeif.md)** Removes specific records from a data source.

**[RemoveIf](functions/function-remove-removeif.md)** Removes records from a data source based on a condition.

**[RenameColumns](functions/function-table-shaping.md)** Renames columns of a table.

**Replace** Replaces part of a string with another string. *Coming Soon.*

**[Revert](functions/function-revert.md)** Reloads and clears errors for the records of a data source.

**[RGBA](functions/function-colors.md)** Returns a color value for a set of red, green, blue, and alpha components.

**Right** Returns the right portion of a string. *Coming Soon.*

**Round** Rounds to the closest number. *Coming Soon.*

**RoundDown** Rounds down to the largest previous number. *Coming Soon.*

**RoundUp** Rounds up to the smallest next number. *Coming Soon.*

## S ##

**SaveData** Saves a collection to PowerApps private storage. *Coming Soon.*

**[Second](functions/function-datetime-parts.md)** Retrieves the second portion of a date/time value.  

**[ShowColumns](functions/function-table-shaping.md)** Returns a table with only selected columns.

**Shuffle** Returns a randomly shuffled version of a table.  *Coming Soon.*

**[Sort](functions/function-sort.md)** Returns a sorted table.

**[Sqrt](functions/function-numericals.md)** Returns the square root of a number.  

**StdevP** Returns the standard deviation of its arguments.  *Coming Soon.*

**Substitute** Replaces part of a string with another string. *Coming Soon.*

**[Sum](functions/function-aggregates.md)** Calculates the sum of a table expression or a set of arguments.  

## T ##

**Table** Creates a temporary table.  *Coming Soon.*

**Text** Formats a number as a string. *Coming Soon.*

**[Time](functions/function-date-time.md)** Returns a date/time value, based on Hour, Minute, and Second values.  

**[TimeValue](functions/function-datevalue-timevalue.md)** Converts a time-only string to a date/time value.

**Today** Returns the current date/time value. *Coming Soon.*

**Trim** Strips spaces from both ends of a string.  *Coming Soon.*

## U ##

**Ungroup** Removes a grouping. *Coming Soon.*

**[Update](functions/function-update-updateif.md)** Replaces a record in a data source.

**[UpdateContext](functions/function-updatecontext.md)** Creates or updates one or more [context variables](functions/working-with-variables.md#context-variables) of the current screen.

**[UpdateIf](functions/function-update-updateif.md)** Modifies a set of records in a data source based on a condition.

**[Upper](functions/function-lower-upper-proper.md)** Converts letters in a string of text to all uppercase.

**User** Returns information about the current user. *Coming Soon.*

## V ##

**Value** Converts a string to a number. *Coming Soon.*

**[Validate](functions/function-validate.md)** Checks whether the value of a single column or a complete record is valid for a data source.

**VarP** Returns the variance of its arguments.  *Coming Soon.*

## Y ##

**[Year](functions/function-datetime-parts.md)** Retrieves the year portion of a date/time value.  
