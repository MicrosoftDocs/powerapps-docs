<properties
	pageTitle="How to migrate apps between environments and tenants | Microsoft PowerApps"
	description="How to migrate apps among environments and tenants"
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
   ms.date="10/19/2016"
   ms.author="ricksal"/>

# Environment and tenant app migration
Learn how to migrate an app from one environment to another.

## The scenario
One common scenario where you may want to migrate apps is where you have a Test or Dev environment and a Production environment. Here, developers and testers have wide access to the apps. When it comes time to migrate a new app to production, that environment has rigorous control over permissions to update and change it.

Another scenario is one where each customer has their own environment and data, and when a new customer is added, a new environment is created for them, and you would migrate a number of apps into their environment.

## Migrating an app

When preparing to migrate an app into another environment, the following artifacts are needed:
* a business data platform export package
* a <powerapp-name>.msapp files)
* Swagger files and icons for any custom APIs

### Importing the business data platform export package
creating a new role

### Recreating the custom APIs in the new environment

### Recreating the apps in the new environment

* open Studio and change the environment to the new one

* open the msapps files in the new environment, fix data connections and sources, and test the app

* assign correct users/groups and share out the app in the new environment
