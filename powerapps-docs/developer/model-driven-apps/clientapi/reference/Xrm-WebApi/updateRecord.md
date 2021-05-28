---
title: "updateRecord (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the updateRecord method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: f5d4c8a9-4188-472a-83bf-b986dd135754
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# updateRecord (Client API reference)



[!INCLUDE[./includes/updateRecord-description.md](./includes/updateRecord-description.md)] 

## Syntax

`Xrm.WebApi.updateRecord(entityLogicalName, id, data).then(successCallback, errorCallback);`

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
<td>The table logical name of the record you want to update. For example: "account".</td>
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
<td><p>A JSON object containing <code>key: value</code> pairs, where `key` is the property of the table and <code>value</code> is the value of the property you want to update.</p>
<p>See examples later in this topic to see how you can define the <code>data</code> object for various update scenarios.</td>
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

On success, returns a promise object containing the values specified earlier in the description of the **successCallback** parameter.

## Examples

These examples use some of the same request objects as demonstrated in [Update and delete tables using the Web API](../../../../data-platform/webapi/update-delete-entities-using-web-api.md) to define the data object for updating a table record.

### Basic update 

Updates an existing account record with record ID = 5531d753-95af-e711-a94e-000d3a11e605.

```JavaScript
// define the data to update a record
var data =
    {
        "name": "Updated Sample Account ",
        "creditonhold": true,
        "address1_latitude": 47.639583,
        "description": "This is the updated description of the sample account",
        "revenue": 6000000,
        "accountcategorycode": 2
    }
// update the record
Xrm.WebApi.updateRecord("account", "5531d753-95af-e711-a94e-000d3a11e605", data).then(
    function success(result) {
        console.log("Account updated");
        // perform operations on record update
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Update associations to the related tables

To update association to the related table records (lookups), set the value of single-valued navigation properties using the `@odata.bind` annotation to another record. However, for mobile clients in the offline mode, you cannot use the `@odata.bind` annotation, and instead have to pass a **lookup** object (**logicalname** and **id**) pointing to the target record. Here are code examples for both the scenarios:

**For online scenario (connected to server)**

The following example updates an account record to associate another contact record as the primary contact for the account:

```JavaScript
// define the data to update a record
var data =
    {
        "primarycontactid@odata.bind": "/contacts(61a0e5b9-88df-e311-b8e5-6c3be5a8b200)"
    }
// update the record
Xrm.WebApi.updateRecord("account", "5531d753-95af-e711-a94e-000d3a11e605", data).then(
    function success(result) {
        console.log("Account updated");
        // perform operations on record update
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

**For mobile offline scenario**

Here is the updated sample code to update an account record to associate another contact record as the primary contact for the account from mobile clients when working in the offline mode:

```JavaScript
// define the data to update a record
var data =
    {
        "primarycontactid":
        {
            "logicalname": "contact",
            "id": "61a0e5b9-88df-e311-b8e5-6c3be5a8b200"
        }
    }
// update the record
Xrm.WebApi.offline.updateRecord("account", "5531d753-95af-e711-a94e-000d3a11e605", data).then(
    function success(result) {
        console.log("Account updated");
        // perform operations on record update
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```
### Update associations to the related tables of type Activity

To update association to the related tables of type Activity, set the value of single-valued navigation properties using the `@odata.bind` annotation to another record.

**Update related opportunity column on task**

```JavaScript
// define the data to update a record
var data =
    {
        "new_relatedopportunities_task@odata.bind": "/opportunities(61a0e5b9-88df-e311-b8e5-6c3be5a8b200)"
    }
// update the record
Xrm.WebApi.updateRecord("task", "5531d753-95af-e711-a94e-000d3a11e605", data).then(
    function success(result) {
        console.log("Task updated");
        // perform operations on record update
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```
**Update Regarding column on task**

 ```JavaScript
// define the data to update a record
var data =
    {
        "regardingobjectid_account_task@odata.bind": "/accounts(61a0e5b9-88df-e311-b8e5-6c3be5a8b200)"
    }
// update the record
Xrm.WebApi.updateRecord("task", "5531d753-95af-e711-a94e-000d3a11e605", data).then(
    function success(result) {
        console.log("Task updated");
        // perform operations on record update
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Update associations for collection-valued navigation properties
The [Xrm.WebApi.online.execute](online/execute.md) API can be used to associate and disassociate collection-valued navigation properties. This is **NOT** supported for mobile offline scenarios.

### Related topics

[Xrm.WebApi](../xrm-webapi.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]