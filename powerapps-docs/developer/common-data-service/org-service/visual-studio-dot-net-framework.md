---
title: "Visual Studio and the .NET Framework (Common Data Service for Apps) | Microsoft Docs" 
description: "Learn about managed code development tools and requirements."
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Visual Studio and the .NET Framework

The .NET SDK assemblies for Common Data Service for Apps are built on .NET Framework 4.5.2. 

You can use Visual Studio to build your managed code applications using .NET Framework 4.5.2 or later. 

> [!IMPORTANT]
> You should build any custom client applications using Microsoft .NET Framework 4.6.2 or later.
> Only applications using Transport Level Security (TLS) 1.2 or better security are allowed to connect with CDS for Apps. TLS 1.2 is not the default protocol used by .NET Framework 4.5.2, but it is in .NET Framework 4.6.2.
> 
> More information: [Blog Post: Updates coming to Dynamics 365 Customer Engagement connection security](https://blogs.msdn.microsoft.com/crm/2017/09/28/updates-coming-to-dynamics-365-customer-engagement-connection-security/)
> 
> [!TIP]
> When installing .NET Framework 4.6.2 on your development computer, be sure to install the developer pack and not just the run-time. This will enable the 4.6.2 framework to be chosen in the **New Project** dialog box of Visual Studio and in the target framework drop-down menu of the project’s properties.  

You can use a Visual Studio Community edition for development. 

[comment]: <> (However, use of extensions isn’t supported in the Express edition so you won’t be able to install useful extensions in that version of Visual Studio)

More information: [Support for .NET Framework versions](/dynamics365/customer-engagement/developer/supported-extensions#SupportNET)

For a complete statement of supported and unsupported development, see [Supported Extensions for Dynamics 365](/dynamics365/customer-engagement/developer/supported-extensions#SupportNET).

## See Also

 [Developer Tools](/dynamics365/customer-engagement/developer/developer-tools)