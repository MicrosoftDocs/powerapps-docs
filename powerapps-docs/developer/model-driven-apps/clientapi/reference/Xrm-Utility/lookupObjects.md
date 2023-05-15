---
title: "lookupObjects (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the lookupObjects method.
author: chmoncay
ms.author: chmoncay
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
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
|defaultEntityType|String|No|The default table type to use.|
|defaultViewId|String|No|The default view to use.|
|disableMru|Boolean|No|Decides whether to display the most recently used(MRU) item.<br />Available only for Unified Interface.|
|entityTypes|Array|Yes|The table types to display.|
|filters|Array of objects|No|Used to filter the results. Each object in the array contains the following values:<br /><ul><li>**filterXml**: String. The FetchXML filter element to apply.</li><li>**entityLogicalName**: String. The table type to which to apply this filter.</li></ul>|
|searchText|String|No|Indicates the default search term for the lookup control. This is supported only on [Unified Interface](/power-platform/admin/about-unified-interface).|
|viewIds|Array|No|The views to be available in the view picker. Only system views are supported.|

**successCallback**: Function. A function to call when the lookup control is invoked. An array of objects with the following properties is passed:<br/><ul><li>**entityType**: String. table type of the record selected in the lookup control.</li><li>**id**: String. ID of the record selected in the lookup control.</li><li>**name**: String. Name of the record selected in the lookup control.</li></ul>


**errorCallback**: Function. A function to call when the operation fails. It is not considered a failure if the user cancels the operation.

## Example

```javascript
//define data for lookupOptions
var lookupOptions = 
{
  defaultEntityType: "account",
   entityTypes: ["account"],
  allowMultiSelect: false,
   defaultViewId:"0D5D377B-5E7C-47B5-BAB1-A5CB8B4AC10",
   viewIds:["0D5D377B-5E7C-47B5-BAB1-A5CB8B4AC10","00000000-0000-0000-00AA-000010001003"],
   searchText:"Allison",
   filters: [{filterXml: "<filter type='or'><condition attribute='name' operator='like' value='A%' /></filter>",entityLogicalName: "account"}]
};

// Get account records based on the lookup Options
Xrm.Utility.lookupObjects(lookupOptions).then(
  function(success){
console.log(success);},
function(error){console.log(error);});
```

### Related topics

[Xrm.Utility](../xrm-utility.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
