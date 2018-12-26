---
title: PowerApps for United States Government customers - Overview
description: For U.S. Government customers, learn about the features and limitations for the PowerApps US Government service
author: evchaki
manager: kvivek
ms.service: powerapps
ms.component: pa-admin
ms.topic: conceptual
ms.date: 03/21/2018
ms.author: evchaki
search.audienceType: 
  - admin
search.app: 
  - D365CE
  - PowerApps
  - Powerplatform

LocalizationGroup: Get started
---
# PowerApps for US Government customers
The **PowerApps service** has a version available for United States Government customers as part of the **Office 365 US Government Community** subscriptions. The **PowerApps service** version discussed in this article is specifically designed for US Government customers, and is separate and different from the commercial version of the **PowerApps service**.

The following sections describe the *features* available to the US Government version of the **PowerApps service**, clarifies some of the *limitations*, lists Frequently Asked Questions (**FAQ**) and answers (including how to sign up), and provides links for more information.

## Features of PowerApps US Government
The following features are available to **PowerApps US Government** customers:

* Create and run Canvas Apps
* Create data connections

## Connectivity between Government and Public Azure Cloud services 

Azure is distributed among multiple clouds. Be default, tenants are allowed to open firewall rules to a  cloud-specific instance, but cross-cloud networking is different and requires opening specific firewall rules to communicate between services. If you are a PowerApps customer and you have existing SQL instances in the public cloud which you need to access, you must open specific firewall rules in SQL to the Azure Government Cloud IP space, for the following datacenters:

* USGov Iowa
* USGov Virginia
* USGov Texas
* USGov Arizona

In the public cloud the IP spaces are available, but for the government cloud, you must open an Azure Support ticket to request the IP ranges for the above listed datacenters. 


## Limitations of PowerApps US Government
Some of the features that are available in the commercial version of the **PowerApps service** are *not* available in the **PowerApps service** for US Government customers. The PowerApps team is actively working on making these features available to US Government customers, and will update this article when these features become available.

* **Embed in SharePoint Online** - it is not possible to embed PowerApps content in SharePoint Online.
 
To resolve issues, please contact your account representative.

## Frequently Asked Questions (FAQ) for the US Government version of the Power BI service
The following questions (and answers) are provided to help you quickly get information you need about the service.

**Question:** Is the URL for connecting to **PowerApps** for US Government different than the commercial **PowerApps** URL?

**Answer:** Yes, the URLs are different. The following table shows each URL:

| Commercial version URL | US Government version URL |
| --- | --- |
| [https://web.powerapps.com](https://web.powerapps.com) |[https://gov.create.powerapps.us](https://gov.create.powerapps.us) |



## Next steps
There are all sorts of things you can do with PowerApps. For more information and learning, including an article that shows you how to sign up for the service, check out the following resources:

* [Guided Learning for PowerApps](/learn/browse/?products=bizapps-power-apps)
* [Get started with the PowerApps](/powerapps/#pivot=home&panel=getstarted)
