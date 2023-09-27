---
title: Create a canvas app with data from Microsoft Lists (contains video)
description: In Power Apps, automatically create a canvas app to manage data in a list created using Microsoft Lists.
author: mduelae

ms.topic: conceptual
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 01/27/2022
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - Steven-Jia
  - mduelae
  - navjotm
  - emcoope-msft
---
# Create a canvas app with data from Microsoft Lists

In this topic, you'll use Power Apps to create a canvas app based on items in a list created using Microsoft Lists. You can create the app from within Power Apps or SharePoint Online. From within Power Apps, you can create the app based on a list in an on-premises SharePoint site if you [connect to it](connections/connection-sharepoint-online.md#create-a-connection) through a data gateway.

The app that you create will contain three screens:

- In the browse screen, you can scroll through all items in the list.
- In the details screen, you can show all information about a single item in the list.
- In the edit screen, you can create an item or update information about an existing item.

You can apply the concepts and techniques in this topic to any list in SharePoint. To follow the steps exactly:

1. In a SharePoint Online site, create a list named **SimpleApp**.
2. In a column named **Title**, create entries for **Vanilla**, **Chocolate**, and **Strawberry**.

The principles of generating an app won't change even if you create a list that's far more complex, with many columns of various types such as text, dates, numbers, and currency.

> [!IMPORTANT]
> Power Apps doesn't support all types of SharePoint data. For more information, see [Known issues](connections/connection-sharepoint-online.md#known-issues).

Watch this video to learn how to create a canvas app from a list:
> [!VIDEO https://www.microsoft.com/videoplayer/embed/RWLj3n]


## Create an app from within Power Apps

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Depending on how you want to create your app, from the home screen, select one of the following options:
   - To create a single-page gallery app with a responsive layout, choose either:
      - **Start with data** > **Select external data** > **From SharePoint**.
      - **Start with a page design** > **Gallery connected to external data** > **From SharePoint**.
   - To create a three screen mobile app, select **Start with an app template** > **From SharePoint**.
1. If you don't have a SharePoint connection already created, you'll be prompted to. To select a different connection, select on the **...** button to switch account or create a new connection. 
1. Enter the SharePoint URL and then select **Connect**. Or, select a recent site.
1. Select a list and then select, **Create app**.

Your app opens in Power Apps Studio where you can design, build, and manage your app. More information: [Understand Power Apps Studio](power-apps-studio.md)

You'll probably want to make more changes before you use this app or share it with others. As a best practice, save your work so far by selecting the save icon on the upper-right corner before you proceed. Give your app a name, and then select **Save**.


## Create an app from within SharePoint Online

If you create an app of a list from the SharePoint Online command bar, the app appears as a view of that list. You can also run the app on an iOS or Android device, in addition to a web browser.

1. In SharePoint Online, open a list, and then select **Integrate** > **Power Apps** > **Create an app**.

    ![Create an app.](./media/app-from-sharepoint/generate-new-app.png)

1. In the panel that appears, type a name for your app, and then select **Create**.

   A new tab appears in your web browser that shows the app that you created based on your list. The app appears in [Power Apps Studio](intro-maker-portal.md), where you can customize it.


1. (optional) Refresh the browser tab for your list (by selecting it and then, for example, pressing F5), and then follow these steps to run or manage your app:

    - To run the app (in a separate browser tab), select **Open**.
    - To let others in your organization run the app, select **Make this view public**.

        To let others edit your app, [share it](share-app.md) with **Can edit** permissions.

    - To remove the view from SharePoint, select **Remove this view**.

        To remove the app from Power Apps, [delete the app](delete-app.md).

> [!NOTE]
> Apps created from the list currently do not show in the Power Apps Mobile.

## Next steps
In this topic, you created an app to manage data in a list. As a next step, create an app from a more complex list, and then customize the app (starting with the browse screen) to better suit your needs.

> [!div class="nextstepaction"]
> [Customize a default browse screen](customize-layout-sharepoint.md)

### See also

- [SharePoint integration scenarios](sharepoint/scenarios-intro.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
