---
title: Import or export data | Microsoft Docs
description: Import or export an entity.
services: powerapps
documentationcenter: na
author: kfend
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 12/06/2016
ms.author: kfend

---
# Import or export data from the Common Data Service
You can move data into or out of the Common Data Service in one of two ways:

* If you want to do a one-time bulk import or export of data, you can use Microsoft Excel for multiple entities.
* If you want an ongoing import or export of data for a single entity to another service, such as Dynamics 365 or Salesforce, or even to an Excel file. To set up ongoing import or export, you can use [Microsoft Flow](https://flow.microsoft.com).

## Import or export data once
### Import data from Excel
1. On [powerapps.com](https://web.powerapps.com), expand the **Common Data Service** section and click or tap **Entities** in the left navigation pane.
2. Next to **New entity**, click or tap the ellipsis, and then click or tap **Import data**.
3. Select the entity that you want to import data into, and then click or tap **Next**.
4. Click or tap **Search**. Select the file that you want to import data from.
5. If the **Mapping Status** is not **Match** with a green check mark, then you will need to specify the mapping between the entity fields and the columns in the Excel file. To map the columns:
   1. Click or tap **Show Mapping**.
   2. For each entity field, select the matching column in the Excel file.
   3. Click or tap **Save changes**.
6. Click **Import**.

### Export data to Excel
You can do a one-time data export from a standard entity or custom entity, and you can export data from more than one entity at a time. If you export data from more than one entity, each entity is exported into its own Microsoft Excel file.

1. On [powerapps.com](https://web.powerapps.com), click or tap **Entities** in the left navigation pane.
2. Next to **New entity**, click or tap the ellipsis, and then click or tap **Export data**.
3. Select the entities that you want to export data from, and then click or tap **Export to Excel**.
4. When **Export Completed** appears, click or tap **Download exported data** to download the data.

## Use Microsoft Flow to set up ongoing import or export
You can set up ongoing import or export for a single standard entity or custom entity at a time. Some possible places you can connect to include:

* Dynamics 365
* Salesforce
* Microsoft Excel files stored in any cloud file provider
* A Microsoft SQL database, both in the cloud and on-premises
* A custom connector that you define to connect to your own systems

Today, when you use Microsoft Flow to import or export data, it is not a full synchronization service. When an object is added to one service, it will be imported into the other system. However, that means if an object is deleted from one system it will not be deleted in the other system.

How to set up the import depends on if a template already exists for the object that you want to import. If a template exists, you can set it up to copy data from one system to another. For more information, see [Create a flow that uses the Microsoft Common Data Service](https://flow.microsoft.com/documentation/common-data-model-intro/). However, if no such template exists, you'll need to create a flow that can use the database. For more details, refer to [How to create a flow from scratch](https://flow.microsoft.com/documentation/get-started-logic-flow/).

