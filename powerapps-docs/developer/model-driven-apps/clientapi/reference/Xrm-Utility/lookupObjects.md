---
title: "lookupObjects (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# lookupObjects (Client API reference)



[!INCLUDE[./includes/lookupObjects-description.md](./includes/lookupObjects-description.md)] 

## Syntax

`Xrm.Utility.lookupObjects(lookupOptions).then(successCallback, cancelCallback)`

## Parameters

**lookupOptions**: Object. Defines the options for opening the lookup dialog. Has the following properties:

|Property Name |Type |Required |Description |
|---|---|---|---|
|allowMultiSelect|Boolean|No|Indicates whether the lookup allows more than one item to be selected.|
|defaultEntityType|String|No|The default entity type to use.|
|defaultViewId|String|No|The default view to use.|
|entityTypes|Array|No|The entity types to display.|
|showBarcodeScanner|Boolean|No|Indicates whether the lookup control should show the barcode scanner in mobile clients.|
|viewIds|Array|No|The views to be available in the view picker. Only system views are supported.|
|successCallback |Function |Yes |A function to call when the lookup control is invoked. An object with the following properties is passed:<br/>- **entityType**: String. Entity type of the record selected in the lookup control.<br/>- **id**: String. ID of the record selected in the lookup control.<br/>- **name**: String. Name of the record selected in the lookup control.|
|errorCallback |Function |Yes |A function to call when you cancel the lookup control or the operation fails.  |


### Related topics

[Xrm.Utility](../xrm-utility.md)