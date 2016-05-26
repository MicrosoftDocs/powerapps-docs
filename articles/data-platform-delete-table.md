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

You can delete custom tables but not standard tables. To delete a table:

1. Sign in to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab in the left navigation pane. Click **Tables** to navigate to the table management page.
3. Find the table you need. You can search for it in the search bar at the top.
4. Click the table to navigate to the fields page which will show all the fields of the table.
5. Click the **Delete** button at the top.

**Notes**

* When you delete a table, both the table definition and the data stored in the table will be deleted.
* Deleting a table might break any apps using the table.
* If the table has lookup fields (relationships to other tables), you might not be able to delete the table directly. You need to delete the other tables it relates to first.
