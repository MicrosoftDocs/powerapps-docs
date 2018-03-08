---
title: Create new entities in the Common Data Service (CDS) using Power Query | Microsoft Docs
description: Step-by-step instructions for creating a new entity in the CDS using Power Query.
services: ''
suite: powerapps
documentationcenter: na
author: mllopis
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 08/18/2017
ms.author: millopis

---
# Create new entities in the Common Data Service (CDS) using Power Query
With the integration of **Power Query**, business app developers can create new entities in the Common Data Service (CDS) from a wide range of data sources.

The **Common Data Service** lets users securely store and manage data within a set of standard and custom entities. An *entity* is a set of fields used to store data, similar to a table within a database. Once the data is stored in the Common Data Service, you can use **Microsoft PowerApps** to build rich applications that use the stored data.

With **Power Query** integration, business app developers using PowerApps can create new entities in the **Common Data Service** based on data from external data sources, such as on-premises data sources like relational databases (SQL Server, IBM DB2, and so on), Excel, Access, and text files, as well as online services such as Salesforce, Azure SQL Database and Data Warehouse, Web APIs, OData feeds, and many more sources. In addition to the wide array of data sources to which you can connect, using **Power Query** also lets you filter, transform, and combine data before loading it into the Common Data Service.

![New entity from data](./media/data-platform-cds-newentity-pq/data-platform-cds-pq-01.jpg)

## Enabling the CDS New Entities from Power Query feature
This feature is available in your PowerApps tenant, but is not turned on by default. You can enable it in [web.powerapps.com](https://aka.ms/pqocds).

> [!NOTE]
> You can create new custom entities only in databases that you have created.

In the PowerApps portal, take the following steps to enable this feature:

1. Browse to the **Common Data Service > Entities** tab, in the left navigation pane.

2. From the **Entities** list, select the **New Entity** dropdown.

3. From the list that appears in the dropdown menu, select **New Entity from Data (Technical Preview)** as shown in the following image.
   
    ![New entity from data](./media/data-platform-cds-newentity-pq/data-platform-cds-pq-02.jpg)
4. Once you select **New Entity from Data (Technical Preview)** from the menu, a dialog appears with the list of available connectors in this Technical Preview, as shown in the following image.
   
   ![Available connectors](./media/data-platform-cds-newentity-pq/data-platform-cds-pq-03.jpg)
5. Once you've selected the connector you want to use, you can continue to the next steps to specify data source connection details and credentials, select which tables to import, and so on. You may be able to access the **Query Editor** as well (using the **Edit** button in the **Navigator** view) and thereby apply filters or data transformation steps before importing data into CDS.
   
    ![](media/data-platform-cds-newentity-pq/data-platform-cds-pq-04.jpg)

## Adjust load settings and other behavior
Once you've completed the steps in the previous section, and have a data source ready to use to create new entities in CDS using **Power Query**, you can adjust additional load settings, such as refresh behavior and entity-specific settings (such as Display Name, Primary Keys, and others).

![](media/data-platform-cds-newentity-pq/data-platform-cds-pq-05.jpg)

Once those steps are completed and you select **Load**, you will have created new custom entities in CDS. You can also edit queries after the initial load by accessing the **Entity** menu for a specific entity.

We're very excited about this functionality, and are eager to hear your feedback. Please [send us your suggestions and feedback](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1) about this feature!

