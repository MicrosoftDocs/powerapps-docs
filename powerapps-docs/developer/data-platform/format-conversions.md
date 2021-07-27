---
title: "Format conversions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about File columns that store file data within the application, supporting columns, retrieving data, and uploading file data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/30/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.topic: "article"
author: "nkrb" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Format conversion

You can change the format of a data type to any of the compatible formats for that type. Changing your format will retain your previous metadata settings (maxsize, etc) if they exist in the new target format. If an inbound payload does not include a format, Dataverse will assume the format is not to be changed. You can convert a format by submitting an API call with the desired payload in the FormatName attribute. Do not change the value in Format as any newly added Format selections will be ignored.

> ![NOTE] 
> At this time, format conversions can only be triggered by API. UI support is coming soon.

Conversions will not change any data that is in the column, due to this, a user may have some unexpected formatting issues to resolve after the change.

As indicated in the table above, there are some restrictions for conversions:

- JSON can only be used if a table is part of non-SQL storage (i.e. Log)

- Users cannot convert columns with the formats of emailbody, internalextentdata to other formats. Any conversion for these will be silently ignored and no error will be provided.

- Users cannot convert a column to the formats of emailbody, internalextentdata to other formats. If attempted an error will occur.

- Date (behavior = DateOnly) cannot be converted to DateTime, but Date with a behavior of User Local or Time Zone Independent can be changed to DateTime.

If a user tries to change a data type to an incompatible format the following error will be displayed:

The format \<\<formatname\>\> is not valid for the \<\<datatype\>\> type column \<\<columnname\>\> of table \<\<tablename\>\>

Example: The format datetime is not valid for the text type column “Record
Title” of table “Case Records”

OData API

NOTE: This is only an example to show where these values may appear. This is not
meant to be pasted in to replace existing code.

To change the format of a data type, you will submit the new format details into
an Odata API PUT call:

API Structure:

```http
POST [Organization
URI]/api/data/v9.0/EntityDefinitions(402fa40f-287c-e511-80d2-00155d2a68d2)/Attributes
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