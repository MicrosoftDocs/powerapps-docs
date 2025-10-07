---
title: "How to: Connect your code app to Dataverse (preview)"
description: "Learn how to connect your code app to Dataverse"
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 09/29/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Connect your code app to Dataverse (preview)

This guide helps developers use the Power Apps SDK to connect their code app to Microsoft Dataverse.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

## Prerequisites

- Power Apps code apps SDK [@microsoft/power-apps - npm package](https://www.npmjs.com/package/@microsoft/power-apps)
- Power Apps CLI (PAC CLI) version 1.46 or later
- An environment with Dataverse enabled
- [You must be connected to the environment using PAC CLI](/power-platform/developer/cli/introduction#manage-auth-profiles)

## Steps

1. Ensure you're connected to your environment using PAC CLI.
1. Use the [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command to add Dataverse as a data source to your code app

   ```powershell
   pac code add-data-source -a dataverse -t <table-logical-name>
   ```

   Replace `<table-logical-name>` with the logical name of the Dataverse table you want to connect to.

## Supported scenarios

The following scenarios are supported when connecting to Dataverse using the Power Apps SDK:

- Add Dataverse entities to code apps using the PAC CLI
- Perform CRUD operations:

  - Create
  - Retrieve
  - RetrieveMultiple
  - Update
  - Delete

- Delegation for:

  - `Filter`
  - `Sort`
  - `Top` queries

- Paging support

## Set up your code app

Before performing create, read, update, and delete (CRUD) operations in your code app, complete these two setup steps.

1. **Ensure Power Apps SDK initialization before data calls**

   In your `App.tsx` file, implement logic that waits for the Power Apps SDK to fully initialize before performing any data operations. This prevents errors caused by uninitialized services or missing context.

   Use an asynchronous function or state management to confirm initialization before making API calls. For example:

   ```typescript
   useEffect(() => {
   // Define an async function to initialize the Power Apps SDK
   const init = async () => {
         try {
               await initialize(); // Wait for SDK initialization
               setIsInitialized(true); // Mark the app as ready for data operations
         } catch (err) {
               setError('Failed to initialize Power Apps SDK'); // Handle initialization errors
               setLoading(false); // Stop any loading indicators
         }
   };

   init(); // Call the initialization function when the component mounts
   }, []);

   useEffect(() => {
   // Prevent data operations until the SDK is fully initialized
   if (!isInitialized) return;

   // Place your data reading logic here
   }, []);
   ```

1. **Import required types and services**

   When you add a data source, model and service files are automatically generated and placed in the `/generated/services/` folder.
   For example, if you add the built-in [Accounts](../../data-platform/reference/entities/account.md) table as a data source, the following files are created:

   - `AccountsModel.ts` – Defines the data model for the Accounts table.

   - `AccountsService.ts` – Provides service methods for interacting with the Accounts data.

   You can import and use them in your code like this:

   ```typescript
   import { AccountsService } from './generated/services/AccountsService';
   import type { Accounts } from './generated/models/AccountsModel';
   ```

## Create records

1. **Create the record object using the generated model**

   The generated models reflect the schema of your Dataverse table and should be used to create record objects.

   > [!NOTE]
   > When creating a record, exclude system-managed or read-only columns such as primary keys and ownership fields. [Browse table definitions in your environment](../../data-platform/browse-your-metadata.md) describes a tool you can use to understand which columns are read-only. For example, in the [Accounts table](../../data-platform/reference/entities/account.md), don't include the following fields:
   >
   > - accountid
   > - ownerid
   > - owneridname
   > - owneridtype
   > - owneridyominame

   Example:

   ```typescript

   const record: Omit<
            Accounts,
            | "accountid"
            | "ownerid"
            | "owneridname"
            | "owneridtype"
            | "owneridyominame"
      > = {
            name: formData.name,
            statecode: 0,
            numberofemployees: 7,
         // ... other fields

   ```

1. **Submit the record using the generated service**

   Use the functions in the generated service file to submit your record. For example, for the Accounts entity:

   ```typescript
   try {
   const result = await AccountsService.create(record);
   if (result.success) {
      // Handle success
   }
   } catch (error) {
   // Handle error
   }
   ```

## Read data

You can retrieve a single record or compose a query to return multiple records.

**Retrieve a single record**

To retrieve a single record, you need its primary key (for example, `accountid`).

```typescript
const accountId = "00000000-0000-0000-0000-000000000000"; // Replace with actual GUID

try {
      const result = await AccountsService.get(accountId);
      if (result.data) {
            console.log('Account retrieved:', result.data);
      }
} catch (err) {
      console.error('Failed to retrieve account:', err);
}
```

**Retrieve multiple records**

To retrieve all records from a Dataverse table, use the `getAll` method:

```typescript
try {
   const result = await AccountsService.getAll();
   if (result.data) {
         const accounts = result.data;
         console.log(`Retrieved ${accounts.length} accounts`);
   }
} catch (err) {
   console.error('Failed to retrieve accounts:', err);
}
```

The `getAll` method accepts an optional parameter that implements the `IGetAllOptions` interface. Use these options to customize the query:

```typescript
interface IGetAllOptions {
   maxPageSize?: number;    // Maximum number of records per page
   select?: string[];       // Specific fields to retrieve
   filter?: string;         // OData filter string
   orderBy?: string[];     // Fields to sort by
   top?: number;           // Maximum number of records to retrieve
   skip?: number;          // Number of records to skip
   skipToken?: string;     // Token for pagination
}
```

> [!IMPORTANT]
> Always limit the number of columns you're retrieving with the `select` parameter.

Here's an example with multiple options:

```typescript
const fetchAccounts = async () => {
const options: IGetAllOptions = {
      select: ['name', 'accountnumber', 'address1_city'],
      filter: "address1_country eq 'USA'",
      orderBy: ['name asc'],
      top: 50
};

try {
      const result = await AccountsService.getAll(options);
      return result.data || [];
} catch (err) {
      console.error('Failed to fetch accounts:', err);
      return [];
}
};
```

## Update records

To update a record, you need:

1. The record's primary key (for example, `accountid`)
1. The changes you want to make

> [!IMPORTANT]
> When you update a record, only include the properties you're changing in the request body. Simply setting changed properties of a record that you previously retrieved, and including that data in your request updates each property even though the value is the same. This can cause system events that can trigger business logic that expects that the values changed. This can cause properties to appear to have been updated in auditing data when in fact they haven't actually changed.

This example updates the `name` and `telephone1` properties of the account record:

```typescript
const accountId = "<your-account-guid>";
const changes = {
      name: "Updated Account Name",
      telephone1: "555-0123"
};

try {
      await AccountsService.update(accountId, changes);
      console.log('Account updated successfully');
} catch (err) {
      console.error('Failed to update account:', err);
}
```

## Delete records in Dataverse

To delete a record, you need the record's primary key (for example, `accountid`).

For example:

```typescript
const accountId = "<00000000-0000-0000-0000-000000000000>"; // Replace with actual GUID

try {
  await AccountsService.delete(accountId);
  console.log('Account deleted successfully');
} catch (err) {
  console.error('Failed to delete account:', err);
}
```

## Unsupported scenarios

The following features aren't yet supported:

- Option sets, lookup fields (including polymorphic lookups)
- Dataverse actions and functions
- Deleting Dataverse datasources via PAC CLI
- Schema definition (entity metadata) CRUD
- FetchXML support
- Alternate key support

### Related information

- [How to: Connect your code app to data](connect-to-data.md)  
- [Power Apps CLI](/power-platform/developer/cli/introduction)
