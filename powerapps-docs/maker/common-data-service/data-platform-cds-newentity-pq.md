---
title: Adding data to an entity in the Common Data Service using Power Query | Microsoft Docs
description: Step-by-step instructions for using Power Query to add data to a new or existing entity in the Common Data Service for Apps from another data source.
services: ''
suite: powerapps
documentationcenter: na
author: AFTOwen
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/17/2018
ms.author: anneta

---
# Add data to an entity in the Common Data Service by using Power Query
In this procedure, you'll create an entity in the [Common Data Service for Apps](data-platform-intro.md) and fill that entity with data from an OAuth feed by using Power Query. You can use the same techniques to integrate data from these online and on-premises sources, among others:

* SQL Server
* Salesforce
* IBM DB2
* Access
* Excel
* web APIs
* OData feeds
* text files

You can also filter, transform, and combine data before you load it into a new or existing entity.

If you don't have a license for PowerApps, you can [sign up for free](../signup-for-powerapps.md).

## Prerequisites
To follow this topic, you must switch to an [environment](../canvas-apps/working-with-environments.md) in which you can create entities.

## Specify the source data

1. Sign in to [PowerApps](https://web.powerapps.com), and then click or tap the down arrow for **Data** near the left edge.

	![PowerApps home page](./media/data-platform-cds-newentity-pq/sign-in.png)

1. In the list that appears, click or tap **Data Integration**, and then click or tap **New Project** near the upper-right corner of the window.

1. In the list of data sources, click or tap **OData**.

	![Choose the OAuth connector](./media/data-platform-cds-newentity-pq/choose-odata.png)

1. Under **Connection settings**, type or paste this URL, and then select **Next**:<br>
`http://services.odata.org/V4/Northwind/Northwind.svc/`

1. In the list of tables, select the **Customers** check box, and then click or tap **Next**.

	![Select the Customers table](./media/data-platform-cds-newentity-pq/select-table.png)

1. (optional) Modify the schema to suit your needs by choosing which columns to include, transforming the table in one or more ways, adding an index or conditional column, or making other changes.

1. In the lower-right corner, click or tap **Next**.

## Specify the target entity
1. Under **Load settings**, select **Load to new entity**.

    ![Specify the name of the new entity](./media/data-platform-cds-newentity-pq/new-entity-name.png)

    You can give the new entity a different name or display name, but leave the default values to follow this tutorial exactly.

1. In the **Primary name field** list, click or tap **ContactName**, and then click or tap **Next** in the lower-right corner.

    You can specify a different primary-name field, map a different column in the source table to each field in the entity that you're creating, or both. To follow this tutorial exactly, leave the default column mapping.

1. When the **Load status** is **Completed**, select **Done** in the lower-right corner.

1. Under **Data** (near the left edge), select **Entities** to show the list of entities in your database.

    The **Customers** entity that you created from an OData feed appears as a custom entity.

    ![List of standard and custom entities](./media/data-platform-cds-newentity-pq/entity-list.png)

> [!WARNING]
> If you use Power Query to add data to an existing entity, all data that the entity previously contained will be overwritten.

If you select **Load to existing entity**, you can specify an entity into which you add data from the **Customers** table. You could, for example, add the data to the **Account** entity with which the Common Data Service ships. Under **Source column**, you can further specify that data in the **ContactName** column from the **Customers** table should be added to the **Name** column in the **Accounts** entity.

![Specify the name of the new entity](./media/data-platform-cds-newentity-pq/existing-entity.png)

We're very excited about this functionality, and are eager to hear your feedback. Please [send us your suggestions and feedback](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1) about this feature!

