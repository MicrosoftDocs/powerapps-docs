---
title: Create an app from scratch using a Common Data Service database | Microsoft Docs
description: Create an app to add, update, and delete records.
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
# Create an app from scratch using a Common Data Service database
Build an app to manage data that's stored in the Common Data Service, using standard entities (which are built in), custom entities (which your organization creates), or both.

When you build an app from the Common Data Service, you don't need to create a connection from Microsoft PowerApps, as you do with data sources such as SharePoint, Dynamics 365, or Salesforce. You only need to specify the entities that you want to show, manage, or use for both activities in the app.




1. Create a Common Data Service database. For more information, see [Create a Common Data Service database](administrator/create-database.md).
2. On [powerapps.com](https://web.powerapps.com), in the left navigation pane, click or tap **New app**.
3. In the dialog box that appears, click or tap **PowerApps Studio for web**. (You can also click or tap **PowerApps Studio for Windows**, and then follow the instructions to install PowerApps Studio for Windows. Although the instructions that follow use PowerApps Studio for web, the instructions for the Microsoft Windows app are similar.)
4. Under **Start with a blank canvas or template**, click or tap **Phone layout** on the **Blank app** tile.
5. If prompted, click or tap **Skip** to skip the tutorial.
6. Click or tap the **Content** tab.
7. Click or tap **Data sources**.
8. In the rightmost pane, click or tap **Add data source**.
9. Click or tap the Common Data Service that you want to use.
10. In the list of entities, select the check box for one or more entities that you want to use, and then click or tap **Connect**.

The entities that you specified appear in the list of data sources, and you can build your app as [Create an app from scratch](get-started-create-from-blank.md) describes.

