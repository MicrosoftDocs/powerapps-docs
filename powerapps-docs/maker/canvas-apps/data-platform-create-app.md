---
title: Create an app in PowerApps for the Common Data Service for Apps | Microsoft Docs
description: Automatically generate an app in PowerApps to manage data in the Common Data Service for Apps
services: powerapps
documentationcenter: na
author: AFTOwen
manager: kfile

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 01/22/2018
ms.author: anneta

---
# Quickstart: Create an app in PowerApps for the Common Data Service for Apps

This quickstart shows how to automatically create your first app using a Common Data Service database within PowerApps. In this article, you select an entity, create an app, and then see what you created. Every generated app automatically includes screens to browse records, show record details, and create or update records. This is a quick way to get a working app using the Common Data Service. You can also customize the app.

This app can access data in a standard entity, which is built in, or in a custom entity, which you or someone in your organization creates. [Understand entities](../../common-data-service/data-platform-intro.md) is a good resource to get acquainted with the Common Data Service.

To follow this quickstart, you must create or switch to an environment in which a [database in the Common Data Service](../../administrator/create-database.md) has been created and contains sample data.

If you're not signed up for PowerApps, you can [sign up for free](https://web.powerapps.com/signup?redirect=marketing&email=).

## Sign in to PowerApps

Sign in to [PowerApps](https://web.powerapps.com). 

## Choose an entity

1. In the left menu, select **Apps**, and then select **Create an app**.

2. Under **Start with your data**, select **Common Data Service**. You may be asked to **Create**.

3. Under **Choose an entity** select an entity (such as **Account**), and then select **Connect**.

	Your app may take a few minutes to create.

    ![Select the Account entity](./media/data-platform-create-app/cds-choose-entity-connect.png)

## View your app   
In PowerApps Studio, select **See a preview of this app**. Play the app. Select the different accounts, and use the arrows to navigate within your app. You can also sort the list and add items to it.

![Preview your app](./media/data-platform-create-app/cds-database-app.png)

## Clean up your resources
To keep this app, save it by pressing Ctrl + S. Otherwise, press Ctrl + F4 (or open the **File** menu and then select **Close**).

## Next steps
In this quickstart, you created an app to manage sample data in an entity of a Common Data Service database. The first screen of the app contains a gallery, which you can customize to better suit your needs. 

> [!div class="nextstepaction"]
> [Customize a gallery](customize-layout-sharepoint.md)
