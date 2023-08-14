---
title: Create a table row using the Web API
description: Learn how to use the Web API to send a POST request to create a table row in Microsoft Dataverse.
ms.date: 07/22/2023
ms.service: powerapps
ms.topic: how-to
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Create a table row using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Use a `POST` request to send data to create a table row (entity record). You can create multiple related table rows in a single operation using *deep insert*. You also need to know how to set values to associate a new table row to existing tables using the `@odata.bind` annotation.  

> [!NOTE]
> For information about how to create and update the table (entity) definitions using the Web API, see [Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md).

<a name="bkmk_basicCreate"></a>

## Basic create

 This example creates an new account entity record. `accounts` is the entity set name for the [account EntityType](xref:Microsoft.Dynamics.CRM.account). The response `OData-EntityId` header contains the URI of the created entity.

 **Request:**

```http

POST [Organization URI]/api/data/v9.0/accounts
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
    "name": "Sample Account",
    "creditonhold": false,
    "address1_latitude": 47.639583,
    "description": "This is the description of the sample account",
    "revenue": 5000000,
    "accountcategorycode": 1
}
```

 **Response:**

```http

HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.0/accounts(7eb682f1-ca75-e511-80d4-00155d2a68d1)

```

To create an record you must identify the valid [entity set name](web-api-service-documents.md#entity-set-name), property names, and types. For all system tables and attributes (table columns), you can find this information in the article for that entity in the [Web API Entity Type Reference](xref:Microsoft.Dynamics.CRM.EntityTypeIndex). For custom tables or columns, refer to the definition of that table in the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document). More information: [Web API EntityTypes](web-api-entitytypes.md)

<a name="bkmk_createWithDataReturned"></a>

## Create with data returned

You can compose your `POST` request so that data from the created record is returned with a status of `201 (Created)`. To get this result, you must use the `return=representation` preference in the request headers.

To control which properties are returned, append the `$select` query option to the URL to the entity set. You may also use `$expand` to return related entities.

Nested `$expand` on collection-valued navigation properties will not return data when used with the `return=representation` preference. More information: [Nested $expand on collection-valued navigation properties](query-data-web-api.md#nested-expand-on-collection-valued-navigation-properties)

When an entity is created in this way, the `OData-EntityId` header containing the URI to the created record isn't returned.

This example creates a new account entity and returns the requested data in the response.

**Request:**

 ```http

POST [Organization URI]/api/data/v9.0/accounts?$select=name,creditonhold,address1_latitude,description,revenue,accountcategorycode,createdon
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Content-Type: application/json; charset=utf-8
Prefer: return=representation

{
    "name": "Sample Account",
    "creditonhold": false,
    "address1_latitude": 47.639583,
    "description": "This is the description of the sample account",
    "revenue": 5000000
}

```

**Response:**

```http

HTTP/1.1 201 Created
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: return=representation
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts/$entity",
    "@odata.etag": "W/\"536530\"",
    "accountid": "d6f193fc-ce85-e611-80d8-00155d2a68de",
    "accountcategorycode": 1,
    "description": "This is the description of the sample account",
    "address1_latitude": 47.63958,
    "creditonhold": false,
    "name": "Sample Account",
    "createdon": "2016-09-28T22:57:53Z",
    "revenue": 5000000.0000,
    "_transactioncurrencyid_value": "048dddaa-6f7f-e611-80d3-00155db5e0b6"
}

```

## Create multiple records in a single request

The fastest way to create multiple records of the same type in a single request is to use the [CreateMultiple action](xref:Microsoft.Dynamics.CRM.CreateMultiple). At the time of this writing the [CreateMultiple action](xref:Microsoft.Dynamics.CRM.CreateMultiple) is a preview feature. Not all standard tables support this action, but all elastic tables do.

More information:

- [Bulk Operation messages (preview)](../bulk-operations.md)
- [Sample: Web API Use CreateMultiple and UpdateMultiple (preview)](samples/create-update-multiple.md)
- [Use CreateMultiple with elastic tables](../use-elastic-tables.md#use-createmultiple-with-elastic-tables)

<a name="bkmk_CreateRelated"></a>

## Create related table rows in one operation

 You can create entities related to each other by defining them as navigation properties values. This pattern is known as *deep insert*. This approach has two advantages. It's more efficient, because it replaces replacing multiple simpler creation and association operations with one combined *atomic* operation. An atomic operation succeeds or fails entirely.

 As with a basic create, the response `OData-EntityId` header contains the URI of the created entity. The URIs for the related entities created aren't returned. You can get the primary key values of the records if you use the `Prefer: return=representation` header so it returns the values of the created record. More information: [Create with data returned](#create-with-data-returned)

 For example, the following request body posted to the `accounts` entity set creates a total of four records in the context of creating an account.

- A contact is created because it's defined as an object property of the single-valued navigation property `primarycontactid`.

- An opportunity is created because it's defined as an object in an array that's set to the value of a collection-valued navigation property `opportunity_customer_accounts`.

- A task is created because it's defined an object in an array that's set to the value of a collection-valued navigation property `Opportunity_Tasks`.

> [!NOTE]
> When you create a new table row, you can't insert a non-primary image at the same time. For a non-primary image to be added, the row must already exist.

**Request:**

```http
POST [Organization URI]/api/data/v9.0/accounts
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
 "name": "Sample Account",
 "primarycontactid":
 {
     "firstname": "John",
     "lastname": "Smith"
 },
 "opportunity_customer_accounts":
 [
  {
      "name": "Opportunity associated to Sample Account",
      "Opportunity_Tasks":
      [
       { "subject": "Task associated to opportunity" }
      ]
  }
 ]
}

```

**Response:**

 ```http

HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.0/accounts(3c6e4b5f-86f6-e411-80dd-00155d2a68cb)

```

<a name="bkmk_associateOnCreate"></a>

## Associate table rows on create

 To associate new records with existing records when they're created, use the `@odata.bind` annotation to set the value of navigation properties.

 The following request body posted to the `accounts` entity set creates an account associated with an existing contact with the `contactid` value of `00000000-0000-0000-0000-000000000001` and two existing tasks with `activityid` values of `00000000-0000-0000-0000-000000000002` and `00000000-0000-0000-0000-000000000003`.

This request is using the `Prefer: return=representation` header so it returns the values of the created record. More information: [Create with data returned](#create-with-data-returned)

**Request:**

```http

POST [Organization URI]/api/data/v9.0/accounts?$select=name&$expand=primarycontactid($select=fullname),Account_Tasks($select=subject)
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Prefer: return=representation

{
    "name": "Sample Account",
    "primarycontactid@odata.bind": "/contacts(00000000-0000-0000-0000-000000000001)",
    "Account_Tasks@odata.bind": [
        "/tasks(00000000-0000-0000-0000-000000000002)",
        "/tasks(00000000-0000-0000-0000-000000000003)"
    ]
}

```

**Response:**

```http

HTTP/1.1 201 Created
OData-Version: 4.0
Preference-Applied: return=representation

{
    "@odata.context": "[Organization URI]/api/data/v9.1/$metadata#accounts(name,primarycontactid(fullname),Account_Tasks(subject))/$entity",
    "@odata.etag": "W/\"36236432\"",
    "name": "Sample Account",
    "accountid": "00000000-0000-0000-0000-000000000004",
    "primarycontactid": {
        "@odata.etag": "W/\"28877094\"",
        "fullname": "Yvonne McKay (sample)",
        "contactid": "00000000-0000-0000-0000-000000000001"
    },
    "Account_Tasks": [
        {
            "@odata.etag": "W/\"36236437\"",
            "subject": "Task 1",
            "activityid": "00000000-0000-0000-0000-000000000002"
        },
        {
            "@odata.etag": "W/\"36236440\"",
            "subject": "Task 2",
            "activityid": "00000000-0000-0000-0000-000000000003"
        }
    ]
}

```



<a name="bkmk_SuppressDuplicateDetection"></a>

## Check for duplicate records

By default, duplicate detection is suppressed when you're creating records using the Web API. To enable duplicate detection, include the `MSCRM.SuppressDuplicateDetection: false` header with your POST request to enable duplicate detection. Duplicate detection only applies when the following conditions are true:

- The organization has enabled duplicate detection.
- The entity is enabled for duplicate detection.
- Active duplicate detection rules are applied.

More information:

- [Detect duplicate data using code](../detect-duplicate-data-with-code.md)
- [Detect duplicate data using Web API](manage-duplicate-detection-create-update.md#bkmk_create)

<a name="bkmk_initializefrom"></a>

## Create a record from another record

Use the [InitializeFrom function](xref:Microsoft.Dynamics.CRM.InitializeFrom) to create a record in the context of an existing record where  the relationship between the tables is mapped. For information about creating these mappings, see:

- [Map table columns](../../../maker/data-platform/map-entity-fields.md)
- [Customize table and column mappings](../customize-entity-attribute-mappings.md)

To determine whether two entities can be mapped, use the following query:

`GET [Organization URI]/api/data/v9.1/entitymaps?$select=sourceentityname,targetentityname&$orderby=sourceentityname`

Creating a new record from another record is a two-step process. First, use the `InitializeFrom` function to return property values mapped from the original record. Then, combine the response data returned in the `InitializeFrom` function with any changes you want to make and then `POST` the data to create the record.

The following example shows how to create an account record using the values of an existing account record with `accountid` value equal to `00000000-0000-0000-0000-000000000001`.

### Step 1: Get the data with InitializeFrom

**Request:**

```http
GET [Organization URI]/api/data/v9.0/InitializeFrom(EntityMoniker=@p1,TargetEntityName=@p2,TargetFieldType=@p3)?@p1={'@odata.id':'accounts(00000000-0000-0000-0000-000000000001)'}&@p2='account'&@p3=Microsoft.Dynamics.CRM.TargetFieldType'ValidForCreate'
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
```

**Response:**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts/$entity",
    "@odata.type": "#Microsoft.Dynamics.CRM.account",
    "parentaccountid@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)",
    "transactioncurrencyid@odata.bind": "transactioncurrencies(732e87e1-1d96-e711-80e4-00155db75426)",
    "address1_line1": "123 Maple St.",
    "address1_city": "Seattle",
    "address1_country": "United States of America"
}
```

### Step 2: Create the new record

The response received from `InitializeFrom` function consists of values of mapped columns between the source table and target table and the GUID of the parent record. The column mapping between tables that have a relationship is different for different tables and is customizable, so the response from `InitializeFrom` function request may vary for different organizations.



Other property values can also be set and/or modified for the new record by adding them in the JSON request body, as shown in the following example:

```http
POST [Organization URI]/api/data/v9.0/accounts
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

    {
        "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts/$entity",
        "@odata.type": "#Microsoft.Dynamics.CRM.account",
        "parentaccountid@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)",
        "transactioncurrencyid@odata.bind": "transactioncurrencies(732e87e1-1d96-e711-80e4-00155db75426)",
        "name":"Contoso Ltd",
        "numberofemployees":"200",
        "address1_line1":"100 Maple St.",
        "address1_city":"Seattle",
        "address1_country":"United States of America",
        "fax":"73737"
    }
}
```

## Create documents in storage partitions

If you're creating large numbers of records for elastic tables, you can create the entities in storage partitions to speed up access to those entity records.

More information: [Create a record in an elastic table](../use-elastic-tables.md#create-a-record-in-an-elastic-table)

### See also

[Web API basic operations sample (C#)](samples/webapiservice-basic-operations.md)   
[Web API basic operations sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)   
[InitializeFrom function](xref:Microsoft.Dynamics.CRM.InitializeFrom)   
[Perform operations using the Web API](perform-operations-web-api.md)   
[Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md)   
[Query data using the Web API](query-data-web-api.md)   
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)   
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)   
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)   
[Use Web API functions](use-web-api-functions.md)   
[Use Web API actions](use-web-api-actions.md)   
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)   
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)   
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)   

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
