---
title: Access and store data for a Power Apps project
description: Learn how to access and store data for your Power Apps project. Explore methods for handling new, existing, and copied data effectively.
#customer intent: As a Power Apps maker, I want to understand how to access and store data so that I can design an effective data model for my app.
author: taiki-yoshida
ms.topic: concept-article
ms.custom: guidance
ms.date: 02/20/2026
ms.subservice: guidance
ms.author: tayoshi
ms.reviewer: jhaskett-msft

---

# Where's the data?

You can retrieve and store data in three different ways.

:::row:::
    :::column:::
        :::image type="content" source="media/new-data.png" alt-text="Screenshot of new data icon.":::

        **New data** If your app creates data that doesn't already exist anywhere, such as in situations where the existing business process was done using paper, store the data either in Microsoft Dataverse or a SharePoint custom list. 
        
        This topic is discussed in [Data modeling: Designing your data structure](data-modeling.md).
    :::column-end:::
   :::column:::
        :::image type="content" source="media/read-write.png" alt-text="Screenshot of read/write from existing system icon.":::

       **Read/write from an existing system** This type of data requires you to retrieve the latest information from an existing database or system. In these cases, you need to request data at the time you need it.
        
    :::column-end:::
    :::column:::
        :::image type="content" source="media/copy-data.png" alt-text="Screenshot of copy data icon.":::

        **Make a copy of the data** In situations where you should never modify or overwrite original data, copy the data to another data store such as Dataverse. This approach ensures that the data in the original system stays unchanged, yet your app can work with it. This scenario is common when working with data in accounting and revenue-related systems.

    :::column-end:::
:::row-end:::

## Accessing existing data

Apps created with Power Apps have two ways of using existing data. One is by using a connector, which allows
you to connect directly to a data source. The other is by using a dataflow, which copies
a snapshot of the data.

- **Using a connector**: A connector is a feature in Power Apps where you can connect to various systems
and sources&mdash;such as SharePoint, SQL Server, or Office 365&mdash;and directly retrieve data from them or save data to them. More information: [Overview of connector for canvas-app](../../maker/canvas-apps/connections-list.md)

- **Using a dataflow**: Dataflow is a feature in Power Apps where you can extract, transform, and load
data from another system to Dataverse or Azure Data Lake storage. Unlike a connector, it fetches data in a scheduled batch. Instead of just retrieving the data as-is from the data source, you can use Power Query Online to manipulate, cleanse, and transform data before you store it to the target storage. More information: [Self-service data prep with dataflows](../../maker/data-platform/self-service-data-prep-with-dataflows.md)

The method you choose depends on your use cases and how data needs to be handled. The following table lists some items to use for comparison.

|   Item to compare     | Connectors                                   | Dataflow                                           |
|-----------------------|----------------------------------------------|----------------------------------------------------|
| Freshness of data     | Real-time                                    | Static or snapshot                                 |
| Direction             | Bidirectional                                | One direction (from origin to Dataverse) |
| Modify existing data? | Yes                                          | No                                                 |
| Use cases             | Production order, Timesheet, Sales quotation | Customer master, Past invoices, Employee list      |

We provide more technical information in the next article, [Working with enterprise systems](enterprise-systems.md).

## Example: Expense report data

Our expense report project includes each of the three types of data storage needs:

- **New data**: Because the expense reports were on paper, we need a new storage system for the data created by the employee filling out the expense report. We need to design a data model for that need.

- **Writing to an existing system**: When the Accounting team exports the data from the expense reporting into the finance system, they need to use a data connector.

- **Copied data**: Our expense reports also include some data that we looked up from Microsoft Entra ID, such as the employee ID, manager, and department. We don't want to change that data in the original system, but we do need to keep a copy of it. We want to record the employee's manager and department at the time they created the report, not at some point in the future when we look at the report again. (They might have changed departments or even left the company.)

> [!div class="nextstepaction"]
> [Next step: Working with enterprise systems](enterprise-systems.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
