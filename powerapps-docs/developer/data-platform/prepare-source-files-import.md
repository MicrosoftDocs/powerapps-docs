---
title: "Prepare source files for import (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Data import supports source files formatted as comma-separated values (.csv), XML Spreadsheet 2003 (.xml), or text files." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/15/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Prepare source files for import

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Before you can import data into Microsoft Dataverse, you must create the source data files.  
  
The data source files that you use in an import must be formatted as comma-separated values (.csv), XML Spreadsheet 2003 (.xml), or text files. The use of source files enables the transfer of data from database systems that use different formats into Dataverse.  
  
A source file may contain data for one table or multiple tables, such as accounts and contacts. For the source files that contain multiple table data, you must provide a map that includes the `<EntitiesPerFile>` tag. Set the value of this tag to “Multiple” to indicate that there is more than one table type in the source file. Add the `Dedupe = “Eliminate”` column to the `<EntityMap>` tag. This assures that if the file contains duplicate rows for the table type, a single row is used to minimize lookup related errors.  
  
You can download an example of a data map with multiple table types from [Microsoft Downloads: DataImportMaps.zip](https://download.microsoft.com/download/D/5/F/D5F73E15-439B-4EBC-BFFB-C6837B146C76/DataImportMaps.zip). Look at the `MapForSalesForceContactAccount.xml` file.  
  
 The column values in the source file can be separated by commas, tabs, or other characters that are defined in the `ImportFile.FieldDelimiterCode` column.  
  
> [!NOTE]
>  Do not use non-printable characters, **null** (\0) or break (\b), as delimiters for the column values.  
  
 The first row in the source file should contain column headings. If you do not include headings, use the `ImportFile.IsFirstRowHeader` column to specify that the first row represents actual data. In this case, default column headings are created with the names Col1, Col2, and so on.  

### See Also

[Import data](import-data.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import tables](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]