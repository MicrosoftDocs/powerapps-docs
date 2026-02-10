---
title: "Web API table schema operations sample (PowerShell) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform operations that change the Dataverse data structures using the Web API with PowerShell."
ms.date: 05/14/2024
author: mkannapiran
ms.author: kamanick
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API table schema operations sample (PowerShell)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This PowerShell sample demonstrates how to perform operations that create and modify table, column, and relationship definitions using the Dataverse Web API.

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS/MetadataOperations)
  
This sample implements the Dataverse operations and console output detailed in [Web API table schema operations sample](../web-api-metadata-operations-sample.md) and uses the [Dataverse Web API PowerShell Helper functions](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/README.md) to manage authentication and provide reusable functions to perform common operations. These scripts are referenced using [dot sourcing](/powershell/module/microsoft.powershell.core/about/about_scripts#script-scope-and-dot-sourcing) with the following lines:

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
1. Open the `/dataverse/webapi/PS/MetadataOperations/MetadataOperationsSample.ps1` file using Visual Studio Code
1. Edit this line to use the URL of the environment you want to connect to:

   `Connect 'https://yourorg.crm.dynamics.com/' # change this`

1. (Optional) Set the `$deleteCreatedRecords` variable to `$false` if you don't want to delete the records this sample creates.
1. Press <kbd>F5</kbd> to run the sample.
1. The first time you run the sample a browser window opens. In the browser window, enter or select the credentials you want to use to authenticate.

To connect as a different user, run the [Disconnect-AzAccount command](/powershell/module/az.accounts/disconnect-azaccount) and try again.

## Code

The code for this sample is at: [PowerApps-Samples/dataverse/webapi/PS/MetadataOperations/MetadataOperationsSample.ps1](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/PS/MetadataOperations/MetadataOperationsSample.ps1)

## Demonstrates

This sample has 11 regions:

### Section 0: Create Publisher and Solution

Operations: Create a solution record and an associated publisher record.

> [!NOTE]
> All solution components created in this sample will be associated to the solution so that they can be exported. For operations without a named message, this association is created using the `MSCRM.SolutionUniqueName` request header setting the solution unique name set as the value.
> All names of solution components are prefixed using the publisher customization prefix.

### Section 1: Create, Retrieve and Update Table

Operations:

1. Create a new `sample_BankAccount` user-owned table by sending a `POST` request to `/EntityDefinitions`.
1. Retrieve the created table by sending a `GET` request to `/EntityDefinitions(LogicalName='sample_bankaccount')`.
1. Update the table by sending a `PUT` request to `/EntityDefinitions(LogicalName='sample_bankaccount')`.

### Section 2: Create, Retrieve and Update Columns

Operations:

1. Attempt to retrieve a `sample_boolean` boolean column by sending a `GET` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_boolean')`.
1. If the column doesn't already exist, create a new `sample_boolean` boolean column for the `sample_BankAccount` table by sending a `POST` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes`.
1. Update the `sample_boolean` boolean column by sending a `PUT` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_boolean')`.
1. Update the option labels for the `sample_boolean` boolean column using the [UpdateOptionValue action](xref:Microsoft.Dynamics.CRM.UpdateOptionValue).
1. Attempt to retrieve a `sample_datetime` datetime column for the `sample_BankAccount` table, and create it if it doesn't exist.
1. Attempt to retrieve a `sample_decimal` decimal column for the `sample_BankAccount` table, and create it if it doesn't exist.
1. Attempt to retrieve a`sample_integer` integer column for the `sample_BankAccount` table, and create it if it doesn't exist.
1. Attempt to retrieve a `sample_memo` memo column for the `sample_BankAccount` table, and create it if it doesn't exist.
1. Attempt to retrieve a `sample_money` money column for the `sample_BankAccount` table, and create it if it doesn't exist.
1. Attempt to retrieve a `sample_choice` choice column for the `sample_BankAccount` table, and create it if it doesn't exist.
1. Add a new option to the `sample_choice` column using the [InsertOptionValue action](xref:Microsoft.Dynamics.CRM.InsertOptionValue).
1. Change the order of the  options of the `sample_choice` column using the [OrderOption action](xref:Microsoft.Dynamics.CRM.OrderOption).
1. Delete one of the options of the `sample_choice` column using the [DeleteOptionValue action](xref:Microsoft.Dynamics.CRM.DeleteOptionValue).
1. Attempt to retrieve a  `sample_multiselectchoice` multi-select choice column for the `sample_BankAccount` table, and create it if it doesn't exist.
1. Create a new Status option for the `sample_BankAccount` table using the [InsertStatusValue Action](xref:Microsoft.Dynamics.CRM.InsertStatusValue). 

### Section 3: Create and use Global OptionSet

Operations:

1. Create a new global choice named `sample_colors` by sending a `POST` request to `/GlobalOptionSetDefinitions`.
1. Retrieve the `sample_colors` global choice by sending a `GET` request to  `/GlobalOptionSetDefinitions(<id value>)`.
1. Create a new `sample_colors` choice column for the `sample_BankAccount` table using the `sample_colors` global choice by sending a `POST` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes` and associating it to the global choice.

### Section 4: Create Customer Relationship

Operations:

1. Create a new `sample_customerid` customer column for the `sample_BankAccount` table using the [CreateCustomerRelationships Action](xref:Microsoft.Dynamics.CRM.CreateCustomerRelationships).
1. Retrieve the `sample_customerid` customer column by sending a `GET` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_customerid')`.
1. Retrieve the relationships created for the customer column by sending `GET` requests to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata`.`.

### Section 5: Create and retrieve a one-to-many relationship

Operations:

1. Verify that the `sample_BankAccount` table is eligible to be referenced in a 1:N relationship using the [CanBeReferenced function](xref:Microsoft.Dynamics.CRM.CanBeReferenced).
1. Verify that the `contact` table is eligible to be reference other tables in a 1:N relationship using the [CanBeReferencing function](xref:Microsoft.Dynamics.CRM.CanBeReferencing).
1. Identify what other tables can reference the `sample_BankAccount` table in a 1:N relationship using the [GetValidReferencingEntities function](xref:Microsoft.Dynamics.CRM.GetValidReferencingEntities).
1. Create a 1:N relationship between `sample_BankAccount` and `contact` tables by sending a `POST` request to `/RelationshipDefinitions`.
1. Retrieve the 1:N relationship by sending `GET` request to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata`.

### Section 6: Create and retrieve a many-to-one relationship

Operations:

1. Create a N:1 relationship between `sample_BankAccount` and `account` tables by sending `POST` a request to `/RelationshipDefinitions`.
1. Retrieve the N:1 relationship by sending a `GET` request to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata`.

### Section 7: Create and retrieve a many-to-many relationship

Operations:

1. Verify that the `sample_BankAccount` and `contact` tables are eligible to participate in a N:N relationship using the [CanManyToMany function](xref:Microsoft.Dynamics.CRM.CanManyToMany).
1. Verify that the `sample_BankAccount` and `contact` tables are eligible to participate in a N:N relationship using the [GetValidManyToMany Function](xref:Microsoft.Dynamics.CRM.GetValidManyToMany).
1. Create a N:N relationship between `sample_BankAccount` and `contact` tables by sending a `POST` request to `/RelationshipDefinitions`.
1. Retrieve the N:N relationship by sending `GET` request to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata`.

### Section 8: Export managed solution

Operations: Export the solution created in [Section 0: Create Publisher and Solution](#section-0-create-publisher-and-solution) containing the items created in this sample using the [ExportSolution Action](xref:Microsoft.Dynamics.CRM.ExportSolution).

### Section 9: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. In this sample the records are deleted in the reverse order in which they were created.

### Section 10: Import and Delete managed solution

Operations:

1. Import the solution exported in [Section 8](#section-8-export-managed-solution) using the [ImportSolution action](xref:Microsoft.Dynamics.CRM.ImportSolution).
1. Query the solution table to get the `solutionid` of the imported solution.
1. Delete the imported solution using the `solutionid`.

## Clean up

By default this sample will delete all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you will be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)<br />
[Use the Web API with table definitions](../use-web-api-metadata.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Basic Operations Sample (PowerShell)](basic-operations-powershell.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
