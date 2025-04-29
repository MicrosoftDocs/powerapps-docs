---
title: "deleteRecord (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the deleteRecord method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# deleteRecord (Client API reference)

[!INCLUDE[./includes/deleteRecord-description.md](./includes/deleteRecord-description.md)] 

## Syntax

`Xrm.WebApi.deleteRecord(entityLogicalName, id).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`entityLogicalName`|String|Yes|The table logical name of the record you want to delete. For example: `account`.|
|`id`|String|Yes|GUID of the table record you want to delete.|
|`successCallback`|Function|No|A function to call when a record is deleted. See [Return Value](#return-value)|
|`errorCallback`|Function|No|A function to call when the operation fails. An object with the following properties is passed:<br /> - `errorCode`: Number. The error code as a positive decimal number.  For example, the error code documented as `0x80040333` will be returned as `2147746611`.<br /> - `message`: String. An error message describing the issue.|

## Return Value

On success, returns a promise object to the `successCallback` with the following properties:

|Name|Type|Description|
|---|---|---|
|`entityType`|String|The table logical name of the record.|
|`id`|String|GUID of the record.|
|`name`|String|Name of the  record.|

## Examples

These examples use some of the same request objects as demonstrated in [Update and delete tables using the Web API](../../../../data-platform/webapi/update-delete-entities-using-web-api.md) to define the data object for updating an entity record.

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
 
### Related articles

[Xrm.WebApi](../xrm-webapi.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
