---
title: SecurityPrivilegesMetadata (Power Apps component framework API reference) | Microsoft Docs
description: Information about table definitions security privileges.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# SecurityPrivilegesMetadata

Provides all the information about the table definitions security privileges.

## Available for

Model-driven apps

## Properties

|Name|Type|Description|
|-----|----|---------|
|CanBeBasic|boolean|Determines if the user has privilege depth as basic.|
|CanBeDeep|boolean|Determines if the user has privilege depth as deep.|
|CanBeEntityReference|boolean|Determines if the user has privilege depth as table/entity reference.|
|CanBeParentEntityReference|boolean|Determines if the user has privilege depth as parent table/entity reference.|
|CanBeLocal|boolean|Determines if the user has privilege depth as local.|
|Name|string|Name of the privilege.|
|PrivilegeId|string|The GUID of the privilege.|
|PrivilegeType|Object|Type of privilege like create, read, write.|


### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
