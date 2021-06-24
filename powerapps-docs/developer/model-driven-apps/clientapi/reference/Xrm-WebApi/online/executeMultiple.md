---
title: "Xrm.WebApi.online.executeMultiple (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the Xrm.WebApi.online.executeMultiple method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: d4e92999-3b79-4783-8cac-f656fc5f7fda
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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

In this case, `req1`, `req2`, and `req3` will be executed in transaction.

```JavaScript
var changeSet = [req1, req2, req3];
var requests = [changeSet];
Xrm.WebApi.online.executeMultiple(requests).then(successCallback, errorCallback);
```


**Execute a mix of individual requests and multiple requests in a transaction:**

In this case, `req1`, `req2`, and `req3` will be executed in transaction, but `req4` and `req5` will be executed individually.

```JavaScript
var changeSet = [req1, req2, req3];
var requests = [req4, req5, changeset];
Xrm.WebApi.online.executeMultiple(requests).then(successCallback, errorCallback);
```

## Parameters

<table style="width:100%">
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>requests</td>
<td>Array of objects</td>
<td>Yes</td>
<td><p>An array of one of the following types:</p>
<ul>
<li>objects where each object is an action, function, or CRUD request that you want to execute against the Web API endpoint. Each object exposes a <b>getMetadata</b> method that lets you define the metadata for the action, function, or CRUD request you want to execute. This is the same object that you pass in the <code>execute</code> method. For information about the object, see <a href="execute.md">execute</a>.</li>
<li>Change set (an array of objects), where each object in the change set is as defined above. In this case, all the request objects specified in the change set will get executed in a transaction.</li>
</ul>
<p>See request examples earlier in the **Syntax** section for more information.</p>
</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when operation is executed successfully. An array of response objects are passed to the function where each response object has the following values:</p>
<ul>
<li><b>json</b>: (Optional). Promise. Response body in JSON format.</li>
<li><b>text</b>: (Optional). Promise. Response body in plaintext format. </li>
<li><b>headers</b>: Object. Response headers.</li>
<li><b>ok</b>: Boolean. Indicates whether the request was successful.</li>
<li><b>status</b>: Number. Numeric value in the response status code. For example: <b>200</b></li>
<li><b>statusText</b>: String. Description of the response status code. For example: <b>OK</b></li>
<li><b>type</b>: String. Response type. Values are: the empty string (default), "arraybuffer", "blob", "document", "json", and "text".</b></li>
<li><b>url</b>: String. Request URL of the action, function, or CRUD request that was sent to the Web API endpoint.</b></li>
</ul>
</td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to call when the operation fails.</td>
</tr>
</table>

## Return Value

On success, returns a promise containing an array of objects with the values specified earlier in the description of **successCallback** function.

### See also

[Xrm.WebApi](../../xrm-webapi.md)



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]