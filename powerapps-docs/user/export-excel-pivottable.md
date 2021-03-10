---
title: "Export to an Excel PivotTable in model-driven Power Apps| MicrosoftDocs"
description: How to export to an Excel PivotTable in model-driven Power Apps
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 3/9/2021
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
# Export to an Excel PivotTable

You can export app data to an Office Excel PivotTable to see patterns and trends in data. An Excel PivotTable is a great way to summarize, analyze, explore, and present your app data. You can export up to 100,000 rows at a time.  
  
The option to export data to an Excel PivotTable isn’t available in all row types. If you don’t see the option, it’s not available for that row.  
  
1. On the left nav, select a table.
2. On the command bar select the **Export to Excel** menu, and then select **Dynamic PivotTable**.  

   > [!div class="mx-imgBorder"] 
   > ![Export to excel](media/export-excel-pivottable.png "Select export to Excel")
  
3. In the **Select Columns for Pivot Excel** dialog box, select the column settings and then select **Export**.

   > [!div class="mx-imgBorder"] 
   > ![Select Columns and then select export](media/export-excel-pivottable-1.png "Select Columns and then select export")

  
   By default, the **PivotTable Column List** includes only columns that are displayed in the **Select Columns for Pivot Excel** list.  
  
4. When the download is complete, navigate to the location of the downloaded file.
  
   > [!NOTE]
   > When you download a worksheet it should automatically save to your computer. However, if it doesn't then make sure that you save it before you open and edit it. Otherwise, you might get this error message:**Excel cannot open or save any more documents because there is not enough available memory or disk space.**  
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
  
7. Drag the columns from the PivotTable Column List to the PivotTable. For more information, see [Overview of PivotTables and PivotCharts](https://support.microsoft.com/office/overview-of-pivottables-and-pivotcharts-527c8fa3-02c0-445a-a2db-7794676bce96).  
  
## Tips  
  
- Currency values are exported to Excel as numbers. After you complete the export, see the Excel Help topic “Display numbers as currency" to format the data as currency.
  
- The date and time values that you see in the app show up only as Date when you export the file to Excel, but the cell actually shows both the date and time.  
  
- If you’re going to make changes and import the data file back into the app, remember that secured, calculated, and composite columns (such as Full Name) are read-only and can’t be imported into the app. You’ll be able to edit these columns in Excel, but when you import the data back into the app, these columns won’t be updated. If you want to update these columns, such as a contact’s name, it’s recommended that you use that view to export your data, update it in Excel, and import it back to the app for changes.  
  
 


[!INCLUDE[footer-include](../includes/footer-banner.md)]
