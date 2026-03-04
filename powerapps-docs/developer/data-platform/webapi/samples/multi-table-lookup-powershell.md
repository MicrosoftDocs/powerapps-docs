---
title: "Web API multi-table lookup sample (PowerShell)"
description: "This sample demonstrates how to create and use multi-table lookup (polymorphic lookup) columns in Dataverse using the Web API with PowerShell."
ms.date: 03/04/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Web API multi-table lookup sample (PowerShell)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This PowerShell sample demonstrates how to create and use multi-table lookup columns, sometimes called *polymorphic lookups*, using the Dataverse Web API.

> [!div class="nextstepaction"]
> [View this sample on GitHub](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS/PolymorphicLookup)

This sample demonstrates the operations described in [Use multi-table lookup columns](../multitable-lookup.md) and uses the [Dataverse Web API PowerShell Helper functions](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md) to manage authentication and provide reusable functions to perform common operations. These scripts are referenced using [dot sourcing](/powershell/module/microsoft.powershell.core/about/about_scripts#script-scope-and-dot-sourcing) with the following lines:

```powershell
. $PSScriptRoot\..\Core.ps1
. $PSScriptRoot\..\TableOperations.ps1
. $PSScriptRoot\..\CommonFunctions.ps1
. $PSScriptRoot\..\MetadataOperations.ps1
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
1. Open the `/dataverse/webapi/PS/PolymorphicLookup/PolymorphicLookupSample.ps1` file using Visual Studio Code.
1. Edit this line to use the URL of the environment you want to connect to:

   `Connect 'https://yourorg.crm.dynamics.com/' # change this`

1. (Optional) Set the `$deleteCreatedRecords` variable to `$false` if you don't want to delete the records this sample creates.
1. Press <kbd>F5</kbd> to run the sample.
1. The first time you run the sample a browser window opens. In the browser window, enter or select the credentials you want to use to authenticate.

To connect as a different user, run the [Disconnect-AzAccount command](/powershell/module/az.accounts/disconnect-azaccount) and try again.

## Code

The code for this sample is at: [PowerApps-Samples/dataverse/webapi/PS/PolymorphicLookup/PolymorphicLookupSample.ps1](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/PolymorphicLookup/PolymorphicLookupSample.ps1)

## Demonstrates

This sample has 9 sections:

### Section 0: Create Publisher and Solution

Operations:

1. Query for an existing publisher with the `examplepublisher` unique name by sending a `GET` request to `/publishers`.
1. Create the publisher if it doesn't already exist by sending a `POST` request to `/publishers`.
1. Query for an existing solution named `polymorphiclookupexamplesolution` by sending a `GET` request to `/solutions`.
1. Create the solution if it doesn't already exist by sending a `POST` request to `/solutions`.

> [!NOTE]
> All solution components created in this sample will be associated to the solution so that they can be exported. For operations without a named message, this association is created using the `MSCRM.SolutionUniqueName` request header set to the solution unique name.
> All names of solution components are prefixed using the publisher customization prefix.

### Section 1: Create Referenced Tables

Operations:

1. Create a `sample_Book` table by sending a `POST` request to `/EntityDefinitions`, if it doesn't already exist. This table includes a primary `sample_name` attribute and a `sample_CallNumber` string column.
1. Create a `sample_Audio` table by sending a `POST` request to `/EntityDefinitions`, if it doesn't already exist. This table includes a primary `sample_name` attribute and a `sample_AudioFormat` string column.
1. Create a `sample_Video` table by sending a `POST` request to `/EntityDefinitions`, if it doesn't already exist. This table includes a primary `sample_name` attribute and a `sample_VideoFormat` string column.

These three tables serve as the *referenced tables* that the polymorphic lookup column can point to.

### Section 2: Create Referencing Table

Operations: Create a `sample_Media` table by sending a `POST` request to `/EntityDefinitions`, if it doesn't already exist. This table includes a primary `sample_name` attribute and will host the polymorphic lookup column.

The `sample_Media` table serves as the *referencing table* — the table that contains the multi-table lookup column.

### Section 3: Create Polymorphic Lookup Attribute

Operations:

1. Create a `sample_MediaPolymorphicLookup` lookup column on the `sample_Media` table along with one-to-many relationships to each of the three referenced tables (`sample_Book`, `sample_Audio`, and `sample_Video`) using the [CreatePolymorphicLookupAttribute action](xref:Microsoft.Dynamics.CRM.CreatePolymorphicLookupAttribute). This single action creates the attribute and all three relationships at once.
1. Retrieve the `ReferencingEntityNavigationPropertyName` for each of the three relationships (`sample_media_sample_book`, `sample_media_sample_audio`, `sample_media_sample_video`) by sending `GET` requests to `/RelationshipDefinitions`. These navigation property names are needed to associate records using `@odata.bind` syntax.

### Section 4: Create Sample Data Records

Operations:

1. Retrieve the `EntitySetName` for each of the four tables by sending `GET` requests to `/EntityDefinitions`.
1. Create two `sample_Book` records by sending `POST` requests to `sample_books`.
1. Create two `sample_Audio` records by sending `POST` requests to `sample_audios`.
1. Create two `sample_Video` records by sending `POST` requests to `sample_videos`.
1. Create four `sample_Media` records by sending `POST` requests to `sample_medias`. Each media record uses the navigation property name retrieved in Section 3 and `@odata.bind` syntax to set the polymorphic lookup to point to a record from one of the three referenced tables.

### Section 5: Retrieve Sample Data

Operations:

1. Query all `sample_Media` records, selecting the `sample_name` and `_sample_mediapolymorphiclookup_value` columns by sending a `GET` request to `/sample_medias`. The query uses the `Microsoft.Dynamics.CRM.lookuplogicalname` and `OData.Community.Display.V1.FormattedValue` OData annotations to display the entity type and formatted name of each lookup value.
1. Filter `sample_Media` records where the polymorphic lookup points to a specific `sample_Book` record by sending a `GET` request to `/sample_medias` with an appropriate `$filter`.
1. Filter `sample_Media` records where the polymorphic lookup points to a specific `sample_Audio` record by sending a `GET` request to `/sample_medias` with an appropriate `$filter`.

### Section 6: Export Managed Solution

Operations: Export the solution created in [Section 0: Create Publisher and Solution](#section-0-create-publisher-and-solution) as a managed solution package using the [ExportSolution action](xref:Microsoft.Dynamics.CRM.ExportSolution). The exported `.zip` file is saved locally for use in Section 8.

### Section 7: Delete Sample Tables and Solution

Operations:

1. Delete the `sample_Media` table by sending a `DELETE` request to `/EntityDefinitions`. The referencing table must be deleted before the referenced tables.
1. Delete the `sample_Book`, `sample_Audio`, and `sample_Video` tables by sending `DELETE` requests to `/EntityDefinitions`.
1. Query the unmanaged solution by sending a `GET` request to `/solutions` filtered by unique name.
1. Delete the unmanaged solution by sending a `DELETE` request to `/solutions(<solutionid>)`.

### Section 8: Import and Delete Managed Solution

Operations:

1. Import the managed solution exported in [Section 6: Export Managed Solution](#section-6-export-managed-solution) using the [ImportSolution action](xref:Microsoft.Dynamics.CRM.ImportSolution).
1. Query the imported solution by sending a `GET` request to `/solutions` filtered by unique name.
1. Delete the imported managed solution by sending a `DELETE` request to `/solutions(<solutionid>)`.

## Clean up

By default this sample deletes all the records created in it. If you want to view created records after the sample is completed, change the `$deleteCreatedRecords` variable to `$false` and you will be prompted to decide if you want to delete the records.

### See also

[Use multi-table lookup columns](../multitable-lookup.md)<br />
[Use the Dataverse Web API](../overview.md)<br />
[Use the Web API with table definitions](../use-web-api-metadata.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API table schema operations sample (PowerShell)](metadata-operations-powershell.md)

[!INCLUDE[footer-include](../../../../includes/footer-include.md)]
