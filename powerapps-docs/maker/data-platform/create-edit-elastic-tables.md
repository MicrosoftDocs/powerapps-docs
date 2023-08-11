---
title: Create and edit elastic tables (preview)
description: Learn how to create an elastic Microsoft Dataverse table.
ms.custom: ""
ms.date: 08/11/2023
ms.reviewer: matp
author: Mattp123
ms.topic: how-to
ms.subservice: dataverse-maker
ms.author: matp
---
# Create and edit elastic tables (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

An elastic table is a table managed by Microsoft Dataverse. Elastic tables come with the same familiar user experience and API that are offered with standard tables. They share many aspects and options with standard tables, but come with their own unique features and capabilities that are powered by Azure Cosmos DB.

As with standard tables, elastic tables are included with your Dataverse database capacity use.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Watch this video that to learn about elastic tables.
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RW15oAi ]

## When to consider Dataverse elastic tables?

Elastic tables are designed to handle large volumes of data in real-time. With elastic tables, you can import, store, and analyze large volumes of data without scalability, latency, or performance issues.

Elastic tables have unique capabilities for flexible schema, horizontal scaling, and automatic removal of data after a time-period.

Elastic tables automatically scale to ingest tens of millions of rows every hour. Background processes can collate the IoT signals, predict maintenance requirements, and proactively schedule technicians.

Consider a scenario where Contoso is a retailer with millions of existing customers. Contoso has a large database of customers and are looking to increase sales while retaining customers. Based on prior customer history, they're looking to have 24-hour flash sale events with different coupons targeting their customers and products. They have estimated that the number of coupons required will be 100 million plus per flash sale campaign. Marketing plans to run multiple 24-hour campaigns targeting different customer segments.  

The requirement for Contoso's marketing application is that it must be able to ingest up to 100 million or more coupon details within a few hours, read millions of coupons per hour, and send coupons to customers.  

Elastic tables will automatically scale for this high throughput scenario.  

For example, in the above scenario, an elastic table named *Coupon* with millions of records can be associated with Dataverse standard tables like *Contact* (customer info) and *Offer* (a custom standard table). Since the elastic tables are isolated from the standard tables, performance for the overall marketing application won't be negatively impacted. In addition, time-to-live capability with elastic table (*Coupon* in this scenario) allows removal of data automatically after fixed periods and ensure optimization of storage capacity.

Use elastic tables when:

- Your data might be unstructured or semi-structured, or if your data model might constantly change.
- You need automatic horizontal scaling.
- You need to handle a high volume of read and write requests.

Use standard tables when:

- Your application requires strong consistency.
- Your application requires relational modeling and needs transactional capability across tables and during plugin execution stages.
- Your application requires complex joins.

The choice of table should be based on the specific needs of your application. A combination of both types of tables may be appropriate.

## Horizontal scaling and performance  

As your business data grows, elastic tables provide unlimited auto scalability based on your application workload, both for storage size and throughput, such as the number of records created, updated, or deleted in a given timeframe.

If your business scenario requires very large volume of data writes, application makers can make use of Dataverse multiple request API's, such as `CreateMultiple`, `UpdateMultiple`, and `DeleteMultiple`, to achieve more throughput within Dataverse throttling limits. More information: [Developer guide: Bulk Operation messages (preview)](../../developer/data-platform/bulk-operations.md)

### Automatic removal of data

Time to live (TTL) policies ensure that you're always working with the most up-to-date and accurate information, while optimizing resources and reducing risk. The TTL live value is set in seconds on a record, and it's interpreted as a delta from the time that a record was last modified.

### Flexible schema with JSON columns

Elastic tables enable you to store and query data with varying structures, without the need for pre-defined schemas or migrations. There's no need to write custom code to map the imported data into a fixed schema. More information: [Developer guide: Query JSON columns in elastic tables (Preview)](../../developer/data-platform/query-json-columns-elastic-tables.md)

## Considerations when you use elastic tables  

Although elastic tables are great for handling large volume of requests at scale, the advantages come with a few trades offs, which should be kept in mind:

- Elastic tables don't support multi-record transactions. This means that multiple write operations happening as part of a single request execution aren't transactional with each other. For example, if you have a synchronous plug-in step registered on the `PostOperation` stage for `Create message` on an elastic table, any error in your plug-in won't roll back the created record in Dataverse. Validations in preplug-ins will still work as expected since they run before the main stage.
- Elastic tables support strong consistency only within a logical session. Outside session context, you might not see changes to a row immediately. More information: [Developer guide: Consistency level](../../developer/data-platform/elastic-tables.md#consistency-level)
- Elastic tables don't support filters on related tables when creating views, advanced find, or any query in general using API. If you frequently need to filter on related table columns, we recommend that you denormalize columns from related tables, which needs filtering into the main table itself. Consider a retailer with two elastic tables: customer and address. One customer has many addresses. You want to return query results for all customers from the customer table whose city value in the address table is New York. In this example, when querying customer table, you want to apply a filter on the city column of the related address table. This isn't supported for elastic tables. One way to make this work is to denormalize the city column into the Customer table so that all customers city values are present in the customer table itself.

## Elastic tables feature support

- Create, retrieve, update, delete (CRUD) operations including API multiple operations (for high throughput), bulk deletion, and requests from plug-ins.
- Relationships: 
   - One-to-many
   - Many-to-one 
- Record ownership, change tracking, auditing, mobile offline, and Dataverse search.

### Security features support

Elastic tables adhere to the Dataverse security model.

When creating an elastic table, you can set:

- Either user or organization owned
- Field level security

### Features currently not supported with elastic tables

Table features currently not supported with elastic tables:

- Business rules
- Charts
- Business process flows
- One Dataverse connector for Power BI
- Many-to-many (N:N) relationships to standard tables
- Many-to-one (N:1) relationships when the N table is a standard table (lookup)
- Alternate key
- Duplicate detection
- Calculated and rollup columns
- Currency columns
- [Column comparison in queries using FetchXML, Web API, or the SDK API](../../developer/data-platform/column-comparison.md)
- Table sharing
- Composite indexes
- Cascade operations: Delete, Reparent, Assign, Share, Unshare
- Ordering on lookup columns
- Aggregate queries:
  - Distinct value of `attribute1` while orderby on `attribute2` value
  - Pagination when having multiple distincts
  - Distinct with multiple order by
  - Order by and group by together
  - Group by on link entity (left outer join)
  - Distinct on user owned tables  
- Table connections
- Access teams
- Queues

Column data types currently not available with elastic tables:

- Currency
- File
- Formula
- Whole number format other than None (Duration, Language code, and Time zone)
- Lookup based on the Customer option

## Create an elastic table

You create an elastic table just like any other new table in Dataverse.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and select Tables on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **New table** > **New table** on the command bar.
1. On the right properties pane, expand **Advanced options**.
1. Select **Elastic** as the table **Type**.
1. Select the properties you want, and then select **Save**. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)

## Known issues

- Currently Power Apps (make.powerapps.com) allows you to set a many-to-one (N:1) relationship with an elastic table where the N table is a standard table. Standard table will have a lookup column pointing to an elastic table row. While retrieving rows for a standard table in such a relationship, the lookup column that points to an elastic table row won't have the formatted value returned when the elastic table row has the `partitionid` set. More information: [Developer Guide: Partitioning and horizontal scaling](../../developer/data-platform/elastic-tables.md#partitioning-and-horizontal-scaling)
- Getting related rows when making a query on an elastic table currently doesn't work. However, getting related rows works when retrieving a single elastic table row.
- When [time to live (TTL)](#automatic-removal-of-data) is used on a row, the row will get deleted from the elastic table when TTL has expired. If it's synchronized to a data lake using [Synapse Link for Dataverse](export-to-data-lake.md) before TTL expiry, it won't be deleted from the data lake.

## For developers

Elastic tables have different behaviors and capabilities than standard tables when developers use them with Dataverse APIs. The following articles for developers describe these differences:

- [Elastic tables (preview)](../../developer/data-platform/elastic-tables.md)
- [Create elastic tables using code (preview)](../../developer/data-platform/create-elastic-tables.md)
- [Use elastic tables using code (preview)](../../developer/data-platform/use-elastic-tables.md)
- [Query JSON columns in elastic tables (preview)](../../developer/data-platform/query-json-columns-elastic-tables.md)
- [Bulk Operation messages (preview)](../../developer/data-platform/bulk-operations.md)
- [Elastic table sample code (preview)](../../developer/data-platform/elastic-table-samples.md)



## See also

[Create and edit tables using Power Apps](create-edit-entities-portal.md)

