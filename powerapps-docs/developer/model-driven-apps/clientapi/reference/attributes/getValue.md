---
title: "getValue (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: acc78a1e-212a-4eef-88c5-8272f9ba3009
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getValue (Client API reference)

Retrieves the data value for an attribute.

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).getValue()`

## Return Value

**Type**: Depends on the type of attaribute. 

| Attribute Type | Return Type| 
|----|-----|
| boolean | [Boolean](https://msdn.microsoft.com/library/t7bkhaz6.aspx) |
| datetime| [Date](https://msdn.microsoft.com/library/cd9w2te4.aspx)<br/> To get the string version of a date using the PowerApps user’s locale preferences, use the [format](https://msdn.microsoft.com/library/bb384009.aspx) and [localeFormat](https://msdn.microsoft.com/library/bb383816.aspx) methods. Other methods will format dates using the operating system locale rather than the user’s PowerApps locale preferences. | 
| decimal| [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)| 
| Double | [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)| 
| integer | [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)|
| lookup | [Array](https://msdn.microsoft.com/library/k4h76zbx.aspx) <br/>An array of lookup objects.<br/><br/>NOTE: Certain lookups allow for multiple records to be associated in a lookup, such as the To: field for an email entity record. Therefore, all lookup data values use an array of lookup objects – even when the lookup attribute does not support more than one record reference to be added. <br/><br/>Each lookup has the following properties:<br/>- *entityType*: String. The name of the entity displayed in the lookup.<br/>- *id*: String: The string representation of the GUID value for the record displayed in the lookup.<br/>- *name*: String: The text representing the record to be displayed in the lookup.|
| memo  | [String](https://msdn.microsoft.com/library/ecczf11c.aspx)  |
| money| [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)  |
| optionset | [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)  |
| string | [String](https://msdn.microsoft.com/library/ecczf11c.aspx) |


### Related topic
[setValue (Client API reference)](setValue.md)
