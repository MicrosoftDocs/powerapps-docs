---
title: "Export to an Excel dynamic worksheet in model-driven Power Apps| MicrosoftDocs"
description: How to export to an Excel dynamic worksheet in model-driven Power Apps
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 3/12/2021
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Export data to an Excel dynamic worksheet

Export your app data to an Excel dynamic worksheet to get the most up-to-date information from your app. When you export your data to an Excel dynamic worksheet and then make changes to your data in the app, you can use the refresh feature in Excel to get the lastest information from the app.

In the example below, we downloaded an Excel dynamic worksheet then went back to the app and changed the **Reserve for days** column from **5** days to **10**. Then opened the Excel worksheet and refreshed the data to get the lastest information from the app.

![Demo of how the Excel to dynamic workseeting feature](media/export-excel-dynamicsworksheet-demo.gif "Demo of how the Excel to dynamic workseeting feature")


You can export up to 100,000 rows at a time. You can’t export data to a dynamic worksheet in Excel for all table. If you don’t see the option for a table, then it’s not available for that table.


If you're a app makeer, you can use the Microsoft Power Apps Excel Add-in to download your app data and make edit in Excel and then save the data back to your app. For more information, see [Open table data in Excel](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-excel-addin).
  
1. On the left nav, select a table.

2. On the command bar select the **Export to Excel** menu and then select **Dynamic Worksheet**.

   > [!div class="mx-imgBorder"] 
   > ![Export to Excel dynamic worksheet](media/open-dynamic-worksheet.png "Select export to Excel dynamic worksheet")
  
3. Select the columns to export and then select **Export**.  

   > [!div class="mx-imgBorder"] 
   > ![Select columns to export](media/open-dynamic-worksheet-1.png "*Select columns to export**")
  
4. When the download is complete, navigate to the location of the downloaded file.
  
   > [!NOTE]
   > When you download a worksheet it should automatically save to your computer. However, if it doesn't then make sure that you save it before you open and edit it. Otherwise, you might get this error message: **Excel cannot open or save any more documents because there is not enough available memory or disk space.**  
   > 
   > To fix the issue:  
   > 
   >    1. Open Excel and go to **File** > **Options** > **Trust Center** **Settings Center Settings** > **Protected View**.  
   >    2. In **Protected View**, clear all three items.  
   >    3. Select **OK** > **OK**.  
   >     
   >    We still strongly recommend that you save and then open the data file rather than disabling protected view, which might put your computer at risk.  
  
5. Open the saved Excel file.
  
6. If you see the security warning **External Data Connections have been disabled**, select **Enable Content**.  

   > [!div class="mx-imgBorder"] 
   > ![Enable content](media/enable-content.png "Enable content") 

7. Go back to your app and update you app data.
8. To see your updates in the Excel dynamics worksheet, in Excel go to **Data** > **Refresh All**.

   > [!div class="mx-imgBorder"] 
   > ![Refresh your app data in Excel](media/refresh-data.png "Refresh your app data in Excel") 
  

## Refresh All doesn't work

After I use the **Export to Excel** command to export a file to my local computer, I open the file and select **Data** . **Refresh All under Data**. The data disappears and workbook appears blank.

This issue occurs when the data that you're accessing is password-protected and the Excel file can't submit passwords to external data sources. To resolve this issue, you must edit and save the web query.

Here's how to resolve it:

1. In the Excel file, select the **Data** tab > **Queries and Connections**.

   > [!div class="mx-imgBorder"] 
   > ![Go to Queries and Connections](media/excel-dynamic-ts-1.png "Go to Queries and Connections") 
   
3. The **Queries & Connections** pane opens on the right of the window. On the **Connections** tab, right-click to select the **Query_from_Microsoft_CRM query** and then select **Properties**.

   > [!div class="mx-imgBorder"] 
   > ![Go connections properties](media/excel-dynamic-ts-2.png "Go connections properties")
   
5. The **Connection Properties** window opens. On **Definition** tab, and then **Edit Query**

   > [!div class="mx-imgBorder"] 
   > ![Go connections properties](media/excel-dynamic-ts-3.png "Go connections properties")

6. When prompted, enter username and password. Enter the same user and password that you use to sign in to your app.

7. Select **GO**.

   > [!div class="mx-imgBorder"] 
   > ![Select Go](media/excel-dynamic-ts-4.png "Select GO")

8. Close the **X** to close window.

   > [!div class="mx-imgBorder"] 
   > ![Close the window](media/excel-dynamic-ts-5.png "Close the window")

9. This should fix the issue. Refresh the data in the worksheet again by going to, **Data** > **Refresh All**. 

   > [!div class="mx-imgBorder"] 
   > ![Refresh your app data in Excel](media/refresh-data.png "Refresh your app data in Excel") 



## Tips  
  
- You can email a dynamic Excel file or store it as a shared file if the recipients are in the same domain as you. When recipients open the dynamic file, only see the data that they have permission to view. 
  
- Some system views can be exported only to a static Excel worksheet.  
  
- Currency values are exported to Excel as numbers. To format the data as currency after you have completed the export, see [Format numbers as currency](https://support.microsoft.com/office/format-numbers-as-currency-0a03bb38-1a07-458d-9e30-2b54366bc7a4).

- The date and time values that you see in the app show up only as Date when you export the file to Excel, but the cell actually shows both the date and time.  
  
- If you’re going to make changes and import the data file back into the app, remember that secured, calculated, and composite columns (such as Full Name) are read-only and can’t be imported into the app. You’ll be able to edit these columns in Excel, but when you import the data back into the app, these columns will not be updated. If you want to update these columns, such as a contact’s name, then it’s recommended that you use that view to export your data, update it in Excel, and import it back to the app for changes. For more information, see [Open table data in Excel](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-excel-addin).

- If you have any issues with dynamic worksheet, see [Troubleshoot export to Excel](ts-export-to-excel.md).  
 



[!INCLUDE[footer-include](../includes/footer-banner.md)]
