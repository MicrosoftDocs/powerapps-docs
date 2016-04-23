<properties
	pageTitle="Create an app using tables | Microsoft PowerApps"
	description="Create an app using PowerApps data platform"
	services="powerapps"
	documentationCenter="na"
	authors="guangyang"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/19/2016"
   ms.author="guayan"/>

# Create an app using tables

PowerApps data platform makes it really easy to store data using both standard tables provided by the platform and custom tables created by your organization. After having some tables in PowerApps, using them to create an app is really simple.

There are two ways to create an app using tables:

1. Create from data
2. Create from scratch

The important thing to know is that the PowerApps data platform will be enabled automatically as a data connection, tables then can be added as data sources to PowerApps. This is the same experience as external connections like SharePoint Online, Dynamics CRM or Salesforce.

## Create from data

This the simplest way to create an app using tables in just a few minutes. Following are the steps:

1. Open PowerApps Studio and login with your organizational account.
2. Click **New** and then select **Start from your data**.
3. A list of connections will show up for you to choose from. Select **PowerApps data platform** and click **Connect**. Notice that this is available to you automatically, no additional login is needed.
4. From the list of tables, select the one you want to use. Then click **Connect** again.

After this, the standard "create from data" experience will start. For more information, please refer to [Create an app from a set of data](#get-started-create-from-data.md).

## Create from scratch

Sometimes, you may want to start from scratch which will give you the most flexibility. Following are the steps:

1. Open PowerApps Studio and login with your organizational account.
2. Click **New** and then select **Start from scratch**. This will create an empty app.
3. Click **Content** and then **Data sources** in the ribbon to open the data sources pane on the right.
4. Click **Insert your data** to add a data source.
5. A list of connections will show up for you to choose from. Select **PowerApps data platform** and click **Connect**. Notice that this is available to you automatically, no additional login is needed.
6. From the list of tables, select the one you want to use. Then click **Connect** again.

After this, a data source pointing to the selected table will be added to the app. You then can use it via controls and formulas.

For more information about in general how to create an app from scratch, please refer to [Create an app from scratch](#get-started-create-from-blank.md).