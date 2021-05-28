---
title: "formContext.data (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about working with processes in model-driven apps using client API."
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 32e8d1d0-4093-4588-a517-2930eec34dce
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# formContext.data (Client API reference)

Provides properties and methods to work with the data on a form.

![formContext Data object model](../../media/ClientAPI-formContext-data-Model.png)

## Properties

|Name|Description|
|--|--|
|attributes|Collection of non-table data on the form. Items in this collection are of the same type as the columns collection, but they are not columns of the form table. <br/>More information: [Collections](collections.md)|
|entity|Provides methods to retrieve information specific to the record displayed on the page, the save method, and a collection of all the columns included on the form. Column data is limited to columns represented on the form. <br/>More information: [formContext.data.entity](formContext-data-entity.md)|
|process|Provides objects and methods to interact with the business process flow data on a form.<br/>More information: [formContext.data.process](formContext-data-process.md)|

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## Methods 

|Name|Description|
|--|--|
|[addOnLoad](formContext-data/addOnload.md)|[!INCLUDE[formContext-data/includes/addOnLoad-description.md](formContext-data/includes/addOnLoad-description.md)]|
|[getIsDirty](formContext-data/getIsDirty.md)|[!INCLUDE[formContext-data/includes/getIsDirty-description.md](formContext-data/includes/getIsDirty-description.md)]|
|[isValid](formContext-data/isValid.md)|[!INCLUDE[formContext-data/includes/isValid-description.md](formContext-data/includes/isValid-description.md)]|
|[refresh](formContext-data/refresh.md)|[!INCLUDE[formContext-data/includes/refresh-description.md](formContext-data/includes/refresh-description.md)]|
|[removeOnLoad](formContext-data/removeOnLoad.md)|[!INCLUDE[formContext-data/includes/removeOnLoad-description.md](formContext-data/includes/removeOnLoad-description.md)]|
|[save](formContext-data/save.md)|[!INCLUDE[formContext-data/includes/save-description.md](formContext-data/includes/save-description.md)]|


### Related topics

[formContext.data.entity](formContext-data-entity.md)

[formContext.data.process](formContext-data-process.md)






[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]