---
title: updateRecord | Microsoft Docs
description: Updates a table record.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
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

`context.webAPI.updateRecord(entityLogicalName, id, data).then(successCallback, errorCallback);`

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
<td>The table logical name of the record you want to update. For example: &quot;account&quot;.</td>
</tr>
<tr>
<td>id</td>
<td>String</td>
<td>Yes</td>
<td>GUID of the table record you want to update.</td>
</tr>
<tr>
<td>data</td>
<td>Object</td>
<td>Yes</td>
<td><p>A JSON object containing <code>key: value</code> pairs, where <code>key</code> is the property of the table and <code>value</code> is the value of the property you want to update.</p>
</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when a record is updated. An object with the following properties will be passed to identify the updated record:</p>
<ul>
<li><b>entityType</b>: String. The table type of the updated record.</li>
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

Type: LookupValue[]


### Related topics

[Web API](../webapi.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]