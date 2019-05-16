---
title: Operators | Microsoft Docs
description: Data types in canvas apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/04/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Data types in canvas apps

Information flows through an app in small, discrete pieces.  For example, a "Birthday" and an "Anniversary" would both flow through as a Date.  Dates carry with them constraints, such as  

while "Birthday" may be stored in a field specifically designed to hold a date.         

Canvas apps support the data types explained in this article.  When connecting to external data sources, all external data types are mapped to these data types.

## Data type list

| Data type | Description | Examples |
|-----------|-------------|---------|
| Boolean | A *true* or *false* value.  Can be used directly in **If**, **Filter** and other functions without a comparison.  | *true* |
| Hyperlink | A Unicode text string that holds a hyperlink. | "http://powerapps.microsoft.com" |
| Currency | Currency value stored in a floating point number. Currency values are the same as number values but will be shown in some situations with a currency symbol.  | 123<br>4.56 |  
| Image | 
| Color | A color including an alpha channel.  | Color.Red<br>ColorValue( "#102030" )<br>RGBA( 255, 128, 0, 0.5 ) | 
| Date | A date only. |
| DateTime | A date with time. |
| Number | Floating point number. | 123<br>-4.567<br>8.903e121 |
| Time | A time only. | 
| Text | A Unicode text string. |
| GUID | A [Globally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier). | GUID()<br>GUID( "123e4567-e89b-12d3-a456-426655440000" ) |
| Record Reference | A reference to a record in any CDS entity. | First(Accounts).Owner which can be either a User or a Team |  
| Media | 
| Option set | An option from a set of options, backed by a number. It combines both a numeric value that is storead and used for comparisons with a text label for display to app users. | 
| Two option | An option from a set of two options, backed by a boolean.  It combines both a boolean value that is stored and used for comparisons with a text label for display to app users.  The boolean value can be used directly in **If**, **Filter** and other boolean contexts. |

Many of these data types are similar and have the same underlying representation, such as a Hyperlink field being treated as Text.  The additional data types allow for better default experiences in the form and other controls.

## Blank

All data types can have a value of *blank*, in other words contain no value.  The term "null" is often used in databases for this same concept.  

Use the **Blank** function with **Set** or **Patch** to set a variable or column to *blank*.  For example, **Set( x, Blank() )** removes any value in the global variable **x**.  

Use the [**IsBlank** function](functions/function-isblank-isempty.md) to test for a *blank* value.  Use the [**Coalesce** function](functions/function-isblank-isempty.md) function to replace possible *blank* values with a non-*blank* value. 

Because all data types support *blank*, the Boolean and Two option data types effectively have three possible values.

## Numbers and Currency

Number and Currency data types use the [IEEE 754 double precision floating point standard](https://en.wikipedia.org/wiki/IEEE_754).  This provides a very large range of numbers in which to work, from –1.79769 x 10<sup>308</sup> to 1.79769 x 10<sup>308</sup>.  The smallest representable value is 5 x 10<sup>–324</sup>

Whole numbers (or integers) can be exactly represented in the range –9,007,199,254,740,991 (–(2<sup>53</sup> – 1)) to 9,007,199,254,740,991 (2<sup>53</sup> – 1).  This is larger than the 32-bit (or 4-byte) integer data types that are commonly used in databases.  Note that 64-bit (or 8-byte) integer data types cannot be exactly represented; you may want to use the Text data type instead to hold, display, and enter these values but calculations cannot be performed.

Because floating point arithmetic is approximate it can sometimes give unexpected results.  There are many well known examples. Take the formula **55 / 100 * 100**.  One would expect this to return exactly 55 and that **(55 / 100 * 100) - 55** would return exactly zero.  But this is not the case, this formula returns a very small number 7.1054 x 10<sup>–15</sup>.  That tiny difference will normally not cause any problems and it will be rounded away when displayed.

Currencies are often stored and calculations performed using decimal math, with a smaller range but greater control over the precision.  By default, currencies will be mapped in and out of floating point values when used in a Canvas app and therefore the result may be different than calculations that are done in a native decimal data type.  As with large integers, if this will cause problems, you may want to use a Text data type to hold, display, and enter these values.

## Text and binary data types

There is no preset limit on the size of Text and binary data (Images, Media, Blobs).  

The underlying JavaScript implementation in the browser may impose a limit which is often over 100 MB.  

The amount of available memory on your device may impose another limit which is likely lower.  Testing common scenarios on the devices you expect to use is the only way to know that there will be adequate memory.  

## Dates and times

Date only, time only, and date time values are supported.

### Time zones

Within an app, all dates and times are expressed in the time zone of the app's user.  Dates and times are translated in and out of this time zones when they are stored and retrieved, if needed.  

For example, Common Data Service has **User local** date/time values that are stored in the database in UTC (Coordinated Universal Time).  When values are pulled from the database, they are translated from UTC to the time zone of the app's user, and when pushed back to the database they are translated back into UTC.  Common Data Service also has **Time zone independent** date/time values which are not translated in or out.  These translation are done automatically.  

Canvas apps use the time zone of the browser.  This differs from  Model-driven apps where the translation is based on the user's settings in Common Data Service.  Normally these are the same, but there can be cases where an app user has two different settings and will see two different results.

### Numeric values 

Under the covers, all date times values hold the number of milliseconds since January 1, 1970 00:00:00 UTC.  Use the [**Value** function](functions/function-value.md) to retrieve this numerical value.  

It is possible to add a single Time value to a Date value, for example **Date( 1970, 1, 1, ) + Time( 9, 12, 00 )**.  Other direct numerical operations between these types are either not supported or will return unexpected results.  Use the [**DateAdd**](functions/function-dateadd-datediff.md) and [**DateDiff**](functions/function-dateadd-datediff.md) functions to add or subtract from one of these values.

> [!NOTE]
> **Document team note:**  Our support for adding/subtracting date times is inconsistent.  In some cases I think we try to mimic Excel's behavior of 1 = 1 day rather than 1 = 1 millisecond.   Here are some of the odd results:
> 
> - Value( Date( 2000,1,1 ) ) = 946,713,600,000 (30 years in milliseconds)
> - Value( Date( 2000,1,2 ) ) - Value( Date( 2000,1,1 ) ) = 86,400,000 (24 hours in milliseconds)
> - **Date( 2000,1,2 ) - Date(2000,1,1) = 1 (Excel one day)**  
> - **Date( 2000,1,2 ) - Date(2000,1,1) + Date(2000,1,1) = 946,800,000,000** (30 years + 1 day in millesconds, I assume the first subtraction results in a number which causes the last Date to be coerced to a number)
>
> - Value( Date( 1970,1,1 ) ) = 28,800,000 (8 hours offset for pacific time)
> - Value( Time( 1,0,0 ) ) = 32,400,000 (9 hours offset for pacific time)
> - **Value( Date( 1970,1,1 ) ) + Value( Time( 1,0,0 ) ) = 61,200,000** (17 hours, 8 + 9 hour offsets for pacific time)
> - **Date( 1970,1,1 ) + Time( 1,0,0 ) = 32,400,000** (9 hour offset for pacific time.
> - **Date( 1970, 1,1 ) + Time( -1,0,0 ) = 111,600,000 I have no idea where this number is coming from**, formatted as a date it is 1970-01-01 23 : 00 : 00**
> - Date( 2000,1,2) - Time(1,0,0) = compile time error
> - Date( 2000,1,2) + Time(1,0,0) + Time(2,0,0) = compile time error
> - DateTimeValue( "January 1, 1970" ) + Time(1,0,0) = compile time error
> 
> I think we should, over time, clean this up.  I think we should standardize on milliseconds and not try to convert to/from Excel's representation.  As this would be a breaking change, it is something we'd need to put under a preview flag.
>
> Or we should outright block add/subract between date/time values.  And allow DateAdd to take a Date/TIme value as its second argument so we can back compat to this function.
>
> I am still trying to get my head around us using date/time values with a timezone offset internally.  That seems really messy and is the source of much pain when working with SQL.  I'd prefer that we were time zone agnostic, that Value(Date(1970,1,1)) returned 0.  Perhaps another change that should be under the preview flag. 
>
> I'd like to provide some relief for this blog post: https://powerapps.microsoft.com/en-us/blog/working-with-time-columns-in-sql-server/

## Option sets and two options



## Compound data types



