---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Write a plug-in

<!-- This should be the how-to topic supporting the new tutorials

• Tutorial: Write a plug-in
• Tutorial: Debug a plug-in
• Tutorial: Update a plug-in

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/write-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/register-deploy-plugins

See Plug-in Tutorials written up at https://microsoft-my.sharepoint.com/:w:/p/jdaly/EZ1SzmOh-B5Bnt4C9rxGWysB6NtUQonOxq5sGSPkn5vNAA?e=wuehTb 

Plug-ins and workflow activities are both 'plug-ins'
Yet, I think workflow activities are easier to understand as 'workflow extensions' - because that is what they do... 

-->

The process of writing a plug-in is:

1. Create a .NET Framework Class library project in Visual Studio
1. Add the Microsoft.CrmSdk.CoreAssemblies NuGet package to the project
1. Implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface on classes that will be registered as steps.
1. Add your code to the <xref:Microsoft.Xrm.Sdk.IPlugin.Execute> method required by the interface
1. Sign & build the assembly
1. Test the assembly
    1. Register the assembly in a test environment
    1. Test the behavior of the assembly
    1. Verify expected trace logs are written
    1. Debug the assembly as needed



A plug-in is a class within an assembly created using a .NET Framework Class library project using .NET Framework 4.5.2 in Visual Studio. Each class in the project that will be registered as a step i

### See also

[Write plug-ins to extend business processes](plug-ins.md)
