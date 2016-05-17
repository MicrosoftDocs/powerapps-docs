<properties
   pageTitle="Create an app to manage data from SharePoint Online | Microsoft PowerApps"
   description="Create an app to manage data, such as account information, from SharePoint Online"
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="jamesol-msft"
   manager="darshand"
   editor=""
   tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="05/03/2016"
   ms.author="jamesol"/>

# Create an app to manage data from SharePoint Online #

Create an app for adding, updating, and deleting data in a SharePoint list. Specify the list, create the app automatically, and then specify which data you want to show. Test the app by displaying, sorting, filtering, and updating data.

## Prerequisites

- [Sign up](signup-for-powerapps.md) for PowerApps and [install](http://aka.ms/powerappsinstall) PowerApps. When you open PowerApps, sign in using the same credentials that you used to sign up.
- PowerApps only supports creating apps for SharePoint Online custom lists. Document libraries are currently not supported, but will be soon.
- Check to make sure that your list only contains columns supported by PowerApps. The following table lists the column types that are supported by PowerApps:  

	| SharePoint online list column type | Supported by PowerApps |
|---|---|
| Boolean (Yes/No) | Yes |
| Single line of text | Yes |
| Number | Yes |
| Hyperlink | Yes |
| Multiple lines of text | Yes |
| Date and Time | Yes |
| Currency | Yes |
| Picture | Yes (read-only) |
| Lookup | Yes (read-only) |
| Person or Group | Yes (read-only) |
| Managed Metadata | Yes (read-only) |
| Choice | Yes (read-only) |
| Calculated | Yes (read-only) |
| Task Outcome | No |
| External data | No |


> [AZURE.NOTE] For the column types marked as *Yes (read-only)*, full support is coming soon. 

## Create an app ##
1. In PowerApps, select **New** (near the left edge of the screen).  

	![](./media/app-from-sharepoint/Menu.png)

2. Under **Create an app from your data**, select Phone layout on the **SharePoint Online** tile.  

	![](./media/app-from-sharepoint/AFD.png)

3. If you haven't connected to SharePoint Online before, select **Connect** when prompted, and then provide your credentials.  

	![](./media/app-from-sharepoint/Connect.png)

4. Under **Connect to a SharePoint site**, type or paste the URL of the SharePoint site that you want to use, and then select **Go**.  

	![Specify the SharePoint site](./media/app-from-sharepoint/EnterSite.png)

5. Under **Choose a list**, select the list that you want to use and then select **Connect**.  

	![Select a list](./media/app-from-sharepoint/SelectList.png)

	Here are the columns of the SharePoint Online custom list that is used for the examples in this article:  
	![](./media/app-from-sharepoint/ListColumns.png)

	PowerApps builds an app that has three screens:  
	<!-- **Edit form** control add-form.md -->
	
	- **BrowseScreen1** shows a list of all items and some information about the items, so that users can easily browse for the item they want.  
	- **DetailScreen1** shows all information about a single item.  
	- **EditScreen1** provides an **[Edit form](add-form.md)** control for adding an item or updating information about an item.  

## Customize the app ##
When an app is built automatically, heuristics suggest the best layout and content based on the data. You might need to change the app for your needs.

1. If you haven't used PowerApps before, take the intro tour by reading each description before selecting **Next** (and then selecting **Done**), or select **Skip**.

2. On the **Home** tab of the ribbon, select **Layouts**, and then select an option that includes images.  

	![Layout option with icons](./media/app-from-sharepoint/change-layout.png)

	The layout of **BrowseScreen1** changes to reflect your selection.  

	![BrowseScreen1 with new layout](./media/app-from-sharepoint/browse.png)

	**Note**: If you open the **Layout** tab with **DetailScreen1** or **EditScreen1** showing, you can choose different options, which reflect the data on that screen.

3. In the list of thumbnails, select **DetailScreen1**.  
![](./media/app-from-sharepoint/left-pane.png)

4. Select a field on the screen that you want to customize.  
![](./media/app-from-sharepoint/SelectField.png)

5. In the **Options** pane, you can use the card selector to change the control that is used to display this field in the **DetailsScreen1**.  
![](./media/app-from-sharepoint/CardSelector.png)  

	The following tables lists the supported cards for each SharePoint Online list column type:  

	| SharePoint online list column type | Supported Cards |
|---|---|
| Yes/No | View text <br/>View toggle |
| Number | View percentage <br/>View rating <br/>View text |
| Hyperlink | View URL <br/>View text |
| Single line of text | View text |
| Multiple lines of text | View text |
| Date and Time | View text |
| Currency | View percentage <br/>View rating <br/>View text |
| Picture | View image <br/>View text |
| Lookup | View lookup |
| Person or Group | View lookup |
| Managed Metadata | View lookup |
| Choice | View lookup |


6. If you select the **View lookup** card for a field, then you have the option to choose which property of the field is displayed in the card.  To do so, select the **Ellipsis** next to the field in the **Options** pane and select **Advanced Options**.  
![](./media/app-from-sharepoint/Elipsis.png)

7. In the **Data** section, select the property of the field you want to be displayed using the **Value** dropdown.  
![](./media/app-from-sharepoint/AdvancedOptions.png)

## Run the app ##
As you customize the app, you can test your changes by running the app in **Preview** mode.

1. In the list of thumbnails, select **BrowseScreen1**, and then open preview by selecting the **Preview** icon near the upper-right corner (or by pressing **F5**).  

	![Preview icon](./media/app-from-sharepoint/open-preview.png)

2. On **BrowseScreen1**, select the arrow for a record to show details about that record.  

	![Select an arrow on BrowseScreen1](./media/app-from-sharepoint/preview-item.png)

3. On **DetailsScreen1**, select the edit icon (in the upper-right corner) to edit the record.  

	![Edit a record](./media/app-from-sharepoint/select-edit.png)

4. On **EditScreen1**, change the information in one or more fields, and then select the check mark in the upper-right corner to save your changes.  

	![Save changes on EditScreen1](./media/app-from-sharepoint/edit-item.png)

5. Editing the item in the app will update the record in the SharePoint Online list.  

	![Updated List](./media/app-from-sharepoint/UpdatedList.png)

## Next steps ##
- Press Ctrl-S to save your app so that you can run it from other devices.
- Customize your app further, as [Create an app from scratch](get-started-create-from-blank.md) describes.
- [Share the app](share-app.md) so that other people can run it.
