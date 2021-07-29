---
title: "Format conversions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about File columns that store file data within the application, supporting columns, retrieving data, and uploading file data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/30/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.topic: "article"
author: "nkrb" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Format Validations

In the past, it was possible to configure incompatible formats for data types by making direct XML modifications. These modifications could then be packed in a solution, which when deployed, would set incompatible formats for data types in the import environment. These could result in unexpected issues within clients or even outright failure of apps, workflows or other applications. To prevent this, format validations will occur on both API operations and Solution Imports.

## API operations (Update and Retrieve)

As noted in the [API Behavior section](#api-behavior), performing a Retrieve or Update will update the format values if the requesting user has permissions to
edit the columns.

- Retrieving a format for a data type will result in incompatible formats being changed to the default of “text” in the response.

- If the Update call uses the response from Retrieve, the corrected format will be included and will be written to the active layer.

## Solution Import

A solution import that includes format values on data types will fail in the following instances:

- A solution attempts to add a new column into a table that includes an invalid format for the data type

- A solution is imported that contains a column with an invalid format for a data type for a column that already exists in the top layer of the installed solution.

In the second scenario if your current top layer solution has a column that includes a data type with an invalid format, the import will be successful, until the top layer’s incompatible format is updated.

If your solution is failing because of an invalid format, you can perform the retrieve and update process in the source org to fix the invalid format and then repackage the solution.

### Related articles

[Data type format conversions](data-type-format-conversions.md)

[Format and FormatName columns](format-and-formatname-columns.md)