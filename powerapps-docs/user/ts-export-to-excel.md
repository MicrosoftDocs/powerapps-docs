---
title: "Troubleshoot export to excel | MicrosoftDocs"
description: "Troubleshoot export to excel."
ms.date: 06/26/2020
ms.service:
  - "dynamics-365-sales"
ms.topic: article
author: udaykirang
ms.author: udag
manager: shujoshi
---

# Troubleshooting export to excel

## Data disappears after I refresh the imported Excel file

**Problem**

After I export the Excel file through **Export to Excel** to my local computer, I open the file and select **Refresh All** under **Data**, the data disappears and worksheet appears blank.

**Resolution**

This issue occurs when the data that you're accessing is password protected and Excel file can’t submit passwords to external data sources. To resolve this issue, you must edit and save the Web query. Follow these steps:

1.	On the Excel file, select **Data** > **Queries and Connections**.

    > [!div class="mx-imgBorder"]
    > ![Select data and then select Queries and Connections](media/ts-e2e-select-queries-connections.png "Select data and then select Queries and Connections")
     
    The **Queries & Connections** pane opens on the right of the window.

    > [!div class="mx-imgBorder"]
    > ![Queries and Connections pane](media/ts-e2e-queries-connections-pane.png "Queries and Connections pane")

2.	In the **Connection** tab, right-click the **Query_from_Microsoft_CRM** query and then select **Properties**.

    > [!div class="mx-imgBorder"]
    > ![Select properties](media/ts-e2e-select-properties-from-query.png "Select properties")
 
    The **Connection Properties** window opens.

3.	Go to **Definition** tab and select **Edit Query**.

    > [!div class="mx-imgBorder"]
    > ![Select edit query](media/ts-e2e-select-edit-query.png "Select edit query")
 
    The **Edit Web Query** window opens.

4.	Select **Go** and the following error message displays.

    > [!div class="mx-imgBorder"]
    > ![Error message](media/ts-e2e-error-message.png "Error message")
 
5.	Select **Ok** and then select **Import**.

6.	Close the **Edit Web Query** window and refresh the data.




