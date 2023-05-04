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

An elastic table is a table managed by the Microsoft Dataverse storage service. Elastic tables come with the same familiar user experience and API that are offered with standard tables. They share many aspects and options with standard tables, but come with their own unique features and capabilities that are powered by Azure Cosmos DB.

> [!IMPORTANT]
> This is a preview feature.
> 
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## When to consider elastic tables?

Imagine you have a custom Dataverse table that regularly imports large numbers of rows, in excess of tens of millions of rows. App users work with the table within one or more apps to query and transact on the data. Because elastic tables provide improved query and transact performance over standard or virtual tables for very large datasets, they might be a good choice in this situation.

Elastic tables are designed to handle large volumes of data in real-time. With elastic tables, you can import, store, and analyze large volumes of data without scalability, latency, or performance issues.

Elastic tables have unique capabilities for partitioning and scaling, removal of stale data, and JSON support.

### Automatic removal of stale data

Time to live (TTL) policies ensure that you're always working with the most up-to-date and accurate information, while optimizing resources and reducing risk. The TTL live value is set in seconds on a record, and it's interpreted as a delta from the time that a record was last modified.

### Flexible schema with JSON columns

Elastic tables enable you to store and query data with varying structures, without the need for pre-defined schemas or migrations. The JSON format is familiar to your web and mobile developers.
  
## Considerations when you use elastic tables  

Elastic tables don't provide the same level transaction support as standard tables. Standard tables support strong, consistent transactions support. Elastic tables support what is called *eventual consistency* for transactions, which means that updates made to the database might take some time to propagate to all nodes in the system. This is relevant when you plan to use asynchronous operations, such as Power Automate flows. More information: [Eventual consistency](/azure/cosmos-db/consistency-levels#eventual-consistency).

Elastic tables support many of the table properties supported by standard tables:

- Record ownership, change tracking, auditing, mobile offline, Dataverse search and long term data retention.
- Create, update, delete (CRUD) operations including `XMultiple` (for high throughput), bulk delete, and requests from plugins.
- Relationships:
   - 1:N (One-to-Many)
   - (1) -> ET (N)
   - ET (1) -> Standard (N)
   - N: 1 (Many-to-One)
   - ET (N) -> ET (1)
- Security features:
   - User and organization owned tables
   - Field level security
   - Change tracking triggers (like when a record is created, send email) <!-- you mean change tracking attribute? -->

Additionally, elastic tables, which are powered by Cosmos DB, so queries only support left-outer JOIN. Elastic tables don't support queries that require other JOINS across tables. This means that filters on related tables when creating views or with Advanced Find won't work. We recommend that you denormalize columns from related tables into the main table if filters on related tables are needed. <!-- what does it mean to denormalize columns from related tables into the main table? -->

### Not supported with elastic tables

Table features currently not supported with elastic tables:

- Many-to-many, N:N, relationships to standard tables
- Many-to-one, N:1, relationships when the N table is a standard table (lookup)
- Custom alternate keys
- Duplicate detection rules
- Business rules
- Charts
- Business process flows
- Calculated or rollup columns
- Column comparison <!-- What is this? -->
- Table sharing
- Cascade relationships - Delete/Reparent/Assign/Share/Unshare
- Ordering on lookup columns
- One Dataverse connector for PowerBI
- Table connections
- Access teams
- Queues

Column data types currently not available with elastic tables:

- Single line of text
- Choice
- Currency
- File
- Formula
- Whole number format other than None (Duration, Language code, and Time zone)
- Lookup based on the Customer option.

## Create an elastic table

You create an elastic table just like any other new table in Dataverse.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and select Tables on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **New table** > **New table** on the command bar.
1. On the right properties pane, expand **Advanced options**.
1. Select **Elastic** as the table **Type**.
1. Select the properties you want, and then select **Save**. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)

## See also

[Create and edit tables using Power Apps](create-edit-entities-portal.md)