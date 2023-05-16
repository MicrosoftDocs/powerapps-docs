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

## When to consider Dataverse elastic tables?

Elastic tables are designed to handle large volumes of data in real-time. With elastic tables, you can import, store, and analyze large volumes of data without scalability, latency, or performance issues.

Elastic tables have unique capabilities for flexible schema, horizontal scaling, and automatic removal of data after a time-period.

Elastic tables automatically scale to ingest tens of millions of rows every hour. Background processes can collate the IoT signals, predict maintenance requirements, and proactively schedule technicians.

Consider a scenario where Contoso is a retailer with millions of existing customers. Contoso has a large database of customers and are looking to increase sales while retaining customers. Based on prior customer history, they're looking to have 24-hour flash sale events with different coupons targeting their customers and products. They have estimated that the number of coupons required will be 100 million plus per flash sale campaign. Marketing plans to run multiple 24-hour campaigns targeting different customer segments.  

The requirement for Constoso’s marketing application is that it must be able to ingest up to 100 million or more coupon details within a few hours, read millions of coupons per hour, and send coupons to customers.  

Elastic tables will automatically scale for this high throughput scenario.  

For example, in the above scenario, an elastic table named *Coupon* with millions of records can be associated with Dataverse standard tables like *Contact* (customer info) and *Offer* (a custom standard table). Since the elastic tables are isolated from the standard tables, performance for the overall marketing application won't be negatively impacted. In addition, time-to-live capability with elastic table (*Coupon* in this scenario) allows removal of data automatically after fixed periods and ensure optimization of storage capacity.

## Horizontal scaling and performance  

As your business data grows, elastic tables provide unlimited auto scalability based on your application workload, both for storage size and throughput, such as the number of records created, updated, or deleted in a given timeframe. 

If your business scenario requires very large volume of data writes, application makers can make use of Dataverse XMultiple <!-- what is xmultiple? Use a term that exists in the Power Platform vernacular --> API's to achieve more thoughput within Dataverse throttling limits. Learn more.

### Automatic removal of data

Time to live (TTL) policies ensure that you're always working with the most up-to-date and accurate information, while optimizing resources and reducing risk. The TTL live value is set in seconds on a record, and it's interpreted as a delta from the time that a record was last modified.

### Flexible schema with JSON columns

Elastic tables enable you to store and query data with varying structures, without the need for pre-defined schemas or migrations. There's no need to write custom code to map the imported data into a fixed schema. <!-- Need link to How to query JSON columns in elastic tables -->

## Considerations when you use elastic tables  

Elastic tables don't provide the same level transaction support as standard tables. Standard tables support strong, consistent transactions support. Elastic tables support what is called *eventual consistency* for transactions, which means that updates made to the database might take some time to propagate to all nodes in the system. More information: [Eventual consistency](/azure/cosmos-db/consistency-levels#eventual-consistency).

Elastic tables support only left-outer JOIN in queries. This means that filters on related tables when creating views or in Advanced Find won't work. We recommend to denormalize columns by grouping them on the same table, such as  from related tables into the main table if filters on related tables are needed.

### Denormalize columns

Consider a retailer with two elastic tables: customer and address. One customer has many addresses. You want to return query results for all customers from the customer table whose city value in the address table is *New York*.

This requires an inner join of the two tables, which isn't supported with elastic tables. One way to make this work for the elastic tables is to denormalize the city data into the customer table so that all customers city values are present in the customer table.  

## Elastic tables feature support

- Record ownership, change tracking, auditing, mobile offline, and Dataverse search.
- Create, retrieve, update, delete (CRUD) operations including `XMultiple` (for high throughput), bulk delete, and requests from plugins.
- Bulk deletion.
- Relationships:
  - 1:N (One-to-many)
    - One elastic table -> Many elastic tables
    - One elastic table -> Many standard tables
  - N:1 (Many-to-one)
    - Many elastic tables -> One standard table

> [!IMPORTANT]
> When you add a lookup column to a standard table that references an elastic table, don't set the `partitionid` value on the elastic table records. Lookup columns that reference an elastic table only work correctly when a `partitionid` value isn't used for the record in the elastic table. When no `partitionid` value is specified when the row is created, it defaults to the primary key value, and the lookup works as expected. But, if the row is created with a `partitionid` value other than the primary key value, the lookup won't work.
> 
> You can add this kind of  lookup column three  different ways: 
> 
> - By adding a lookup column on a standard table that references to an elastic table.
> - By creating a many-to-one relationship on a standard table where the related (one) table is an elastic table.
> - By creating a one-to-many relationship on an elastic table where the related (many) table is a standard table.

Security features:

- User and organization owned tables
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
- Composite indexes (all fields are indexed)
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

## Known issue

Currently Power Apps (make.powerapps.com) allows you to set a many-to-one (N:1) relationship with an elastic table where the N table is a standard table. However this relationship isn't supported and won't function as expected.

## See also

[Create and edit tables using Power Apps](create-edit-entities-portal.md)