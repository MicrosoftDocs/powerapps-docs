---
title: updateRecord | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 179ced61-ff0f-45ef-aa14-835ce99532cf
---

# updateRecord

[!INCLUDE [updaterecord-description](includes/updaterecord-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.webapi.updateRecord(entityLogicalName, id, data).then(successCallback, errorCallback);`

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
<td>The entity logical name of the record you want to update. For example: &quot;account&quot;.</td>
</tr>
<tr>
<td>id</td>
<td>String</td>
<td>Yes</td>
<td>GUID of the entity record you want to update.</td>
</tr>
<tr>
<td>data</td>
<td>Object</td>
<td>Yes</td>
<td><p>A JSON object containing <code>key: value</code> pairs, where <code>key</code> is the property of the entity and <code>value</code> is the value of the property you want to update.</p>
<p>See examples later in this topic to see how you can define the <code>data</code> object for various update scenarios.</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when a record is updated. An object with the following properties will be passed to identify the updated record:</p>
<ul>
<li><b>entityType</b>: String. The entity type of the updated record.</li>
<li><b>id</b>: String. GUID of the updated record.</li>
</ul></td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to call when the operation fails. An object with the following properties will be passed:
<ul>
<li><b>errorCode</b>: Number. The error code.</li>
<li><b>message</b>: String. An error message describing the issue.</li>
</ul></td>
</tr>
</table>

## Return Value

On success, returns a promise object containing the attributes specified earlier in the description of the **successCallback** parameter.


### Related topics

[Web API](../webapi.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)