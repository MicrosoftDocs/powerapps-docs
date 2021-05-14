---
title: "retrieveRecord (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the retrieveRecord method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
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
# retrieveRecord (Client API reference)



[!INCLUDE[./includes/retrieveRecord-description.md](./includes/retrieveRecord-description.md)] 

## Syntax

`Xrm.WebApi.retrieveRecord(entityLogicalName, id, options).then(successCallback, errorCallback);`

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
<td>The table logical name of the record you want to retrieve. For example: "account".</td>
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
<p>You specify the query options starting with <code>?</code>. You can also specify multiple query options by using <code>&</code> to separate the query options. For example:</p>
<code>?$select=name&$expand=primarycontactid($select=contactid,fullname)</code>
<p>See examples later in this article to see how you can define the <code>options</code> parameter for various retrieve scenarios.</td>
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

On success, returns a promise containing a JSON object with the retrieved columns and their values.

## Examples

### Basic retrieve 

Retrieves the name and revenue of an account record with record ID = 5531d753-95af-e711-a94e-000d3a11e605.

```JavaScript
Xrm.WebApi.retrieveRecord("account", "a8a19cdd-88df-e311-b8e5-6c3be5a8b200", "?$select=name,revenue").then(
    function success(result) {
        console.log("Retrieved values: Name: " + result.name + ", Revenue: " + result.revenue);
        // perform operations on record retrieval
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

The above example displays the following in your console; you might see other values depending on your data:

`Retrieved values: Name: Sample Account, Revenue: 5000000`

### Retrieve related tables for a table instance by expanding single-valued navigation properties

 The following example demonstrates how to retrieve the contact for an account record with record ID = a8a19cdd-88df-e311-b8e5-6c3be5a8b200. For the related contact record, we are only retrieving the **contactid** and **fullname** properties.

```JavaScript
Xrm.WebApi.retrieveRecord("account", "a8a19cdd-88df-e311-b8e5-6c3be5a8b200", "?$select=name&$expand=primarycontactid($select=contactid,fullname)").then(
    function success(result) {
        console.log("Retrieved values: Name: " + result.name + ", Primary Contact ID: " + result.primarycontactid.contactid +
                ", Primary Contact Name: " + result.primarycontactid.fullname);
        // perform operations on record retrieval
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

The above example displays the following in your console; you might see other values depending on your data:

`Retrieved values: Name: Adventure Works, Primary Contact ID: 49a0e5b9-88df-e311-b8e5-6c3be5a8b200, Primary Contact Name: Adrian Dumitrascu`

 
### Related topics

[Xrm.WebApi.retrieveMultipleRecords](retrieveMultipleRecords.md)

[Xrm.WebApi](../xrm-webapi.md)






[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]