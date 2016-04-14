<properties
	pageTitle="Create an app from Excel data | Microsoft PowerApps"
	description="Create an app automatically based on an Excel file in the cloud, customize the app, and then explore how it works."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="sarafankit"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/12/2016"
   ms.author="ankitsar"/>

# Create an app from Excel data #
Create an app automatically based on an Excel file in the cloud, customize the app, and then explore how it works.

**Prerequisites**

- [Sign up](signup-for-powerapps.md) for PowerApps, [install](http://aka.ms/powerappsinstall) it, open it, and then sign in by providing the same credentials that you used to sign up.

- A Box, Dropbox, Google Drive, OneDrive, or OneDrive for Business account into which you've saved [this Excel file](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx), which contains sample data for this tutorial. The tutorial shows how to use OneDrive, but the process is similar for the other types of accounts.

**Note:** You can just as easily create an app based on a [SharePoint](app-from-sharepoint.md) list, [Salesforce](app-from-salesforce.md) data, a table in [Dynamics CRM](app-from-dynamics.md), or another [data source](add-and-manage-connections.md).

## Create the app ##
1. In PowerApps, select **New** (near the left edge of the screen).

	![New option on the File menu](./media/get-started-create-from-data/file-new.png)

1. Under **Create an app from your data**, select **Phone layout** on the **OneDrive** tile.

	![Option to create an app from data](./media/get-started-create-from-data/create-from-data.png)

1. If you haven't connected to OneDrive before, select **Connect** when prompted, and then provide your credentials.

	![Connect to OneDrive](./media/get-started-create-from-data/connect-onedrive.png)  

1. Under **Select an Excel file**, browse to **FlooringEstimates.xlsx**, and then select it.

	![FlooringEstimates Excel file](./media/get-started-create-from-data/choose-spreadsheet.png)  

1. Under **Select a table**, select **FlooringEstimates** , and then select **Connect**.  

	![Select FlooringEstimates table](./media/get-started-create-from-data/choose-table.png)

PowerApps builds an app that has three screens:

- **BrowseScreen1** shows a list of all items and some information about them so that users can easily browse for the item they want.
- **DetailScreen1** shows all information about a single item.
- **EditScreen1** provides controls for adding an item or updating information about an item.

## Customize the app ##
When an app is built automatically, heuristics suggest the best layout and content based on the data. You might need to change the app for your needs.

1. If you haven't used PowerApps before, take the intro tour by reading each description before selecting **Next** (and then selecting **Done**), or select **Skip**.

1. On the **Options** pane, select the **Layout** tab, and then select an option that includes images.

	![Layout option with icons](./media/get-started-create-from-data/change-layout.png)

	The layout of **BrowseScreen1** changes to reflect your selection.

	![BrowseScreen1 with new layout](./media/get-started-create-from-data/browse-layout.png)

	**Note:** If you open the **Layout** tab with **DetailScreen1** or **EditScreen1** showing, you can choose different options, which reflect the data on that screen.

1. In the list, select the upper text box for the first item.

	![Select first text box](./media/get-started-create-from-data/select-gallery-textbox.png)

1. In the **Options** pane, select **Name** in the top list.

    ![Set first text box](./media/get-started-create-from-data/set-gallery-textbox.png)

1. In the design workspace, select the lower text box for the first item.

1. In the **Options** pane, select **Category** in the bottom list.

	**BrowseScreen1** changes to show your selections.

	![BrowseScreen1 with new content](./media/get-started-create-from-data/browse-content.png)

	**Note:** By default, you can scroll through the list (called a gallery) by using a mousewheel or by swiping up and down. To show the scrollbar, [set the gallery's **ShowScrollbar** property](add-configure-controls.md) to **true**.

1. In the list of thumbnails, select **DetailScreen1**.

    ![DetailScreen 1 Thumbnail](./media/get-started-create-from-data/detail-screen-thumbnail.png)

1. Select **Name**, and then drag the field's title bar above **Category**.

    ![Select a card](./media/get-started-create-from-data/select-card.png)

    ![Drop a card](./media/get-started-create-from-data/card-on-top.png)

1. In the list of thumbnails, select **EditScreen1**.

    ![EditScreen 1 Thumbnail](./media/get-started-create-from-data/edit-screen-thumbnail.png)

1. In the **Options** pane, select the card selector for **Overview**.

    ![Expand Card Selector](./media/get-started-create-from-data/card-selector.png)

1. Select the **Edit text card** option with multiple lines.

    ![Multi-line Card](./media/get-started-create-from-data/select-multiline-card.png)

## Run the app ##
As you customize the app, you can test your changes by running the app in **Preview** mode.

1. In the list of thumbnails, select **BrowseScreen1**, and then open Preview by pressing **F5** (or by selecting the Preview icon near the upper-right corner).

	![Preview icon](./media/get-started-create-from-data/open-preview.png)

1. On **BrowseScreen1**, select the arrow for a record to show details about that record.

	![Select an arrow on BrowseScreen1](./media/get-started-create-from-data/select-record.png)

1. On **DetailsScreen1**, select the edit icon (in the upper-right corner) to edit the record.

	![Edit a record](./media/get-started-create-from-data/edit-record.png)

1. On **EditScreen1**, change the information in one or more fields, and then select the check mark in the upper-right corner to save your changes.

	![Save changes on EditScreen1](./media/get-started-create-from-data/save-record.png)

## Next steps ##
- Press Ctrl-S to save your app so that you can run it from other devices.
- Customize your app further, as [Create an app from scratch](get-started-create-from-blank.md) describes.
- [Share the app](share-app.md) so that other people can run it.
