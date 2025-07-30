---
title: "attribute.getValue (Client API reference)"
description: Retrieves the data value for a column.
author: clromano
ms.author: clromano
ms.date: 06/09/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# attribute.getValue (Client API reference)

Retrieves the data value for a column.

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getValue()`

## Return Value

**Type**: Depends on the type of column. The value may be null.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

| Column Type | Return Type| 
|----|-----|
| boolean | [Boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean) |
| datetime| [Date](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date)<br/> To get the string version of a date using the Power Apps user's locale preferences, use the [format](/previous-versions/bb384009(v=vs.140)) and [localeFormat](/previous-versions/bb383816(v=vs.140)) methods. Other methods will format dates using the operating system locale rather than the user's Power Apps locale preferences. | 
| decimal| [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)| 
| Double | [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)| 
| integer | [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)|
| lookup | [Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array) <br/>An array of lookup objects.<br/><br/>NOTE: Certain lookups allow for multiple records to be associated in a lookup, such as the To: column for an email table record. Therefore, all lookup data values use an array of lookup objects – even when the lookup column does not support more than one record reference to be added. <br/><br/>Each lookup has the following properties:<br/>- *entityType*: String. The name of the table displayed in the lookup.<br/>- *id*: String: The string representation of the GUID value for the record displayed in the lookup.<br/>- *name*: String: The text representing the record to be displayed in the lookup.|
| memo  | [String](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)  |
| money| [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)  |
|choices|[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array) <br/> An array of numbers.|
| choice | [Number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)  |
| string | [String](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) |


### Related article

[setValue (Client API reference)](setValue.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
