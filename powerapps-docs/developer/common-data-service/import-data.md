---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Import data

<!--
Was Mike Carter


https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/import-data



This should be the generic high-level content to support either web api or org service

Should there be a separate topic for organization service and Web API?
All these functions & actions exist:

RetrieveParsedDataImportFile Function
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/retrieveparseddataimportfile?view=dynamics-ce-odata-9
GetDistinctValuesImportFile Function
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/getdistinctvaluesimportfile?view=dynamics-ce-odata-9
ParseImport Function
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/parseimport?view=dynamics-ce-odata-9
TransformImport Action
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/transformimport?view=dynamics-ce-odata-9
ImportRecordsImport Action
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/importrecordsimport?view=dynamics-ce-odata-9
ExportMappingsImportMap Action
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/exportmappingsimportmap?view=dynamics-ce-odata-9
ImportMappingsImportMap Action
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/web-api/importmappingsimportmap?view=dynamics-ce-odata-9

Or should the core general content simply include both?

-->
If you want to import data into Common Data Service for Apps, you can use the *data import* feature. Data import lets you upload data from various customer relationship management systems and data sources into CDS for Apps. You can import data into standard and customized attributes of most business and custom entities. You can also include related data, such as notes and attachments.  
  
Common Data Service for Apps includes a web application tool called Import Data Wizard. You use this tool to import data records from one or more comma-separated values (.csv), XML Spreadsheet 2003 (.xml), or text files.  
  
 For more information about the Import Data Wizard, see CDS for Apps Help.  
  
 The Common Data Service for Apps web services provide the following additional capabilities that aren’t available in the Import Data Wizard:  
  
- Create data maps that include complex transformation mapping, such as concatenation, split, and replace.  
  
- Define custom transformation mapping.  
  
- View source data that is stored inside the temporary parse tables.  
  
- Access error logs to build custom error reporting tools with improved error logging views.  
  
- Run data import by using command-line scripts.  
  
- Add `LookupMap`XML tags in the data map to indicate that the data lookup will be initiated and performed on a source file that is used in the import.  
  
- Add custom `OwnerMetadata`XML tags in the data map to match the user records in the source file with the records of the user (system user) in CDS for Apps.  
  
- Use optional validation checks.  
  
  > [!NOTE]
  >  Validation isn’t optional in the Import Data Wizard.  
  
  To implement data import, you typically do the following:  
  
- Create a comma-separated values (CSV), XML Spreadsheet 2003 (XMLSS), or text source file.  
  
- Create a data map or use an existing data map.  
  
- Associate an import file with a data map.  
  
- Upload the content from a source file to the associated import file.  
  
- Parse the import file.  
  
- Transform the parsed data.  
  
- Upload the transformed data into the target CDS for Apps server.  
  
  You can import data from one source file or several source files. A source file can contain data for one entity type or multiple entity types.  
  
  Parsing, transforming, and uploading of data is done by the asynchronous jobs that run in the background.  
  
> [!NOTE]
>  By default, all custom entities are enabled for import. To determine if a business entity is enabled for import, see the entity metadata for the specific entity. If an entity is enabled for import, the entity metadata property `IsImportable` is set to `true`. The value of this property can’t be changed for the out-of-the-box business entities. [!INCLUDE[metadata_browser](../includes/metadata-browser.md)]  


### See Also

[Prepare source files for import](prepare-source-files-import.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import entities](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />
