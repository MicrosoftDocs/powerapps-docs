---
title: "Export data to Excel in Power Apps | MicrosoftDocs"
description: How to export data to Excel
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 03/08/2021
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
  - D365CE
searchScope:
  - D365-App-msdynce_saleshub
  - D365-Entity-lead
  - D365-UI-View
  - Power Platform
  - Power Apps
---
# Export data to Excel

Export data from your model-driven app to Excel. You can export up to 100,000 rows of data at a time.

1. From the left nav, selet a table that you want to export data from.
2. On the command bar, select **Export to Excel**.

   > [!div class="mx-imgBorder"] 
   > ![Export to excel](media/export_to_excel.png "Select export to Excel")

The data is exported in the same format that you see in your app. Text will remain text, numbers will remain numbers, and dates will remain dates. However, when you export data from your app to Excel, some cell formats might change. The following table summarizes how you’ll see the data in apps and how the cell format changes when you export the data to Excel.  
  
  
| Data format in model-driven apps |                                            Cell format in Excel                                             |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Text, Ticker Symbol, Phone, Options set, and Look Up            |                                                       Shows as Text and option set becomes drop-down list                                                       |
|                                 Email, URL                                 |                                                                        Shows as General                                                                         |
|                                   Number                                   |                                                             Shows as Number without group separator                                                             |
|                                  Currency                                  |                                                         Shows as Number and does not include dollar sign ($)                                                         |
|                          Date only, Date and Time                          |                                                                       Shows as Date only                                                                        |
|                       Calculated and Roll-up columns                        | Editable in Excel but can’t be imported back to Power Apps |
|                               Secured columns                               | Editable in Excel but can’t be imported back to Power Apps |
  
## Export options

You have serveral other export options such as Excel Oline, Static Worksheet, Dynamics Worksheet, or Dynamics PivotTable.

> [!div class="mx-imgBorder"] 
> ![Export to excel options](media/export_to_excel_options.png "Select export to Excel options")


The table below summerizes the different options, pick the one that works best for you.
  
|                                                                                                               Task                                                                                                                |                                              Learn more                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
|   Do an *ad-hoc* or *what if* analysis without modifying app data. Or, quick bulk edit to multiple rows.   | [Open app data in Excel Online](export-to-excel-online.md) |
|                                                                   Get a snapshot of the data at the current date and time or if you want to share the data with others.                                                                    |           [Export to an Excel static worksheet](export-excel-static-worksheet.md)           |
| Get the most up-to-date information and be able to refresh it in Excel and match what you see in your app at any time. |          [Export to an Excel dynamic worksheet](export-excel-dynamic-worksheet.md)          |
|                                                                      View your app data in a pivot table.                                                                      |                 [Export to an Excel PivotTable](export-excel-pivottable.md)                 |


## Tips

- When you export data in Excel (.xlsx format) and then add or modify columns, you can’t import the data back into your app. This is not supported for the .xlsx file format.  
  
- If you’re using Excel 2010, you might get this error message when you export data from the Accounts area: 
 
  `The file is corrupt and cannot be opened.`  
  
  The error message occurs due to a setting in Excel. To fix the issue, do this:  
  
  1. Open Excel 2010 and go to **File** > **Options** > **Trust Center** > **Trust Center settings**.  
  
  2. Select **Protected view** and then clear the check boxes for the first two options.  
  
  35. Select **OK** and then close the **Options** dialog box.  


### See also

[Troubleshoot export to excel](ts-export-to-excel.md)  


[!INCLUDE[footer-include](../includes/footer-banner.md)]
