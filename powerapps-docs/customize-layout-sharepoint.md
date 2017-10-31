---
title: Customize a gallery layout | Microsoft Docs
description: Specify which controls to show, which fields to show in each control, and which columns to use for sorting and searching for records.
services: ''
suite: powerapps
documentationcenter: na
author: skjerland
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 05/02/2017
ms.author: sharik

---
# Customize a gallery layout in PowerApps
After you generate an app automatically in PowerApps, customize the browse screen, which appears by default. Specify which layout to use, which columns to show, and which columns to use when sorting and filtering records.

* For information about how to generate an app automatically, see [Generate an app to manage data in a SharePoint list](app-from-sharepoint.md).
* If you're unfamiliar with PowerApps, see [Introduction to PowerApps](getting-started.md).

## Prerequisites
You can review this tutorial for general concepts only, or you can follow it exactly if you complete these steps.

1. [Create a connection](connect-to-sharepoint.md) from PowerApps to SharePoint.
2. Create a SharePoint list, named **AppGen**, that contains these columns.
   
    ![Sample columns from SharePoint](./media/customize-layout-sharepoint/list-columns.png)
3. Add these items to the list that you just created.
   
    ![Sample data](./media/customize-layout-sharepoint/sample-data.png)
4. [Generate an app automatically](app-from-sharepoint.md) based on the list that you just created.
5. In the left navigation bar, click or tap an icon in the upper-right corner to switch to the thumbnail view.
   
    ![Toggle the views](./media/customize-layout-sharepoint/toggle-view.png)

## Customize the gallery
1. In the left navigation bar, click or tap the top thumbnail to ensure that **BrowseScreen1** is selected.
   
    ![Thumbnail for BrowseScreen1](./media/customize-layout-sharepoint/browse-thumbnail.png)
   
    **BrowseScreen1** shows the **AccountID** and **Title** of each item in the SharePoint list.
   
    ![Browse screen shows titles and account IDs](./media/customize-layout-sharepoint/browse-accountid.png)
   
    Next, you'll specify that the **OrderDate** for each item will appear instead of the **AccountID**.
2. Click or tap the **AccountID** for the first item on the screen.
   
    When you click or tap a UI element (called a control), you select it, and a selection border with resize handles appears around that control.
   
    ![Select body of first item](./media/customize-layout-sharepoint/select-body.png)
3. In the right-hand pane, open the **Title1** list, and then click or tap **OrderDate**.
   
    ![Show title](./media/customize-layout-sharepoint/bind-data.png)
   
    **BrowseScreen1** reflects your change.
   
    ![Layout with dates](./media/customize-layout-sharepoint/browse-dates.png)

For more information about galleries, see [Show a list of items in PowerApps](add-gallery.md).

## Set the sort and search columns
1. Select the **Gallery** control by clicking or tapping any record except the first one.
   
    ![Select gallery](./media/customize-layout-sharepoint/select-gallery.png)
2. Near the upper-left corner, ensure that the property list shows **Items**.
   
    ![Items property](./media/customize-layout-sharepoint/items-property.png)
   
    The value of this property, which appears in the formula bar, determines not only the source of data that appears on the screen but also the filter and sort columns.
   
    For example, the formula bar might contain this formula by default.
   
    ![Default Items property](./media/customize-layout-sharepoint/default-items.png)
   
    Based on this formula, users can show only those records that start with one or more letters in the **AccountID** column.
   
    ![Default search columns](./media/customize-layout-sharepoint/default-search.png)
   
    If a user typed, for example, the letter "A" into the search bar, the screen would show the record for Europa. The title of that record doesn't match the search criterion, but the account ID does. Later in this procedure, you'll change the formula to filter records based on the **Title** column.
   
    In any generated app, users can sort records alphabetically in ascending or descending order by clicking or tapping the sort button near the upper-right corner. This formula specifies that the records will be sorted based on the **AccountID** column.
   
    ![Default sort column](./media/customize-layout-sharepoint/default-sort.png)
   
    Later in this procedure, you'll change the formula to sort the records based on the **Title** column instead.
3. In the formula bar, replace both instances of **AccountID** with **Title** (including the double quotation marks around the second instance).
   
    The formula bar should now contain a formula that resembles this example:<br>
    **SortByColumns(Filter(AppGen, StartsWith(Title, TextSearchBox1.Text)), "Title", If(SortDescending1, Descending, Ascending))**
   
    > [!NOTE]
> The number that appears after **TextSearchBox** might be higher, depending on what actions you took previously. However, the formula should still work as expected.

## Test sorting and searching
1. Open Preview mode by pressing F5 (or by clicking or tapping the play button near the upper-right corner).
   
    ![Open Preview mode](./media/customize-layout-sharepoint/open-preview.png)
2. Near the upper-right corner of **BrowseScreen1**, click or tap the sort button one or more times to change the alphabetical sort order between ascending and descending.
   
    ![Test the sort button](./media/customize-layout-sharepoint/test-sort.png)
3. In the search box, type one more letters to show only those records of which the title starts with the letter or letters that you type.
   
    ![Test the search bar](./media/customize-layout-sharepoint/test-search.png)
4. Remove all text from the search bar, and then close Preview mode by pressing Esc (or by clicking or tapping the close icon *under* the title bar for PowerApps).
   
    ![Close Preview mode](./media/customize-layout-sharepoint/close-preview.png)

## Change the title of the screen
1. Click or tap the title of the screen to select it.
   
    ![Select screen title](./media/customize-layout-sharepoint/select-screen-title.png)
2. Ensure that the property list shows **Text**, and then type the name that you want, surrounded by double quotation marks, in the formula bar.
   
    ![Update screen title](./media/customize-layout-sharepoint/update-screen-title.png)
   
    **BrowseScreen1** reflects your change.
   
    ![New screen title](./media/customize-layout-sharepoint/new-screen-title.png)

## Next steps
* Press Ctrl-S to save your changes.
* [Customize the forms](customize-forms-sharepoint.md) in the app by showing, hiding, and reordering the fields that the forms show.

