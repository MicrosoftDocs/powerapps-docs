---
title: createRecord | Microsoft Docs
description: Creates a table record.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 9179f03b-9d26-4253-9535-13ab544d58ac
---

# createRecord

[!INCLUDE [createrecord-description](includes/createrecord-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.webAPI.createRecord(entityLogicalName, data).then(successCallback, errorCallback);`

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
<td>Logical name of the table you want to create. For example: &quot;account&quot;.</td>
</tr>
<tr>
<td>data</td>
<td>Object</td>
<td>Yes</td>
<td><p>A JSON object defining the columns and values for the new table record.</p>
<p>See examples later in this topic to see how you can define the <code>data</code> object for various create scenarios.</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when a record is created. An object with the following properties will be passed to identify the new record:</p>
<ul>
<li><b>entityType</b>: String. The table logical name of the new record.</li>
<li><b>id</b>: String. GUID of the new record.</li>
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