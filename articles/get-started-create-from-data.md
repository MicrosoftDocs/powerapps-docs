<properties
	pageTitle="Create a PowerApp from an existing data set"
	description="Create a PowerApp automatically based on an existing set of data that you specify and then customize the UI to better suit your needs."
	services="powerapps"
	documentationCenter="na"
	authors="AFTOwen"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/15/2015"
   ms.author="anneta"/>

# Create a PowerApp from data
Create a PowerApp automatically based on data that you specify, explore how the PowerApp works by default, and then customize it to better fit how you work.

[What are PowerApps?](http://www.kratosapps.com/tutorials)

**Prerequisites**

- Install [PowerApps](http://aka.ms/powerappsinstall )
- Learn how to [configure a control](get-started-test-drive.md#configure-a-control) in PowerApps
- A set of data in the cloud, such as in DropBox or OneDrive

For this tutorial, the data source is an Excel file in Dropbox. The file, named **eventsignup.xls**, contains this data [formatted as a table](https://support.office.com/en-us/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370) and named **Schedule**.

![Source data in Excel](./media/get-started-create-from-data/excel-source.jpg)

## Connect to data ##

1. Under **Start from your data**, select **Get started**.

	![Option to create a PowerApp from data](./media/get-started-create-from-data/create-from-data.jpg)

1. In the list of connections, select the one that contains the data you want to use, select the data, and then select **Connect**.

	![Specify an Excel file in a Dropbox account](./media/get-started-create-from-data/choose-excel-file.jpg)

1. Select a table, and then select **Connect**.

	![Specify a table in an Excel file](./media/get-started-create-from-data/choose-table.jpg)

A PowerApp is created from the data that you specified.

## Explore the PowerApp ##

When the PowerApp is created, it appears in the default workspace, where you can customize the PowerApp to better fit your needs. Before you make changes, you'll explore how the PowerApp works in **Preview**. By running a PowerApp in **Preview**, you can completely test the PowerApp before you share it with others.

1. Press F5 to open **Preview**.

	The first screen, named **BrowseScreen1**, shows which people are signed up for each shift in a schedule.

	![The default BrowseScreen1](./media/get-started-create-from-data/default-browsescreen.jpg)

1. Select the up and down arrows near the top of the screen to reverse the sort order (by the name of the first volunteer).

	![BrowseScreen1 in reverse alphabetical order](./media/get-started-create-from-data/browsescreen-sorted.jpg)

1. In the **Search items** box, type **n** to show only those shifts for which the name of the first volunteer contains that letter.

	![BrowseScreen1 filtered by name](./media/get-started-create-from-data/browsescreen-filtered.jpg)

1. Select the arrow for the first item to show details about that item.

	![Navigate from BrowseScreen1 to DetailScreen1](./media/get-started-create-from-data/right-arrow.jpg)

	The **DetailScreen1** appears, showing all data for the item you specified. You can delete or update that item by using the elements near the top of the screen.

	![The default DetailScreen1](./media/get-started-create-from-data/default-detailscreen.jpg)

1. Select the pencil icon to update the item.

	![The pencil icon](./media/get-started-create-from-data/pencil-icon.jpg)

	The **EditScreen1** appears, with text boxes so that you can change the item, a cancel icon in the upper-left corner, and a save icon in the upper-right corner.

	![The default EditScreen1](./media/get-started-create-from-data/default-editscreen.jpg)

	**Note:** If you select the plus sign on **BrowseScreen1**, **EditScreen1** appears with all the text boxes blank so that you can create an item.

1. Replace either or both of the names with whatever names you want, and then select the save icon.

	![Updating an item](./media/get-started-create-from-data/replace-name.jpg)

	Your change or changes appear in **DetailsScreen1** and in your data source in the cloud.

1. Press Esc to return to the default workspace, in which you can customize your PowerApp.

## Change the layout, the content, and the theme ##
You can customize a PowerApp by adding or deleting a screen, changing a property of a screen, and changing a specific element on a screen.

1. Display **BrowseScreen1** by selecting its thumbnail in the left navigation bar.

	![Thumbnail for BrowseScreen1](./media/get-started-create-from-data/browsescreen1-thumbnail.jpg)

1. Near the lower-right corner of the screen, select **Quick tools**.

	![Button to open Quick tools pane](./media/get-started-create-from-data/open-quick-tools.jpg)

1. In the **Quick tools** pane, select the **Layout** tab, and then select a different layout, such as the one shown in this graphic.

	![Change layout](./media/get-started-create-from-data/change-layout.jpg)

	**BrowseScreen1** shows the day of each shift and the name of each volunteer but not the time of each shift.

	![BrowseScreen1 in new layout, default](./media/get-started-create-from-data/new-layout-default.jpg)

1. In the **Quick tools** pane, select the **Content** tab, and then select **StartTime** in the **Heading12** list.

	![Change what the heading control shows](./media/get-started-create-from-data/change-heading.jpg)

	The time of each shift appears above the day and the name of a volunteer.

	![BrowseScreen1 with ShiftTime added](./media/get-started-create-from-data/list4-fixed.jpg)

1. In the **Quick tools** pane, select **Theme**, and then select a different theme, such as **Red**.

	![Change the theme](./media/get-started-create-from-data/change-theme.jpg)

	The colors on all screens in the PowerApp change to reflect the new theme, as the left navigation bar shows.

	![Left navigation bar shows all screens with updated theme](./media/get-started-create-from-data/new-theme.jpg)

## Customize the app further ##

1. On **BrowseScreen1**, select the name of the volunteer for the first shift in the list.

	![Volunteer name selected](./media/get-started-create-from-data/select-volunteer.jpg)

	The label is now selected so that you can change its properties. When you change the property of an element in the first item of a gallery, you automatically change that property of the same element in all other items of the gallery.

1. On the **Home** tab of the ribbon, click the **FontWeight** button, and then click **Bold**.

	![The option to make text bold](./media/get-started-create-from-data/label-bold.jpg)

	The volunteer name in each item of the gallery appears in bold text.

	![BrowseScreen1 with volunteer name in bold](./media/get-started-create-from-data/browsescreen-bold.jpg)

1. Select the time information for the first shift in the list.

	![Shift time selected](./media/get-started-create-from-data/select-shifttime.jpg)

1. Drag the white square on the right edge of the selection box so that the label just fits the information it contains.

	![Resizing label for shift time](./media/get-started-create-from-data/resize-shifttime.jpg)

1. Resize the other two labels the same way, and then move all three labels (by dragging their selection boxes) so that they appear in a row that's horizontally aligned with the arrow for each item.

	![Align all labels in a row on BrowseScreen1](./media/get-started-create-from-data/browsescreen-aligned.jpg)

1. Select the line near the bottom of the first item in the list, and then press Delete.

	![Select the separator line](./media/get-started-create-from-data/select-separator.jpg)

1. Select the empty space in the first item in the list, below the labels that you just aligned.

	The gallery template is selected.

	![Select the gallery template in BrowseScreen1](./media/get-started-create-from-data/select-browsescreen-template.jpg)

1. Resize the gallery template to show more items on the screen.

	![Show more items in BrowseScreen1](./media/get-started-create-from-data/browsescreen-condensed.jpg)

When you finish customizing your app, you can [save and share it with other people](get-started-test-drive.md#save-and-share-your-app).
