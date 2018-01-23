---
title: Create an app using Common Data Service | Microsoft Docs
description: Use PowerApps to automatically create an app using a common data service (CDS) database to add, update, or delete records
services: powerapps
documentationcenter: na
author: kfend
manager: anneta

ms.service: powerapps
ms.devlang: na
ms.topic: quickstart
ms.custom: mvc
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 01/22/2018
ms.author: mandia

---
# Quickstart: Create an app using Common Data Service

This quickstart shows how to automatically create your first app using a Common Data Service database within PowerApps. In this article, you create a new app, select a Common Data Service entity, and then see what you created. Every generated app automatically includes screens to browse records, show record details, and create or update records. This is a quick way to get a working app using Common Data Service. You can also customize the app. 

This app can access data in standard entities that are built-in, or in a custom entity that you or someone in your organization creates. [Understand entities](data-platform-intro.md) is a good resource to get acquainted with Common Data Service. 

To follow this quickstart, you need to create a [Common Data Service database](create-database.md). Be sure you **Create a database** to get sample data.

If you're not signed up for PowerApps, you can [sign up for free](https://web.powerapps.com/signup?redirect=marketing&email=).

## Sign in to PowerApps

Open a web browser, and go to [https://web.powerapps.com]([https://web.powerapps.com). Sign in with your account.

## Choose the entity

1. In the left menu, select **Apps**, and then select **Create an app**.

2. In **Start with your data**, select **Common Data Service**. You may be asked to **Create**.
 
3. **Choose an entity**, such as **Account**, and **Connect**. It may take a few minutes to create your app.

    ![Select the Account entity](./media/data-platform-create-app/cds-choose-entity-connect.png)

## View your app   
In PowerApps Studio, select **See a preview of this app**. Play the app. Select the different accounts, and use the arrows to navigate within your app. You can also sort the list, and add new items to the list.

![Preview your app](./media/data-platform-create-app/cds-database-app.png)

## Clean up your resources
Apps aren't saved until you save them. If you want to keep this app, then save it (Ctrl + S). If you don't want to save this app, then close it using `Ctrl + F4`, or go to the **File** menu, and select **Close**. 

To remove the Common Data Service database (and entities), go to the **File** menu, and select **Connections**. In the list, select your Common Data Service, and then **Delete**.

## Next steps
In this quick start, you created an app using existing data in a Common Data Service database. To get more hands-on experience creating apps, use one of our templates.

> [!div class="nextstepaction"]
> [Create and run an app from a template](get-started-test-drive.md)