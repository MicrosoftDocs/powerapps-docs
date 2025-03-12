---
title: "DataverseWebAPI.js sample library"
description: "This article describes the classes included in the DataverseWebAPI.js sample library used by samples in this group of single page application samples."
ms.date: 03/30/2025
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---
# DataverseWebAPI.js sample library

The `DataverseWebAPI.js` file contains the implementation of the `Client` class and other related classes for interacting with the Dataverse Web API in the [Web API Data operations Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md). This library provides a set of methods to perform CRUD operations, batch requests, and other interactions with the Dataverse Web API.

This library contains definitions of the following classes:

|Class|Description|
|---|---|
|[`Client`](#client)|The `Client` class represents the Dataverse Web API Client. It provides methods to interact with the Dataverse Web API.|
|[`WebAPIRequest`](#webapirequest)|Represents a web API request used for batch processing.|
|[`WebAPIResponse`](#webapiresponse)|Represents a web API response used for batch processing.|
|[`ChangeSet`](#changeset)|Represents a set of changes used with batch processing. All requests within the changeset must succeed or fail as a group.|

You can find the code for this library below in [DataverseWebAPI.js sample library code](#dataversewebapijs-sample-library-code)


## Client class

The `Client` class represents the Dataverse Web API Client. It provides methods to interact with the Dataverse Web API.

### Constructor

#### `constructor(baseUrl, getTokenFunc, version = "v9.2")`

Creates an instance of the `Client`.

- **Parameters:**
  - `baseUrl` (string): The base URL for the Dataverse API.
  - `getTokenFunc` (function): A function that returns an access token.
  - `version` (string, optional): A string to override the default version. Default is `"v9.2"`.

### Methods

#### `async Send(method, resource, query = null, data = null, extraHeaders = null)`

Sends an HTTP request with the specified method, URL, data, and extra headers if needed.

- **Parameters:**
  - `method` (string): The HTTP method to use (e.g., 'GET', 'POST').
  - `resource` (string): The resource to which the request is sent. The URL before '?'.
  - `query` (string, optional): The query string parameters to include in the request. The value after '?'.
  - `data` (Object, optional): The data to be sent as the request body.
  - `extraHeaders` (Object, optional): Additional headers to include in the request.

- **Returns:** `Promise<Response|Error>`: The response from the fetch call or an error if the request fails.

#### `async WhoAmI()`

Retrieves information about the current user by calling the "WhoAmI" message.

- **Returns:** `Promise<Object|Error>`: A promise that resolves to the user information in JSON format, or an error if the request fails.

#### `async Create(entitySetName, data)`

Creates a new record in the specified entity set.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set where the new entity will be created.
  - `data` (Object): The data for the new entity.

- **Returns:** `Promise<Object|Error>`: A promise that resolves to an object containing the ID of the created entity, or an error if the request fails.

#### `async Retrieve(entitySetName, id, query = null, includeAnnotations = true)`

Retrieves a record from the specified entity set by ID, with optional query options.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set from which to retrieve the entity.
  - `id` (string): The ID of the entity to retrieve.
  - `query` (string, optional): The OData query options to apply.
  - `includeAnnotations` (boolean, optional): Whether OData annotations are returned in the response. Default value is `true`.

- **Returns:** `Promise<Object|Error>`: A promise that resolves to the retrieved entity in JSON format, or an error if the request fails.

#### `async Refresh(record, primarykeyName)`

Refreshes the given record by fetching the latest data from the server.

- **Parameters:**
  - `record` (Object): The record to refresh. Must contain `@odata.etag` and `@odata.context` properties.
  - `primarykeyName` (string): The name of the primary key property in the record.

- **Returns:** `Promise<Object>`: The refreshed record.

#### `async CreateRetrieve(entitySetName, data, query, includeAnnotations = true)`

Creates and retrieves a record from the specified entity set.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set.
  - `data` (Object): The data to be sent in the request body.
  - `query` (string, optional): The query string to be appended to the entity set URL.
  - `includeAnnotations` (boolean, optional): Whether to include OData annotations in the response. Default value is `true`.

- **Returns:** `Promise<Object>`: The response data as a JSON object.

#### `async RetrieveMultiple(collectionResource, query, maxPageSize = 100, includeAnnotations = true)`

Retrieves multiple records from a specified entity set collection with optional query parameters.

- **Parameters:**
  - `collectionResource` (string): The name of the entity set or a filtered collection expression to retrieve records from.
  - `query` (string): The OData query options to apply.
  - `maxPageSize` (number, optional): The maximum number of records to retrieve per page. Default is `100`.
  - `includeAnnotations` (boolean, optional): Whether to include OData annotations in the response. Default value is `true`.

- **Returns:** `Promise<object>`: The response from the server containing the retrieved entities.

#### `async GetNextLink(nextLink, maxPageSize = 100, includeAnnotations = true)`

Retrieves the next page of records from a specified entity set collection using the `@odata.nextLink` value.

- **Parameters:**
  - `nextLink` (string): The `@odata.nextLink` value from the previous response.
  - `maxPageSize` (number, optional): The maximum number of records to retrieve per page. Default is `100`.
  - `includeAnnotations` (boolean, optional): Whether to include OData annotations in the response. Default value is `true`.

- **Returns:** `Promise<object>`: The response from the server containing the retrieved entities.

#### `async FetchXml(entitySetName, fetchXml)`

Asynchronously fetches data from a specified entity set using FetchXML.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set to query.
  - `fetchXml` (string): The FetchXML query string.

- **Returns:** `Promise<Object>`: The JSON response from the server.

#### `async GetCollectionCount(collectionResource)`

Asynchronously retrieves the count of items in a specified collection.

- **Parameters:**
  - `collectionResource` (string): The resource URL of the collection.

- **Returns:** `Promise<number>`: The count of items in the collection, up to `5000`.

#### `async Update(entitySetName, id, data, etag = null)`

Updates a record in the specified entity set by ID with the provided data.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set where the record exists.
  - `id` (string): The ID of the record to update.
  - `data` (Object): The data to update the record with.
  - `etag` (string, optional): Specify the etag value to prevent update when a newer record exists.

- **Returns:** `Promise<Response|Error>`: A promise that resolves to the response of the update operation, or an error if the request fails.

#### `async Delete(entitySetName, id, etag = null)`

Deletes an entity from the specified entity set by ID.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set from which to delete the entity.
  - `id` (string): The ID of the entity to delete.
  - `etag` (string, optional): Specify the etag value to prevent delete when a newer record exists.

- **Returns:** `Promise<Response|Error>`: A promise that resolves to the response of the delete operation, or an error if the request fails.

#### `async SetValue(entitySetName, id, columnName, value)`

Sets the value of a specified column for a given record.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set.
  - `id` (string): The ID of the record.
  - `columnName` (string): The logical name of the column to set the value for.
  - `value` (*): The value to set for the specified column.

- **Returns:** `Object`: The response from the server.

#### `async GetValue(entitySetName, id, columnName)`

Retrieves the value of a specified column for a given record.

- **Parameters:**
  - `entitySetName` (string): The name of the entity set.
  - `id` (string): The ID of the record.
  - `columnName` (string): The name of the column to retrieve the value from.

- **Returns:** `Object`: The response from the server.

#### `async Associate(targetSetName, targetId, navigationProperty, relatedSetName, relatedId)`

Associates records by creating data in the relationship to link them.

- **Parameters:**
  - `targetSetName` (string): The name of the target entity set.
  - `targetId` (string|number): The ID of the target record.
  - `navigationProperty` (string): The navigation property that defines the relationship.
  - `relatedSetName` (string): The name of the related entity set.
  - `relatedId` (string|number): The ID of the record to associate with the target.

- **Returns:** `Promise<object>`: The response from the server after creating the association.

#### `async Disassociate(targetSetName, targetId, navigationProperty, relatedId)`

Disassociates a record from another record by deleting data in the relationship to link them.

- **Parameters:**
  - `targetSetName` (string): The name of the target entity set.
  - `targetId` (string|guid): The ID of the target record.
  - `navigationProperty` (string): The navigation property that defines the relationship.
  - `relatedId` (string|guid): The ID of the related record.

- **Returns:** `Promise<object>`: The response from the server after deleting the association.

#### `async SendRequest(request)`

Sends a web API request and returns the response.

- **Parameters:**
  - `request` (WebAPIRequest): The request object to be sent.

- **Returns:** `Promise<WebAPIResponse>`: The response from the web API.

#### `async Batch(requests, continueOnError = false)`

Sends a batch request containing multiple WebAPIRequest or ChangeSet items.

- **Parameters:**
  - `requests` (Array<WebAPIRequest|ChangeSet>): An array of WebAPIRequest or ChangeSet items to be included in the batch request.
  - `continueOnError` (boolean, optional): A flag indicating whether to continue processing subsequent requests if an error occurs. Default is `false`.

- **Returns:** `Promise<Array<WebAPIResponse>>`: The parsed response from the batch request.

## WebAPIRequest class

Represents a web API request used for batch processing.

### Constructor

#### `constructor(method, resource, query = null, body = null, headers = null, contentID = null)`

Creates an instance of `WebAPIRequest`.

- **Parameters:**
  - `method` (string): The HTTP method for the request (For example: 'GET', 'POST').
  - `resource` (string): The resource endpoint for the request.
  - `query` (string, optional): The query string for the request, if any.
  - `body` (Object, optional): The body of the request, if any.
  - `headers` (Object, optional): The headers for the request, if any.
  - `contentID` (string, optional): The content ID, if any.

### Properties

- `method` (string): The HTTP method for the request.
- `resource` (string): The resource endpoint for the request.
- `query` (string, optional): The query string for the request, if any.
- `headers` (Object, optional): The headers for the request, if any.
- `body` (Object, optional): The body of the request, if any.
- `contentID` (string, optional): The content ID, if any.

### Methods

- `getBatchBody(Id, inChangeSet = false)`: Generates the batch request body for the OData service.

## WebAPIResponse class

Represents a web API response used for batch processing.

### Constructor

#### `constructor()`

Creates an instance of `WebAPIResponse`.

### Properties

- `statusCode` (number): The status code of the response.
- `statusText` (string): The status text of the response.
- `headers` (Object): The headers of the response.
- `body` (Object): The body of the response.

### Methods

- `async init(response)`: Initializes the `WebAPIResponse` object with the response from the server.

## ChangeSet class

Represents a set of changes used with batch processing. All requests within the changeset must succeed or fail as a group.

### Constructor

#### `constructor(requests)`

Creates an instance of `ChangeSet`.

- **Parameters:**
  - `requests` (Array<WebAPIRequest>): An array of `WebAPIRequest` objects.

### Properties

- `requests` (Array<WebAPIRequest>): The array of `WebAPIRequest` objects in the change set.

### Methods

- `getChangeSetText(batchId)`: Gets the text for the changeset in the `$batch` operation.

## DataverseWebAPI.js sample library code

The following is the code for the DataverseWebAPI.js sample library

```javascript
/**
 * @class Client
 * @classdesc This class represents the Dataverse Web API Client.
 */
class Client {
  #baseUrl; // https://your-org.api.crm.dynamics.com
  #version; // v9.2
  #path; // /api/data/v9.2/
  #apiEndpoint; // https://your-org.api.crm.dynamics.com/api/data/v9.2/
  #getTokenFunc; // Function to get the token, passed in the constructor

  /**
   * Creates an instance of Client.
   *
   * @constructor
   * @param {string} baseUrl - The base URL for the Dataverse API.
   * @param {function} getTokenFunc - A function that returns an access token.
   * @param {string} version - A string to override the default version.
   */
  constructor(baseUrl, getTokenFunc, version = "v9.2") {
    this.#baseUrl = baseUrl;
    this.#version = version;
    this.#path = `/api/data/${this.#version}/`;
    this.#apiEndpoint = baseUrl + this.#path;
    this.#getTokenFunc = getTokenFunc;
  }

  //#region Validation Functions

  /**
   * Checks if a given string is a valid GUID.
   *
   * @param {string} str - The string to be tested.
   * @returns {boolean} - Returns true if the string is a valid GUID, otherwise false.
   */
  #isGUID(str) {
    const guidRegex =
      /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/;
    return guidRegex.test(str);
  }
  /**
   * Validates if a given variable is an object that can be used with JSON.stringify.
   *
   * @param {any} obj - The variable to be tested.
   * @returns {boolean} - Returns true if the variable is a valid object for JSON.stringify, otherwise false.
   */
  #isValidObjectForJSON(obj) {
    return obj !== null && typeof obj === "object" && !Array.isArray(obj);
  }
  /**
   * Validates if a given string is a valid XML document.
   *
   * @param {string} xmlString - The XML string to be tested.
   * @returns {boolean} - Returns true if the string is a valid XML document, otherwise false.
   */
  #isValidXML(xmlString) {
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlString, "text/xml");
    const parserError = xmlDoc.getElementsByTagName("parsererror");
    return parserError.length === 0;
  }
  /**
   * Validates if a given string is a weak ETag.
   *
   * @param {string} etag - The ETag string to be tested.
   * @returns {boolean} - Returns true if the string is a valid weak ETag, otherwise false.
   */
  #isValidWeakETag(etag) {
    const weakEtagRegex = /^W\/"([0-9a-fA-F]+)"$/;
    const result = weakEtagRegex.test(etag);
    if (!result) {
      console.error(`The etag ${etag} is not a valid weak ETag.`);
    }
    return result;
  }

  //#endregion Validation Functions

  /**
   * Sends an HTTP request with the specified method, URL, data, and extra headers if needed.
   *
   * @async
   * @function Send
   * @param {string} method - The HTTP method to use (e.g., 'GET', 'POST').
   * @param {string} resource - The resource to which the request is sent. The URL before '?'.
   * @param {string} query - The query string parameters to include in the request. The value after '?'. (optional).
   * @param {Object} [data] - The data to be sent as the request body (optional).
   * @param {Object} [extraHeaders] - Additional headers to include in the request (optional).
   * @returns {Promise<Response|Error>} The response from the fetch call or an error if the request fails.
   * @throws {Error} If the fetch request fails.
   */
  async Send(method, resource, query = null, data = null, extraHeaders = null) {
    //#region Parameter Validation
    const validMethods = ["POST", "PATCH", "PUT", "GET", "DELETE"];
    if (!validMethods.includes(method.toUpperCase())) {
      throw new Error(`Method ${method} is not supported.`);
    }
    if (typeof resource !== "string") {
      throw new Error("resource parameter value is not a valid string.");
    }
    if (query && typeof query !== "string") {
      throw new Error("query parameter value is not a valid string.");
    }

    if (!resource.startsWith("$batch")) {
      if (data && !this.#isValidObjectForJSON(data)) {
        throw new Error(
          "data parameter value is not a valid object to convert to JSON."
        );
      }
    }

    if (extraHeaders && typeof extraHeaders !== "object") {
      throw new Error("extraHeaders parameter value is not a valid object.");
    }
    //#endregion Parameter Validation

    const token = await this.#getTokenFunc();
    let baseHeaders = {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
      Accept: "application/json",
      "OData-Version": "4.0",
      "OData-MaxVersion": "4.0",
    };
    if (extraHeaders) {
      baseHeaders = { ...baseHeaders, ...extraHeaders };
    }

    let url = `${this.#apiEndpoint}${resource}`;
    if (query) {
      url += query.startsWith("?") ? query : `?${query}`;
    }

    const resourceURL = new URL(url, this.#baseUrl);

    const request = new Request(resourceURL, {
      method: method,
      headers: baseHeaders,
      // Special case for batch requests
      body: resource.startsWith("$batch")
        ? data
        : data
        ? JSON.stringify(data)
        : null,
    });

    try {
      const response = await fetch(request);
      if (!response.ok) {
        // Handle 304 Not Modified for GET requests
        if (response.status === 304 && method === "GET") {
          return response;
        }
        const error = await response.json();
        console.error(error);
        throw new Error(error.error.message);
      }
      return response;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }
  /**
   * Retrieves information about the current user by calling the "WhoAmI" message.
   *
   * @async
   * @function WhoAmI
   * @returns {Promise<Object|Error>} A promise that resolves to the user information in JSON format, or an error if the request fails.
   * @throws {Error} If the request fails.
   */
  async WhoAmI() {
    try {
      const response = await this.Send("GET", "WhoAmI");
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Creates a new record in the specified entity set.
   *
   * @async
   * @function Create
   * @param {string} entitySetName - The name of the entity set where the new entity will be created.
   * @param {Object} data - The data for the new entity.
   * @returns {Promise<Object|Error>} A promise that resolves to an object containing the ID of the created entity, or an error if the request fails.
   * @throws {Error} If the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/create-entity-web-api
   */
  async Create(entitySetName, data) {
    //#region Parameter Validation
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a string.");
    }
    if (!this.#isValidObjectForJSON(data)) {
      throw new Error(
        "data parameter value is not a valid object to convert to JSON."
      );
    }
    //#endregion Parameter Validation
    try {
      const response = await this.Send("POST", entitySetName, null, data);
      let url = response.headers.get("OData-EntityId");
      // Extract the ID from the OData-EntityId header value
      let id = url.substring(url.lastIndexOf("(") + 1, url.lastIndexOf(")"));
      return id;
    } catch (error) {
      throw error;
    }
  }

  /**
   * Retrieves a record from the specified entity set by ID, with optional query options.
   *
   * @async
   * @function Retrieve
   * @param {string} entitySetName - The name of the entity set from which to retrieve the entity.
   * @param {string} id - The ID of the entity to retrieve.
   * @param {string} [query] - The odata query options to apply
   * @param {boolean} [includeAnnotations] - Whether OData annotations are returned in the response. Default value is true.
   * @returns {Promise<Object|Error>} A promise that resolves to the retrieved entity in JSON format, or an error if the request fails.
   * @throws {Error} If the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/retrieve-entity-using-web-api
   */
  async Retrieve(entitySetName, id, query = null, includeAnnotations = true) {
    //#region Parameter Validation
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a string.");
    }
    if (!this.#isGUID(id)) {
      throw new Error(`The id ${id} is not a valid GUID.`);
    }
    if (includeAnnotations && typeof includeAnnotations !== "boolean") {
      throw new Error("includeAnnotations parameter value is not a boolean.");
    }
    //#endregion Parameter Validation
    let extraHeaders = null;
    if (includeAnnotations) {
      extraHeaders = {
        Prefer: 'odata.include-annotations="*"',
      };
    }
    let resource = `${entitySetName}(${id})`;

    try {
      const response = await this.Send(
        "GET",
        resource,
        query,
        null,
        extraHeaders
      );
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Refreshes the given record by fetching the latest data from the server.
   *
   * @async
   * @param {Object} record - The record to refresh. Must contain @odata.etag and @odata.context properties.
   * @param {string} primarykeyName - The name of the primary key property in the record.
   * @throws {Error} If the record does not have the required @odata.etag and @odata.context properties.
   * @throws {Error} If the entity set name and columns cannot be extracted from the record.
   * @throws {Error} If the id cannot be extracted from the record using the primary key name.
   * @returns {Promise<Object>} The refreshed record.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-conditional-operations-using-web-api#conditional-retrievals
   */
  async Refresh(record, primarykeyName) {
    //#region Parameter Validation
    const errorMessage =
      "record parameter value doesn't have required @odata.etag and @odata.context properties.";

    const etag = record["@odata.etag"];
    const context = record["@odata.context"];

    if (!etag || !context) {
      throw new Error(errorMessage);
    }

    if (!this.#isValidWeakETag(etag)) {
      throw new Error("extracted etag value is not a valid ETag value.");
    }

    const columnsMatch = context.match(/\(([^)]+)\)/);
    const entitySetNameMatch = context.match(/#(\w+)\(/);

    if (!entitySetNameMatch || !columnsMatch) {
      throw new Error(
        "Cannot extract entity set name and columns from record."
      );
    }

    if (primarykeyName && typeof primarykeyName !== "string") {
      throw new Error("primarykeyName parameter value is not a string.");
    }

    const id = record[primarykeyName];
    if (!id) {
      throw new Error(`Can't extract id from record using ${primarykeyName}.`);
    }
    if (!this.#isGUID(id)) {
      throw new Error(
        `The ${primarykeyName} value '${id}' is not a valid GUID.`
      );
    }
    //#endregion Parameter Validation

    // This operation can't use the Prefer: odata.include-annotations="*" header
    // because it will never return 304 Not Modified.
    let extraHeaders = {
      "If-None-Match": etag,
    };

    const columns = columnsMatch[1].split(",");
    // This operation can't use any $expand query options
    // because it will never return 304 Not Modified.
    const query = `$select=${columns}`;
    const entitySetName = entitySetNameMatch[1];

    let resource = `${entitySetName}(${id})`;

    try {
      const response = await this.Send(
        "GET",
        resource,
        query,
        null,
        extraHeaders
      );
      if (!response.ok) {
        if (response.status === 304) {
          console.log("The record was NOT modified on the server.");
          return record;
        } else {
          const error = await response.json();
          console.error(error);
          throw new Error(error.error.message);
        }
      }
      console.log("The record WAS modified on the server.");
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Creates and retrieves a record from the specified entity set.
   *
   * @async
   * @param {string} entitySetName - The name of the entity set.
   * @param {Object} data - The data to be sent in the request body.
   * @param {string} [query] - The query string to be appended to the entity set URL.
   * @param {boolean} [includeAnnotations=true] - Whether to include OData annotations in the response.
   * @returns {Promise<Object>} The response data as a JSON object.
   * @throws {Error} If the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/create-entity-web-api#create-with-data-returned
   */
  async CreateRetrieve(entitySetName, data, query, includeAnnotations = true) {
    //#region Parameter Validation
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a string.");
    }
    if (!this.#isValidObjectForJSON(data)) {
      throw new Error(
        "data parameter value is not a valid object to convert to JSON."
      );
    }
    if (includeAnnotations && typeof includeAnnotations !== "boolean") {
      throw new Error(
        "includeAnnotations parameter value is not a boolean value."
      );
    }
    //#endregion Parameter Validation

    let preferHeaders = ["return=representation"];

    if (includeAnnotations) {
      preferHeaders.push('odata.include-annotations="*"');
    }
    const extraHeaders = {
      Prefer: preferHeaders.join(","),
    };

    let resource = entitySetName;

    try {
      const response = await this.Send(
        "POST",
        resource,
        query,
        data,
        extraHeaders
      );
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Retrieves multiple records from a specified entity set collection with optional query parameters.
   *
   * @async
   * @function RetrieveMultiple
   * @param {string} collectionResource - The name of the entity set or a filtered collection expression to retrieve records from.
   * @param {string} query - The OData query options to apply.
   * @param {number} maxPageSize - The maximum number of records to retrieve per page defaults to 100.
   * @param {boolean} [includeAnnotations = true] - Whether to include OData annotations in the response.
   * @returns {Promise<object>} The response from the server containing the retrieved entities.
   * @throws {Error} Throws an error if the retrieval fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/overview
   */
  async RetrieveMultiple(
    collectionResource,
    query,
    maxPageSize = 100,
    includeAnnotations = true
  ) {
    //#region Parameter Validation
    if (typeof collectionResource !== "string") {
      throw new Error("collectionResource parameter value is not a string.");
    }

    if (maxPageSize && typeof maxPageSize !== "number") {
      throw new Error("maxPageSize parameter value is not a number value.");
    }
    if (includeAnnotations && typeof includeAnnotations !== "boolean") {
      throw new Error(
        "includeAnnotations parameter value is not a boolean value."
      );
    }
    //#endregion Parameter Validation

    let resource = `${collectionResource}`;
    let extraHeaders = null;
    let preferHeaders = [];

    if (maxPageSize) {
      preferHeaders.push(`odata.maxpagesize=${maxPageSize}`);
    }
    if (includeAnnotations) {
      preferHeaders.push('odata.include-annotations="*"');
    }

    if (preferHeaders.length > 0) {
      extraHeaders = {
        Prefer: preferHeaders.join(","),
      };
    }

    try {
      const response = await this.Send(
        "GET",
        resource,
        query,
        null,
        extraHeaders
      );
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Retrieves the next page of records from a specified entity set collection using the @odata.nextLink value.
   *
   * @async
   * @function GetNextLink
   * @param {string} nextLink the @odata.nextLink value from the previous response
   * @param {number} maxPageSize - The maximum number of records to retrieve per page defaults to 100.
   * @param {boolean} [includeAnnotations=true] - Whether to include OData annotations in the response.
   * @returns {Promise<object>} The response from the server containing the retrieved entities.
   * @throws {Error} Throws an error if the retrieval fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/page-results
   */
  async GetNextLink(nextLink, maxPageSize = 100, includeAnnotations = true) {
    //#region Parameter Validation
    if (typeof nextLink !== "string") {
      throw new Error("nextLink parameter value is not a string.");
    }
    if (maxPageSize && typeof maxPageSize !== "number") {
      throw new Error("maxPageSize parameter value is not a number value.");
    }
    if (includeAnnotations && typeof includeAnnotations !== "boolean") {
      throw new Error(
        "includeAnnotations parameter value is not a boolean value."
      );
    }
    //#endregion Parameter Validation

    let extraHeaders = null;
    let preferHeaders = [];

    if (maxPageSize) {
      preferHeaders.push(`odata.maxpagesize=${maxPageSize}`);
    }
    if (includeAnnotations) {
      preferHeaders.push('odata.include-annotations="*"');
    }

    if (preferHeaders.length > 0) {
      extraHeaders = {
        Prefer: preferHeaders.join(","),
      };
    }

    // Make the nextLink a relative URL as expected by Send method
    const resource = nextLink.replace(this.#apiEndpoint, "");

    try {
      const response = await this.Send(
        "GET",
        resource,
        null,
        null,
        extraHeaders
      );
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Asynchronously fetches data from a specified entity set using FetchXML.
   *
   * @async
   * @function FetchXml
   * @param {string} entitySetName - The name of the entity set to query.
   * @param {string} fetchXml - The FetchXML query string.
   * @returns {Promise<Object>} The JSON response from the server.
   * @throws Will throw an error if the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/fetchxml/retrieve-data?tabs=webapi
   */
  async FetchXml(entitySetName, fetchXml) {
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a string.");
    }
    if (!this.#isValidXML(fetchXml)) {
      throw new Error(
        "fetchXml parameter string value doesn't represent a valid XML document."
      );
    }
    let resource = `${entitySetName}`;

    // Encode the FetchXML query string
    const query = `fetchXml=${encodeURIComponent(fetchXml).replace(
      /%20/g,
      "+"
    )}`;

    // Always including annotations so paging data is available
    let extraHeaders = {
      Prefer: 'odata.include-annotations="*"',
    };

    try {
      const response = await this.Send(
        "GET",
        resource,
        query,
        null,
        extraHeaders
      );
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Asynchronously retrieves the count of items in a specified collection.
   *
   * @async
   * @function GetCollectionCount
   * @param {string} collectionResource - The resource URL of the collection.
   * @returns {Promise<number>} The count of items in the collection, up to 5000
   * @throws Will throw an error if the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/count-rows
   */
  async GetCollectionCount(collectionResource) {
    if (typeof collectionResource !== "string") {
      throw new Error(
        "collectionResource parameter value is not a valid string."
      );
    }
    try {
      const response = await this.Send("GET", collectionResource + "/$count");
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Updates a record in the specified entity set by ID with the provided data.
   *
   * @async
   * @function Update
   * @param {string} entitySetName - The name of the entity set where the record exists.
   * @param {string} id - The ID of the record to update.
   * @param {Object} data - The data to update the record with.
   * @param {string} etag - Specify the etag value to prevent update when newer record exists. (optional)
   * @returns {Promise<Response|Error>} A promise that resolves to the response of the update operation, or an error if the request fails.
   * @throws {Error} If the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update
   */
  async Update(entitySetName, id, data, etag = null) {
    //#region Parameter Validation
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a valid string.");
    }
    if (!this.#isGUID(id)) {
      throw new Error(`The id ${id} is not a valid GUID.`);
    }
    if (!this.#isValidObjectForJSON(data)) {
      throw new Error(
        "data parameter value is not a valid object to convert to JSON."
      );
    }
    if (etag && !this.#isValidWeakETag(etag)) {
      throw new Error("etag parameter value is not a valid ETag value.");
    }
    //#endregion Parameter Validation

    // Prevents create operation
    let ifMatchHeaderValue = "*";

    if (etag) {
      // Prevents update when newer record exists
      ifMatchHeaderValue = etag;
    }

    try {
      const response = await this.Send(
        "PATCH",
        `${entitySetName}(${id})`,
        null,
        data,
        { "If-Match": ifMatchHeaderValue }
      );
      return response;
    } catch (error) {
      throw error;
    }
  }

  /**
   * Deletes an entity from the specified entity set by ID.
   *
   * @async
   * @function Delete
   * @param {string} entitySetName - The name of the entity set from which to delete the entity.
   * @param {string} id - The ID of the entity to delete.
   * @param {string} etag - Specify the etag value to prevent delete when newer record exists. (optional)
   * @returns {Promise<Response|Error>} A promise that resolves to the response of the delete operation, or an error if the request fails.
   * @throws {Error} If the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete
   */
  async Delete(entitySetName, id, etag = null) {
    //#region Parameter Validation
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a string.");
    }
    if (!this.#isGUID(id)) {
      throw new Error(`The id ${id} is not a valid GUID.`);
    }
    if (etag && typeof etag !== "string") {
      throw new Error("etag parameter value is not a string.");
    }
    if (etag && !this.#isValidWeakETag(etag)) {
      throw new Error("etag parameter value is not a valid ETag value.");
    }
    //#endregion Parameter Validation

    let extraHeaders = null;
    if (etag) {
      extraHeaders = {
        "If-Match": etag,
      };
    }
    try {
      const response = await this.Send(
        "DELETE",
        `${entitySetName}(${id})`,
        null,
        null,
        extraHeaders
      );
      return response;
    } catch (error) {
      throw error;
    }
  }

  /**
   * Sets the value of a specified column for a given record.
   * @async
   * @function SetValue
   * @param {string} entitySetName - The name of the entity set.
   * @param {string} id - The ID of the record.
   * @param {string} columnName - The logical name of the column to set the value for.
   * @param {*} value - The value to set for the specified column.
   * @returns {Object} The response from the server.
   * @throws Will throw an error if the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/update-delete-entities-using-web-api#update-a-single-property-value
   */
  async SetValue(entitySetName, id, columnName, value) {
    //#region Parameter Validation
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a string.");
    }
    if (!this.#isGUID(id)) {
      throw new Error(`The id ${id} is not a valid GUID.`);
    }
    if (typeof columnName !== "string") {
      throw new Error("columnName parameter value is not a string.");
    }
    if (value === undefined) {
      throw new Error("value parameter value is undefined.");
    }
    //#endregion Parameter Validation

    try {
      const response = await this.Send(
        "PUT",
        `${entitySetName}(${id})/${columnName}`,
        null,
        { value: value },
        { "If-None-Match": null }
      );
      return response;
    } catch (error) {
      throw error;
    }
  }
  /**
   * Retrieves the value of a specified column for a given record.
   * @async
   * @function GetValue
   * @param {string} entitySetName - The name of the entity set.
   * @param {string} id - The ID of the record.
   * @param {string} columnName - The name of the column to retrieve the value from.
   * @returns {Object} The response from the server.
   * @throws Will throw an error if the request fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/retrieve-entity-using-web-api#retrieve-a-single-property-value
   */
  async GetValue(entitySetName, id, columnName) {
    //#region Parameter Validation
    if (typeof entitySetName !== "string") {
      throw new Error("entitySetName parameter value is not a string.");
    }
    if (!this.#isGUID(id)) {
      throw new Error(`The id ${id} is not a valid GUID.`);
    }
    if (typeof columnName !== "string") {
      throw new Error("columnName parameter value is not a string.");
    }
    //#endregion Parameter Validation

    try {
      const response = await this.Send(
        "GET",
        `${entitySetName}(${id})/${columnName}`,
        null,
        null,
        { "If-None-Match": null }
      );

      const data = await response.json();
      return data.value;
    } catch (error) {
      throw error;
    }
  }

  /**
   * Associates records by creating data in the relationship to link them.
   *
   * @async
   * @function Associate
   * @param {string} targetSetName - The name of the target entity set.
   * @param {string|number} targetId - The ID of the target record.
   * @param {string} navigationProperty - The navigation property that defines the relationship.
   * @param {string} relatedSetName - The name of the related entity set.
   * @param {string|number} relatedId - The ID of the record to associate with the target.
   * @returns {Promise<object>} The response from the server after creating the association.
   * @throws {Error} Throws an error if the association fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api#add-a-record-to-a-collection
   */
  async Associate(
    targetSetName,
    targetId,
    navigationProperty,
    relatedSetName,
    relatedId
  ) {
    //#region Parameter Validation
    if (typeof targetSetName !== "string") {
      throw new Error("targetSetName parameter value is not a string.");
    }
    if (!this.#isGUID(targetId)) {
      throw new Error(`The targetId ${targetId} is not a valid GUID.`);
    }
    if (typeof navigationProperty !== "string") {
      throw new Error("navigationProperty parameter value is not a string.");
    }
    if (typeof relatedSetName !== "string") {
      throw new Error("relatedSetName parameter value is not a string.");
    }
    if (!this.#isGUID(relatedId)) {
      throw new Error(`The relatedId ${relatedId} is not a valid GUID.`);
    }
    //#endregion Parameter Validation

    try {
      const response = await this.Send(
        "POST",
        `${targetSetName}(${targetId})/${navigationProperty}/$ref`,
        null,
        { "@odata.id": `${this.#apiEndpoint}/${relatedSetName}(${relatedId})` }
      );
      return response;
    } catch (error) {
      throw error;
    }
  }

  /**
   * Disassociates an record from another record by deleting data in the relationship to link them.
   *
   * @async
   * @function Disassociate
   * @param {string} targetSetName - The name of the target entity set.
   * @param {string|guid} targetId - The ID of the target record.
   * @param {string} navigationProperty - The navigation property that defines the relationship.
   * @param {string|guid} relatedId - The ID of the related record.
   * @returns {Promise<object>} The response from the server after deleting the association.
   * @throws {Error} Throws an error if the disassociation fails.
   * https://learn.microsoft.com/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api#remove-a-record-from-a-collection
   */
  async Disassociate(targetSetName, targetId, navigationProperty, relatedId) {
    //#region Parameter Validation
    if (typeof targetSetName !== "string") {
      throw new Error("targetSetName parameter value is not a string.");
    }
    if (!this.#isGUID(targetId)) {
      throw new Error(`The targetId ${targetId} is not a valid GUID.`);
    }
    if (typeof navigationProperty !== "string") {
      throw new Error("navigationProperty parameter value is not a string.");
    }
    if (typeof relatedId !== "string") {
      throw new Error("relatedId parameter value is not a string.");
    }
    if (!this.#isGUID(relatedId)) {
      throw new Error(`The relatedId ${relatedId} is not a valid GUID.`);
    }
    //#endregion Parameter Validation
    try {
      const response = await this.Send(
        "DELETE",
        `${targetSetName}(${targetId})/${navigationProperty}(${relatedId})/$ref?`
      );
      return response;
    } catch (error) {
      throw error;
    }
  }

  /**
   * Sends a web API request and returns the response.
   *
   * @async
   * @function SendRequest
   * @param {WebAPIRequest} request - The request object to be sent.
   * @throws {Error} Throws an error if the request parameter is not an instance of WebAPIRequest.
   * @returns {Promise<WebAPIResponse>} The response from the web API.
   */
  async SendRequest(request) {
    //#region Parameter Validation
    if (!request instanceof WebAPIRequest) {
      throw new Error(
        `request parameter value '${request}' is not a WebAPIRequest.`
      );
    }
    //#endregion Parameter Validation

    try {
      // TODO: Should all requests be composed using WebAPIRequest?
      const response = await this.Send(
        request.method,
        request.resource,
        request.query,
        request.body,
        request.headers
      );
      const webAPIResponse = new WebAPIResponse();
      await webAPIResponse.init(response);
      return webAPIResponse;
    } catch (error) {
      throw error;
    }
  }

  // Parses batch responses for the Batch method
  #parseBatchText(batchResponse) {
    const batchBoundary = batchResponse.match(/--batchresponse_[\w-]+/)[0];
    const batchParts = batchResponse
      .split(batchBoundary)
      .filter((part) => part.trim() !== "--" && part.trim() !== "");
    const parts = [];
    for (const part of batchParts) {
      if (
        part.startsWith(
          "\r\nContent-Type: multipart/mixed; boundary=changesetresponse_"
        )
      ) {
        const changeSetBoundary = part.match(/--changesetresponse_[\w-]+/)[0];
        const changeSetParts = part
          .split(changeSetBoundary)
          .filter((part) => part.trim() !== "--" && part.trim() !== "");
        for (const changeSetPart of changeSetParts) {
          if (
            changeSetPart.trim() !== "" &&
            !changeSetPart.startsWith(
              "\r\nContent-Type: multipart/mixed; boundary=changesetresponse_"
            )
          ) {
            parts.push(changeSetPart);
          }
        }
      } else {
        parts.push(part);
      }
    }

    function parseHttpStatus(httpStatusString) {
      const regex = /^HTTP\/1\.1 (\d{3}) (.+)$/;
      const match = httpStatusString.match(regex);

      if (match) {
        const statusCode = match[1];
        const statusText = match[2];
        return { statusCode: parseInt(statusCode, 10), statusText: statusText };
      } else {
        throw new Error("Invalid HTTP status string format");
      }
    }

    let responses = [];

    for (const part of parts) {
      const subParts = part.split("\r\n");

      let response = new WebAPIResponse();

      for (let i = 0; i < subParts.length; i++) {
        if (subParts[i] === "") {
          continue;
        }
        if (subParts[i].startsWith("{")) {
          response.body = JSON.parse(subParts[i]);
          continue;
        }
        if (subParts[i].startsWith("HTTP/1.1")) {
          const parsedStatus = parseHttpStatus(subParts[i]);
          response.statusCode = parsedStatus.statusCode;
          response.statusText = parsedStatus.statusText;
        }
        if (subParts[i].includes(":")) {
          const [key, value] = subParts[i].split(": ");
          response.headers[key.trim()] = value.trim();
        }
      }

      responses.push(response);
    }
    return responses;
  }

  /**
   * Sends a batch request containing multiple WebAPIRequest or ChangeSet items.
   *
   * @async
   * @function Batch
   * @param {Array<WebAPIRequest|ChangeSet>} requests - An array of WebAPIRequest or ChangeSet items to be included in the batch request.
   * @param {boolean} [continueOnError=false] - A flag indicating whether to continue processing subsequent requests if an error occurs.
   * @throws {Error} Throws an error if the requests parameter is not a valid array or contains invalid items.
   * @returns {Promise<Array<WebAPIResponse>>} The parsed response from the batch request.
   */
  async Batch(requests, continueOnError = false) {
    //#region Parameter Validation
    if (!Array.isArray(requests)) {
      throw new Error("requests parameter value is not a valid array.");
    }

    for (const request of requests) {
      if (
        !(request instanceof WebAPIRequest) &&
        !(request instanceof ChangeSet)
      ) {
        throw new Error(
          "requests parameter value contains items that are not WebAPIRequest or ChangeSet."
        );
      }
    }
    //#endregion Parameter Validation

    const batchId = Math.random().toString(16).slice(2);
    const batchItems = requests.map((request, index) => {
      if (request instanceof ChangeSet) {
        return request.getChangeSetText(batchId);
      }
      if (request instanceof WebAPIRequest) {
        return request.getBatchBody(batchId, false);
      }
    });

    const batchRequestBody = [...batchItems, `--batch_${batchId}--\r\n`].join(
      "\r\n"
    );

    try {
      const batchRequestHeaders = {
        "Content-Type": `multipart/mixed; boundary=batch_${batchId}`,
        "If-None-Match": null,
      };
      if (continueOnError) {
        batchRequestHeaders["Prefer"] = "odata.continue-on-error";
      }

      // Send the batch request
      const response = await this.Send(
        "POST",
        "$batch",
        null,
        batchRequestBody,
        batchRequestHeaders
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const text = await response.text();

      return this.#parseBatchText(text);
    } catch (error) {
      console.error(error.message);
      throw error;
    }
  }
}

/**
 * Represents a web API request used for batch processing.
 */
class WebAPIRequest {
  #validateMethodValue(method) {
    const validMethods = ["POST", "PATCH", "PUT", "GET", "DELETE"];
    if (!validMethods.includes(method.toUpperCase())) {
      throw new Error(`method parameter value ${method} is not valid.`);
    }
  }
  #validateResourceValue(resource) {
    if (typeof resource !== "string") {
      throw new Error("resource parameter value is not a string.");
    }
    if (resource.includes("?") || resource.includes("&")) {
      throw new Error(
        "resource parameter value should not include query parameters."
      );
    }
  }
  #validateQueryValue(query) {
    if (query && typeof query !== "string") {
      throw new Error("query parameter value is not a string.");
    }
  }
  #validateBodyValue(body) {
    if (body && typeof body !== "object") {
      throw new Error("body parameter value is not an object.");
    }
  }
  #validateHeadersValue(headers) {
    if (headers && typeof headers !== "object") {
      throw new Error("headers parameter value is not an object.");
    }
  }
  #validateContentIDValue(contentID) {
    if (contentID && typeof contentID !== "string") {
      throw new Error("contentID parameter value is not a string.");
    }
  }

  /**
   * Creates an instance of WebAPIRequest.
   *
   * @param {string} method - The HTTP method for the request (e.g., 'GET', 'POST').
   * @param {string} resource - The resource endpoint for the request.
   * @param {string} [query=null] - The query string for the request, if any.
   * @param {Object|null} [body=null] - The body of the request, if any.
   * @param {Object|null} [headers=null] - The headers for the request, if any.
   * @param {string} [contentID] - The content ID, if any.
   */
  constructor(
    method,
    resource,
    query = null,
    body = null,
    headers = null,
    contentID = null
  ) {
    this.#validateMethodValue(method);
    this.#validateResourceValue(resource);
    this.#validateQueryValue(query);
    this.#validateBodyValue(body);
    this.#validateHeadersValue(headers);
    this.#validateContentIDValue(contentID);

    this._method = method;
    this._resource = resource;
    this._query = query;
    this._body = body;
    this._headers = headers;
    this._contentID = contentID;
  }
  /**
   * Gets the HTTP method of the request.
   *
   * @returns {string} The HTTP method.
   */
  get method() {
    return this._method;
  }

  // Sets the HTTP method of the request.
  set method(value) {
    this.#validateMethodValue(value);
    this._method = value;
  }
  // Gets the resource relative URL of the request.
  get resource() {
    return this._resource;
  }

  // Sets the resource relative URL of the request.
  set resource(value) {
    this.#validateResourceValue(value);
    this._resource = value;
  }

  // Gets the query string options of the request.
  get query() {
    return this._query;
  }

  // Sets the query string options of the request.
  set query(value) {
    this.#validateQueryValue(value);
    this._query = value;
  }

  // Gets the headers of the request.
  get headers() {
    return this._headers;
  }
  // Sets the headers of the request.
  set headers(value) {
    this.#validateHeadersValue(value);
    this._headers = value;
  }

  // Sets the body of the request.
  set body(value) {
    this.#validateBodyValue(value);
    this._body = value;
  }

  // Gets the Content-ID of the request.
  get contentID() {
    return this._contentID;
  }
  // Sets the Content-ID of the request.
  set contentID(value) {
    if (typeof value !== "string") {
      throw new Error("contentID parameter value is not a string.");
    }
    this._contentID = value;
  }

  /**
   * Gets the object that needs to be serialized to JSON for the request body.
   *
   * @returns {object} The object representing the body of the request.
   */
  get body() {
    return this._body;
  }
  /**
   * Generates the batch request body for the OData service.
   *
   * @param {string} Id - The unique identifier for the batch request or change set
   * @param {bool} inChangeSet - Whether the request is in a change set.
   * @returns {string} The formatted batch request body.
   */
  getBatchBody(Id, inChangeSet = false) {
    let url = `/api/data/v9.2/${this.resource}`;
    if (this.query) {
      if (this.query.startsWith("?")) {
        url += this.query;
      } else {
        url += "?" + this.query;
      }
    }
    const batchBody = [
      inChangeSet ? `--changeset_${Id}` : `--batch_${Id}`,
      `Content-Type: application/http`,
      `Content-Transfer-Encoding: binary`,
    ];

    if (this._contentID && inChangeSet) {
      batchBody.push(`Content-ID: ${this.contentID}`);
    }
    batchBody.push("");
    batchBody.push(`${this.method} ${url} HTTP/1.1`);

    if (this._body) {
      batchBody.push("Content-Type: application/json; type=entry");
    }

    // Any additional headers for the request.
    if (this._headers) {
      for (const [key, value] of Object.entries(this.headers)) {
        batchBody.push(`${key}: ${value}`);
      }
    }

    batchBody.push("", JSON.stringify(this.body));

    return batchBody.join("\r\n");
  }
}

/**
 * Represents a web API response used for batch processing.
 */
class WebAPIResponse {
  constructor() {
    this._headers = {};
    this._body = null;
  }

  // Initializes the WebAPIResponse object with the response from the server.
  async init(response) {
    if (!response instanceof Response) {
      throw new Error("response parameter value is not a valid Response.");
    }
    this._statusCode = response.status;
    this._statusText = response.statusText;
    this._headers = response.headers;
    if (
      response.status >= 200 &&
      response.status !== 204 && // No content
      response.status !== 304 // Not modified
    ) {
      this._body = await response.json();
    }
  }

  // Gets the status code of the response.
  get statusCode() {
    return this._statusCode;
  }
  // Sets the status code of the response.
  set statusCode(value) {
    if (typeof value !== "number") {
      throw new Error("statusCode parameter value is not a number.");
    }
    this._statusCode = value;
  }
  // Gets the status text of the response.
  get statusText() {
    return this._statusText;
  }
  // Sets the status text of the response.
  set statusText(value) {
    if (typeof value !== "string") {
      throw new Error("statusText parameter value is not a string.");
    }
    this._statusText = value;
  }

  // Gets the headers of the response.
  get headers() {
    return this._headers;
  }

  // Sets the headers of the response.
  set headers(value) {
    if (typeof value !== "object") {
      throw new Error("headers parameter value is not an object.");
    }
    this._headers = value;
  }

  // Gets the body of the response.
  get body() {
    return this._body;
  }

  // Sets the body of the response.
  set body(value) {
    if (typeof value !== "object") {
      throw new Error("body parameter value is not an object.");
    }
    this._body = value;
  }
}

/**
 * Represents a set of changes used with batch processing.
 */
class ChangeSet {
  // Validates the requests in the change set.
  #validateRequests(requests) {
    if (!Array.isArray(requests)) {
      throw new Error("requests value is not a valid array.");
    }

    if (!requests.every((request) => request instanceof WebAPIRequest)) {
      throw new Error("requests value is not an array of WebAPIRequest.");
    }

    if (requests.some((request) => request.method === "GET")) {
      throw new Error("requests within change set cannot use GET method.");
    }
  }

  // Constructor for ChangeSet class
  constructor(requests) {
    this.#validateRequests(requests);
    this._requests = [];
    this._requests = requests;
    this._id = Math.random().toString(16).slice(2);
  }

  // Gets the array of WebAPIRequest objects in the change set.
  get requests() {
    return this._requests;
  }
  // Sets the array of WebAPIRequest objects in the change set.
  set requests(value) {
    this.#validateRequests(value);
    this._requests = value;
  }

  // Gets the text for the changeset in the $batch operation.
  getChangeSetText(batchId) {
    const batchBody = [
      `--batch_${batchId}\r\n`,
      `Content-Type: multipart/mixed; boundary=changeset_${this._id}\r\n`,
    ];
    let count = 1;
    for (const request of this._requests) {
      request.contentID = count.toString();
      // Use the getBatchBody method setting inChangeSet parameter to true
      const requestBody = request.getBatchBody(this._id, true);
      batchBody.push(`\r\n${requestBody}`);
      count++;
    }
    batchBody.push(`\r\n--changeset_${this._id}--\r\n`);

    return batchBody.join("");
  }
}

// Group public classes in a namespace object for export
const DataverseWebAPI = {
  Client,
  WebAPIRequest,
  WebAPIResponse,
  ChangeSet,
  // Add other classes here as needed
};

export { DataverseWebAPI };

```

### See also

[Use the Dataverse Web API](overview.md)   
[Web API Samples](web-api-samples.md)   
[Web API Samples (C#)](web-api-samples-csharp.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
