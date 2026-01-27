---
title: "Web API Conditional Operations Sample (PowerShell)"
description: "This sample demonstrates how to perform operations that are conditionally based upon the version of the table row contained on the Microsoft Dataverse server and/or currently maintained by the client, using the Dataverse Web API with PowerShell and Visual Studio Code."
ms.date: 01/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Web API Conditional Operations Sample (PowerShell)

This PowerShell version 7.4.0 sample demonstrates how to perform operations that are conditionally based upon the version of the table row contained on the Microsoft Dataverse server and/or currently maintained by the client. This sample implements the Dataverse operations and console output detailed in [Web API Conditional Operations Sample](../web-api-conditional-operations-sample.md).

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
1. Open the `ConditionalOperations.ps1` file using Visual Studio Code
1. Edit this line to use the URL of the environment you want to connect to:

   `Connect 'https://yourorg.crm.dynamics.com/' # change this`

1. (Optional) Set the `$deleteCreatedRecords` variable to `$false` if you don't want to delete the records this sample creates.
1. Press <kbd>F5</kbd> to run the sample.
1. The first time you run the sample a browser window opens. In the browser window, enter or select the credentials you want to use to authenticate.

To connect as a different user, run the [Disconnect-AzAccount command](/powershell/module/az.accounts/disconnect-azaccount) and try again.

## Code

The code for this sample is at: [PowerApps-Samples/dataverse/webapi/PS/ConditionalOperations/ConditionalOperations.ps1](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/ConditionalOperations/ConditionalOperations.ps1)

## Demonstrates

This sample has four regions:

### Section 0: Create sample records

Operations: Create an account record and retrieve it to capture the initial ETag value.

### Section 1: Conditional GET

Operations:

- Attempt to retrieve the account using `If-None-Match` header with the initial ETag value, demonstrating that a `304 NotModified` response is returned when the record hasn't changed.
- Update the account's telephone number.
- Attempt to retrieve the account again using `If-None-Match` header with the initial ETag value, demonstrating that the full record is returned because it has been modified.

### Section 2: Optimistic concurrency on delete and update

Operations:

- Attempt to delete the account using `If-Match` header with the initial ETag value, demonstrating that a `412 PreconditionFailed` error is returned when the ETag doesn't match.
- Attempt to update the account using `If-Match` header with the initial ETag value, demonstrating that a `412 PreconditionFailed` error is returned when the ETag doesn't match.
- Update the account using `If-Match` header with the current ETag value, demonstrating that the update succeeds when the ETag matches.
- Retrieve the account to confirm the update.

### Section 3: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. This section loops through that list and deletes each record.

## Clean up

By default this sample deletes all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you'll be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)
[Perform conditional operations using the Web API](../perform-conditional-operations-using-web-api.md)
[Quick Start Web API with PowerShell and Visual Studio Code](../quick-start-ps.md)
[Use PowerShell and Visual Studio Code with the Dataverse Web API](../use-ps-and-vscode-web-api.md)
[Web API Samples](../web-api-samples.md)
[Web API Conditional Operations Sample](../web-api-conditional-operations-sample.md)
[Web API Conditional Operations Sample (C#)](webapiservice-conditional-operations.md)
[Web API Conditional Operations Sample (Client-side JavaScript)](conditional-operations-client-side-javascript.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
