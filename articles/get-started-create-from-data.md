<properties
	pageTitle="Create an app from a set of data | Microsoft PowerApps"
	description="Create an app automatically based on an existing set of data that you specify and then customize the UI to better suit your needs."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="ankitsar"
	manager="darshand"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="01/06/2015"
   ms.author="anneta"/>

# Create an app from a set of data

Create an app automatically based on data that you specify, explore how the app works by default, and then customize it to better fit how you work.

**Prerequisites**

- Install [PowerApps for Windows](http://aka.ms/powerappsinstall) 
- Learn how to [configure a control](add-configure-controls.md).
- Download this [Excel file](https://pwrappssamples.blob.core.windows.net/samples/FlooringEstimates.xlsx), and save it in your OneDrive account.

**Note:** You can create an app based on a [SharePoint list](app-from-sharepoint.md), [Salesforce data](app-from-saleforce.md), or [a table in Dynamics CRM](app-from-dynamics.md) just as easily.

## Create the app ##

1. Open PowerApps, you may have to sign in if you are opening PowerApps for the first time.

1. In PowerApps, click or tap **New** on the **File** menu (near the left edge of the screen).

	![New option on the File menu](./media/get-started-create-from-data/file-new.png)

1. Under **Create an app from your data**, click or tap **Phone layout** on **OneDrive** tile. (Note: You can use OneDrive for Business, DropBox or Google Drive as well, the steps are similar to OneDrive.)

	![Option to create an app from data](./media/get-started-create-from-data/create-from-data.png)

1. If you have not connected to OneDrive before, you will be prompeted to create a new Connection. Click or tap **Connect**, and when prompted, provide your credentials.

	![Connect to OneDrive](./media/get-started-create-from-data/connect-onedrive.png)  

1. Under **Select an Excel file**, browse to excel file and then click or tap **flooringestimates.xlsx**.

	![FlooringEstimates Excel file](./media/get-started-create-from-data/choose-spreadsheet.png)  

1. Under **Select a table**, click or tap the **FlooringEstimates** table, and then click or tap **Connect**.  

	![Select FlooringEstimates table](./media/get-started-create-from-data/choose-table.png)  

PowerApps builds an app that contains three screens:

- **BrowseScreen1** shows a list of all items and some information about them  so that users can easily browse for the item they want.
- **DetailScreen1** shows all information about a single item.
- **EditScreen1** enables users to add an item or update information about an item.

When an app is built automatically, heuristics suggest the best layout and content based on the data. You might need to adjust the default settings to optimize the app for your needs.

## Customize the app ##

1. In the **Layout** tab of the **Quick tools** pane, click or tap an option that includes icons.

	![Layout option with icons](./media/get-started-create-from-data/change-layout.png)

	The layout of **BrowseScreen1** changes to reflect your selection.

	![BrowseScreen1 with new layout](./media/get-started-create-from-data/browse-layout.png)

	**Note:** If you open the **Layout** tab with **DetailScreen1** or **EditScreen1** showing, you can choose different options, which reflect the data on that screen.

1. Click or tap the first image in the list, and then from the **Options** pane set its value to **ImageURL**

	![BrowseScreen1 with new layout](./media/get-started-create-from-data/set-image-url.png)

1. Set the upper text box to **Name**, and set the lower text box to **Category**.

	The content of **BrowseScreen1** changes to reflect your selections.

	![BrowseScreen1 with new content](./media/get-started-create-from-data/browse-content.png)

	**Note:** By default, you can scroll through the list (called a gallery) by using a mousewheel or by swiping up and down. To show the scrollbar, [set the gallery's **ShowScrollbar** property](get-started-test-drive.md#configure-a-control) to **true**.

1. Click or tap the **DetailScreen1** from the screen thumbnails on the left side.

1. Click or tap on the ![View Form] on the screen canvas, to bring up the Options pane for the Form on the right.

1. Drag & Drop the Name field to the top position

1. Hide the Category field 

1. Set the Image control type to View Image

**Note**: You can customize the **EditScreen1** in similar fashion as the **DetailScreen1** to show the controls which you want the user to be able to use.

## Run the app ##
1. With **BrowseScreen1** showing, open Preview by pressing F5 (or by clicking or tapping the Preview icon near the upper-right corner).

	![Preview icon](./media/get-started-create-from-data/open-preview.png)

1. On **BrowseScreen1**, click or tap the arrow for a record to show details about that record.

	![Select an arrow on BrowseScreen1](./media/get-started-create-from-data/select-record.png)

1. On **DetailsScreen1**, click or tap the edit icon (in the upper-right corner) to edit the record.

	![Edit a record](./media/get-started-create-from-data/edit-record.png)

1. On **EditScreen1**, change the information in one or more fields, and then select the checkmark in the upper-right corner to save your changes.

	![Save changes on EditScreen1](./media/get-started-create-from-data/save-record.png)

## Next steps ##

- You can further customize your app by performing similar tasks to those that [Create an app from scratch](get-started-create-from-blank.md) describes.
- [Save and share your app](get-started-test-drive.md#save-and-share-your-app) with other people.
