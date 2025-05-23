---
title: "Web API Basic Operations Sample (PowerShell)"
description: "This sample demonstrates how to perform basic CRUD (Create, Retrieve, Update, and Delete) and association and dissociation operations on Microsoft Dataverse table rows, using the Dataverse Web API with PowerShell and Visual Studio Code."
ms.date: 01/20/2024
author: MicroSri
ms.author: sriknair
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Basic Operations Sample (PowerShell)

This PowerShell version 7.4.0 sample demonstrates how to perform common data operations using the Dataverse Web API and Visual Studio Code. This sample implements the Dataverse operations and console output detailed in [Web API Basic Operations Sample](../web-api-basic-operations-sample.md).

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
1. Open the `BasicOperations.ps1` file using Visual Studio Code
1. Edit this line to use the URL of the environment you want to connect to:

   `Connect 'https://yourorg.crm.dynamics.com/' # change this`

1. (Optional) Set the `$deleteCreatedRecords` variable to `$false` if you don't want to delete the records this sample creates.
1. Press <kbd>F5</kbd> to run the sample.
1. The first time you run the sample a browser window opens. In the browser window, enter or select the credentials you want to use to authenticate.

To connect as a different user, run the [Disconnect-AzAccount command](/powershell/module/az.accounts/disconnect-azaccount) and try again.

## Code

The code for this sample is at: [PowerApps-Samples/dataverse/webapi/PS/BasicOperations/BasicOperations.ps1](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/BasicOperations/BasicOperations.ps1)

## Demonstrates

This sample has five regions:

### Section 1: Basic Create and Update operations

Operations:

- Create a contact record.
- Update the contact record.
- Retrieve the contact record.
- Update a single property of the contact record.
- Retrieve a single property of the contact record.

### Section 2: Create record associated to another

Operations: Associate a new record to an existing one.

### Section 3: Create related records

Operations: Create the following entries in one operation: an account, its associated primary contact, and open tasks for that contact.  These entity types have the following relationships:

```
Accounts
    |---[Primary] Contact (N-to-1)
        |---Tasks (1-to-N)
```

### Section 4: Associate and Disassociate records

Operations:

- Add a contact to the account `contact_customer_accounts` collection.
- Remove a contact from the account `contact_customer_accounts` collection.
- Associate a security role to a user using the `systemuserroles_association` collection.
- Remove a security role for a user using the `systemuserroles_association` collection.

### Section 5: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. This section loops through that list and deletes each record.

## Clean up

By default this sample deletes all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you'll be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)   
[Quick Start Web API with PowerShell and Visual Studio Code](../quick-start-ps.md)   
[Use PowerShell and Visual Studio Code with the Dataverse Web API](../use-ps-and-vscode-web-api.md)   
[Create a table row using the Web API](../create-entity-web-api.md)   
[Update and delete table rows using the Web API](../update-delete-entities-using-web-api.md)   
[Retrieve an table row using the Web API](../retrieve-entity-using-web-api.md)   
[Web API Samples](../web-api-samples.md)   
[Web API Basic Operations Sample](../web-api-basic-operations-sample.md)   

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
