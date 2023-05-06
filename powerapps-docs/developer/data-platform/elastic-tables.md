---
title: "Use elastic tables (Preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use elastic tables with code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.topic: "article"
ms.date: 04/03/2022
author: pnghub
ms.author: gned
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Use elastic tables (Preview)

Elastic tables are great..

## Using Partitions

An optional partition key can be specified to create a logical partition for non-relational custom entity data stored in NoSql tables of Azure heterogenous storage ([Azure Cosmos DB](/azure/cosmos-db/introduction)). Having a partition key improves application performance for large sets of data (millions of records) by grouping data items into logical sets within a table. For example, a table containing products can be grouped logically into product categories to improve retrieval of all items within a product category. The partition key value can be a string or numeric type. Once specified, the partition key value can't be changed.

When no partition key is specified, the table is the logical boundary and retrieving a single item or a set of logically related items from a large data set will not be as performant as when using a partition key.

A unique new partition key value must be used to create a new logical partition. The same value must be used to create additional items in the same logical partition and to retrieve, update, or delete items belonging to that logical partition.

Here are a few more details about the partition key and partition management:

- The key value must be unique in the environment.
- A partition is limited to 20 GB of data, and there is no method available to check the partition's current size.
- There is no defined limit to the number of partitions you can allocate in an environment.
- Partition allocation is automatic. Specifying a unique partition key during a Create operation creates a partition. When all data has been deleted from the partition, the partition is automatically deleted.
- There is no method available to rename a key.
- Presently, only the Create, Update, Retrieve, and Delete entity operations support storage partitioning.

### Create a record

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK Create sample does

```csharp
public static Guid CreateExample(IOrganizationService service)
{
   var entity = new Entity("new_customer")
   {
         Attributes = {
            { "new_firstname", "Monica" },
            { "new_lastname", "Thompson" },
            // First use of the partition ID value during an entity Create operation
            // also creates the partition where that entity record is stored.
            { "partitionid", "CustomerPartition" }
         }
   };

   return service.Create(entity);
}
```

#### [Web API](#tab/webapi)

Introduce what the Web API Create sample does

**Request**

```http
POST [Organization URI]/api/data/v9.1/new_customers?partitionid="CustomerPartition"
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
{
  "new_firstname": "Monica",
  "new_lastname": "Thompson",
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.0/new_customers(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

---

### Update a record

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK Update sample does

```csharp
public static void UpdateExample(IOrganizationService service, Guid id)
{
   var entity = new Entity("new_customer", id)
   {
         Attributes = {
            { "new_firstname", "Cora" },
            { "partitionid", "CustomerPartition" }
         }
   };

   service.Update(entity);
}
```

#### [Web API](#tab/webapi)

Introduce what the Web API Update sample does

**Request**

```http
PATCH [Organization URI]/api/data/v9.0/new_customers(00000000-0000-0000-0000-000000000001)?partitionid="CustomerPartition"
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-Match: *  
  
{  
    "new_firstname": "Cora"
}
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0
```

---

### Retrieve a record

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK Retrieve sample does

```csharp
public static Entity RetrieveExample(IOrganizationService service, Guid id)
{
   var request = new RetrieveRequest
   {
         ColumnSet = new ColumnSet("new_firstname"),
         Target = new EntityReference("new_customer", id),
         ["partitionId"] = "CustomerPartition"
   };

   var response = (RetrieveResponse)service.Execute(request);
   return response.Entity;
}
```

#### [Web API](#tab/webapi)

Introduce what the Web API Retrieve sample does

**Request**

```http
GET [Organization URI]/api/data/v9.2/new_customers(00000000-0000-0000-0000-000000000001)?partitionId="CustomerPartition"
&$select=new_firstname
Accept: application/json
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
"@odata.context": "[Organization URI]/api/data/v9.2/$metadata#new_customers(new_firstname)/$entity",  
"@odata.etag": "W/\"502186\"",  
"new_firstname": "Cora"
}
```

---

### Query records

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK Query sample does

```csharp
public static EntityCollection RetrieveMultipleExample(IOrganizationService service)
{
   var request = new RetrieveMultipleRequest
   {
         Query = new QueryExpression()
         {
            EntityName = "new_customer",
            ColumnSet = new ColumnSet("new_firstname")
         },
         ["partitionId"] = "CustomerPartition"
   };

   var response = (RetrieveMultipleResponse)service.Execute(request);
   return response.EntityCollection;
}
```

#### [Web API](#tab/webapi)

Introduce what the Web API Query sample does

**Request**

```http
GET [Organization URI]/api/data/v9.2/new_customers?partitionId="CustomerPartition"
&$select=new_firstname
Accept: application/json
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#new_customers(new_firstname)",
    "value": [
        {
            "@odata.etag": "W/\"81052965\"",
            "new_firstname": "Cora"
        }
    ]
}
```

---

### Upsert a record

<!-- TODO: Upsert examples should show using alternate keys -->

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK Upsert sample does

```csharp
public static void UpsertExample(IOrganizationService service, Guid id)
{
   var request = new UpsertRequest
   {
         Target = new Entity("new_customer", id)
         {
            Attributes = {
               { "new_firstname", "Andre" },
               { "new_firstname", "Lawson" },
               { "partitionid", "CustomerPartition" }
            }
         }
   };

   service.Execute(request);
}
```

#### [Web API](#tab/webapi)

Introduce what the Web API Upsert sample does

> [!NOTE]
> Upsert is identical to update except that the `If-Match: *` request header isn't included.

**Request**

```http
PATCH [Organization URI]/api/data/v9.0/new_customers(00000000-0000-0000-0000-000000000001)?partitionid="CustomerPartition"
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
  
{  
    "new_firstname": "Cora"
}
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0
```

---

### Delete a record

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK Delete sample does

```csharp
public static void DeleteExample(IOrganizationService service, Guid id)
{
   var request = new DeleteRequest
   {
         Target = new EntityReference("new_customer", id),
         ["partitionId"] = "CustomerPartition"
   };

   service.Execute(request);
}
```

#### [Web API](#tab/webapi)

Introduce what the Web API Delete sample does

**Request**

```http
DELETE [Organization URI]/api/data/v9.0/new_customers(00000000-0000-0000-0000-000000000001)?partitionId="CustomerPartition"
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0
```

---

## Bulk operations

## Transactional behavior

## Query JSON columns

## Create elastic tables

## Frequently Asked Questions (FAQ)

<!-- 

FAQ should only be used to refer to content that is ALREADY described in the docs.
They should ALWAYS include a link to the section of the docs where the information was provided in context. 

-->

## Tabbed Template

<!-- Copy the following whenever you want to have a sample that is for SDK or Web API -->

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK sample does

```csharp

```

#### [Web API](#tab/webapi)

Introduce what the Web API sample does

**Request**

```http

```

**Response**

```http

```

---

### See Also

[Use optional parameters](optional-parameters.md)<br />
[Partitioning and horizontal scaling in Azure Cosmos DB](/azure/cosmos-db/partitioning-overview)