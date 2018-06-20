---
title: "Debug a custom workflow activity (Common Data Service for Apps) | Microsoft Docs"
description: "Learn more about how to debug a custom workflow activity"
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 0922585a-006b-4229-8f6d-b7849062a156
caps.latest.revision: 15
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Debug a custom workflow activity

<!-- TODO:
This content is about debugging on the server and won't work for Common Data Service for Apps.
See https://community.dynamics.com/crm/b/microsoftdynamicscrmandstuff/archive/2013/03/08/debugging-workflow-custom-activities-with-plugin-registration-tool

Maybe this was supposed to refer to this:
[Analyze plug-in performance](../analyze-plugin-performance.md)
or
[Debug a plug-In](../debug-plugin.md)

To debug a custom workflow activity, copy the .pdb file for the assembly to the `%installdir%\server\bin\assembly` folder. The assembly can be deployed as on-disk or stored in the database. The recommended deployment is in the database, but for debugging you should select on-disk. Next, attach the debugger to the `CrmAsyncService.exe` process. Make sure that you remove the .pdb file when you’ve finished debugging because it uses memory to have it loaded. For detailed information, see [Debug a plug-In](../debug-plugin.md).   -->
  
### See also  
[Custom workflow activities (workflow assemblies)](../custom-workflow-activities-workflow-assemblies.md)   
[Update a custom workflow activity using assembly versioning](update-custom-workflow-activity-using-assembly-versioning.md)
