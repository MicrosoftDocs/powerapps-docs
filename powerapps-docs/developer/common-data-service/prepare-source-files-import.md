---
title: "Prepare source files for import (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Data import supports source files formatted as comma-separated values (.csv), XML Spreadsheet 2003 (.xml), or text files." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
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

Before you can import data into Common Data Service(CDS) for Apps, you must create the source data files.  
  
The data source files that you use in an import must be formatted as comma-separated values (.csv), XML Spreadsheet 2003 (.xml), or text files. The use of source files enables the transfer of data from database systems that use different formats into CDS for Apps.  
  
A source file may contain data for one entity type or multiple entity types, such as accounts and contacts. For the source files that contain multiple entity data, you must provide a map that includes the `<EntitiesPerFile>` tag. Set the value of this tag to “Multiple” to indicate that there is more than one entity type in the source file. Add the `Dedupe = “Eliminate”` attribute to the `<EntityMap>` tag. This assures that if the file contains duplicate rows for the entity type, a single row is used to minimize lookup related errors.  
  
You can download an example of a data map with multiple entity types from [Microsoft Downloads: DataImportMaps.zip](http://download.microsoft.com/download/D/5/F/D5F73E15-439B-4EBC-BFFB-C6837B146C76/DataImportMaps.zip). Look at the `MapForSalesForceContactAccount.xml` file.  
  
 The field values in the source file can be separated by commas, tabs, or other characters that are defined in the `ImportFile.FieldDelimiterCode` attribute.  
  
> [!NOTE]
>  Do not use non-printable characters, **null** (\0) or break (\b), as delimiters for the field values.  
  
 The first row in the source file should contain column headings. If you do not include headings, use the `ImportFile.IsFirstRowHeader` attribute to specify that the first row represents actual data. In this case, default column headings are created with the names Col1, Col2, and so on.  

### See Also

[Import data](import-data.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import entities](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />