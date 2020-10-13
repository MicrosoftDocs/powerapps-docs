---
title: "Export data to Excel in Power Apps | MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 07/09/2020
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
# Export data to Excel

Do you need to analyze your data from and convert that data into actionable items that help you drive more sales? Now you can do this when you export your data to Excel or Excel Online. Also, analyzing large datasets is not a problem because you can export up to 100,000 rows of data.
  
You can choose to export static worksheets or dynamic worksheets, which you can import back in to the app. If you need more advanced functions, you can export a dynamic PivotTable, which makes it very easy to organize and summarize data.  
  
You can export data to a standard Excel file that you can use on any device such as your phone, tablet, or desktop computer. The data is exported in the same format that you see in the app. Text will remain text, numbers will remain numbers, and dates will remain dates. However, when you export data from the app to Excel, some cell formats might change. The following table summarizes how you’ll see the data in apps and how the cell format changes when you export the data to Excel.  
  
## Cell format when data is exported from model-driven apps
  
| Data format in model-driven apps |                                            Cell format in Excel                                             |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Text, Ticker Symbol, Phone, Options set, and Look Up            |                                                       Shows as Text and option set becomes drop-down list                                                       |
|                                 Email, URL                                 |                                                                        Shows as General                                                                         |
|                                   Number                                   |                                                             Shows as Number without group separator                                                             |
|                                  Currency                                  |                                                         Shows as Number and does not include dollar sign ($)                                                         |
|                          Date only, Date and Time                          |                                                                       Shows as Date only                                                                        |
|                       Calculated and Roll-up fields                        | Editable in Excel but can’t be imported back to Power Apps |
|                               Secured fields                               | Editable in Excel but can’t be imported back to Power Apps |
  
## See which type of export works best for you  
  
|                                                                                                               Task                                                                                                                |                                              Learn more                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
|   Do an *ad-hoc* or *what if* analysis without modifying app data. Or, quick bulk edit to multiple records.   | [Export to Excel Online](export-to-excel-online.md) |
|                                                                   Get a snapshot of the data at the current data and time or you want to share it with others.                                                                    |           [Export to an Excel static worksheet](export-excel-static-worksheet.md)           |
| Get the most up-to-date information and be able to refresh it in Excel and match what you see in the app at any time. |          [Export to an Excel dynamic worksheet](export-excel-dynamic-worksheet.md)          |
|                                                                      View app data in a pivot table.                                                                      |                 [Export to an Excel PivotTable](export-excel-pivottable.md)                 |



When you export data in Excel (.xlsx format) and then add or modify columns, you can’t import the data back into Dynamics 365. This is not supported for the .xlsx file format.  
  
If you’re using Excel 2010, you might get this error message when you export data from the Accounts area: 
 
`The file is corrupt and cannot be opened.`  
  
The error message occurs due to a setting in Excel. To fix the issue, do this:  
  
1. Open Excel 2010.  
  
2. Go to **File** > **Options**.  
  
3. Go to **Trust Center** > **Trust Center settings**.  
  
4. Select **Protected view** and then clear the check boxes for the first two options.  
  
5. Select **OK** and then close the **Options** dialog box.  

## Limit the number of records that can be exported to Excel using Web API

Update the `maxrecordsforexporttoexcel` attribute of the Organization entity using the Web API.

## Example

The Web API request given below will set the value of `maxrecordsforexporttoexcel` attribute to 100.

```html
PUT [Organization URI]/api/data/v9.1/organizations(df617a54-bc85-48bf-a4f2-3c4208a405e1)
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0 

{
    "maxrecordsforexporttoexcel": 100
}
```

> [!NOTE]
> The default value of `maxrecordsforexporttoexcel` attribute is 100000. If the value of `maxrecordsforexporttoexcel` attribute is increased to more than 100000, then timeouts may occur and export may fail. It is recommended to split the records into multiple views and then upload.

### See also

[Troubleshoot export to excel](ts-export-to-excel.md)  
