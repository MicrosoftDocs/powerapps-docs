---
title: "How to: Connect Your Code App to Dataverse"
description: "Connect your code app to Dataverse, add tables as data sources, and use generated services for CRUD operations. Follow this guide to get started."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 11/24/2026
ms.reviewer: jdaly
ms.topic: how-to
ai-usage: ai-assisted
contributors:
 - JimDaly
---
# How to: connect your code app to Dataverse

This guide shows developers how to connect their code app to Microsoft Dataverse by using the [Power Apps client library for code apps](https://www.npmjs.com/package/@microsoft/power-apps). Learn how to add a Dataverse table as a data source and use generated services for CRUD operations.

## Prerequisites

- Power Apps client library for code apps
- [Power Apps CLI](../reference/cli.md)
- An environment with Dataverse enabled
- A code app initialized for the environment

> [!IMPORTANT]
> Expanded queries, aggregation, and saved-view methods require Power Apps CLI version 1.4.0 or later and `@microsoft/power-apps` version 1.6.0 or later. If you regenerate Dataverse services with CLI version 1.4.0 or later, update the app's client library to version 1.6.0 or later before building. Earlier client libraries don't provide the types and methods that the regenerated services require. You don't need to regenerate existing services just to keep using their existing APIs.

## Steps

From the root of your code app project, use [`pa app add data-source`](../reference/cli.md#pa-app-add-data-source) to add the Dataverse table as a data source:

```powershell
pa app add data-source --connector dataverse --table <table-logical-name>
```

Replace `<table-logical-name>` with the logical name of the Dataverse table you want to connect to.

## Supported scenarios

The [Power Apps client library for code apps](https://www.npmjs.com/package/@microsoft/power-apps) supports the following scenarios when you connect to Dataverse:

- Add Dataverse entities to code apps.
- Retrieve formatted values (labels) for option sets option values.
- [Get metadata for Dataverse tables](get-table-metadata.md).
- Work with lookups. Currently, you need to use the guidance to [associate with a single-valued navigation property](../../data-platform/webapi/associate-disassociate-table-rows.md) or [associate records on create](../../data-platform/webapi/create-table-row.md#associate-table-rows-on-create) when working with lookups. A dedicated how-to guide is coming soon. The Power Apps team is actively working to make lookups easier to use in code apps.
- Image and file upload and download (preview). When you add Dataverse as a data source by using the Power Apps CLI, the generated functions are part of `src/generated/services`.
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

- Paging support.
- Expand related records and aggregate data with OData queries.
- Retrieve records from saved system views.

> [!TIP]
> Looking for a complete working example? The [Dataverse demo app](https://github.com/microsoft/PowerAppsCodeApps/tree/main/samples/Dataverse) demonstrates all the patterns covered in this article - CRUD operations, lookup fields, image and file upload and download, and generated services - in a React/TypeScript app you can explore and extend. To run the app yourself, follow the setup instructions in [PowerAppsCodeApps/samples/Dataverse/DEVELOPMENT.md](https://github.com/microsoft/PowerAppsCodeApps/blob/main/samples/Dataverse/DEVELOPMENT.md) to configure it for your environment.

## Set up your code app

Before you perform create, read, update, and delete (CRUD) operations in your code app, import the required types and services.

When you add a data source, the system automatically generates model and service files and places them in the `/generated/services/` folder.
For example, if you add the built-in [Accounts](../../data-platform/reference/entities/account.md) table as a data source, the system creates the following files:

- `AccountsModel.ts` – Defines the data model for the Accounts table.
- `AccountsService.ts` – Provides service methods for interacting with the Accounts data.

You can import and use these files in your code like this:

```typescript
import { AccountsService } from './generated/services/AccountsService';
import type { Accounts } from './generated/models/AccountsModel';
```

## Create records

Use the generated model types and service methods to create new Dataverse records from your code app.

1. **Create the record object using the generated model**

   The generated models reflect the schema of your Dataverse table. Use them to create record objects.

   > [!NOTE]
   > When creating a record, exclude system-managed or read-only columns such as primary keys and ownership fields. To understand which columns are read-only, see [Browse table definitions in your environment](../../data-platform/browse-your-metadata.md). For example, in the [Accounts table](../../data-platform/reference/entities/account.md), don't include the following fields:
   >
   > - accountid
   > - ownerid
   > - owneridname
   > - owneridtype
   > - owneridyominame

   Form a record with only the fields you want to populate. For example, for the Accounts entity:

   ```typescript

   const newAccount = {
      name: "New Account"
      statecode: 0,
      accountnumber: "ACCOO1"
      ...
   };
   ```

1. **Submit the record using the generated service**

   Use the functions in the generated service file to submit your record. For example, for the Accounts entity:

   ```typescript
   try {
   const result = await AccountsService.create(newAccount as Omit<Accounts, 'accountid'>);

   if (result.data) {
   console.log('Account created:', result.data);
   return result.data;
   }
   } catch (err) {
   console.error('Failed to create account:', err);
   throw err;
   };
   ```

## Read data

You can retrieve a single record or compose a query to return multiple records.

### Retrieve a single record

To retrieve a single record, you need its primary key (for example, `accountid`).

```typescript
const accountId = "<00000000-0000-0000-0000-000000000000>"; // Replace with actual ID value

try {
      const result = await AccountsService.get(accountId);
      if (result.data) {
            console.log('Account retrieved:', result.data);
      }
} catch (err) {
      console.error('Failed to retrieve account:', err);
}
```

### Retrieve multiple records

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
   expand?: string[];       // Related records to include
   apply?: string;          // OData aggregation expression
   filter?: string;         // OData filter string
   orderBy?: string[];     // Fields to sort by
   top?: number;           // Maximum number of records to retrieve
   skip?: number;          // Number of records to skip
   skipToken?: string;     // Token for pagination
}
```

> [!IMPORTANT]
> Always limit the number of columns you retrieve by using the `select` parameter.

Here's an example with multiple options:

```typescript
const fetchAccounts = async () => {
   const options: IGetAllOptions = {
      select: ['name', 'accountnumber', 'address1_city'],
      filter: "address1_country eq 'USA'",
      orderBy: ['name asc'],
      top: 50
   };

   const result = await AccountsService.getAll(options);
   if (!result.success) {
      throw result.error ?? new Error('Failed to fetch accounts.');
   }

   return result.data;
};
```

Check `result.success` before using `result.data`. An unsuccessful operation can return error information in `result.error` instead of throwing an exception.

### Expand related records

Use `expand` with `get` or `getAll` to include related records. Each array entry must be a nonempty OData expression. Use navigation property names from your Dataverse table metadata, not display names. For more information, see [Join tables using OData](../../data-platform/webapi/query/join-tables.md).

When the response includes properties outside the generated model, pass an explicit result type. For example, retrieve Accounts with the primary contact's full name:

```typescript
type AccountWithContact = Accounts & {
   primarycontactid?: { fullname?: string } | null;
};

const result = await AccountsService.getAll<AccountWithContact>({
   select: ['accountid', 'name'],
   expand: ['primarycontactid($select=fullname)']
});

if (!result.success) {
   throw result.error ?? new Error('Failed to retrieve accounts and contacts.');
}

for (const account of result.data) {
   console.log(account.name, account.primarycontactid?.fullname);
}
```

To expand related records for one account, call `AccountsService.get<AccountWithContact>(accountId, { expand: ['primarycontactid($select=fullname)'] })`.

### Aggregate data

Use `apply` with `getAll` to send an OData aggregation expression. Define a result type that matches the aggregate aliases instead of the generated table model. For example, count the Accounts records:

```typescript
type AccountCount = { total: number };

const result = await AccountsService.getAll<AccountCount>({
   apply: 'aggregate($count as total)'
});

if (!result.success) {
   throw result.error ?? new Error('Failed to count accounts.');
}

console.log(result.data);
```

The type argument describes one returned record, not an array. It provides compile-time typing, not runtime validation. Without a type argument, `get` and `getAll` retain the generated model type. These options use OData, not FetchXML. For supported expressions and query limits, see [Aggregate data using OData](../../data-platform/webapi/query/aggregate-data.md).

### Retrieve records from a saved system view

Use the generated `getSavedQuery` method to retrieve records from a Dataverse system view. Pass the view's saved query ID as a nonblank GUID:

```typescript
import type { IDataverseQueryOptions } from '@microsoft/power-apps/data';

type AccountViewRow = {
   accountid: string;
   name?: string;
};

const savedQueryId = '<saved-query-guid>';
const options: IDataverseQueryOptions = { maxPageSize: 100 };
const page = await AccountsService.getSavedQuery<AccountViewRow>(
   savedQueryId,
   options
);

if (!page.success) {
   throw page.error ?? new Error('Failed to retrieve the system view.');
}

console.log(page.data);

if (page.nextLink) {
   const nextPage = await AccountsService.getSavedQuery<AccountViewRow>(
      savedQueryId,
      { maxPageSize: 100, nextLink: page.nextLink }
   );

   if (!nextPage.success) {
      throw nextPage.error ?? new Error('Failed to retrieve the next view page.');
   }

   console.log(nextPage.data);
}
```

Replace `<saved-query-guid>` with the system view's ID and adjust `AccountViewRow` to match the view's columns. For more information about saved query IDs, see [Retrieve and execute predefined queries](../../data-platform/webapi/retrieve-and-execute-predefined-queries.md).

[`IDataverseQueryOptions`](/javascript/api/@microsoft/power-apps/idataversequeryoptions) supports only `maxPageSize` and `nextLink`. The default page size is 500. The view defines the query; don't pass `select`, `filter`, `expand`, or `apply` to this method.

For each subsequent page, pass the complete returned `nextLink` unchanged with the original saved query ID. The URL must target the same environment and table. Don't reconstruct it from `skipToken`. For ordinary `getAll` calls, continue to use `IGetAllOptions.skipToken`; `nextLink` isn't a `getAll` option or a CLI flag.

Saved-view retrieval is supported only for Dataverse tables and isn't supported by the built-in mock executor. Test it against your Dataverse environment.

## Update records

To update a record, you need:

1. The record's primary key value. For example, with the account table, the `accountid` value.
1. The changes you want to make.

> [!IMPORTANT]
> When you update a record, only include the properties you're changing in the request. If you set some changed properties of a record that you previously retrieved and include that data in your request, you update all properties even though their values didn't change. False updates like these can trigger business logic that expects the values changed, or can corrupt auditing data to indicate that someone changed data that didn't change.

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

To delete a record, you need the record's primary key value. For example, with the account table, the `accountid` value.

For example:

```typescript
const accountId = "<00000000-0000-0000-0000-000000000000>"; // Replace with actual ID value

try {
  await AccountsService.delete(accountId);
  console.log('Account deleted successfully');
} catch (err) {
  console.error('Failed to delete account:', err);
}
```

## Unsupported scenarios

The following features aren't yet supported:

- Polymorphic lookups
- Schema definition (entity metadata) CRUD
- FetchXML support
- Alternate key support

### Related information

- [Add data sources to your code app](connect-to-data.md)
- [Power Apps CLI](/power-platform/developer/cli/introduction)
