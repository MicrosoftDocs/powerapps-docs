---
title: Retrieve a table row using the Web API
description: "Compose a GET request to retrieve a table row using the Dataverse Web API. See examples for selecting properties, alternate keys, and navigation properties."
ms.topic: how-to
ms.date: 03/12/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---

# Retrieve a table row using the Web API

Use a `GET` request to retrieve data for a record specified as the resource with a unique identifier. When you retrieve a table row (entity record), you can also request specific properties and expand navigation properties to return properties from related records in different tables.  

> [!NOTE]
> For information about retrieving table definitions, see [Query table definitions using the Web API](query-metadata-web-api.md).

<a name="bkmk_basicRetrieve"></a>

## Basic retrieve

The following example returns data for an account entity record with the primary key value equal to 00000000-0000-0000-0000-000000000001:

```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)
```

This example returns all the properties for the account record, which isn't a performance best practice. Always use the `$select` system query option to limit the properties returned while retrieving data. This practice is especially important when you retrieve multiple rows of data. For more information, see [Query Data using the Web API](query/overview.md).

<a name="bkmk_requestProperties"></a>

## Retrieve specific properties

To limit the properties returned when you retrieve data with a GET request, use the `$select` system query option with a comma-separated list of property names. Request only the properties you need for better performance. If you don't specify properties to return, the request returns all properties.

The following example retrieves the `name` and `revenue` properties for the account entity with the primary key value equal to `00000000-0000-0000-0000-000000000001`:

**Request:**
```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)?$select=name,revenue HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
"@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,revenue)/$entity",  
"@odata.etag": "W/\"502186\"",  
"name": "A. Datum Corporation (sample)",  
"revenue": 10000,  
"accountid": "00000000-0000-0000-0000-000000000001",  
"_transactioncurrencyid_value":"b2a6b689-9a39-e611-80d2-00155db44581"  
}

```

When you request certain types of properties, you see more read-only properties returned automatically.

If you request a money value, the `_transactioncurrencyid_value` [lookup property](query/select-columns.md#lookup-property-data) is returned. This property contains only the GUID value of the transaction currency, so you can use it to retrieve information about the currency by using the [transactioncurrency EntityType](xref:Microsoft.Dynamics.CRM.transactioncurrency). Alternatively, you can get more data in the same request by requesting annotations.

If you request a property that's part of a composite attribute for an address, you get the composite property, too. For example, if your query requests the `address1_line1` property for a contact, the `address1_composite` property is also returned.

<a name="BKMK_UsingAltKeys"></a>

## Retrieve record using an alternate key

If an entity has an alternate key defined, you can use it instead of the unique identifier to retrieve, update, or delete the entity. By default, no alternate keys are configured for entities. Alternate keys are available only if your organization or a solution adds them.

Alternate key values with the following characters `/`,`<`,`>`,`*`,`%`,`&`,`:`,`\\`,`?`,`+` aren't currently supported.

For example, if the `Contact` entity has an alternate key definition that includes both the `firstname` and `emailaddress1` properties, you can retrieve the contact using a query with data provided for those keys:

```http
GET [Organization URI]/api/data/v9.2/contacts(firstname='Joe',emailaddress1='abc@example.com')
```

If the alternate key definition contains a lookup type field (for example, the `primarycontactid` property for the `account` entity), you can retrieve the `account` using the [Lookup properties](web-api-properties.md#lookup-properties), as in the following example:

```http
GET [Organization URI]/api/data/v9.2/accounts(_primarycontactid_value=00000000-0000-0000-0000-000000000001)
```

<a name="bkmk_retrieveSingleValue"></a>

## Retrieve records in storage partitions

When you [retrieve a record in an elastic table](../use-elastic-tables.md#retrieve-a-record-in-elastic-table) that's stored in a partition, be sure to specify the partition key.

## Retrieve a single property value

When you only need to retrieve the value of a single property, append the name of the property to the entity URI. Reducing the amount of data returned is a performance best practice.

The following example returns only the value of the `name` property for an `account` entity:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)/name HTTP/1.1
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
"@odata.context":"[Organization URI]/api/data/v9.2/$metadata#accounts(00000000-0000-0000-0000-000000000001)/name",
"value":"Adventure Works (sample)"
}
```

### Retrieve the raw value of a property

To retrieve the raw value of a primitive property instead of JSON, append `/$value` to the URL. For example:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)/name/$value HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```
**Response:**

 ```http
HTTP/1.1 200 OK
Content-Type: text/plain
OData-Version: 4.0

Adventure Works (sample)
```

Using the raw value isn't common unless you're working with file or image data. For more information, see [Download a file in a single request using the Web API](../file-column-data.md#download-a-file-in-a-single-request-using-web-api).

<a name="bkmk_retrieveNavigationPropertyValues"></a>

## Retrieve navigation property values

You can access the values of navigation properties, or lookup fields, by appending the name of the navigation property to the URI of an individual entity.

The following example returns the `fullname` of the primary `contact` of an `account` by using the `primarycontactid` single-valued navigation property:

**Request:**

 ```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)/primarycontactid?$select=fullname HTTP/1.1
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
"@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname)/$entity",  
"@odata.etag": "W/\"500128\"",  
"fullname": "Rene Valdes (sample)",  
"contactid": "ff390c24-9c72-e511-80d4-00155d2a68d1"  
}
```

For collection-valued navigation properties, you can request to return only references to the related entities or just a count of the related entities.

The following example returns references to tasks related to a specific account by adding `/$ref` to the request.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)/AccountTasks/$ref HTTP/1.1
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Collection($ref)",
    "value":
  [
    { "@odata.id": "[Organization URI]/api/data/v9.2/tasks(6b5941dd-d175-e511-80d4-00155d2a68d1)" },
    { "@odata.id": "[Organization URI]/api/data/v9.2/tasks(fcbb60ed-d175-e511-80d4-00155d2a68d1)" }
  ]
}
```

The following example returns the number of tasks related to a specific account by using the `Account_Tasks` collection-valued navigation property with `/$count` appended: 

 **Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)/Account_Tasks/$count HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
```

**Response:**

```http
ï»¿2
```

> [!NOTE]
> The value returned includes the UTF-8 byte order mark (BOM) characters (`ï»¿`), which indicates that this value is a UTF-8 document.

<a name="bkmk_expandRelated"></a>

## Retrieve related records by expanding navigation properties

Use the `$expand` system query option to control what data from related entities is returned. For more information, see [Join Tables](query/join-tables.md).

<a name="bkmk_DetectIfChanged"></a>

## Detect if a record changed since it was retrieved

As a performance best practice, request only the data you need. If you previously retrieved an entity record, use the *ETag* associated with that record to perform conditional retrievals. For more information, see [Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged).

<a name="bkmk_formattedValues"></a>

## Retrieve formatted values

Request [formatted values](query/select-columns.md#formatted-values) for individual record retrievals the same way you query entity sets.

### See also

[Perform operations using the Web API](perform-operations-web-api.md)   
[Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md)   
[Query data using the Web API](query/overview.md)   

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
