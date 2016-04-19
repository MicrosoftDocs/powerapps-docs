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

You can share an app using tables in a similar fashion as of an app not using tables. Having said that, there are some limitations during private preview.

To learn more about app sharing, please refer to [Share an app](#share-app.md).

## Share with "can use" or "can use and share" permission

You can share an app using tables with others without any limitation when the permission is

1. Can use
2. Can use and share

You can share it with an individual or a group.

When choosing to share the app this way, it means that everyone you shared the app with will be able to access and manage the data in the tables. They cannot manage the tables themselves.

## Share with "can edit" permission

You should only share "can edit" permission with other colleges who are explicitly whitelisted for PowerApps data platform private preview. Otherwise, the people you shared the app with will only be able to edit the app but not the tables it uses.

You should NOT use groups in this case since group sharing is not supported for tables in data platform.

When choosing to share the app this way, it means that all the whitelisted users you shared the app with will be able to fully manage your workspace where all your tables are in. They'll be able to modify all your tables, delete them and create new ones.

## Share with entire organization

This is not supported for now.