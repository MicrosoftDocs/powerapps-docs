<properties
    pageTitle="Show a list of items | Microsoft PowerApps"
    description="Use a gallery to show a list of items in your app, and filter the list by specifying a criterion."
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
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="04/18/2016"
    ms.author="ankitsar"/>

# Show a list of items in Microsoft PowerApps  #
Show a list of items from Excel, as this topic describes, or from any other type of data source by adding a [**Gallery**](./controls/control-gallery.md) control to your app. Filter the list by configuring the gallery to show only those items that match the filter criterion in a [**Text input**](./controls/control-text-input.md) control.

**Prerequisites**

- Create an app in PowerApps, or add a screen to an app.
- Learn how to [configure a control](./add-configure-controls.md) in PowerApps.
- Create a [connection](./add-data-connection.md) to the **FlooringEstimates** table from [this Excel file](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx), which contains sample data for this tutorial.

## Add a gallery ##
1. On the **Home** tab, select **Layouts**, and then select the option that contains a thumbnail image, a header, and a description.

	![Add a layout with a heading, a subtitle, and a body element](./media/add-gallery/add-gallery.png)

1. Select the gallery, and then select **Options** (near the lower-right corner).

	![Open Options pane](./media/add-gallery/open-options.png)

	The **Gallery** tab of the **Options** pane appears.

    ![Connections option on the File menu](./media/add-gallery/gallery-options.png)

1. Select the data-source icon, and then select the **FlooringEstimates** data source.

    ![Select datasource](./media/add-gallery/select-data-source.png)

	The gallery shows the data from the source that you specified.

## Add a control to the gallery ##
1. In the upper-left corner of the gallery, select the pencil icon to edit the gallery template.

    ![Edit Gallery Item](./media/add-gallery/edit-item.png)

1. Add a [**Text box**](./controls/control-text-box.md) control to the gallery template, and then move and resize the new control so that it doesn't overlap with other controls in the template.

    ![Add Text Box](./media/add-gallery/add-text-box.png)

1. With the text box still selected, select **Price** in the bottom list on the **Options** pane.  

    ![Change Text Box binding](./media/add-gallery/change-binding.png)

    The gallery shows the new values

    ![Final Gallery](./media/add-gallery/final-gallery.png)

## Filter the gallery ##
The **Items** property of a gallery determines which items it shows. You'll configure that property so that the gallery shows only those items for which the product name contains the text in **TextSearchBox1**.

![Text search box](./media/add-gallery/text-search-box.png)

1. Set the **Items** property of the gallery to this formula:

	**If(IsBlank(TextSearchBox1.Text), FlooringEstimates, Filter(FlooringEstimates, TextSearchBox1.Text in Text(Name)))**

1. Type part of or all of the name of a product in the text box.

	The gallery shows only those items that meet the filter criterion.

## Sort the gallery ##
The **Items** property of a gallery determines the order of items that it shows. You'll configure that property so that the gallery shows the order of items as set by **ImageSortUpDown1**.

![Image for sorting](./media/add-gallery/image-sorting.png)

1. Set the **Items** property of the gallery to this formula:

    **Sort(If(IsBlank(TextSearchBox1.Text), FlooringEstimates, Filter(FlooringEstimates, TextSearchBox1.Text in Text(Name))), Name, If(SortDescending1, SortOrder.Descending, SortOrder.Ascending))**

1. Select the sort icon to change the sorting order of the gallery by the names of the products.

To sort and filter your gallery, replace the *DataSource* in this formula with name of your data source, and replace *ColumnName* with the name of the column by which you want to sort, filter, or both.

**Sort(If(IsBlank(TextSearchBox1.Text),** *DataSource*, **Filter(** *DataSource*, **TextSearchBox1.Text in Text(** *ColumnName* **))),** *ColumnName*, **If(SortDescending1, SortOrder.Descending, SortOrder.Ascending))**

## Next steps ##
- Learn more about working with a [gallery](./working-with-forms.md) and [formulas](./working-with-formulas.md).
