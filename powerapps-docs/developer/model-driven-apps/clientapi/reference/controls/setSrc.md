---
title: "setSrc (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setSrc method.
author: chmoncay
ms.author: chmoncay
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setSrc (Client API reference)



Sets the URL to be displayed in an IFRAME or web resource. 

## Control types supported

iframe, webresource

## Syntax

`formContext.getControl(arg).setSrc(string);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`string`|String|Yes|The URL.|

### Related articles

[getSrc](getSrc.md)<br/>
[Known issues: Component from an IFRAME](/power-platform/admin/doc-management-known-issues#components-from-an-iframe)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
