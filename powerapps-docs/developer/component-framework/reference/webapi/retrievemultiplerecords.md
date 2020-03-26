---
title: retrieveMultipleRecords | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 824a53f9-c743-435a-9de2-8128846f3191
---

# retrieveMultipleRecords

[!INCLUDE [retrievemultiplerecords-description](includes/retrievemultiplerecords-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.webAPI.retrieveMultipleRecords(entityLogicalName, options, maxPageSize).then(successCallback, errorCallback);`

## Parameters

<table style="width:100%">
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>entityLogicalName</td>
<td>String</td>
<td>Yes</td>
<td>The entity logical name of the records you want to retrieve. For example: &quot;account&quot;.</td>
</tr>
<tr>
<td>options</td>
<td>String</td>
<td>No</td>
<td><p>OData system query options or FetchXML query to retrieve your data. </p> 
<ul>
<li>Following system query options are supported: <b>$select</b>, <b>$top</b>, <b>$filter</b>, <b>$expand</b>, and <b>$orderby</b>.</li>
<li>To specify a FetchXML query, use the <code>fetchXml</code> attribute to specify the query.</li>
</ul>
<p>NOTE: You must always use the <b>$select</b> system query option to limit the properties returned for an entity record by including a comma-separated list of property names. This is an important performance best practice. If properties aren’t specified using <b>$select</b>, all properties will be returned.</li>
<p>You specify the query options starting with <code>?</code>. You can also specify multiple system query options by using <code>&amp;</code> to separate the query options.
<p>See examples later in this topic to see how you can define the <code>options</code> parameter for various retrieve multiple scenarios.</td>
</tr>
<tr>
<td>maxPageSize</td>
<td>Number</td>
<td>No</td>
<td><p>Specify a positive number that indicates the number of entity records to be returned per page. If you do not specify this parameter, the default value is passed as 5000.</p>
<p>If the number of records being retrieved is more than the specified <code>maxPageSize</code> value, <code>nextLink</code> attribute in the returned promise object will contain a link to retrieve the next set of entities. </td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when entity records are retrieved. An object with the following attributes is passed to the function:</p>
<ul>
<li><b>entities</b>: An array of JSON objects, where each object represents the retrieved entity record containing attributes and their values as <code>key: value</code> pairs. The Id of the entity record is retrieved by default.</li>
<li><b>nextLink</b>: String. If the number of records being retrieved is more than the value specified in the <code>maxPageSize</code> parameter in the request, this attribute returns the URL to return next set of records.</li>
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

Type: [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise)<RetrieveMultipleResponse>

Description: The `RetrieveMultipleResponse` returns a promise that contains an array of JSON objects containing the retrieved entity records and the **nextLink** attribute with the URL pointing to next set of records in case paging (`maxPageSize`) is specified in the request, and the record count returned exceeds the paging value. It has the following parameters:

|parameter|Return Value|Description|
|----|------|-------|
|entities|`Entity[]`|An array of JSON objects, where each object represents the retrieved entity record containing attributes and their values.|
|nextLink|`string`|If the number of records being retrieved is more than the value specified in the 'maxPageSize' parameter in the request, this attribute returns the URL to return next set of records.|


### Related topics

[Web API](../webapi.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)