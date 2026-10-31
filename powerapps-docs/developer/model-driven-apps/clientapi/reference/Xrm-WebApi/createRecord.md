---
title: "createRecord (Client API Reference) in Model-Driven Apps"
description: Learn how to use the createRecord Client API method to create table records in model-driven apps, including syntax, parameters, return values, and examples.
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
# createRecord (Client API reference)

[!INCLUDE[./includes/createRecord-description.md](./includes/createRecord-description.md)] 

## Syntax

`Xrm.WebApi.createRecord(entityLogicalName, data).then(successCallback, errorCallback);`

## Parameters


|Name|Type|Required|Description|
|---|---|---|---|
|`entityLogicalName`|String|Yes|Logical name of the table you want to create. For example: `account`.|
|`data`|Object|Yes|A JSON object defining the columns and values for the new table record. See [Examples](#examples)|
|`successCallback`|Function|No|A function to call when a record is created. See [Return Value](#return-value)|
|`errorCallback`|Function|No|[!INCLUDE [errorcallback-description](includes/errorcallback-description.md)]|


## Return value

On success, returns a promise object to the `successCallback` with the following properties:

|Name|Type|Description|
|---|---|---|
|`entityType`|String|The table logical name of the new record.|
|`id`|String|GUID of the new record.|

## Examples

These examples use the same request objects as the following article: [Create a table row using the Web API](../../../../data-platform/webapi/create-table-row.md). The article shows how to define the data object for creating a table record.

|Example|Demonstrates|Web API Example|
|---|---|---|
|[Basic create](#basic-create-example)|How to create an account record with column values.|[Basic create](../../../../data-platform/webapi/create-table-row.md#basic-create)|
|[Create related table records along with the primary record](#create-related-table-records-along-with-the-primary-record-example)|How to create an account and related contact, opportunity, and task records in one operation.|[Create related table rows in one operation](../../../../data-platform/webapi/create-table-row.md#create-related-table-rows-in-one-operation)|
|[Associate tables when creating new records](#associate-tables-when-creating-new-records-example)|How to associate a new account with an existing contact using `@odata.bind`.|[Associate table rows on create](../../../../data-platform/webapi/create-table-row.md#associate-table-rows-on-create)|

### Basic create example

Creates a sample account record.

```JavaScript
// define the data to create new account
var data =
    {
        "name": "Sample Account",
        "creditonhold": false,
        "address1_latitude": 47.639583,
        "description": "This is the description of the sample account",
        "revenue": 5000000,
        "accountcategorycode": 1,
        "opendeals_date": new Date("2024-02-03T00:00:00Z")
    }

// create account record
Xrm.WebApi.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

> [!NOTE]
> Creating records with a primary image isn't supported for offline mode. You can set primary images only by using create in online mode. You can't set other image columns by using create. [Learn more about Primary images](../../../../data-platform/image-column-data.md#primary-images)

### Create related table records along with the primary record example

 You can create tables related to each other by defining them as navigation property values. This pattern is known as *deep insert*. In this example, you create a sample account record along with the primary contact record and an associated opportunity record.

> [!NOTE]
> Creating related table records in a single create operation isn't supported for offline mode.

```JavaScript
// define data to create primary and related table records
var data =
    {
        "name": "Sample Account",
        "primarycontactid":
        {
            "firstname": "John",
            "lastname": "Smith"
        },
        "opportunity_customer_accounts":
        [
            {
                "name": "Opportunity associated to Sample Account",
                "Opportunity_Tasks":
                [
                    { "subject": "Task associated to opportunity" }
                ]
            }
        ]
    }

// create account record
Xrm.WebApi.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Associate tables when creating new records example

To associate new table records to existing table records, set the value of single-valued navigation properties by using the `@odata.bind` annotation.

> [!NOTE]
> The names of single-valued navigation properties aren't always the same as the `LogicalName` for the lookup attribute. Ensure you're using the `Name` attribute value of the `NavigationProperty` element in the Web API $metadata service document. For more information, see [Web API Navigation Properties](../../../../data-platform/webapi/web-api-navigation-properties.md).

Here's a code example:

The following example creates an account record and associates it to an existing contact record to set the latter as the primary contact for the new account record:

```JavaScript
var data =
    {
        "name": "Sample Account",
        "primarycontactid@odata.bind": "/contacts(465b158c-541c-e511-80d3-3863bb347ba8)"
    }

// create account record
Xrm.WebApi.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

**Deprecated method for mobile offline scenario**

> [!NOTE]
> Instead of using the `@odata.bind` annotation example shown previously, the deprecated **lookup** object with case-sensitive properties (`logicalname` and `id`) is still supported for existing customizations. However, use the `@odata.bind` annotation for both online and offline scenarios instead of using this deprecated object.

The following example uses the deprecated method to create an account record and associate it to an existing contact record to set the latter as the primary contact for the new account record from mobile clients when working in the offline mode:

```JavaScript
var data =
    {
        "name": "Sample Account",
        "primarycontactid":
        {
            "logicalname": "contact",
            "id": "465b158c-541c-e511-80d3-3863bb347ba8"
        } 
    }

// create account record
Xrm.WebApi.offline.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```
 
### Related articles

[Create a table row using the Web API](../../../../data-platform/webapi/create-table-row.md)<br />
[Xrm.WebApi](../xrm-webapi.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
