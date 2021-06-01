---
title: "setValue (Client API reference)| MicrosoftDocs"
description: Sets the data value for a column.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1324b465-6012-47d4-bf35-837df82014cb
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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
| boolean| [Boolean](https://msdn.microsoft.com/library/t7bkhaz6.aspx) |
| datetime|[Date](https://msdn.microsoft.com/library/cd9w2te4.aspx) <br/><br/>In Unified Interface, date values are assumed to be UTC.<br/>In the legacy web client, date values are assumed to be in the user's time zone.|
| decimal| [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)|
| double| [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx) |
| Integer|[Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)|
| lookup  | [Array](https://msdn.microsoft.com/library/k4h76zbx.aspx) An array of lookup objects. <br/><br/>Certain lookups, known as ‘partylist’ lookups, allow for multiple records to be associated in a lookup, such as the **To:** column for an email table record. Therefore, all lookup data values use an array of lookup objects – even when the lookup column does not support more than one record reference to be added.<br/><br/>Each lookup has the following properties:<br/>- *entityType*: String. The name of the table displayed in the lookup.<br/>- *id*: String: The string representation of the GUID value for the record displayed in the lookup. The value should match the following format: {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}<br/>- *name*: String: The text representing the record to be displayed in the lookup.|
| memo  | [String](https://msdn.microsoft.com/library/ecczf11c.aspx)  |
| money| [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)  |
| choice | [Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)  |
| string | [String](https://msdn.microsoft.com/library/ecczf11c.aspx)|
| memo | [String](https://msdn.microsoft.com/library/ecczf11c.aspx)|
| money|[Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)|
| choice, choices|[Number](https://msdn.microsoft.com/library/dwab3ed2.aspx)<br/><br/>The [getOptions](getOptions.md) method returns option values as strings. You must use [parseInt](https://msdn.microsoft.com/library/x53yedee.aspx) to convert them to numbers before you can use those values to set the value of an choice column. Valid statuscode (Status Reason) options depend on the current statecode of the record. The statecode (Status) column cannot be set in form scripts. To understand which statecode values are valid, refer to the column definitions. For custom tables use the table definitions browser. Finally, also consider any custom state transitions that have been applied to the column. More information: [Define status reason transitions](/dynamics365/customer-engagement/customize/define-status-reason-transitions).| 
| String| [String](https://msdn.microsoft.com/library/ecczf11c.aspx) <br/><br/> A String column with the email format requires that the string represents a valid email address.|


> [!NOTE]
> Updating a column using **setValue** will not cause the **OnChange** event handlers to run. If you want the **OnChange** event handlers to run you must use [fireOnChange](../attributes/fireOnChange.md) in addition to **setValue**. <br/><br/>
When model-driven apps for tablets is not connected to the server, **setValue** will not work.<br/><br/>You cannot set the value of composite columns. More information: [Write scripts for composite columns](../composite-attributes.md).

### Related topic
[getValue (Client API reference)](getValue.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]