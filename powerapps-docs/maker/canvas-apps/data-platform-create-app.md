---
title: Generate a canvas app from Common Data Service for Apps | Microsoft Docs
description: In PowerApps, automatically generate a canvas app to manage data in Common Data Service for Apps
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: quickstart
ms.custom: canvas
ms.reviewer: 
ms.date: 05/06/2018
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Generate a canvas app from Common Data Service for Apps in PowerApps

In PowerApps, automatically generate a canvas app based on a list of sample accounts in [Common Data Service (CDS) for Apps](../common-data-service/data-platform-intro.md). In this app, you can browse all accounts, show details of a single account, and create, update, or delete an account.

If you're not signed up for PowerApps, [sign up for free](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) before you start.

## Prerequisites

To follow this quickstart, you must be assigned to the [Environment Maker](https://docs.microsoft.com/power-platform/admin/database-security.md#predefined-security-roles) security role, and you must [switch to an environment](working-with-environments.md) in which a database in CDS for Apps has been created, contains data, and allows updates. If no such environment exists and you have administrative privileges, you can [create an environment](https://docs.microsoft.com/power-platform/admin/environments-administration.md#create-an-environment) that meets this requirement.

## Generate an app

1. Sign in to [PowerApps](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and, if necessary, switch environments as specified earlier in this topic.

1. Under **Make your own app**, hover over **Start from data**, and then select **Make this app**.

	![Option to create an app](./media/data-platform-create-app/start-from-data.png)

1. On the **Common Data Service** tile, select **Phone layout**.

	![Connection tile](./media/data-platform-create-app/connection-tile.png)

1. Under **Choose a table**, select **Accounts**, and then select **Connect**.

1. If the **Welcome to PowerApps Studio** dialog box appears, select **Skip**.

Your app opens to the browse screen, which shows a list of accounts in a control called a gallery. Near the top of the screen, a title bar shows icons for refreshing the data in the gallery, sorting the data in the gallery alphabetically, and adding data to the gallery. Under the title bar, a search box provides the option to filter the data in the gallery based on text that you type or paste. 

By default, the gallery shows an email address, a city, and an account name. As you'll see in [Next steps](data-platform-create-app.md#next-steps), you can customize the gallery to change how the data appears and even show other types of data.

![Browse screen](./media/data-platform-create-app/browse-screen.png)

## Save the app
You'll probably want to make more changes before you use this app or share it with others. As a best practice, save your work so far before you proceed.

1. Near the upper-left corner, select the **File** tab.

1. In the **App settings** page, set the app name to **AppGen**, change the background color to deep red, and change the icon to a checkmark.

	![App settings page](./media/data-platform-create-app/app-settings.png)

1. Near the left edge, select **Save** and then, in the lower-left corner, select **Save**.

## Next steps
In this quickstart, you created an app to manage sample data about accounts in CDS for Apps. As a next step, customize the gallery and other elements of the default browse screen to better suit your needs.

> [!div class="nextstepaction"]
> [Customize a gallery](customize-layout-sharepoint.md).
