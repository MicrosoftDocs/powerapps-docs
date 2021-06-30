---
title: deleteRecord | Microsoft Docs
description: Deletes a table record.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5c9968bf-d535-425c-b1f1-0db6b7822de1
---

# deleteRecord

[!INCLUDE [deleterecord-description](includes/deleterecord-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.webAPI.deleteRecord(entityLogicalName, id).then(successCallback, errorCallback);`

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
<td>The table logical name of the record you want to delete. For example: &quot;account&quot;. </td>
</tr>
<tr>
<td>id</td>
<td>String</td>
<td>Yes</td>
<td>GUID of the table record you want to delete.</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when a record is deleted. An object with the following properties will be passed to identify the deleted record:</p>
<ul>
<li><b>entityType</b>: String. The table type of the record.</li>
<li><b>id</b>: String. GUID of the record.</li>
<li><b>name</b>: String. Name of the record.</li>
</ul></td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to call when the operation fails.</td>
</tr>
</table>

## Return Value

Type: LookupValue[]

### Related topics

[Web API](../webapi.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]