<properties
	pageTitle="Share an app that uses an entity | Microsoft PowerApps"
	description="Share an app that uses an entity."
	services="powerapps"
	documentationCenter="na"
	authors="robinarh"
	manager="robinarh"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/18/2016"
   ms.author="robinr"/>

# Share an app that uses an entity
You share an app that uses an entity in the same way as you [share any other app](share-app.md), but with some restrictions.

- If you share the app with the **Can use** or **Can use and share** permission, users and groups can display and manage all data in the entity or entities that the app uses. However, those users and groups can't modify the schemas of those entities or delete them.

- If you share the app with the **Can edit** permission, users and groups can fully manage your database. They can modify and even delete your entities, in addition to creating, modifying, and deleting their own.

	**Important**: You should grant **Can edit** permission only to other authors of the app.

- You can't share an app with an entire organization if the app uses one or more entities.


