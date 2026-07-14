---
title: "retrieveRecord (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the retrieveRecord method.
author: sriharibs-msft
ms.author: srihas
ms.date: 04/29/2025
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# retrieveRecord (Client API reference)



[!INCLUDE[./includes/retrieveRecord-description.md](./includes/retrieveRecord-description.md)] 

## Syntax

`Xrm.WebApi.retrieveRecord(entityLogicalName, id, options).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`entityLogicalName`|String|Yes|The table logical name of the record you want to retrieve. For example: `account`.|
|`id`|String|Yes|GUID of the table record you want to retrieve.|
|`options`|String|No|OData system query options to control what is returned. See [Options](#options)|
|`successCallback`|Function|No|A function to call when a record is retrieved. A JSON object with the retrieved properties and values passed to the function.|
|`errorCallback`|Function|No|[!INCLUDE [errorcallback-description](includes/errorcallback-description.md)]|

## Options

To control what is returned, use the `$select` and `$expand` OData system query options to retrieve your data.

Use the `$select` system query option to limit the properties returned by including a comma-separated list of property names. Selecting specific properties is an important performance best practice. If properties aren't specified using `$select`, all properties are returned.

Use the `$expand` system query option to control what data from related tables is returned. If you just include the name of the navigation property, you receive all the properties for related records. You can limit the properties returned for related records using the `$select` system query option in parentheses after the navigation property name. Use this for both *single-valued* and *collection-valued* navigation properties. For offline we only support nested `$select` option inside the  `$expand`.

You specify the query options starting with `?`. You can also specify multiple query options by using `&` to separate the query options. For example:

`?$select=name&$expand=primarycontactid($select=contactid,fullname)`

See [Examples](#examples) to see how you can define the options parameter for various retrieve scenarios.


## Return Value

On success, returns a promise containing a JSON object with the retrieved columns and their values.
If the requested record doesn't exist, returns an error.

## Examples

See the following examples:

- [Basic retrieve](#basic-retrieve)
- [Retrieve related tables for a table instance by expanding single-valued navigation properties](#retrieve-related-tables-for-a-table-instance-by-expanding-single-valued-navigation-properties)

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

The above example displays the following text in your console; you might see other values depending on your data:

`Retrieved values: Name: Sample Account, Revenue: 5000000`

### Retrieve related tables for a table instance by expanding single-valued navigation properties

 The following example demonstrates how to retrieve the contact for an account record with record ID = a8a19cdd-88df-e311-b8e5-6c3be5a8b200. For the related contact record, we're only retrieving the **contactid** and **fullname** properties.

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

The above example displays the following text in your console; you might see other values depending on your data:

`Retrieved values: Name: Adventure Works, Primary Contact ID: 49a0e5b9-88df-e311-b8e5-6c3be5a8b200, Primary Contact Name: Adrian Dumitrascu`

 
### Related articles

[Xrm.WebApi.retrieveMultipleRecords](retrieveMultipleRecords.md)   
[Xrm.WebApi](../xrm-webapi.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
