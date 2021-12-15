---
title: Apply business logic using code (Microsoft Dataverse)| Microsoft Docs
description: Learn how to write code to customize business data processing in Microsoft Dataverse.
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
ms.date: 03/12/2021
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Apply business logic using code

Whenever possible, you should first consider applying one of the several declarative process options to define or apply business logic. More information: [Apply business logic in Microsoft Dataverse](../../maker/data-platform/processes.md)

When a declarative process doesn’t meet a requirement, as a developer you have several options. This topic will introduce common options to write code.

## Create a plug-in

You can write a custom event handler, known as a plug-in, and register it on the Dataverse server. The plug-in is registered to execute on a specific event of the Dataverse database transaction. When executed, the plug-in can create, read, modify, or delete data being processed during the current database transaction. In this way, plug-ins allow you to customize or extend the data processing of Dataverse.

More information: [Write plug-ins to extend business processes](plug-ins.md)

## Create a workflow extension

You can write and register custom workflow activities to provide additional actions within the process designer. Your new actions will be available in the workflow designer for users to apply - for example a condition or some new operation. In this way you can add new custom actions in the process designer for users of your environment.

More information: [Workflow extensions](workflow/workflow-extensions.md)

### See also

[Dataverse Developer Overview](overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]