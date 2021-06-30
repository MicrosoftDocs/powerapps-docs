---
title: Client | Microsoft Docs
description: Provides access to the methods to determine which client is being used, whether the client is connected to server, and what kind of device is being used.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4ce41c82-bf4a-4d34-9344-5311c24d76de
---

# Client

[!INCLUDE [client-description](includes/client-description.md)]

## Syntax

`context.client;`

## Available for 

Model-driven and canvas apps

## Properties

### disableScroll

Disables the scrolling capabilities for the components. This property is supported in both model-driven and canvas apps.

**Type**: `boolean`

## Methods

|Method | Description |Available for|
| ------------- |-------------|------|
|[getClient](client/getclient.md)|[!INCLUDE [getclient-description](client/includes/getclient-description.md)]|Model-driven and canvas apps|
|[getFormFactor](client/getformfactor.md)|[!INCLUDE [getformfactor-description](client/includes/getformfactor-description.md)]|Model-driven and canvas apps|
|[isOffline](client/isoffline.md)|[!INCLUDE [isoffline-description](client/includes/isoffline-description.md)]|Model-driven apps|

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

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]