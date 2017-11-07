---
title: Overview of regions | Microsoft Docs
description: 'Regions in PowerApps: where apps are deployed, available regions, features specific to a region'
services: ''
suite: powerapps
documentationcenter: na
author: skjerland
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 05/04/2017
ms.author: sharik

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

## What features are specific to a given region?
Environments can be created in different regions, and are bound to that geographic location. When you create an app in an environment, that app is deployed in datacenters in that geographic location. This applies to any items you create in that environment, including  databases in the Common Data Service, apps, connections, gateways, and custom connectors.

For optimal performance, if your users are in Europe, create and use the environment in the Europe region. If your users are in the United States, create and use the environment in the U.S.

> [!NOTE]
> On-premises data gateways aren't available in the India region or in custom environments. You must create gateways in the default environment.

