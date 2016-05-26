<properties
	pageTitle="Share an app using tables | Microsoft PowerApps"
	description="Share an app in PowerApps using tables"
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

# Share an app using tables

You share an app using tables the same way you share an app that does not use tables, but there are some limitations in the private preview.

To learn more about app sharing, see [Share an app](share-app.md).

## Share with "can use" or "can use and share" permission

You can share an app using tables with others without any limitation when the permission is either o of the following:

* Can use
* Can use and share

You can share it with an individual or a group.

When you choose to share an app this way, everyone you shared the app with will be able to access and manage the data in the tables. They cannot manage the tables themselves.

## Share with "can edit" permission

You should only share "can edit" permission with others who are explicitly approved for the PowerApps data platform private preview. Otherwise, the people you shared the app with will only be able to edit the app but not the tables it uses.

You should **not** use groups in this case, because group sharing is not supported for tables in the data platform.

When you choose to share an app this way, all the approved users you shared the app with will be able to fully manage your workspace where all your tables are. They'll be able to modify all your tables, delete them, and create new ones.

## Share with an entire organization

This is not supported in the private preview.
