---
title: "Sample: Export and import data map (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a data map and export it" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Export and import a data map

<!-- 
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-export-import-data-map 

-->

This sample shows how to create an import map (data map) in Common Data Service for Apps, export it as an XML formatted data, import modified mappings, and create a new import map CDS for Apps based on the imported mappings.

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
4. The `ChangeMappingName` method parse the xml to change the name attribute.

### Clean up

1. Display an option to delete the sample data that is created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.


### See Also

[Import data](../../import-data.md)<br />
[Prepare source files for import](../../prepare-source-files-import.md)<br />
[Create data maps for import](../../create-data-maps-for-import.md)<br />
[Add transformation mappings for import](../../add-transformation-mappings-import.md)<br />
[Configure data import](../../configure-data-import.md)<br />
[Run data import](../../run-data-import.md)<br />
[Data import entities](../../data-import-entities.md)<br />
[Sample: Import data using complex data map](import-data-complex-data-map.md)<br />
