---
title: "How to: SharePoint operations (preview)"
description: "Learn how to do SharePoint operations in code apps"
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 11/20/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: SharePoint operations (preview)

Use the Power Apps SDK to connect your code app to SharePoint and use the generated models and services to perform CRUD (Create, Read, Update, Delete) operations on a SharePoint list.  

## Prerequisites

- Power Apps code apps SDK [@microsoft/power-apps - npm package](https://www.npmjs.com/package/@microsoft/power-apps)
- [Power Apps CLI (PAC CLI)](/power-platform/developer/cli/introduction) version 1.50 or later
- [You must be connected to the environment using PAC CLI](/power-platform/developer/cli/introduction#manage-auth-profiles)

## Supported scenarios

The following scenarios are supported when connecting to SharePoint using the Power Apps SDK:

- Add SharePoint lists as data sources by using the PAC CLI
- Perform CRUD operations on a SharePoint list
- Get possible values for choice, lookup, or person/group columns

## Set up your code app

Before performing create, read, update, and delete (CRUD) operations in your code app, complete these setup steps.

### Ensure Power Apps SDK initialization before data calls

In your `App.tsx` file, implement logic that waits for the Power Apps SDK to fully initialize before performing any data operations. This approach prevents errors caused by uninitialized services or missing context.

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

### Add your SharePoint data source

Add your SharePoint data source by following the instructions in [Connect to data](connect-to-data.md).

### Import required types and services

When you add a data source, model and service files are automatically generated and placed in the `/generated/services/` folder. For example, if you add the `ChoicesTest1` list, the following files are created:

- `ChoicesTest1Model.ts` – Defines the data model for the ChoicesTest1 list.
- `ChoicesTest1Service.ts` – Provides service methods for interacting with data in the ChoicesTest1 list.

You can import and use these files in your App.tsx code like this:

```typescript
import { ChoicesTest1Service } from './generated/services/ChoicesTest1Service'; 
import type { ChoicesTest1 } from './generated/models/ChoicesTest1Model'; 
```

## Read records

This example fetches all items and sets the state.

```typescript
const loadRecords = async () => { 
  try { 
    const result = await ChoicesTest1Service.getAll(); 
    if (result.data) { 
      setRecords(result.data); // result.data is T[] 
    } else { 
      // handle empty or error 
    } 
  } catch (err) { 
    // handle error 
  } 
}; 
```

This example reads a single record.

```typescript
const fetchOne = async (id: string) => { 
  const r = await ChoicesTest1Service.get(id); 
  if (r.data) { 
    // r.data is a single record typed as ChoicesTest1 
  } 
}; 
```

## Create records

For the examples in the following steps, the example types from the model file are `ChoicesTest1`, `Choices1Value`, `personValue`, and `lookupValue`.

 1. Map selected IDs to expanded objects  
   
   > [!NOTE]
   > Generated models might include internal property names with `#` (for example: `Choices1#Id`) that are used for binding in forms but shouldn't be included in the payload sent to the SharePoint connector. When you update or create a row in your list, the SharePoint API expects you to provide the expanded object for referenced columns (author, editor, person/group columns, and so on) rather than just the IDs.
   Refer to the [SharePoint API documentation](/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints) for more information.
   
   ```typescript
   const choices1Obj = selectedChoices1Id 
   ? choices1Options.find(c => c.Id === selectedChoices1Id) 
   : undefined; 
   const personObj = selectedPersonClaims 
   ? personOptions.find(p => p.Claims === selectedPersonClaims) 
   : undefined; 
   const lookupObj = selectedLookupId 
   ? lookupOptions.find(l => l.Id === selectedLookupId) 
   : undefined; 
   ```
   
 1. Build payload and create
   
   Make sure to omit the properties containing `#`, include expanded objects for choice, lookups, and people, and add content type info if necessary. Use the generated model types to help build the payload.
   
   ```typescript
   // Content type (example static sample; retrieve dynamically if needed) 
   const contentTypeId = "0x0100..."; // replace with your content type id 
   
   const payload = { 
   Title: titleValue, 
   Choices1: choices1Obj, 
   Choices2: choices2Obj, 
   Choices3: choices3Obj, 
   person: personObj, 
   yesno: yesnoBoolean, 
   lookup: lookupObj,
   "{ContentType}": { 
      "@odata.type": "#Microsoft.Azure.Connectors.SharePoint.SPListExpandedContentType",
      Id: contentTypeId, 
      Name: "Item" 
   } 
   } as Partial<Omit<ChoicesTest1, "ID">>; 
   
   // create 
   const created = await ChoicesTest1Service.create(payload as Omit<ChoicesTest1, "ID">); 
   if (created.data) { 
   // success 
   } 
   ```
   
## Update records

Use `update(id, payload)` from the generated service file. Provide the same expanded objects as you would when creating a record.

For example:

```typescript
const updatePayload = { 
  Title: updatedTitle, 
  Choices1: updatedChoices1Obj, 
  // ... 
} as Partial<Omit<ChoicesTest1, "ID">>; 

await ChoicesTest1Service.update(recordId, updatePayload); 
```

## Delete records

Ensure `recordId` is the string ID the service expects. This is often a numeric item ID converted to string.

```typescript
await ChoicesTest1Service.delete(recordId); 
```

## Referenced entities (Choices / Lookup / Person)

To populate dropdowns, call `getReferencedEntity()`. SharePoint always returns a value array that contains objects from the referenced entity. You might want to normalize the response, as some connectors return a structure in the format `{ value: [] }`, while others provide the array directly.  

```typescript
// The first parameter is a search term, the second is the referenced entity name 
const res = await ChoicesTest1Service.getReferencedEntity("", "Choices1"); 
// normalize: 
const dataArray = (res.data as { value?: any[] })?.value || res.data; 
const options = Array.isArray(dataArray) ? dataArray : []; 
// map to select options: 
const selectOpts = options.map(o => ({ id: o.Id, label: o.Value })); 
```

## Unsupported scenarios

The Power Apps SDK and the PAC CLI allow CRUD operations on SharePoint lists, but don't support Document Processing APIs or actions like item synchronization or permission changes. You can add these features by creating a custom service file for your code app.