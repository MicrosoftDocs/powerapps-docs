---
title: Add data to an entity in Common Data Service by using Power Query | Microsoft Docs
description: Step-by-step instructions for how to use Power Query to add data to a new or existing entity in Common Data Service from another data source.
author: mllopis
manager: kfile
ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: cds
ms.date: 05/04/2020
ms.author: millopis
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Add data to an entity in Common Data Service by using Power Query
In this procedure, you'll create an entity in [Common Data Service](data-platform-intro.md) and fill that entity with data from an OData feed by using Power Query. You can use the same techniques to integrate data from these online and on-premises sources, among others:

* SQL Server
* Salesforce
* IBM DB2
* Access
* Excel
* Web APIs
* OData feeds
* Text files

You can also filter, transform, and combine data before you load it into a new or existing entity.

If you don't have a license for Power Apps, you can [sign up for free](../signup-for-powerapps.md).

## Prerequisites
Before you start to follow this topic:
- Switch to an [environment](../canvas-apps/working-with-environments.md) in which you can create entities.
- You must have a Power Apps per user plan or Power Apps per app plan.

## Specify the source data

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. In the navigation pane, select **Data** to expand it, and then select **Entities**. 

    > [!div class="mx-imgBorder"] 
    > ![Power Apps home page](./media/data-platform-cds-newentity-pq/entities-get-data.png)

1. In the command menu, select **Get data**.

1. In the list of data sources, select **OData**.

    > [!div class="mx-imgBorder"] 
    > ![Choose the OAuth connector](./media/data-platform-cds-newentity-pq/choose-odata.png)

1. Under **Connection settings**, type or paste this URL, and then select **Next**:<br>
`https://services.odata.org/V4/Northwind/Northwind.svc/`

1. In the list of tables, select the **Customers** check box, and then select **Transform data**.

    > [!div class="mx-imgBorder"] 
    > ![Select the Customers table](./media/data-platform-cds-newentity-pq/select-table.png)

1. (optional) Modify the schema to suit your needs by choosing which columns to include, transforming the table in one or more ways, adding an index or conditional column, or making other changes.

1. In the lower-right corner, select **Next**.

## Specify the target entity
1. Under **Load settings**, select **Load to new entity**.

    > [!div class="mx-imgBorder"] 
    > ![Specify the name of the new entity](./media/data-platform-cds-newentity-pq/new-entity-name.png)

    You can give the new entity a different name or display name, but leave the default values to follow this tutorial exactly.

1. In the **Unique primary name field** list, select **ContactName**, and then select **Next**.

    You can specify a different primary-name field, map a different column in the source table to each field in the entity that you're creating, or both. You can also specify whether Text columns in your query output should be created as either Multiline Text or Single-Line Text in the Common Data Service. To follow this tutorial exactly, leave the default column mapping.

1. Select **Refresh manually** for Power Query - Refresh Settings, and then select **Create**.

1. Under **Data** (near the left edge), select **Entities** to show the list of entities in your database.

    The **Customers** entity that you created from an OData feed appears as a custom entity.

    > [!div class="mx-imgBorder"] 
    > ![List of standard and custom entities](./media/data-platform-cds-newentity-pq/entity-list.png)

> [!WARNING]
> If you use Power Query to add data to an existing entity, all data in that entity will be overwritten.

If you select **Load to existing entity**, you can specify an entity into which you add data from the **Customers** table. You could, for example, add the data to the **Account** entity with which the Common Data Service ships. Under **Field mapping**, you can further specify that data in the **ContactName** column from the **Customers** table should be added to the **Name** column in the **Account** entity.

  > [!div class="mx-imgBorder"] 
  > ![Specify the name of the new entity](./media/data-platform-cds-newentity-pq/existing-entity.png)

We're excited about this functionality and eager to hear your feedback. Please [send us your suggestions and feedback](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1) about this feature!

If an [error message about permissions](data-platform-cds-newentity-troubleshooting-mashup.md) appears, talk to your administrator.

> [!WARNING]
> There is a limit of 500,000 rows per run and per project that can be loaded using this feature.
