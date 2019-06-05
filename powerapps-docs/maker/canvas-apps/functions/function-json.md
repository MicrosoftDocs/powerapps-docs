---
title: JSON function | Microsoft Docs
description: Reference information, including syntax, for the JSON function in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/02/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# JSON function in PowerApps
Generates a JSON text string for a table, record, or value.

## Description
The **JSON** function returns the JSON (JavaScript Object Notation) representation of a data structure as a text string, suitable for transmitting across a network or storing.  The format is described by [ECMA-404](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf) and [IETF RFC 8259](https://tools.ietf.org/html/rfc8259) and is widely used with JavaScript and other programming languages.

The data structure can consist of primitive values and records or tables that can be arbitrarily nested.  The following [canvas data types](data-types.md) are supported: 

| Data Type | Description | Result example |
|-----------|-------------|---------| 
| **Boolean** | *true* or *false*. | `true` |
| **Color** | String containing the 8-digit hexadecimal representation for the color in the format "#rrggbbaa" with *rr* is the red component, *gg* is green, *bb* is blue, and *aa* is the alpha channel where *00* is fully transparent and *ff* is fully opaque. The string can be passed to the [**ColorValue** function](function-colors.md).  | `"#102030ff"` |
| **Currency, Number** | Number using a dot decimal separator that is independent of the user's language.  Scientific notation is used if needed. | `1.345` |
| **Date** | String containing the date in ISO 8601 **yyyy-mm-dd** format. | `"2019-03-31"` |
| **DateTime** | String containing an ISO 8601 date/time. Date/time values are time zone agnostic and will be saved with a "Z" indicating UTC.  | `"2019-03-31T22:32:06.822Z"`  |
| **GUID** | String containing the GUID value.  Alphabetic characters will be lowercase. | `"751b58ac-380e-4a04-a925-9f375995cc40"`
| **Image, Media** | If **IncludeBinaryData** is specified, media files are encoded in a string.  Web references using the http: and https: URL schemes are not modified.  References to in memory binary data, such as captured with the [**Camera**](../controls/control-camera.md) control and any other references with the appres: and blob: URL schemes will be encoded with the ["data:*mimetype*;base64,..."](https://en.wikipedia.org/wiki/Data_URI_scheme) format. | `"data:image/jpeg;base64,/9j/4AA..."` |
| **Number** | Number using a dot decimal separator that is independent of the user's language.  Scientific notation is used if needed. | `1.345` |
| **Option&nbsp;set** | The numeric value of the option set, not the label used for display. The numeric value is used because it is language independent.  | `1001` |
| **Time** | String containing an ISO 8601 **HH:mm:ss.fff** format.  | `"23:12:49.000"` |
| **Record** | **{** and **}** are wrapped around the comma delimited list of fields and their values.  This is similar to canvas app record notation except that the name is always quoted.  Records that are based on a Many-to-One relationship are not supported.  | `{ "First Name": "Fred", "Age": 21 }` |
| **Table** | **[** and **]** are wrapped around the comma delimited list of records.  Tables that are based on a a One-to-Many relationship are not supported.  | `[ { "First Name": "Fred", "Age": 21 }, { "First Name": "Jean", "Age": 20 } ]` |
| **Two&nbsp;option** | The Boolean value of the two option, *true* or *false*, not the label used for display.  The Boolean value is used because it is language independent. | `false` |
| **Hyperlink, Text** | Double quoted string.  Embedded double quote characters are escaped with a backslash, newlines are replaced with "\n", and other standard JavaScript replacements. | `"This is a string."` | 

Use the optional *Format* argument to control the readability of the result and how some data types are handled.  By default, the output is as compact as possible for transmission across a network with no unnecessary spaces or newlines and unsupported data types and binary data are not allowed.  Multiple formats can be combined with the **&** operator.

| JSONFormat Enum | Description |
|-----------------|-------------|
| **Compact** | Default.  The output will be as compact as possible with no added spaces or newlines. | 
| **IndentFour** | To improve readability, the output will add a newline for each column and nesting level and use four space characters for each indentation level. |
| **IncludeBinaryData** | Images, videos, and audio clips columns are included in the result.  Including binary data can dramatically increase the size of the result and impact performance of your app.  Care should be taken with using this setting as the result can be very large and degrade the performance of your app.    |
| **IgnoreBinaryData** | Images, videos, and audio clips columns are not included in the result. Without either **IncludeBinaryData** or **IgnoreBinaryData** the function will produce an error if it encounters binary data. |
| **IgnoreUnsupportedTYpes** | Unsupported data types are allowed but will not be included in the result.  By default unsupported data types produce an error. |  

Use the [**ShowColumns** and **DropColumns** functions](function-table-shaping.md) to control what data is included in the result and to avoid unsupported data types.

Because **JSON** can be both memory and compute intensive, this function can only be used in [behavior functions](../working-with-formulas-in-depth.md).   You can capture the result from **JSON** into a [variable](../working-with-variables.md) which can then be used in data flow. 

For columns that have both a display name and a logical name, the logical name will be used in the result.  Display names are dependent on the language of the app user and are therefore inappropriate for data transfers to a common service.

## Syntax
**JSON**( *DataStructure* [, *Format* ] )

* *DataStructure* – Required. The data structure to be converted to JSON.  Tables, records, and primitive values are supported, arbitrarily nested.
* *Format* - Optional.  **JSONFormat** enum value.  Default is **Compact** with no extra newlines or spaces and binary data columns are disallowed.

## Examples

### Hierarchical data
1. Insert a [**Button**](../controls/control-button.md) control and set its **OnSelect** property to this formula.

    ```powerapps-dot
    ClearCollect( CityPopulations,
        { City: "London",    Country: "United Kingdom", Population: 8615000 }, 
        { City: "Berlin",    Country: "Germany",        Population: 3562000 }, 
        { City: "Madrid",    Country: "Spain",          Population: 3165000 }, 
        { City: "Hamburg",   Country: "Germany",        Population: 1760000 }, 
        { City: "Barcelona", Country: "Spain",          Population: 1602000 }, 
        { City: "Munich",    Country: "Germany",        Population: 1494000 } 
    );
    ClearCollect( CitiesByCountry, GroupBy( CityPopulations, "Country", "Cities" ) )
    ```

2. Press the button.  This results in this data structure in the **CitiesByCountry** collection.

    ![](media/function-json/cities-grouped.png)

1. Insert a second **Button** control and set its **OnSeletct** property to this formula:

    ```powerapps-dot
    Set( CitiesByCountryJSON, JSON( CitiesByCountry ) )
    ```

1. Press the button.  This results in the JSON representation for **CitiesByCountry** to be places in the global variable **CitiesByCountryJSON**.

1. Insert a [**Label**](../controls/control-text-box.md) control and set its **Text** property to.

    ```powerapps-dot
    CitiesByCountryJSON
    ```

    You'll see the following result, all on a single line with no spaces, suitable for transmission across a network:

    ```json
    [{"Cities":[{"City":"London","Population":8615000}],"Country":"United Kingdom"},{"Cities":[{"City":"Berlin","Population":3562000},{"City":"Hamburg","Population":1760000},{"City":"Munich","Population":1494000}],"Country":"Germany"},{"Cities":[{"City":"Madrid","Population":3165000},{"City":"Barcelona","Population":1602000}],"Country":"Spain"}]
    ```

1. Change the second button's formula to make the output more readable.

    ```powerapps-dot
    JSON( CitiesByCountry, JSONIndent.IndentFour )
    ```

1. Press the second button again.  The label control will now show the more readable.

    ```json
    [
        {
            "Cities": [
                {
                    "City": "London",
                    "Population": 8615000
                }
            ],
            "Country": "United Kingdom"
        },
        {
            "Cities": [
                {
                    "City": "Berlin",
                    "Population": 3562000
                },
                {
                    "City": "Hamburg",
                    "Population": 1760000
                },
                {
                    "City": "Munich",
                    "Population": 1494000
                }
            ],
            "Country": "Germany"
        },
        {
            "Cities": [
                {
                    "City": "Madrid",
                    "Population": 3165000
                },
                {
                    "City": "Barcelona",
                    "Population": 1602000
                }
            ],
            "Country": "Spain"
        }
    ]
    ```

### Images and media in base64

1. Add an [**Image** control](../controls/control-image.md) to a screen.

    This control brings with it **SampleImage**.

2. Add a [**Button** control](../controls/control-button.md) and set its **OnSelect** property to the formula.

    ```powrapps-dot
    Set( ImageJSON, JSON( SampleImage, JSONFormat.IncludeBinaryData ) )
    ```

1.  Press the button.

1. Add a [**Label** control] and set its **Text** property to the formula.

    ```powerapps-dot
    ImageJSON
    ```

1. Resize the control and reduce the font size as needed to see most of the result.  You will see the text string that was captured from calling the **JSON** function.

    ```json
    "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxzdmcgdmVyc2lvbj0iMS4xIg0KCSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bWxuczphPSJodHRwOi8vbnMuYWRvYmUuY29tL0Fkb2JlU1ZHVmlld2VyRXh0ZW5zaW9ucy8zLjAvIg0KCSB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjI3MHB4IiBoZWlnaHQ9IjI3MHB4IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCAyNzAgMjcwIiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCgk8ZyBjbGFzcz0ic3QwIj4NCgkJPHJlY3QgeT0iMC43IiBmaWxsPSIjRTlFOUU5IiB3aWR0aD0iMjY5IiBoZWlnaHQ9IjI2OS4zIi8+DQoJCTxwb2x5Z29uIGZpbGw9IiNDQkNCQ0EiIHBvaW50cz0iMjc3LjksMTg3LjEgMjQ1LDE0My40IDE4OC42LDIwMi44IDc1LDgwLjUgLTQuMSwxNjUuMyAtNC4xLDI3MiAyNzcuOSwyNzIiLz4NCgkJPGVsbGlwc2UgZmlsbD0iI0NCQ0JDQSIgY3g9IjIwMi40IiBjeT0iODQuMSIgcng9IjI0LjQiIHJ5PSIyNC4zIi8+DQoJPC9nPg0KPC9zdmc+"
    ```
