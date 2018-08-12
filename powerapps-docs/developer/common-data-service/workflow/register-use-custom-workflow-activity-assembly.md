---
title: "Register and use a custom workflow activity assembly (Common Data Service for Apps) | Microsoft Docs"
description: "Learn about registering and using a custom workflow activity assembly"
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
    - "Dynamics 365 (online)"
ms.assetid: 2dd2fe35-f681-4548-9b2b-5ad7c8470b8d
caps.latest.revision: 50
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Register and use a custom workflow activity assembly

After you compile your custom workflow activity to create an assembly, you have to register the assembly with Common Data Service for Apps. Your custom activity then appears in the process form of CDS for Apps depending on which deployment you registered the custom workflow activity with.

<a name="register"></a>

## Register a custom workflow activity

 Custom workflow activity assemblies are registered using the Plug-in Registration tool. The tool provides a graphical user interface and supports registering assemblies that contain plug-ins or custom workflow activities. You must register the assembly in the sandbox (partial trust).

 For more information about how to register and deploy a custom activity assembly by using the tool, see [Specify the Name and Group Name for a Custom Workflow Activity](create-custom-workflow-activity.md#NameandGroupName).

> [!NOTE]
> [!INCLUDE [proc-download-plugin-registration-tool](../../../includes/proc-download-plugin-registration-tool.md)] The `PluginRegistration.exe` can be added to the Visual Studio **Tools** menu as an external tool to speed up the development process.

<a name="use"></a>

## Use a custom workflow activity in a process

After you have registered your custom workflow activity assembly, you can use it in the process designer in CDS for Apps.

To use your custom workflow activity in a process:

1. Sign in to CDS for Apps.
<!-- TODO: Update this for CDS portal
1. **Settings** > **Processes**. -->
1. Create or open an existing process.
1. In the process designer, click or tap **Add Step**. Your custom workflow activity name will appear in the drop-down list.

### See also

[Custom workflow activities (workflow assemblies)](custom-workflow-activities-workflow-assemblies.md)<br />
[Debug a custom workflow activity](debug-custom-workflow-activity.md)<br />
<!-- TODO:
[Plug-in isolation, trusts, and statistics](../plugin-isolation-trusts-statistics.md)<br />
[Register and Deploy Plug-Ins](../register-deploy-plugins.md) -->
