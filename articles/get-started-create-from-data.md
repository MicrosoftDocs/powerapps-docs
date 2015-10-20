<properties
	pageTitle="Create an app from data in PowerApps"
	description=""
	services="powerapps"
	authors="AFTOwen"
 />

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/20/2015"
   ms.author="anneta"/>

# Create an app from data
Create an app automatically based on data that you specify, explore how the app works by default, and then customize the app to better fit how you work.

[What is PowerApps?](http://www.kratosapps.com/tutorials)

**Prerequisites**

- Sign up for and install [PowerApps]()
- A set of data in the cloud, such as in DropBox or OneDrive
- Familiarity with how to [configure a control](get-started-test-drive.md#configure-a-control) in PowerApps

## Connect to data ##
You can create an app based on data from any of several kinds of sources. For this tutorial, the data source is an Excel file in Dropbox. The file, named **eventsignup.xls**, contains this data [formatted as a table](https://support.office.com/en-us/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370) and named **Schedule**.

![Source data in Excel](./media/get-started-create-from-data/excel-source.jpg)

1. Sign in to PowerApps, and then click **New** in the left navigation bar.

	![The New option in the left navigation bar](./media/get-started-create-from-data/file-new.jpg)

1. Leave the default option to create a phone app.

	![The option buttons for creating a tablet or phone app](./media/get-started-create-from-data/phone-app.jpg)

1. Under **Start from Data**, click **Get started**.

	![Option to create an app from data](./media/get-started-create-from-data/create-from-data.jpg)

1. If you don't already have a connection to a data source, click **Available Connections**, click an option in the list that appears, and then click **Add Connection**.

	![Create connection to Dropbox](./media/get-started-create-from-data/dropbox-connection.jpg)

1. Click a data set, and then click **Connect**.

	![Specify an Excel file in a Dropbox account](./media/get-started-create-from-data/choose-excel-file.jpg)

1. Click a table, and then click **Connect**.

	![Specify a table in an Excel file](./media/get-started-create-from-data/choose-table.jpg)

An app is created from the data that you specified.

## Explore the app ##

When the app is created, it appears in the default workspace, where you can customize the app to better fit your needs. Before you make changes, you'll explore how the app works in **Preview**. By running an app in **Preview**, you can completely test an app before you share it with others.

1. Press F5 to open **Preview**.

	![The default BrowseScreen](./media/get-started-create-from-data/default-browsescreen.jpg)

	The first screen, named **BrowseScreen**, shows which people are signed up for each shift in a schedule. You can sort the data, add an item, and search for an item by using the elements near the top of the screen.

1. Click the arrow for the first item to show details about that item.

	![Navigate from BrowseScreen to DetailScreen](./media/get-started-create-from-data/right-arrow.jpg)

	The **DetailScreen** appears, showing all data for the item you specified. You can delete or update that item by using the elements near the top of the screen.

	![The default DetailScreen](./media/get-started-create-from-data/default-detailscreen.jpg)

1. Click the pencil icon to update the item.

	![The pencil icon](./media/get-started-create-from-data/pencil-icon.jpg)

	The **EditScreen** appears, with text boxes so that you can change the item, a cancel icon in the upper-left corner, and a save icon in the upper-right corner.

	![The default EditScreen](./media/get-started-create-from-data/default-editscreen.jpg)

	**Note:** If you click the plus sign on the **BrowseScreen**, the **EditScreen** appears with all the text boxes blank so that you can create an item.

1. Replace either or both of the names with whatever names you want, and then click the save icon.

	![Updating an item](./media/get-started-create-from-data/replace-name.jpg)

	The updated data appears in the app and the source.

1. Press Esc to return to the default workspace, in which you can customize the app.

## Change the layout, the content, and the theme ##
You can customize the default app by adding or deleting a screen, changing a property of a screen, and changing a specific element on a screen.

1. Near the lower-right corner of the screen, click **Quick start**.

	![Button to open Quick Start pane](./media/get-started-create-from-data/open-quick-start.jpg)

	The Quick Start pane opens and shows the **Layout** tab by default.

	![Layout tab of the Quick Start pane](./media/get-started-create-from-data/qs-layout.jpg)

1. With **BrowseScreen1** showing, choose a different layout, such as **List4**.

	**BrowseScreen1** shows the day and staff information but not the time information from the shift schedule.

	![The BrowseScreen set to List4 layout, default](./media/get-started-create-from-data/list4-default.jpg)

1. In the Quick Start pane, click **Content** to open the **Content** tab.

	![Content tab of the Quick Start pane](./media/get-started-create-from-data/qs-content.jpg)

1. In the **Heading2** list, click **StartDay**. and, in the **Subtitle2** list, click **StartTime**.

	**StartDay** and **StartTime** appear near the left edge of the screen, and **Staff1** appears near the right edge.

	![The BrowseScreen set to List4 layout, updated](./media/get-started-create-from-data/list4-fixed.jpg)

1. In the Quick Start pane, click **Theme** to open	the **Theme** tab.

	![Theme tab of the Quick Start pane](./media/get-started-create-from-data/qs-theme.jpg)

1. Click a different theme, such as **Burgundy**.

	The colors on all screens in the app change to reflect the new theme.

	![Left navigation bar shows all screens with updated theme](./media/get-started-create-from-data/new-theme.jpg)

## Customize the app further ##

1. On the **BrowseScreen1** screen, click **Sunday** just under the search icon.

	![Heading2 label selected](./media/get-started-create-from-data/select-heading2.jpg)

	The label is now selected so that you can change its properties. When you change the property of an element in the first item of a gallery, you automatically change that property of the same element in all other items of the gallery.

1. On the **Home** tab of the ribbon, click the **FontWeight** button, and then click **Bold**.

	![The option to make text bold](./media/get-started-create-from-data/label-bold.jpg)

	The day information in all items of the gallery appear in bold text.

	![BrowseScreen1 with day information in bold](./media/get-started-create-from-data/browsescreen-bold.jpg)

1. Click the time information in the first item of the gallery to select that label.

	![Subtitle2 label selected](./media/get-started-create-from-data/select-subtitle2.jpg)

1. Drag the white square on the right edge of the selection box so that the label just fits the information it contains.

	![Resizing Subtitle2](./media/get-started-create-from-data/resize-subtitle2.jpg)

1. Move all three labels, by dragging their selection boxes, so that they appear in a row that's horizontally aligned with the arrow for each item.

	![Align all labels in a row on Browsescreen](./media/get-started-create-from-data/browsescreen-aligned.jpg)

## Change the sort and filter criteria

1. With **BrowseScreen1** showing, click below the last item.

	The gallery that contains the schedule data is selected so that you can change its properties. In the properties list, the **Items** property is selected automatically, and its default value is this expression:

	![The default value of the **Items** property](./media/get-started-create-from-data/sort-before.jpg)

1. Change value of the **Items** property to this expression, which shows the updates in red bold.

	![The value of the **Items** property, set to sort by StartDay](./media/get-started-create-from-data/sort-after.jpg)

1. Press F5, and then click the sort button, near the top of the screen, more than once.

	![Sort button](./media/get-started-create-from-data/sort-button.jpg)

	The items are sorted alphabetically by **StartDay**, switching between ascending and descending order.

1. In the search box, delete the space that it contains by default, and then type one or more letters in at least one of the **Staff1** names.

	The screen shows only shifts that are staffed by people whose names contain the text that you specify.

	![BrowseScreen1 showing only the items that contain the search string in Staff1](./media/get-started-create-from-data/browsescreen-filtered.jpg)

1. Press Esc to return to the default workspace.

When you finish customizing your app, you can share it with other people, as the last procedure in [Create an app with a template](get-started-test-drive.md) describes.
