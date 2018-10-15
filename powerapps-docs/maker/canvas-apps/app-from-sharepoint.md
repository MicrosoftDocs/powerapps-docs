---
title: Generate a canvas app from a SharePoint list | Microsoft Docs
description: In PowerApps, automatically generate a canvas app to manage data in a SharePoint list
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 08/09/2018
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Generate a canvas app in PowerApps from a SharePoint list

In this topic, you'll use PowerApps to automatically generate a canvas app based on items in a SharePoint list. You can generate the app from within PowerApps or SharePoint Online. From within PowerApps, you can generate the app based on a list in an on-premises SharePoint site if you [connect to it](connect-to-sharepoint.md) through a data gateway.

The app that you generate will contain three screens:

- In the browse screen, you can scroll through all items in the list.
- In the details screen, you can show all information about a single item in the list.
- In the edit screen, you can create an item or update information about an existing item.

You can apply the concepts and techniques in this topic to any list in SharePoint. To follow the steps exactly:

1. In a SharePoint Online site, create a list named **SimpleApp**.
2. In a column named **Title**, create entries for **Vanilla**, **Chocolate**, and **Strawberry**.

The principles of generating an app won't change even if you create a list that's far more complex, with many columns of various types such as text, dates, numbers, and currency.

> [!IMPORTANT]
> PowerApps doesn't support all types of SharePoint data. For more information, see [Known issues](connections/connection-sharepoint-online.md#known-issues).

## Generate an app from within PowerApps

1. Sign in to [PowerApps](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. Under **Make your own app**, hover over **Start from data**, and then select **Make this app**.

	![Option to create an app](./media/app-from-sharepoint/start-from-data.png)

1. On the SharePoint tile, select **Phone layout**.

	![Option to create an app](./media/app-from-sharepoint/sharepoint-tile.png)

1. With the **Connect directly** option selected, select **Create**.

    ![Create connection](./media/app-from-sharepoint/create-connection.png)

1. Under **Connect to a SharePoint site**, type or paste the URL for your SharePoint Online site, and then select **Go**.

    Include only the site URL (not the name of the list), as in this example:<br>`https://microsoft.sharepoint.com/teams/Contoso`

1. Under **Choose a list**, select **SimpleApp**, and then select **Connect**.

    After a few minutes, your app opens to the browse screen, which shows the items that you created in your list. If your list has data in more columns than just **Title**, the app will show that data. Near the top of the screen, a title bar shows icons for refreshing the list, sorting the list, and creating an item in the list. Under the title bar, a search box provides the option to filter the list based on text that you type or paste. 

    ![Browse screen](./media/app-from-sharepoint/browse-screen.png)

    You'll probably want to make more changes before you use this app or share it with others. As a best practice, save your work so far by pressing Ctrl-S before you proceed. Give your app a name, and then select **Save**.

## Generate an app from within SharePoint Online

If you create an app of a custom list from the SharePoint Online command bar, the app appears as a view of that list. You can also run the app on an iOS or Android device, in addition to a web browser.

1. In SharePoint Online, open a custom list, select **PowerApps** on the command bar, and then select **Create an app**.

    ![Create an app](./media/app-from-sharepoint/generate-new-app.png)

2. In the panel that appears, type a name for your app, and then select **Create**.

    ![Name the app](./media/app-from-sharepoint/app-name.png)

    A new tab appears in your web browser that shows the app that you automatically generated based on your SharePoint list. The app appears in PowerApps Studio, where you can customize it.

    ![Default app](./media/app-from-sharepoint/default-app.png)

3. (optional) Refresh the browser tab for your SharePoint list (by selecting it and then, for example, pressing F5), and then follow these steps to run or manage your app:

    - To run the app (in a separate browser tab), select **Open**.
    - To let others in your organization run the app, select **Make this view public**.

        To let others to edit your app, [share it](share-app.md) with **Can edit** permissions.

    - To remove the view from SharePoint, select **Remove this view**.

        To remove the app from PowerApps, [delete the app](delete-app.md).

## Next steps
In this topic, you created an app to manage data in a SharePoint list. As a next step, generate an app from a more complex list, and then customize the app (starting with the browse screen) to better suit your needs.

> [!div class="nextstepaction"]
> [Customize a default browse screen](customize-layout-sharepoint.md)
