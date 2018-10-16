---
title: "Export data to Excel in PowerApps | MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 10/16/2018
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
  - D365CE
---
---
# Export data to Excel

Do you need to analyze your data from PowerApps and convert that data into actionable items that help you drive more sales? Now you can do this when you export your data to Excel or Excel Online to do a quick data analysis. Also, analyzing large datasets is not a problem because you can export up to 100,000 rows of data.
  
You can choose to export static worksheets or dynamic worksheets, which you can import back into PowerApps. If you need more advanced functions, you can export a dynamic PivotTable, which makes it very easy to organize and summarize dataa.  
  
Export data to a standard Excel file that that you can use on any device such as your phone, tablet, or desktop computer. The data is exported in the same format as you see in PowerApps. Text will remain text, numbers will remain numbers, and dates will remain dates. However, when you export data from PowerApps to Excel the some cell format may change. The table below summarizes how you’ll see the data in PowerApps and how the cell format changes when you export the data to Excel.  
  
## Cell format when data is exported from PowerApps
  
| Data format in PowerApps |                                            Cell format in Excel                                             |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Text, Ticker Symbol, Phone, Options set, and Look Up            |                                                       Shows as Text and option set becomes drop-down list                                                       |
|                                 Email, URL                                 |                                                                        Shows as General                                                                         |
|                                   Number                                   |                                                             Shows as Number without group separator                                                             |
|                                  Currency                                  |                                                         Shows as Number and does not include “$” symbol                                                         |
|                          Date only, Date and Time                          |                                                                       Shows as Date only                                                                        |
|                       Calculated and Roll up fields                        | Editable in Excel but can’t be imported back to PowerApps |
|                               Secured fields                               | Editable in Excel but can’t be imported back to PowerApps |
  
## See which type of export works best for you  
  
|                                                                                                               Task                                                                                                                |                                              Learn more                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
|   Do an *ad-hoc* or *what if* analysis without modifying PowerApps data. Or, quick bulk edit to multiple records.   | [Export to Excell Online ](export-to-excel-online.md) |
|                                                                   Get a snapshot of the data at the current data and time or you want to share it with others.                                                                    |           [Export to an Excel static worksheet](export-excel-static-worksheet.md)           |
| Get the most update-to-date information and be able to refresh it in Excel and match what you see in PowerApps at any time. |          [Export to an Excel dynamic worksheet](export-excel-dynamic-worksheet.md)          |
|                                                                      View PowerApps data in a pivot table.                                                                      |                 [Export to an Excel PivotTable](export-excel-pivottable.md)                 |



- When you export data in Excel (.xlsx format) and then add or modify columns, you can’t import the data back in to Dynamics 365. This is not supported for .xlsx file format.  
  
- If you’re using Excel 2010, you may get this error message when you export data from Accounts area: 
 
      “The file is corrupt and cannot be opened.”  
  
   The error message occurs due to a setting in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)]. To fix the issue, do this:  
  
  1. Open [!INCLUDE[pn_ms_Excel_2010_short](../includes/pn-ms-excel-2010-short.md)]  
  
  2. Go to **File** > **Options**.  
  
  3. Go to **Trust Center** > **Trust center settings**.  
  
  4. Click **Protected view**. Then clear the check boxes for the first two options.  
  
  5. Click **OK** and then close the **Options** dialog box.  
  

