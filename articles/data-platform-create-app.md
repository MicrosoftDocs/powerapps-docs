<properties
	pageTitle="Create an app using the Common Data Model | Microsoft Common Data Model"
	description="Create an app to add, update, and delete records in the Common Data Model"
	services="powerapps"
	documentationCenter="na"
	authors="karthik-1"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="07/21/2016"
   ms.author="karthikb"/>

# Create an app using the Common Data Model #
Create an app to manage data that's stored in the Common Data Model, using standard entities (which are built in), custom entities (which your organization creates), or both.

If you're unfamiliar with the Common Data Model, see [Understand entities](data-platform-intro.md).

PowerApps can generate an app automatically based on a single entity that you specify, or you can create an app from scratch that uses one or more entities that you specify.

In either case, you don't need to create a connection from PowerApps to the Common Data Model, as you do with external connections such as SharePoint, Dynamics CRM, and Salesforce. You need only specify the entities or entities that you want to show, manage, or both in the app.

## Generate an app automatically ##

[AZURE.VIDEO nb:cid:UUID:e0d83908-aedd-4db3-8ea9-2dbd4695c662]

1. [Sign up for PowerApps](signup-for-powerapps.md), and then do *either* of the following:

	- [Open PowerApps](https://create.powerapps.com/api/start) in a browser.
	- [Install PowerApps](http://aka.ms/powerappsinstall) from the Windows Store. Open PowerApps, sign in, and then click or tap **New** on the **File** menu (along the left edge).

		![New option on the File menu](./media/data-platform-create-app/file-new.png)

1. Under **Create an app from your data**, click or tap **Phone layout** on the **Common Data Model** tile.

	![Create app from data](./media/data-platform-create-app/afd-cdm.png)

1. If prompted, click or tap **Create my database**.

	![Create database](./media/data-platform-create-app/create-database.png)

1. Under **Choose an entity**, click or tap the **Contact** entity.

	![Choose Contact entity](./media/data-platform-create-app/afd-choose-entity.png)

1. Click or tap **Connect** to automatically generate an app.

	![Connect button](./media/data-platform-create-app/connect-button.png)

1. If you're not familiar with PowerApps, identify key areas of the app by taking the intro tour (or click or tap **Skip**).

	![Opening screen of the quick tour](./media/data-platform-create-app/quick-tour.png)

	**Note**: You can always take the tour later by clicking or tapping the question-mark icon near the upper-right corner and then clicking or tapping **Take the intro tour**.

## Customize the browse screen ##
1. In the right-hand pane, click or tap the layout that shows just a header.

	![Choose layout](./media/data-platform-create-app/choose-layout.png)

1. Under the search box, click or tap the **Text box** control to select it.

 	Whenever you select a control, a selection box (with resize handles) surrounds that control.

	![Select text box](./media/data-platform-create-app/select-text-box.png)

1. In the right-hand pane, click or tap the down arrow to open the list of fields.

	![Open drop-down list](./media/data-platform-create-app/open-dropdown.png)

1. Click or tap **Last Name** to show data from that field in the **Text box** control that you selected.

	![Choose LastName](./media/data-platform-create-app/choose-lastname.png)

1. Select the gallery by clicking or tapping any name except the top one.

	A selection box surrounds the gallery.

	![Select gallery](./media/data-platform-create-app/select-gallery.png)

1. Near the upper-left corner, ensure that the property list shows **Items**.

	![Items property](./media/data-platform-create-app/items-property.png)

1. In the formula bar, highlight the default formula.

	![Default value of the Items property](./media/data-platform-create-app/default-items.png)

1. Press Delete to delete the default formula, and then copy this formula.
<br>**SortByColumns(Search(Contact, TextSearchBox1.Text, "LastName"), "LastName", If(SortDescending1, Descending, Ascending))**

1. In the formula bar, paste the formula that you just copied.

	![Updated value of the Items property](./media/data-platform-create-app/new-items-formula.png)

	The names are sorted alphabetically.

## Test the browse screen ##
1. Open Preview mode by pressing F5 (or by clicking or tapping the play icon near the upper-right corner).

	![Open Preview mode](./media/data-platform-create-app/open-preview.png)

1. Near the upper-right corner, click or tap the sort button one or more times to change order in which the names are listed.

	![Change sort order](./media/data-platform-create-app/sort-button.png)

1. In the search box, type a letter such as "w" to show only those names that contain the letter that you typed.

	![Filter list](./media/data-platform-create-app/search-w.png)

1. Click or tap the arrow to the right of the first name in the list.

	![Right arrow](./media/data-platform-create-app/right-arrow.png)

1. Return to the design workspace by pressing Esc (or by clicking or tapping the close icon near the upper-right corner, under the title bar).

	![Close Preview mode](./media/data-platform-create-app/close-preview.png)

## Customize the details screen ##
1. Click or tap the **CellPhone** card to select it.

	![Select card](./media/data-platform-create-app/select-card.png)

1. In the right-hand pane, click or tap the eye icon for the **CellPhone** card to hide it.

	![Hide card](./media/data-platform-create-app/hide-card.png)

1. Repeat the previous step for each of these cards:

	- **Description**
	- **Facebook**
	- **FullName**

1. Click or tap the **FirstName** card to select it.

	![Select FirstName card](./media/data-platform-create-app/select-firstname.png)

1. Drag the title of that card up until the **BusinessPhone** card is highlighted.

1. Release the mouse button so that the **FirstName** card appears above the **BusinessPhone** card.

1. Repeat the last three steps except move the **LastName** card so that it appears between the **FirstName** card and the **BusinessPhone** card

## Customize the edit screen ##
1. Near the upper-right corner of the details screen, click or tap the pencil icon.

	![Select BusinessPhone card](./media/data-platform-create-app/edit-record.png)

1. Repeat the steps in the previous procedure to show, hide, and arrange the cards on the edit screen as you did on the details screen.

## Build an app from scratch ##

[AZURE.VIDEO nb:cid:UUID:5e58b2b8-44a0-467f-b6ec-58dee9fd925a]

1. [Sign up for PowerApps](signup-for-powerapps.md), and then do *either* of the following:

	- [Open PowerApps](https://create.powerapps.com/api/start) in a browser.
	- [Install PowerApps](http://aka.ms/powerappsinstall) from the Windows Store. Open PowerApps, sign in, and then click or tap **New** on the **File** menu (along the left edge).

		![New option on the File menu](./media/data-platform-create-app/file-new.png)

1. Under **Create an app**, click or tap **Phone layout** on the **Blank app** tile.

	![Create from blank](./media/data-platform-create-app/create-from-blank.png)

1. If you're not familiar with PowerApps, identify key areas of the app by taking the intro tour (or click or tap **Skip**).

	![Opening screen of the quick tour](./media/data-platform-create-app/quick-tour.png)

	**Note**: You can always take the tour later by clicking or tapping the question-mark icon near the upper-right corner and then clicking or tapping **Take the intro tour**.

1. In the right-hand pane, click or tap **Data sources** to open that tab, and then click or tap **Add data source**.

1. In the list of connections, click or tap **Common Data Model**, and then click or tap **Connect**.

1. If prompted, click or tap **Create my database**.

1. In the list of entities, select the check box for one or more entities that you want to use, and then click or tap **Connect**.

The entities or entities that you specified appear in the list of data sources, and you can build your app as [Create an app from scratch](get-started-create-from-blank.md) describes.
