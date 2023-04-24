---
title: Create and edit elastic tables
description: Learn how to create an elastic Microsoft Dataverse table.
ms.custom: ""
ms.date: 04/24/2023
ms.reviewer: matp
author: Mattp123
ms.topic: how-to
ms.subservice: dataverse-maker
ms.author: matp
---
# Create and edit elastic tables (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

An elastic table is a table managed by the Microsoft Dataverse storage service. Elastic tables come with the same familiar user experience and API as makers and users love with standard tables. They share many aspects and options with standard tables, but they also come with their own unique features and capabilities powered by Azure Cosmos DB.

> [!IMPORTANT]
> This is a preview feature.
> 
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## When to consider elastic tables?

Imagine you have a custom Dataverse table that is used on a regular basis, which imports large numbers of rows, in excess of tens of millions of rows over time. App users work with the table within one or more apps to query and transact on the data. Because elastic tables provide improved query and transact performance over standard or virtual tables for very large datasets, they might be a good choice in this situation.

Elastic tables are designed to handle massive amounts of data in real-time, so you can:

- Import and process data streams quickly and at scale, without impacting other Dataverse traffic. Ingestion rates over 90-M records per hour (25,000/second) have been observed.
- Store and analyze terabytes or even petabytes of data without worrying about scalability, latency, or performance issues.

Elastic tables have unique capabilities.

### Partitioning and scaling

Elastic tables use the Cosmos DB partitioning mechanism to horizontally scale out data across multiple physical servers, allowing for high availability, low latency, and scalability. Partitions are the logical units of data that are distributed across multiple physical servers by Dataverse. Each partition contains a subset of the data stored in the database, and the partition key is used to determine which partition a particular piece of data belongs to. Elastic table scaling involves adding or removing physical servers to accommodate increased or decreased workload demand. Dataverse automatically manages the partitioning and distribution of data across these servers, so you don't need to worry about managing individual servers or partitions yourself.

### Automatic removal of stale data

Time to live (TTL) policies ensure that you're always working with the most up-to-date and accurate information, while optimizing resources and reducing risk. The TTL live value is set in seconds on a record, and it's interpreted as a delta from the time that a record was last modified.

### Flexible schema with JSON columns

Elastic tables enable you to store and query data with varying structures, without the need for pre-defined schemas or migrations. The JSON format is familiar to your web and mobile developers.
  
## Create an elastic table

You create an elastic table just like any other new table in Dataverse.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and select Tables on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **New table** > **New table** on the command bar.
1. On the right properties pane, expand **Advanced options**.
1. Select **Elastic** as the table **Type**.
1. Select the options you want, and then select **Save**. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)

## Considerations when you use elastic tables  

Elastic tables don't provide the same level transaction support as standard tables. Standard tables support strong, consistent transactions support. Elastic tables support what is called *eventual consistency* for transactions, which means that updates made to the database might take some time to propagate to all nodes in the system. This is relevant when you plan to use asynchronous operations, such as Power Automate flows. More information: [Eventual consistency](/azure/cosmos-db/consistency-levels#eventual-consistency).

Elastic tables do support most of the table options supported by standard tables, such as record ownership, change tracking, auditing, mobile offline, Dataverse search and long term data retention.

### Table features not supported

The following table features aren't available for elastic tables.

- Many-to-many, N:N, relationships to standard tables.
- Many-to-one, N:1, relationships when the N table is a standard table (lookup).
- Custom alternate keys. More information: [Work with alternate keys](/power-apps/developer/data-platform/define-alternate-keys-entity)
- Table options: Apply duplication detection rules.

Row options not supported with elastic tables:

- Can have connections
- Can have access team
- Can be added to a queue

Column data types not supported with elastic tables:

- Single line of text
- Choice
- Currency
- File
- Formula
- Whole number format other than None (Duration, Language code, and Time zone)
- Lookup based on the **Customer** option.

## See also

[Create and edit tables using Power Apps](create-edit-entities-portal.md)