---
title: Generate an app from Excel | Microsoft Docs
description: Use PowerApps to automatically generate an app using an Excel file stored in a cloud-storage account
services: ''
suite: powerapps
documentationcenter: na
author: AFTOWen
manager: kfile

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.custom: mvc
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/18/2018
ms.author: anneta

---
# Generate an app from Excel in PowerApps
In this topic, you'll automatically generate your first app in PowerApps using data from an Excel table. You'll select an Excel file, generate an app, and then run the app that you generate. Every generated app includes screens to browse records, show record details, and create or update records. By generating an app, you can quickly get a working app using Excel data, and then you can customize the app to better suit your needs. 

The Excel file must be in a cloud-storage account, such as OneDrive, Google Drive, or Dropbox. This topic uses OneDrive for Business.

To follow this topic, download the [Flooring Estimates](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx) file in Excel, and save it in your [cloud storage account](connections/cloud-storage-blob-connections.md). As an alternative, you can use your own Excel file if the data is [formatted as a table](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664). 

If you don't have a license for PowerApps, you can [sign up for free](../signup-for-powerapps.md).

## Generate the app
1. Sign in to [PowerApps](https://web.powerapps.com).

    ![PowerApps home page](./media/get-started-create-from-data/sign-in.png)

1. Under **Make apps like these**, hover over **Start from data**, and then select **Make this app**.

	![Option to create an app](./media/get-started-create-from-data/make-this-app.png)

1. Under **Start with your data**, click or tap **Phone layout** on the tile for your cloud-storage account.

	![Option to create an app](./media/get-started-create-from-data/odfb-tile.png)

1. If prompted, click or tap **Connect**, and provide your credentials for that account.

1. Under **Choose an Excel file**, browse to **FlooringEstimates.xlsx**, and then click or tap it. 

1. Under **Choose a table**, click or tap **FlooringEstimates**, and then click or tap **Connect**.

	![Option to create an app](./media/get-started-create-from-data/choose-table.png)

## Run the app
1. Open Preview by pressing F5 (or by clicking or tapping the play icon near the upper-right corner).

	![Open Preview](./media/get-started-create-from-data/open-preview.png)

1. Toggle the sort order by clicking or tapping the sort icon near the upper-right corner.

	![Sort icon](./media/get-started-create-from-data/sort-icon.png)

1. Filter the list by typing or pasting one or more characters in the search box.

1. Click or tap the plus icon to add a record, add whatever data you want, and then click or tap the checkmark icon to save your changes.

1. Click or tap the next arrow for the record that you added, click or tap the pencil icon to edit the record, update one or more fields, and then click or tap the checkmark icon to save your changes.

1. Click or tap the next arrow for the record that you added, click or tap the pencil icon to edit the record, update one or more fields, and then click or tap the cancel icon to discard your changes.

1. Click or tap the next arrow for the record that you added, and then click or tap the trash icon to delete that record.

## Next steps
Customize the default browse screen to better suit your needs. For example, you can sort and filter the list by product name, not category.

> [!div class="nextstepaction"]
> [Customize a default browse screen](customize-layout-sharepoint.md).