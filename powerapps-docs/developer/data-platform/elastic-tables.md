---
title: Elastic tables for developers (preview)
description: This article provides information to developers about Dataverse elastic tables and how to use elastic tables using code.
ms.topic: article
ms.date: 08/11/2023
author: pnghub
ms.author: gned
ms.reviewer: jdaly
contributors:
 - sumantb-msft
 - JimDaly
---

# Elastic tables for developers (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Dataverse elastic tables are powered by Azure Cosmos DB. They automatically scale horizontally to handle large amounts of data and high levels of throughput with low latency. Elastic tables are suitable for applications that have unpredictable, spiky, or rapidly growing workloads.

This article focuses on information that developers need to know about using elastic tables. For more information about the capabilities of elastic tables and what is supported, go to [Create and edit elastic tables (preview)](../../maker/data-platform/create-edit-elastic-tables.md).

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## When to use elastic tables

The specific requirements of your data and your application determine whether you should use elastic tables or standard tables.

Use elastic tables in these situations:

- Your data might be unstructured or semi-structured, or your data model might constantly be changing.
- You need horizontal scaling to handle workload growth over time or bursty workload at a given point.
- You must handle a high volume of read and write requests.

Use standard tables in these situations:

- Your application requires strong data consistency.
- Your application requires relational modeling and needs transactional capability across tables or during plug-in execution.
- Your application requires complex joins.

A combination of elastic and standard tables might be appropriate for your data and your application.

For more information about differences in the modeling of elastic tables, go to:

- [Adding columns](create-elastic-tables.md#adding-columns)
- [Alternate keys](create-elastic-tables.md#alternate-keys)
- [Adding relationships](create-elastic-tables.md#adding-relationships)

## Partitioning and horizontal scaling

Elastic tables use Azure Cosmos DB partitioning to scale individual tables to meet the performance requirements of your application. All elastic tables contain a system-defined **Partition Id** string column. This column has the schema name `PartitionId` and the logical name `partitionid`.

Azure Cosmos DB ensures that the rows in a table are divided into distinct subsets, based on the value of the `partitionid` column for each row. These subsets are called [logical partitions](/azure/cosmos-db/partitioning-overview#logical-partitions).

> [!IMPORTANT]
> To get the best performance that is available with elastic tables, you must choose and consistently apply a partitioning strategy. If you don't set a `partitionid` value for each row, the value will remain null, and you won't be able to change it later.
> 
> If you use a custom `partitionid` value, the primary key value doesn't have a unique constraint. In other words, you can create multiple records that have the same primary key but different `partitionid` values. It's important to understand that unique references for elastic tables are a combination of the primary key and the `partitionid` value.

### Choosing a partitionid value

The `partitionid` value that you should use depends on the nature of your data. A logical partition in an elastic table consists of a set of rows that have the same `partitionid` value. For example, in a table that contains data about different products, you can use the product category as the `partitionid` value for the table. In this case, groups of items that have specific values for the product category, such as `Clothing`, `Books`, `Electronic Appliances`, and `Pet supplies`, form distinct logical partitions.

Dataverse transparently and automatically manages logical partitions that are associated with a table. There is no limit on the number of logical partitions that you can have in a table. In addition, there is no risk that a logical partition will be deleted if its underlying rows are deleted.

For all elastic tables, the `partitionid` column should meet these criteria:

- The values in it don't change. After a row is created that has a `partitionid` value, you can't change it.
- It has a high cardinality value. In other words, the property should have a wide range of possible values. Each logical partition can store 20 gigabytes (GB) of data. Therefore, by choosing a `partitionid` value that has a wide range of possible values, you ensure that the table can scale without reaching limits for any specific logical partition.
- It spreads data as evenly as possible among all logical partitions.
- No values are larger than 1,024 bytes.
- No values contain slashes (/), angle brackets (<, \>), asterisks (\*), percent signs (%), ampersands (&), colons (:), backslashes (\\), question marks (?), or plus signs (\+). These characters aren't supported for alternate keys.

If a `partitionid` value isn't specified for a row, Dataverse uses the primary key value as the default `partitionid` value. For write-heavy tables of any size, or for cases where rows are mostly retrieved by using the primary key, the primary key is a great choice for the `partitionid` column.

## Consistency level

Elastic table supports strong consistency during a *logical session*. A logical session is a connection between a client and Dataverse. When a client performs a write operation on an elastic table, it receives a *session token* that uniquely identifies the logical session. To have strong consistency, you must maintain the logical session context by including the session token with all subsequent requests.

Session tokens ensure that all the read operations that are performed during the same logical session context return the most recent write that was made during that logical session. In other words, session tokens ensure that reads always honor the *read-your-writes* and *write-follows-reads* guarantees during a logical session. If a different logical session performs a write operation, other logical sessions might not immediately detect those changes.

The session token is available as an `x-ms-session-token` value in the response of all write operations. To retrieve the most up-to-date row, you must include this value when you retrieve data.

- If you're using the SDK, use the `SessionToken` optional parameter.
- If you're using Web API, use the `MSCRM.SessionToken` request header.

If you retrieve a record without a session token, the recently applied changes might not be applied. Instead, they might be returned in subsequent requests.

[Learn more about using the session token](use-elastic-tables.md#work-with-the-session-token).

## Transactional behavior

Elastic tables don't support multi-record transactions. For a single request execution, multiple write operations that occur during the same synchronous plug-in stage or during different synchronous plug-in stages aren't transactional with each other.

For example, you have a synchronous plug-in step that is registered on the `PostOperation` stage of the `Create` message on an elastic table. In this case, an error that occurs in the plug-in does **not** roll back the record that is created in Dataverse. You should always avoid intentionally canceling any operation by throwing [InvalidPluginExecutionException](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException) in the `PreOperation` or `PostOperation` synchronous stage. If the error is thrown after the `Main` operation, the request returns an error, but the data operation succeeds. Any write operations that are started in the `PreOperation` stage succeed.

However, you should always apply validation rules in a plug-in that is registered for the `PreValidation` synchronous stage. Validation is the purpose of this stage. Even when you use elastic tables, the request returns an error, and the data operation won't begin. [Learn more about the event execution pipeline](event-framework.md#event-execution-pipeline).

Elastic tables also don't support grouping requests in a single database transaction that uses the SDK [ExecuteTransactionRequest class](xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest) or in a Web API `$batch` operation changeset. Currently, these operations succeed but aren't atomic. In the future, an error will be thrown.

To learn more about multi-record transactions, go to:

- [Execute messages in a single database transaction](org-service/use-executetransaction.md)
- [Change sets](webapi/execute-batch-operations-using-web-api.md#change-sets)
- [Known issue: No error is returned when elastic table data operations are grouped in a transaction](#no-error-is-returned-when-elastic-table-data-operations-are-grouped-in-a-transaction)

## Expire data by using Time to live

Dataverse automatically includes a **Time to live** integer column with elastic tables. This column has the schema name `TTLInSeconds` and the logical name `ttlinseconds`.

When a value is set in this column, it defines the amount of time, in seconds, before the row expires and is automatically deleted from database. If no value is set, the record persists indefinitely, just like standard tables.

## Scenario

The examples in related articles use this scenario.

Contoso operates a large number of Internet of Things (IoT) devices that the company has deployed all across the world. Contoso must store and query large amounts of sensor data that is emitted from the IoT devices so that it can monitor their health and gather other insights.

To store and query the large volume of IoT data, Contoso creates an elastic table that is named `contoso_SensorData`. It uses a string column that is named `contoso_DeviceId` as the `partitionid` value for each row that corresponds to a device. Because each `contoso_DeviceId` value is unique to a device, and Contoso performs queries mostly in context of a given `contoso_DeviceId` value, it serves as a good partition strategy for the whole dataset.

Related articles:

- [Create elastic tables using code (preview)](create-elastic-tables.md)
- [Use elastic tables using code (preview)](use-elastic-tables.md)
- [Query JSON columns in elastic tables (preview)](query-json-columns-elastic-tables.md)
- [Elastic table sample code (preview)](elastic-table-samples.md)

## Known issues

The following known issues with elastic tables should be addressed before this feature becomes generally available.

### No error is returned when elastic table data operations are grouped in a transaction

Dataverse doesn't return an error when you group data operations by using the SDK [ExecuteTransactionRequest class](xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest) or a Web API `$batch` operation changeset. Although these data operations are completed, no transaction is applied. Because no transaction can be applied, these operations should fail and return an error.

### No x-ms-session-token value is returned for delete operations

Dataverse doesn't return the `x-ms-session-token` value for delete operations. [Learn more about how this value is used to managed data consistency](#consistency-level).

### The partitionId optional parameter isn't available for all messages

Whenever a record that uses a custom `partitionid` value must be identified, such as for `Retrieve`, `Update`, or `Upsert` operations, you need a way to reference the `partitionid` value. In this case, you can use the alternate key to reference the record. If you prefer, you should also be able to use the `partitionId` optional parameter style. Currently, only `Retrieve` and `Delete` operations support using the `partitionId` optional parameter. [Learn more about using the partitionId parameter](use-elastic-tables.md#using-the-partitionid-parameter).

### Records synchronized with Synapse Link for Dataverse not deleted from data lake when TTL expires

When [time to live (TTL)](#expire-data-by-using-time-to-live) is used on a row, the row will get deleted from the elastic table when TTL has expired. If it's synchronized to a data lake using [Synapse Link for Dataverse ](../../maker/data-platform/export-to-data-lake.md) before TTL expiry, it won't be deleted from the data lake.

## Frequently asked questions

This section will include any frequently asked questions (FAQ). If you have a question that isn't addressed in the documentation, select the **This Page** button in the **Feedback** section at the bottom of the page. You must have a GitHub account to submit questions in this way.

<!-- 

FAQ should only be used to refer to content that is ALREADY described in the docs.
They should ALWAYS include a link to the section of the docs where the information was provided in context. 

-->

## Next steps

> [!div class="nextstepaction"]
> [Create elastic tables using code](create-elastic-tables.md)<br/>

### See also

[Use elastic tables using code (preview)](use-elastic-tables.md)   
[Query JSON columns in elastic tables (preview)](query-json-columns-elastic-tables.md)   
[Bulk operation messages (preview)](bulk-operations.md)   
[Elastic table sample code (preview)](elastic-table-samples.md)   
[Partitioning and horizontal scaling in Azure Cosmos DB](/azure/cosmos-db/partitioning-overview)
