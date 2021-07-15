---
title: Format a table in Excel and naming tips
description: Learn about how to format a table in an Excel file to use the table as the source of data while building a canvas app.
author: yifwang
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 04/03/2018
ms.subservice: canvas-maker
ms.author: yifwang
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Format a table in Excel and naming tips
In Power Apps, you can create a canvas app based on Excel data only if it's formatted as a table. By following this content, you'll learn how to format a table in Excel and some tips of naming Excel columns.

## How to format a table in Excel
You can convert your data to a table by selecting **Format as Table** in the **Home** tab of Excel.

![Excel format a table.](./media/how-to-excel-tips/format-table.png)

You can also create a table by selecting **Table** on the **Insert** tab.

![Excel insert a table.](./media/how-to-excel-tips/insert-table.png)

To find your table easily, go to **Design** under **Table Tools**, and rename your table. It's useful to give your table a meaningful name, especially when the same Excel file contains more than one table.

![Excel rename a table.](./media/how-to-excel-tips/rename-table.png)

## Naming tips in Excel
If a column in your table contains images, include "image" in the name of that column. This keyword will bind that column to an image control in a gallery.

![Connect Excel table with images.](./media/how-to-excel-tips/connect-gallery.png)

## Next steps
* [Generate an app from Excel in Power Apps](get-started-create-from-data.md) based on a table that you specify. The app will have three screens by default: one each for browsing records, displaying details about a single record, and creating or updating a record.
* [Create an app from scratch](get-started-create-from-blank.md) using the table you format in Excel. You can manually create and customize your app to display, browse, or edit the data in your table.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]