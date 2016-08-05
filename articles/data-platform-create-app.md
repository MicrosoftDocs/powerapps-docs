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

# Create an app using the Common Data Model #
Create an app to manage data that's stored in the Common Data Model, using standard entities (which are built in), custom entities (which your organization creates), or both.

If you're unfamiliar with the Common Data Model, see [Understand entities](data-platform-intro.md).

PowerApps can create an app automatically based on an entity that you specify, or you can create an app from scratch that uses one or more entities that you specify.

In either case, you don't need to create a connection from PowerApps to the Common Data Model, as you do with external connections such as SharePoint, Dynamics CRM, and Salesforce. You need only specify the entities or entities that you want to show, manage, or both in the app.

**Prerequisites**

1. [Sign up](signup-for-powerapps.md) for PowerApps, [install](http://aka.ms/powerappsinstall) it, open it, and then sign in by providing the same credentials that you used to sign up.
1. Click or tap **New** on the **File** menu (near the left edge).

## Create an app automatically ##
1. Under **Create an app from your data**, click or tap **Phone layout** on the **Common Data Model** tile.

1. If prompted, click or tap **Create my database**.

1. Under **Choose an entity**, click or tap the entity that you want to use, and then click or tap **Connect**.

PowerApps automatically creates an app with three screens, as [Create an app from a set of data](get-started-create-from-data.md) describes.

## Create a app from scratch ##
1. Under **Create an app**, click or tap **Phone layout** on the **Blank app** tile.

1. In the right-hand pane, click or tap **Data sources** to open that tab, and then click or tap **Add data source**.

1. In the list of connections, click or tap **Common Data Model**, and then click or tap **Connect**.

1. If prompted, click or tap **Create my database**.

1. In the list of entities, select the check box for one or more entities that you want to use, and then click or tap **Connect**.

The entities or entities that you specified appear in the list of data sources, and you can build your app as [Create an app from scratch](get-started-create-from-blank.md) describes.
