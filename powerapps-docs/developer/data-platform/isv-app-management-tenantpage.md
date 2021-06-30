---
title: Tenant page of ISV Studio | Microsoft Docs
description: Learn about the Tenant page capabilities provided by the ISV Studio portal.
services: ''
suite: powerapps
documentationcenter: na
author: "nkrb" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.reviewer: nabuthuk
ms.workload: na
ms.date: 01/11/2021
ms.author: nabuthuk
search.audienceType: 
  - developer
search.app: 
  - PowerApps
---

# The Tenant page

To view the install history of a tenant, the ISV can switch to **Top tenants** view on the home page and select a tenant.

![Install history of a tenant](media/isv-portal-homepage-tenantpivot.png)

The Tenant page contains the following graphs and metrics:

![Tenant page](media/isv-portal-tenantpage.png)

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Installs by date

The line chart shown below illustrates the number of app installations occurred by date. 

When hovering over the graph, the following information is shown:

Install Count: Number of app installations happened on a particular date.

> [!div class="mx-imgBorder"]
> ![Successfully installed apps](media/isv-portal-tenantpage-graph1.png)

## Installs by geo

The pie chart shown below illustrates the number of app installations occurred by Geo.

When hovering over the graph, the following information is shown:

1. Geo
2. Install Count

> [!div class="mx-imgBorder"]
> ![Package installs by environment type](media/isv-portal-tenantpage-graph2.png)

## Installs by environment

The pie chart shown below illustrates the ratio of production vs. sandbox app installs across the install base.

When hovering over the graph, the following information is shown:

1. Environment
2. Install Count

> [!div class="mx-imgBorder"]
> ![Package Installs by environment location](media/isv-portal-tenantpage-graph3.png)

## Installs by application

The column chart shown below displays the package unique names where versions of the selected app are displayed. All packages are selected by default, and all installed versions of all package (by tenant) are displayed on the graph. The user can select one or more packages and versions for further slicing and dicing. When the user selects a package, the version drop-down is updated to have the corresponding version of the selected package.

When hovering over any item of the graph, the following information is shown:

1. Application
1. Count
1. Package
1. Version 
1. Environment

> [!div class="mx-imgBorder"]
> ![Package and version installs by environment](media/isv-portal-tenantpage-graph4.png)

## Filtering the tenant page

ISVs can filter the tenant page using the filters available. For example, an ISV can filter to see the metrics at Package & Solution version, Geo, and Date range level.

### See also

[Introduction to ISV Studio for the Power Platform](isv-app-management.md)  
[Home page](isv-app-management-homepage.md)<br/> 
[App page](isv-app-management-apppage.md)<br/> 
[AppSource checker](isv-app-management-appsource-checker.md)<br/> 
[Connector Certification](isv-app-management-certification.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]