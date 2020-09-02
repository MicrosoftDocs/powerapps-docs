---
title: Analyze tables with Power BI Desktop | Microsoft Docs
description: Explains how analyze Project Oakdale tables with Power BI Desktop.
author: Mattp123
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/01/2020
ms.author: simatthe
ms.reviewer: matp
---

# Analyze table data with Power BI Desktop

You can use Power BI Desktop to view tables in Project Oakdale. The table data that you can access from your environment is read-only.

## View table data

1. Make sure the TDS endpoint setting is enabled for your environment. More information: [Manage feature settings](/power-platform/admin/settings-features)

1. Sign into Teams, and then select the link for **Power Apps**.
   > [!div class="mx-imgBorder"] 
   > ![Sign into Power Apps](media/create-table1.png)

1. Select the **Build** tab, and then select **See all**.
   > [!div class="mx-imgBorder"] 
   > ![The Build tab](media/create-table2.png)

1. Select **Tables** from the left pane, select the table your want, and then on the command bar select **Analyze in Power BI**.

   The pbids file for your environment is downloaded to your browser’s default download folder.

1. Open the .pbids file to access it in Power BI Desktop.

1. The pbids file is loaded in Power BI Desktop. In the **SQL Server database** dialog box, select **Microsoft account**, select **Sign in**, and then in the browser window that appears enter your credentials.

1. In the **SQL Server database** dialog box in Power BI Desktop, select **Connect**.

   The environment appears in the **Power BI Desktop Navigator** window. Expand it to view the tables available to analyze. Select a table to view its data.

### See also
[Create tables in Teams](create-table.md) <br />
[Download Power BI tools and apps](https://powerbi.microsoft.com/downloads/)
