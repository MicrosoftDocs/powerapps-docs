---
title: "Troubleshoot export to Excel | MicrosoftDocs"
description: "Troubleshoot export to Excel."
ms.date: 06/30/2020
ms.service:
  - "dynamics-365-sales"
ms.topic: article
author: udaykirang
ms.author: udag
manager: shujoshi
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

4. Select **Go**.

    > [!div class="mx-imgBorder"]
    > ![Error message](media/ts-e2e-error-message.png "Error message")

5. In the error message that appears, select **OK**, and then select **Import**.

6. Close the **Edit Web Query** window, and refresh the data.
