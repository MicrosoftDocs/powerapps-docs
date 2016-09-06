<properties
	pageTitle="Create an app using the Common Data Model | Microsoft Common Data Model"
	description="Create an app to add, update, and delete records in the Common Data Model"
	services="powerapps"
	documentationCenter="na"
	authors="karthik-1"
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

# Build an app from scratch using the Common Data Model #
Build an app to manage data that's stored in the Common Data Model, using standard entities (which are built in), custom entities (which your organization creates), or both.

If you're unfamiliar with the Common Data Model, see [Understand entities](data-platform-intro.md).

When you build an app from the Common Data Model, you don't need to create a connection from PowerApps, as you do with data sources such as SharePoint, Dynamics CRM, and Salesforce. You need only specify the entities or entities that you want to show, manage, or both in the app.

[AZURE.VIDEO nb:cid:UUID:5e58b2b8-44a0-467f-b6ec-58dee9fd925a]

1. [Sign up for PowerApps](signup-for-powerapps.md), and then do *either* of the following:

	- [Open PowerApps](https://create.powerapps.com/api/start) in a browser.
	- [Install PowerApps](http://aka.ms/powerappsinstall) from the Windows Store. Open PowerApps, sign in, and then click or tap **New** on the **File** menu (along the left edge).

		![New option on the File menu](./media/data-platform-create-app-scratch/file-new.png)

1. Under **Create an app**, click or tap **Phone layout** on the **Blank app** tile.

	![Create from blank](./media/data-platform-create-app-scratch/create-from-blank.png)

1. If prompted and you're not familiar with PowerApps, identify key areas of the app by taking the intro tour (or click or tap **Skip**).

	![Opening screen of the quick tour](./media/data-platform-create-app-scratch/quick-tour.png)

	**Note**: You can always take the tour later by clicking or tapping the question-mark icon near the upper-right corner and then clicking or tapping **Take the intro tour**.

1. In the right-hand pane, click or tap **Data sources** to open that tab, and then click or tap **Add data source**.

1. In the list of connections, click or tap **Common Data Model**, and then click or tap **Connect**.

1. If prompted, click or tap **Create my database**.

1. In the list of entities, select the check box for one or more entities that you want to use, and then click or tap **Connect**.

The entities or entities that you specified appear in the list of data sources, and you can build your app as [Create an app from scratch](get-started-create-from-blank.md) describes.
