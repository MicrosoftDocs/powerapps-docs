---
title: "Web API Functions and Actions Sample (PowerShell)"
description: "This sample demonstrates how to call bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API with PowerShell and Visual Studio Code."
ms.date: 01/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Web API Functions and Actions Sample (PowerShell)

This PowerShell version 7.4.0 sample demonstrates how to call bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API. This sample implements the Dataverse operations and console output detailed in [Web API Functions and Actions Sample](../web-api-functions-actions-sample.md).

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS/FunctionsAndActions)

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
1. Open the `FunctionsAndActions.ps1` file using Visual Studio Code
1. Edit this line to use the URL of the environment you want to connect to:

   `Connect 'https://yourorg.crm.dynamics.com/' # change this`

1. (Optional) Set the `$deleteCreatedRecords` variable to `$false` if you don't want to delete the records this sample creates.
1. Press <kbd>F5</kbd> to run the sample.
1. The first time you run the sample a browser window opens. In the browser window, enter or select the credentials you want to use to authenticate.

To connect as a different user, run the [Disconnect-AzAccount command](/powershell/module/az.accounts/disconnect-azaccount) and try again.

## Code

The code for this sample is at: [PowerApps-Samples/dataverse/webapi/PS/FunctionsAndActions/FunctionsAndActions.ps1](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/FunctionsAndActions/FunctionsAndActions.ps1)

## Demonstrates

This sample has nine regions:

### Section 1: Unbound Function WhoAmI

Operations: Call the [WhoAmI Function](xref:Microsoft.Dynamics.CRM.WhoAmI) to retrieve information about the current user.

### Section 2: Unbound Function FormatAddress

Operations:

- Call the [FormatAddress Function](xref:Microsoft.Dynamics.CRM.FormatAddress) with parameters for an address in the United States.
- Call the same function with parameters for an address in Japan to demonstrate different formatting.

### Section 3: Unbound Function InitializeFrom

Operations:

- Create an account record as the original record.
- Call the [InitializeFrom Function](xref:Microsoft.Dynamics.CRM.InitializeFrom) to get data for a new record based on the original.
- Create a new account record using the data returned from `InitializeFrom`.

### Section 4: Unbound Function RetrieveCurrentOrganization

Operations: Call the [RetrieveCurrentOrganization Function](xref:Microsoft.Dynamics.CRM.RetrieveCurrentOrganization) to retrieve information about the current organization.

### Section 5: Unbound Function RetrieveTotalRecordCount

Operations: Call the [RetrieveTotalRecordCount Function](xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount) to retrieve the total number of records for specified tables.

### Section 6: Bound Function IsSystemAdmin custom API

Operations:

- Detect if the `sample_IsSystemAdmin` custom API is installed in the organization.
- If not installed, import the managed solution containing the custom API.
- Retrieve system user records and test each one using the `sample_IsSystemAdmin` function to determine if they have the System Administrator security role.

### Section 7: Unbound Action GrantAccess

Operations:

- Create an account record to share.
- Retrieve an enabled user other than the current user.
- Use the [RetrievePrincipalAccess Function](xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess) to check the user's access rights.
- Use the [GrantAccess Action](xref:Microsoft.Dynamics.CRM.GrantAccess) to grant additional access rights to the user.
- Verify the access rights were granted using `RetrievePrincipalAccess` again.

### Section 8: Bound Action AddPrivilegesRole

Operations:

- Create a security role associated with the current user's business unit.
- Retrieve the role with expanded privileges to show default privileges.
- Retrieve information about specific privileges to add to the role.
- Use the [AddPrivilegesRole Action](xref:Microsoft.Dynamics.CRM.AddPrivilegesRole) to add privileges to the role.
- Retrieve the role again to confirm the privileges were added.

### Section 9: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. This section loops through that list and deletes each record.

## Clean up

By default this sample deletes all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you'll be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)   
[Use Web API functions](../use-web-api-functions.md)   
[Use Web API actions](../use-web-api-actions.md)   
[Quick Start Web API with PowerShell and Visual Studio Code](../quick-start-ps.md)   
[Use PowerShell and Visual Studio Code with the Dataverse Web API](../use-ps-and-vscode-web-api.md)   
[Web API Samples](../web-api-samples.md)   
[Web API Functions and Actions Sample](../web-api-functions-actions-sample.md)   
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)   
[Web API Functions and Actions Sample (Client-side JavaScript)](functions-actions-client-side-javascript.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
