---
title: "Data type format conversions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about data type format conversions in Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/30/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.topic: "article"
author: "nkrb" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Data type format conversions

Microsoft Dataverse has several [data types](/powerapps/maker/data-platform/types-of-fields) that can be configured with different formats. You can specify the format of the column using either the [solution explorer](/powerapps/maker/data-platform/create-edit-fields)  or by API operations. The following sections provides additional details about data type formats, including:

- [Supported formats by data type](#supported-formats-by-data-type)

- [Format conversions](#format-conversion)

- [Format validations](format-validations.md)

## Supported formats by data type

The format column specifies the UI on how to display the content. Some formats available in the UI are Phone, Email, or Duration. Suppose you have experimented with these formats before. In that case, you know that the formats applied do not perform any validation on context, domains, or any other values. They instruct the UI which control to use for that type.

### Formats

The following table provides information about the formats available for each data type:

| **Data Type**         | **Format name**    | **Description**            | **Available to app maker?** | **Notes**       |
|-----------------------|--------------------|----------------------------|-------------------------|-----------------|
| Text                  | Text               | Basic text column that contains text characters.  | Yes   | Default format value for the text column.  |
|                       | Text Area          | Text column that contains text characters and also allows line breaks.   | Yes |      |
|                       | Email              | The text provides a mailto link to open the user’s email application.    | Yes |   |
|                       | URL                | The text provides a hyperlink to open the page specified. Any text that does not begin with a valid protocol will have “https://” prepended to it.    | Yes  |       |
|                       | Ticker Symbol      | For most languages, the text will be enabled as a link to open the [MSN Money](https://money.msn.com/) website to show details about the stock price represented by the ticker symbol. | Yes     |   |
|                       | Phone              | Columns will be click-enabled to initiate calls.  | Yes |         |
|                       | JSON               | Stores text using JSON formatting   | Yes (API only)   | Only in non-SQL stores like Audit. |
|                       | Rich Text          | Allows rich text formatting, including HTML markup.   | Yes (API only) |   |
|                       | Version Number     | Stores the version number for rows.   | No  | System use only.  |
|                       | Text               | Basic text column that contains text characters.  | Yes   |        |
| Multiline Text (Memo) | Text Area          | Text column that contains text characters and also allows line breaks. | Yes | |
|                       | Email              | For internal use only.   | No  |  |
|                       | JSON               |   Stores text using JSON formatting  | Yes (API Only) | Only in non-SQL stores like Log. |
|                       | RichText           | Allows for rich text formatting, including HTML markup.   | Y (API Only)  |      |
|                       | InternalExtentData | For internal use only.   | No                       | System use only  |
|                       | None/string.Empty  | This option simply displays a number.      | Yes                       | Default format value for whole number column. |
| Whole Number          | Duration           | This format option displays a list of duration options. The data stored in the database is always a number of minutes. The field looks like a drop-down list and provides suggested options like 1 minute, 15 minutes, 30 minutes all the way up to 3 days. People can choose these options or type in a number of minutes and it resolves to that period of time. For example, type in 60 and it resolves to 1 hour. Or they can enter “1 hour” or “2 days” and it will resolve to display that time.
The duration must be entered in the following format: “x minutes”, “x hours” or “x days”. Hours and days can also be entered using decimals, for example, “x.x hours” or “x.x days”.
 <br/> **NOTE**: Values must be expressible in minutes, sub-minute values will be rounded to the nearest minute.    | Yes   | System reads this value in seconds. |
|                       | Timezone           | This option displays a select list of time zones using Time Zone Codes. Each of these zones is stored as a number. For example, for the time zone (GMT-08:00) Pacific Time (US & Canada), the TimeZoneCode is 4. Model driven apps display these codes into time zone names, Canvas apps will display as the number stored.| Yes |     |
|                       | Language           | This option displays a list of the languages provisioned for your organization. The values are stored as a number using LCID codes. Language codes are four-digit or five-digit locale IDs.  Valid locale ID values can be found at [Locale ID (LCID) Chart)](https://docs.microsoft.com/previous-versions/windows/embedded/ms912047(v=winembedded.10)). Model driven apps will display the languages as the language name, Canvas apps will display as the number stored.| Yes   |  |
|                       | Locale             | Value that corresponds to a specific locale using ISO standard values.   | Yes (API Only)  | Not shown in Power Apps Maker UI. |
|  Date and Time        | Date Only          |Date only. Includes a time of 00:00:00 if the **User Local** or **Time-Zone Independent** is selected.|Yes||
|                       |Date and Time       |Date and time format.| Yes| Default format value for DateTime column.|

## Format conversion

You can change the format of the data type to any of the compatible formats that data type supports. Changing the format retains your previous table definitions (maxsize) if they exist in the new target format. If an inbound payload does not include a format, Dataverse assumes the format shouldn't be changed. You can convert the format by an API call with the desired payload in the `FormatName` column. It is recommended not change the value in `Format` column as any newly added `Format` selections are ignored.

> [!NOTE] 
> At this time, format conversions are only done by performing API operations. 

Changing Formats doesn't change any data present in the column. Due to this, you may notice some unexpected formatting issues that need to be resolved after the conversion.

As mentioned in the table above, there are some restrictions for format conversions:

- JSON can only be used if a table is part of non-SQL storage (i.e., Log).

- You cannot convert columns with the formats of type `emailbody`, `internalextentdata` to other formats. Any conversion for these are ignored and no error message is provided.

- You cannot convert a column to the formats of `emailbody`, `internalextentdata` to other formats. If attempted, an error will occur.

- Date only cannot be converted to DateTime, but Date with a behavior of **User Local** or **Time-Zone Independent** can be changed to DateTime.


If you change the data type to an incompatible format, the following error is displayed:

The format \<\<formatname\>\> is not valid for the \<\<datatype\>\> type column \<\<columnname\>\> of table \<\<tablename\>\>. For example, the format datetime is not valid for the text type column.

To change the format of a data type, you need to add the new format details into an OData API **POST** call:

```http
POST [Organization URI]/api/data/v9.0/EntityDefinitions(402fa40f-287c-e511-80d2-00155d2a68d2)/Attributes
HTTP/1.1

Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
{
 "AttributeType": \<\<Data type you are setting the format for\>\>,
 "AttributeTypeName": {
"Value": *\<\<Datatype Type\>\>*
},
"Description": {
"\@odata.type": "Microsoft.Dynamics.CRM.Label",
"LocalizedLabels": [
{
"\@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
"Label": *\<\<text label to use for the format\>\>*
"LanguageCode": 1033
}
]
},
"DisplayName": {
"\@odata.type": "Microsoft.Dynamics.CRM.Label",
"LocalizedLabels": [
{
"\@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
"Label": *\<\<text label to use for the format\>\>*
"LanguageCode": 1033
}
]
},
"RequiredLevel": {
"Value": "None",
"CanBeChanged": true,
"ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
},
"SchemaName": *\<\<Your chosen schema name\>\>*
"\@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
"FormatName": {
"Value": *\<\<Formatname value\>\>*
},
"MaxLength": 100
}
```

### Related articles


[Format and FormatName columns](format-and-formatname-columns.md)

[Format validations](format-validations.md)
