<properties
	pageTitle="Share an app that uses an entity | Microsoft Common Data Model"
	description="In PowerApps, share an app that uses an entity."
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
   ms.date="08/04/2016"
   ms.author="karthikb"/>

# Share an app that uses an entity #
In PowerApps, share an app that uses an entity in the same way as you [share any other app](share-app.md), but this release of the Common Data Model has some restrictions.

- If you share the app with the **Can use** or **Can use and share** permission, users and groups can display and manage all data in the entity or entities that the app uses. However, those users and groups can't modify the schemas of those entities or delete them.

- If you share the app with **Can edit** permission, users and groups can fully manage your database. They can modify and even delete your entities, in addition to creating, modifying, and deleting their own.

	**Important**: You should grant **Can edit** permission only to other authors of the app.

- In this release of the Common Data Model, you can't share an app with an entire organization if the app uses one or more entities.

If you're unfamiliar with the Common Data Model, see [Understand entities](data-platform-intro.md).
