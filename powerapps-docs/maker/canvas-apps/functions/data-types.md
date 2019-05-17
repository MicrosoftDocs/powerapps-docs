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

Information flows through an app in small, discrete values, very much like the cells of a spreadsheet. For example, a **Birthday** and an **Anniversary** would both flow through as a **Date** that includes the year, the month, and the day. The app knows how to format these values, constrain input to what is appropriate for each, and share the values with a database. **Birthday** and **Anniversary** differ to people, but the system handles them in exactly the same manner. **Date**, in this case, is an example of a [data type](https://en.wikipedia.org/wiki/Data_type).

This article provides details for the data types that canvas apps support. When an app connects to an external data source, each data type in that source is mapped to a data type for canvas apps.

| Data type | Description | Examples |
|-----------|-------------|---------|
| **Boolean** | A *true* or *false* value.  Can be used directly in **If**, **Filter** and other functions without a comparison.  | *true* |
| **Hyperlink** | A text string that holds a hyperlink. | **"http://powerapps.microsoft.com"** |
| **Currency** | A currency value stored in a floating-point number. Currency values are the same as number values with currency-formatting options.  | **123**<br>**4.56** |
| **Image** | A [Universal Resource Identifier (URI)](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)  text string to an image in .jpeg, .png, .svg, .gif, and other common web image formats. | **"appres://blobmanager/7b12ffa2..."** |
| **Color** | A color specification, including an alpha channel. | **Color.Red**<br>**ColorValue( "#102030" )**<br>**RGBA( 255, 128, 0, 0.5 )** | 
| **Date** | A date without a time, in the time zone of the app's user. | **Date( 2019, 5, 16 )** |
| **DateTime** | A date with a time, in the time zone of the app's user. | **DateTimeValue( "May 16, 2019 1:23:09 PM" )** |
| **GUID** | A [Globally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier). | **GUID()**<br>**GUID( "123e4567-e89b-12d3-a456-426655440000" )** |
| **Media** | A URI text string to a video or audio recording. | **"appres://blobmanager/3ba411c..."** |
| **Number** | A floating-point number. | **123**<br>**-4.567**<br>**8.903e121** |
| **Option set** | A choice from a set of options, backed by a number. This data type combines a numeric value that's stored and used for comparisons with a localizable text label that the app shows. | **ThisItem.OrderStatus** |
| **Record reference** | A reference to a record in an entity, often used with polymorphic lookups. | **First(Accounts).Owner** |  
| **Time** | A time without a date, in the time zone of the app's user. | **Time( 11, 23, 45 )** |
| **Text** | A Unicode text string. | **"Hello, World"** |
| **Two option** | A choice from a set of two options, backed by a Boolean. This data type combines a boolean value that's stored and used for comparisons with a localizable text label that the app shows.  | **ThisItem.Taxable** |

Many of these data types are similar and have the same underlying representation, such as a **Hyperlink** field being treated as **Text**.  The additional data types allow for better default experiences in forms and other controls.

## Blank

All data types can have a value of *blank* (in other words, no value). The term "null" is often used in databases for this concept.  

Use the **Blank** function with the **Set** or **Patch** function to set a variable or field to *blank*. For example, **Set( x, Blank() )** removes any value in the global variable **x**.  

Use the [**IsBlank**](function-isblank-isempty.md) function to test for a *blank* value.  Use the [**Coalesce**](function-isblank-isempty.md) function to replace possible *blank* values with non-*blank* values.

Because all data types support *blank*, the Boolean and Two option data types effectively have three possible values.

## Text, Hyperlink, Image, and Media

All four of these data types are based on a [Unicode](https://en.wikipedia.org/wiki/Unicode) text string.

### Size limits

These data types have no preset limit on their length.

The underlying JavaScript implementation in your browser or on your device may impose a limit, but it's usually well over 100 MB.

The amount of available memory on your device may impose another limit that's likely lower than 100 MB. To determine whether your app will run within these limits, test common scenarios on all devices on which it should run.

### Images and Media URIs

Images and media are references by a URI text string. For example, the **Image** property of the [**Image**](../controls/control-image.md) control accepts links to images on the web, such as **"https://northwindtraders.com/logo.jpg"**. The property also accepts inline images that use the [data URI scheme](https://en.wikipedia.org/wiki/Data_URI_scheme), as in this example:

```powerapps-dot
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAFAQMAAACtnVQoAAAABlBMVEUAAAB0J3UMNU6VAAAAAXRSTlMAQObYZgAAABRJREFUCNdjUGJgCGVg6GgAkkA2AA8/AffqCEBsAAAAAElFTkSuQmCC"
```

That URI displays a scaled-up version of two purple diamonds:

![](media/data-types/double-diamonds.png)

The same is true if you take a picture with the [**Camera**](../controls/control-camera.md) control. The image is held in memory, and the **Photo** property of the control returns a URI to reference the image. For example, you might take a picture, and the camera's **Photo** property might return **"appres://blobmanager/7b12ffa2ea4547e5b3812cb1c7b0a2a0/1"**. You can feed this text string directly to the **Image** property of an image to display the photo that you took.

The app might not retrieve images and files stored in databases until it needs to display that information. You can implement that behavior if you reference the image in this form **"appres://datasources/Contacts/table/..."** As in the camera example, you can show this image by feeding this reference to the **Image** property of the image control.

## Numbers and Currency

Number and Currency data types use the [IEEE 754 double precision floating point standard](https://en.wikipedia.org/wiki/IEEE_754). This standard provides a very large range of numbers in which to work, from –1.79769 x 10<sup>308</sup> to 1.79769 x 10<sup>308</sup>.  The smallest representable value is 5 x 10<sup>–324</sup>.

Canvas apps can exactly represent whole numbers (or integers) in the range –9,007,199,254,740,991 (–(2<sup>53</sup> – 1)) to 9,007,199,254,740,991 (2<sup>53</sup> – 1). This range is larger than the 32-bit (or 4-byte) integer data types that databases commonly use. However, canvas apps can't represent 64-bit (or 8-byte) integer data types; you might want to use the Text data type instead to hold, display, and enter these values, as well as comparing them to determine whether they're equal. You can't perform numerical calculations on them in this form.

Floating-point arithmetic is approximate, so it can sometimes give unexpected results with many documented examples. One would expect that the formula **55 / 100 * 100** to return exactly 55 and that **(55 / 100 * 100) - 55** would return exactly zero. However, this formula returns 7.1054 x 10<sup>–15</sup>, which is very small. That tiny difference will normally not cause any problems, and the app will round it away when displaying the result. However, small differences can compound in subsequent calculations and appear to give the wrong answer.

Database systems often store currencies and perform calculations by using decimal math, with a smaller range but greater control over the precision. By default, canvas apps map currencies in and out of floating-point values; therefore, the result might differ from calculations that are done in a native decimal data type. If this type of discrepancy will cause problems, you may want to use a Text data type to work with these values as you might with large integers.

## Date, Time, and DateTime

These three data types hold the same information about dates and times. A **Date** value can include time information with it, which is usually midnight. A **Time** value can carry date information, which is usually January 1, 1970. Canvas apps sometimes distinguish between these data types to determine default formats and controls.

### Time zones

Canvas apps express all dates and times in the time zone of the app's user. If necessary, these apps translate dates and times in and out of this time zone when storing and retrieving them.

Canvas apps use the time zone of the browser instead of the user's setting in Common Data Service, as model-driven apps do. These settings typically match, but results will differ if these settings differ.

### UTC and Time-zone independent

Common Data Service stores **User local** date/time values in the database in [UTC (Coordinated Universal Time)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). When a canvas app pulls these values from the database, the app translates them from UTC to the time zone of the app's user. The app translates the values back into UTC when pushing them back to the database. SharePoint date/time values undergo similar translations.

Common Data Service also has **Time zone independent** date/time values, which the app doesn't translate in or out. The same value appears to all app users, no matter what time zone they're in.

SQL Server has **Datetime2** and other date/time data types that don't include a time-zone offset. Canvas apps assume these values are stored in UTC because the database doesn't indicate how they should be interpreted. If the values are meant to be time-zone independent, correct for the UTC translations by using the [**TimeZoneOffset**](function-dateadd-datediff.md#converting-to-utc) function.

### Numeric equivalents

Under the covers, all date/time values hold the number of milliseconds since January 1, 1970 00:00:00 UTC in your local time zone. Retrieve this numerical value by using the [**Value**](function-value.md) function. Under the covers, the JavaScript data object is used to hold the values.

Because every date is in your local time zone, the formula **Value( Date( 1970, 1, 1 ) )** won't return zero in most parts of the world. For example, this number will be 28,800,000 milliseconds (the equivalent of eight hours) in a time zone that's offset by eight hours from UTC.

You should avoid adding and subtracting date and time values directly because of the impact of time zones. Either use the **Value** function to convert to milliseconds first, or use the [**DateAdd**](function-dateadd-datediff.md) and [**DateDiff**](function-dateadd-datediff.md) functions to add or subtract from one of these values.

### Converting Unix times

Unix times are the number of seconds since January 1, 1970 00:00:00 UTC, which is the same starting base as PowerApps. To convert between the two, you need only to multiply or divide by 1,000.

For example, Unix time hit 1,000,000,000 on September 9, 2001, at 01:46:40 UTC. To display 1,000,000,000 as a date/time, multiply it by 1,000 to convert it to milliseconds, and then feed to the [**Text**](function-text.md) function. The formula **Text( 1000000000 * 1000, DateTimeFormat.UTC )** returns the string **2001-09-09T01:46:40.000Z**.

However, the function returns **Saturday, September 8, 2001 18:46:40** if you use the **DateTimeFormat.LongDateTime24** format in a time zone that's eight hours offset from UTC. This result shows the DateTime value correctly based on the local time zone.

### Time values in SQL Server

Canvas apps read and write values of the [**Time**](https://docs.microsoft.com/en-us/sql/t-sql/data-types/time-transact-sql) data type in SQL Server as Text strings in the [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations). For example, you must parse this string format and use the [**Time**](function-date-time.md) function to convert the text string **"PT2H1M39S"** to a Time value:

```powerapps-dot
First(
    ForAll(
        MatchAll( "PT2H1M39S", "PT(?:(?<hours>\d+)H)?(?:(?<minutes>\d+)M)?(?:(?<seconds>\d+)S)?" ),
        Time( Value( hours ), Value( minutes ), Value( seconds ) )
    )
).Value
```

## Option sets and Two options

Option sets and two-option data types provide a list of choices for an end user to select. For example, an **Order Status** option set might offer the choices **New**, **Shipped**, **Invoiced**, and **Closed**. The two-option type offers only two choices.

Both of these data types show their labels in a text-string context. For example, a label shows one of the order-status options if the label's **Text** property is set to a formula that references that option set. For app users in different locations, these option labels might be localized.

When an app user selects an option and saves that change, the app transmits the data to the database, which stores that data in a representation that's independent of language instead of a label. An option in an option set is transmitted and stored as a number, and an option in a two-option type is transmitted and stored as a Boolean.

The labels are for display purposes only. You can't perform direct comparisons with the labels because they're specific to a language. Instead, each option set has an enumeration that works with the underlying number or Boolean. For example, you can use this formula:

`If( ThisItem.OrderStatus = "Active"...`

You can't use this formula:

`If( ThisItem.OrderStatus = OrderStatus.Active, ...`

In addition, two-option values can also behave as Boolean values. For example, a two-option value named **TaxStatus** might have the labels **Taxable** and **Non-Taxable**, which correspond to *true* and *false* respectively. To demonstrate, you can use this formula:

`If( ThisItem.Taxable = TaxStatus.Taxable, ...`

You can also use this equivalent formula:

`If( ThisItem.Taxable, ...`

## Record references

Record references hold references or pointers to specific records in an entity. More information: [Working with references](../working-with-references.md).