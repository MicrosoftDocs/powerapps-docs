---
title: Quickstart for generating an app in PowerApps for the Common Data Service for Apps | Microsoft Docs
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
ms.date: 03/10/2018
ms.author: anneta

---
# Quickstart: Generate an app in PowerApps for the Common Data Service for Apps

In this quickstart, you'll use PowerApps to automatically generate your first app based on a list of sample accounts in the [Common Data Service with Apps](../common-data-service/data-platform-intro.md). In this app, you can browse all accounts, shows details of a single account, and create, update, or delete an account.

To follow this quickstart, you must switch to an [environment](working-with-environments.md) in which a database in the Common Data Service has been created and contains data. If no such environment exists and you have administrative privileges, you can [create an environment](../../administrator/environments-administration.md#create-an-environment) that meets this requirement.

If you're not signed up for PowerApps, you can [sign up for free](https://web.powerapps.com).

## Generate an app
1. Sign in to [PowerApps](https://web.powerapps.com).

	![PowerApps home page](./media/data-platform-create-app/sign-in.png)

1. Under **Make apps like these**, hover over **Start from data**, and then select **Make this app**.

	![Option to create an app](./media/data-platform-create-app/make-this-app.png)

1. Under **Start with your data**, select the arrow that points to the right.

	![Arrow icon](./media/data-platform-create-app/right-arrow.png)

1. Under **Connections**, select your connection to the Common Data Service.

1. Type **Accounts** in the search box (near the right edge), select **Accounts** under **Choose a table**, and then select **Connect**.

	![Select an entity](./media/data-platform-create-app/select-entity.png)

	After a few minutes, your app opens to the browse screen, which shows a list of accounts, a search bar above that list, and icons for refreshing the list, sorting the list, and creating a record.

To keep this app, save it by pressing Ctrl + S. Otherwise, press Ctrl + F4 (or open the **File** menu and then select **Close**).

## Next steps
In this quickstart, you created an app to manage sample data in the Common Data Service for Apps. In this app, the browse screen shows a list of accounts, but you'll probably want to customize the list to show different types of data.

> [!div class="nextstepaction"]
> [Customize a gallery](customize-layout-sharepoint.md)
