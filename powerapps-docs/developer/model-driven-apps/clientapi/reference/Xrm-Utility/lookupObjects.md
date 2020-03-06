---
title: "lookupObjects (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 01/24/2019
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# lookupObjects (Client API reference)



[!INCLUDE[./includes/lookupObjects-description.md](./includes/lookupObjects-description.md)] 

## Syntax

`Xrm.Utility.lookupObjects(lookupOptions).then(successCallback, errorCallback)`

## Parameters

**lookupOptions**: Object. Defines the options for opening the lookup dialog. Has the following properties:

|Property Name |Type |Required |Description |
|---|---|---|---|
|allowMultiSelect|Boolean|No|Indicates whether the lookup allows more than one item to be selected.|
|defaultEntityType|String|No|The default entity type to use.|
|defaultViewId|String|No|The default view to use.|
|disableMru|Boolean|No|Decides whether to display the most recently used(MRU) item.<br />Available only for Unified Interface.|
|entityTypes|Array|No|The entity types to display.|
|filters|Array of objects|No|Used to filter the results. Each object in the array contains the following attributes:<br /><ul><li>**filterXml**: String. The FetchXML filter element to apply.</li><li>**entityLogicalName**: String. The entity type to which to apply this filter.</li></ul>|
|searchText|String|No|Indicates the default search term for the lookup control. This is supported only on [Unified Interface](https://docs.microsoft.com/power-platform/admin/about-unified-interface).|
|showBarcodeScanner|Boolean|No|Indicates whether the lookup control should show the barcode scanner in mobile clients.|
|viewIds|Array|No|The views to be available in the view picker. Only system views are supported.|
|successCallback |Function |Yes |A function to call when the lookup control is invoked. An array of objects with the following properties is passed:<br/><ul><li>**entityType**: String. Entity type of the record selected in the lookup control.</li><li>**id**: String. ID of the record selected in the lookup control.</li><li>**name**: String. Name of the record selected in the lookup control.</li>|
|errorCallback |Function |Yes |A function to call when you cancel the lookup control or the operation fails.  |


### Related topics

[Xrm.Utility](../xrm-utility.md)
