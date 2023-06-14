---
title: "Elastic tables for developers (preview)"
description: "Provides information to developers about Dataverse elastic tables and how to use elastic tables using code."
ms.topic: article
ms.date: 06/10/2023
author: pnghub
ms.author: gned
ms.reviewer: jdaly
contributors:
 - sumantb-msft
 - JimDaly
---

# Elastic tables (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Dataverse elastic tables are powered by Azure Cosmos DB. They automatically scale horizontally to handle large amounts of data and high levels of throughput with low latency. Elastic tables are suitable for applications with unpredictable, spiky or rapidly growing workloads.

This article focuses on information developers need to know about using elastic tables. For more information about capabilities of elastic tables and what is supported, see [Create and edit elastic tables (preview)](../../maker/data-platform/create-edit-elastic-tables.md)

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## When to use elastic tables

Whether you should use an elastic table depends on the specific needs of your data and your application.

Use elastic tables when:

- Your data may be unstructured or semi-structured, or if your data model may constantly be changing.
- You need horizontal scaling to handle workload growth over time or bursty workload at a given point.
- You need to handle a high volume of read and write requests.

Use standard tables when:

- Your application requires strong data consistency.
- Your application requires relational modeling and needs transactional capability across tables or during plugin execution.
- Your application requires complex joins.

The choice of table should be based on the specific needs of your application. A combination of both types of tables may be appropriate.

For more information about differences in modeling elastic tables, see:

- [Adding Columns](create-elastic-tables.md#adding-columns)
- [Alternate keys](create-elastic-tables.md#alternate-keys)
- [Adding Relationships](create-elastic-tables.md#adding-relationships)


## Partitioning and horizontal scaling

Elastic tables use Azure Cosmos DB partitioning to scale individual tables to meet the performance needs of your application. All elastic tables contain a system-defined **Partition Id** string column with the schema name `PartitionId` and logical name `partitionid`.

Azure Cosmos DB ensures that the rows in a table are divided into distinct subsets called [logical partitions](/azure/cosmos-db/partitioning-overview#logical-partitions) that are formed based on the value of the `partitionid` column of each row.

> [!IMPORTANT]
> To get the optimum performance available with elastic tables, you must choose and consistently apply a partitioning strategy. If you don't set a `partitionid` value for each row, the value will remain null and you will not be able to change it later.
> 
> When you use a custom `partitionid` value, the primary key value doesn't have a unique constraint. In other words, you can create multiple records with the same primary key, but different `partitionid` values. It is important to understand that unique references for elastic tables is the combination of the primary key AND the `partitionid` value.

#### Choosing a PartitionId value

The `partitionid` value you should use depends on the nature of your data.  A logical partition in an elastic table consists of a set of rows that have the same `partitionid`. For example, in a table that contains data about various products, you can use product category as the `partitionid` for the table. Groups of items that have specific values for product category, such as `Clothing`, `Books`, `Electronic Appliances` and `Pet supplies`, form distinct logical partitions.

Dataverse transparently and automatically manages logical partitions associated with a table. There's no limit on the number of logical partitions you can have in a table. You also don't have to worry about deleting a logical partition when the underlying rows belonging to that partition is deleted.

For all elastic tables, the `partitionid` column should:

- Have a value that doesn't change. Once a row is created with a `partitionid` value, you can't change it.
- Have a high cardinality value. In other words, the property should have a wide range of possible values. Each logical partition can store 20 GB of data. So, choosing a `partitionid` with a wide range of possible values ensures that the table can scale without reaching limits for any specific logical partition.
- Spread data as evenly as possible between all logical partitions.
- Have values that are no larger than 1024 bytes.
- Not contain values with the following characters that aren't supported for alternate keys: `/`,`<`,`>`,`*`,`%`,`&`,`:`,`\\`,`?`,`+`.

When `partitionid` isn't specified for a row, Dataverse uses the primary key value as the default `partitionid` value. For write-heavy tables of any size, or for cases where rows are mostly retrieved using the primary key, the primary key is naturally a great choice for the `partitionid` column.

## Consistency level

Elastic table supports strong consistency within a logical session. A logical session is a connection between client and Dataverse. When a client performs a write operation on an elastic table, it receives a *session token* that uniquely identifies this logical session. To have strong consistency, you need to maintain the logical session context. To maintain the logical session context, you must include the session token with all subsequent requests.

With session tokens, all the read operations performed within the same logical session context return the most recent write made within that logical session. In other words, reads are guaranteed to honor the *read-your-writes*, and *write-follows-reads* guarantees within a logical session. If a different logical session performs a write operation, other logical sessions may not see those changes immediately.

Find the session token as a `x-ms-session-token` value in the response of all write operations.  You need to include this value when you retrieve data to retrieve the most up-to-date row.

- With the SDK, use the `SessionToken` optional parameter.
- With Web API, use the `MSCRM.SessionToken` request header

If you retrieve a record without a session token, the changes applied recently may not be applied, but are returned in subsequent requests.

More information: [Work with Session token](use-elastic-tables.md#work-with-session-token)

## Transactional behavior

Elastic tables don't support multi-record transactions. For a single request execution, multiple write operations happening in same or different synchronous plugin stages aren't transactional with each other.

For example, if you have a synchronous plug-in step registered on the `PostOperation` stage of the `Create` message on an elastic table, any error in your plug-in <u>won't</u> roll back the created record in Dataverse. You should always avoid intentionally canceling any operation by throwing a [InvalidPluginExecutionException](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException) in the `PreOperation` or `PostOperation` synchronous stages. If the error is thrown after the `Main` operation, the request will return an error, but the data operation will succeed. If any write operations are started in the `PreOperation` stage, they'll succeed.

However, you should always apply validation rules in a plug-in registered for the `PreValidation` synchronous stage. Validation is the purpose of this stage. Even with elastic tables, the request returns an error and the data operation won't begin. More information: [Event execution pipeline](event-framework.md#event-execution-pipeline)

Elastic tables also don't support grouping requests in a single database transaction using the SDK [ExecuteTransactionRequest](xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest) class or in a Web API `$batch` operation change set. Currently, these operations succeed but aren't atomic. In the future, an error is thrown.  

More information:

- [Execute messages in a single database transaction](org-service/use-executetransaction.md)
- [Change sets](webapi/execute-batch-operations-using-web-api.md#change-sets)
- [Known issue: Error not returned when grouping elastic table data operations in a transaction](#error-not-returned-when-grouping-elastic-table-data-operations-in-a-transaction)


## Expire data with Time to live

Dataverse automatically creates an integer column with the name **Time to live**, schema name `TTLInSeconds` and logical name `ttlinseconds`.

When a value is set to this column, it defines the time in seconds after which the row will expire and be deleted from database automatically. If no value is set, the record persists indefinitely, just like standard tables.

## Scenario

The examples in related articles use this scenario.

Imagine Contoso operates large number of Internet of Things (IoT) devices deployed by the company all across the world. Contoso needs to store and query large amounts of sensor data being emitted from IoT devices so that they can monitor health of device and gathering other insights.

Contoso can create an elastic table named `contoso_SensorData` to store and query large volume of IoT data. It can choose to use a string column named `contoso_DeviceId` as the partitionid value for each row corresponding to that device. Since `contoso_DeviceId` is unique to each device and Contoso performs queries mostly in context of a given `contoso_DeviceId`, it acts as a good partition strategy for entire dataset.


## Known issues

Following are known issues with elastic tables that should be addressed before this feature is generally available.

### Error not returned when grouping elastic table data operations in a transaction

Dataverse doesn't return an error when you group data operations using SDK [ExecuteTransactionRequest](xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest) class or with Web API `$batch` `ChangeSets`. These data operations complete, but no transaction is applied. No transaction can be applied, so this operation should fail and return an error.

### x-ms-session-token value not returned for delete operations

Dataverse doesn't return the `x-ms-session-token` value for delete operations. More information: [Consistency level](#consistency-level)

### partitionId optional parameter not available for all messages

Anytime a record that uses a custom `partitionid` must be identified, such as for `Retrieve`, `Update`, or `Upsert` operations you need a way to reference the `partitionid` value. You can use the alternate key to reference the record. You should also be able to use the `partitionId` optional parameter style if you prefer. At this time, only `Retrieve` and `Delete` operations support using the `partitionId` optional parameter. More information: [Using partitionId parameter](use-elastic-tables.md#using-partitionid-parameter)

## Frequently Asked Questions (FAQ)

This section includes any frequently asked questions. If you have a question that isn't addressed in the documentation, select the **This Page** button in the **Feedback** section at the bottom of the page. You need to have a GitHub account to submit questions this way.

## Next steps

> [!div class="nextstepaction"]
> [Create elastic tables using code](create-elastic-tables.md)<br/>

<!-- 

FAQ should only be used to refer to content that is ALREADY described in the docs.
They should ALWAYS include a link to the section of the docs where the information was provided in context. 

-->

### See Also

[Use elastic tables](use-elastic-tables.md)<br />
[Query JSON columns in elastic tables](query-json-columns-elastic-tables.md)<br />
[Bulk operations with elastic tables](bulk-operations-elastic-tables.md)<br />
[Elastic table sample code (preview)](elastic-table-samples.md)<br />
[Partitioning and horizontal scaling in Azure Cosmos DB](/azure/cosmos-db/partitioning-overview)
