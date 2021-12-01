---
title: Accessing and storing data for a Power Apps project | Microsoft Docs
description: As part of the design phase of a Power Apps project, document where and how you'll access existing data you need, and decide where you'll store data you create.
author: taiki-yoshida
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: tayoshi
ms.reviewer: kathyos

---

# Where's the data?

You can retrieve and store data three different ways.

:::row:::
    :::column:::
        ![New data.](media/new-data.png "New data")

        **New data** If your app is creating data that doesn't already exist anywhere, such
        as in situations where the existing business process was done using paper, we recommend storing
        the data either in Microsoft Dataverse or a SharePoint custom list. 
        
        We'll discuss this topic in [Data modeling: Designing your data structure](data-modeling.md).
    :::column-end:::
   :::column:::
        ![Read/write from existing system.](media/read-write.png "Read/write from existing system")

       **Read/write from an existing system** This is a type of data where you need to
       retrieve the latest information from an existing database or system. In these cases,
       data needs to be requested at the time you need it.
        
    :::column-end:::
    :::column:::
        ![Make a copy of existing data.](media/copy-data.png "Make a copy of existing data")

        **Make a copy of the data** In situations where original data should never be
        modified or overwritten, you can copy the data to another data store such as
        Dataverse. This ensures that the data in the original system won't be
        changed, yet your app can work with it. This scenario is common when
        working with data in accounting and revenue-related systems.

    :::column-end:::
:::row-end:::

## Accessing existing data

Apps created with Power Apps have two ways of using existing data. One is by using a connector, which allows
you to connect directly to a data source. The other is by using a dataflow, which copies
a snapshot of the data.

- **Using a connector**: A connector is a feature in Power Apps where you can connect to various systems
and sources&mdash;such as SharePoint, SQL Server, or Office 365&mdash;and directly
retrieve data from them or save data to them. More information: [Overview of canvas-app connectors for Power Apps](../../maker/canvas-apps/connections-list.md)

- **Using a dataflow**: Dataflow is a feature in Power Apps where you can extract, transform, and load
data from another system to Dataverse or Azure Data Lake storage.
Unlike a connector, it fetches data in a scheduled batch. Instead of just
retrieving the data as-is from the data source, you can use Power Query
Online to manipulate, cleanse, and transform data before you store it to the
target storage. More information: [Self-service data prep with dataflows](../../maker/data-platform/self-service-data-prep-with-dataflows.md)

The method you choose depends on your use cases and how data needs to be handled. The following table lists some items to use for comparison.

|   Item to compare     | Connectors                                   | Dataflow                                           |
|-----------------------|----------------------------------------------|----------------------------------------------------|
| Freshness of data     | Real-time                                    | Static or snapshot                                 |
| Direction             | Bidirectional                                | One direction (from origin to Dataverse) |
| Modify existing data? | Yes                                          | No                                                 |
| Use cases             | Production order, Timesheet, Sales quotation | Customer master, Past invoices, Employee list      |

We provide additional technical information in the next article, [Working with enterprise systems](enterprise-systems.md).

## Example: Expense report data

Our expense report project includes each of the three types of data storage
needs:

- **New data**: Because the expense reports were on paper, we need a new
    storage system for the data created by the employee filling out the expense
    report. We'll need to design a data model for that.

- **Writing to an existing system**: When the Accounting team exports the data
    from the expense reporting into the finance system, they'll need to use a
    data connector.

- **Copied data**: Our expense reports also include some data that we looked up from
    Azure Active Directory, such as the employee ID, manager, and department. We
    don't want to change that data in the original system, but we do need to
    keep a copy of it. We want to record the employee's manager and department at
    the time they created the report, not at some point in the future when we
    look at the report again. (They might have changed departments or even left
    the company.)

> [!div class="nextstepaction"]
> [Next step: Working with enterprise systems](enterprise-systems.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]