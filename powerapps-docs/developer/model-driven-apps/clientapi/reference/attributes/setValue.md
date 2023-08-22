---
title: "setValue (Client API reference)| MicrosoftDocs"
description: Sets the data value for a column.
author: HemantGaur
ms.author: hemantg
ms.date: 03/14/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setValue (Client API reference)

Sets the data value for a column. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).setValue(value)`

## Parameters

Depends on the type of column.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

| Column Type|Parameters Type|
-------|------|
| boolean| [Boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean) |
| datetime|[Date](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) <br/><br/>In Unified Interface, date values are assumed to be UTC.<br/>In the legacy web client, date values are assumed to be in the user's time zone.|
| decimal| [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)|
| double| [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number) |
| Integer|[Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)|
| lookup  | [Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array) An array of lookup objects. <br/><br/>Certain lookups, known as 'partylist' lookups, allow for multiple records to be associated in a lookup, such as the **To:** column for an email table record. Therefore, all lookup data values use an array of lookup objects – even when the lookup column doesn't support more than one record reference to be added.<br/><br/>Each lookup has the following properties:<br/>- *entityType*: String. The name of the table displayed in the lookup.<br/>- *id*: String: The string representation of the GUID value for the record displayed in the lookup. The value should match the following format: {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}<br/>- *name*: String: The text representing the record to be displayed in the lookup.|
| memo  | [String](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)  |
| money| [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)  |
| choice | [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)  |
| string | [String](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)|
| memo | [String](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)|
| money|[Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)|
| choice, choices|[Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)<br/><br/>The [getOptions](getOptions.md) method returns option values as strings. You must use [parseInt](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseint) to convert them to numbers before you can use those values to set the value of a choice column. Valid statuscode (Status Reason) options depend on the current statecode of the record. The statecode (Status) column can't be set in form scripts. To understand which statecode values are valid, refer to the column definitions. For custom tables, use the table definitions browser. Finally, also consider any custom state transitions that have been applied to the column. More information: [Define status reason transitions for the Case or custom tables](../../../../../maker/data-platform/define-status-reason-transitions.md).| 
| String| [String](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) <br/><br/> A String column with the email format requires that the string represents a valid email address.|


> [!NOTE]
> Updating a column using **setValue** will not cause the **OnChange** event handlers to run. If you want the **OnChange** event handlers to run you must use [fireOnChange](../attributes/fireOnChange.md) in addition to **setValue**.

### Related article

[getValue (Client API reference)](getValue.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
