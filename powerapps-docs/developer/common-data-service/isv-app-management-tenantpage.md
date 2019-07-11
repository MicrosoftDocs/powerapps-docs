---
title: Tenant page of ISV Studio | Microsoft Docs
description: Learn about the Tenant page capabilities provided by the ISV Studio portal.
services: ''
suite: powerapps
documentationcenter: na
author: "phecke" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.reviewer: pehecke
ms.workload: na
ms.date: 07/11/2019
ms.author: prkoduku
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# The Tenant page

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The Tenant page contains the metrics described in the following sections of this topic.

![Tenant page](media/isv-portal-tenant-page.png)

## App installs by environment

The ISV app distribution across all environments of the selected tenant.

![isv-portal-app-installs-by-environment.png](media/isv-portal-app-installs-by-environment.png)

## Installs by environment type

Productions vs. sandbox installations of the ISV apps in the selected tenant.

![Installs by environment type](media/isv-portal-installs-by-environment-type.png)

## Installs by location

The geographical distribution of the tenant based on installs is displayed here.

![Installs by location](media/isv-portal-installs-by-tenant-location.png)

## App versions by environment

App names, package unique names, and versions of the selected tenant are displayed in drop-down menus. The first
    app package is selected by default, where all the installed versions of the
    selected package (by organization) is displayed on the graph. The user can
    select only one app and package at a time but can multi-select the package
    versions. When the user selects an app, the package drop-down is updated to
    display the corresponding packages of the selected app. When the user
    selects a package, the versions drop-down is updated to display the
    corresponding versions of the selected package.

![App versions by environment](media/isv-portal-app-versions-by-environment.png)

### See also

[Introduction to ISV Studio for the Power Platform](isv-app-management.md)  
[Home page](isv-app-management-homepage.md)  
[App page](isv-app-management-apppage.md)
