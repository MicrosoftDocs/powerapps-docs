---
title: "Import Data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to import external data into Microsoft Dataverse. Data import lets you upload data from various customer relationship management systems and data sources into Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/10/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Import data

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

If you want to import data from external sources into Microsoft Dataverse, you can use the *data import* feature. Data import lets you upload data from various customer relationship management systems and data sources into Dataverse. You can import data into standard and customized columns of most business and custom tables. You can also include related data, such as notes and attachments.  
  
Dataverse includes a web application tool called Import Data Wizard. You use this tool to import data rows from one or more comma-separated values (.csv), XML Spreadsheet 2003 (.xml), or text files.  
  
 For more information about the Import Data Wizard, see Dataverse Help.  
  
 The Dataverse web services provide the following additional capabilities that aren’t available in the Import Data Wizard:  
  
- Create data maps that include complex transformation mapping, such as concatenation, split, and replace.  
  
- Define custom transformation mapping.  
  
- View source data that is stored inside the temporary parse tables.  
  
- Access error logs to build custom error reporting tools with improved error logging views.  
  
- Run data import by using command-line scripts.  
  
- Add `LookupMap`XML tags in the data map to indicate that the data lookup will be initiated and performed on a source file that is used in the import.  
  
- Add custom `OwnerMetadata`XML tags in the data map to match the user rows in the source file with the rows of the user (system user) in Dataverse.  
  
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
  
- Upload the transformed data into the target Dataverse server.  
  
  You can import data from one source file or several source files. A source file can contain data for one table type or multiple table types.  
  
  Parsing, transforming, and uploading of data is done by the asynchronous jobs that run in the background.  
  
> [!NOTE]
>  By default, all custom tables are enabled for import. To determine if a business table is enabled for import, see the metadata for the specific table. If the table is enabled for import, the definition property `IsImportable` is set to `true`. The value of this property can’t be changed for the out-of-the-box business tables. <!--[!INCLUDE[metadata_browser](../includes/metadata-browser.md)]-->  


### See Also

[Prepare source files for import](prepare-source-files-import.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import tables](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]