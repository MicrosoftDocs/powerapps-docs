---
title: Apply business logic using code (Common Data Service (CDS) for Apps)| Microsoft Docs
description: Learn how developers can use code to apply business logic in Common Data Service for Apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/26/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Apply business logic using code

Whenever possible, you should first consider applying one of the several declarative process options to define or apply business logic. More information: [Apply business logic using business processes and flows](../../maker/model-driven-apps/guide-staff-through-common-tasks-processes.md)

When a declarative process doesn’t meet a requirement, as a developer you have several options. This topic will introduce common options to write code.

## Create a plug-in

You can write a .NET assembly to plug-in to the data transaction to apply business logic on the server. With Common Data Service for Apps there is a framework you use to register specific events to execute code defined within a class in an assembly. 

More information: [Write plug-ins to extend business processes](plug-ins.md)

## Create a workflow extension

You can write a .NET assembly to provide new options within the process designer. This method provides a new option for people using the workflow designer to apply a condition or perform a new action. A workflow extension can then be re-used by people who are not developers to apply the logic in your code.

More information: [Workflow extensions](workflow/workflow-extensions.md)

### See also

[Common Data Service for Apps Developer Overview](overview.md)
