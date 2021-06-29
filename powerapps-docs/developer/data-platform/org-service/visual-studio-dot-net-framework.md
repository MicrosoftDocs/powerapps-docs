---
title: "Visual Studio and the .NET Framework (Microsoft Dataverse) | Microsoft Docs" 
description: "Learn about managed code development tools and requirements."
ms.custom: intro-internal
ms.date: 07/03/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Visual Studio and the .NET Framework

The Microsoft Dataverse SDK assemblies are built using .NET Framework 4.6.2. You can use Visual Studio to build your managed code applications using .NET Framework 4.6.2 or later.

Plug-ins and custom workflow assemblies should use .NET Framework 4.6.2. While assemblies built using later versions should generally work, if they use any features introduced after 4.6.2 an error will occur.

> [!IMPORTANT]
> You should build any custom client applications using Microsoft .NET Framework 4.6.2 or later.
> Only applications using Transport Level Security (TLS) 1.2 or better security are allowed to connect with Dataverse. TLS 1.2 is not the default protocol used by .NET Framework 4.5.2, but it is in .NET Framework 4.6.2. 
>
> More information: <https://cloudblogs.microsoft.com/dynamics365/bdm/2017/09/28/updates-coming-to-dynamics-365-customer-engagement-connection-security/>
>
> [!TIP]
> When installing .NET Framework 4.6.2 on your development computer, be sure to install the developer pack and not just the run-time. This will enable the 4.6.2 Framework to be chosen in the **New Project** dialog box of Visual Studio and in the target framework drop-down menu of the project’s properties.  

You can use a Visual Studio Community edition for development. However, use of extensions isn’t supported in the Express edition so you won’t be able to install useful extensions in that version of Visual Studio.

More information: [Support for .NET Framework versions](/dynamics365/customer-engagement/developer/supported-extensions#SupportNET)

For a complete statement of supported and unsupported development, see [Supported Extensions for Dynamics 365](/dynamics365/customer-engagement/developer/supported-extensions#SupportNET).

## See Also

[Developer Tools](/dynamics365/customer-engagement/developer/developer-tools)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
