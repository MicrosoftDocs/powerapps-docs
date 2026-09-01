---
title: Apply business logic using code (Microsoft Dataverse)| Microsoft Docs
description: Learn how to write code to customize business data processing in Microsoft Dataverse.
ms.date: 08/28/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
suite: powerapps
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Apply business logic using code

Whenever possible, consider applying one of the several declarative process options to define or apply business logic. For more information, see [Apply business logic in Microsoft Dataverse](../../maker/data-platform/processes.md).

When a declarative process doesn't meet a requirement, you have several options as a developer. This article introduces common options to write code.

## Create a plug-in

You can write a custom event handler, known as a plug-in, and register it on the Dataverse server. Register the plug-in to execute on a specific event of the Dataverse database transaction. When executed, the plug-in can create, read, modify, or delete data being processed during the current database transaction. By using plug-ins, you can customize or extend the data processing of Dataverse.

For more information, see [Write plug-ins to extend business processes](plug-ins.md).

## Create a workflow extension

You can write and register custom workflow activities to provide more actions within the process designer. Users can apply your new actions in the workflow designer, such as a condition or a new operation. By using this approach, you can add new custom actions in the process designer for users of your environment.

For more information, see [Workflow extensions](workflow/workflow-extensions.md).

### See also

[Dataverse Developer Overview](overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
