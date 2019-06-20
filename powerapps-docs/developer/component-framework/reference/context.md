---
title: Context | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
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



## client

The interface for `context.client`

**Type**: [Client](client.md)

## device

The interface for `context.device`

**Type**: [Device](device.md)

## factory

The interface for `context.factory`

**Type**: [Factory](factory.md)

## formatting

The interface for `context.formatting`

**Type**: [Formatting](formatting.md)

## mode

The interface for `context.mode`

**Type**: [Mode](mode.md)

## navigation

The interface for `context.navigation`

**Type**: [Navigation](navigation.md)

## parameters

The data provided to the control. Structure defined by the component’s manifest, corresponding to parameter and data-set nodes

**Type**: `TInputs`

## resources

The resource interface of `context.resource`

**Type**: [Resources](resources.md)

## updatedProperties

An array of strings indicated which values have changed on the context object since the last time it was passed to this control

**Type**: `string[]`

## userSettings

The interface for `context.userSettings`

**Type**: [UserSettings](usersettings.md)

## utils

The interface for `context.utils`

**Type**: [Utility](utility.md)

## webAPI

The interface for `context.webApi`

**Type**: [WebApi](webapi.md)

### Related topics

[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)