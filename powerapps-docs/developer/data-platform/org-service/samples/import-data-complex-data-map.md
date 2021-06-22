---
title: "Sample: Import data using complex data map (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create new records by using data import" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Import data using complex data map

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to create new records by using data import. The sample uses a complex data map. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ImportComplexDataMap).

>[!NOTE]
> The source data for this sample is contained in the following file `ImportComplexDataMap\import accounts.csv`

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## How this sample works

In order to simulate the scenario described above, the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `ImportMap` method creates an import map.
1. The `ColumnMapping` method creates a column mapping for a `text` type column.
1. The `EntityReference` method relates the column mapping with the data map.
1. The `LookUpMapping` method creates a lookup mapping to the parent account.
1. The `ImportFile` method creates a import file.
1. The `GetHeaderColumnsImportFileRequest` method retrieves the header columns used in the import file.
1. The `ParseImportRequest` method parses the import file. 
1. The `RetrievedParsedDataImportFileRequest` method retrieves the data from the parse table.
1. The `TransformImportRequest` method transforms the import.


### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


### See Also

[Import data](../../import-data.md)<br />
[Prepare source files for import](../../prepare-source-files-import.md)<br />
[Create data maps for import](../../create-data-maps-for-import.md)<br />
[Add transformation mappings for import](../../add-transformation-mappings-import.md)<br />
[Configure data import](../../configure-data-import.md)<br />
[Run data import](../../run-data-import.md)<br />
[Data import tables](../../data-import-entities.md)<br />
[Sample: Export and import a data map](export-import-data-map.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]