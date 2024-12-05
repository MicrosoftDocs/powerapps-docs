---
title: "formContext.data.entity (Client API reference) in model-driven apps"
description: Provides properties and methods to retrieve information specific to the record displayed on the page, the save method, and a collection of all the columns included in the form.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# formContext.data.entity (Client API reference)

Provides properties and methods to retrieve information specific to the record displayed on the page, the save method, and a collection of all the columns included in the form. Column data is limited to columns represented on the form.

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## Properties

|Name|Description|
|--|--|
|`attributes`|Collection of columns for a record displayed on the form. <br/>More information: [Collections](collections.md) and [Columns](attributes.md).

## Methods

|Name|Description|
|---------|-----------|
|[addOnSave](formContext-data-entity/addOnSave.md)|[!INCLUDE[formContext-data-entity/includes/addOnSave-description.md](formContext-data-entity/includes/addOnSave-description.md)]| 
|[addOnPostSave](formContext-data-entity/addOnPostSave.md)|[!INCLUDE [addonpostsave-description](formContext-data-entity/includes/addonpostsave-description.md)]|
|[getDataXml](formContext-data-entity/getDataXml.md)|[!INCLUDE[formContext-data-entity/includes/getDataXml-description.md](formContext-data-entity/includes/getDataXml-description.md)]|
|[getEntityName](formContext-data-entity/getEntityName.md)|[!INCLUDE[formContext-data-entity/includes/getEntityName-description.md](formContext-data-entity/includes/getEntityName-description.md)]|
|[getEntityReference](formContext-data-entity/getEntityReference.md)|[!INCLUDE[formContext-data-entity/includes/getEntityReference-description.md](formContext-data-entity/includes/getEntityReference-description.md)]|
|[getId](formContext-data-entity/getId.md)|[!INCLUDE[formContext-data-entity/includes/getId-description.md](formContext-data-entity/includes/getId-description.md)]|
|[getIsDirty](formContext-data-entity/getIsDirty.md)|[!INCLUDE[formContext-data-entity/includes/getIsDirty-description.md](formContext-data-entity/includes/getIsDirty-description.md)]|
|[getPrimaryAttributeValue](formContext-data-entity/getPrimaryAttributeValue.md)|[!INCLUDE[formContext-data-entity/includes/getPrimaryAttributeValue-description.md](formContext-data-entity/includes/getPrimaryAttributeValue-description.md)]|
|[isValid](formContext-data-entity/isValid.md)|[!INCLUDE[formContext-data-entity/includes/isValid-description.md](formContext-data-entity/includes/isValid-description.md)]|
|[removeOnPostSave](formContext-data-entity/removeOnPostSave.md)|[!INCLUDE [removeonpostsave-description](formContext-data-entity/includes/removeonpostsave-description.md)]|
|[removeOnSave](formContext-data-entity/removeOnSave.md)|[!INCLUDE[formContext-data-entity/includes/removeOnSave-description.md](formContext-data-entity/includes/removeOnSave-description.md)]|
|[save](formContext-data-entity/save.md)|[!INCLUDE[formContext-data-entity/includes/save-description.md](formContext-data-entity/includes/save-description.md)]|

### Related articles

[Understand Xrm object model](../understand-clientapi-object-model.md)   
[Controls (Client API reference)](controls.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
