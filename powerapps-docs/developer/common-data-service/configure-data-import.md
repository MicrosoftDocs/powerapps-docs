---
title: "Configure data import (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Configuration information that is required for importing data is contained in the data import entity and the import source file entity." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Configure data import

<!-- 
Was Mike Carter's

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/configure-data-import 

Child topic of 
powerapps-docs/developer/common-data-service/import-data.md
-->

The configuration information that is required for importing data is contained in the data import (`Import`) entity and the import source file (`ImportFile`) entity.  
  
 To configure data import, do the following:  
  
- Use the `Import.ModeCode` attribute to specify whether to create or update data during import. If you are using early bound types, you can use the `ImportModeCode` enumeration. For a list of the ModeCode values, see the picklist values for this entity. To view the entity metadata for your organization, install the Metadata Browser solution described in [Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata). You can also browse the reference documentation for entities in the [Entity Reference](/dynamics365/customer-engagement/developer/about-entity-reference).  
  
- Use the `ImportFile.FileTypeCode` attribute to specify the type of the import file. If you are using early bound types, you can use the `ImportFileType` enumeration. For a list of the FileTypeCode values, see the picklist values for this entity.  
  
- Use the `ImportFile.DataDelimiterCode` attribute to specify the single character data delimiter in the import file. If you are using early bound types, you can use the `ImportDataDelimiter` enumeration. For a list of the ImportDataDelimiter values, see the picklist values for this entity.  
  
- Use the `ImportFile.FieldDelimiterCode` attribute to specify the single character field delimiter in the import file. If you are using early bound types, you can use the `ImportFieldDelimiter` enumeration. For a list of the FieldDelimiterCode values, see the picklist values for this entity.  
  
- Set `ImportFile.IsFirstRowHeader` to `true` to indicate that the first row in the source file contains column headings or to `false` to indicate that the first row contains actual data. If set to `false`, default column headings are generated.  
  
- Set `ImportFile.ImportId` to the ID of the import (data import) that the import file is associated with.  
  
- Set `ImportFile.ImportMapId` to the ID of the associated import map (data map).  
  
- Set `ImportFile.EnableDuplicateDetection` to `true` to enable duplicate detection during data import.  
  
- Read the content of the source file into the `ImportFile.Content`.  
  
> [!IMPORTANT]
>  We do not recommend updating records by using data import programmatically. To update, use the data export and import capabilities of the CDS for Apps Web application. Use **Export to Excel** to export records to an XML Spreadsheet 2003 (.xml) file. This is the only valid source file type for the Update mode. Re-importing data from the XML Spreadsheet 2003 (.xml) source file ensures that the data integrity in CDS for Apps is maintained. To import updated data, use the CDS for Apps Import Data Wizard. For more information about the Import Data Wizard, see CDS for Apps Help.  
 
### See Also

[Import data](import-data.md)<br />
[Blog Post: How to Import attachments programmatically](http://blogs.msdn.com/b/crm/archive/2012/08/06/how-to-import-attachments-programmatically.aspx)<br />
[Prepare source files for import](prepare-source-files-import.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import entities](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />