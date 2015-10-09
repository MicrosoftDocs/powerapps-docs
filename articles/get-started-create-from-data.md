<properties
	pageTitle="Create an app from data in KratosApps"
	description=""
	services="kratosapps"
	authors="AFTOwen"
 />

<tags
   ms.service="kratosapps"
   ms.devlang="na"
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/06/2015"
   ms.author="anneta"/>

# Create an app from data
Create an app automatically based on data that you specify, explore how the app works by default, and then customize the app to better fit how you work.

[What is KratosApps?]()

**Prerequisites**

- Sign up for and install [KratosApps]()
- A set of data in the cloud, such as in DropBox or OneDrive
- Familiarity with how to [configure a control](get-started-test-drive.md#configure-a-control) in KratosApps

## Connect to data ##
You can create an app based on data from any of several kinds of sources. For this tutorial, the data source is an Excel file in Dropbox. The file, named **eventsignup.xls**, contains this data [formatted as a table](https://support.office.com/en-us/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370) and named **Schedule**.

![Source data in Excel](./media/get-started-create-from-data/excel-source.jpg)

1. Sign in to KratosApps, and then click **New** in the left navigation bar.

	![The New option in the left navigation bar](./media/get-started-create-from-data/file-new.jpg)

1. Leave the default option to create a phone app.

	![The option buttons for creating a tablet or phone app](./media/get-started-create-from-data/phone-app.jpg)

1. Under **Start from Data**, click **Get started**.

	![Option to create an app from data](./media/get-started-create-from-data/create-from-data.jpg)

1. If you don't already have a connection to a data source:
	1. Click **Available Connections**, and then click an option in the list that appears.
	1. Name the connection you're about to create, click **Add Connection**, and provide any requested credentials to connect to that data source.

	![Create connection to Dropbox](./media/get-started-create-from-data/dropbox-connection.jpg)

1. Click a data set, and then click **Connect**.

	![Specify an Excel file in a Dropbox account](./media/get-started-create-from-data/choose-excel-file.jpg)

1. Click a table, and then click **Connect**.

	![Specify a table in an Excel file](./media/get-started-create-from-data/choose-table.jpg)

An app is created from the data that you specified.

## Exploring the app ##

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

## Customizing the app ##
You can customize elements on any of the default screens, and you can even [add and delete screens]() to better suit your needs. To change how the **BrowseScreen** shows data, you configure an element in the first item, which automatically updates the same element in all other items.

1. In the first item, click the day name to select that label.

	![Select Body1](./media/get-started-create-from-data/select-body1.jpg)

1. On the **Home** tab, click the text-color option, and then click the green option in the list that appears.

	![Change text color](./media/get-started-create-from-data/change-text-color.jpg)

	The day in each item appears in green.

	![Each day appears in green](./media/get-started-create-from-data/green-days.jpg)

1. In the first item, click the name that appears in the upper-right corner, and move it until the two names are aligned on their right edges.

	![Select Heading1](./media/get-started-create-from-data/select-heading1.jpg)

	All names are aligned on their right edges.

1. If **Express Mode** isn't already showing, click **Express Mode** near the lower-right corner.

	![Open Express Mode](./media/get-started-create-from-data/open-express-mode.jpg)

1. In **Express Mode**, click **Content** to show options for changing the kinds of data that appear in each element on the screen.

	![Show Content options](./media/get-started-create-from-data/content-tab.jpg)

1. In the **Heading1** list, choose **Shift**.
1. In the **Subtitle1** list, choose **Leader**.

 	The time for each shift moves to the upper-right corner of each item, and both people appear near the bottom instead of near the right edge.

	![Change data in two labels](./media/get-started-create-from-data/swapped-positions.jpg)

When you finish customizing your app, you can share it with other people, as the last procedure in [Create an app with a template](get-started-test-drive.md) describes.
