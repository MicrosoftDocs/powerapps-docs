<properties
	pageTitle="Open entity data in Excel | Microsoft PowerApps"
	description="Open entity data in Excel for interactive viewing and editing"
	services="powerapps"
	documentationCenter="na"
	authors="chrisgarty"
	manager="robinarh"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="08/19/2016"
   ms.author="cgarty"/>

# Open entity data in Excel #

[AZURE.VIDEO nb:cid:UUID:3d731aa8-6eb0-4d36-a9e5-d28bf44b28a0]

Opening entity data in Excel allows for quick and easy viewing and editing of data facilitated by the PowerApps Excel Add-in. The PowerApps Excel Add-in requires Excel 2016.

**Note**: If your Azure Active Directory (AAD) tenant is configured to use Active Directory Federation Services (ADFS) then you need to have to ensure that the May 2016 update has been applied so the Excel Add-in can facilitate sign-in correctly.

## Open entity data in Excel

1. In your web browser, open [powerapps.com](https://web.powerapps.com) and sign in.
1. In the left navigation pane, click or tap **Entities**. All of the entities will be shown.
1. Click the actions menu **"..."** to the right of the desired Entity
1. Click **Open in Excel** and open the workbook that is provided. The generated workbook has binding information for the desired entity, a pointer to your environment, and a pointer to the PowerApps Excel Add-in.  
1. In Excel, click **Enable editing** to allow the PowerApps Excel Add-in to run. The Excel Add-in will run in a task pane on the right side of the workbook.
1. If this is the first time running the Add-in, click **Trust this Add-in** to allow the PowerApps Excel Add-in to run.
1. If needed, click **Sign in** and sign in with the same credentials used on [powerapps.com](https://web.powerapps.com). The Excel Add-in will use a previous sign-in context and automatically sign-in if possible, so verify the user name in the top right of the Excel Add-in.
1. The Excel Add-in will automatically read the data for the selected entity. Note that there will be no data in the workbook until the Excel Add-in reads it in.

## View and refresh entity data in Excel ##
Once entity data is read into the workbook by the Excel Add-in, it can be refreshed at any time by clicking the **Refresh** button in the Excel Add-in.


## Edit entity data in Excel ##
Entity data can be changed as needed and then published back by clicking the **Publish** button in the Excel Add-in.

To edit a record, select the desired cell and make changes to the cell value.

To add a new record, either:

1. Put focus in the table and click the **New** button in the Excel Add-in.
1. Put focus in the last row in the table and press the **tab** key until the cursor moves out of the last column and into the next row, creating an additional table row.
1. Put focus in the row immediately below the table and start entering data. The table will grow to include that row when focus moves out of that cell.

To delete a record, either:

1. Right-click the row number beside the table and click **Delete**
1. Right-click in the desired table row and click **Delete > Table Rows**


## Add or remove columns ##
The set of columns automatically added into the workbook can be adjusted using the designer:

1. Enable the data source designer of the Excel Add-in by clicking the **Options** button (gear symbol) and checking **Enable design**.
1. Click the **Design** button in the Excel Add-in. All the data sources are listed.
1. Next to the data source, click the **Edit** pencil button.
1. Adjust the list of **Selected fields** as needed:
	- Add a field from the list of **Available fields** to **Selected fields** by clicking on the field and clicking **Add**, or by double-clicking the field.
	- Remove a field from the list of **Selected fields** by clicking on the field and clicking **Remove**, or by double-clicking the field.
	- Change the order of fields by clicking on the field in the list of **Selected fields** and clicking **Up** or **Down**.
1. Apply the changes to the data source by clicking **Update** and then click **Done** to exit the designer. If a field (column) was added, click **Refresh** to pull in a refreshed set of data.

## Troubleshooting ##
There are a few troublesome situations that can be resolved with some simple steps:

1. If a "Forbidden" message appears while metadata is being loaded by the Excel Add-in, then the account signed into the Excel Add-in doesn't have permission to use the targeted Common Data Model database. To resolve this situation, verify that the correct user name is shown at the top right of the Excel Add-in. If needed, click the user name at the top right of the Excel Add-in, sign out, and sign back in.
1. If a blank web page opens during the sign in process, then the account requires ADFS but the version of Excel running the Add-in is not recent enough to support loading a sign-in dialog. Update the version of Excel being used, if needed by [moving from the deferred channel to the current channel](https://technet.microsoft.com/library/mt455210.aspx) using the [Office deployment tool](https://technet.microsoft.com/library/jj219422.aspx).

If you encounter a troublesome situation not detailed here, then contact us via the [support pages](https://powerapps.microsoft.com/support/).

## Next steps ##
- [Manage fields in an entity](data-platform-manage-fields.md)
- [Define relationships between entities](data-platform-entity-lookup.md)
- [Generate an app by using a Common Data Service database](data-platform-create-app.md)
