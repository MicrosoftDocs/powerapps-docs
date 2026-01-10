---
title: "Format validations (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to validate format conversions in Microsoft Dataverse." 
ms.date: 06/15/2022
ms.reviewer: jdaly
ms.topic: article
author: mkannapiran
ms.author: kamanick
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Format validations

You may have configured incompatible formats for data types in the past by directly making changes in the XML file. When these changes are packaged into a solution and imported into an environment, you may see unexpected issues or failures of apps, workflows, or other applications. To prevent this, format validations are introduced for both API operations and Solution imports.

## API operations (Update and Retrieve)

Performing a retrieve or update operation updates the format values if you have permission to change the columns. More information:

- Retrieving a format for a data type results in incompatible formats being changed to the default of "text" in the response.
- If the update operation uses the response from retrieve, the corrected format will be included and will be written to the active layer.

## Solution import

When you import solutions that include format values on data types, will fail in the following scenarios:

- When you create a solution and attempt to add a new column to a table that includes an invalid format for the data type.
- When a solution is imported that contains a column with an invalid format for the data type for a column that already exists in the installed solution.

In the second scenario, if your installed solution has a column that includes a data type with an invalid format, the import will be successful until the columns' incompatible format is updated in the installed solution.

Suppose your solution is failing because of an invalid format. In that case, you can perform the retrieve and update process in the source org to fix the invalid format and then repackage the solution.

### Related articles

[Data type format conversions](data-type-format-conversions.md)<br />
[Format and FormatName columns](format-and-formatname-columns.md)
