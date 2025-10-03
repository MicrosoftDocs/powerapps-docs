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
- You must be connected to the environment using PAC CLI

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

## Read data from a Dataverse table

Follow these steps to read data from a Dataverse table in your application:

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

1. **Use model and service files for data access**

   Use the provided model and service files to access Dataverse data. These files should encapsulate logic for:

   - Building queries
   - Handling responses
   - Managing data transformations

1. **Build the application**

   After implementing your data access logic, build the application to ensure that all new code compiles correctly and integrates with existing functionality.

   ```powershell
   npm run dev
   ```

1. **Run and test**

   Run the application to verify that data is successfully read from the targeted Dataverse table. Test across multiple scenarios to ensure reliability and handle errors gracefully.

   ```powershell
    pac code run
   ```

## Create records in a Dataverse table
Follow these steps to successfully create records in Dataverse.

1. **Define your record type**

   First, create a TypeScript interface or type that includes the required OData annotation.

   ```typescript
   type CreateRecordPayload = { 
   // Required OData annotation 
   '@odata.type': string; 
   // Your record fields 
   name: string; 
   // ... other fields 
   };
   ```
2. **Create the record object**

   When preparing your record data, always include the OData type annotation. For standard Dataverse tables, the @odata.type annotation always follows the pattern of ‘#Microsoft.Dynamics.CRM.\<logicaltablename\>’

   ```typescript
   const newRecord: CreateRecordPayload = { 
   // Specify the entity type 
   '@odata.type': '#Microsoft.Dynamics.CRM.account',  // for Account entity   
   // Add your record data 
   name: 'New Account Name', 
   // ... other fields 
   };
   ```

3. **Submit the record**

   Use the appropriate service to create the record.

   ```typescript
   try { 
   const result = await YourEntityService.create(newRecord); 
   if (result.success) { 
    // Handle success 
   } 
   } catch (error) { 
   // Handle error 
   }
   ```
**Here is a complete example showing best practices:**

```typescript
// Type definition 
type CreateAccountPayload = { 
  '@odata.type': string; 
  name: string; 
  accountnumber?: string; 
  // ... other fields 
}; 

// Create record function 
async function createAccount(accountData: Omit<CreateAccountPayload, '@odata.type'>) { 
  const record: CreateAccountPayload = { 
    '@odata.type': '#Microsoft.Dynamics.CRM.account', 
    ...accountData 
  }; 

  try { 
    const result = await AccountsService.create(record); 
    if (!result.success) { 
      throw new Error(result.error?.message || 'Failed to create account'); 
    } 
    return result.data; 
  } catch (error) { 
    console.error('Error creating account:', error); 
    throw error; 
  } 
}
// Usage 
await createAccount({ 
  name: 'New Customer Account', 
  accountnumber: 'ACC-001' 
}); 
```


## Unsupported scenarios

The following features aren't yet supported:

- Option sets, Lookup fields, Polymorphic entities
- Dataverse Actions
- Deleting Dataverse datasources via PAC CLI
- Entity Metadata updates
- FetchXML support

### Related information

- [How to: Connect your code app to data](connect-to-data.md)  
- [Power Apps CLI](/power-platform/developer/cli/introduction)
