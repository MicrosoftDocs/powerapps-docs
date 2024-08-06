---
title: Select columns using OData
description: Learn how to use OData to select columns when you retrieve data from Microsoft Dataverse Web API.
ms.date: 07/11/2024
author: MicroSri
ms.author: sriknair
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Select columns using OData

> [!IMPORTANT]
> When you query data, it's important to limit the amount of data returned to optimize performance. Only select the columns with data that you need.

Use the `$select` [query option](overview.md#odata-query-options) to choose which columns to return with your query. In OData, every column is represented as a [*property*](../web-api-properties.md). If you don't include a `$select` query option, all properties are returned.

The following example requests the `name` and `revenue` properties from the first row of the `accounts` EntitySet resource:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue&$top=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,revenue)",
    "value": [
        {
            "@odata.etag": "W/\"81052965\"",
            "name": "Litware, Inc. (sample)",
            "revenue": 20000.0000,
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "accountid": "4624eff7-53d3-ed11-a7c7-000d3a993550"
        }
    ]
}
```

The primary key property is always returned so you don't need to include it in your `$select`. In this example, `accountid` is the primary key.

Other property values may also be included in the response. In this case, the `_transactioncurrencyid_value` [lookup property](../web-api-properties.md#lookup-properties) for the related [Currency (TransactionCurrency)  table/entity reference](../../reference/entities/transactioncurrency.md) is included because `revenue` is a currency property.

### Which properties are available?

All the available properties for an entity are found in the [$metadata service document](../web-api-service-documents.md#csdl-metadata-document). More information: [Web API Properties](../web-api-properties.md)

The entity types included with Dataverse are described in the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex>.

> [!TIP]
> The easiest way to quickly discover which properties are available is to send a request using the `$top` query option with a value of `1` without using `$select`.

### Formatted values

Formatted values are string values generated on the server that you can use in your application. Formatted values include:

- The localized labels for choice, choices, yes/no, status, and status reason columns
- The primary name value for lookup and owner properties
- Currency values with currency symbols
- Formatted date values in the user's time zone

To include formatted values in your results, use the [Prefer request header](https://www.rfc-editor.org/rfc/rfc7240) to send the [odata.include-annotations preference](http://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793628)

```
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

Formatted values are one of several annotations you can request. Use `Prefer: odata.include-annotations="*"` to include all annotations. More information: [Request annotations](../compose-http-requests-handle-errors.md#request-annotations)

The formatted value is returned with the record with an annotation that follows this convention:

```
<property name>@OData.Community.Display.V1.FormattedValue
```

For example:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue,_primarycontactid_value,customertypecode,modifiedon
&$top=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

The following table describes the values and formatted values that are returned for the requested properties.

|Property|Value|Formatted value|
|---------|---------|---------|
|`name`|`Litware, Inc. (sample)`|None|
|`revenue`|`20000.0000`|`$20,000.00`|
|`_primarycontactid_value`|`70bf4d48-34cb-ed11-b596-0022481d68cd`|`Susanna Stubberod (sample)`|
|`customertypecode`|`1`|`Competitor`|
|`modifiedon`|`2023-04-07T21:59:01Z`|`4/7/2023 2:59 PM`|
|`_transactioncurrencyid_value`|`228f42f8-e646-e111-8eb7-78e7d162ced1`|`US Dollar`|
|`accountid`|`78914942-34cb-ed11-b596-0022481d68cd`|None|

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,revenue)",
    "value": [
{
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "revenue@OData.Community.Display.V1.FormattedValue": "$20,000.00",
            "revenue": 20000.0000,
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "customertypecode@OData.Community.Display.V1.FormattedValue": "Competitor",
            "customertypecode": 1,
            "modifiedon@OData.Community.Display.V1.FormattedValue": "4/7/2023 2:59 PM",
            "modifiedon": "2023-04-07T21:59:01Z",
            "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

### Lookup property data

When a [lookup property](../web-api-properties.md#lookup-properties) represents a multi-table, or polymorphic, relationship, you need to request specific annotations to determine which table contains the related data.

For example, many tables have records that users or teams may own. Ownership data is stored in a lookup column named `ownerid`. This column is a single-valued navigation property in OData. You could use `$expand` to create a join to get this value, but you can't use `$select`. However, you can use `$select` to get the corresponding `_ownerid_value` lookup property.

When you include the `_ownerid_value` lookup property with your `$select`, it returns a GUID value. This value doesn't tell you whether the owner of the record is a user or a team. You need to request annotations to get this data.

To include these annotations in your results, use the [Prefer request header](https://www.rfc-editor.org/rfc/rfc7240) to send the [odata.include-annotations preference](http://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793628) with these settings:

```
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"
```

> [!TIP]
> Or you can use `Prefer: odata.include-annotations="*"` to include all annotations. More information: [Request annotations](../compose-http-requests-handle-errors.md#request-annotations)


**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,_ownerid_value&$top=2
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"
```

The following response returns two different account records. The `_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname` annotation tells you that a `team` owns the first one, and a `systemuser` owns the second one.

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_ownerid_value)",
    "value": [
        {
            "@odata.etag": "W/\"81550512\"",
            "name": "Adventure Works (sample)",
            "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
            "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "team",
            "_ownerid_value": "39e0dbe4-131b-e111-ba7e-78e7d1620f5e",
            "accountid": "1adef0b8-54d3-ed11-a7c7-000d3a993550"
        },
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
            "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
            "_ownerid_value": "4026be43-6b69-e111-8f65-78e7d1620f5e",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

- `<lookup property name>@Microsoft.Dynamics.CRM.lookuplogicalname` is the logical name of the related table.
- `<lookup property name>@Microsoft.Dynamics.CRM.associatednavigationproperty` is the name of the corresponding single-valued navigation property. You can use `$expand` using this value in another request to get more data from the related record.

### Column aliases

For Web API, [use fetchxml to specify customized aliases for columns](../../fetchxml/select-columns.md?tabs=webapi#column-aliases).

There is currently no way to specify column aliases using Dataverse Web API using OData. OData 4.0 doesn't include the [$compute system query option introduced in OData 4.01](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html#_Toc31361047) that is required to provide this capability.


## Next steps

Learn how to join tables.

> [!div class="nextstepaction"]
> [Join tables](join-tables.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]