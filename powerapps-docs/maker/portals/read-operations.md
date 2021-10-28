---
title: Portals read operations using the Web API
description: Learn how to create read operations using the portals Web API.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/31/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - tapanm-msft
    - nickdoelman
---

# Query data using portals Web API (preview)

You can use [available Web API operations](web-api-overview.md#web-api-operations) in portals. Web API operations consist of HTTP requests and responses. This article shows sample read operations, methods, URI, and the sample JSON you can use in the HTTP request.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites

- Enable table and field for Web API operations. More information: [Site settings for the Web API](web-api-overview.md#site-settings-for-the-web-api)

- The portals Web API accesses table records and follows the table permissions given to users through the associated web roles. Ensure you configure the correct table permissions. More information: [Create web roles](configure/create-web-roles.md)

## Site setting for Web API read operations

You must configure the site setting **WebAPI/enableReadOperationPreview** and set its value to **True** to enable read operations using portals Web API.

:::image type="content" source="media/read-operations/enable-read.png" alt-text="Enable Web API read operation site setting. " border="true":::

> [!Important]
> This site setting is only required during the preview period.

## Query records

This example queries account records.

| **Operation** | **Method** | **URI** |
|-------------------------|-------------------------|-------------------------|
| Retrieve table records | **GET** | `[Portal URI]/_api/accounts`</br></br>**Example:</br>** `https://contoso.powerappsportals.com/_api/accounts` |

**Sample response**

```json
{
"value": [
    {
    "@odata.etag": "W/\"1066412\"",
    "name": "Fourth Coffee (sample)",
    "accountid": "d2e11ba8-92f6-eb11-94ef-000d3a5aa607"
    },
    {
    "@odata.etag": "W/\"1066413\"",
    "name": "Litware, Inc. (sample)",
    "accountid": "d4e11ba8-92f6-eb11-94ef-000d3a5aa607"
    }
]
}
```

Use **$select** and **$top** system query options to return the name property for the first three accounts:

| **Operation** | **Method** | **URI** |
|-------------------------|-------------------------|-------------------------|
| Retrieve first three entity records | **GET** | `[Portal URI]/_api/accounts?$select=name,revenue&$top=3`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$select=name,revenue&$top=3` |

Retrieve account by using account ID:

| **Operation** | **Method** | **URI** |
|-------------------------|-------------------------|-------------------------|
| Retrieve specific property for a record | **GET** | `[Portal URI]/_api/accounts(e0e11ba8-92f6-eb11-94ef-000d3a5aa607)?$select=name`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts(e0e11ba8-92f6-eb11-94ef-000d3a5aa607)?$select=name` |

**Sample response**

```json
{
    "@odata.etag": "W/\"1066414\"",
    "name": "Adventure Works (sample)",
    "accountid": "d6e11ba8-92f6-eb11-94ef-000d3a5aa607"
}
```

## Apply system query options

Each of the system query options you append to the URL for the entity set is added using the syntax for query strings. The first is appended after \[**?**\] and the following query options are separated using \[**&**\]. All query options are case-sensitive as shown in the following example.

| **Method** | **URI** |
|-------------------------|-------------------------|
| **GET** | `[Portal URI]/_api/accounts?$select=name,revenue&$filter=revenue gt 90000&$top=3`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$select=name,revenue&$filter=revenue gt 90000&$top=3` |

## Request specific properties

Use the **$select** system query option to limit the properties returned as shown in the following example.

| **Method** | **URI** |
|-------------------------|-------------------------|
| **GET** | `[Portal URI]/_api/accounts?$select=name,revenue&$top=3`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$select=name,revenue&$top=3` |

> [!IMPORTANT]
> This is a performance best practice. If properties aren't specified and you have configured the `Webapi/<table name>/fields` site setting value to `*` then all properties will be returned using `$select`. If no properties are specified then an error will be returned.

## Filter results

Use the **$filter** system query option to set criteria for which rows will be returned.

### Standard filter operators

The Web API supports the standard OData filter operators listed in the following table.

| **Operator**             | **Description**       | **Example**                                                              |
|--------------------------|-----------------------|--------------------------------------------------------------------------|
| **Comparison Operators** |                       |                                                                          |
| eq                       | Equal                 | *$filter=revenue eq 100000*                                              |
| ne                       | Not Equal             | *$filter=revenue ne 100000*                                              |
| gt                       | Greater than          | *$filter=revenue gt 100000*                                              |
| ge                       | Greater than or equal | *$filter=revenue ge 100000*                                              |
| lt                       | Less than             | *$filter=revenue lt 100000*                                              |
| le                       | Less than or equal    | *$filter=revenue le 100000*                                              |
| **Logical Operators**    |                       |                                                                          |
| and                      | Logical and           | *$filter=revenue lt 100000 and revenue gt 2000*                          |
| or                       | Logical or            | *$filter=contains(name,'(sample)') or contains(name,'test')*             |
| not                      | Logical negation      | *$filter=not contains(name,'sample')*                                    |
| **Grouping Operators**   |                       |                                                                          |
| ( )                      | Precedence grouping   | *(contains(name,'sample') or contains(name,'test')) and revenue gt 5000* |

### Standard query functions

The Web API supports these standard OData string query functions:

| **Function** | **Example**                         |
|--------------|-------------------------------------|
| contains     | *$filter=contains(name,'(sample)')* |
| endswith     | *$filter=endswith(name,'Inc.')*     |
| startswith   | *$filter=startswith(name,'a')*      |

## Order results

Specify the order in which items are returned using the **$orderby** system query option. Use the **asc** or **desc** suffix to specify ascending or descending order respectively. The default is ascending if the suffix isn't applied. The following example shows retrieving the name and revenue properties of accounts ordered by ascending revenue and by descending name.

| **Method** | **URI** |
|-------------------------|-------------------------|
| **GET** | `[Portal URI]/_api/accounts?$select=name,revenue&$orderby=name asc,revenue desc&$filter=revenue gt 90000`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$select=name,revenue&$orderby=name asc,revenue desc&$filter=revenue gt 90000` |

## Aggregate and grouping results

By using **$apply,** you can aggregate and group your data dynamically as seen in the following examples.

| **Scenarios**                                                | **Example**                                                                                        |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| List of unique statuses in the query                         | *accounts?$apply=groupby((statuscode))*                                                            |
| Aggregate sum of the estimated value                         | *opportunities?$apply=aggregate(estimatedvalue with sum as total)*                                 |
| Average size of the deal based on estimated value and status | *opportunities?$apply=groupby((statuscode),aggregate(estimatedvalue with average as averagevalue)* |
| Sum of estimated value based on status                       | *opportunities?$apply=groupby((statuscode),aggregate(estimatedvalue with sum as total))*           |
| Total opportunity revenue by account name                    | *opportunities?$apply=groupby((parentaccountid/name),aggregate(estimatedvalue with sum as total))* |
| Primary contact names for accounts in 'WA'                   | *accounts?$apply=filter(address1\_stateorprovince eq 'WA')/groupby((primarycontactid/fullname))*   |
| Last created record date and time                            | *accounts?$apply=aggregate(createdon with max as lastCreate)*                                      |
| First created record date and time                           | *accounts?$apply=aggregate(createdon with min as firstCreate)*                                     |

## Retrieve a count of rows

Use the **$count** system query option with a value of true to include a count of entities that match the filter criteria up to 5000.

| **Method** | **URI** |
|-------------------------|-------------------------|
| **GET** | `[Portal URI/_api/accounts?$select=name&$filter=contains(name,'sample')&$count=true`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$select=name&$filter=contains(name,'sample')&$count=true` |

**Sample response**

```json
{
"@odata.count": 10,
"value": [
    {
    "@odata.etag": "W/\"1066412\"",
    "name": "Fourth Coffee (sample)",
    "accountid": "d2e11ba8-92f6-eb11-94ef-000d3a5aa607"
    },
    {
    "@odata.etag": "W/\"1066413\"",
    "name": "Litware, Inc. (sample)",
    "accountid": "d4e11ba8-92f6-eb11-94ef-000d3a5aa607"
    },
    {
    "@odata.etag": "W/\"1066414\"",
    "name": "Adventure Works (sample)",
    "accountid": "d6e11ba8-92f6-eb11-94ef-000d3a5aa607"
    }
]
}
```

If you don't want to return any data except for the count, you can apply **$count** to any collection to get just the value.

| **Method** | **URI** |
|-------------------------|-------------------------|
| **GET** | `[Portal URI/_api/accounts/$count`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts/$count` |

**Sample response**

`3`

## Column comparison

The following example shows how to compare columns using the Web API:

| **Method** | **URI** |
|-------------------------|-------------------------|
| GET | `[Portal URI]/_api/contacts?$select=firstname&$filter=firstname eq lastname`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/contacts?$select=firstname&$filter=firstname eq lastname` |

## Retrieve related table records with a query

Use the **$expand** system query option in the navigation properties to control what data from related entities is returned.

### Retrieve related table records by expanding single-valued navigation properties

The following example shows how to retrieve the contact for all the account records. For the related contact records, we're only retrieving the **contactid** and **fullname**.

| **Method** | **URI** |
|-------------------------|-------------------------|
| GET | `[Portal URI]/_api/accounts?$select=name&$expand=primarycontactid($select=contactid,fullname)`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$select=name&$expand=primarycontactid($select=contactid,fullname)` |

**Sample response**

```json
{
"value": [
    {
    "@odata.etag": "W/\"1066412\"",
    "name": "Fourth Coffee (sample)",
    "accountid": "d2e11ba8-92f6-eb11-94ef-000d3a5aa607",
        "primarycontactid": {
        "contactid": "e6e11ba8-92f6-eb11-94ef-000d3a5aa607",
        "fullname": "Yvonne McKay (sample)"
        }
    },
    {
    "@odata.etag": "W/\"1066413\"",
    "name": "Litware, Inc. (sample)",
    "accountid": "d4e11ba8-92f6-eb11-94ef-000d3a5aa607",
        "primarycontactid": {
        "contactid": "e8e11ba8-92f6-eb11-94ef-000d3a5aa607",
        "fullname": "Susanna Stubberod (sample)"
        }
    }
]
}
```

### Retrieve related tables by expanding collection-valued navigation properties

If you expand on collection-valued navigation parameters to retrieve related entities for entity sets, only one level of depth is returned if there's data. Otherwise, the collection will return an empty array.

| **Method** | **URI** |
|-------------------------|-------------------------|
| **GET** | `[Portal URI]/_api/accounts?$top=5&$select=name&$expand=Account_Tasks($select=subject,scheduledstart)`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$top=5&$select=name&$expand=Account_Tasks($select=subject,scheduledstart)` |

### Retrieve related tables by expanding both single-valued and collection-valued navigation properties

The following example demonstrates how you can expand related entities for entity sets using both single and collection-valued navigation properties.

| **Method** | **URI** |
|-------------------------|-------------------------|
| **GET** | `[Portal URI]/_api/accounts?$top=5&$select=name&$expand=primarycontactid($select=contactid,fullname),Account_Tasks($select=subject,scheduledstart)`</br></br>**Example:**</br>`https://contoso.powerappsportals.com/_api/accounts?$top=5&$select=name&$expand=primarycontactid($select=contactid,fullname),Account_Tasks($select=subject,scheduledstart)` |

## Next Step

[Portals write, update and delete operations using the Web API](write-update-delete-operations.md)

### See also

[Web API overview](web-api-overview.md)</br>
[Tutorial: Use portal Web API](webapi-tutorial.md)</br>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]