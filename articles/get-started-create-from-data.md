<properties
	pageTitle="Create an app from a set of data | Microsoft PowerApps"
	description="Create an app automatically based on an existing set of data that you specify and then customize the UI to better suit your needs."
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
   ms.date="01/06/2015"
   ms.author="anneta"/>

# Create an app from a set of data

Create an app automatically based on data that you specify, customize it to better fit how you work and then explore how the app works.

**Prerequisites**

- Install [PowerApps for Windows](http://aka.ms/powerappsinstall).
- Download this [Excel file]((./media/get-started-create-from-data/FlooringEstimates.xlsx), and save it in your OneDrive account.


**Note:** You can create an app based on a [SharePoint list](app-from-sharepoint.md), [Salesforce data](app-from-saleforce.md), [a table in Dynamics CRM](app-from-dynamics.md), or other [data sources](add-and-manage-connections.md)  just as easily.

## Create the app ##

1. Open PowerApps, you may have to sign in if you are opening PowerApps for the first time.

1. In PowerApps, select **New** (near the left edge of the screen).

	![New option on the File menu](./media/get-started-create-from-data/file-new.png)

1. Under **Create an app from your data**, select **Phone layout** on **OneDrive** tile. (Note: You can use OneDrive for Business, DropBox, Box, or Google Drive as well, the steps are similar to OneDrive.)

	![Option to create an app from data](./media/get-started-create-from-data/create-from-data.png)

1. If you have not connected to OneDrive before, you will be prompted to create a Connection. Select **Connect**, and when prompted, provide your credentials.

	![Connect to OneDrive](./media/get-started-create-from-data/connect-onedrive.png)  

1. Under **Select an Excel file**, browse to **FlooringEstimates.xlsx** excel file, and then select it.

	![FlooringEstimates Excel file](./media/get-started-create-from-data/choose-spreadsheet.png)  

1. Under **Select a table**, select the **FlooringEstimates** table, and then select **Connect**.  

	![Select FlooringEstimates table](./media/get-started-create-from-data/choose-table.png)  

PowerApps builds an app that has three screens:

- **BrowseScreen1** shows a list of all items and some information about them so that users can easily browse for the item they want.
- **DetailScreen1** shows all information about a single item.
- **EditScreen1** is used to add an item or update information about an item.

## Customize the app ##
When an app is built automatically, heuristics suggest the best layout and content based on the data. You might need to change the app for your needs.

1. Select the **Layout** tab on the **Options** pane, and then select an option that includes images.

	![Layout option with icons](./media/get-started-create-from-data/change-layout.png)

	The layout of **BrowseScreen1** changes to reflect your selection.

	![BrowseScreen1 with new layout](./media/get-started-create-from-data/browse-layout.png)

	**Note:** If you open the **Layout** tab with **DetailScreen1** or **EditScreen1** showing, you can choose different options, which reflect the data on that screen.

1. Select the first text box in the list, and then from the **Options** pane set its value to **Name**

	![Select first text box](./media/get-started-create-from-data/select-gallery-textbox.png)
    
    On the Options pane:
    
    ![Set first text box](./media/get-started-create-from-data/set-gallery-textbox.png)

1. Set the lower text box to **Category**.

	**BrowseScreen1** changes to show your selections.

	![BrowseScreen1 with new content](./media/get-started-create-from-data/browse-content.png)

	**Note:** By default, you can scroll through the list (called a gallery) by using a mousewheel or by swiping up and down. To show the scrollbar, [set the gallery's **ShowScrollbar** property](get-started-test-drive.md#configure-a-control) to **true**.

1. Select the **DetailScreen1** from the screen thumbnails on the left side.

    ![DetailScreen 1 Thumbnail](./media/get-started-create-from-data/detail-screen-thumbnail.png) 

1. Select the **Name** field on the screen, and then using the field title bar **Drag & Drop** it to the top position on the form.
    
    ![Select a card](./media/get-started-create-from-data/select-card.png)
    
    ![Drop a card](./media/get-started-create-from-data/card-on-top.png)
     
1. Select the **EditScreen1** from the screen thumbnails on the left side.

    ![EditScreen 1 Thumbnail](./media/get-started-create-from-data/edit-screen-thumbnail.png)

1. Select the **Overview** field on the screen, and expand the card selector from the **Options** pane on the right side.

    ![Expand Card Selector](./media/get-started-create-from-data/card-selector.png)

1. Select the **Multi-line edit text card** to change the **Overview** field to a multi-line edit text box.
    
    ![Multi-line Card](./media/get-started-create-from-data/select-multiline-card.png)

## Run the app ##
As you are changing the app for your needs, you can try the app by running it in **Preview** mode 

1. Select **BrowseScreen1** from the screen thumbnails, and open Preview by pressing **F5** (or by selecting the Preview icon near the upper-right corner).

	![Preview icon](./media/get-started-create-from-data/open-preview.png)

1. On **BrowseScreen1**, Select the arrow for a record to show details about that record.

	![Select an arrow on BrowseScreen1](./media/get-started-create-from-data/select-record.png)

1. On **DetailsScreen1**, Select the edit icon (in the upper-right corner) to edit the record.

	![Edit a record](./media/get-started-create-from-data/edit-record.png)

1. On **EditScreen1**, change the information in one or more fields, and then select the check mark in the upper-right corner to save your changes.

	![Save changes on EditScreen1](./media/get-started-create-from-data/save-record.png)

## Next steps ##
- [Save your app](save-an-app.md) to use it from your mobile phone or tablet, and [share it]((share-app.md) with other people.
- You can further customize your app by performing similar tasks to those that [create an app from scratch](get-started-create-from-blank.md) describes.