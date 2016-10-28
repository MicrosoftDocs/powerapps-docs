<properties
	pageTitle="Create an app from scratch using a Common Data Service database | Microsoft PowerApps"
	description="Create an app to add, update, and delete records."
	services="powerapps"
	documentationCenter="na"
	authors="robinarh"
	manager="robinr"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/28/2016"
   ms.author="robinr"/>

# Create an app from scratch using a Common Data Service database
Build an app to manage data that's stored in the Common Data Service, using standard entities (which are built in), custom entities (which your organization creates), or both.

When you build an app from the Common Data Service, you don't need to create a connection from Microsoft PowerApps, as you do with data sources such as SharePoint, Dynamics 365, or Salesforce. You only need to specify the entities that you want to show, manage, or use for both activities in the app.

[AZURE.VIDEO nb:cid:UUID:5db63c4d-6aeb-45c5-9609-8f4bbdd37bc6]

1. Create a Common Data Service database. For more information, see [Create a Common Data Service database](create-cdm-database.md).
1. On [powerapps.com](https://web.powerapps.com), in the left navigation pane, click or tap **New app**.
1. In the dialog box that appears, click or tap **PowerApps Studio for web**. (You can also click or tap **PowerApps Studio for Windows**, and then follow the instructions to install PowerApps Studio for Windows. Although the instructions that follow use PowerApps Studio for web, the instructions for the Microsoft Windows app are similar.)
1. Under **Start with a blank canvas or template**, click or tap **Phone layout** on the **Blank app** tile.
1. If prompted, click or tap **Skip** to skip the tutorial.
1. Click or tap the **Content** tab.
1. Click or tap **Data sources**.
1. In the rightmost pane, click or tap **Add data source**.
1. Click or tap the Common Data Service that you want to use.
1. In the list of entities, select the check box for one or more entities that you want to use, and then click or tap **Connect**.

The entities that you specified appear in the list of data sources, and you can build your app as [Create an app from scratch](get-started-create-from-blank.md) describes.
