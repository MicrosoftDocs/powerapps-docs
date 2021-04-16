---
title: "formContext.data.entity (Client API reference) in model-driven apps| MicrosoftDocs"
description: Provides properties and methods to retrieve information specific to the record displayed on the page, the save method, and a collection of all the columns included in the form.
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

# formContext.data.entity (Client API reference)

Provides properties and methods to retrieve information specific to the record displayed on the page, the save method, and a collection of all the columns included in the form. Column data is limited to columns represented on the form.

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## Properties

|Name|Description|
|--|--|
|attributes|Collection of columns for a record displayed on the form. <br/>More information: [Collections](collections.md) and [Columns](attributes.md).

## Methods

|Name|Description|
|---------|-----------|
|[addOnSave](formContext-data-entity/addOnSave.md)|[!INCLUDE[formContext-data-entity/includes/addOnSave-description.md](formContext-data-entity/includes/addOnSave-description.md)]| 
|[addOnPostSave](events/postsave.md)|This method is used to support or execute custom logic using web resources to perform after `Save` actions when the `save` event is successful or failed due to server errors.| 
|[getDataXml](formContext-data-entity/getDataXml.md)|[!INCLUDE[formContext-data-entity/includes/getDataXml-description.md](formContext-data-entity/includes/getDataXml-description.md)]|
|[getEntityName](formContext-data-entity/getEntityName.md)|[!INCLUDE[formContext-data-entity/includes/getEntityName-description.md](formContext-data-entity/includes/getEntityName-description.md)]|
|[getEntityReference](formContext-data-entity/getEntityReference.md)|[!INCLUDE[formContext-data-entity/includes/getEntityReference-description.md](formContext-data-entity/includes/getEntityReference-description.md)]|
|[getId](formContext-data-entity/getId.md)|[!INCLUDE[formContext-data-entity/includes/getId-description.md](formContext-data-entity/includes/getId-description.md)]|
|[getIsDirty](formContext-data-entity/getIsDirty.md)|[!INCLUDE[formContext-data-entity/includes/getIsDirty-description.md](formContext-data-entity/includes/getIsDirty-description.md)]|
|[getPrimaryAttributeValue](formContext-data-entity/getPrimaryAttributeValue.md)|[!INCLUDE[formContext-data-entity/includes/getPrimaryAttributeValue-description.md](formContext-data-entity/includes/getPrimaryAttributeValue-description.md)]|
|[isValid](formContext-data-entity/isValid.md)|[!INCLUDE[formContext-data-entity/includes/isValid-description.md](formContext-data-entity/includes/isValid-description.md)]|
|[removeOnSave](formContext-data-entity/removeOnSave.md)|[!INCLUDE[formContext-data-entity/includes/removeOnSave-description.md](formContext-data-entity/includes/removeOnSave-description.md)]|
|[save](formContext-data-entity/save.md)|[!INCLUDE[formContext-data-entity/includes/save-description.md](formContext-data-entity/includes/save-description.md)]|

### Related topics

[Understand Xrm object model](../understand-clientapi-object-model.md)

[Controls (Client API reference)](controls.md)






[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]