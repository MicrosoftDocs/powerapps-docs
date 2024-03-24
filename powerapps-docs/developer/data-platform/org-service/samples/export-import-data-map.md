---
title: "Sample: Export and import data map (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a data map and export it" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/24/2022
ms.reviewer: "pehecke"

ms.topic: sample
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType:
  - developer
---

# Sample: Export and import a data map

This sample shows how to create an import map (data map) in Microsoft Dataverse, export it as an XML formatted data, import modified mappings, and create a new import map for Dataverse based on the imported mappings.

> [!div class="nextstepaction"]
> [SDK for .NET: Export and import a data map sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/ExportImportDataMap)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

See the text description in the [Setup](#setup) section as the program's primary functionality is performed during setup.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateImportMapping` method creates the import mapping record.
3. The `RetrieveMappingXML` method exports the mapping (Xml) that is created.
4. The `ChangeMappingName` method parses the Xml to change the name column.
5. The `ImportMappingsByXml` method creates a mapping from the (previously exported) Xml.

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
