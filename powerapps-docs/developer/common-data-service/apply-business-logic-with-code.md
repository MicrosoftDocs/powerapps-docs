---
title: Apply business logic using code (Common Data Service)| Microsoft Docs
description: Learn how developers can use code to apply business logic in Common Data Service.
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
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Apply business logic using code

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Whenever possible, you should first consider applying one of the several declarative process options to define or apply business logic. More information: [Apply business logic in Common Data Service](../../maker/common-data-service/cds-processes.md)

When a declarative process doesn’t meet a requirement, as a developer you have several options. This topic will introduce common options to write code.

## Create a plug-in

You can write a .NET assembly to plug-in to the data transaction to apply business logic on the server. With Common Data Service there is a framework you use to register specific events to execute code defined within a class in an assembly. 

More information: [Write plug-ins to extend business processes](plug-ins.md)

## Create a workflow extension

You can write a .NET assembly to provide new options within the process designer. This method provides a new option for people using the workflow designer to apply a condition or perform a new action. A workflow extension can then be re-used by people who are not developers to apply the logic in your code.

More information: [Workflow extensions](workflow/workflow-extensions.md)

### See also

[Common Data Service Developer Overview](overview.md)
