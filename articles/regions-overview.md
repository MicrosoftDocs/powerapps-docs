<properties
	pageTitle="Overview of Environments | Microsoft PowerApps"
	description="What environments are, how to use them"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="RickSaling"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/20/2016"
   ms.author="ricksal"/>

# Regions overview in Microsoft PowerApps

## Q & A

#### Question: How do I find out where my data is stored?
All data is stored in the region that hosts the environment. For example, if your environment is created in the Europe region, then all your data is stored in Europe data centers.

The Microsoft PowerApps admin center shows you the region. This is only available to Administrators:

1. Go to [admin.powerapps.com](https://admin.powerapps.com), and sign-in with your work account.
2. In the admin center, all existing environments are listed, including the **Region** where your data is stored:

   ![](./media/regions-overview/environment-list.png)

#### Question: What regions are available?
The following regions are available, or will be available:

- United States
- Europe
- Asia
- Australia
- India
- Japan
- Canada (available after General Availability (GA))
- United Kingdom (available after General Availability (GA))  

#### Question: What features are specific to a given region?
Environments can be created in different regions, and are bound to that geographic location. When you create an app in an environment, that app is stored in datacenters in that geographic location. This applies to any items you create in that environment, including  databases in the Common Data Service, apps, connections, gateways, and custom APIs.

For the optimal performance, if your users are in Europe, then create and use the environment in the Europe region. If your users are in the United States, then create and use the environment in the U.S.

**Gateways**:
- Currently not available in the **India** region.
- Currently supported in the default environment. They are not supported in custom environments.
