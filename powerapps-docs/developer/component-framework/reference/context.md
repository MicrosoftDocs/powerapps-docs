---
title: Context | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6e066350-9d22-4078-b497-26be7d2fa374
---

# Context

[!INCLUDE [context-description](includes/context-description.md)]

## Available for 

Model-driven apps and canvas apps (public preview)

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

The data provided to the component. Structure defined by the component’s manifest, corresponding to parameter and data-set nodes.

**Type**: `TInputs`

### resources

The resource interface of `context.resource`

[!INCLUDE [resource-description](includes/resources-description.md)]

### updatedProperties

An array of strings with values that have changed since the last time it was passed and [parameters](#parameters). `updatesProperties` is currently only supported for model-driven apps and always returns empty string for canvas apps.

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