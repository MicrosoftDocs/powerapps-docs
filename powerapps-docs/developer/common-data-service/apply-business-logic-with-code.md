---
title: Apply business logic with code | Microsoft Docs
description: Learn how developers can use code to apply business logic in Common Data Service for Apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/26/2018
ms.author: jdaly
---

<!-- This topic was not migrated it was written for PowerApps -->

# Apply business logic with code

Whenever possible, you should first look to applying one of several declarative process options when a requirement involves defining business logic. See [Create custom business logic through processes](../../maker/model-driven-apps/guide-staff-through-common-tasks-processes.md)

When a declarative process doesn’t meet a requirement, as a developer you have several options. This topic will introduce common options to write code.

## Create a workflow extension

You can write a .NET assembly to provide new options within the process designer. This method provides a new option for people using the workflow designer to apply a condition or perform a new action. A workflow extension can then be re-used by people who are not developers to apply the logic in your code.

More information: [Custom workflow activities (workflow assemblies)](custom-workflow-activities-workflow-assemblies.md)

## Create a plug-in

You can write a .NET assembly to plug-in to the data transaction to apply business logic on the server. With Common Data Service for Apps there is a framework you use to register specific events to execute code defined within a class in an assembly. 

More information: [Write plug-ins to extend business processes](plug-ins.md)

### See also

[Common Data Service for Apps Developer Overview](overview.md)
