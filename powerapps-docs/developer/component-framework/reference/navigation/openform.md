---
title: openForm | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: bea56947-d976-4974-9ac7-2d5f5c7b6732
---

# openForm

[!INCLUDE [openform-description](includes/openform-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.navigation.openForm(options, parameters)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|options|`EntityFormOptions`|Yes|Entity form options for opening the form. The EntityFormOptions has the following attributes:<br/>- **createFromEntity**: `Lookup`. Designates a record that will provide default values based on mapped attribute values. The lookup object has the following String properties: `entityType`, `id`, and `name`. <br/>- **entityId**: `String`. ID of the entity record to display the form for.<br/>- **entityName**: `String`. Logical name of the entity to display the form for.<br/>- **formId**: `String`. ID of the form instance to be displayed.<br/>- **height**: `Number`. Height of the form window to be displayed in pixels.<br/>- **openInNewWindow**: `boolean`. whether to display form in a new window or a new tab. If you specify `true` and do not specify values for height or width, the form will display in a new tab. <br/>- **useQuickCreateForm**: `Boolean`. whether to open a quick create form. If you do not specify this, by default `false` is passed.<br/>- **width**: `Number`. Width of the form window to be displayed in pixels.<br/>- **windowPosition**: `Number`. Specify one of the following values for the window position of the form on the screen: `1:center` <br/> `2:side`|
|parameters|`Object`|No|An dictionary object that passes extra parameters to the form. Invalid parameters will cause an error. More information [see field values using parameters passed to a form](https://docs.microsoft.com/powerapps/developer/model-driven-apps/set-field-values-using-parameters-passed-form) and [Configure a form to accept custom query string parameters](https://docs.microsoft.com/powerapps/developer/component-framework/sample-controls/navigation-api-control)|

## Return Value

Type: `Promise<OpenFormSuccessResponse>`. The `openFormSuccessResponse` returns an array of type `savedEntityReference` with the values present in the [EntityReference](../entityreference.md) method.

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise)

### Related topics

[Navigation](../navigation.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)
