<properties
	pageTitle="Import or export data | Microsoft Common Data Model"
	description="Import or export an entity from the Common Data Model"
	services="powerapps"
	documentationCenter="na"
	authors="RobinARH"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="08/03/2016"
   ms.author="robinr"/>

# Import or export data from the Common Data Model #
You can move data into or out of the Microsoft Common Data model in one of two ways:

- If you want to do a one-time bulk import or export of data, you can use Microsoft Excel, for multiple entities.

- If you want an ongoing import or export of data for a single entity to another service, such as Dynamics CRM or Salesforce, or even to an Excel file. To set up ongoing import or export, you can use [Microsoft Flow](https://flow.microsoft.com).

## One-time export a table from PowerApps to a Microsoft Excel file ##

You can do a one-time data export from a standard entities or a custom entities, and you can export data from more than one table at a time. If you export data from more than one table, each table is exported into its own Microsoft Excel file.

1. In [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Tables**.
1. Next to **New Table**, click or tap the ellipsis, and then click or tap **Export data**.
1. Select the entities from which you want to export data, and then click or tap **Export**.
1. When **Export Completed** appears, download the data to a file by clicking or tapping **Download exported data**.

## Use Microsoft Flow to set up ongoing import or export ##

You can set up ongoing import or export for a single standard entity or custom entity at a time. Some possible places you can connect to include:

- Microsoft Dynamics CRM
- Salesforce.com
- Microsoft Excel files stored in any cloud file provider
- A Microsoft SQL database, both in the cloud and on-premises
- A custom API that you define to connect to your own systems

Today, when you use Microsoft Flow to import data or export data, it is not a full syncronziation service. Whenver an object is added to one service, it will be imported into the other system. However, that means if an object is deleted from one system it will not be deleted in the other system.

How to set up the import depends on if a template already exists for the object you want to import. If a template exists, you can set up it up to copy data from  one system to another. [Go here to read more about how to use a template to import data into the Common Data Model](https://flow.microsoft.com/documentation/get-started-logic-template/). On the other hand, if no such template exists, you'll need to create a flow from scratch that can use the data model. [Go here to read more about how to create a flow from scratch](https://flow.microsoft.com/documentation/get-started-logic-flow/).
