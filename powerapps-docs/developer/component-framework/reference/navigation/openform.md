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

Model-driven apps

## Syntax

`context.navigation.openForm(options, parameters)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|options|`EntityFormOptions`|Yes|Entity form options for opening the form. The EntityFormOptions has the following attributes:<br/>- **createFromEntity**: `Lookup`. Designates a record that will provide default values based on mapped attribute values. The lookup object has the following String properties: `entityType`, `id`, and `name`. <br/>- **entityId**: `String`. ID of the entity record to display the form for.<br/>- **entityName**: `String`. Logical name of the entity to display the form for.<br/>- **formId**: `String`. ID of the form instance to be displayed.<br/>- **height**: `Number`. Height of the form window to be displayed in pixels.<br/>- **openInNewWindow**: `boolean`. whether to display form in a new window.<br/>- **useQuickCreateForm**: `Boolean`. whether to open a quick create form. If you do not specify this, by default `false` is passed.<br/>- **width**: `Number`. Width of the form window to be displayed in pixels.<br/>- **windowPosition**: `Number`. Specify one of the following values for the window position of the form on the screen: `1:center` <br/> `2:side`|
|parameters|`Object`|No|An dictionary object that passes extra parameters to the form. Invalid parameters will cause an error. More information [see field values using parameters passed to a form](https://docs.microsoft.com/en-us/powerapps/developer/model-driven-apps/set-field-values-using-parameters-passed-form) and [Configure a form to accept custom querystring parameters](https://docs.microsoft.com/en-us/powerapps/developer/component-framework/sample-controls/navigation-api-control)|

## Return Value

Type: `Promise`

## Remarks

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) and [File](https://developer.mozilla.org/docs/Web/API/File)


### Related topics

[Navigation](../navigation.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)