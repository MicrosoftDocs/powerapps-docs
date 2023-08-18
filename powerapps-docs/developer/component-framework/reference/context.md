---
title: Context (Power Apps component framework API reference) | Microsoft Docs
description: Provides all the properties and methods available in the Power Apps component framework
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Context

[!INCLUDE [context-description](includes/context-description.md)]

[FAQ: How can I access the record ID or table name?](../faq.yml#how-can-i-access-the-record-id-or-table-name)

## Available for

Model-driven apps, canvas apps, & portals.

## Properties

### client

[!INCLUDE [client-description](includes/client-description.md)]
**Type**: [Client](client.md)

### device

[!INCLUDE [device-description](includes/device-description.md)]

**Type**: [Device](device.md)

### factory

[!INCLUDE [factory-description](includes/factory-description.md)]

**Type**: [Factory](factory.md)

### formatting

[!INCLUDE [formatting-description](includes/formatting-description.md)]

**Type**: [Formatting](formatting.md)

### mode

[!INCLUDE [mode-description](includes/mode-description.md)]

**Type**: [Mode](mode.md)

### navigation

[!INCLUDE [navigation-description](includes/navigation-description.md)]

**Type**: [Navigation](navigation.md)

### parameters

The data provided to the component. Structure defined by the component's manifest, corresponding to parameter and dataset nodes.

**Type**: `IInputs`

### resources

The resource interface of `context.resources`

[!INCLUDE [resource-description](includes/resources-description.md)]

**Type**: [Resources](resources.md)

### updatedProperties

An array of strings with values that have changed since the last time it was passed and [parameters](#parameters). More information: [updatedProperties](updatedproperties.md)

**Type**: `string[]`

### userSettings

[!INCLUDE [usersettings-description](includes/usersettings-description.md)]

**Type**: [UserSettings](usersettings.md)

### utils

[!INCLUDE [utility-description](includes/utility-description.md)]

**Type**: [Utility](utility.md)

### webAPI

[!INCLUDE [webapi-description](includes/webapi-description.md)]

**Type**: [WebApi](webapi.md)

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
