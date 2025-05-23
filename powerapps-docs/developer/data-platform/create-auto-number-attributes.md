---
title: "Create autonumber columns (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about creating autonumber column in the same way you create a string column using the StringAttributeMetadata class except that you use the new AutoNumberFormat property. Use the AutoNumberFormat property to define a pattern that includes sequential numbers and random strings by composing placeholders that indicate the length and type of values that are generated."
keywords: "Autonumber columns"
ms.date: 06/15/2022
ms.reviewer: jdaly
ms.topic: how-to
author: mkannapiran
ms.author: kamanick
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Create autonumber columns

With Microsoft Dataverse, you can add an autonumber column for any table. To create autonumber columns in Power Apps, see [Autonumber columns](../../maker/data-platform/autonumber-fields.md).

This article explains how you can programmatically create an autonumber column and set a seed value for sequential elements. In addition, the article shows how to set the sequence number for the next record if you need to reset the seed at any time later.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

> [!NOTE]
>The setting of the seed is optional. There is no need to call the seed if you don't need to reseed.

You can create an autonumber column in the same way you create a string column using the [StringAttributeMetadata Class](xref:Microsoft.Dynamics.CRM.StringAttributeMetadata) except that you use the [AutoNumberFormat Property](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AutoNumberFormat). Use the `AutoNumberFormat` property to define a pattern that includes sequential numbers and random strings by composing placeholders that indicate the length and type of values that are generated. The random strings help you to avoid duplicates or collisions, especially when offline clients trying to create autonumbers.

When you create an autonumber column, the [FormatName Property](xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata.FormatName) or the [Format Property](xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata.Format) values must be `Text`. Since these values are the default values, you'll typically not set this property. You can't create an autonumber column that uses any other special format such as `Email`, `Phone`, `TextArea`, `Url`, or any other [existing formats](xref:Microsoft.Xrm.Sdk.Metadata.StringFormatName).

SQL generates the sequential segment guarantees uniqueness.

> [!NOTE]
>You can modify an existing format text column to be an autonumber format.

In model-driven apps using Unified Interface, controls bound to an autonumber column need to explicitly be set as disabled. If you don't set the initial column value on the form, the value is set only after you save the table. Autonumbering can be applied to column values in views, grids, and so on.

## Examples

The following examples show how to create a new autonumber column named `new_SerialNumber` for a custom table named `new_Widget` that has a value that looks like this: `WID-00001-AB7LSFG-20170913070240` using the Web API and the Dataverse SDK for .NET.

#### [Web API](#tab/webapi)

You can create and update table definitions using the Web API. More information: [Create and update table definitions using the Web API](/powerapps/developer/data-platform/webapi/create-update-entity-definitions-using-web-api).

**Request:**

```http
POST [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='new_widget')/Attributes HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
 "AttributeType": "String",
 "AttributeTypeName": {
  "Value": "StringType"
 },
 "Description": {
  "@odata.type": "Microsoft.Dynamics.CRM.Label",
  "LocalizedLabels": [
   {
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
    "Label": "Serial Number of the widget.",
    "LanguageCode": 1033
   }
  ]
 },
 "DisplayName": {
  "@odata.type": "Microsoft.Dynamics.CRM.Label",
  "LocalizedLabels": [
   {
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
    "Label": "Serial Number",
    "LanguageCode": 1033
   }
  ]
 },
 "RequiredLevel": {
  "Value": "None",
  "CanBeChanged": true,
  "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
 },
 "SchemaName": "new_SerialNumber",
 "AutoNumberFormat": "WID-{SEQNUM:5}-{RANDSTRING:6}-{DATETIMEUTC:yyyyMMddhhmmss}",
 "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
 "FormatName": {
  "Value": "Text"
 },
 "MaxLength": 100
}
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.0/EntityDefinitions(00aa00aa-bb11-cc22-dd33-44ee44ee44ee)/Attributes(11bb11bb-cc22-dd33-ee44-55ff55ff55ff)
```



#### [SDK for .NET](#tab/sdk)

Using the SDK for .NET <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> and <xref:Microsoft.Dynamics.CRM.StringAttributeMetadata> classes:

```csharp
string conn = $@"
    Url = {url};
    AuthType = OAuth;
    UserName = {userName};
    Password = {password};
    AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
    RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
    LoginPrompt=Auto;
    RequireNewInstance = True";

var service = new CrmServiceClient(conn);
// var service = new ServiceClient(conn);

var widgetSerialNumberAttributeRequest = new CreateAttributeRequest
  {
    EntityName = "newWidget",
    Attribute = new StringAttributeMetadata
      {
        //Define the format of the column
        AutoNumberFormat = "WID-{SEQNUM:5}-{RANDSTRING:6}-{DATETIMEUTC:yyyyMMddhhmmss}",
        LogicalName = "new_serialnumber",
        SchemaName = "new_SerialNumber",
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        // The MaxLength defined for the string column must be greater than the length of the 
        // AutoNumberFormat value, that is, it should be able to fit in the generated value.
        MaxLength = 100, 
        DisplayName = new Label("Serial Number", 1033),
        Description = new Label("Serial Number of the widget.", 1033)
      }
  };
  service.Execute(widgetSerialNumberAttributeRequest);
```

---

> [!NOTE]
> Autonumber values are preselected by the database when the record is started. If a record is started but cancelled, the number it was assigned is not used. If, during this time, another record is completed with the next sequential number, gaps will be present in the autonumbering of records.

## AutoNumberFormat options

These examples show how you can configure the [AutoNumberFormat Property](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AutoNumberFormat) to get different results:

|AutoNumberFormat value|Example value|
|:----------|:----------|
|`CAR-{SEQNUM:3}-{RANDSTRING:6}`|`CAR-123-AB7LSF`|
|`CNR-{RANDSTRING:4}-{SEQNUM:4}`|`CNR-WXYZ-1000`|
|`{SEQNUM:6}-#-{RANDSTRING:3}`  |`123456-#-R3V`|
|`KA-{SEQNUM:4}`                |`KA-0001`|
|`{SEQNUM:10}`                  |`1234567890`|
|`QUO-{SEQNUM:3}#{RANDSTRING:3}#{RANDSTRING:5}`|`QUO-123#ABC#PQ2ST`|
|`QUO-{SEQNUM:7}{RANDSTRING:5}` |`QUO-0001000P9G3R`|
|`CAS-{SEQNUM:6}-{RANDSTRING:6}-{DATETIMEUTC:yyyyMMddhhmmss}`|`CAS-002000-S1P0H0-20170913091544`|
|`CAS-{SEQNUM:6}-{DATETIMEUTC:yyyyMMddhh}-{RANDSTRING:6}`|`CAS-002002-2017091309-HTZOUR`|
|`CAS-{SEQNUM:6}-{DATETIMEUTC:yyyyMM}-{RANDSTRING:6}-{DATETIMEUTC:hhmmss}`|`CAS-002000-201709-Z8M2Z6-110901`|

The random string placeholders are optional. You can include more than one random string placeholder. Use any of the format value for datetime placeholders from [Standard date and time format strings](/dotnet/standard/base-types/standard-date-and-time-format-strings).

### String length

The table shows the string length value for the random and sequential placeholders.

|Placeholder|String Length|Output Scenario|
|---------|---------|---------|
|`{RANDSTRING:MIN_LENGTH}`|The value of `MIN_LENGTH` is between 1 and 6.|When you save the row, the autonumber column generates the random string with the defined length if the value is between 1 and 6. If you use the `MIN_LENGTH` value as 7 or beyond 7, you get to see an Invalid Argument error.|
|`{SEQNUM:MIN_LENGTH}`|The minimum value of the `MIN_LENGTH` is 1. The number continues to increment beyond the minimum length.|When you save the row, the autonumber column works fine and continue to work fine for larger values of `MIN_LENGTH`.|

For sequential value placeholders, the `MIN_LENGTH` is a minimum length. If you set the value to be 2, the initial value is 01, and the 100th row value is 100. The number continues to increment beyond the minimum length. The value in setting the length for sequential values is to establish a consistent length for the autogenerated value by adding more 0s to the initial value. It doesn't limit the absolute value. Random value placeholders are always the same length.

Because the sequential values can get larger than the minimum length allotted for them, you shouldn't adjust the [StringAttributeMetadata.MaxLength Property](xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata.MaxLength) to match the length of your formatted value. There's little value in setting this property and it could cause an error in the future if the value exceeds the `MaxLength` value. Make sure you leave enough room for a realistic range of sequential values.

> [!NOTE]
> There is no validation of the placeholder values when you create the column. The error appears only when you try to save a table that uses an incorrectly configured `AutoNumberFormat` value.
> For example, if you specify the length of the random string more than 6, the first person creating a new table  gets an Invalid Argument error when they first try to save the table containing the new autonumber column.

## Update autonumber columns

If you create an autonumber column with an incorrect configuration or you want to modify an existing autonumber column, you can update the column the `AutoNumberFormat` value.

The following code snippet demonstrates how to retrieve, modify, and update the autonumber column using the SDK for .NET:

To modify an existing autonumber column, you must retrieve the column using the [RetrieveAttributeRequest Class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest).

```csharp
// Create the retrieve request
var attributeRequest = new RetrieveAttributeRequest
  {
    EntityLogicalName = entityName.ToLower(),
    LogicalName = "new_serialnumber",
    RetrieveAsIfPublished = true
  };
// Retrieve attribute response
var attributeResponse = (RetrieveAttributeResponse)_serviceProxy.Execute(attributeRequest);
```

After retrieving the autonumber column, you need to modify and update the column.

```csharp
//Modify the retrieved autonumber column
AttributeMetadata retrievedAttributeMetadata = attributeResponse.AttributeMetadata;
//Modify the existing column by writing the format as per your requirement
retrievedAttributeMetadata.AutoNumberFormat = "CAR-{RANDSTRING:5}{SEQNUM:6}";  

// Update the autonumber column            
var updateRequest = new UpdateAttributeRequest
  {
    Attribute = retrievedAttributeMetadata,
    EntityName = "newWidget",
  };
// Execute the request
_serviceProxy.Execute(updateRequest);
```

## Set a seed value

By default, all autonumber sequential values start with 1000 and use 0 as the prefix depending on the length. In this way, the length of the value is always same. If you want to change the initial value, you need to change the initial seed value using the `SetAutoNumberSeed` message to set the next number that is used for the sequential segment.

For example, when the length of the sequential number is 5, you might want to start with an initial value of 10000 instead of the default value of 00001.
If you want to choose a different starting value after creating the autonumbering column, use the `SetAutoNumberSeed` message. Use the [SetAutoNumberSeedRequest class](xref:Microsoft.Crm.Sdk.Messages.SetAutoNumberSeedRequest) when using the SDK assemblies and [SetAutoNumberSeed Action](xref:Microsoft.Dynamics.CRM.SetAutoNumberSeed) when using the Web API.

The `AutoNumberSeed` message has the following parameters:

|Name|Type|Description|
|:----------|:----------|:----------|
|`EntityName`|string|The logical name of the table that contains the column you want to set the seed on.|
|`AttributeName`|string|The logical name of the column you want to set the seed on.|
|`Value`|int|Next autonumber value for the column.|

> [!NOTE]
> Setting the seed only changes the **current number value** for the specified column in the current environment. It does not imply a common **start value** for the column. The seed value is not included in a solution when installed in a different environments. To set the starting number after a solution import, use **SetAutoNumberSeed** message in the target environment.

### SetAutoNumberSeed Examples

The following samples set the seed to 10000 for an autonumber column named `new_SerialNumber` for a custom table named `new_Widget`.

#### [Web API](#tab/webapi)

Using the Web API [SetAutoNumberSeed Action](xref:Microsoft.Dynamics.CRM.SetAutoNumberSeed).

**Request:**

```http
POST [Organization URI]/api/data/v9.0/SetAutoNumberSeed HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
 "EntityName": "new_Widget",
 "AttributeName": "new_Serialnumber",
 "Value": 10000
} 
```

**Response:**

```json
HTTP/1.1 204 No Content
OData-Version: 4.0
```

More information: [Use Web API actions > Unbound actions](webapi/use-web-api-actions.md#unbound-actions)

#### [SDK for .NET](#tab/sdk)

Using the [SetAutoNumberSeedRequest class](xref:Microsoft.Crm.Sdk.Messages.SetAutoNumberSeedRequest):

```csharp

string conn = $@"
    Url = {url};
    AuthType = OAuth;
    UserName = {userName};
    Password = {password};
    AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
    RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
    LoginPrompt=Auto;
    RequireNewInstance = True";

var service = new CrmServiceClient(conn);
// var service = new ServiceClient(conn);

//Define the seed 
SetAutoNumberSeedRequest req = new SetAutoNumberSeedRequest();
req.EntityName = "newWidget";
req.AttributeName = "newSerialnumber";
req.Value = 10000;
service.Execute(req);
```

---
## Community tools

### Auto Number Manager

**[Auto Number Manager](https://www.xrmtoolbox.com/plugins/Rappen.XrmToolBox.AutoNumManager/)** for XrmToolBox is a community driven tool for Dataverse that provides a UI to set, update, and remove autonumber format on new or existing columns.

See the [Developer tools](developer-tools.md) article for community developed tools and [anm.xrmtoolbox.com](https://anm.xrmtoolbox.com) for more information about Auto Number Manager.

> [!NOTE]
> The community tools are not a product of Dataverse and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com). 

### See Also

[Work with table definitions using code](metadata-services.md)<br />
[Customize table definitions](customize-entity-metadata.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
