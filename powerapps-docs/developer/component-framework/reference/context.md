---
title: Context | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6e066350-9d22-4078-b497-26be7d2fa374
---

# Context

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

[!INCLUDE [context-description](includes/context-description.md)]

## Available for 

Model-driven apps

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

An array of strings indicated which values have changed on the context object since the last time it was passed to this component.

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

[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)