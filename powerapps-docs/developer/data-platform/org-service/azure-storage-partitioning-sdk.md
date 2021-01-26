---
title: "Improve performance when accessing documents using storage partitions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to improve performance when accessing non-relational documents." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 01/25/2021
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
# Improve performance when accessing documents using storage partitions

An optional partition key can be specified to create a logical partition for non-relational documents stored in NoSql tables of Azure heterogenous storage. Having a partition key improves application performance for large sets of data (millions of documents) by grouping data items into logical sets within a table. For example, a table containing products can be grouped logically into product categories to improve retrieval of all items within a product category. The partition key value can be a string or numeric type. Once specified, the partition key value can't be changed.

When no partition key is specified, the table is the logical boundary and retrieving a single item or a set of logically related items from a large data set will not be as performant as when using a partition key.

## Creating and accessing a partition

A unique new partition key value must be used to create a new logical partition. The same value must be used to create additional items in the same logical partition and to retrieve, update, or delete items belonging to the logical partition.

```csharp
public void Run(CrmServiceClient client)
{
    // Create
    Entity entity = new Entity("new_msdyn_customer");
    entity["new_firstname"] = "Hello";
    entity["new_lastname"] = "World";
    entity["partitionid"] = "CategoryPartition"; // First use of the key.
    Guid id = client.Create(entity); // This results in the partition being created.

    // Update
    UpdateRequest updateRequest = new UpdateRequest();
    entity = new Entity("new_msdyn_customer", id);
    entity["new_firstname"] = "NewHello";
    //entity["new_lastname"] = "NewWorld";
    entity["partitionid"] = "CategoryPartition";
    updateRequest.Target = entity;
    var updateResponse = (UpdateResponse)client.Execute(updateRequest);

    // Retrieve
     RetrieveRequest request = new RetrieveRequest();
     request.ColumnSet = new ColumnSet("new_firstname");
     request.Target = new EntityReference("new_msdyn_customer", id);
     request["partitionId"] = "CategoryPartition";
     var response = (RetrieveResponse)client.Execute(request);

     // RetrieveMultiple
     RetrieveMultipleRequest retreiveMultipleRequest = new RetrieveMultipleRequest();
     retreiveMultipleRequest.Query = new QueryExpression()
     {
         EntityName = "new_msdyn_customer",
         ColumnSet = new ColumnSet("new_firstname")
     };
     retreiveMultipleRequest["partitionId"] = "CategoryPartition";
     var retrieveResponse = (RetrieveMultipleResponse)client.Execute(retreiveMultipleRequest);

     // Update
     UpsertRequest upsertRequest = new UpsertRequest();
     entity = new Entity("new_msdyn_customer", id);
     entity["new_firstname"] = "NewHello";
     entity["new_lastname"] = "NewWorld";
     entity["partitionid"] = "CategoryPartition";
     upsertRequest.Target = entity;
     var upsertResponse = (UpsertResponse)client.Execute(upsertRequest);

     // Delete
     DeleteRequest deleteRequest = new DeleteRequest();
     deleteRequest.Target = new EntityReference("new_msdyn_customer", id);
     deleteRequest["partitionId"] = "CategoryPartition";
     var deleteResponse = (DeleteResponse)client.Execute(deleteRequest);
}
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

[Passing optional parameters with a request](use-messages#passing-optional-parameters-with-a-request)  
[Create entities using the Organization Service](entity-operations-create.md)  
[Retrieve an entity using the Organization Service](entity-operations-retrieve.md)  
[Update and Delete entities using the Organization Service](entity-operations-update-delete.md)
