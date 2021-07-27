---
title: "Data type format conversions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about File columns that store file data within the application, supporting columns, retrieving data, and uploading file data." # 115-145 characters including spaces. This abstract displays in the search result.
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

Microsoft Dataverse has several [data types](/powerapps/maker/data-platform/types-of-fields) that can be configured with different formats. You can specify the format of the column of your wish using either the Power Apps Maker portal or by API operations. The next several sections will provide additional details about data type formats, including:

- Formats for Text, Numbers, and DateTime

- Format columns

- Conversion between formats within a data type

- Format validations

## Supported formats by data type

The format column specifies the UI on how to display the content. Some formats available in the UI are Phone, Email, or Duration. Suppose you have experimented with these formats before. In that case, you know that the formats applied do not perform any validation on context, domains, or any other values. They instruct the UI which control to use for that type.

### Formats

The following table provides information about the formats available for each data type, a brief description, and if users can select the format.

| **Data Type**         | **Format name**    | **Description**            | **Available to Maker?** | **Notes**       |
|-----------------------|--------------------|----------------------------|-------------------------|-----------------|
| Text                  | Text               | Basic text column that contains text characters.  | Yes   | Default format value for the string column.  |
|                       | TextArea           | Text column that allows basic formatting like line breaks.   | Yes |      |
|                       | Email              | Instructs to use their email control when selected.    | Yes |   |
|                       | URL                | Instructs to use their URL/web control when selected    | Yes  |       |
|                       | TickerSymbol       | Instructs to use their control to retrieve stock market details when selected. | Yes     |   |
|                       | Phone              | Instructs to use their phone control when selected.  | Yes |         |
|                       | JSON               | Stores JSON content that can be used within apps, flows.   | Yes (API only)   | Only in non-SQL stores like Audit |
|                       | RichText           | Allows rich text formatting, including HTML markup.   | Yes (API only) |   |
|                       | VersionNumber      | Stores the version number for rows.   | No  | System use only  |
|                       | Text               | Basic text column.  | Yes   |        |
| Multiline Text (Memo) | TextArea           | Text column that allows basic formatting like line breaks. | Yes | |
|                       | Email          | For internal use only.   | No  |  |
|                       | JSON              | Stores JSON content which can be used within apps, flows.    | Yes (API Only) | Only in non-SQL stores like Log |
|                       | RichText           | Allows for rich text formatting, including HTML markup.   | Y (API Only)  |      |
|                       | InternalExtentData | For internal use only.   | No                       | System use only  |
|                       | None/string.Empty  | Integer value.      | Yes                       | Default format value for Integer column. |
| Integer               | Duration           | Integer value to show the duration of time.    | Yes   | System reads this value in seconds. |
|                       | Timezone           | Integer value that corresponds to a specific time zone using ISO standard values.  | Yes |     |
|                       | Language           | Integer value that corresponds to a specific language using ISO standard values. | Yes   |  |
|                       | Locale             | Integer value that corresponds to a specific locale using ISO standard values.   | Yes (API Only)  | Not shown in Power Apps Maker UI. |
|                       | Date               |Date only. Includes a time of 00:00:00 if the USer Local or Time zone independent is selected.|Yes||
|Date and Time               |DateTime            |Date and time format.| Yes| Default format value for DateTime column.|

## Format conversion

You can change the format of the data type to any of the compatible formats for that type. Changing the format retains your previous table definitions (maxsize) if they exist in the new target format. If an inbound payload does not include a format, Dataverse assumes the format shouldn't be changed. You can convert the format by an API call with the desired payload in the `FormatName` column. Do not change the value in `Format` column as any newly added `Format` selections are ignored.

>  ![NOTE] 
>  At this time, format conversions are only done by API operations. 

Conversions will not change any data present in the column. Due to this, you may notice some unexpected formatting issues that need to be resolved after the change.

As indicated in the table above, there are some restrictions for conversions:

- JSON can only be used if a table is part of non-SQL storage (i.e., Log)

- You cannot convert columns with the formats of `emailbody`, `internalextentdata` to other formats. Any conversion for these is ignored and no error message is provided.

- You cannot convert a column to the formats of `emailbody`, `internalextentdata` to other formats. If attempted, an error will occur.

- Date only cannot be converted to DateTime, but Date with a behavior of User Local or Time Zone independent can be changed to DateTime.

If you change the data type to an incompatible format, the following error is displayed:

The format \<\<formatname\>\> is not valid for the \<\<datatype\>\> type column \<\<columnname\>\> of table \<\<tablename\>\>. For example, the format datetime is not valid for the text type column “Record Title” of table “Case Records”

OData API

> ![NOTE]
> This is only an example to show where these values may appear. This is not meant to be pasted in to replace existing code.

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


[Format and FormatName columns](format-and-formatname-attributes.md)

[Format Validations](format-validations.md)