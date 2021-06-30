---
title: Introductions to the Power Platform ISV Studio app install failure analytics| Microsoft Docs
description: Measure app's performance and get insights.
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
ms.date: 10/28/2020
ms.author: nabuthuk
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Install failures


[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

As an ISV, you need data like failure details or failure count to quickly resolve the issues for the customers. You can use the install failures feature to get the install failures data. 

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The install failures features makes it easy for you to quickly resolve the issues that customer encounter while installing your application by providing the detailed error logs thus reducing the time for the customers to get the issues resolved.

With the install failures feature, you can see the install failures data by date, GEO, package, and by solution version. You can also see the failure details on the install failures dashboard. 

> [!div class="mx-imgBorder"]
> ![Install failure dashboard](media/isv-install-failure-report.png "Install failure dashboard")
 
## View the install failure dashboard

To view the install failure data:

1. Sign in to [ISV studio](https://aka.ms/ISVStudio/).
1. On the **Home** page, you can see a list of published applications. Select the desired application for which you want to see the install failure details. 
1. Scroll-down to the page to view all the apps. Select the app and select the **Install Failures** tab.
1. You can also see the install failure details by directly selecting the install failure icon from the list of apps as shown in the screenshot:

   > [!div class="mx-imgBorder"]
   > ![Failure icon](media/isv-install-failure-icon.png "Failure icon")

The install failures tab contains the following graphs and metrics.

### Failure by date

The line chart shown below illustrates the number of app installation failures occurred by date. When hovering over the graph, the following information is shown:

 1. Failure Count 
 1. Date 

> [!div class="mx-imgBorder"]
> ![Date](media/isv-failure-by-date.png "Date")

### Failure by Geo

The pie chart shown below illustrates the number app installation failures by GEO. When hovering over the graph, the following information is shown:

1. Geo 
1. Failure Count

> [!div class="mx-imgBorder"]
> ![Geo](media/isv-failure-by-geo.png "Geo")

### Failure by solution version

The bar chart shown below illustrates the number of app installation failures occurred by package version. When hovering over the graph, the following information is shown:

1. Package Version
1. Failure Type
1. Failure Count

> [!div class="mx-imgBorder"]
> ![Package version](media/isv-failure-by-package-version.png "Package version")

### Failure details

Tracks the information about the app install failure error in detail. The following details are shown in the failure details tab:

1. Category
1. Date 
1. Count
1. Failure
1. Type
1. Package
1. Version
1. Environment
1. Tenant

> [!div class="mx-imgBorder"]
> ![Install error details](media/isv-install-error-details.png "Install error details")

You can drill through the **Failure** column to see the full failure details. To see the full failure details, right-click on one of the error messages on the **Failure details** tab and then select **Drill through** > **Failure details**.

> [!div class="mx-imgBorder"]
> ![Failure details](media/isv-failure-details-drill-through.png "Failure details")

### Filtering the install failure dashboard

ISVs can filter the install failures dashboard using the filters available. For example, an ISV can filter to see the metrics at **Package & Solution version**, **Geo**, and **Date range** level.   

### See also

[App usage analytics](isv-app-usage-analytics.md)<br/>
[Home page](isv-app-management-homepage.md)  
[App page](isv-app-management-apppage.md)<br/> 
[Tenant page](isv-app-management-tenantpage.md)<br/>
[AppSource checker](isv-app-management-appsource-checker.md)<br/>
[Connector Certification](isv-app-management-certification.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]