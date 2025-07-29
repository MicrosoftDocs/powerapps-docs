---
title: "Sample: Column-level security using Dataverse Web API (PowerShell)"
description: "This sample shows how to work with column-level security using the Dataverse Web API with PowerShell."
ms.date: 07/30/2025
author: paulliew
ms.subservice: dataverse-developer
ms.author: paulliew
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
---
# Sample: Column-level security using Dataverse Web API (PowerShell)

This sample shows how to perform column-level security operations using [Dataverse Web API](../overview.md) with PowerShell.

> [!div class="nextstepaction"]
> [Web API Powershell column-level security sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS/ColumnLevelSecurity)

## Prerequisites

Before running this sample you should read these articles that explain concepts and patterns used by these samples:

- [Quick Start Web API with PowerShell and Visual Studio Code](../quick-start-ps.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](../use-ps-and-vscode-web-api.md)

This sample requires:

- Visual Studio Code. [Download Visual Studio Code](https://code.visualstudio.com/download)
- PowerShell extension for Visual Studio Code.  [Install PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)
- PowerShell 7.4 or higher. See [Install PowerShell on Windows, Linux, and macOS](/powershell/scripting/install/installing-powershell)
- Az PowerShell module version 11.1.0 or higher. See [How to install Azure PowerShell](/powershell/azure/install-azure-powershell)

   To update an existing installation to the latest version, use `Update-Module -Name Az -Force`

- Access to Dataverse with system administrator privileges.
- An application user account with **Basic User** access. See the [Configure users section](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS/ColumnLevelSecurity#configure-users) for instructions about how to create this user.



## How to run this sample

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
1. Open the [ColumnLevelSecurity.ps1](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/ColumnLevelSecurity/ColumnLevelSecurity.ps1) file using Visual Studio Code.
1. Create a file named `.env` using the data found in the [.env.example](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/ColumnLevelSecurity/.env.example) file.
1. In the `.env` file, replace the placeholder values:

   ```env
   # The environment this application will connect to.
   BASE_URL=https://<yourorg>.api.crm.dynamics.com/
   # The application user application id
   CLIENT_ID=00001111-aaaa-2222-bbbb-3333cccc4444
   # The application user secret
   CLIENT_SECRET=Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2
   # The Entra tenant id
   TENANT_ID=aaaabbbb-0000-cccc-1111-dddd2222eeee
   ```

1. Set the `BASE_URL` to the URL of the environment you want to run the sample against
1. See the [Configure users section](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS/ColumnLevelSecurity#configure-users) for instructions to set the `CLIENT_ID`, `CLIENT_SECRET`, and `TENANT_ID` values.
1. Press <kbd>F5</kbd> to run the sample.

When the sample runs, you will be prompted in the default browser to select an environment user account and enter a password.

## What this sample does

This sample demonstrates the capabilities described in [Column-level security with code](../../column-level-security.md):

- Discover which columns can be secured in a Dataverse environment
- Discover which columns are currently secured
- Secure columns in a Dataverse environment
- Grant read or write access to selected fields to individual users
- Modify access to secured fields for individual users
- Revoke access to selected fields for individual users
- Provide read and write access to specific groups of users
- Enable masking of secured columns
- Retrieve unmasked values for secured columns

## Sample files

The code for this sample is in the following files:

|File|Description|
|---------|---------|
|`ColumnLevelSecurity.ps1`|Controls the flow of the sample. Contains definition of `Setup`, `Run`, and `Cleanup` functions and calls them at the end.|
|`Examples.ps1`|Contains 12 functions that demonstrate operations related to column-level security operations.|
|`Helpers.ps1`|Contains constants and functions used by the sample to manage setting up and running the sample. These functions are not the focus of this sample.|

This sample is designed to be resilient when errors occur so you should be able to run the sample again if it failed previously.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

The `Setup` function in this sample does the following:

1. Create a solution publisher named `ColumnLevelSecuritySamplePublisher` with customization prefix of `sample` if it doesn't exist.
1. Create a solution named `ColumnLevelSecuritySampleSolution` if it doesn't exist. All subsequent items created are created in the context of this solution.
1. Create a table named `sample_Example` if it doesn't exist.
1. Create 4 string columns in the `sample_Example` table if they don't exist. The table schema names are:

   - `sample_Email`
   - `sample_GovernmentId`
   - `sample_TelephoneNumber`
   - `sample_DateOfBirth`

1. Remove any existing sample data in the `sample_Example` table.
1. Add three rows of sample data with information in each column of the `sample_Example` table.
1. Create a new security role named **Column-level security sample role**.
1. Add privileges for the `sample_Example` table to the security role.
1. Associate the user to the security role.
1. Create a [Field Security Profile](../../reference/entities/fieldsecurityprofile.md) record named **Example Field Security Profile** that will be used in the [Manage access to secure column data to groups](#manage-access-to-secure-column-data-to-groups) section of the sample.
1. Associate the application user to the field security profile.
1. Wait 30 seconds for the cache to catch up with the new objects created.

### Demonstrate

The `Run` function in this sample does the following:

#### Retrieve information about columns

1. Use the `Dump-ColumnSecurityInfo-Example` function to download a CSV file with data about which columns in the system can be secured.
1. Use the `Get-SecuredColumnList-Example` function to retrieve and show a list of environment columns that are already secured.

#### Secure columns

1. Demonstrate that the application user can retrieve data from all the columns in the `sample_Example` table.
1. Use the `Set-ColumnIsSecured-Example` function to secure the 4 columns
1. Demonstrate that the application user can no longer retrieve data from the secured columns in the `sample_Example` table.

#### Grant access to secure column data to individuals

1. Use the `Grant-ColumnAccess-Example` function to grant the application users read access to specific record field values by creating a [Field Sharing (PrincipalObjectAttributeAccess)](../../reference/entities/principalobjectattributeaccess.md) record.
1. Demonstrate that the application user can now retrieve data from specific secured record fields in the `sample_Example` table.
1. Demonstrate that the application user is not allowed to write data to the secured columns.
1. Use the `Modify-ColumnAccess-Example` function to grant write access to a specific record field.
1. Demonstrate that the application user is now allowed to write data to the specific record field.
1. Use the `Revoke-ColumnAccess-Example` function to delete the `PrincipalObjectAttributeAccess` records that gave the application user access to the secured columns.

#### Manage access to secure column data to groups

1. Add field permissions to the **Example Field Security Profile** record that was created in `Setup` by creating [Field Permission (FieldPermission)](../../reference/entities/fieldpermission.md) records
1. Demonstrate that the application user can view only the secured columns specified in the field permission records.
1. Demonstrate that the application user is not allowed to write data to the specific record field not enabled with field permissions.

#### Masking

1. Retrieve ID values for existing masking rules. Create new [Secured Masking Column (AttributeMaskingRule)](../../reference/entities/attributemaskingrule.md) records to specify masking rules for columns of the `sample_Example` table.
1. Update the `canreadunmasked` column values of the [Field Permission (FieldPermission)](../../reference/entities/fieldpermission.md) records created earlier.
1. Wait 30 seconds for the cache to catch up with the new objects created.
1. Demonstrate that the application user can now retrieve data with masked values.
1. Demonstrate that the application user can now retrieve unmasked values with a `GET` requests on the `sample_examples` collection to return multiple records when using the [UnMaskedData optional parameter](../../optional-parameters.md#return-unmasked-data).
1. Demonstrate that the application user can now retrieve unmasked values with a `GET` request to retrieve a single record when using the [UnMaskedData optional parameter](../../optional-parameters.md#return-unmasked-data).

#### Export solution

Use an exported solution to test the functionality of the sample configurations outside of this sample.

1. Export the solution created with all the configurations as an unmanaged solution.
1. Export the solution created with all the configurations as a managed solution

### Clean up

The static `Cleanup` function in this sample does the following:

When the `$DELETE_CREATED_OBJECTS` setting in `Helpers.ps1` is `true`, the `Cleanup` function will try to delete all components created during `Setup` or `Run`. The goal is to return the environment to the original state. If you don't want the items to be deleted, you can change the setting to `false`.

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
