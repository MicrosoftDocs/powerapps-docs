---
title: "DataverseWebAPI.js sample library"
description: "This article describes the classes included in the DataverseWebAPI.js sample library used by samples in this group of single page application samples."
ms.date: 03/22/2025
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---
# DataverseWebAPI.js sample library

The [`DataverseWebAPI.js` sample library](#dataversewebapijs-sample-library-code) contains the implementation of the [`Client`](#client-class) and [`ChangeSet`](#changeset-class) classes for interacting with the Dataverse Web API in the [Web API Data operations Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md). This sample library demonstrates a set of methods to perform CRUD operations, batch requests, and other interactions with the Dataverse Web API.

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/JS/SPASample/src/scripts/DataverseWebAPI.js)

This library demonstrates:

- Using configuration data passed to the library
- Managing errors returned by the Dataverse Web API
- Helping keep code [DRY](https://wikipedia.org/wiki/Don%27t_repeat_yourself) and encourage reuse.
- A pattern of code reuse by:

   - All operations pass through a common [Send method](#sendrequest) that accepts a single [Request class](https://developer.mozilla.org/docs/Web/API/Request) instance and adds common headers including `Authorization`.
   - Providing a [Batch method](#batchrequests-continueonerror--false) that accepts [Request](https://developer.mozilla.org/docs/Web/API/Request) classes and returns [Response](https://developer.mozilla.org/docs/Web/API/Response) classes.
   - Each method provided represents a sample showing how to construct a `Request` instance that can be used with the `Batch` method.

> [!NOTE]
> This sample library is a helper that is used by all the Dataverse JavaScript client-side Web API samples, but it isn't an SDK. It's tested only to confirm that the samples that use it run successfully. This sample code is provided 'as-is' with no warranty for reuse.

This library doesn't:

- **Manage authentication**. It depends on a function passed from an application that provides the access token to use.
- **Provide for any code generation capabilities**. All methods used in the samples are written by hand. All business entity data uses JavaScript objects rather than a class representing the entity type.
- **Provide an object model for composing OData queries**. All queries show the OData query syntax as query parameters.

This library contains definitions of the following classes:

|Class|Description|
|---|---|
|[`Client`](#client-class)|Represents the Dataverse Web API Client. It provides methods to interact with the Dataverse Web API.|
|[`ChangeSet`](#changeset-class)|Represents a set of changes used with batch processing. All requests within the changeset must succeed or fail as a group.|

You can find the code for this library in [DataverseWebAPI.js sample library code](#dataversewebapijs-sample-library-code) and also on [GitHub at PowerApps-Samples/blob/master/dataverse/webapi/JS/SPASample/src/scripts/DataverseWebAPI.js](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/JS/SPASample/src/scripts/DataverseWebAPI.js).


## `Client` class

Represents the Dataverse Web API Client. It provides methods to interact with the Dataverse Web API.

### Client constructor

#### `constructor(baseUrl, getTokenFunc, version = "9.2")`

Creates an instance of the `Client`.

- **Parameters:**
  - `baseUrl` (string): The base URL for the Dataverse API.
  - `getTokenFunc` (function): A function that returns an access token.
  - `version` (string, optional): A string to override the default version. Default is `"9.2"`.

### Public Methods

> [!NOTE]
> All public methods are [asynchronous](https://developer.mozilla.org/docs/Learn_web_development/Extensions/Async_JS).

#### `Send(request)`

Sends an HTTP request using [fetch](https://developer.mozilla.org/docs/Web/API/Fetch_API) with required standard headers, including the `Authorization` headers. All other public methods use this method to send the request.

- **Parameters:**
  - `request` ([Request](https://developer.mozilla.org/docs/Web/API/Request)): The request to send.

- **Returns:** `Promise<Response|Error>`: The response from the fetch call or an error if the request fails.

#### `WhoAmI()`

Retrieves information about the current user by calling the [WhoAmI function](/power-apps/developer/data-platform/webapi/reference/whoami).

- **Returns:** `Promise<Object|Error>`: A promise that resolves to the user information in JSON format, or an error if the request fails.

#### `Create(entitySetName, data)`

Creates a new record in the specified entity set as described in [Create a table row using the Web API](create-entity-web-api.md).

- **Parameters:**
  - `entitySetName` (string): The name of the entity set where the new entity will be created.
  - `data` (Object): The data for the new entity.

- **Returns:** `Promise<Object|Error>`: A promise that resolves to an object containing the ID of the created entity, or an error if the request fails.

#### `Retrieve(entitySetName, id, query = null, includeAnnotations = true)`

Retrieves a record from the specified entity set by ID, with optional query options as described in [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md).

- **Parameters:**
  - `entitySetName` (string): The name of the entity set from which to retrieve the entity.
  - `id` (string): The ID of the entity to retrieve.
  - `query` (string, optional): The OData query options to apply.
  - `includeAnnotations` (boolean, optional): Whether OData annotations are returned in the response. Default value is `true`.

- **Returns:** `Promise<Object|Error>`: A promise that resolves to the retrieved entity in JSON format, or an error if the request fails.

#### `Refresh(record, primarykeyName)`

Refreshes the given record by fetching the latest data from the server using [conditional retrieval](perform-conditional-operations-using-web-api.md#conditional-retrievals).

- **Parameters:**
  - `record` (Object): The record to refresh. Must contain `@odata.etag` and `@odata.context` properties.
  - `primarykeyName` (string): The name of the primary key property in the record.

- **Returns:** `Promise<Object>`: The refreshed record.

#### `CreateRetrieve(entitySetName, data, query, includeAnnotations = true)`

Creates and retrieves a record from the specified entity set as described in [create with data returned](create-entity-web-api.md#create-with-data-returned).

- **Parameters:**
  - `entitySetName` (string): The name of the entity set.
  - `data` (Object): The data to be sent in the request body.
  - `query` (string, optional): The query string to be appended to the entity set URL.
  - `includeAnnotations` (boolean, optional): Whether to include OData annotations in the response. Default value is `true`.

- **Returns:** `Promise<Object>`: The response data as a JSON object.

#### `RetrieveMultiple(collectionResource, query, maxPageSize = 100, includeAnnotations = true)`

Retrieves multiple records from a specified entity set collection with optional query parameters as described in [use OData to query data](query/overview.md).

- **Parameters:**
  - `collectionResource` (string): The name of the entity set or a filtered collection expression to retrieve records from.
  - `query` (string): The OData query options to apply.
  - `maxPageSize` (number, optional): The maximum number of records to retrieve per page. Default is `100`.
  - `includeAnnotations` (boolean, optional): Whether to include OData annotations in the response. Default value is `true`.

- **Returns:** `Promise<object>`: The response from the server containing the retrieved entities.

#### `GetNextLink(nextLink, maxPageSize = 100, includeAnnotations = true)`

Retrieves the next page of records from a specified entity set collection using the `@odata.nextLink` value as described in [page results](query/page-results.md).

- **Parameters:**
  - `nextLink` (string): The `@odata.nextLink` value from the previous response.
  - `maxPageSize` (number, optional): The maximum number of records to retrieve per page. Default is `100`.
  - `includeAnnotations` (boolean, optional): Whether to include OData annotations in the response. Default value is `true`.

- **Returns:** `Promise<object>`: The response from the server containing the retrieved entities.

#### `FetchXml(entitySetName, fetchXml)`

Asynchronously fetches data from a specified entity set using FetchXML as described in [use FetchXml to retrieve data](../fetchxml/retrieve-data.md?tabs=webapi).

- **Parameters:**
  - `entitySetName` (string): The name of the entity set to query.
  - `fetchXml` (string): The FetchXML query string.

- **Returns:** `Promise<Object>`: The JSON response from the server.

#### `GetCollectionCount(collectionResource)`

Asynchronously retrieves the count of items in a specified collection as described in [count rows](query/count-rows.md).

- **Parameters:**
  - `collectionResource` (string): The resource URL of the collection.

- **Returns:** `Promise<number>`: The count of items in the collection, up to `5000`.

#### `Update(entitySetName, id, data, etag = null)`

Updates a record in the specified entity set by ID with the provided data as described in [basic update](update-delete-entities-using-web-api.md#basic-update).

- **Parameters:**
  - `entitySetName` (string): The name of the entity set where the record exists.
  - `id` (string): The ID of the record to update.
  - `data` (Object): The data to update the record with.
  - `etag` (string, optional): Specify the etag value to prevent update when a newer record exists.

- **Returns:** `Promise<Response|Error>`: A promise that resolves to the response of the update operation, or an error if the request fails.

#### `Delete(entitySetName, id, etag = null)`

Deletes an entity from the specified entity set by ID as described by [basic update](update-delete-entities-using-web-api.md#basic-delete)

- **Parameters:**
  - `entitySetName` (string): The name of the entity set from which to delete the entity.
  - `id` (string): The ID of the entity to delete.
  - `etag` (string, optional): Specify the etag value to prevent delete when a newer record exists.

- **Returns:** `Promise<Response|Error>`: A promise that resolves to the response of the delete operation, or an error if the request fails.

#### `SetValue(entitySetName, id, columnName, value)`

Sets the value of a specified column for a given record as described in [update a single property value](update-delete-entities-using-web-api.md#update-a-single-property-value).

- **Parameters:**
  - `entitySetName` (string): The name of the entity set.
  - `id` (string): The ID of the record.
  - `columnName` (string): The logical name of the column to set the value for.
  - `value` (*): The value to set for the specified column.

- **Returns:** `Object`: The response from the server.

#### `GetValue(entitySetName, id, columnName)`

Retrieves the value of a specified column for a given record as described in [retrieve a single property value](retrieve-entity-using-web-api.md#retrieve-a-single-property-value)

- **Parameters:**
  - `entitySetName` (string): The name of the entity set.
  - `id` (string): The ID of the record.
  - `columnName` (string): The name of the column to retrieve the value from.

- **Returns:** `Object`: The response from the server.

#### `Associate(targetSetName, targetId, navigationProperty, relatedSetName, relatedId)`

Associates records by creating data in the relationship to link them as described in [add a record to a collection](associate-disassociate-entities-using-web-api.md#add-a-record-to-a-collection).

- **Parameters:**
  - `targetSetName` (string): The name of the target entity set.
  - `targetId` (string|number): The ID of the target record.
  - `navigationProperty` (string): The navigation property that defines the relationship.
  - `relatedSetName` (string): The name of the related entity set.
  - `relatedId` (string|number): The ID of the record to associate with the target.

- **Returns:** `Promise<object>`: The response from the server after creating the association.

#### `Disassociate(targetSetName, targetId, navigationProperty, relatedId)`

Disassociates a record from another record by deleting data in the relationship to link them as described in [remove a record from a collection](associate-disassociate-entities-using-web-api.md#remove-a-record-from-a-collection).

- **Parameters:**
  - `targetSetName` (string): The name of the target entity set.
  - `targetId` (string|guid): The ID of the target record.
  - `navigationProperty` (string): The navigation property that defines the relationship.
  - `relatedId` (string|guid): The ID of the related record.

- **Returns:** `Promise<object>`: The response from the server after deleting the association.


#### `getBatchBody(request, id, inChangeSet = false)`

For internal use only. This method is public because it's used by the [ChangeSet class](#changeset-class). There are no scenarios where you need to use this method while using this library.


#### `Batch(requests, continueOnError = false)`

Sends a batch request containing multiple ([Request](https://developer.mozilla.org/docs/Web/API/Request) or [ChangeSet](#changeset-class) items as described in [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md).

- **Parameters:**
  - `requests` (Array&lt;([Request](https://developer.mozilla.org/docs/Web/API/Request)|[ChangeSet](#changeset-class)&gt;): An array of `Request` or `ChangeSet` items to be included in the batch request.
  - `continueOnError` (boolean, optional): A flag indicating whether to continue processing subsequent requests if an error occurs. Default is `false`.

- **Returns:** `Promise<Array<Response>>`: The parsed response from the batch request.

## `ChangeSet` class

Represents a set of changes used with batch processing. All requests within the changeset must succeed or fail as a group.

### ChangeSet constructor

#### `constructor(requests)`

Creates an instance of `ChangeSet`.

- **Parameters:**
  - `requests` (Array&lt;Request&gt;): An array of [Request](https://developer.mozilla.org/docs/Web/API/Request) objects.

### Properties

- `requests` (Array&lt;Request&gt;): The array of [Request](https://developer.mozilla.org/docs/Web/API/Request) objects in the change set.

### Methods

- `getChangeSetText(batchId)`: For internal use only. Gets the text for the changeset in the `$batch` operation. This method is public because it's used by the [Client class Batch method](#batchrequests-continueonerror--false). There are no scenarios where you need to use this method directly with this library.

## DataverseWebAPI.js sample library code

The following is the code for the DataverseWebAPI.js sample library

:::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/SPASample/src/scripts/DataverseWebAPI.js":::

### See also

[Use the Dataverse Web API](overview.md)   
[Web API Samples](web-api-samples.md)   
[Web API Samples (C#)](web-api-samples-csharp.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
