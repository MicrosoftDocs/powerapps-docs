---
title: Popup | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b0af1803-ae3a-41c2-a8a5-b15970bd6f96
---

# Popup

[!INCLUDE [popup-description](includes/popup-description.md)]

## closeOnOutsideClick

Indicates whether popup close on an outside mouse click.

**Type**: `boolean`

## content

Static DOM element to be inserted.

**Type**: [HTMLElement](https://developer.mozilla.org/docs/Web/API/HTMLElement)

## id

The id to be set to the anchor control if any.

**Type**: `string`

## name

The name of the Popup. Used like a reference to open Popups.

**Type**: `string`

## popupToOpen

The name of Popup which should be opened.

**Type**: `string`

### Remarks

Should be defined only in a root popup. To open nested popups, should be provided string like `rootName.nestedName.[allOtherNestedNames]`. To close popups, should be provided empty string. This property will be automatically propagated to children.

## type

The type of Popup

**Type**: `enum`

The `type` value is an enum with the following possible values

|Value|Member|
|--|--|
|1|Root|
|2|Nested|

### Remarks

Should be only one `Root` Popup for each set of Popups.

### Related topics

[PowerApps Control Framework API Reference](index.md)<br />
[PowerApps Control Framework Overview](../overview.md)
