---
title: Generate a canvas app from Excel | Microsoft Docs
description: Use PowerApps to automatically generate a canvas app using an Excel file stored in a cloud-storage account
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 01/14/2019
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Generate a canvas app from Excel in PowerApps

In this topic, you'll automatically generate your first canvas app in PowerApps using data from an Excel table. You'll select an Excel file, generate an app, and then run the app that you generate. Every generated app includes screens to browse records, show record details, and create or update records. By generating an app, you can quickly get a working app using Excel data, and then you can customize the app to better suit your needs. 

The Excel file must be in a cloud-storage account, such as OneDrive, Google Drive, or Dropbox. This topic uses OneDrive for Business.

If you don't have a license for PowerApps, you can [sign up for free](../signup-for-powerapps.md).

## Prerequisites

To follow this topic exactly, download the [Flooring Estimates](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx) file in Excel, and save it in your [cloud storage account](connections/cloud-storage-blob-connections.md).

> [!IMPORTANT]
> You can use your own Excel file, but the data must be formatted as a table. For more information, see [Format a table](how-to-excel-tips.md). 

## Generate the app

1. Sign in to [PowerApps](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. Under **Make your own app**, hover over **Start from data**, and then select **Make this app**.

    ![Option to create an app](./media/get-started-create-from-data/start-from-data.png)

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

    For example, type or paste **Honey** to show the only record for which that string appears in the product's name, category, or overview.

    ![Filter example](./media/get-started-create-from-data/filter-example.png)

1. Add a record:

    1. Select the plus icon.

        ![Plus icon](./media/get-started-create-from-data/plus-icon.png)

    1. Add whatever data you want, and then select the checkmark icon to save your changes.

        ![Save icon](./media/get-started-create-from-data/save-icon.png)

1. Edit a record:

    1. Select the arrow for the record that you want to edit.

        ![Next arrow](./media/get-started-create-from-data/next-arrow.png)

    1. Select the pencil icon.

        ![Pencil icon](./media/get-started-create-from-data/pencil-icon.png)

    1. Update one or more fields, and then select the checkmark icon to save your changes.

        ![Save icon](./media/get-started-create-from-data/save-icon.png)

        As an alternative, select the cancel icon to discard your changes.

1. Delete a record:

    1. Select the next arrow for the record that you want to delete.

        ![Next arrow](./media/get-started-create-from-data/next-arrow.png)

    1. Select the trash icon.

        ![Trash icon](./media/get-started-create-from-data/trash-icon.png)

## Next steps

Customize the default browse screen to better suit your needs. For example, you can sort and filter the list by product name only, not category or overview.

> [!div class="nextstepaction"]
> [Customize a default browse screen](customize-layout-sharepoint.md).
