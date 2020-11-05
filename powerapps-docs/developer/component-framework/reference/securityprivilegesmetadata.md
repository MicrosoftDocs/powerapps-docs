---
title: SecurityPrivilegesMetadata | Microsoft Docs
description: Information about table metadata security privileges.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2020
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# SecurityPrivilegesMetadata

Provides all the information about the table metadata security privileges.

## Available for

Model-driven apps

## Properties

|Name|Type|Description|
|-----|----|---------|
|CanBeBasic|boolean|Determines if the user has privilege depth as basic.|
|CanBeDeep|boolean|Determines if the user has privilege depth as deep.|
|CanBeEntityReference|boolean|Determines if the user has privilege depth as table reference.|
|CanBeParentEntityReference|boolean|Determines if the user has privilege depth as parent table reference.|
|CanBeLocal|boolean|Determines if the user has privilege depth as local.|
|Name|string|Name of the privilege.|
|PrivilegeId|string|The GUID of the privilege.|
|PrivilegeType|Object|Type of privilege like create, read, write.|


### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)