---
title: "deleteRecord (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 848c277b-bd44-4388-852a-0f59a3a15538
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# deleteRecord (Client API reference)



[!INCLUDE[./includes/deleteRecord-description.md](./includes/deleteRecord-description.md)] 

## Syntax

`Xrm.WebApi.deleteRecord(entityLogicalName, id).then(successCallback, errorCallback);`

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
<td>The entity logical name of the record you want to delete. For example: "account". </td>
</tr>
<tr>
<td>id</td>
<td>String</td>
<td>Yes</td>
<td>GUID of the entity record you want to delete.</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when a record is deleted. An object with the following properties will be passed to identify the deleted record:</p>
<ul>
<li><b>entityType</b>: String. The entity type of the record.</li>
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

On success, returns a promise object containing the attributes specified earlier in the description of the **successCallback** parameter.

## Examples

These examples use some of the same request objects as demonstrated in [Update and delete entities using the Web API](../../../../common-data-service/webapi/update-delete-entities-using-web-api.md) to define the data object for updating an entity record.

Deletes an account with record ID = 5531d753-95af-e711-a94e-000d3a11e605.

```JavaScript
Xrm.WebApi.deleteRecord("account", "5531d753-95af-e711-a94e-000d3a11e605").then(
    function success(result) {
        console.log("Account deleted");
        // perform operations on record deletion
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```
 
### Related topics

[Xrm.WebApi](../xrm-webapi.md)




