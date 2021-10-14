---
title: Popup | Microsoft Docs
description: Provides access to get all the information about the popup.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b0af1803-ae3a-41c2-a8a5-b15970bd6f96
---

# Popup

[!INCLUDE [popup-description](includes/popup-description.md)]

## Available for 

Model-driven apps

## Properties

### closeOnOutsideClick

Indicates whether popup close on an outside mouse click. When set to `false`, the popup will not be closed on an outside mouse click.

**Type**: `boolean`

### content

Static DOM element to be inserted.

**Type**: [HTMLElement](https://developer.mozilla.org/docs/Web/API/HTMLElement)

### id

The id to be set to the anchor component if any.

**Type**: `string`

### name

The name of the popup. Used as the reference to open popups.

**Type**: `string`

### popupToOpen

The name of popup which should be opened.

**Type**: `string`

### Remarks

Should be defined only in a root popup. To open nested popups, should be provided string like `rootName.nestedName.[allOtherNestedNames]`. To close popups, should be provided empty string. This property will be automatically propagated to children.

## type

The type of popup, which is described in the enum PopupType. There should be only one `root` popup for each set of popups.

**Type**: `enum`

The `type` value is an enum with the following possible values

|Value|Member|
|--|--|
|1|Root|
|2|Nested|

### Remarks

Should be only one `Root` Popup for each set of Popups.

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]