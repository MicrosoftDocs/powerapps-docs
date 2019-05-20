---
title: Data types | Microsoft Docs
description: Data types in canvas apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/19/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Data types in canvas apps

Information flows through an app in small, discrete values, very much like the cells of a spreadsheet. For example, data in a **Birthday** field and an **Anniversary** field would both flow through as a **Date** that includes the year, the month, and the day. The app knows how to format these values, constrain input to what is appropriate for each, and share the values with a database. Birthdays differ from anniversaries to people, but the system handles them in exactly the same manner. In this case, **Date** is an example of a [data type](https://en.wikipedia.org/wiki/Data_type).

This article provides details for the data types that canvas apps support. When an app connects to an external data source, each data type in that source is mapped to a data type for canvas apps.

| Data type | Description | Examples |
|-----------|-------------|---------|
| **Boolean** | A *true* or *false* value.  Can be used directly in **If**, **Filter** and other functions without a comparison.  | *true* |
| **Hyperlink** | A text string that holds a hyperlink. | **"http://powerapps.microsoft.com"** |
| **Currency** | A currency value that's stored in a floating-point number. Currency values are the same as number values with currency-formatting options.  | **123**<br>**4.56** |
| **Image** | A [Universal Resource Identifier (URI)](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)  text string to an image in .jpeg, .png, .svg, .gif, and other common web-image formats. | **MyImage** added as an app resource<br>**"https://northwindtraders.com/logo.jpg"**<br>**"appres://blobmanager/7b12ffa2..."** |
| **Color** | A color specification, including an alpha channel. | **Color.Red**<br>**ColorValue( "#102030" )**<br>**RGBA( 255, 128, 0, 0.5 )** |
| **Date** | A date without a time, in the time zone of the app's user. | **Date( 2019, 5, 16 )** |
| **DateTime** | A date with a time, in the time zone of the app's user. | **DateTimeValue( "May 16, 2019 1:23:09 PM" )** |
| **GUID** | A [Globally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier). | **GUID()**<br>**GUID( "123e4567-e89b-12d3-a456-426655440000" )** |
| **Media** | A URI text string to a video or audio recording. | **MyVideo** added as an app resource<br>**"https://northwindtraders.com/intro.mp4"**<br>**"appres://blobmanager/3ba411c..."** |
| **Number** | A floating-point number. | **123**<br>**-4.567**<br>**8.903e121** |
| **Option set** | A choice from a set of options, backed by a number. This data type combines a numeric value that's stored and used for comparisons with a localizable text label that the app shows. | **ThisItem.OrderStatus** |
| **Record** | A record of data values. A compound data type that contains instances of other data types listed in this topic.  More information: [Working with tables](../working-with-tables.md). | **{ Company: "Northwind Traders",<br>Staff: 35, <br>NonProfit: false }** |
| **Record reference** | A reference to a record in an entity, often used with polymorphic lookups. More information: [Working with references](../working-with-references.md).| **First(Accounts).Owner** |
| **Table** | A table of records.  All of the records must have the same names for their fields with the same data types, and omitted fields are treated as *blank*. This compound data type contains instances of other data types that are listed in this topic. More information: [Working with tables](../working-with-tables.md). | **Table( { FirstName: "Sidney",<br>LastName: "Higa" }, <br>{ FirstName: "Nancy",<br>LastName: "Anderson" } )**
| **Text** | A Unicode text string. | **"Hello, World"** |
| **Time** | A time without a date, in the time zone of the app's user. | **Time( 11, 23, 45 )** |
| **Two option** | A choice from a set of two options, backed by a Boolean. This data type combines a boolean value that's stored and used for comparisons with a localizable text label that the app shows.  | **ThisItem.Taxable** |

Many of these data types are similar and have the same underlying representation, such as a **Hyperlink** field being treated as **Text**.  The additional data types provide better default experiences in forms and other controls.

## Blank

All data types can have a value of *blank* (in other words, no value). The term "null" is often used in databases for this concept.  

Use the **Blank** function with the **Set** or **Patch** function to set a variable or field to *blank*. For example, **Set( x, Blank() )** removes any value in the global variable **x**.  

Use the [**IsBlank**](function-isblank-isempty.md) function to test for a *blank* value.  Use the [**Coalesce**](function-isblank-isempty.md) function to replace possible *blank* values with non-*blank* values.

Because all data types support *blank*, the **Boolean** and **Two option** data types effectively have three possible values.

## Text, Hyperlink, Image, and Media

All four of these data types are based on a [Unicode](https://en.wikipedia.org/wiki/Unicode) text string.

### Size limits

These data types have no preset limit on their length.

The underlying JavaScript implementation in your browser or on your device may impose a limit, but it's usually well over 100 MB.

The amount of available memory on your device may impose another limit that's likely lower than 100 MB. To determine whether your app will run within these limits, test common scenarios on all devices on which it should run.

### Image and Media resources

Through the **File** menu, you can add image, video, and audio files as app resources. The name of the imported file becomes the resource name in the app. In this graphic, the Northwind Traders logo, which is named **nwindlogo**, has been added to an app:

![](media/data-types/nwind-resource.png)

To use this resource in an app, specify it in the **Image** property of an [**Image**](../controls/control-image.md) control:

![](media/data-types/nwind-image.png)

### URIs for images and other media

You can dig a little deeper into that last example by setting the **Text** property of a [**Label**](../controls/control-text-box.md) control to **nwindlogo**. The label shows a text string:

![](media/data-types/nwind-text.png)

Canvas apps reference each image or other media file, whether it's in the cloud or added as an app resource, by a URI text string.

For example, the **Image** property of an **Image** control accepts not only app resources but also links to images on the web, such as "https://northwindtraders.com/logo.jpg". The property also accepts inline images that use the [data URI scheme](https://en.wikipedia.org/wiki/Data_URI_scheme), as in this example:

```powerapps-dot
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAFAQMAAACtnVQoAAAABlBMVEUAAAB0J3UMNU6VAAAAAXRSTlMAQObYZgAAABRJREFUCNdjUGJgCGVg6GgAkkA2AA8/AffqCEBsAAAAAElFTkSuQmCC"
```

That URI displays a scaled-up version of two purple diamonds:

![](media/data-types/double-diamonds.png)

The same is true with the [**Camera**](../controls/control-camera.md) control. You can show the last image captured if you set the **Image** property of an **Image** control to the **Photo** property of a **Camera** control. The app holds the image in memory, and the **Photo** property of the camera returns a URI reference to the image. For example, you might take a picture, and the camera's **Photo** property could return **"appres://blobmanager/7b12ffa2ea4547e5b3812cb1c7b0a2a0/1"**.

Images and media stored in databases is referenced by URI.  This avoids retrieving the actual data until actually needed.  For example, an attachment of a Common Data Service entity might return **"appres://datasources/Contacts/table/..."** As in the camera example, you can display this image by setting the **Image** property of the image control to this reference which will retrieve the binary data.

When you save an image or another media data type to a database, the app sends the actual image or media data, not the URI reference.

## Number and Currency

**Number** and **Currency** data types use the [IEEE 754 double precision floating point standard](https://en.wikipedia.org/wiki/IEEE_754). This standard provides a very large range of numbers in which to work, from –1.79769 x 10<sup>308</sup> to 1.79769 x 10<sup>308</sup>.  The smallest representable value is 5 x 10<sup>–324</sup>.

Canvas apps can exactly represent whole numbers (or integers) between –9,007,199,254,740,991 (–(2<sup>53</sup> – 1)) and 9,007,199,254,740,991 (2<sup>53</sup> – 1), inclusive. This range is larger than the 32-bit (or 4-byte) integer data types that databases commonly use. However, canvas apps can't represent 64-bit (or 8-byte) integer data types; you might want to store the number in a text field or use a calculated column to make a copy of the number in a text field, so that it is mapped into a  **Text** data type in the canvas app.  In this manner, you can hold, display, and enter these values, as well as comparing them to determine whether they're equal; however, you can't perform numerical calculations on them in this form.

Floating-point arithmetic is approximate, so it can sometimes give unexpected results with many documented examples. You might expect the formula **55 / 100 * 100** to return exactly 55 and **(55 / 100 * 100) - 55** to return exactly zero. However, the latter formula returns 7.1054 x 10<sup>–15</sup>, which is very small but not zero. That tiny difference will normally not cause a problem, and the app will round it away when showing the result. However, small differences can compound in subsequent calculations and appear to give the wrong answer.

Database systems often store currencies and perform calculations by using decimal math, with a smaller range but greater control over the precision. By default, canvas apps map currencies in and out of floating-point values; therefore, the result might differ from calculations that are done in a native decimal data type. If this type of discrepancy will cause problems, you might want to work with these values as **Text**, just as you might with large integers described above.

## Date, Time, and DateTime

### Time zones

Date/times come in two main flavors:
- **User local**: The date/time is displayed and entered in the time zone of the app's user.  These values are stored in [UTC (Coordinated Universal Time)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) and then adjusted for display and entry by the app.  A user in Canada will see a different date/time than a user in Japan although both describe the same moment in time; for both users the displayed value will have been adjusted for their individual time zones.
- **Time zone independent**: The date/time is displayed and entered with the same value for all users, no matter which time zone they are in.   A user in Canada sees the same value as a user in Japan.  This is often used because it is simpler overall and the app author does not expect the app to be used in different time zones.

For example:

| Date/time type | Value stored in the database | Value displayed and entered 7 hours west of UTC | Value displayed and entered 4 hours east of UTC | 
|--------------------------|------------------------------|------------------------------|
| User local | Sunday, May 19, 2019<br>4:00 AM | Saturday, May 18, 2019<br>9:00 PM | Sunday, May 19, 2019<br>8:00 AM |
| Time zone independent | Sunday, May 19, 2019<br>4:00 AM | Sunday, May 19, 2019<br>4:00 AM |  Sunday, May 19, 2019<br>4:00 AM | 

SQL Server has [**Datetime**, **Datetime2**, and other date/time data types](https://docs.microsoft.com/en-us/sql/t-sql/functions/date-and-time-data-types-and-functions-transact-sql?view=sql-server-2017) that don't include a time-zone offset. Canvas apps assume these values are stored in UTC and treated as **User local** because the database doesn't indicate how to interpret them. If the values are meant to be time-zone independent, correct for the UTC translations by using the [**TimeZoneOffset**](function-dateadd-datediff.md#converting-to-utc) function.

For **User local** date/times, canvas apps use the time zone of the browser or device, but model-driven apps use the user's setting in Common Data Service. These settings typically match, but results will differ if these settings differ.

### UTC and Time-zone independent

Common Data Service stores **User local** date/time values in [UTC (Coordinated Universal Time)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). No translation is required for these values as they flow in and out of a canvas app.  

Common Data Service also has **Time zone independent** date/time values.  These values are translated in and out of UTC with the inverse of the app user's time zone offset, compensating for the time zone offset applied when displayed or entered.  


### Numeric equivalents

All date/time values in a canvas app are held and calculated in UTC.  Values are translated to the app user's time zone at the point they are displayed or entered.  

This is true for **Time zone independent** values as well.  When read from and written to a data source, these values are automatically adjusted to compensate for the time zone of the app's user.  The app will then treat them as UTC values, consistent with all other date/time values in the app.  Because of this compensation, their original time zone independent value is displayed to the user when the app adjusts the UTC value for the app user's time zone.

To look at this more closely, we can access the underlying numerical value for a date/time with the [**Value**](function-value.md) function.  It returns the date/time as the raw number of milliseconds since January 1, 1970 00:00:00.000 UTC. 

Because every date/time is held in UTC, the formula **Value( Date( 1970, 1, 1 ) )** won't return zero in most parts of the world because the **Date** function returns a date in UTC. For example, the formula would return 28,800,000 in a time zone that's offset from UTC by eight hours. That number reflects the number of milliseconds in eight hours.

Returning to our example from above:

| Date/time type | Value stored in the database |  Value displayed and entered 7 hours west of UTC | **Value** function returns |
|--------------------------|------------------------------|------------------------------|
| User local | Sunday, May 19, 2019<br>4:00 AM | Saturday, May 18, 2019<br>9:00 PM | 1,558,238,400,000<br> (Sunday, May 19, 2019<br>4:00 AM UTC) |
| Time zone independent | Sunday, May 19, 2019<br>4:00 AM | Sunday, May 19, 2019<br>4:00 AM |1,558,263,600,000<br> (Sunday, May 19, 2019<br>11:00 AM UTC) |

### Converting Unix times

Unix times reflect the number of seconds since January 1, 1970 00:00:00 UTC. Because canvas apps use milliseconds instead of seconds, you can convert between the two by multiplying or dividing by 1,000.

For example, Unix time shows September 9, 2001, at 01:46:40 UTC as 1,000,000,000. To show that a date/time in a canvas app, multiply that number by 1,000 to convert it to milliseconds, and then use it in a [**Text**](function-text.md) function. The formula **Text( 1000000000 * 1000, DateTimeFormat.UTC )** returns the string **2001-09-09T01:46:40.000Z**.

However, that function returns **Saturday, September 8, 2001 18:46:40** if you use the **DateTimeFormat.LongDateTime24** format in a time zone that's -7 hours offset from UTC (7 hours west of UTC). This result shows the DateTime value correctly based on the local time zone.

### Time values in SQL Server

Canvas apps read and write values of the [**Time**](https://docs.microsoft.com/en-us/sql/t-sql/data-types/time-transact-sql) data type in SQL Server as text strings in the [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations). For example, you must parse this string format and use the [**Time**](function-date-time.md) function to convert the text string **"PT2H1M39S"** to a **Time** value:

```powerapps-dot
First(
    ForAll(
        MatchAll( "PT2H1M39S", "PT(?:(?<hours>\d+)H)?(?:(?<minutes>\d+)M)?(?:(?<seconds>\d+)S)?" ),
        Time( Value( hours ), Value( minutes ), Value( seconds ) )
    )
).Value
```
### Mixing date and time information

Despite their different names, **Date**, **Time**, and **DateTime** all hold the same information about dates and times. 

A **Date** value can include time information with it, which is usually midnight. A **Time** value can carry date information, which is usually January 1, 1970. Common Data Service also stores time information with a Date Only field and by default only shows the date information.  Similarly, canvas apps sometimes distinguish between these data types to determine default formats and controls.

Adding and subtracting date and time values directly is not recommended as time zone and other conversions could cause confusing results. Either use the **Value** function to convert date/time values to milliseconds first and take into account the app user's time zone, or use the [**DateAdd**](function-dateadd-datediff.md) and [**DateDiff**](function-dateadd-datediff.md) functions to add or subtract from one of these values.

## Option sets and Two options

Option sets and two-option data types provide a two or more choices for an end user to select. For example, an **Order Status** option set might offer the choices **New**, **Shipped**, **Invoiced**, and **Closed**. The two-option type offers only two choices.

Both of these data types show their labels in a text-string context. For example, a label control shows one of the order-status options if the control's **Text** property is set to a formula that references that option set. Option labels might be localized for app users in different locations.

When an app user selects an option and saves that change, the app transmits the data to the database, which stores that data in a representation that's independent of language. An option in an option set is transmitted and stored as a number, and an option in a two-option type is transmitted and stored as a Boolean.

The labels are for display purposes only. You can't perform direct comparisons with the labels because they're specific to a language. Instead, each option set has an enumeration that works with the underlying number or Boolean. For example, you can't use this formula:

`If( ThisItem.OrderStatus = "Active", ...`

But you can use this formula:

`If( ThisItem.OrderStatus = OrderStatus.Active, ...`

For global option sets (which entities share), the name of the option-set enumeration matches the name of the global option set. For local option sets (which are scoped to an entity), the name might contain the name of the entity. This behavior avoids conflicts if another entity has an option set that has the same name. For example, the **Accounts** entity might have an **OrderStatus** option set, and it's name might be **OrderStatus (Accounts)**. That name contains one or more spaces and parentheses, so you must surround it with single quotation marks if you reference it in a formula.

In addition, two-option values can also behave as Boolean values. For example, a two-option value named **TaxStatus** might have the labels **Taxable** and **Non-Taxable**, which correspond to *true* and *false* respectively. To demonstrate, you can use this formula:

`If( ThisItem.Taxable = TaxStatus.Taxable, ...`

You can also use this equivalent formula:

`If( ThisItem.Taxable, ...`