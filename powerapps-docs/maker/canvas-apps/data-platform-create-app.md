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

1. Under **Start with your data**, select the arrow that points to the right.

1. Under **Connections**, select your connection to the Common Data Service.

1. Near the right edge, type **Accounts** in the search box. 

1. Under **Choose a table**, select **Accounts**, and then select **Connect**.

	After a few minutes, your app opens to the browse screen, which shows a list of accounts, a search bar above that list, and icons for refreshing the list, sorting the list, and creating a record. In the next section, you'll customize this screen to make it easier to use.

## Customize the browse screen
1. Click or tap near the center of the list to select it.

1. In the right-hand pane, select **Accounts** to open the **Data** pane.

1. Under **Layout**, select the down arrow to show layout options, and then select the option that shows only a title.

1. Select the first item in the list, and then select the down arrow in the **Data** pane to show a list of options for that element.

1. In the list of options for the selected element, select **Account name (name)**.

	The list shows the name of each account.

To keep this app, save it by pressing Ctrl + S. Otherwise, press Ctrl + F4 (or open the **File** menu and then select **Close**).

## Next steps
In this quickstart, you created an app to manage sample data in an entity of a Common Data Service database. The first screen of the app contains a gallery, which you can customize to better suit your needs. 

> [!div class="nextstepaction"]
> [Customize a gallery](customize-layout-sharepoint.md)
