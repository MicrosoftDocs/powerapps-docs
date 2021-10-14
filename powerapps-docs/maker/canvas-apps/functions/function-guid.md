---
title: GUID function in Power Apps
description: Reference information including syntax and examples for the GUID function in Power Apps.
author: gregli-msft
manager: kvivek

ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 07/17/2020
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# GUID function in Power Apps
Converts a GUID ([Globally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier)) string to a GUID value or creates a new GUID value.

## Description
Use the **GUID** function to convert a string that contains the hexadecimal representation of a GUID into a GUID value that can be passed to a database. GUID values are used as keys by database systems such as Microsoft Dataverse and SQL Server.

The string passed can contain uppercase or lowercase letters, but it must be 32 hexadecimal digits in either of these formats:

- **"123e4567-e89b-12d3-a456-426655440000"** (hyphens in standard locations)
- **"123e4567e89b12d3a456426655440000"** (no hyphens)

If you don't specify an argument, this function creates a new GUID.

To convert a GUID value to a string, simply use it in a string context. The GUID value will be converted to a hexadecimal representation string with hyphens and lowercase letters. 

When generating a new GUID, this function uses pseudo-random numbers to create a version 4 [IETF RFC 4122](https://www.ietf.org/rfc/rfc4122.txt) GUID. When converting a string to a GUID, this function supports any GUID version by accepting any string of 32 hexadecimal digits.

## Volatile functions
**GUID** is a volatile function when used without an argument. Each time the function is evaluated, it returns a different value.  

When used in a data-flow formula, a volatile function will return a different value only if the formula in which it appears is reevaluated. If nothing else changes in the formula, it will have the same value throughout the execution of your app.

For example, a label control for which the **Text** property is set to **GUID()** won't change while your app is active. Only closing and reopening the app will result in a different value.

The function will be reevaluated if it's part of a formula in which something else has changed. If we set the **Text** property of a **Label** control to this formula, for example, a GUID is generated each time the user changes the value of the **Text input** control:

**TextInput1.Text & " " & GUID()**

When used in a [behavior formula](../working-with-formulas-in-depth.md), **GUID** will be evaluated each time the formula is evaluated. For more information, see the examples later in this topic.

## Syntax
**GUID**( [ *GUIDString* ] )

* *GUIDString* – Optional.  A text string that contains the hexadecimal representation of a GUID. If no string is supplied, a new GUID is created.

## Examples

#### Basic usage

To return a GUID value based on the hexadecimal string representation:

```powerapps-dot
GUID( "0f8fad5b-d9cb-469f-a165-70867728950e" )
```

You can also provide the GUID string without hyphens. This formula returns the same GUID value:

```powerapps-dot
GUID( "0f8fad5bd9cb469fa16570867728950e" )
```

Used in context, to set the **Status** field of a new database record to a well-established value:

```powerapps-dot
Patch( Products, Default( Products ), { Status: GUID( "F9168C5E-CEB2-4faa-B6BF-329BF39FA1E4" ) } )
```

You probably don't want to show GUIDs to your users, but GUIDs can help you debug your app. To show the value of the **Status** field in the record that you created in the previous example, set the **Text** property of a **Label** control to this formula:

```powerapps-dot
First( Products ).Status
```

The **Label** control will show **f9168c5e-ceb2-4faa-b6bf-329bf39fa1e4**.

#### Create a table of GUIDs

1. Set the **[OnSelect](../controls/properties-core.md)** property of a **[Button](../controls/control-button.md)** control to this formula:

    ```powerapps-dot
    ClearCollect( NewGUIDs, ForAll( Sequence(5), GUID() ) )
    ```

    This formula creates a single-column table that's used to iterate five times, resulting in five GUIDs.

1. Add a **[Data table](../controls/control-data-table.md)** control, set its **Items** property to **NewGUIDs**, and show the **Value** field.

1. While holding down the Alt key, select the button by clicking or tapping it.

    The data table shows a list of GUIDs:

    ![A screen showing a data table with five different GUID values.](media/function-guid/guid-collection-1.png)

1. Select the button again to show a different list of GUIDs:

    ![The same screen showing a data table with a new set of five different GUID values.](media/function-guid/guid-collection-2.png)

To generate a single GUID instead of a table, use this formula:

```powerapps-dot
Set( NewGUID, GUID() )
```


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]