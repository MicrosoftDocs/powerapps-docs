---
title: "Improve performance when accessing documents using storage partitions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to improve performance when accessing non-relational documents." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 01/27/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Access documents faster using storage partitions

An optional partition key can be specified to create a logical partition for non-relational documents stored in NoSql tables of Azure heterogenous storage. Having a partition key improves application performance for large sets of data (millions of documents) by grouping data items into logical sets within a table. For example, a table containing products can be grouped logically into product categories to improve retrieval of all items within a product category. The partition key value can be a string or numeric type. Once specified, the partition key value can't be changed.

When no partition key is specified, the table is the logical boundary and retrieving a single item or a set of logically related items from a large data set will not be as performant as when using a partition key.

## Creating and accessing a partition

A unique new partition key value must be used to create a new logical partition. The same value must be used to create additional items in the same logical partition and to retrieve, update, or delete items belonging to the logical partition.

```http
// Create
POST [Organization URI]/api/data/v9.1/new_msdyn_customers?partitionid=<pID>
Content-Type: application/json
{
  "new_firstname": "Hello",
  "new_lastname": "World",
}

// Retrieve
GET [Organization URI]/api/data/v9.1/new_msdyn_customers(<cID>)?partitionid=<pID>
GET [Organization URI]/api/data/v9.1/new_msdyn_customers?partitionId=<ID>

// Update
PATCH [Organization URI]/api/data/v9.1/new_msdyn_customers(<cID>)?partitionid=<pID>
Content-Type: application/json
{
  "new_firstname": "Hello",
  "new_lastname": "World",
}

// Delete
DELETE [Organization URI]/api/data/v9.1/new_msdyn_customers(<cID>)?partitionid=<pID>
```

## Additional information

Here are a few more details about the partition key and partition management.

- The key value must be unique in the environment.
- A partition is limited to 20 GB of data, and there is no method available to check the partition's current size.
- There is no defined limit to the number of partitions you can allocate in an environment.
- Partition allocation is automatic. Specifying a unique partition key during a Create operation creates a partition. When all data has been deleted from the partition, the partition is deleted.
- There is no method available to rename a key.
- Presently, only the Create, Update, Retrieve, and Delete entity operations support storage partitioning.


### See Also

[Create an entity record using the Web API](create-entity-web-api.md)  
[Retrieve an entity record using the Web API](retrieve-entity-using-web-api.md)  
[Update and delete entities using the Web API](update-delete-entities-using-web-api.md)
