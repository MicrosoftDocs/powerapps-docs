---
title: "Connector methods for generative pages"
description: "Learn how to use the dataApi connector methods in generative pages."
ms.date: 10/19/2026
author: jasongre
ms.author: jasongre
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - ruxyrezidenttm
ai-usage: ai-assisted
---
# Connector methods for generative pages

Use the connector methods of the `dataApi` object to work with data exposed by a Power Platform connector bound to the page.

> [!NOTE]
> Connector methods are optional in the shared `dataApi` contract. Some hosts don't implement them, so check that a method exists before calling it. A method being present doesn't mean the page has a connector bound to it, or that the connection, dataset, table, or operation is configured, authorized, or permitted as expected.
>
> Unlike the action and function methods, connector methods reject the returned promise when a call fails — for example, when the connection reference can't be resolved, the connection isn't authorized and the user doesn't complete the consent prompt, or the connector returns an error status. `executeConnectorOperation` resolves with `ok: false` for most error statuses, but still rejects for a missing operation, an unauthorized connection (403) without completed consent, or a transport failure. Wrap connector calls in `try`/`catch`.

|Method|Description|
|---|---|
|[`createConnectorRow`](#createconnectorrow-method)|Creates a new row in the specified connector table.|
|[`deleteConnectorRow`](#deleteconnectorrow-method)|Deletes a row from the specified connector table.|
|[`executeConnectorOperation`](#executeconnectoroperation-method)|Invokes a named operation exposed by a REST (operation-keyed) connector, such as Office 365 Users.|
|[`getConnectorSwagger`](#getconnectorswagger-method)|Retrieves the Swagger (OpenAPI) definition for the connector.|
|[`getConnectorTableSchema`](#getconnectortableschema-method)|Retrieves the schema for a table (also called an entity or list) exposed by the connector.|
|[`listConnectorDatasets`](#listconnectordatasets-method)|Lists the datasets available for the connector.|
|[`listConnectorOperations`](#listconnectoroperations-method)|Lists the operations exposed by a REST (operation-keyed) connector.|
|[`listConnectorTables`](#listconnectortables-method)|Lists the tables available in the specified connector dataset.|
|[`queryConnectorTable`](#queryconnectortable-method)|Queries a table exposed by the connector with the specified options.|
|[`retrieveConnectorRow`](#retrieveconnectorrow-method)|Retrieves a single row from the specified connector table.|
|[`updateConnectorRow`](#updateconnectorrow-method)|Updates an existing row in the specified connector table.|

## `queryConnectorTable` method

Queries a table exposed by the connector by using the specified options.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page (for example, `sp_shared_sharepointonline`). |
| `dataset` | `string` | The dataset that contains the table, such as a SharePoint site URL. |
| `tableName` | `string` | The table's internal name, from the `name` property returned by [`listConnectorTables`](#listconnectortables-method). Don't use the display name. |
| `options` | [QueryConnectorTableOptions](#queryconnectortableoptions) | Options for querying the table. |

#### QueryConnectorTableOptions

| Name | Type | Description |
|------|------|-------------|
| `select` | `string[]` | (Recommended) Array of column names to retrieve. |
| `filter` | `string` | (Optional) Filter expression supported by the connector. |
| `orderBy` | `string` | (Optional) Order-by expression supported by the connector. |
| `top` | `number` | (Optional) Maximum number of rows to return. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, the promise returns an object containing a data table with the results with these properties:

| Name | Type | Description |
|------|------|-------------|
| `rows` | `Object[]` | Array of row data. |
| `hasMoreRows` | `boolean` | Indicates if there are more rows available. |

`queryConnectorTable` returns a single page of results. It doesn't return a continuation function, and there's currently no supported way to fetch the next page. When `hasMoreRows` is `true`, more rows matched than were returned. Narrow the query with `filter`, or tell the user that the results are incomplete.

### queryConnectorTable example

```typescript
if (!dataApi.listConnectorTables || !dataApi.queryConnectorTable) {
  throw new Error("Connector methods aren't available on this page.");
}

const tables = await dataApi.listConnectorTables(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing"
);
const documentsTable = tables.find((table) => table.displayName === "Documents");
if (!documentsTable) {
  throw new Error("The Documents table wasn't found in this dataset.");
}
const documentsTableName = documentsTable.name;

const result = await dataApi.queryConnectorTable(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing",
  documentsTableName,
  {
    select: ["Title", "Modified"],
    top: 50,
  }
);
```

The following examples assume `documentsTableName` holds the table's `name` from `listConnectorTables`, as shown above.

## `listConnectorTables` method

Lists the tables (lists or entities) available in the specified connector dataset.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |
| `dataset` | `string` | The dataset to list tables for. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing an array of table information. Each entry has these properties:

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | The internal name of the table. |
| `displayName` | `string` | The display name of the table. |

### listConnectorTables example

```typescript
const tables = await dataApi.listConnectorTables?.(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing"
);
```

## `listConnectorDatasets` method

Lists the datasets available for the connector, such as the SharePoint sites a connection can access.

### Parameters

Set a value for this required parameter.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing an array of dataset information. Each entry has these properties:

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | The internal name or identifier of the dataset. |
| `displayName` | `string` | The display name of the dataset. |

### listConnectorDatasets example

```typescript
const datasets = await dataApi.listConnectorDatasets?.("sp_shared_sharepointonline");
```

## `listConnectorOperations` method

Lists the operations defined in the connector's Swagger definition, excluding operations marked internal, sorted by display name. This method is most useful for REST (operation-keyed) connectors such as Office 365 Users. For tabular connectors, use the query and row methods instead of the operations this method lists.

### Parameters

Set a value for this required parameter.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing an array of operation information. Each entry has these properties:

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | The operation ID as defined in the connector's Swagger definition. Pass this value to `executeConnectorOperation`. |
| `displayName` | `string` | The human-readable operation name for display, such as the Swagger summary. Falls back to `name` if no summary is defined. |

### listConnectorOperations example

```typescript
const operations = await dataApi.listConnectorOperations?.("sp_shared_sharepointonline");
```

## `getConnectorSwagger` method

Retrieves the Swagger (OpenAPI) definition for the connector, which describes the operations it exposes. The returned document describes the connector overall. It doesn't include per-table column schemas for tabular connectors. Use [`getConnectorTableSchema`](#getconnectortableschema-method) for that information.

### Parameters

Set a value for this required parameter.

| Name | Type | Description |
|------|------|-------------|
| `connectorApiId` | `string` | The connector API identifier, such as `/providers/Microsoft.PowerApps/apis/shared_sharepointonline`. This identifier is different from the connection reference logical name (`connectorLogicalName`) used by most other connector methods. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the connector's Swagger definition as an object.

### getConnectorSwagger example

```typescript
if (!dataApi.getConnectorSwagger) {
  throw new Error("getConnectorSwagger isn't available on this page.");
}

const swagger = await dataApi.getConnectorSwagger(
  "/providers/Microsoft.PowerApps/apis/shared_sharepointonline"
);
```

## `getConnectorTableSchema` method

Retrieves the schema (column definitions) for a table exposed by the connector. The connector defines the schema it returns, and it varies by connector. Don't assume it includes every dynamic column a table might contain.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |
| `dataset` | `string` | The dataset that contains the table. |
| `tableName` | `string` | The table's internal name, from the `name` property returned by [`listConnectorTables`](#listconnectortables-method). Don't use the display name. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the table's schema as an object.

### getConnectorTableSchema example

```typescript
if (!dataApi.getConnectorTableSchema) {
  throw new Error("getConnectorTableSchema isn't available on this page.");
}

const schema = await dataApi.getConnectorTableSchema(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing",
  documentsTableName // from listConnectorTables
);
```

## `retrieveConnectorRow` method

Retrieves a single row from the specified connector table.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |
| `dataset` | `string` | The dataset that contains the table. |
| `tableName` | `string` | The table's internal name, from the `name` property returned by [`listConnectorTables`](#listconnectortables-method). Don't use the display name. |
| `id` | `string` | The ID of the row to retrieve. |
| `options` | [RetrieveConnectorRowOptions](#retrieveconnectorrowoptions) | (Optional) Options for retrieving the row. |

#### RetrieveConnectorRowOptions

| Name | Type | Description |
|------|------|-------------|
| `select` | `string[]` | (Recommended) Array of column names to retrieve. If omitted, no `$select` projection is sent — the connector determines which columns to return and doesn't guarantee to return every column in the row. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the row data.

### retrieveConnectorRow example

```typescript
if (!dataApi.retrieveConnectorRow) {
  throw new Error("retrieveConnectorRow isn't available on this page.");
}

const row = await dataApi.retrieveConnectorRow(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing",
  documentsTableName, // from listConnectorTables
  "1"
);
```

## `createConnectorRow` method

Creates a new row in the specified connector table.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |
| `dataset` | `string` | The dataset that contains the table. |
| `tableName` | `string` | The table's internal name, from the `name` property returned by [`listConnectorTables`](#listconnectortables-method). Don't use the display name. |
| `row` | `object` | The row data to create. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the response body returned by the connector, if any. Depending on the connector, this value can be the created row, a partial row, or no value.

### createConnectorRow example

```typescript
if (!dataApi.createConnectorRow) {
  throw new Error("createConnectorRow isn't available on this page.");
}

const newRow = await dataApi.createConnectorRow(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing",
  documentsTableName, // from listConnectorTables
  { Title: "New document" }
);
```

## `updateConnectorRow` method

Updates an existing row in the specified connector table.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |
| `dataset` | `string` | The dataset that contains the table. |
| `tableName` | `string` | The table's internal name, from the `name` property returned by [`listConnectorTables`](#listconnectortables-method). Don't use the display name. |
| `id` | `string` | The ID of the row to update. |
| `row` | `object` | The row data to update. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the response body returned by the connector, if any. Depending on the connector, this value can be the updated row, a partial row, or no value. To read the row's current values, call [`retrieveConnectorRow`](#retrieveconnectorrow-method).

### updateConnectorRow example

```typescript
if (!dataApi.updateConnectorRow) {
  throw new Error("updateConnectorRow isn't available on this page.");
}

const updatedRow = await dataApi.updateConnectorRow(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing",
  documentsTableName, // from listConnectorTables
  "1",
  { Title: "Updated title" }
);
```

## `deleteConnectorRow` method

Deletes a row from the specified connector table.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |
| `dataset` | `string` | The dataset that contains the table. |
| `tableName` | `string` | The table's internal name, from the `name` property returned by [`listConnectorTables`](#listconnectortables-method). Don't use the display name. |
| `id` | `string` | The ID of the row to delete. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the result of the operation. When the operation succeeds, it returns no value.

### deleteConnectorRow example

```typescript
if (!dataApi.deleteConnectorRow) {
  throw new Error("deleteConnectorRow isn't available on this page.");
}

await dataApi.deleteConnectorRow(
  "sp_shared_sharepointonline",
  "https://contoso.sharepoint.com/sites/Marketing",
  documentsTableName, // from listConnectorTables
  "1"
);
```

## `executeConnectorOperation` method

Invokes a named operation exposed by a REST (operation-keyed) connector, such as HTTP, Teams send-message, or Office 365 Users. Tabular connectors should use the query and row CRUD methods instead.

### Parameters

Set values for these required parameters.

| Name | Type | Description |
|------|------|-------------|
| `connectorLogicalName` | `string` | The logical name of the connection reference bound to the page. |
| `operationName` | `string` | The operation ID as defined in the connector's Swagger definition. |
| `parameters` | `object` | The parameters required by the operation. Pass an empty object (`{}`) if the operation takes no parameters — this parameter is required even when there's nothing to send. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing the operation result with these properties. The promise rejects if the connection reference can't be resolved, the connector's Swagger definition can't be retrieved, the operation isn't found in it, the call can't be dispatched, or the connection isn't authorized (HTTP 403) and the user doesn't complete the connection consent prompt.

| Name | Type | Description |
|------|------|-------------|
| `ok` | `boolean` | `true` when the underlying HTTP status is less than 400. This status includes redirect (3xx) statuses, so don't treat `ok` alone as proof the operation returned data — also check `status` or inspect `body`. |
| `status` | `number` | The raw HTTP status code returned by the connector. |
| `body` | `unknown` | The parsed JSON response body, or the raw string if the body isn't JSON. |

### executeConnectorOperation example

The following example assumes an operation named `CopyFile` that accepts `sourceUrl` and `destinationUrl` parameters. Verify the operation ID and its parameters against the connector's own Swagger definition (for example, with [`listConnectorOperations`](#listconnectoroperations-method) or [`getConnectorSwagger`](#getconnectorswagger-method)) before using it, since available operations and their parameters vary by connector.

```typescript
if (!dataApi.executeConnectorOperation) {
  throw new Error("executeConnectorOperation isn't available on this page.");
}

try {
  const result = await dataApi.executeConnectorOperation(
    "sp_shared_sharepointonline",
    "CopyFile",
    { sourceUrl: "/sites/Marketing/Shared Documents/file.docx", destinationUrl: "/sites/Sales/Shared Documents/file.docx" }
  );

  if (result.ok) {
    console.log(result.body);
  }
  else {
    console.log(result.status);
  }
}
catch (error) {
  console.log(error);
}
```
