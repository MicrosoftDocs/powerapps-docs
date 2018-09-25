---
title: "Export data to Excel (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 09/15/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 7505920c-fb5b-4794-acdb-110e307f0ffe
caps.latest.revision: 41
author: "jimholtz"
ms.author: "jimholtz"
manager: "brycho"
search.audienceType: 
  - enduser
search.app: 
  - D365CE
---
# Export data to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)]

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

Do you need to analyze your data from [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] and convert that data into actionable items that help you drive more sales?  Now you can do this when you export your data to [!INCLUDE[pn_microsoft_excel](../includes/pn-microsoft-excel.md)] or [!INCLUDE[pn_excel_online](../includes/pn-excel-online.md)] to do a quick data analysis. Also, analyzing large datasets is not a problem because you can export up to 100,000 rows of data.  
  
 You can choose to export static worksheets or dynamic worksheets, which you can import back into [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]. If you need more advanced functions, you can export a dynamic PivotTable, which makes it very easy to organize and summarize data.  
  
 Export data to a standard [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] file that that you can use on any device such as your phone, tablet, or desktop computer. The data is exported in the same format as you see in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]. Text will remain text, numbers will remain numbers, and dates will remain dates. However, when you export data from [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] the some cell format may change. The table below summarizes how you’ll see the data in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] and how the cell format changes when you export the data to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)].  
  
## Cell format when data is exported from [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] to [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)]  
  
| Data format in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] |                                            Cell format in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)]                                             |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Text, Ticker Symbol, Phone, Options set, and Look Up            |                                                       Shows as Text and option set becomes drop-down list                                                       |
|                                 Email, URL                                 |                                                                        Shows as General                                                                         |
|                                   Number                                   |                                                             Shows as Number without group separator                                                             |
|                                  Currency                                  |                                                         Shows as Number and does not include “$” symbol                                                         |
|                          Date only, Date and Time                          |                                                                       Shows as Date only                                                                        |
|                       Calculated and Roll up fields                        | Editable in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] but can’t be imported back to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] |
|                               Secured fields                               | Editable in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] but can’t be imported back to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] |
  
## See which type of export works best for you  
  
|                                                                                                               Task                                                                                                                |                                              Learn more                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
|   Do an *ad-hoc* or *what if* analysis without modifying [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data. Or, quick bulk edit to multiple [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] records.   | [Analyze your Dynamics 365 data in Excel Online](analyze-dynamics-365-data-excel-online.md) |
|                                                                   Get a snapshot of the data at the current data and time or you want to share it with others.                                                                    |           [Export to an Excel static worksheet](export-excel-static-worksheet.md)           |
| Get the most update-to-date information and be able to refresh it in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] and match what you see in [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] at any time. |          [Export to an Excel dynamic worksheet](export-excel-dynamic-worksheet.md)          |
|                                                                      View [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] data in a pivot table.                                                                      |                 [Export to an Excel PivotTable](export-excel-pivottable.md)                 |

## Other considerations

- When you export data in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)] (.xlsx format) and then add or modify columns, you can’t import the data back in to [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]. This is not supported for .xlsx file format.  
  
- If you’re using [!INCLUDE[pn_ms_Excel_2010_short](../includes/pn-ms-excel-2010-short.md)], \ you may get this error message when you export data from Accounts area: 
 
      “The file is corrupt and cannot be opened.”  
  
   The error message occurs due to a setting in [!INCLUDE[pn_Excel_short](../includes/pn-excel-short.md)]. To fix the issue, do this:  
  
  1. Open [!INCLUDE[pn_ms_Excel_2010_short](../includes/pn-ms-excel-2010-short.md)]  
  
  2. Go to **File** > **Options**.  
  
  3. Go to **Trust Center** > **Trust center settings**.  
  
  4. Click **Protected view**. Then clear the check boxes for the first two options.  
  
  5. Click **OK** and then close the **Options** dialog box.  
  
## Community tools 

**Export to Excel** is a tool provided by the XrmToolbox community developed for [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] Customer Engagement. See the [Developer tools](../developer/developer-tools.md) topic for community developed tools.

> [!NOTE]
> The community tools are not a product of [!include[pn_microsoft_dynamics](../includes/pn-microsoft-dynamics.md)] and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com). 
  
## Privacy notice  
[!INCLUDE[cc_privacy_export_to_excel](../includes/cc-privacy-export-to-excel.md)]

### See also  
 [Analyze your data with Excel templates](../admin/analyze-your-data-with-excel-templates.md)   
 [Analyze with Excel Online](analyze-dynamics-365-data-excel-online.md)   
 [Export to Excel PivotTable](export-excel-pivottable.md)   
 [Export to Excel static worksheet](export-excel-dynamic-worksheet.md)   
