---
title: Context | Microsoft Docs
description: Provides all the properties and methods available in the Power Apps component framework
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 14/19/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6e066350-9d22-4078-b497-26be7d2fa374
---

# Context

[!INCLUDE [context-description](includes/context-description.md)]

## Available for

Model-driven and canvas apps

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

The data provided to the component. Structure defined by the component’s manifest, corresponding to parameter and dataset nodes.

**Type**: `TInputs`

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

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
