---
title: "Retrieve a table row using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read how to form a GET request using the Microsoft Dataverse Web API to retrieve table data specified as the resource with a unique identifier"
ms.custom: ""
ms.date: 05/03/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: abae4614-9e03-45e7-94fa-9e6e7225ece5
caps.latest.revision: 21
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "ryjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Retrieve a table row using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Use a `GET` request to retrieve data for a table specified as the resource with a unique identifier. When retrieving a table row (entity record) you can also request specific properties and expand navigation properties to return properties from related tables.  

> [!NOTE]
> For information about retrieving table definitions, see [Query table definitions using the Web API](query-metadata-web-api.md).

<a name="bkmk_basicRetrieve"></a>

## Basic retrieve example

This example returns data for an account entity record with the primary key value equal to 00000000-0000-0000-0000-000000000001.

```http
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)
```

To retrieve more than one entity record at a time, see [Basic query example](query-data-web-api.md#bkmk_basicQuery) in the [Query Data using the Web API](query-data-web-api.md) topic.

> [!CAUTION]
> The above example will return all the properties for account record, which is not a performance best practice for retrieving data. This example was just to illustrate how you can do a basic retrieve of an entity record in Microsoft Dataverse. Because all the properties were returned, we haven't included the response information for the request in this example.
>
> As a performance best practice, you must always use the `$select` system query option to limit the properties returned while retrieving data. See the following section, **Retrieve specific properties**, for information about this.
  
<a name="bkmk_requestProperties"></a>

## Retrieve specific properties

Use the `$select` system query option to limit the properties returned by including a comma-separated list of property names. This is an important performance best practice. If properties aren’t specified using `$select`, all properties will be returned.  

The following example retrieves `name` and `revenue` properties  for the account entity with the primary key value equal to 00000000-0000-0000-0000-000000000001

**Request**
```http
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)?$select=name,revenue HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**
```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
"@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts(name,revenue)/$entity",  
"@odata.etag": "W/\"502186\"",  
"name": "A. Datum Corporation (sample)",  
"revenue": 10000,  
"accountid": "00000000-0000-0000-0000-000000000001",  
"_transactioncurrencyid_value":"b2a6b689-9a39-e611-80d2-00155db44581"  
}

```

When you request certain types of properties you can expect additional read-only properties to be returned automatically.

If you request a money value, the `_transactioncurrencyid_value` lookup property will be returned. This property contains only the GUID value of the transaction currency so you could use this value to retrieve information about the currency using the <xref:Microsoft.Dynamics.CRM.transactioncurrency?text=transactioncurrency EntityType />. Alternatively, by requesting annotations you can also get additional data in the same request. More information:[Retrieve data about lookup properties](query-data-web-api.md#bkmk_lookupProperty)  

If you request a property that is part of a composite attribute for an address, you will get the composite property as well. For example, if your query requests the `address1_line1` property for a contact, the `address1_composite` property will be returned as well.

<a name="BKMK_UsingAltKeys"></a>

## Retrieve using an alternate key

If an entity has an alternate key defined, you can also use the alternate key to retrieve the entity instead of the unique identifier for the entity. For example, if the `Contact` entity has an alternate key definition that includes both the `firstname` and `emailaddress1` properties, you can retrieve the contact using a query with data provided for those keys as shown here.

```http
GET [Organization URI]/api/data/v9.0/contacts(firstname='Joe',emailaddress1='abc@example.com')
```

If the alternate key definition contains lookup type field (for example, the `primarycontactid` property for the `account` entity), you can retrieve the `account` using the [lookup property](./web-api-types-operations.md#lookup-properties) as shown here.

```http
GET [Organization URI]/api/data/v9.0/accounts(_primarycontactid_value=00000000-0000-0000-0000-000000000001)
```

Any time you need to uniquely identify an entity to retrieve, update, or delete, you can use alternate keys configured for the entity. By default, there are no alternate keys configured for entities. Alternate keys will only be available if the organization or a solution adds them.

<a name="bkmk_retrieveSingleValue"></a>

## Retrieve documents in storage partitions

If you are retrieving entity data stored in partitions be sure to specify the partition key when retrieving that data.

More information: [Access table data faster using storage partitions](azure-storage-partitioning.md)

## Retrieve a single property value

When you only need to retrieve the value of a single property for an entity, you can append the name of the property to the URI for an entity to return only the value for that property. This is a performance best practice because less data needs to be returned in the response.

This example returns only the value of the `name` property for an `account` entity.

**Request**

```http
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)/name HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```
**Response**

 ```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
"@odata.context":"[Organization URI]/api/data/v9.0/$metadata#accounts(00000000-0000-0000-0000-000000000001)/name",
"value":"Adventure Works (sample)"
}
```

<a name="bkmk_retrieveNavigationPropertyValues"></a>

## Retrieve navigation property values

In the same way that you can retrieve individual property values, you can also access the values of navigation properties (lookup fields) by appending the name of the navigation property to the URI referencing an individual entity.

The following example returns the `fullname` of the primary `contact` of an `account` using the `primarycontactid` single-valued navigation property.  

**Request**

 ```http
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)/primarycontactid?$select=fullname HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```
**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{  
"@odata.context": "[Organization URI]/api/data/v9.0/$metadata#contacts(fullname)/$entity",  
"@odata.etag": "W/\"500128\"",  
"fullname": "Rene Valdes (sample)",  
"contactid": "ff390c24-9c72-e511-80d4-00155d2a68d1"  
}
```

For collection-valued navigation properties you have the option to request to return only references to the related entities or just a count of the related entities.

The following example will just return references to tasks related to a specific account by adding `/$ref` to the request.

**Request**

```http
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)/AccountTasks/$ref HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
  
{
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#Collection($ref)",
    "value":
  [
    { "@odata.id": "[Organization URI]/api/data/v9.0/tasks(6b5941dd-d175-e511-80d4-00155d2a68d1)" },
    { "@odata.id": "[Organization URI]/api/data/v9.0/tasks(fcbb60ed-d175-e511-80d4-00155d2a68d1)" }
  ]
}
```

The following example returns the number of tasks related to a specific account using the `Account_Tasks` collection-valued navigation property with `/$count` appended.  

 **Request**

```http
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)/Account_Tasks/$count HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
```

**Response**

```http
ï»¿2
```

> [!NOTE]
> The value returned includes the UTF-8 byte order mark (BOM) characters (`ï»¿`) that represent that this is a UTF-8 document.

<a name="bkmk_expandRelated"></a>

## Retrieve related tables for a table by expanding navigation properties

Use the `$expand` system query option to control what data from related entities is returned. There are two types of navigation properties:  

- *Single-valued* navigation properties correspond to Lookup attributes that support many-to-one relationships and allow setting a reference to another entity.
- *Collection-valued* navigation properties correspond to one-to-many or many-to-many relationships.  

If you simply include the name of the navigation property, you’ll receive all the properties for related records. You can limit the properties returned for related records using the `$select` system query option in parentheses after the navigation property name. Use this for both single-valued and collection-valued navigation properties.

> [!NOTE]
> To retrieve related entities for entity sets, see [Retrieve related tables by expanding navigation properties](query-data-web-api.md#bkmk_expandRelated).  

- **Retrieve related entities for an entity instance by expanding single-valued navigation properties**: <br />The following example demonstrates how to retrieve the contact for an account entity. For the related contact record, we are only retrieving the contactid and fullname.

  **Request**

  ```http
  GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)?$select=name&$expand=primarycontactid($select=contactid,fullname) HTTP/1.1  
  Accept: application/json  
  OData-MaxVersion: 4.0  
  OData-Version: 4.0  
  ```

  **Response**

  ```http
  HTTP/1.1 200 OK  
  Content-Type: application/json; odata.metadata=minimal  
  OData-Version: 4.0  

  {  
    "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#accounts(name,primarycontactid,primarycontactid(contactid,fullname))/$entity",  
    "@odata.etag":"W/\"550616\"",  
    "name":"Adventure Works (sample)",  
    "accountid":"00000000-0000-0000-0000-000000000001",  
    "primarycontactid":
    {  
    "@odata.etag":"W/\"550626\"",  
    "contactid":"c59648c3-68f7-e511-80d3-00155db53318",  
    "fullname":"Nancy Anderson (sample)"  
    }
  }
  ```

  Instead of returning the related entities for entity records, you can also return references (links) to the related entities by expanding the single-valued navigation property with the `$ref` option. The following example returns links to the contact record for the account entity.  

  **Request**

  ```http
  GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)?$select=name&$expand=primarycontactid/$ref HTTP/1.1  
  Accept: application/json  
  OData-MaxVersion: 4.0  
  OData-Version: 4.0  
  ```

  **Response**

  ```http
  HTTP/1.1 200 OK  
  Content-Type: application/json; odata.metadata=minimal  
  OData-Version: 4.0  
  
  {  
    "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#accounts(name,primarycontactid)/$entity",  
    "@odata.etag":"W/\"550616\"",  
    "name":"Adventure Works (sample)",  
    "accountid":"00000000-0000-0000-0000-000000000001",  
    "_primarycontactid_value":"c59648c3-68f7-e511-80d3-00155db53318",  
    "primarycontactid": { "@odata.id":"[Organization URI]/api/data/v9.0/contacts(c59648c3-68f7-e511-80d3-00155db53318)" }
  }
  ```

- **Retrieve related entities for an entity instance by expanding collection-valued navigation properties**:<br /> The following example demonstrates how you can retrieve all the tasks assigned to an account record.

  **Request**

  ```http
  GET [Organization URI]/api/data/v9.0/accounts(915e89f5-29fc-e511-80d2-00155db07c77)?$select=name
  &$expand=Account_Tasks($select=subject,scheduledstart)
  Accept: application/json
  OData-MaxVersion: 4.0
  OData-Version: 4.0
  ```

  **Response**

  ```http
  HTTP/1.1 200 OK  
  Content-Type: application/json; odata.metadata=minimal  
  OData-Version: 4.0

  {
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts(name,Account_Tasks,Account_Tasks(subject,scheduledstart))/$entity",
    "@odata.etag": "W/\"514069\"",
    "name": "Sample Child Account 1",
    "accountid": "915e89f5-29fc-e511-80d2-00155db07c77",
    "Account_Tasks":
     [
      {
        "@odata.etag": "W/\"514085\"",
        "subject": "Sample Task 1",
        "scheduledstart": "2016-04-11T15:00:00Z",
        "activityid": "a983a612-3ffc-e511-80d2-00155db07c77"
      },
      {
        "@odata.etag": "W/\"514082\"",
        "subject": "Sample Task 2",
        "scheduledstart": "2016-04-13T15:00:00Z",
        "activityid": "7bcc572f-3ffc-e511-80d2-00155db07c77"
      }
     ]
  }
  ```
  
 > [!NOTE]
 > If you expand on collection-valued navigation parameters to retrieve related entities for *entity sets*, a @odata.nextLink property will be returned instead for the related entities. You should use the value of the @odata.nextLink property with a new GET request to return the required data. More information:[Retrieve related tables by expanding navigation properties](query-data-web-api.md#bkmk_expandRelated)

- **Retrieve related entities for an entity instance by expanding both single-valued and collection-valued navigation properties**: The following example demonstrates how you can expand related entities for an entity instance using both single- and collection-values navigation properties.  

  **Request**

  ```http 
  GET [Organization URI]/api/data/v9.0/accounts(99390c24-9c72-e511-80d4-00155d2a68d1)?$select=accountid
  &$expand=parentaccountid($select%20=%20createdon,%20name),Account_Tasks($select%20=%20subject,%20scheduledstart) HTTP/1.1  
  Accept: application/json
  OData-MaxVersion: 4.0
  OData-Version: 4.0
  ```

  **Response**

  ```http
  HTTP/1.1 200 OK  
  Content-Type: application/json; odata.metadata=minimal  
  OData-Version: 4.0  

  {
   "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts(accountid,parentaccountid,Account_Tasks,parentaccountid(createdon,name),Account_Tasks(subject,scheduledstart))/$entity",
   "@odata.etag": "W/\"514069\"",
   "accountid": "915e89f5-29fc-e511-80d2-00155db07c77",
   "parentaccountid": 
      {
        "@odata.etag": "W/\"514074\"",
        "createdon": "2016-04-06T00:29:04Z",
        "name": "Adventure Works (sample)",
        "accountid": "3adbf27c-8efb-e511-80d2-00155db07c77"
      },
    "Account_Tasks":
      [
        {
          "@odata.etag": "W/\"514085\"",
          "subject": "Sample Task 1",
          "scheduledstart": "2016-04-11T15:00:00Z",
          "activityid": "a983a612-3ffc-e511-80d2-00155db07c77"
        },
        {
          "@odata.etag": "W/\"514082\"",
          "subject": "Sample Task 2",
          "scheduledstart": "2016-04-13T15:00:00Z",
          "activityid": "7bcc572f-3ffc-e511-80d2-00155db07c77"
        }
      ]
  }
  ```

> [!NOTE]
> You can’t use the `/$ref` or `/$count` path segments to return only the URI for the related entity or a count of the number of related entities.

<a name="bkmk_optionsOnExpand"></a>

## Options to apply to expanded tables

 You can apply certain system query options on the entities returned for a collection-valued navigation property. Use a semicolon-separated list of system query options enclosed in parentheses after the name of the collection-valued navigation property. You can use `$select`, `$filter`, `$orderby`, `$top`, and `$expand`.

 The following example filters the results of task entities related to an `account` to those with a subject that ends with “1.”

```http
?$expand=Account_Tasks($filter=endswith(subject,'1');$select=subject)  
```

The following example specifies that related tasks should be returned in ascending order based on the `createdon` property.

```http
?$expand=Account_Tasks($orderby=createdon asc;$select=subject,createdon)  
```

 The following example returns only the first related task.

```http
?$expand=Account_Tasks($top=1;$select=subject)
```

 The following example applies nested `$expand` options to return details about the `systemuser` who last modified the account and the name of the `businessunit` that user belongs to.

```http
?$select=name&$expand=modifiedby($select=fullname;$expand=businessunitid($select=name))
```

> [!NOTE]
> - Nested `$expand` options can only be applied to single-valued navigation properties.
>
> - Each request can include a maximum of 10 `$expand` options. There is no limit on the depth of nested `$expand` options, but the limit of 10 total `$expand` options applies to these as well.
>
> - This is a subset of the system query options described in the “11.2.4.2.1 Expand Options” section of [OData Version 4.0 Part 1: Protocol Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html). The options `$skip`, `$count`, `$search`, and `$levels` aren’t supported for the Web API.

More information about nested $expand option use: [Multi-level expand of single-valued navigation properties](retrieve-related-entities-query.md#multi-level-expand-of-single-valued-navigation-properties)

<a name="bkmk_DetectIfChanged"></a>

## Detect if a table has changed since it was retrieved

As a performance best practice you should only request data that you need. If you have previously retrieved an entity record, you can use the *ETag* associated with a previously retrieved record to perform conditional retrievals on that record. More information: [Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged).

<a name="bkmk_formattedValues"></a>

## Retrieve formatted values

Requesting formatted values for individual record retrievals is done the same way as done when querying entity sets. More information: [Include formatted values](query-data-web-api.md#bkmk_includeFormattedValues).

### See also

[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create a table using the Web API](create-entity-web-api.md)<br />
[Update and delete tables using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]