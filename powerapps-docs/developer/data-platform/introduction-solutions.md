---
title: Introduction to solutions | Microsoft Docs
description: Learn about using solutions to package your Microsoft Dataverse customizations.
services: ''
suite: powerapps
documentationcenter: na
author: "shmcarth" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.reviewer: "pehecke"
ms.custom: intro-internal
ms.workload: na
ms.date: 03/17/2021
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Introduction to solutions

*Solutions* are how customizers and developers author, package, and maintain units of software that extend Microsoft Dataverse. For example, Dynamics 365 for Sales, Marketing, Customer Service apps are composed of solutions. Customizers and developers distribute solutions so that organizations can use Dataverse to install and uninstall the business functionality defined by the solution.

Every customization that you make to Dataverse, or to a previously installed solution, is part of a solution. Every change you apply is tracked and any dependencies can be calculated. When you export a managed solution, it contains all the changes that have been applied for that solution into a file that you can then import into a different Dataverse environment.

If you intend to transport customizations or extensions between different Dataverse environments or distribute solutions using AppSource, you must understand the solution framework.

> [!NOTE]
> For detailed information about how to effectively use solutions for a successful application lifecycle management (ALM) implementation, see [Application lifecycle management (ALM) with Microsoft Power Platform](/power-platform/alm).

### See also

[Solution concepts](/power-platform/alm/solution-concepts-alm)  
[Solution layers](/power-platform/alm/solution-layers-alm)  
[Managed properties](/power-platform/alm/managed-properties-alm)  
[Create packages for the Package Deployer tool](/power-platform/alm/package-deployer-tool)  
[Team development using shared source control](/power-platform/alm/basics-alm#team-development-using-shared-source-control)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]