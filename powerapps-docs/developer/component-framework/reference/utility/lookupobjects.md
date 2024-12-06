---
title: lookupObjects (Power Apps component framework API reference) | Microsoft Docs
description: Opens a lookup dialog allowing the user to select one or more items.
author: anuitz
ms.author: anuitz
ms.date: 03/01/2024
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
 - rarattay
---

# lookupObjects

[!INCLUDE [lookupobjects-description](includes/lookupobjects-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.utils.lookupObjects(lookupOptions)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|lookupOptions|`UtilityApi.LookupOptions`|Yes|Defines the options for opening the lookup dialog. See [Remarks](#remarks) |

## Return Value

Type: Promise<LookupValue[]>

## Remarks

The lookupOptions available for components is different from those for the [Client API Xrm.Utility.lookupObjects lookupOptions properties](../../../model-driven-apps/clientapi/reference/Xrm-Utility/lookupObjects.md#lookupoptions-properties) available for model-driven app client side scripts.

### lookupOptions properties

For components, lookupOptions parameter has the following properties:

|Property Name |Type |Required |Description |
|---|---|---|---|
|`allowMultiSelect`|Boolean|No|Indicates whether the lookup allows more than one item to be selected.|
|`defaultEntityType`|String|No|The default table type to use.|
|`defaultViewId`|String|No|The default view to use.|
|`entityTypes`|Array|Yes|The table types to display.|
|`searchText`|String|No|Indicates the default search term for the lookup control. This is supported only on [Unified Interface](/power-platform/admin/about-unified-interface).|
|`viewIds`|Array|No|The views to be available in the view picker. Only system views are supported.|

The `disableMru` and `filters` properties available for model-driven app client scripts are not available for components.


### Related articles

[Utility](../utility.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
