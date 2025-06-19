---
title: external-service-usage element | Microsoft Docs
description: Indicates whether this control is using external service or not.
author: anuitz
ms.author: anuitz
ms.date: 02/22/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# external-service-usage element

[!INCLUDE [external-service-usage-description](includes/external-service-usage-description.md)]

## Available for

Canvas apps

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

## Child Elements


|Element|Description|Occurrences|Available for|
|--|--|--|-------|
|[domain](domain.md)|[!INCLUDE [domain-description](includes/domain-description.md)]|0 or more|Canvas apps |


## Example 1

External usage enabled for www.microsoft.com only.

```xml
<external-service-usage enabled="true">
   <domain>www.Microsoft.com</domain>
</external-service-usage>
```

## Example 2

External usage enabled for multiple domains.

```xml
<external-service-usage enabled="false">
  <domain>www.contoso.com</domain>
  <domain>www.yourcompany.com</domain>
</external-service-usage>
```

## Example 3

External usage isn't enabled.

```xml
<external-service-usage enabled="false" />
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]