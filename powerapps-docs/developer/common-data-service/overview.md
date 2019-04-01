---
title: Common Data Service Developer Guide | Microsoft Docs
description: Learn how developers can add value using Common Data Service.
author: JimDaly
manager: annbe
ms.service: powerapps
ms.topic: article
ms.date: 03/27/2019
ms.author: jdaly
ms.reviewer: kvivek
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Common Data Service Developer Guide

PowerApps offers users, businesses, independent software vendors (ISVs), and systems integrators (SIs) a powerful platform for building line-of-business apps. **Common Data Service** is the underlying data platform for PowerApps that contains the core functionality of [Dynamics 365 for Customer Engagement platform](/dynamics365/customer-engagement/developer/developer-guide) such as server-side logic (plug-ins and workflows), business process flows, a highly sophisticated security model, and an extensible platform for developers to build apps. 

> [!NOTE]
> This effectively means that Common Data Service is also the underlying platform for Customer Engagement apps such as Dynamics 365 for Sales, Dynamics 365 for Customer Service, and Dynamics 365 for Marketing. If you are already experienced with Dynamics 365 for Customer Engagement apps, you will will be able to apply your experience to customize and extend Common Data Service to build apps. 

There are many aspects to how developers can contribute to creating apps that use Common Data Service. While it is possible to build an application with code using Common Data Service as your data source, most projects will use either [model-driven apps](/powerapps/maker/model-driven-apps/model-driven-app-overview) or [canvas apps](/powerapps/maker/canvas-apps/getting-started) to generate the experience that people will use. 

## Working with model-driven apps

Model-driven apps are built on Common Data Service, and can only connect to a Common Data Service environment. All the data that defines a model-driven app is stored within Common Data Service.

Model-driven apps share the method of distributing customizations and extensions used by Common Data Service using [Solutions](introduction-solutions.md).

Model driven apps also have a number of points for developers to write code to extend. For information on what developers can do with model-driven apps, see [Model-driven apps Developer Guide](../model-driven-apps/overview.md)

## Understand when to write code

Because Common Data Service includes many capabilities for people to configure custom business logic without writing code, the most common scenarios for developers to contribute involve filling spaces in-between where existing features may not provide functionality you need to meet a requirement. Fortunately, Common Data Service provides many points for developers to extend the common functionality using code.

For a developer who will contribute to projects it is important that they understand what can be done without writing code. You should familiarize yourself with these capabilities. More information: [What is Common Data Service?](../../maker/common-data-service/data-platform-intro.md) 

## Content for on-premises deployments

Common Data Service is not available for on-premise deployments at this time. Content in this guide does not include information about options that are only available for on-premises or internet facing deployments (IFD). For information related to these options, see the [Developer Guide for Dynamics 365 for Customer Engagement apps](/dynamics365/customer-engagement/developer/developer-guide).

> [!div class="nextstepaction"]
> [Get started](get-started-cds-developers.md)

### See also

[PowerApps for developers](/powerapps/#pivot=home&panel=developer)<br/>
[Model-driven apps Developer Guide](../model-driven-apps/overview.md)
