---
title: "Create a table row using the Web API (Microsoft Dataverse) | Microsoft Docs"
description: "Read how to create a POST request to send data to create a table row on Microsoft Dataverse using the Web API"
ms.custom: ""
ms.date: 05/03/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 244259ca-2fbc-4fd4-9a74-6166e6683355
caps.latest.revision: 51
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Create a table row using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Use a POST request to send data to create a table row (entity record). You can create multiple related table rows in a single operation using *deep insert*. You also need to know how to set values to associate a new table row to existing tables using the `@odata.bind` annotation.  

> [!NOTE]
> For information about how to create and update the table (entity) definitions using the Web API, see [Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md).

<a name="bkmk_basicCreate"></a>

## Basic Create

 This example creates a new account entity record. The response `OData-EntityId` header contains the Uri of the created entity.

 **Request**

```http

POST [Organization URI]/api/data/v9.0/accounts HTTP/1.1
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

 **Response**

```http

HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.0/accounts(7eb682f1-ca75-e511-80d4-00155d2a68d1)

```

To create a new entity record you must identify the valid property names and types. For all system entities and attributes (table columns), you can find this information in the topic for that entity in the [About the Table Reference](../reference/about-entity-reference.md). For custom entities or attributes, refer to the definition of that entity in the [CSDL $metadata document](web-api-types-operations.md#csdl-metadata-document). More information: [Entity types](web-api-types-operations.md#entity-types)

<a name="bkmk_createWithDataReturned"></a>

## Create with data returned

You can compose your `POST` request so that data from the created record will be returned with a status of `201 (Created)`.  To get this result, you must use the `return=representation` preference in the request headers.

To control which properties are returned, append the `$select` query option to the URL to the entity set. You may also use `$expand` to return related entities.

When an entity is created in this way the `OData-EntityId` header containing the URI to the created record is not returned.

This example creates a new account entity and returns the requested data in the response.

**Request**

 ```http

POST [Organization URI]/api/data/v9.0/accounts?$select=name,creditonhold,address1_latitude,description,revenue,accountcategorycode,createdon HTTP/1.1
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
    "revenue": 5000000,
    "accountcategorycode": 1
}

```

**Response**

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

<a name="bkmk_CreateRelated"></a>

## Create related table rows in one operation

 You can create entities related to each other by defining them as navigation properties values. This is known as *deep insert*.

 As with a basic create, the response `OData-EntityId` header contains the Uri of the created entity. The URIs for the related entities created aren’t returned. You can get the primary key values of the records if you use the `Prefer: return=representation` header so it returns the values of the created record. More information: [Create with data returned](#create-with-data-returned)

 For example, the following request body posted to the `accounts` entity set will create a total of four new entities in the context of creating an account.

- A contact is created because it is defined as an object property of the single-valued navigation property `primarycontactid`.

- An opportunity is created because it is defined as an object within an array that is set to the value of a collection-valued navigation property `opportunity_customer_accounts`.

- A task is created because it is defined an object within an array that is set to the value of a collection-valued navigation property `Opportunity_Tasks`.

> [!NOTE]
> When creating a new table row, it is not possible to combine the row creation with the insert of a non-primary image. For a non-primary image to be added, the row must already exist.

**Request**

```http
POST [Organization URI]/api/data/v9.0/accounts HTTP/1.1
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

**Response**

 ```http

HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.0/accounts(3c6e4b5f-86f6-e411-80dd-00155d2a68cb)

```

<a name="bkmk_associateOnCreate"></a>

## Associate table rows on create

 To associate new entities to existing entities when they are created you must set the value of navigation properties using the `@odata.bind` annotation.

 The following request body posted to the `accounts` entity set will create a new account associated with an existing contact with the `contactid` value of `00000000-0000-0000-0000-000000000001` and two existing tasks with `activityid` values of `00000000-0000-0000-0000-000000000002` and `00000000-0000-0000-0000-000000000003`.

> [!NOTE]
> This request is using the `Prefer: return=representation` header so it returns the values of the created record. More information: [Create with data returned](#create-with-data-returned)

**Request**

```http

POST [Organization URI]/api/data/v9.0/accounts?$select=name&$expand=primarycontactid($select=fullname),Account_Tasks($select=subject) HTTP/1.1
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

**Response**

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

By default, duplicate detection is suppressed when you are creating records using the Web API. You must include the `MSCRM.SuppressDuplicateDetection: false` header with your POST request to enable duplicate detection. Duplicate detection only applies when 1) the organization has enabled duplicate detection, 2) the entity is enabled for duplicate detection, and 3) there are active duplicate detection rules being applied. More information: [Detect duplicate data using code](../detect-duplicate-data-with-code.md)

See [Detect duplicate data using Web API](manage-duplicate-detection-create-update.md#bkmk_create) for more information on how to check for duplicate records during Create operation.

<a name="bkmk_initializefrom"></a>

## Create a new table row from another table

Use `InitializeFrom` function to create a new record in the context of an existing record where a mapping exists between the entities to which the records belong. 

The following example shows how to create an account record using the attribute values of an existing record of account entity with `accountid` value equal to `c65127ed-2097-e711-80eb-00155db75426`.

**Request**

```http
GET [Organization URI]/api/data/v9.0/InitializeFrom(EntityMoniker=@p1,TargetEntityName=@p2,TargetFieldType=@p3)?@p1={'@odata.id':'accounts(c65127ed-2097-e711-80eb-00155db75426)'}&@p2='account'&@p3=Microsoft.Dynamics.CRM.TargetFieldType'ValidForCreate' HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
```

**Response**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts/$entity",
    "@odata.type": "#Microsoft.Dynamics.CRM.account",
    "parentaccountid@odata.bind": "accounts(c65127ed-2097-e711-80eb-00155db75426)",
    "transactioncurrencyid@odata.bind": "transactioncurrencies(732e87e1-1d96-e711-80e4-00155db75426)",
    "address1_line1": "123 Maple St.",
    "address1_city": "Seattle",
    "address1_country": "United States of America"
}
```

The response received from `InitializeFrom` request consists of values of mapped attributes between the source entity and target entity and the GUID of the parent record. The attribute mapping between entities that have an entity relationship is different for different entity sets and is customizable, so the response from `InitializeFrom` function request may vary for different entities and organizations. When this response is passed in the body of create request of the new record, these attribute values are replicated in the new record. The values of custom mapped attributes also get set in the new record during the process.

> [!NOTE]
> To determine whether two entities can be mapped, use this query:<br />
`GET [Organization URI]/api/data/v9.1/entitymaps?$select=sourceentityname,targetentityname&$orderby=sourceentityname`

Other attribute values can also be set and/or modified for the new record by adding them in the JSON request body, as shown in the example below.

```http
POST [Organization URI]/api/data/v9.0/accounts HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

    {
        "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts/$entity",
        "@odata.type": "#Microsoft.Dynamics.CRM.account",
        "parentaccountid@odata.bind": "accounts(c65127ed-2097-e711-80eb-00155db75426)",
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

If you are creating large numbers of entities that contain documents, you can create the entities in storage partitions to speed up access to those entity records.

More information: [Access documents faster using storage partitions](azure-storage-partitioning.md)

### See also

[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)<br />
<xref href="Microsoft.Dynamics.CRM.InitializeFrom?text=InitializeFrom Function" />  
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Retrieve a table using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete tables using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

