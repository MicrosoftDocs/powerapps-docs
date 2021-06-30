---
title: RetrieveRecord | Microsoft Docs
description: Retrieves a table record.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: dddeecc9-5067-420d-8bd7-4c914218e969
---

# retrieveRecord

[!INCLUDE [retrieverecord-description](includes/retrieverecord-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.webAPI.retrieveRecord(entityLogicalName, id, options).then(successCallback, errorCallback);`

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
<td>The table logical name of the record you want to retrieve. For example: &quot;account&quot;.</td>
</tr>
<tr>
<td>id</td>
<td>String</td>
<td>Yes</td>
<td>GUID of the table record you want to retrieve.</td>
</tr>
<tr>
<td>options</td>
<td>String</td>
<td>No</td>
<td><p>OData system query options, <b>$select</b> and <b>$expand</b>, to retrieve your data.</p>
<ul><li>Use the <b>$select</b> system query option to limit the properties returned by including a comma-separated list of property names. This is an important performance best practice. If properties aren’t specified using <b>$select</b>, all properties will be returned.</li>
<li>Use the <b>$expand</b> system query option to control what data from related tables is returned. If you just include the name of the navigation property, you’ll receive all the properties for related records. You can limit the properties returned for related records using the <b>$select</b> system query option in parentheses after the navigation property name. Use this for both <i>single-valued</i> and <i>collection-valued</i> navigation properties.</li>
</ul>
<p>You specify the query options starting with <code>?</code>. You can also specify multiple query options by using <code>&amp;</code> to separate the query options. For example:</p>
<code>?$select=name&amp;$expand=primarycontactid($select=contactid,fullname)</code>
</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when a record is retrieved. A JSON object with the retrieved properties and values will be passed to the function.</p>
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

Type: [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise)<[Entity](../entity.md)>



### Related topics

[Web API](../webapi.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]