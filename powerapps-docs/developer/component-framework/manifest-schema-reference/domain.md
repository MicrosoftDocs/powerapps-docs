---
title: domain element | Microsoft Docs
description: Indicates the domain that the external-usage-element applies to.
author: anuitz
ms.author: anuitz
ms.date: 02/22/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# domain Element

[!INCLUDE [domain-description](includes/domain-description.md)]

## Available for

Canvas apps

## Parent Elements

|Element|Description|
|--|--|
|[external-service-usage](external-service-usage.md)|[!INCLUDE [external-service-usage-description](includes/external-service-usage-description.md)]|

## Example

```xml
<external-service-usage enabled="true">
   <domain>www.Microsoft.com</domain>
</external-service-usage>
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]