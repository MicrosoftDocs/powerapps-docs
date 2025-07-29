---
title: "Sample: Column-level security using Dataverse SDK for .NET"
description: "This sample shows how to work with column-level security using the Dataverse SDK for .NET."
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
  - phecke
---
# Sample: Column-level security using Dataverse SDK for .NET

This sample shows how to perform [column-level security](../../column-level-security.md) operations using [Dataverse SDK for .NET](../overview.md).

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity)

## Prerequisites

- Microsoft Visual Studio 2022
- Access to Dataverse with system administrator privileges.

## How to run this sample

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy.
1. Follow the instructions in the [Configure users](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/README.md#configure-users) section to create a second application user account without the system administrator role.
1. Edit the [/ColumnLevelSecurity/appsettings.json](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/ColumnLevelSecurity/appsettings.json) file to define a connection string specifying the Microsoft Dataverse instance you want to connect to for both the system administrator and second application user.
1. Open the sample solution in Visual Studio and press **F5** to run the sample.

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
|`Program.cs`|Controls the flow of the sample. Contains definition of `Setup`, `Run`, and `Cleanup` methods and calls them in the `Main` method.|
|`Examples.cs`|Contains methods that demonstrate operations related to column-level security operations.|
|`Helpers.cs`|Contains methods used by the sample to manage setting up and running the sample. These methods aren't the focus of this sample.|

This sample is designed to be resilient when errors occur so you should be able to run the sample again if it failed previously.

## How this sample works

In order to create the scenario described in [What this sample does](#what-this-sample-does), the sample does the following operations:

### Setup

The static `Setup` method in this sample does the following operations:

1. Create a solution publisher named `ColumnLevelSecuritySamplePublisher` with customization prefix of `sample` if it doesn't exist.
1. Create a solution named `ColumnLevelSecuritySampleSolution` associated with the publisher if it doesn't exist. 

   All subsequent solution-aware items are created in the context of this solution.

1. Create a table named `sample_Example` if it doesn't exist.
1. Create four string columns in the `sample_Example` table if they don't exist. The table schema names are:

   - `sample_Email`
   - `sample_GovernmentId`
   - `sample_TelephoneNumber`
   - `sample_DateOfBirth`

1. Remove any existing sample data in the `sample_Example` table.
1. Add three rows of sample data with information in each column of the `sample_Example` table.
1. Create a new security role named **Column-level security sample role**.
1. Add privileges for the `sample_Example` table to the security role.
1. Associate the user to the security role.
1. Create a [Field Security Profile](../../reference/entities/fieldsecurityprofile.md) record named **Example Field Security Profile** that is used in the [Manage access to secure column data to groups](#manage-access-to-secure-column-data-to-groups) section of the sample.
1. Associate the application user to the field security profile.
1. Wait 30 seconds for the cache to catch up with the new objects created.

### Demonstrate

The static `Run` method in this sample does the following operations:

#### Retrieve information about columns

1. Use the `Examples.DumpColumnSecurityInfo` method to download a CSV file with data about which columns in the system can be secured.
1. Use the `Examples.GetSecuredColumnList` method to retrieve and show a list of environment columns that are already secured.

#### Secure columns

1. Demonstrate that the application user can retrieve data from all the columns in the `sample_Example` table.
1. Use the `Examples.SetColumnIsSecured` method to secure the four columns
1. Demonstrate that the application user can no longer retrieve data from the secured columns in the `sample_Example` table.

#### Grant access to secure column data to individuals

1. Use the `Examples.GrantColumnAccess` method to grant the application users read access to specific record field values by creating a [Field Sharing (PrincipalObjectAttributeAccess)](../../reference/entities/principalobjectattributeaccess.md) record.
1. Demonstrate that the application user can now retrieve data from specific secured record fields in the `sample_Example` table.
1. Demonstrate that the application user isn't allowed to write data to the secured columns.
1. Use the `Examples.ModifyColumnAccess` method to grant write access to a specific record field.
1. Demonstrate that the application user is now allowed to write data to the specific record field.
1. Use the `Examples.RevokeColumnAccess` method to delete the `PrincipalObjectAttributeAccess` records that gave the application user access to the secured columns.

#### Manage access to secure column data to groups

1. Add field permissions to the **Example Field Security Profile** record that was created in `Setup` by creating [Field Permission (FieldPermission)](../../reference/entities/fieldpermission.md) records
1. Demonstrate that the application user can view only the secured columns specified in the field permission records.
1. Demonstrate that the application user isn't allowed to write data to the specific record field not enabled with field permissions.

#### Masking

1. Retrieve ID values for existing masking rules. Create new [Secured Masking Column (AttributeMaskingRule)](../../reference/entities/attributemaskingrule.md) records to specify masking rules for columns of the `sample_Example` table.
1. Update the `canreadunmasked` column values of the [Field Permission (FieldPermission)](../../reference/entities/fieldpermission.md) records created earlier.
1. Wait 30 seconds for the cache to catch up with the new objects created.
1. Demonstrate that the application user can now retrieve data with masked values.
1. Demonstrate that the application user can now retrieve unmasked values with [RetrieveMultipleRequest class](/dotnet/api/microsoft.xrm.sdk.messages.retrievemultiplerequest) when using the [UnMaskedData optional parameter](../../optional-parameters.md#return-unmasked-data).
1. Demonstrate that the application user can now retrieve unmasked values with [RetrieveRequest class](/dotnet/api/microsoft.xrm.sdk.messages.retrieverequest) when using the [UnMaskedData optional parameter](../../optional-parameters.md#return-unmasked-data).

#### Export solution

Use an exported solution to test the functionality of the sample configurations outside of this sample.

1. Export the solution created with all the configurations as an unmanaged solution.
1. Export the solution created with all the configurations as a managed solution

### Clean up

The static `Cleanup` method in this sample does the following operations:

When the `SampleSettings.DeleteCreatedObjects` setting in `appsettings.json` is `true`, the `Cleanup` method tries to delete all components created during `Setup` or `Run`. The goal is to return the environment to the original state. If you don't want the items to be deleted, you can change the setting to `false`.

### Related samples

[Sample: Column-level security using Dataverse Web API (PowerShell)](column-level-security-powershell.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
