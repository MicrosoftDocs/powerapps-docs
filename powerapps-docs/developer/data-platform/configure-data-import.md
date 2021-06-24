---
title: "Configure data import (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Configuration information that is required for importing data is contained in the data import table and the import source file table." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Configure data import

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

<!-- 
Was Mike Carter's

https://docs.microsoft.com/dynamics365/customer-engagement/developer/configure-data-import 

Child topic of 
powerapps-docs/developer/data-platform/import-data.md
-->

The configuration information that is required for importing data is contained in the data import (`Import`) table and the import source file (`ImportFile`) table.  
  
 To configure data import, do the following:  
  
- Use the `Import.ModeCode` column to specify whether to create or update data during import. If you are using early bound types, you can use the `ImportModeCode` enumeration. For a list of the ModeCode values, see the choice values for this table. To view the metadata for your organization, install the Metadata Browser solution described in [Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata). You can also browse the reference documentation for tables in the [Table Reference](/dynamics365/customer-engagement/developer/about-entity-reference).  
  
- Use the `ImportFile.FileTypeCode` column to specify the type of the import file. If you are using early bound types, you can use the `ImportFileType` enumeration. For a list of the FileTypeCode values, see the choice values for this table.  
  
- Use the `ImportFile.DataDelimiterCode` column to specify the single character data delimiter in the import file. If you are using early bound types, you can use the `ImportDataDelimiter` enumeration. For a list of the ImportDataDelimiter values, see the choice values for this table.  
  
- Use the `ImportFile.FieldDelimiterCode` column to specify the single character column delimiter in the import file. If you are using early bound types, you can use the `ImportFieldDelimiter` enumeration. For a list of the FieldDelimiterCode values, see the choice values for this table.  
  
- Set `ImportFile.IsFirstRowHeader` to `true` to indicate that the first row in the source file contains column headings or to `false` to indicate that the first row contains actual data. If set to `false`, default column headings are generated.  
  
- Set `ImportFile.ImportId` to the ID of the import (data import) that the import file is associated with.  
  
- Set `ImportFile.ImportMapId` to the ID of the associated import map (data map).  
  
- Set `ImportFile.EnableDuplicateDetection` to `true` to enable duplicate detection during data import.  
  
- Read the content of the source file into the `ImportFile.Content`.  
  
> [!IMPORTANT]
>  We do not recommend updating records by using data import programmatically. To update, use the data export and import capabilities of the Microsoft Dataverse Web application. Use **Export to Excel** to export records to an XML Spreadsheet 2003 (.xml) file. This is the only valid source file type for the Update mode. Re-importing data from the XML Spreadsheet 2003 (.xml) source file ensures that the data integrity in Dataverse is maintained. To import updated data, use the Dataverse Import Data Wizard. For more information about the Import Data Wizard, see Dataverse Help.  
 
### See Also

[Import data](import-data.md)<br />
[Blog Post: How to Import attachments programmatically](https://blogs.msdn.com/b/crm/archive/2012/08/06/how-to-import-attachments-programmatically.aspx)<br />
[Prepare source files for import](prepare-source-files-import.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import tables](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]