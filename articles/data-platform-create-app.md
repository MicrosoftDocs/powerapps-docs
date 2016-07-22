<properties
	pageTitle="Create an app using Common Data Model | Microsoft Common Data Model"
	description="Create an app using Microsoft Common Data Model"
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
   ms.date="07/21/2016"
   ms.author="karthikb"/>

# Create an app using Microsoft Common Data Model

Microsoft Common Data Model makes it easy to store data using both standard entities provided by the platform and custom entities created by your organization. After you have the entities you need, using them to create an app is really simple.

There are two ways to create an app using entities in the Common Data Model:

* Create an app from data
* Create an app from scratch

Microsoft Common Data Model is enabled automatically as a data connection so that entities can be added as data sources to PowerApps. This is the same experience as external connections such as Microsoft SharePoint Online, Microsoft Dynamics CRM, or Salesforce.

## Create app from data

The simplest way to create an app using tables takes just a few minutes:

1. Open PowerApps Studio and sign in with your organizational account.
2. Click **New**
3. Under *Create an app from your data*, select **Common data model** and then click the app layout. Common data model is available to you automatically. No additional sign-in is needed.
4. If it is the first time you are using the Common data model, you may need to click on **Create my database**
4. Select the entity you want to use. Click **Connect**.

The standard "create from data" experience will start. For more information, see [Create an app from a set of data](#get-started-create-from-data.md).

## Create app from scratch

Starting from scratch gives you the most flexibility:

1. Open PowerApps Studio and sign in with your organizational account.
2. Click **New** and then select **Blank app** under *Create an app*. This will create an empty app.
3. Click **Content** and then **Data sources** on the ribbon to open the data sources pane on the right.
4. Click **Add data source**.
5. A list of connections appears for you to choose from. Select **Common data model** and then click **Connect**. The platform is available to you automatically. No additional sign-in is needed.
4. If it is the first time you are using the Common data model, you may need to click on **Create my database**
6. In the list of entities, select the one or more entities you want to use. Click **Connect** again.

A data source pointing to the selected table will be added to the app. You can then use it with controls and formulas.

For more information about in general how to create an app from scratch, see [Create an app from scratch](#get-started-create-from-blank.md).
