---
title: "Xrm.WebApi.online.executeMultiple (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the Xrm.WebApi.online.executeMultiple method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Xrm.WebApi.online.executeMultiple (Client API reference)

[!INCLUDE[./includes/executeMultiple-description.md](./includes/executeMultiple-description.md)]

> [!NOTE]
> This method is supported only for the online mode ([Xrm.WebApi.online](../online.md)). 

If you want to execute multiple requests in a transaction, you must pass in a change set as a parameter to this method. [Change sets](../../../../../data-platform/webapi/execute-batch-operations-using-web-api.md#change-sets) represent a collection of operations that are executed in a transaction. You can also pass in individual requests and change sets together as parameters to this method.

> [!NOTE]
> - You cannot include read operations (retrieve, retrieve multiple, and Web API functions) as part of a change set; this is as per the OData v4 specifications.
> - Requests can contain up to 1000 individual requests and cannot contain other batches. More information: [Execute batch operations](../../../../../data-platform/webapi/execute-batch-operations-using-web-api.md).

## Syntax

**Execute multiple requests:**

```JavaScript
var requests = [req1, req2, req3];
Xrm.WebApi.online.executeMultiple(requests).then(successCallback, errorCallback);
```

**Execute multiple requests in a transaction:**

In this case, `req1`, `req2`, and `req3` are executed in a transaction.

```JavaScript
var changeSet = [req1, req2, req3];
var requests = [changeSet];
Xrm.WebApi.online.executeMultiple(requests).then(successCallback, errorCallback);
```


**Execute a mix of individual requests and multiple requests in a transaction:**

In this case, `req1`, `req2`, and `req3` are executed in transaction, but `req4` and `req5` are executed individually.

```JavaScript
var changeSet = [req1, req2, req3];
var requests = [req4, req5, changeset];
Xrm.WebApi.online.executeMultiple(requests).then(successCallback, errorCallback);
```

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`requests`|Array of objects|Yes|An array of one of the following types:<br /><br />**Objects** where each object is an action, function, or CRUD request that you want to execute against the Web API endpoint. Each object exposes a [getMetadata method](execute.md#requestgetmetadata-method) that lets you define the metadata for the action, function, or CRUD request you want to execute. The [execute method](execute.md) accepts this type of parameter.<br /><br />**Change set** (an array of objects), where each object in the change set is as defined above. In this case, all the request objects specified in the change set are executed in a transaction.<br /><br />See request examples in the [Syntax section](#syntax) for more information.|
|`successCallback`|Function|No|A function to call when operation is executed successfully. An array of response objects is passed to the function. See [Return Value](#return-value)|
|`errorCallback`|Function|No|A function to call when the operation fails. An object with the following properties is passed:<br /> - `errorCode`: Number. The error code as a positive decimal number.  For example, the error code documented as `0x80040333` will be returned as `2147746611`.<br /> - `message`: String. An error message describing the issue.|

## Return Value

On success, returns a promise containing an array of objects to the `successCallback`. The objects have these properties:

|Name|Type|Required|Description|
|---|---|---|---|
|`json`|Promise|No|Response body in JSON format.|
|`text`|Promise|No|Response body in plaintext format. |
|`headers`|Object|Yes|Response headers.|
|`ok`|Boolean|Yes|Indicates whether the request was successful.|
|`status`|Number|Yes|Numeric value in the response status code. For example: `200`|
|`statusText`|String|Yes|Description of the response status code. For example: `OK`|
|`type`|String|Yes|Response type. Values are: the empty string (default), `arraybuffer`, `blob`, `document`, `json`, and `text`.|
|`url`|String|Yes|Request URL of the action, function, or CRUD request that was sent to the Web API endpoint.|

### Related articles

[Xrm.WebApi](../../xrm-webapi.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
