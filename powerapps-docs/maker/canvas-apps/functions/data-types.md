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

Information flows through an app in small, discrete values, very much like the cells of a spreadsheet.  For example, a **Birthday** and an **Anniversary** would both flow through as a **Date** that includes year, month, and day.  The app knows how to format these values, how to constrain input to what is appropriate for each, and how to share these values with a database.  Although they have two different meanings to a person, to the system the **Birthday** and **Anniversary** are handled in exactly the same manner.  **Date** in this case is an example of a [data type](https://en.wikipedia.org/wiki/Data_type).  

This article provides details for the data types supported by canvas apps.  When connecting to external data sources, all the data types of the data source are mapped to canvas data types.

| Data type | Description | Examples |
|-----------|-------------|---------|
| **Boolean** | A *true* or *false* value.  Can be used directly in **If**, **Filter** and other functions without a comparison.  | *true* |
| **Hyperlink** | A text string that holds a hyperlink. | **"http://powerapps.microsoft.com"** |
| **Currency** | Currency value stored in a floating point number. Currency values are the same as number values with currency formatting options.  | **123**<br>**4.56** |  
| **Image** | [Universal Resource Identifier (URI)](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)  text string to an image in Jpeg, PNG, SVG, GIF, and other common web image formats. | **"appres://blobmanager/7b12ffa2..."** |
| **Color** | Color including an alpha channel. | **Color.Red**<br>**ColorValue( "#102030" )**<br>**RGBA( 255, 128, 0, 0.5 )** | 
| **Date** | Date only, in the time zone of the app's user. | **Date( 2019, 5, 16 )** |
| **DateTime** | Date with time, in the time zone of the app's user. | **DateTimeValue( "May 16, 2019 1:23:09 PM" )** |
| **GUID** | [Globally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier). | **GUID()**<br>**GUID( "123e4567-e89b-12d3-a456-426655440000" )** |
| **Media** | URI text string to a video or audio recording. | **"appres://blobmanager/3ba411c..."** |
| **Number** | Floating point number. | **123**<br>**-4.567**<br>**8.903e121** |
| **Option set** | Choice from a set of options, backed by a number. It combines both a numeric value that is stored and used for comparisons with a text label for display to app users. | **ThisItem.OrderStatus** |
| **Record reference** | A reference to a record in an entity, often used with polymorphic lookups. | **First(Accounts).Owner** |  
| **Time** | Time only, in the time zone of the app's user. | **Time( 11, 23, 45 )** |
| **Text** | Unicode text string. | **"Hello, World"** |
| **Two option** | Choice from a set of two options, backed by a Boolean.  It combines both a boolean value that is stored and used for comparisons with a text label for display to app users.  | **ThisItem.Taxable** |

Many of these data types are similar and have the same underlying representation, such as a **Hyperlink** field being treated as **Text**.  The additional data types allow for better default experiences in the form and other controls.

## Blank

All data types can have a value of *blank*, in other words no value.  The term "null" is often used in databases for this concept.  

Use the **Blank** function with **Set** or **Patch** to set a variable or field to *blank*.  For example, **Set( x, Blank() )** removes any value in the global variable **x**.  

Use the [**IsBlank** function](function-isblank-isempty.md) to test for a *blank* value.  Use the [**Coalesce** function](function-isblank-isempty.md) function to replace possible *blank* values with a non-*blank* value. 

Because all data types support *blank*, the Boolean and Two option data types effectively have three possible values.

## Text, Hyperlink, Image, and Media

All four of these data types are based on a [Unicode](https://en.wikipedia.org/wiki/Unicode) text string.

### Size limits

There is no preset limit on the length of these data types.  

The underlying JavaScript implementation in your browser or on your device may impose a limit but it is usually well over 100 MB.  

The amount of available memory on your device may impose another limit which is likely lower than 100 MB.  Testing common scenarios on the devices you expect to use is the only way to know that there will be adequate memory. 

### Images and Media URIs

Images and media are references by a URI Text string.  For example, the **Image** property of the [**Image** control](../controls/control-image.md) accepts links to images on the web, such as **"https://northwindtraders.com/logo.jpg"**.  It also accepts inline images that use the [data URI scheme](https://en.wikipedia.org/wiki/Data_URI_scheme) such as:
```powerapps-dot
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAFAQMAAACtnVQoAAAABlBMVEUAAAB0J3UMNU6VAAAAAXRSTlMAQObYZgAAABRJREFUCNdjUGJgCGVg6GgAkkA2AA8/AffqCEBsAAAAAElFTkSuQmCC"
```
which displays a scaled up version of two purple diamonds:

![](media/data-types/double-diamonds.png)

The same is true if you take a picture with the [**Camera** control](../controls/control-camera.md).  The image is held in memory and the **Photo** property of the control will return a URI to reference the image.  For example, you might take a picture and the **Photo** property might return **"appres://blobmanager/7b12ffa2ea4547e5b3812cb1c7b0a2a0/1"**.  You can feed this Text string directly to the **Image** control to display the captured image.

Images and files stored in databases may not be retrieved until displayed. A reference of the form **"appres://datasources/Contacts/table/..."** may be used to reference the image, avoiding downloading the image until needed.  As with the camera, this reference can be fed to the **Image** control to display the image.

## Numbers and Currency

Number and Currency data types use the [IEEE 754 double precision floating point standard](https://en.wikipedia.org/wiki/IEEE_754).  This provides a very large range of numbers in which to work, from –1.79769 x 10<sup>308</sup> to 1.79769 x 10<sup>308</sup>.  The smallest representable value is 5 x 10<sup>–324</sup>

Whole numbers (or integers) can be exactly represented in the range –9,007,199,254,740,991 (–(2<sup>53</sup> – 1)) to 9,007,199,254,740,991 (2<sup>53</sup> – 1).  This is larger than the 32-bit (or 4-byte) integer data types that are commonly used in databases.  But 64-bit (or 8-byte) integer data types cannot be exactly represented; you may want to use the Text data type instead to hold, display, enter, and equal/not equal compare these values.  Numerical calculations will not be possible.

Because floating point arithmetic is approximate it can sometimes give unexpected results with many documented examples. Take the formula **55 / 100 * 100**.  One would expect this to return exactly 55 and that **(55 / 100 * 100) - 55** would return exactly zero.  But this is not the case, this formula returns a very small number 7.1054 x 10<sup>–15</sup>.  That tiny difference will normally not cause any problems and it will be rounded away when displayed.  Small differences can compound in subsequent calculations and can appear to be giving the wrong answer.

In database systems, currencies are often stored and calculations performed using decimal math, with a smaller range but greater control over the precision.  By default, currencies will be mapped in and out of floating point values when used in a canvas app and therefore the result may be different than calculations that are done in a native decimal data type.  As with large integers, if this will cause problems, you may want to use a Text data type to work with these values.

## Date, Time, and DateTime

All three of these data types hold the same date and time information.  A **Date** can include time information with it, which is usually midnight, and a **Time** can carry date information, which is usually January 1, 1970.  The distinction between these data types is used in some cases for default formatting and control selection.

### Time zones

Within an app, all dates and times are expressed in the time zone of the app's user.  Dates and times are translated in and out of this time zones when they are stored and retrieved, if needed.  

Canvas apps use the time zone of the browser.  This differs from  Model-driven apps where the translation is based on the user's setting in Common Data Service.  Normally these are the same, but there can be cases where an app user has two different settings and will see two different results.

### UTC and Time zone independent

Common Data Service uses **User local** date/time values that are stored in the database in [UTC (Coordinated Universal Time)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).  When these values are pulled from the database, they are translated from UTC to the time zone of the app's user, and when pushed back to the database they are translated back into UTC.  SharePoint date/time values are also stored in UTC.

Common Data Service also has **Time zone independent** date/time values which are not translated in or out.  The same value is seen by all app users, no matter what time zone they are in.

SQL Server has **Datetime2** and other date/time data types that do not include a time zone offset. Canvas apps assume these values are stored in UTC since the database does not indicate how they should be interpreted. If the values are meant to be time zone independent then use the [**TimeZoneOffset** function](function-dateadd-datediff.md#converting-to-utc) to correct for the UTC translations.

### Numeric equivalents

Under the covers, all date times values hold the number of milliseconds since January 1, 1970 00:00:00 UTC in your local time zone. Use the [**Value** function](function-value.md) to retrieve this numerical value. Under the covers, the JavaScript data object is used to hold the values.  

Because it is in your local time zone, for most parts of the world the formula **Value( Date( 1970, 1, 1 ) )** will not return zero.  For example, in a time zone that is offset by 8 hours from UTC, this number will be 28,800,000 milliseconds, the equivalent of 8 hours.

Direct adding and subtracting of date and time values should be avoided because of the impact of time zones.  Either use the **Value** function first to convert to milliseconds first or use the [**DateAdd**](function-dateadd-datediff.md) and [**DateDiff**](function-dateadd-datediff.md) functions to add or subtract from one of these values.

### Converting Unix times

Unix times are the number of seconds since January 1, 1970 00:00:00 UTC, which is the same starting base as PowerApps.  All that is needed is to multiply or divide by 1,000 to convert between the two.

For example, Unix time hit 1,000,000,000 on September 9, 2001 at 01:46:40 UTC.  Take this number and multiply by 1,000 to convert to milliseconds and feed to the [**Text** function](function-text.md) to display the number as a date time.  For example **Text( 1000000000 * 1000, DateTimeFormat.UTC )** will result in the string **2001-09-09T01:46:40.000Z**.

If we use the **DateTimeFormat.LongDateTime24** format and live in a time zone that is 8 hours offset from UTC, the result is different: **Saturday, September 8, 2001 18:46:40**.  Which is correct because the time zone has impacted how this DateTime is interpreted.

### SQL Server Time values

The SQL Server [**Time** data type](https://docs.microsoft.com/en-us/sql/t-sql/data-types/time-transact-sql) is read and written by PowerApps as a Text string in the [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).  For example, converting the text string **"PT2H1M39S"** to a Time value requires parsing this string format and using the [**Time** function](function-date-time.md):

```powerapps-dot
First(
    ForAll(
        MatchAll( "PT2H1M39S", "PT(?:(?<hours>\d+)H)?(?:(?<minutes>\d+)M)?(?:(?<seconds>\d+)S)?" ),
        Time( Value( hours ), Value( minutes ), Value( seconds ) )
    )
).Value
```

## Option sets and Two options

Option sets and two option data types provide a list of choices for an end user to select.  For example, an **Order Status** option set may offer the choices **New**, **Shipped**, **Invoiced**, and **Closed**.  Two options are limited to two choices.

Both of these data types will display their labels when in a text string context.  For example, feeding an option set to the **Text** property of a **Label** control will display one of the above labels to the app user.  For app users in different locations, these labels may be localized.

When stored in the database and transmitted over the network to a connector, a language independent representation is used instead of the labels: for option sets a number and for two options a Boolean.  

The labels are for display purposes only.  Direct comparisons with the labels are not permitted as this would not be language independent.  Instead an enumeration is provided for each option set that works with the underlying number or Boolean.  For example, **If( ThisIteem.OrderStatus = "Active", ...** is not allowed while **If( ThisItem.OrderStatus = OrderStatus.Active, ...** is allowed.

In addition, two option values can also behave as Boolean values. For example, consider a two option named **TaxStatus** with labels **Taxable** and **Non-Taxable** corresponding to *true* and *false* respectively. **If( ThsiItem.Taxable = TaxStatus.Taxable, ...** is allowed as is the equivalent **If( ThisItem.Taxable, ...**.

## Record references

Record references hold a reference or pointer to a specific record in an entity.  For more information, read [working with references](../working-with-references.md). 




