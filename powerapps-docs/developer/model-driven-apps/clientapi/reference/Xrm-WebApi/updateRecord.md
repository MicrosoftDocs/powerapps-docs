---
title: "updateRecord (Client API Reference) in Model-Driven Apps"
description: Learn how to use the updateRecord method in model-driven apps to update table records, with syntax, parameters, return values, and code examples.
author: sriharibs-msft
ms.author: srihas
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
ai-usage: ai-assisted
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# updateRecord (Client API reference)

[!INCLUDE[./includes/updateRecord-description.md](./includes/updateRecord-description.md)] 

## Syntax

`Xrm.WebApi.updateRecord(entityLogicalName, id, data).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`entityLogicalName`|String|Yes|The table logical name of the record you want to update. For example: `account`.|
|`id`|String|Yes|GUID of the table record you want to update.|
|`data`|Object|Yes|A JSON object containing `key: value` pairs, where `key` is the property of the table and `value` is the value of the property you want to update.<br />See [Examples](#examples) to see how you can define the `data` object for various update scenarios.|
|`successCallback`|Function|No|A function to call when a record is updated. See [Return Value](#return-value)|
|`errorCallback`|Function|No|[!INCLUDE [errorcallback-description](includes/errorcallback-description.md)]|


## Return value

On success, returns a promise object to the `successCallback` with the following properties:

|Name|Type|Description|
|---|---|---|
|`entityType`|String|The table logical name of the record.|
|`id`|String|GUID of the record.|

## Examples

These examples use some of the same request objects as demonstrated in [Update and delete table rows using the Web API](../../../../data-platform/webapi/update-delete-table-rows.md) to define the data object for updating a table record.

|Example|Demonstrates|Web API Example|
|---|---|---|
|[Basic update](#basic-update-example)|How to update column values on an existing account record.|[Basic update](../../../../data-platform/webapi/update-delete-table-rows.md#basic-update)|
|[Update associations to the related tables](#update-associations-to-the-related-tables-example)|How to change an account's primary contact using `@odata.bind`.|[Associate with a single-valued navigation property](../../../../data-platform/webapi/associate-disassociate-entities-using-web-api.md#associate-with-a-single-valued-navigation-property)|
|[Update associations to the related tables of type Activity](#update-associations-to-the-related-tables-of-type-activity-example)|How to associate a task with an opportunity or set its Regarding lookup to an account.|[Associate with a single-valued navigation property](../../../../data-platform/webapi/associate-disassociate-entities-using-web-api.md#associate-with-a-single-valued-navigation-property)|
|[Update associations for collection-valued navigation properties](#update-associations-for-collection-valued-navigation-properties-example)|How to associate and disassociate related records using `Xrm.WebApi.online.execute`.|[Add a record to a collection](../../../../data-platform/webapi/associate-disassociate-entities-using-web-api.md#add-a-record-to-a-collection) and [Remove a record from a collection](../../../../data-platform/webapi/associate-disassociate-entities-using-web-api.md#remove-a-record-from-a-collection)|

### Basic update example

Updates an existing account record with record ID = `5531d753-95af-e711-a94e-000d3a11e605`.

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

### Update associations to the related tables example

To update association to the related table records (lookups), set the value of single-valued navigation properties by using the `@odata.bind` annotation to point to another record.

Here is code example:

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

**Deprecated method for mobile offline scenario**

> [!NOTE]
>  Instead of using the `@odata.bind` annotation in the preceding example, the deprecated **lookup** object with case-sensitive properties (`logicalname` and `id`) is still supported for existing customizations. However, use of the `@odata.bind` annotation is recommended for both online and offline scenarios instead of using this deprecated object.

The following example uses the deprecated method to update an account record to associate another contact record as the primary contact for the account from mobile clients when working in the offline mode:

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

### Update associations to the related tables of type Activity example

To update associations to the related tables of type Activity, set the value of single-valued navigation properties by using the `@odata.bind` annotation to point to another record.

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

### Update associations for collection-valued navigation properties example

Use the [Xrm.WebApi.online.execute](online/execute.md) API to associate and disassociate collection-valued navigation properties. This feature isn't supported for mobile offline scenarios.

### Related articles

[Xrm.WebApi](../xrm-webapi.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
