---
title: Formula reference for Power Apps
description: Reference information for functions, signals, and enumerations in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/23/2021
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Formula reference for Power Apps

> [!NOTE]
> Have you checked out new [Microsoft Power Fx](/power-platform/power-fx/overview)?

Formulas combine many elements.  Listed below are:

* **Functions** take parameters, perform an operation, and return a value. For example, **Sqrt(25)** returns **5**. Functions are modeled after Microsoft Excel functions.  Some functions have side effects, such as **SubmitForm**, which are appropriate only in a [behavior formula](working-with-formulas-in-depth.md) such as **Button.OnSelect**.
* **Signals** return information about the environment. For example, **[Location](functions/signals.md)** returns the device's current GPS coordinates. Signals don't take parameters or have side effects.
* **Enumerations** return a pre-defined constant value. For example, **[Color](functions/function-colors.md)** is an enumeration that has pre-defined values for **Color.Red**, **Color.Blue**, and so forth.  Common enumerations are included here; function-specific enumerations are described with the function.
* **Named operators**, such as **[ThisItem](functions/operators.md#thisitem-thisrecord-and-as-operators)** and **[Self](functions/operators.md#self-and-parent-operators)**, provide access to information from within a container.

Other elements include:

* [Operators and identifiers](functions/operators.md)
* [Controls and their properties](reference-properties.md)
* [Data types](functions/data-types.md)

## <a id="-a"></a> A
**[Abs](functions/function-numericals.md)** – Absolute value of a number.  

**[Acceleration](functions/signals.md)** – Reads the acceleration sensor in your device.

**[Acos](functions/function-trig.md)** – Returns the arccosine of a number, in radians.

**[Acot](functions/function-trig.md)** – Returns the arccotangent of a number, in radians.

**[AddColumns](functions/function-table-shaping.md)** – Returns a table with [columns](working-with-tables.md#columns) added.

**[And](functions/function-logicals.md)** – Boolean logic AND.  Returns **true** if all arguments are **true**.  You can also use the [**&&** operator](functions/operators.md).

**[App](functions/object-app.md)** – Provides information about the currently running app and control over the app's behavior.

**[Asin](functions/function-trig.md)** – Returns the arcsine of a number, in radians.

**[Assert](functions/function-assert.md)** – Evaluates to true or false in a test.

**[As](functions/operators.md#thisitem-thisrecord-and-as-operators)** – Names the current record in gallery, form, and record scope functions such as **ForAll**, **With**, and **Sum**.

**[AsType](functions/function-astype-istype.md)** – Treats a record reference as a specific table type.

**[Atan](functions/function-trig.md)** – Returns the arctangent of a number, in radians.

**[Atan2](functions/function-trig.md)** – Returns the arctangent based on an (*x*,*y*) coordinate, in radians.

**[Average](functions/function-aggregates.md)** – Calculates the average of a table expression or a set of arguments.

## B
**[Back](functions/function-navigate.md)** – Displays the previous screen.  

**[Blank](functions/function-isblank-isempty.md)** – Returns a *blank* value that can be used to insert a NULL value in a data source.

## C
**[Calendar](functions/function-clock-calendar.md)** – Retrieves information about the calendar for the current locale.

**[Char](functions/function-char.md)** – Translates a character code into a string.

**[Choices](functions/function-choices.md)** – Returns a table of the possible values for a lookup column.

**[Clear](functions/function-clear-collect-clearcollect.md)** – Deletes all data from a [collection](working-with-data-sources.md#collections).

**[ClearCollect](functions/function-clear-collect-clearcollect.md)** – Deletes all data from a collection and then adds a set of [records](working-with-tables.md#records).

**[ClearData](functions/function-savedata-loaddata.md)** – Clears a collection or all collections from an app host such as a local device.

**[Clock](functions/function-clock-calendar.md)** – Retrieves information about the clock for the current locale.

**[Coalesce](functions/function-isblank-isempty.md)** – Replaces *blank* values while leaving non-*blank* values unchanged.

**[Collect](functions/function-clear-collect-clearcollect.md)** – Creates a collection or adds data to a data source.

**[Color](functions/function-colors.md)** – Sets a property to a built-in color value.

**[ColorFade](functions/function-colors.md)** – Fades a color value.

**[ColorValue](functions/function-colors.md)** – Translates a CSS color name or a hex code to a color value.  

**[Compass](functions/signals.md)** – Returns your compass heading.

**[Concat](functions/function-concatenate.md)** – Concatenates strings in a data source.  

**[Concatenate](functions/function-concatenate.md)** – Concatenates strings.

**[Concurrent](functions/function-concurrent.md)** – Evaluates multiple formulas concurrently with one another. 

**[Connection](functions/signals.md)** – Returns information about your network connection.

**[Count](functions/function-table-counts.md)** – Counts table records that contain numbers.

**[Cos](functions/function-trig.md)** – Returns the cosine of an angle specified in radians.

**[Cot](functions/function-trig.md)** – Returns the cotangent of an angle specified in radians.

**[CountA](functions/function-table-counts.md)** – Counts table records that aren't [empty](functions/function-isblank-isempty.md).

**[CountIf](functions/function-table-counts.md)** – Counts table records that satisfy a condition.  

**[CountRows](functions/function-table-counts.md)** – Counts table records.   

## D
**[DataSourceInfo](functions/function-datasourceinfo.md)** – Provides information about a data source.

**[Date](functions/function-date-time.md)** – Returns a date/time value, based on **Year**, **Month**, and **Day** values.  

**[DateAdd](functions/function-dateadd-datediff.md)** – Adds days, months, quarters, or years to a date/time value.

**[DateDiff](functions/function-dateadd-datediff.md)** – Subtracts two date values, and shows the result in days, months, quarters, or years.

**[DateTimeValue](functions/function-datevalue-timevalue.md)** – Converts a date and time string to a date/time value.

**[DateValue](functions/function-datevalue-timevalue.md)** – Converts a date-only string to a date/time value.

**[Day](functions/function-datetime-parts.md)** – Retrieves the day portion of a date/time value.  

**[Defaults](functions/function-defaults.md)** – Returns the default values for a data source.

**[Degrees](functions/function-trig.md)** - Converts radians to degrees.

**[Disable](functions/function-enable-disable.md)** – Disables a signal, such as **[Location](functions/signals.md)** for reading the GPS.

**[Distinct](functions/function-distinct.md)** – Summarizes records of a table, removing duplicates.  

**[Download](functions/function-download.md)** – Downloads a file from the web to the local device.

**[DropColumns](functions/function-table-shaping.md)** – Returns a table with one or more columns removed.

## E
**[EditForm](functions/function-form.md)** – Resets a form control for editing of an item.

**[Enable](functions/function-enable-disable.md)** – Enables a signal, such as **[Location](functions/signals.md)** for reading the GPS.

**[EncodeUrl](functions/function-encode-decode.md)** – Encodes special characters using URL encoding.

**[EndsWith](functions/function-startswith.md)** – Checks whether a text string ends with another text string.

**[Errors](functions/function-errors.md)** – Provides error information for previous changes to a data source.

**[exactin](functions/operators.md#in-and-exactin-operators)** – Checks if a text string is contained within another text string or table, case dependent.  Also used to check if a record is in a table.  

**[Exit](functions/function-exit.md)** – Exits the currently running app and optionally signs out the current user.

**[Exp](functions/function-numericals.md)** - Returns *e* raised to a power.

## F
**[Filter](functions/function-filter-lookup.md)** – Returns a filtered table based on one or more criteria.

**[Find](functions/function-find.md)** – Checks whether one string appears within another and returns the location.

**[First](functions/function-first-last.md)** – Returns the first record of a table.

**[FirstN](functions/function-first-last.md)** – Returns the first set of records (N records) of a table.

**[ForAll](functions/function-forall.md)** – Calculates values and performs actions for all records of a table.

## G
**[GroupBy](functions/function-groupby.md)** – Returns a table with records grouped together.

**[GUID](functions/function-guid.md)** – Converts a GUID string to a GUID value or creates a new GUID value.

## H
**[HashTags](functions/function-hashtags.md)** – Extracts the hashtags (#strings) from a string.

**[Hour](functions/function-datetime-parts.md)** – Returns the hour portion of a date/time value.

## I
**[If](functions/function-if.md)** – Returns one value if a condition is true and another value if not. 

**[IfError](functions/function-iferror.md)** - Detects errors and provides an alternative value or takes action. 

**[in](functions/operators.md#in-and-exactin-operators)** – Checks if a text string is contained within another text string or table, case independent.  Also used to check if a record is in a table.

**[IsBlank](functions/function-isblank-isempty.md)** – Checks for a [blank](functions/function-isblank-isempty.md) value.

**[IsBlankOrError](functions/function-iferror.md)** – Checks for a [blank](functions/function-isblank-isempty.md) value or error.

**[IsEmpty](functions/function-isblank-isempty.md)** – Checks for an empty table.

**[IsError](functions/function-iferror.md)** – Checks for an error.

**[IsMatch](functions/function-ismatch.md)** – Checks a string against a pattern.  Regular expressions can be used.

**[IsNumeric](functions/function-isnumeric.md)** – Checks for a numeric value.

**[IsToday](functions/function-now-today-istoday.md)** – Checks whether a date/time value is sometime today.

**[IsType](functions/function-astype-istype.md)** – Checks whether a record reference  refers to a specific table type.

## J
**[JSON](functions/function-json.md)** - Generates a JSON text string for a table, a record, or a value.

## L
**[Language](functions/function-language.md)** – Returns the language tag of the current user.

**[Last](functions/function-first-last.md)** – Returns the last record of a table.

**[LastN](functions/function-first-last.md)** – Returns the last set of records (N records) of a table.

**[Launch](functions/function-param.md)** – Launches a webpage or a canvas app.

**[Left](functions/function-left-mid-right.md)** – Returns the left-most portion of a string.

**[Len](functions/function-len.md)** – Returns the length of a string.

**[Ln](functions/function-numericals.md)** – Returns the natural log.

**[LoadData](functions/function-savedata-loaddata.md)** – Loads a collection from an app host such as a local device.

**[Location](functions/signals.md)** – Returns your location as a map coordinate by using the Global Positioning System (GPS) and other information.

**[LookUp](functions/function-filter-lookup.md)** – Looks up a single record in a table based on one or more criteria.

**[Lower](functions/function-lower-upper-proper.md)** – Converts letters in a string of text to all lowercase.

## M
**[Match](functions/function-ismatch.md)** – Extracts a substring based on a pattern.  Regular expressions can be used.

**[MatchAll](functions/function-ismatch.md)** – Extracts multiple substrings based on a pattern.  Regular expressions can be used.

**[Max](functions/function-aggregates.md)** – Maximum value of a table expression or a set of arguments.

**[Mid](functions/function-left-mid-right.md)** – Returns the middle portion of a string.

**[Min](functions/function-aggregates.md)** – Minimum value of a table expression or a set of arguments.

**[Minute](functions/function-datetime-parts.md)** – Retrieves the minute portion of a date/time value.  

**[Mod](functions/function-mod.md)** – Returns the remainder after a dividend is divided by a divisor.

**[Month](functions/function-datetime-parts.md)** – Retrieves the month portion of a date/time value.

## N
**[Navigate](functions/function-navigate.md)** – Changes which screen is displayed.

**[NewForm](functions/function-form.md)** – Resets a form control for creation of an item.

**[Not](functions/function-logicals.md)** – Boolean logic NOT.  Returns **true** if its argument is **false**, and returns **false** if its argument is **true**.  You can also use the [**!** operator](functions/operators.md).

**[Notify](functions/function-showerror.md)** – Displays a banner message to the user.

**[Now](functions/function-now-today-istoday.md)** – Returns the current date/time value.

## O
**[Or](functions/function-logicals.md)** – Boolean logic OR.  Returns **true** if any of its arguments are **true**.  You can also use the [**||** operator](functions/operators.md).

## P
**[Param](functions/function-param.md)** – Access parameters passed to a canvas app when launched.

**[Parent](functions/operators.md#self-and-parent-operators)** – Provides access to a container control's properties.

**[Patch](functions/function-patch.md)** – Modifies or creates a record in a data source, or merges records outside of a data source.

**[Pi](functions/function-trig.md)** – Returns the number &pi;.

**[PlainText](functions/function-encode-decode.md)** – Removes HTML and XML tags from a string.

**[Power](functions/function-numericals.md)** – Returns a number raised to a power.  You can also use the [**^** operator](functions/operators.md).

**[Proper](functions/function-lower-upper-proper.md)** – Converts the first letter of each word in a string to uppercase, and converts the rest to lowercase.

## R
**[Radians](functions/function-trig.md)** - Converts degrees to radians.

**[Rand](functions/function-rand.md)** – Returns a pseudo-random number.

**[ReadNFC](functions/function-readnfc.md)** – Reads a Near Field Communication (NFC) tag.

**[Refresh](functions/function-refresh.md)** – Refreshes the records of a data source.

**[Relate](functions/function-relate-unrelate.md)** – Relates records of two tables through a one-to-many or many-to-many relationship.

**[Remove](functions/function-remove-removeif.md)** – Removes one or more specific records from a data source.

**[RemoveIf](functions/function-remove-removeif.md)** – Removes records from a data source based on a condition.

**[RenameColumns](functions/function-table-shaping.md)** – Renames columns of a table.

**[Replace](functions/function-replace-substitute.md)** – Replaces part of a string with another string, by starting position of the string.

**[RequestHide](functions/function-requesthide.md)** – Hides a SharePoint form.

**[Reset](functions/function-reset.md)** – Resets an input control to its default value, discarding any user changes.

**[ResetForm](functions/function-form.md)** – Resets a form control for editing of an existing item.

**[Revert](functions/function-revert.md)** – Reloads and clears errors for the records of a data source.

**[RGBA](functions/function-colors.md)** – Returns a color value for a set of red, green, blue, and alpha components.

**[Right](functions/function-left-mid-right.md)** – Returns the right-most portion of a string.

**[Round](functions/function-round.md)** – Rounds to the closest number.

**[RoundDown](functions/function-round.md)** – Rounds down to the largest previous number.

**[RoundUp](functions/function-round.md)** – Rounds up to the smallest next number.

## S
**[SaveData](functions/function-savedata-loaddata.md)** – Saves a collection to an app host such as a local device.

**[Search](functions/function-filter-lookup.md)** – Finds records in a table that contain a string in one of their columns.  

**[Second](functions/function-datetime-parts.md)** – Retrieves the second portion of a date/time value.

**[Select](functions/function-select.md)** – Simulates a select action on a control, causing the **OnSelect** formula to be evaluated.

**[Self](functions/operators.md#self-and-parent-operators)** – Provides access to the properties of the current control.

**[Sequence](functions/function-sequence.md)** – Generate a table of sequential numbers, useful when iterating with **ForAll**.

**[Set](functions/function-set.md)** – Sets the value of a global variable.

**[SetFocus](functions/function-setfocus.md)** – Moves input focus to a specific control.

**[SetProperty](functions/function-setproperty.md)** – Simulates interactions with input controls.

**[ShowColumns](functions/function-table-shaping.md)** – Returns a table with only selected columns.

**[Shuffle](functions/function-shuffle.md)** – Randomly reorders the records of a table.

**[Sin](functions/function-trig.md)** – Returns the sine of an angle specified in radians.

**[Sort](functions/function-sort.md)** – Returns a sorted table based on a formula.

**[SortByColumns](functions/function-sort.md)** – Returns a sorted table based on one or more columns.

**[Split](functions/function-split.md)** – Splits a text string into a table of substrings.

**[Sqrt](functions/function-numericals.md)** – Returns the square root of a number.

**[StartsWith](functions/function-startswith.md)** – Checks if a text string begins with another text string.

**[StdevP](functions/function-aggregates.md)** – Returns the standard deviation of its arguments.  

**[Substitute](functions/function-replace-substitute.md)** – Replaces part of a string with another string, by matching strings.

**[SubmitForm](functions/function-form.md)** – Saves the item in a form control to the data source.

**[Sum](functions/function-aggregates.md)** – Calculates the sum of a table expression or a set of arguments.  

**[Switch](functions/function-if.md)** – Matches with a set of values and then evaluates a corresponding formula.

## T
**[Table](functions/function-table.md)** – Creates a temporary table.  

**[Tan](functions/function-trig.md)** - Returns the tangent of an angle specified in radians.

**[Text](functions/function-text.md)** – Converts any value and formats a number or date/time value to a string of text.

**[ThisItem](functions/operators.md#thisitem-thisrecord-and-as-operators)** – Returns the record for the current item in a gallery or form control.

**[ThisRecord](functions/operators.md#thisitem-thisrecord-and-as-operators)** – Returns the record for the current item in a record scope function, such as **ForAll**, **With**, and **Sum**.

**[Time](functions/function-date-time.md)** – Returns a date/time value, based on **Hour**, **Minute**, and **Second** values.  

**[TimeValue](functions/function-datevalue-timevalue.md)** – Converts a time-only string to a date/time value.

**[TimeZoneOffset](functions/function-dateadd-datediff.md)** – Returns the difference between UTC and the user's local time in minutes.

**[Today](functions/function-now-today-istoday.md)** – Returns the current date/time value.

**[Trace](functions/function-trace.md)** - Provide additional information in your test results.

**[Trim](functions/function-trim.md)** – Removes extra spaces from the ends and interior of a string of text.

**[TrimEnds](functions/function-trim.md)** – Removes extra spaces from the ends of a string of text only.

## U
**[Ungroup](functions/function-groupby.md)** – Removes a grouping.

**[Unrelate](functions/function-relate-unrelate.md)** – Unrelates records of two tables from a one-to-many or many-to-many relationship.

**[Update](functions/function-update-updateif.md)** – Replaces a record in a data source.

**[UpdateContext](functions/function-updatecontext.md)** – Sets the value of one or more [context variables](working-with-variables.md#use-a-context-variable) of the current screen.

**[UpdateIf](functions/function-update-updateif.md)** – Modifies a set of records in a data source based on a condition.

**[Upper](functions/function-lower-upper-proper.md)** – Converts letters in a string of text to all uppercase.

**[User](functions/function-user.md)** – Returns information about the current user.

## V
**[Validate](functions/function-validate.md)** – Checks whether the value of a single column or a complete record is valid for a data source.

**[Value](functions/function-value.md)** – Converts a string to a number.

**[VarP](functions/function-aggregates.md)** – Returns the variance of its arguments.  

**[ViewForm](functions/function-form.md)** – Resets a form control for viewing of an existing item.

## W
**[Weekday](functions/function-datetime-parts.md)** – Retrieves the weekday portion of a date/time value.

**[With](functions/function-with.md)** – Calculates values and performs actions for a single record, including inline records of named values.

## Y
**[Year](functions/function-datetime-parts.md)** – Retrieves the year portion of a date/time value.  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]