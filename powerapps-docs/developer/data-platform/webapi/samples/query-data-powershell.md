---
title: "Web API Query Data Sample (PowerShell)"
description: "This sample demonstrates how to query Microsoft Dataverse table rows using the Dataverse Web API with PowerShell and Visual Studio Code."
ms.date: 01/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Web API Query Data Sample (PowerShell)

This PowerShell version 7.4.0 sample demonstrates how to perform various query operations on Microsoft Dataverse table rows using the Dataverse Web API. This sample implements the Dataverse operations and console output detailed in [Web API Query Data Sample](../web-api-query-data-sample.md).

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS/QueryData)

This sample uses the [Dataverse Web API PowerShell Helper functions](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md) to manage authentication and provide reusable functions to perform common operations. These scripts are referenced using [dot sourcing](/powershell/module/microsoft.powershell.core/about/about_scripts#script-scope-and-dot-sourcing) with the following lines:

```powershell
. $PSScriptRoot\..\Core.ps1
. $PSScriptRoot\..\TableOperations.ps1
. $PSScriptRoot\..\CommonFunctions.ps1
```

> [!NOTE]
> This sample should work with Windows, Linux, and macOS, but has only been tested on Windows.

## Prerequisites

Before running this sample, you should read these articles that explain concepts and patterns used by these samples:

- [Quick Start Web API with PowerShell and Visual Studio Code](../quick-start-ps.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](../use-ps-and-vscode-web-api.md)

These articles have the same prerequisites.

[!INCLUDE [cc-visual-studio-code-powershell-prerequisites](../../includes/cc-visual-studio-code-powershell-prerequisites.md)]

## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Open the `QueryData.ps1` file using Visual Studio Code
1. Edit this line to use the URL of the environment you want to connect to:

   `Connect 'https://yourorg.crm.dynamics.com/' # change this`

1. (Optional) Set the `$deleteCreatedRecords` variable to `$false` if you don't want to delete the records this sample creates.
1. Press <kbd>F5</kbd> to run the sample.
1. The first time you run the sample a browser window opens. In the browser window, enter or select the credentials you want to use to authenticate.

To connect as a different user, run the [Disconnect-AzAccount command](/powershell/module/az.accounts/disconnect-azaccount) and try again.

## Code

The code for this sample is at: [PowerApps-Samples/dataverse/webapi/PS/QueryData/QueryData.ps1](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/QueryData/QueryData.ps1)

## Demonstrates

This sample has 11 regions:

### Section 0: Create Records to query

Operations: Create an account record with related contact records, and each contact has related task records. This is the sample data used throughout the demonstration.

### Section 1: Selecting specific properties

Operations:

- Use `$select` system query option to retrieve specific properties.
- Include `Prefer: odata.include-annotations="*"` header to get formatted values.

### Section 2: Using query functions

Operations:

- Use standard query functions like `contains`, `endswith`, and `startswith` to filter results.
- Use Dataverse-specific query functions like `LastXHours`, `Last7Days`, `Today`, `Between`, and `In`.
- Use filter operators and logical operators (`eq`, `ne`, `gt`, `and`, `or`).
- Set precedence using parentheses in filter expressions.

### Section 3: Ordering and aliases

Operations:

- Use `$orderby` to sort query results.
- Use parameterized aliases with `$filter` and `$orderby` to simplify queries.

### Section 4: Limit and count results

Operations:

- Use `$top` to limit the number of results returned.
- Use `$count` to get the total count of records matching the query.

### Section 5: Pagination

Operations:

- Use the `Prefer: odata.maxpagesize` request header to control page size.
- Use the `@odata.nextLink` annotation to retrieve subsequent pages of results.

### Section 6: Expanding results

Operations:

- Use `$expand` with single-valued navigation properties to include related records.
- Use `$expand` with collection-valued navigation properties.
- Use `$expand` with multiple navigation properties in a single request.
- Use nested `$expand` to retrieve multiple levels of related records.

### Section 7: Aggregate results

Operations: Use `$apply=aggregate` with functions like `average`, `sum`, `min`, and `max` to calculate aggregate values.

### Section 8: FetchXML queries

Operations:

- Send requests using FetchXML with the `fetchXml` query string parameter.
- Use paging with FetchXML using the `page` and `count` attributes.

### Section 9: Using predefined queries

Operations:

- Execute a saved query (system view) using `savedQuery` parameter.
- Execute a user query (saved view) using `userQuery` parameter.

### Section 10: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. This section loops through that list and deletes each record.

## Clean up

By default this sample deletes all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you'll be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)   
[Query Data using the Web API](../query/overview.md)   
[Quick Start Web API with PowerShell and Visual Studio Code](../quick-start-ps.md)   
[Use PowerShell and Visual Studio Code with the Dataverse Web API](../use-ps-and-vscode-web-api.md)   
[Web API Samples](../web-api-samples.md)   
[Web API Query Data Sample](../web-api-query-data-sample.md)   
[Web API Query Data sample (C#)](webapiservice-query-data.md)   
[Web API Query Data Sample (Client-side JavaScript)](query-data-client-side-javascript.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
