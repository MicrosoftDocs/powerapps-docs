---
title: "Custom workflow activities (workflow assemblies) (Common Data Service for Apps) | Microsoft Docs"
description: "Learn about registration and execution of custom workflow activities in addition to the out-of-box activities provided by Windows Workflow Foundation. You can write custom workflow activities in Microsoft Visual C# or Visual Basic .NET code by creating an assembly that contains one or more classes derived from the Windows Workflow FoundationCodeActivity class."
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
    - "Dynamics 365 (online)"
ms.assetid: d4e6e932-61cd-42fd-a280-ef63bbad45f0
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Custom workflow activities (workflow assemblies)

Common Data Service for Apps supports the registration and execution of custom workflow activities in addition to the out-of-box activities provided by [Windows Workflow Foundation](/dotnet/framework/windows-workflow-foundation/). Windows Workflow Foundation includes an [activity library](/dotnet/framework/windows-workflow-foundation/net-framework-4-5-built-in-activity-library) that provides activities for control flow, sending and receiving messages, doing work in parallel, and more. However, to build applications that satisfy your business needs, you may need activities that perform tasks specific to that application. To make this possible, Windows Workflow Foundation supports the creation of custom workflow activities.  
  
You can write custom workflow activities in Microsoft Visual C# or Visual Basic .NET code by creating an assembly that contains one or more classes derived from the Windows Workflow Foundation [CodeActivity](/dotnet/api/system.activities.codeactivity) class. This assembly is annotated with .NET attributes to provide the metadata that CDS for Apps uses at runtime to link your code to the workflow engine.  
  
After you have created an assembly that contains one or more custom workflow activities, you register this assembly with CDS for Apps. This process is similar to registering a plug-in. The custom workflow activity can then be incorporated into a workflow or dialog in the `Process` form in CDS for Apps. 
  
## In This Section  

[Creating a Custom Workflow Activity](workflow/create-custom-workflow-activity.md)<br />
[Adding Metadata to the Custom Workflow Activity](workflow/add-metadata-custom-workflow-activity.md)<br />
[Using the Web Services within a Custom Workflow Activity](workflow/use-iorganization-web-service-custom-workflow-activity.md)<br />
[Registering the Workflow Assembly](workflow/register-use-custom-workflow-activity-assembly.md)<br />
[Debugging a Custom Workflow Activity](workflow/debug-custom-workflow-activity.md)<br />
[Updating or Upgrading Custom Workflow Activity: Assembly Versioning](workflow/update-custom-workflow-activity-using-assembly-versioning.md)<br />
[Process Classes, Attributes, and Dynamics 365 Types](workflow/process-classes-attributes-and-types.md)<br />
[Sample: Create a custom workflow activity](workflow/sample-create-custom-workflow-activity.md)<br />
[Sample: Update Next Birthday Using a Custom Workflow Activity](workflow/sample-update-next-birthday-using-custom-workflow-activity.md)<br />
[Sample: Calculate a Credit Score with a Custom Workflow Activity](workflow/sample-calculate-credit-score-custom-workflow-activity.md)<br />
  
## Related Sections

<!-- TODO:
[Write Workflows to Automate Business Processes](automate-business-processes-customer-engagement.md)<br />
[Write Plug-Ins for Dynamics 365 Customer Engagement](write-plugin-extend-business-processes.md)<br />
[Plug-in Isolation, Trusts, and Statistics](plugin-isolation-trusts-statistics.md) -->
