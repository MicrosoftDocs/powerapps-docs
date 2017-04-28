<properties
   pageTitle="Customize a gallery layout | Microsoft PowerApps"
   description="Specify which controls to show, which fields to show in each control, and which columns to use for sorting and searching for records."
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="aftowen"
   manager="anneta"
   editor=""
   tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/16/2016"
   ms.author="anneta"/>

# Customize a gallery layout in PowerApps #
After you generate an app automatically in PowerApps, customize the browse screen, which appears by default. Specify which layout to use, which columns to show, and which columns to use when sorting and searching for records.

- For information about how to generate an app automatically, see [Generate an app to manage data in a SharePoint list](app-from-sharepoint.md).
- If you're unfamiliar with PowerApps, see [Introduction to PowerApps](getting-started.md).

## Prerequisites ##
You can review this tutorial for general concepts only, or you can follow it exactly if you complete these steps.

1. [Create a connection](connect-to-sharepoint.md) from PowerApps to SharePoint.
1. Create a SharePoint list, named **AppGen**, that contains these columns.

	![Sample columns from SharePoint](./media/customize-layout-sharepoint/list-columns.png)

1. Add these items to the list that you just created.

	![Sample data](./media/customize-layout-sharepoint/sample-data.png)

1. [Generate an app automatically](app-from-sharepoint.md) based on the list that you just created.

## Customize the gallery ##

1. **BrowseScreen1** shows the SharePoint list and the **Title** and **AccountID** for each item.

	![Browse screen shows titles and account IDs](./media/customize-layout-sharepoint/browse-accountid.png)

	Next, you'll specify that the **OrderDate** for each item will appear instead of the **AccountID**.

1. Click the **AccountID** for the first item on the screen.

	When you click a UI element (called a control), you select it, and a selection border with resize handles appears around that control.

	![Select body of first item](./media/customize-layout-sharepoint/select-body.png)

1. In the right-hand pane, choose what data field to show up in the gallery. Choose **OrderDate** for Heading1.

	![Show title](./media/customize-layout-sharepoint/bind-data.png)

	**BrowseScreen1** reflects your change.

	![Layout with dates](./media/customize-layout-sharepoint/browse-dates.png)

1. Learn more about how to add controls in a gallery, please read [Show a list of items in PowerApps](add-gallery.md).

## Set the sort and search columns ##
1. Select the **Gallery** control by clicking or tapping any record except the first one.

	![Select gallery](./media/customize-layout-sharepoint/select-gallery.png)

1. Near the upper-left corner, ensure that the property list shows **Items**.

	![Items property](./media/customize-layout-sharepoint/items-property.png)

	The value of this property, which appears in the formula bar, determines not only the source of data that appears on the screen but also the search and sort columns.

	For example, the formula bar might contain this formula by default.

	![Default Items property](./media/customize-layout-sharepoint/default-items.png)

	Based on this formula, users can search for all records that contains one or more letters in the **AccountID** column.

	![Default search columns](./media/customize-layout-sharepoint/default-search.png)

	If a user typed, for example, the letter "v" into the search bar, the screen would show the record for Europa. The title of that record doesn't match the search criterion, but the account ID does. Later in this procedure, you'll change the formula to filter records based on the **Title** column.

	In any generated app, users can sort records alphabetically in ascending or descending order by clicking or tapping the sort button near the upper-right corner. This formula specifies that the records will be sorted based on the **ID** column.

	![Default sort column](./media/customize-layout-sharepoint/default-sort.png)

	Later in this procedure, you'll change the formula to sort the records based on the **Title** column instead.

1. In the formula bar, replace **"AccountID"** with **"Title"** (including the double quotation marks).

1. In the formula bar, replace **"ID"** with **"Title"** (including the double quotation marks).

	The formula bar should now contain a formula that resembles this example:<br>
	**SortByColumns(Search(AppGen, TextSearchBox1.Text, "Title"), "Title", If(SortDescending1, Descending, Ascending))**

	**Note**: The number that appears after **TextSearchBox** might be higher, depending on what actions you took previously. However, the formula should still work as expected.

## Test sorting and searching ##
1. Open Preview mode by pressing F5 (or by clicking or tapping the play button near the upper-right corner).

	![Open Preview mode](./media/customize-layout-sharepoint/open-preview.png)

1. Near the upper-right corner of **BrowseScreen1**, click or tap the sort button one or more times to change the alphabetical sort order between ascending and descending.

	![Test the sort button](./media/customize-layout-sharepoint/test-sort.png)

1. In the search box, type one more letters to show only those records of which the title contains the letter or letters that you type, regardless of case.

	![Test the search bar](./media/customize-layout-sharepoint/test-search.png)

1. Remove all text from the search bar, and then close Preview mode by pressing Esc (or by clicking or tapping the close icon *under* the title bar for PowerApps).

	![Close Preview mode](./media/customize-layout-sharepoint/close-preview.png)

## Change the title of the screen ##
1. Click or tap the title of the screen to select it.

	![Select screen title](./media/customize-layout-sharepoint/select-screen-title.png)

1. Ensure that the property list shows **Text**, and then type the name that you want, surrounded by double quotation marks, in the formula bar.

	![Update screen title](./media/customize-layout-sharepoint/update-screen-title.png)

	**BrowseScreen1** reflects your change.

	![New screen title](./media/customize-layout-sharepoint/new-screen-title.png)

## Next steps ##
- Press Ctrl-S to save your changes.
- [Customize the forms](customize-forms-sharepoint.md) in the app by showing, hiding, and reordering the fields that the forms show.
