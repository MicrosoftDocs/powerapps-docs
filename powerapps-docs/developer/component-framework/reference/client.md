---
title: Client (Power Apps component framework API reference) | Microsoft Docs
description: Provides access to the methods to determine which client is being used, whether the client is connected to server, and what kind of device is being used.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# Client

[!INCLUDE [client-description](includes/client-description.md)]

## Syntax

`context.client;`

## Available for

Model-driven apps, canvas apps, & portals.

## Properties

### disableScroll

Disables the scrolling capabilities for the components. This property is supported in both model-driven and canvas apps.

**Type**: `boolean`

## Methods

| Method                                             | Description                                                                                    | Available for                |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------- |
| [getClient](client/getclient.md)                   | [!INCLUDE [getclient-description](client/includes/getclient-description.md)]                   | Model-driven and canvas apps |
| [getFormFactor](client/getformfactor.md)           | [!INCLUDE [getformfactor-description](client/includes/getformfactor-description.md)]           | Model-driven and canvas apps |
| [isOffline](client/isoffline.md)                   | [!INCLUDE [isoffline-description](client/includes/isoffline-description.md)]                   | Model-driven apps            |
| [isNetworkAvailable](client/isnetworkavailable.md) | [!INCLUDE [isnetworkavailable-description](client/includes/isnetworkavailable-description.md)] | Model-driven apps            |

## Example

```TypeScript
private createHTMLTableElement(): HTMLTableElement {
    let tableElement: HTMLTableElement = document.createElement("table");
    tableElement.setAttribute("class", "SampleControlHtmlTable_HtmlTable");
    let key: string = "Example Method";
    let value: string = "Result";
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, true));
    key = "getFormFactor()";
    value = String(this._context.client.getFormFactor());
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    key = "getClient()";
    value = String(this._context.client.getClient());
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
}
```

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
