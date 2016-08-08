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
You can move data into or out of the Common Data Model in one of two ways:

- If you want to do a one-time bulk import or export of data, you can use Microsoft Excel, for multiple entities.

- If you want an ongoing import or export of data for a single entity to another service, such as Dynamics CRM or Salesforce, or even to an Excel file. To set up ongoing import or export, you can use [Microsoft Flow](https://flow.microsoft.com).

## Import or export data once ##

### Import data from Excel ###
1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Entities**.
1. Next to **New entity**, click or tap the ellipsis, and then click or tap **Import data**.
1. Select the entity that you want to import data into, and then click or tap **Next**.
1. Click or tap **Search**, and select the file that you want to import data from.
1. If the **Mapping Status** is not **Match** and a green checkmark, then you will need to specify the mapping between the entity fields and the columns in the Excel file. To map the columns:
    2. Click or tap **Show Mapping**.
    2. For each entity field, select the matching column in the Excel file.
    2. Click or tap **Save changes**.
1. Click **Import**.

### Export data to Excel ###
You can do a one-time data export from a standard entity or a custom entity, and you can export data from more than one entity at a time. If you export data from more than one entity, each entity is exported into its own Microsoft Excel file.

1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Entities**.
1. Next to **New entity**, click or tap the ellipsis, and then click or tap **Export data**.
1.	Select the entities that you want to export data from, and then click or tap **Export to Excel**.
1.	When **Export Completed** appears, click or tap **Download exported data** to download the data.

## Use Microsoft Flow to set up ongoing import or export ##
You can set up ongoing import or export for a single standard entity or custom entity at a time. Some possible places you can connect to include:

- Microsoft Dynamics CRM
- Salesforce.com
- Microsoft Excel files stored in any cloud file provider
- A Microsoft SQL database, both in the cloud and on-premises
- A custom API that you define to connect to your own systems

Today, when you use Microsoft Flow to import data or export data, it is not a full synchronziation service. Whenever an object is added to one service, it will be imported into the other system. However, that means if an object is deleted from one system it will not be deleted in the other system.

How to set up the import depends on if a template already exists for the object you want to import. If a template exists, you can set it up to copy data from one system to another. [Go here to read more about how to use a template to import data into the Common Data Model](https://flow.microsoft.com/documentation/get-started-logic-template/). On the other hand, if no such template exists, you'll need to create a flow from scratch that can use the data model. [Go here to read more about how to create a flow from scratch](https://flow.microsoft.com/documentation/get-started-logic-flow/).
