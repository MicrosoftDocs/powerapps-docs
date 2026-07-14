---
title: Visual Studio and the .NET platform
description: "Learn about managed code development tools and requirements."
ms.collection: get-started
ms.date: 07/06/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
ms.topic: article
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Visual Studio and the .NET platform

Microsoft Dataverse SDK assemblies support both .NET Framework and .NET Core code development. You can use Visual Studio, Visual Studio Code, or other tools to build your .NET managed code application, plug-in, or custom workflow activity.

> [!TIP]
> When you install .NET Framework on your development computer, be sure to install the Developer Pack and not just the run-time. For .NET Core, be sure to install the SDK. This installation enables you to choose the desired framework or SDK in the **New Project** dialog box of Visual Studio and in the target drop-down menu of the project's properties.  

You can use a Visual Studio Community edition for development. However, the Express edition doesn't support use of extensions, so you can't install available extensions in that version of Visual Studio.

More information: [Support for .NET Framework versions](../supported-customizations.md#support-for-net-framework-versions)

For a complete statement of supported and unsupported development, see [Supported customizations for Dataverse](../supported-customizations.md).

## See Also

-[Developer tools and resources](../developer-tools.md)
-[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
