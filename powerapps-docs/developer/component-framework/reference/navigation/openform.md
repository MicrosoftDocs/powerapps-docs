---
title: openForm | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: bea56947-d976-4974-9ac7-2d5f5c7b6732
---

# openForm

[!INCLUDE [openform-description](includes/openform-description.md)]

## Available for 

Model-driven apps only

## Syntax

`openForm(options, parameters)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|options|`EntityFormOptions`|yes|The EntityFormOptions has the following attributes:<br/>- **createFromEntity**: [EntityReference](../entityreference.md). Designates a record that will provide default values based on mapped attribute values. The lookup object has the following String properties: entityType, id, and name. <br/>- **entityId**: `string`. ID of the entity record to display the form for.<br/>- **entityName**: `string`. Logical name of the entity to display the form for.<br/>- **formId**: `string`. ID of the form instance to be displayed.<br/>- **height**: `number`. Height of the form window to be displayed in pixels.<br/>- **openInNewWindow**: `boolean`. whether to display form in a new window.<br/>- **useQuickCreateForm**: `boolean`. whether to open a quick create form. If you do not specify this, by default `false` is passed.<br/>- **width**: `number`. Width of the form window to be displayed in pixels.<br/>- **windowPosition**: `number`. Specify one of the following values for the window position of the form on the screen: `1:center` <br/> `2:side`|
|parameters|`key`|yes|Entity form parameters.|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)


### Related topics

[Navigation](../navigation.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)