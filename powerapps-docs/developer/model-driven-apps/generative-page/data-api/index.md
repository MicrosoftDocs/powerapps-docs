---
title: "dataApi reference for generative pages"
description: "The article provides dataApi reference for generative pages."
ms.date: 01/07/2026
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

When you [generate a page using natural language](../../../../maker/model-driven-apps/generative-pages.md), the AI generates a React page in TypeScript that covers both the front-end user experience by selecting the right components and determining the best layout, and the corresponding business logic.

You have the opportunity to [view and edit the generated code to refine the output](../../../../maker/model-driven-apps/generative-pages.md#view-the-generated-code-iterate-and-publish). Data operations use a `dataApi` object that exposes the following public methods:

|Method|Description|
|---|---|
|[`createRow`](#createrow-method)|Creates a new row in the specified table.|
|[`updateRow`](#updaterow-method)|Updates an existing row in the specified table.|
|[`deleteRow`](#deleterow-method)|Deletes a row from the specified table.|
|[`retrieveRow`](#retrieverow-method)|Deletes a row from the specified table with the specified options.|
|[`queryTable`](#querytable-method)|Queries a table with the specified options.|
|[`getChoices`](#getchoices-method)|Retrieves the choices for the specified choice column name.|


## `createRow` method

Creates a new row in the specified table.
<!-- Compare with https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi/createrecord -->

### Parameters

Set values for these required parameters.

|Name|Type|Description|
|---|---|---|
|`tableName`|string|The logical name of the table to create the row in.|
|`row`|object|The row data to create.|

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, the result returned is the ID value of the created row.

<!-- ### Remarks

TODO: Add any special details to help customers succeed

-->

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
<!-- Compare with https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi/updaterecord -->

### Parameters

Set values for these required parameters.

|Name|Type|Description|
|---|---|---|
|`tableName`|string|The logical name of the table to update the row in.|
|`rowId`|string|The ID of the row to update.|
|`row`|Object|The row data to create.|

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, no value is returned.

<!-- ### Remarks

TODO: Add any special details to help customers succeed

-->

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
<!-- Compare with https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi/deleterecord -->

### Parameters

Set values for these required parameters.

|Name|Type|Description|
|---|---|---|
|`tableName`|string|The logical name of the table to delete the row in.|
|`rowId`|string|The ID of the row to delete.|

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, no value is returned.

<!-- ### Remarks

TODO: Add any special details to help customers succeed

-->

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

Deletes a row from the specified table with the specified options.
<!-- Compare to https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi/retrieverecord -->

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `tableName` | `string` | The logical name of the table to retrieve from |
| `options` | `RetrieveRowOptions` | Options for retrieving the row |

#### RetrieveRowOptions

| Name | Type | Description |
|------|------|-------------|
| `id` | `string` | The ID (Guid) of the row to retrieve |
| `select` | `string[]` | Array of column names to retrieve. If omitted, all columns are returned. (Optional) |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, an object containing the data of the record is returned.

<!-- ### Remarks
TODO: Add any special details to help customers succeed
-->

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

Queries a table with the specified options.
<!-- Compare to https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi/retrievemultiplerecords -->

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `tableName` | `string` | The logical name of the table to query |
| `query` | `QueryTableOptions` | Options for querying the table |

#### QueryTableOptions

| Name | Type | Description |
|------|------|-------------|
| `select` | `string[]` | Array of column names to retrieve. (Optional) |
| `filter` | `string` | OData filter expression. (Optional) |
| `orderBy` | `string` | OData orderby expression (e.g., `name asc`, `createdon desc`). (Optional) |
| `pageSize` | `number` | Maximum number of rows to return per page. (Optional) |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, an object containing a data table with the results is returned.

<!-- 
### Remarks

TODO: Add any special details to help customers succeed.
-->

### Example

```typescript
const result = await dataApi.queryTable("task", {
    select: ["activityid", "subject", "scheduledend", "prioritycode", "statecode"],
    orderBy: "scheduledend asc",
    pageSize: 50,
    filter: "statecode eq 0" // Only active tasks
});
```

## `getChoices` method

Retrieves the choices for the specified choice column name.

### Parameters

This parameter is required.

| Name | Type | Description |
|------|------|-------------|
| `enumName` | `string` | The name of the choice column in format `tablename-columnname` |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, an array of the choice options is returned. Each option has these properties:

|Name|Type|Description|
|---|---|---|
|`label`|string|The localized label value of the option.|
|`value`|number|The numeric value of the option.|

<!-- 
### Remarks

TODO: Add any special details to help customers succeed

Please review the sample_RetrieveOptions Custom API example I've published here: https://github.com/JimDaly/DataversePowerAutomateHelpers?tab=readme-ov-file#sample_retrieveoptions.

This describes my expectations for a function that retrieves options from metadata.

> This Custom API addresses the need that many people have expressed to be able to retrieve the valid options for a given entity attribute. The Web API doesn't expose the equivalent to the RetrieveOptionSet message found in the SDK. But even this message is limited in capability because it only returns information about Global optionsets. There are many 'local' optionsets which are not defined globally.

> Retrieving information about local optionsets in the Web API is made more complicated because the OptionSet property isn't part of the base AttributeMetadata class. It is only found in specific classes derived from AttributeMetadata. This requires that you know the sub-type before you send your request and cast the attribute in the URL, and there are five different types of attributes with options.

> For example, if you want to get the options for an ordinary PicklistAttributeMetadata attribute, you need to compose a URL like this:

> GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='accountcategorycode')/Microsoft.Dynamics.CRM.PicklistAttributeMetadata/OptionSet?$select=Options

> However, the following classes also support OptionSets:

> BooleanAttributeMetadata
> MultiSelectPicklistAttributeMetadata
> StateAttributeMetadata
> StatusAttributeMetadata
> More information Query metadata using the Web API > Retrieving attributes (https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query-metadata-web-api#retrieving-attributes) -->

### Example

```typescript
const categoryChoices = await dataApi.getChoices("account-accountcategorycode");

const stateChoices = await dataApi.getChoices('account-statecode');

const statusChoices = await dataApi.getChoices('account-statuscode');
```
