<properties
   pageTitle="Create an app to manage data from SharePoint | Microsoft PowerApps"
   description="Create an app to manage data, such as account information, from SharePoint"
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="jamesol-msft"
   manager="erikre"
   editor=""
   tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="06/24/2016"
   ms.author="jamesol"/>

# Create an app to manage data from SharePoint #
Create an app for adding, updating, and deleting data in a SharePoint list. Specify the list, create the app automatically, customize the app, and then test it by updating an item in the list.

**Prerequisites**

- [Sign up](signup-for-powerapps.md) for PowerApps, [install](http://aka.ms/powerappsinstall) it, open it, and then sign in by providing the same credentials that you used to sign up.

As of this writing, PowerApps supports lists but not libraries. In addition, you can show data in some types of columns, such as **Choice** and **Picture**, but you can't update that data. For more information, see [Known issues](connection-sharepoint-online.md#known-issues).

The list in this tutorial contains these columns:  
![](./media/app-from-sharepoint/ListColumns.png)

## Create an app ##
1. In PowerApps, click or tap **New** (near the left edge of the screen).

	![](./media/app-from-sharepoint/Menu.png)

1. On the **SharePoint** tile, click or tap **Phone layout**.

1. Follow the steps in either of these bullets:

	- To connect to SharePoint Online, click or tap **Connect directly (cloud services)**.

	- To connect to an on-premises SharePoint site, click or tap **Connect using on-premises data gateway**, specify **Windows** as the authentication type, and then specify your credentials. (If your credentials include a domain name, specify it as *Domain\Alias*.)

	**Note**: If you don't have an on-premises data gateway installed, [install one](gateway-reference.md), and then click or tap the icon to refresh the list of gateways.

	Under **Choose a gateway**, click or tap the gateway that you want to use.

1. Click or tap **Connect**.

1. Under **Connect to a SharePoint site**, type or paste the URL to the site that contains the list that you want to use, and then click or tap **Go**.

	**Note**: Don't include a specific list in the URL.

1. Under **Choose a list**, click or tap the name of the list that you want to use.

	In the search box, you can type or paste at least one letter to show only those lists of which their names contain the letter or letters that you specify. You can also click or tap the sort-order icon to toggle between sorting the list in ascending or descending order.

	![Filter or sort lists](./media/app-from-sharepoint/filter-sort-lists.png)

1. Click or tap **Connect**.

PowerApps builds an app that has three screens:  

- In **BrowseScreen1**, users can easily browse through all items in a **[Gallery](control-gallery.md)** control.  
- In **DetailScreen1**, users can view all information about a specific item in a **[Display form](edit-form.md)** control.  
- In **EditScreen1**, users can add or update an item in an **[Edit form](edit-form.md)** control.  

## Customize the app ##
When PowerApps builds an app automatically, heuristics suggest the best layout and content based on the data. You might need to change the app for your needs.

1. If you haven't used PowerApps before, take the intro tour (or click or tap **Skip**).

2. On the **Home** tab, click or tap **Layouts**, and then click or tap an option that suits your data.  

	**Note**: If you open the **Layout** tab with **DetailScreen1** or **EditScreen1** showing, you can choose different options, which reflect the data on that screen.

	![Layout option with icons](./media/app-from-sharepoint/change-layout.png)

	The layout of **BrowseScreen1** changes to reflect your selection.  

	![BrowseScreen1 with new layout](./media/app-from-sharepoint/browse-screen.png)

1. Click or tap any control, such as the **Image** control, in the first item of the gallery.

	![Select a control in the gallery](./media/app-from-sharepoint/select-image.png)

1. In the right-hand pane, specify the data that you want to show in each control.

	![Specify columns](./media/app-from-sharepoint/specify-columns.png)

	The screen changes to reflect your selections.

	![EditScreen1](./media/app-from-sharepoint/gallery-final.png)

1. Open **DetailsScreen1**, and then change the cards that appear by clicking or tapping the eye icon for each card in the right-hand pane.

	![Show card](./media/app-from-sharepoint/show-card.png)

1. Change the order in which the cards appear by clicking or tapping a card and then dragging its title bar up or down.

	![Move card](./media/app-from-sharepoint/move-card.png)

## Run the app ##
As you customize the app, you can test your changes by running the app in **Preview** mode.

1. In left navigation bar, click or tap **BrowseScreen1**, and then open Preview mode by selecting the **Preview** icon near the upper-right corner (or by pressing **F5**).  

	![Preview icon](./media/app-from-sharepoint/open-preview.png)

2. On **BrowseScreen1**, click or tap the arrow for an item to show details about that item.  

	![Select an arrow on BrowseScreen1](./media/app-from-sharepoint/right-arrow.png)

3. On **DetailsScreen1**, click or tap the edit icon (in the upper-right corner) to edit the record.  

	![Edit a record](./media/app-from-sharepoint/select-edit2.png)

4. On **EditScreen1**, change the information in one or more fields, and then click or tap the check mark in the upper-right corner to save your changes back to the SharePoint list.  

	![Save changes on EditScreen1](./media/app-from-sharepoint/edit-item2.png)

## Next steps ##
- Press Ctrl-S to save your app so that you can run it from other devices.
- [Customize one or more cards](customize-card.md), for example, to show a date in a **[DatePicker](control-date-picker.md)** control.
- [Share the app](share-app.md) so that other people can run it.
