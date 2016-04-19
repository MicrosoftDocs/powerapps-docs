<properties
	pageTitle="Delete table and clear data | Microsoft PowerApps"
	description="Delete a table from PowerApps data platform and clear all data"
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

# Delete table

You can delete a custom table only but not any standard table. To delete a table, following are the steps:

1. Login to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab on the left hand navigation pane. Then Click **Tables** to navigate to the table management page.
3. Find the table you need. You can search for it in the search bar on the top.
4. Click the table to navigate to the fields page where it will show all the fields of the table.
5. Click the **Delete** button on the top.

Notice that

1. When deleting a table, both the table definition and the data stored in the table will be deleted.
2. If there is any app using the table, they may break.
3. If the table has some lookup fields (hence relationships to other tables), you may not be able to delete the table directly, you'll need to delete the other tables it relates to first.