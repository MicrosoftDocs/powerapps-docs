---
title: Create an app from Excel | Microsoft Docs
description: Use PowerApps to automatically create an app using an Excel file stored in the cloud
services: ''
suite: powerapps
documentationcenter: na
author: MandiOhlinger
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
# Quickstart: Create an app using Excel

This quickstart shows how to automatically create your first app using Excel table data within PowerApps. In this article, you create a new app, select an existing Excel file, and then see what you created. Every generated app automatically includes screens to browse records, show record details, and create or update records. This is a quick way to get a working app using Excel data. You can also customize the app. 

The Excel data can be in a cloud-storage account, such as OneDrive, Google Drive, Box, and so on. This quickstart uses OneDrive for Business.

To follow this quickstart, download the [flooring estimates Excel file](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx), and save it in your [cloud storage account](../connections/cloud-storage-blob-connections.md). If you have Excel data [formatted as a table](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664), then you can use your own Excel file. 

If you're not signed up for PowerApps, you can [sign up for free](https://web.powerapps.com/signup?redirect=marketing&email=).

## Sign in to PowerApps

Open a web browser, and go to [https://web.powerapps.com]([https://web.powerapps.com). Sign in with your account.

## Choose the Excel table
1. In the left menu, select **Apps**, and then select **Create an app**.

2. In **Start with your data**, select **OneDrive for Business**. You may have to **Create** the connection. 

3. Select **FlooringEstimates.xlsx**, select the **FlooringEstimates** table, and then select **Connect**. It may take a few minutes to create your app.

    ![Select FlooringEstimates table](./media/get-started-create-from-data/select-flooring-estimates-table.png)

## View your app   
In PowerApps Studio, select **See a preview of this app**. Play the app. Select the different flooring options, and use the arrows to navigate within your app. You can also sort the list, and add new items to the list.

![Preview your app](./media/get-started-create-from-data/refresh-list-add-new-flooring-estimates.png)

## Clean up your resources
Apps aren't saved until you save them. If you want to keep this app, then save it (Ctrl + S). If you don't want to save this app, then close it using `Ctrl + F4`, or go to the **File** menu, and select **Close**. 

To remove the One Drive for Business connection, go to the **File** menu, and select **Connections**. In the list, select your connection, and then **Delete**.

## Next steps
In this quick start, you created an app using existing data in an Excel table. To get more hands-on experience creating apps, use one of our templates.

> [!div class="nextstepaction"]
> [Create and run an app from a template](get-started-test-drive.md)