---
title: Regions overview | Microsoft Docs
description: Learn about regions in PowerApps
author: manasmams
manager: kfile
ms.service: powerapps
ms.component: pa-admin
ms.topic: conceptual
ms.date: 03/21/2018
ms.author: manasma
---

# Regions overview in PowerApps
## How do I find out where my app is deployed?
Your app is deployed in the region that hosts the environment. For example, if your environment is created in the Europe region, then your app is deployed in Europe data centers.

If you're an administrator, you can determine the region of each environment in the PowerApps admin center.

* Go to the [admin center](https://admin.powerapps.com), and sign in with your work account.
  
    In the admin center, all existing environments are listed on the **Environments** tab. This list shows the **Region** where your app is deployed:
  
   ![Environments tab](./media/regions-overview/environment-list.png)

## What regions are available?
* United States
* Canada
* Europe
* Asia
* Australia
* India
* Japan
* United Kingdom

## What features are specific to a given region?
Environments can be created in different regions, and are bound to that geographic location. When you create an app in an environment, that app is deployed in datacenters in that geographic location. This applies to any items you create in that environment, including  databases in the Common Data Service, apps, connections, gateways, and custom connectors.

For optimal performance, if your users are in Europe, create and use the environment in the Europe region. If your users are in the United States, create and use the environment in the U.S.

> [!NOTE]
> Currently, you can only create a database in a Production or Trial environment, which is in the same region as your Azure AD or Office 365 tenant's home region. We are working on enabling creation of database in environments created in a different region than your tenant's home location. Also, you currently cannot create a database in the default environment and an individual environment (created with PowerApps Community Plan).

> [!NOTE]
> On-premises data gateways aren't available in the India region or in custom environments. You must create gateways in the default environment.

<!-- test -->
