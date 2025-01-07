---
title: "Web API table schema operations sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform operations that change the Dataverse data structures using the Web API."
ms.date: 09/02/2022
author: mkannapiran
ms.author: kamanick
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API table schema operations sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This .NET 6.0 sample demonstrates how to perform operations that create and modify table, column, and relationship definitions using the Dataverse Web API.

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).
  
> [!NOTE]
> This sample implements the Dataverse operations and console output detailed in [Web API table schema operations sample](../web-api-metadata-operations-sample.md) and uses the common C# constructs described in [Web API Samples (C#)](../web-api-samples-csharp.md).

## Prerequisites

The following is required to build and run this sample:

- Microsoft Visual Studio 2022.
- Access to Dataverse with privileges to perform data operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the [/dataverse/webapi/C#-NETx/MetadataOperations/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/MetadataOperations) folder.
1. Open the `MetadataOperations.sln` file using Visual Studio 2022
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find this. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Press F5 to run the sample.

## Code

The code for this sample is here: [PowerApps-Samples/dataverse/webapi/C#-NETx/MetadataOperations/Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/MetadataOperations/Program.cs)

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

1. Create a new `sample_boolean` boolean column for the `sample_BankAccount` table by sending a `POST` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes`.
1. Retrieve the `sample_boolean` boolean column by sending a `GET` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_boolean')`.
1. Update the `sample_boolean` boolean column by sending a `PUT` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_boolean')`.
1. Update the option labels for the `sample_boolean` boolean column using the <xref:Microsoft.Dynamics.CRM.UpdateOptionValue?text=UpdateOptionValue Action>.
1. Create and retrieve a new `sample_datetime` datetime column for the `sample_BankAccount` table.
1. Create and retrieve a new `sample_decimal` decimal column for the `sample_BankAccount` table.
1. Create and retrieve a new `sample_integer` integer column for the `sample_BankAccount` table.
1. Create and retrieve a new `sample_memo` memo column for the `sample_BankAccount` table.
1. Create and retrieve a new `sample_money` money column for the `sample_BankAccount` table.
1. Create and retrieve a new `sample_choice` choice column for the `sample_BankAccount` table.
1. Add a new option to the `sample_choice` column using the <xref:Microsoft.Dynamics.CRM.InsertOptionValue?text=InsertOptionValue Action>.
1. Change the order of the  options of the `sample_choice` column using the <xref:Microsoft.Dynamics.CRM.OrderOption?text=OrderOption Action>.
1. Delete one of the options of the `sample_choice` column using the <xref:Microsoft.Dynamics.CRM.DeleteOptionValue?text=DeleteOptionValue Action>.
1. Create and retrieve a new `sample_multiselectchoice` multi-select choice column for the `sample_BankAccoun`t table.
1. Create a new Status option for the `sample_BankAccount` table using the <xref:Microsoft.Dynamics.CRM.InsertStatusValue?text=InsertStatusValue Action>. 

### Section 3: Create and use Global OptionSet

Operations:

1. Create a new global choice named `sample_colors` by sending a `POST` request to `/GlobalOptionSetDefinitions`.
1. Retrieve the `sample_colors` global choice by sending a `GET` request to  `/GlobalOptionSetDefinitions(<id value>)`.
1. Create a new `sample_colors` choice column for the `sample_BankAccount` table using the `sample_colors` global choice by sending a `POST` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes` and associating it to the global choice.

### Section 4: Create Customer Relationship

Operations:

1. Create a new `sample_customerid` customer column for the `sample_BankAccount` table using the <xref:Microsoft.Dynamics.CRM.CreateCustomerRelationships?text=CreateCustomerRelationships Action>.
1. Retrieve the `sample_customerid` customer column by sending a `GET` request to `/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_customerid')`.
1. Retrieve the relationships created for the customer column by sending `GET` requests to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata`.`.

### Section 5: Create and retrieve a one-to-many relationship

Operations:

1. Verify that the `sample_BankAccount` table is eligible to be referenced in a 1:N relationship using the <xref:Microsoft.Dynamics.CRM.CanBeReferenced?text=CanBeReferenced Function>.
1. Verify that the `contact` table is eligible to be reference other tables in a 1:N relationship using the <xref:Microsoft.Dynamics.CRM.CanBeReferencing?text=CanBeReferencing Function>.
1. Identify what other tables can reference the `sample_BankAccount` table in a 1:N relationship using the <xref:Microsoft.Dynamics.CRM.GetValidReferencingEntities?text=GetValidReferencingEntities Function>.
1. Create a 1:N relationship between `sample_BankAccount` and `contact` tables by sending a `POST` request to `/RelationshipDefinitions`.
1. Retrieve the 1:N relationship by sending `GET` request to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata`.

### Section 6: Create and retrieve a many-to-one relationship

Operations:

1. Create a N:1 relationship between `sample_BankAccount` and `account` tables by sending `POST` a request to `/RelationshipDefinitions`.
1. Retrieve the N:1 relationship by sending a `GET` request to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata`.

### Section 7: Create and retrieve a many-to-many relationship

Operations:

1. Verify that the `sample_BankAccount` and `contact` tables are eligible to participate in a N:N relationship using the <xref:Microsoft.Dynamics.CRM.CanManyToMany?text=CanManyToMany Function>.
1. Verify that the `sample_BankAccount` and `contact` tables are eligible to participate in a N:N relationship using the <xref:Microsoft.Dynamics.CRM.GetValidManyToMany?text=GetValidManyToMany Function>.
1. Create a N:N relationship between `sample_BankAccount` and `contact` tables by sending a `POST` request to `/RelationshipDefinitions`.
1. Retrieve the N:N relationship by sending `GET` request to `/RelationshipDefinitions(<id>)/Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata`.

### Section 8: Export managed solution

Operations: Export the solution created in [Section 0: Create Publisher and Solution](#section-0-create-publisher-and-solution) containing the items created in this sample using the <xref:Microsoft.Dynamics.CRM.ExportSolution?text=ExportSolution Action>.

### Section 9: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. In this sample the records are deleted using a `$batch` operation.

### Section 10: Import and Delete managed solution

Operations:

1. Import the solution exported in [Section 8](#section-8-export-managed-solution) using the <xref:Microsoft.Dynamics.CRM.ImportSolution?text=ImportSolution Action>.
1. Query the solution table to get the `solutionid` of the imported solution.
1. Delete the imported solution using the `solutionid`.

## Clean up

By default this sample will delete all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you will be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)<br />
[WebAPIService class library (C#)](webapiservice.md)<br />
[Use the Web API with table definitions](../use-web-api-metadata.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Basic Operations Sample (C#)](webapiservice-basic-operations.md)<br />
[Web API Query Data sample (C#)](webapiservice-query-data.md)<br />
[Web API Conditional Operations sample (C#)](webapiservice-conditional-operations.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API WebApiService Parallel Operations Sample (C#)](webapiservice-parallel-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
