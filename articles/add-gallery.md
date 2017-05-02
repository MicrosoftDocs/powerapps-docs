<properties
    pageTitle="Show a list of items | Microsoft PowerApps"
    description="Use a gallery to show a list of items in your app, and filter the list by specifying a criterion."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="sarafankit"
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
    ms.author="ankitsar"/>

# Show a list of items in PowerApps  #

Show a list of items from any data source by adding a **[Gallery](controls/control-gallery.md)** control to your app. This topic uses Excel as the data source. Filter the list by configuring the gallery to show only those items that match the filter criterion in a **[Text input](controls/control-text-input.md)** control.

**Prerequisites**

- Learn how to [add and configure a control](add-configure-controls.md) in PowerApps.
- Download [this Excel file](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx), which contains sample data for this tutorial.
- Upload the Excel file to a [cloud-storage account](cloud-storage-blob-connections.md), such as OneDrive for Business.
- In a new or existing app, [add a connection](add-data-connection.md) to the **FlooringEstimates** table in the Excel file.
- If you're using an existing app, [add a screen](add-screen-context-variables.md) to it.

## Add a gallery ##

1. Start from inserting **New Screen** and choose **List Screen**. This new screen contains a title bar, a search bar, and a vertical gallery. You can also insert a single gallery in any screen. Here is how to do it. In the **Insert** tab of the ribbon, click the **Gallery** tab to choose which gallery you want to insert. There are 3 sets of gallery layout options namely Vertical, Horizontal, and Flexible Height, each with a respective blank layout option. Choose **Vertical** for this one.

  ![Add gallery](./media/add-gallery/gallery-dropdown.png)

   **Vertical**: Galleries that scroll vertically   

   **Horizontal**: Galleries that scroll horizontally

   **Flexible Height**: The height of each grid dynamically adjusts to the contained content (ex. choose this one if you want to add a News Feed to your app)

2. Select the gallery and this brings the gallery pane on the right. Now choose a layout in the right-hand pane.

	![Add gallery](./media/add-gallery/select-layout.png)

3. In the right-hand pane, click the data-source, and then choose the **FlooringEstimates** data source.

	![Select datasource](./media/add-gallery/choose-data.png)

	The gallery shows the data from the source that you specified. And how to configure sort and search is stated in the latter part of this article.

	![Show data](./media/add-gallery/show-data-default.png)

## Add a control to the gallery ##

1. **Decide on a gallery layout before you do any customization.** The first grid in a gallery control is the gallery template and the rest grids repeat the template. To edit the gallery template, select the first grid, and then insert a control from the ribbon. Another way to do this is to click anywhere on the gallery except the first grid and click on the pencil icon shows in its upper-left corner.

    ![Edit gallery template](./media/add-gallery/edit-item.png)

2. Add a **[Label](controls/control-text-box.md)** control to the gallery template, and then move and resize the new control so that it doesn't overlap with other controls in the template.

	![Add label](./media/add-gallery/add-text-box.png)

3. With the **Label** control still selected, open the highlighted list in the right-hand pane.

	![Open drop-down list](./media/add-gallery/open-dropdown.png)

4. In the list of fields that you just opened, click or tap **Price**.  

    ![Change label binding](./media/add-gallery/change-binding.png)

    The gallery shows the new values

    ![Final Gallery](./media/add-gallery/final-gallery.png)

## Filter the gallery ##

The **[Items](controls/properties-core.md)** property of a gallery determines which items it shows. In this procedure, you configure that property so that the gallery shows only those items for which the product name contains the text in **TextSearchBox1**.

![Text search box](./media/add-gallery/text-search-box.png)

1. Set the **[Items](controls/properties-core.md)** property of the gallery to this formula:

        If(IsBlank(TextSearchBox1.Text), FlooringEstimates, Filter(FlooringEstimates, TextSearchBox1.Text in Text(Name)))

2. Type part or all of a product name in the search box.

	The gallery shows only those items that meet the filter criterion.

## Sort the gallery ##

The **[Items](controls/properties-core.md)** property of a gallery determines the order of items that it shows. In this procedure, you configure that property so that the gallery shows the order of items as set by **ImageSortUpDown1**.

![Image for sorting](./media/add-gallery/image-sorting.png)

1. Set the **[Items](controls/properties-core.md)** property of the gallery to this formula:

        Sort(If(IsBlank(TextSearchBox1.Text), FlooringEstimates, Filter(FlooringEstimates, TextSearchBox1.Text in Text(Name))), Name, If(SortDescending1, SortOrder.Descending, SortOrder.Ascending))

2. Select the sort icon to change the sorting order of the gallery by the names of the products.

To sort *and* filter your gallery, replace both instances of *DataSource* in this formula with name of your data source, and replace both instances of *ColumnName* with the name of the column by which you want to sort and filter.

**Sort(If(IsBlank(TextSearchBox1.Text),** *DataSource*, **Filter(** *DataSource*, **TextSearchBox1.Text in Text(** *ColumnName* **))),** *ColumnName*, **If(SortDescending1, SortOrder.Descending, SortOrder.Ascending))**

## Next steps ##
- Learn more about working with a [gallery](working-with-forms.md) and [formulas](working-with-formulas.md).
