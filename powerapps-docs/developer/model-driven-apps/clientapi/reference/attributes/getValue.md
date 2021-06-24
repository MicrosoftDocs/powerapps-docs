---
title: "getValue (Client API reference)| MicrosoftDocs"
description: Retrieves the data value for a column.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: acc78a1e-212a-4eef-88c5-8272f9ba3009
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getValue (Client API reference)

Retrieves the data value for a column.

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getValue()`

## Return Value

**Type**: Depends on the type of column. 

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

| Column Type | Return Type| 
|----|-----|
| boolean | [Boolean](https://msdn.microsoft.com/library/t7bkhaz6.aspx) |
| datetime| [Date](https://msdn.microsoft.com/library/cd9w2te4.aspx)<br/> To get the string version of a date using the Power Apps user’s locale preferences, use the [format](/previous-versions/bb384009(v=vs.140)) and [localeFormat](/previous-versions/bb383816(v=vs.140)) methods. Other methods will format dates using the operating system locale rather than the user’s Power Apps locale preferences. | 
| decimal| [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)| 
| Double | [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)| 
| integer | [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)|
| lookup | [Array](https://msdn.microsoft.com/library/k4h76zbx.aspx) <br/>An array of lookup objects.<br/><br/>NOTE: Certain lookups allow for multiple records to be associated in a lookup, such as the To: column for an email table record. Therefore, all lookup data values use an array of lookup objects – even when the lookup column does not support more than one record reference to be added. <br/><br/>Each lookup has the following properties:<br/>- *entityType*: String. The name of the table displayed in the lookup.<br/>- *id*: String: The string representation of the GUID value for the record displayed in the lookup.<br/>- *name*: String: The text representing the record to be displayed in the lookup.|
| memo  | [String](https://msdn.microsoft.com/library/ecczf11c.aspx)  |
| money| [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)  |
|choices|[Array](https://msdn.microsoft.com/library/k4h76zbx.aspx) <br/> An array of numbers.|
| choice | [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)  |
| string | [String](https://msdn.microsoft.com/library/ecczf11c.aspx) |


### Related topic
[setValue (Client API reference)](setValue.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]