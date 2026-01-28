---
title: "dataApi reference for generative pages"
description: "The article provides dataApi reference for generative pages."
ms.date: 01/28/2026
author: jasongre
ms.author: jasongre
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - ruxyrezidenttm
---
# dataApi reference for generative pages

When you [generate a page using natural language](../../../../maker/model-driven-apps/generative-pages.md), the AI creates a React page in TypeScript. The generated page covers both the front-end user experience by selecting the right components and determining the best layout, and the corresponding business logic.

You can [view and edit the generated code to refine the output](../../../../maker/model-driven-apps/generative-pages.md#view-the-generated-code-iterate-and-publish). Data operations use a `dataApi` object that exposes the following public methods:

|Method|Description|
|---|---|
|[`createRow`](#createrow-method)|Creates a new row in the specified table.|
|[`updateRow`](#updaterow-method)|Updates an existing row in the specified table.|
|[`deleteRow`](#deleterow-method)|Deletes a row from the specified table.|
|[`retrieveRow`](#retrieverow-method)|Retrieves a row from the specified table with the specified options.|
|[`queryTable`](#querytable-method)|Queries a table with the specified options.|
|[`getChoices`](#getchoices-method)|Retrieves the choices for the specified choice column name.|


## `createRow` method

Creates a new row in the specified table.

### Parameters

Set values for these required parameters.

|Name|Type|Description|
|---|---|---|
|`tableName`|string|The logical name of the table to create the row in.|
|`row`|object|The row data to create.|

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, the result is the ID (Guid) value of the created row.

### Example

```typescript
// Define the row data to create new account
var row =
    {
        "name": "Sample Account",
        "creditonhold": false,
        "address1_latitude": 47.639583,
        "description": "This is the description of the sample account",
        "revenue": 5000000,
        "accountcategorycode": 1,
        "opendeals_date": new Date("2024-02-03T00:00:00Z")
    }

try {
  // Create a new account record
  const newAccountId = await dataApi.createRow("account", row);
  console.log("Account created with ID: " + newAccountId);

  // Create a contact with a lookup to an account
  const newContactId = await dataApi.createRow('contact', {
    firstname: 'John',
    lastname: 'Doe',
    emailaddress1: 'john.doe@contoso.com',
    _parentcustomerid_value: `/account(${newAccountId})`, // Lookup format
  });
}
catch (error) {
  console.log(error.message);
}
```


## `updateRow` method

Updates an existing row in the specified table.

### Parameters

Set values for these required parameters.

|Name|Type|Description|
|---|---|---|
|`tableName`|string|The logical name of the table to update the row in.|
|`rowId`|string|The ID of the row to update.|
|`row`|Object|The row data to update.|

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, it returns no value.

### Example

```typescript
let rowId = "5531d753-95af-e711-a94e-000d3a11e605"

// Define the row to update a record
var row =
    {
        "name": "Updated Sample Account ",
        "creditonhold": true,
        "address1_latitude": 47.639583,
        "description": "This is the updated description of the sample account",
        "revenue": 6000000,
        "accountcategorycode": 2
    }

// update the record

try {
   await dataApi.updateRow("account", rowId, row);
}
catch (error){
  console.log(error.message);
}
```

## `deleteRow` method

Deletes a row from the specified table.

### Parameters

Set values for these required parameters.

|Name|Type|Description|
|---|---|---|
|`tableName`|string|The logical name of the table to delete the row in.|
|`rowId`|string|The ID of the row to delete.|

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, it returns no value.

### Example

```typescript
let rowId = "5531d753-95af-e711-a94e-000d3a11e605";
try {
  await dataApi.deleteRow("account", rowId);
}
catch (error) {
  console.log(error.message);
}
```

## `retrieveRow` method

Retrieves a row from the specified table by using the specified options.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `tableName` | `string` | The logical name of the table to retrieve from |
| `options` | [RetrieveRowOptions](#retrieverowoptions) | Options for retrieving the row |

#### RetrieveRowOptions

| Name | Type | Description |
|------|------|-------------|
| `id` | `string` | The ID (Guid) of the row to retrieve |
| `select` | `string[]` | (Recommended) Array of column names to retrieve. If omitted, all columns are returned.  |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, an object containing the data of the record is returned, including all selected columns.

### Example

```typescript
// Retrieve an account with all columns
const account = await dataApi.retrieveRow('account', {
  id: '30dc51e9-947d-47d8-ad48-4fc48fba4a95',
});

// Retrieve specific columns only
const contact = await dataApi.retrieveRow('contact', {
  id: 'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
  select: ['firstname', 'lastname', '_parentcustomerid_value'],
});
```

## `queryTable` method

Queries a table by using the specified options.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `tableName` | `string` | The logical name of the table to query |
| `query` | [QueryTableOptions](#querytableoptions) | Options for querying the table |

#### QueryTableOptions

| Name | Type | Description |
|------|------|-------------|
| `select` | `string[]` |(Recommended) Array of column names to retrieve.  |
| `filter` | `string` | (Optional) OData filter expression (for example, `statecode eq 0`).  |
| `orderBy` | `string` | (Optional) OData orderby expression (for example, `name asc`, `createdon desc`).  |
| `pageSize` | `number` | (Optional) Maximum number of rows to return per page.  |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, the promise returns an object containing a data table with the results with these properties:

| Name | Type | Description |
|------|------|-------------|
| `rows` | `Object[]` | Array of row data |
| `hasMoreRows` | `boolean` | Indicates if there are more rows available |
| `loadMoreRows` | `function` | Function to load the next page of results. (Optional) |

### Example

```typescript
// Query tasks with options
const result = await dataApi.queryTable("task", {
    select: ["activityid", "subject", "scheduledend", "prioritycode", "statecode"],
    orderBy: "scheduledend asc",
    pageSize: 50,
    filter: "statecode eq 0"
});

// Query accounts with pagination
const pagedAccounts = await dataApi.queryTable('account', {
  select: ['name'],
  pageSize: 50,
});

console.log(`Page 1: ${pagedAccounts.rows.length} accounts`);

if (pagedAccounts.hasMoreRows && pagedAccounts.loadMoreRows) {
  const nextPage = await pagedAccounts.loadMoreRows();
  console.log(`Page 2: ${nextPage.rows.length} accounts`);
}
```

### Remarks

> [!NOTE]
> For best performance, always limit the number of columns returned by using the [QueryTableOptions](#querytableoptions) `select` property.

## `getChoices` method

Retrieves the choices for the specified choice column name.

### Parameters

This parameter is required.

| Name | Type | Description |
|------|------|-------------|
| `enumName` | `string` | The name of the choice column in the format `tablename-columnname` |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, it returns an array of the choice options. Each option has these properties:

|Name|Type|Description|
|---|---|---|
|`label`|string|The localized label value of the option.|
|`value`|number|The numeric value of the option.|

### Example

```typescript
// Returns the accountcategorycode column options from the account table
const categoryChoices = await dataApi.getChoices("account-accountcategorycode");
// Returns the statecode column options from the contact table
const stateChoices = await dataApi.getChoices('contact-statecode');
// Returns the statuscode column options from the account table
const statusChoices = await dataApi.getChoices('account-statuscode');
```
