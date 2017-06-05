<properties
	pageTitle="Data table control: reference | Microsoft PowerApps"
	description="Information, including properties and examples, about the Data table control"
	services="powerapps"
	documentationCenter="na"
	authors="jasongre"
	manager="kfend"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="06/05/2017"
   ms.author="kfend"/>

# Data table control in PowerApps

Shows a set of data in a tabular format.

## Description
The **Data table** control shows a dataset in a format that includes column headers for each field that the control shows. As an app maker, you have full control over which fields appear and in what order. Like the **Gallery** control, the **Data table** control maintains a **Selected** property that points to the selected row. Therefore, you can link the **Data table** control to other controls.

## Capabilities  
PowerApps introduced the **Data table** control on May 5, 2017. This section provides information about capabilities that are supported and capabilities that aren't supported.

### Now available
- Data in a **Data table** control is read-only.
- A single row is always selected in a **Data table** control.
- Link a **Data table** control to a connected or local data source.
- Adjust column widths in a **Data table** control while you run the app, though your changes aren't saved.
- A set of default fields appear in a **Data table** control when you link it to a connector that has implemented this capability, such as the Common Data Service. You can then show or hide these fields and others as necessary.
- **(New)** Customize column width and heading text.
- **(New)** Show hyperlinks in a **Data table** control.
- **(New)** Copy and paste a **Data table** control.

### Not yet available
- Customize the styling of individual columns.
- Add a **Data table** control in a form control.
- Change the height of all rows.
- Show images in a **Data table** control.
- Show fields from related entities.
- Use built-in functionality to filter and sort data by column heading.
- Add a **Data table** control in a **Gallery** control.
- Edit data in the **Data table** control.
- Select multiple rows.

### Known issues
- No data appears if you use the **FirstN** function in the **Items** property.
- If you modify the **Items** property, the field list is reset.
- For some connectors, the connection to the data source is lost if you modify the **Items** property.
 
## Key properties

+ [**Items**](https://powerapps.microsoft.com/en-us/tutorials/properties-core/ "Items") – The source of data that appears in the **Data table** control.
+ **Selected** – The selected row in the **Data table** control.

## Other properties

+ [**BorderColor**](https://powerapps.microsoft.com/en-us/tutorials/properties-color-border/ "BorderColor") – The color of the Data table’s border.
+ [**BorderStyle**](https://powerapps.microsoft.com/en-us/tutorials/properties-color-border/ "BorderStyle") – The style of the Data table’s border. The options are **Solid**, **Dashed**, **Dotted**, and **None**.
+ [**BorderThickness**](https://powerapps.microsoft.com/en-us/tutorials/properties-color-border/ "BorderThickness") – The thickness of the Data table’s border.
+ [**Color**](https://powerapps.microsoft.com/en-us/tutorials/properties-color-border/ "Color") – The default text color for all data rows.
+ [**Fill**](https://powerapps.microsoft.com/en-us/tutorials/properties-color-border/ "Fill") – The default background color for all data rows.
+ [**Font**](https://powerapps.microsoft.com/en-us/tutorials/properties-text/ "Font") – The default font for all data rows.
+ [**FontWeight**](https://powerapps.microsoft.com/en-us/tutorials/properties-text/ "FontWeight") – The default font weight for all data rows.
+ **HeadingColor** – The text color for the column headings.
+ **HeadingFill** – The background color of the column headings.
+ **HeadingFont** – The font of the column headings.
+ **HeadingFontWeight** – The font weight of the column headings.
+ **HeadingSize** – The font size of the column headings.
+ [**Height**](https://powerapps.microsoft.com/en-us/tutorials/properties-size-location/ "Height") – The distance between the Data table’s top and bottom edges.
+ [**HoverColor**](https://powerapps.microsoft.com/en-us/tutorials/properties-color-border/ "HoverColor") – The text color for the row that the mouse pointer is currently pointing at.
+ [**HoverFill**](https://powerapps.microsoft.com/en-us/tutorials/properties-color-border/ "HoverFill") – The background color of the row that the mouse pointer is currently pointing at.
+ **NoDataText** – The message that the user receives when there are no records to show in the Data table.
+ **SelectedColor** – The color of the text in the selected row.
+ **SelectedFill** – The background color of the selected row.
+ [**Size**](https://powerapps.microsoft.com/en-us/tutorials/properties-text/ "Size") – The default font size for all data rows.
+ [**Visible**](https://powerapps.microsoft.com/en-us/tutorials/properties-core/ "Visible") – A value that determines whether the Data table appears or is hidden.
+ [**Width**](https://powerapps.microsoft.com/en-us/tutorials/properties-size-location/ "Width") – The distance between the Data table’s left and right edges.
+ [**X**](https://powerapps.microsoft.com/en-us/tutorials/properties-size-location/ "X") – The distance between the left edge of the Data table and the left edge of its parent container (or the left edge of the screen if there is no parent container).
+ [**Y**](https://powerapps.microsoft.com/en-us/tutorials/properties-size-location/ "Y") – The distance between the top edge of the Data table and the top edge of its parent container (or the top edge of the screen if there is no parent container).

## Related functions

+ [**Filter(DataSource, Formula)**](https://powerapps.microsoft.com/en-us/tutorials/function-filter-lookup/ "Filter(DataSource, Formula)")
+ [**Search(DataSource, SearchString, Column)**](https://powerapps.microsoft.com/en-us/tutorials/function-filter-lookup/ "Search(DataSource, SearchString, Column)")

## Examples
### Basic usage

1. Create a blank tablet app.
2. On the **Insert** tab, click or tap **Data table**.

	![Add a Data table control to a screen](Media/insertDataTable.png "Add a Data table control to a screen")
   
   	A **Data table** control is added to the screen.

3. Rename the **Data table** control **SalesOrderTable**, and resize it so that it covers the whole screen.
4. In the right pane, click or tap the data source icon to the right of the **No data source selected** text, and then click or tap **Add a data source**.

	![Add a data source](Media/addDataToDataTable.png "Add a data source")

5. In the list of connections, click or tap the connection for your Common Data Service database.

	![Select the connection for your data source](Media/chooseCDSDataTable.png "Select your data connection")

6. In the list of entities, click or tap **Sales order**, and then click or tap **Connect**.

  	![Select the Sales order entity](Media/chooseSODataTable.png "Select the Sales order entity")
   
	The **Data table** control is now attached to the **Sales order** data source. Several initial fields appear in the **Data table** control, because we are using a connector that supports that capability.

	![Data table](Media/preOrderDataTable.png "Data table")

7. In the right pane, click or tap the eye icon to show or hide individual fields. For example, click or tap the eye icon next to **CustomerPurchaseOrderReference** to hide this field.

8. In the right pane, reorder the fields by dragging them up or down.

	![Reorder the fields as desired](Media/fieldReorderDataTable.png "Reorder the fields")
  
  	The **SalesOrderTable** control shows the fields in the order that you specified.
  
	![Updated Data table](Media/postOrderDataTable.png "Updated Data table")

### Restyle the header for the Data table control

1. While the **Data table** control is selected, in the right pane, click or tap the **Advanced** tab.
2. Click or tap the field for the **HeadingFill** property, and then change the value to **RGBA(62,96,170,1)**.
3. Click or tap the field for the **HeadingColor** property, and then change the value to **White**.
4. Click or tap the field for the **HeadingSize** property, and then change the value to **14**.

	![Data table](Media/restyledDataTable.png "Data table")

### Connect a Data table control to another control

1. Add an **Edit** form control to the screen.
2. Resize the **Data table** and **Edit form** controls so that the **Data table** control appears in the left part of the screen and the **Edit form** control appears the right part of the screen.

	![Data table and Edit form on the same screen](Media/dataTableEmptyForm.png "Data table and Edit form on the same screen")

3. While **Form1** is selected, in the right pane, change the number of columns to **1**.
4. Connect **Form1** to the **Sales order** data source. Several initial fields appear in **Form1**.

	![Form1 with initial fields](Media/dataTableDisconnectedForm.png "Form1 with initial fields")

5. In the right pane, click or tap the **Advanced** tab.
6. Set the **Item** property for **Form1** to **SalesOrderTable.Selected**. **Form1** shows information from the row that is selected in the **Data table** control.

	![Edit form connected to the Data table](Media/connectedFormDataTable.png "Edit form connected to the Data table")
