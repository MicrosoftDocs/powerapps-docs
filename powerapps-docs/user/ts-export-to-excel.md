---
title: Troubleshoot export to Excel  | Microsoft Docs
description: Troubleshoot export to Excel
author: udaykirang
manager: shujoshi
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 06/30/2020
ms.author: udag
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Troubleshoot export to Excel

## Data disappears after I refresh the exported dynamic Excel file

**Problem**

After I use the **Export to Excel** command to export a file to my local computer, I open the file and select **Refresh All** under **Data**. The data disappears and workbook appears blank.

**Resolution**

This issue occurs when the data that you're accessing is password-protected and the Excel file can't submit passwords to external data sources. To resolve this issue, you must edit and save the web query.

1. In the Excel file, select **Data** > **Queries and Connections**.

    > [!div class="mx-imgBorder"]
    > ![Select Data, and then select Queries and Connections](media/ts-e2e-select-queries-connections.png "Select Data, and then select Queries and Connections")

    The **Queries & Connections** pane opens on the right of the window.

    > [!div class="mx-imgBorder"]
    > ![Queries and Connections pane](media/ts-e2e-queries-connections-pane.png "Queries and Connections pane")

2. On the **Connections** tab, right-click to select the **Query_from_Microsoft_CRM** query, and then select **Properties**.

    > [!div class="mx-imgBorder"]
    > ![Select Properties](media/ts-e2e-select-properties-from-query.png "Select Properties")

    The **Connection Properties** window opens.

3. On the **Definition** tab, select **Edit Query**.

    > [!div class="mx-imgBorder"]
    > ![Select edit query](media/ts-e2e-select-edit-query.png "Select edit query")

4. When prompted, enter username and password.   

5. If the following error message appears, close the **Edit Web Query** window.   

    > [!div class="mx-imgBorder"]
    > ![Error message](media/ts-e2e-error-message.png "Error message")    

6. Refresh the data in Excel.


[!INCLUDE[footer-include](../includes/footer-banner.md)]