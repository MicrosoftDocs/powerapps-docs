---
title: "Sample: Export and import data map (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a data map and export it" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Export and import a data map

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to create an import map (data map) in Microsoft Dataverse, export it as an XML formatted data, import modified mappings, and create a new import map Dataverse based on the imported mappings. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ExportImportDataMap).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `BulkDeleteRequest` message is intended to be used in a scenario where it contains data that is needed to create the bulk delete request.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org. 
2. The `CreateImportMapping` method creates the import mapping record.
3. The `RetrieveMappingXML` method exports the mapping that is created.
4. The `ChangeMappingName` method parse the xml to change the name column.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


### See Also

[Import data](../../import-data.md)<br />
[Prepare source files for import](../../prepare-source-files-import.md)<br />
[Create data maps for import](../../create-data-maps-for-import.md)<br />
[Add transformation mappings for import](../../add-transformation-mappings-import.md)<br />
[Configure data import](../../configure-data-import.md)<br />
[Run data import](../../run-data-import.md)<br />
[Data import tables](../../data-import-entities.md)<br />
[Sample: Import data using complex data map](import-data-complex-data-map.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]