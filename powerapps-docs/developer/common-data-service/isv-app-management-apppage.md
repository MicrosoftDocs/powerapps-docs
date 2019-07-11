---
title: App page of ISV Studio | Microsoft Docs
description: Learn about the App page capabilities provided by the ISV Studio portal.
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

# The App page

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Once the user selects an app, the user is navigated to the app’s detail page
which provides a view to analyze the app’s installs across tenants.

![App detail page](media/isv-portal-app-detail-page.png)

The app detail page contains the metrics described in the following sections of this topic.

## Environment ratio

The production vs. sandbox installations of the app across tenants.

![Environment ratio](media/isv-portal-environment-ratio.png)

## Installs by tenant (28 days)

The number of successful vs. failed installations of the selected app (by tenant) over the last 28 days is displayed here.

![Installs by tenant (28 days)](media/isv-portal-installs-by-tenant(28d).png)

## Installs by location

The geographical distribution of the app by data region is displayed here.

![Installs by location](media/isv-portal-installs-by-location.png)

## Installed package versions by tenant

Displays the package unique names where versions of the selected app are displayed in a drop- down menu. The
    first package is selected by default, and all installed versions of the
    package (by tenant) are displayed on the graph. The user can select only one
    package at a time but can multi-select the versions. When the user selects a
    package, the versions drop down is updated to have the corresponding
    versions of the selected package.

![Installed versions by tenant](media/isv-portal-installed-versions-by-tenant.png)

### See also

[Introduction to ISV Studio for the Power Platform](isv-app-management.md)  
[Home page](isv-app-management-homepage.md)  
[Tenant page](isv-app-management-tenantpage.md)
