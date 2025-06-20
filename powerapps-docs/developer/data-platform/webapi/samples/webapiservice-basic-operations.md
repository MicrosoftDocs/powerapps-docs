---
title: "Web API Basic Operations Sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform basic CRUD (Create, Retrieve, Update, and Delete) and association and dissociation operations on Microsoft Dataverse table rows, using the Dataverse Web API with the WebAPIService class library."
ms.date: 08/29/2022
author: MsSQLGirl
ms.author: sriknair
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Basic Operations Sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This .NET 6.0 sample demonstrates how to perform common data operations using the Dataverse Web API.

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).
  
> [!NOTE]
> This sample implements the Dataverse operations and console output detailed in [Web API Basic Operations Sample](../web-api-basic-operations-sample.md) and uses the common C# constructs described in [Web API Samples (C#)](../web-api-samples-csharp.md).

## Prerequisites

These are required to build and run this sample:

- Microsoft Visual Studio 2022.
- Access to Dataverse with privileges to perform data operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the [/dataverse/webapi/C#-NETx/BasicOperations/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/BasicOperations) folder.
1. Open the `BasicOperations.sln` file using Visual Studio 2022
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find the Url for your environment. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Press F5 to run the sample.

## Code

The code for this sample is here: [PowerApps-Samples/dataverse/webapi/C#-NETx/BasicOperations/Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/BasicOperations/Program.cs)

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

### Section 3: Create related entities

Operations: Create the following entries in one operation: an account, its associated primary contact, and open tasks for that contact.  These entity types have the following relationships:

```
Accounts
    |---[Primary] Contact (N-to-1)
        |---Tasks (1-to-N)
```

### Section 4: Associate and Disassociate entities

Operations:

- Add a contact to the account `contact_customer_accounts` collection.
- Remove a contact from the account `contact_customer_accounts` collection.
- Associate a security role to a user using the `systemuserroles_association` collection.
- Remove a security role for a user using the `systemuserroles_association` collection.

### Section 5: Delete sample entities

Operations: A reference to each record created in this sample was added to a list as it was created. This section loops through that list and deletes each record.

## Clean up

By default this sample deletes all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you'll be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)<br />
[WebAPIService class library (C#)](webapiservice.md)<br />
[Create a table row using the Web API](../create-entity-web-api.md)<br />
[Update and delete table rows using the Web API](../update-delete-entities-using-web-api.md)<br />
[Retrieve an table row using the Web API](../retrieve-entity-using-web-api.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Basic Operations Sample](../web-api-basic-operations-sample.md)<br />
[Web API Query Data sample (C#)](webapiservice-query-data.md)<br />
[Web API Conditional Operations sample (C#)](webapiservice-conditional-operations.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API table schema operations sample (C#)](webapiservice-metadata-operations.md)<br />
[Web API WebApiService Parallel Operations Sample (C#)](webapiservice-parallel-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
