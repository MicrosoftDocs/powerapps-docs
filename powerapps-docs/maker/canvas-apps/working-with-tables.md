---
title: Understand tables and records in canvas apps
description: Reference information about working with tables, columns, and records in canvas apps.
author: gregli-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 07/07/2021
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - gregli-msft
---
# Understand tables and records in canvas apps

In Power Apps, you can create a canvas app that accesses information in Microsoft Excel, SharePoint, SQL Server, and several other sources that store data in records and tables. To work most effectively with this kind of data, review the concepts that underlie these structures.

* A record contains one or more categories of information about a person, a place, or a thing. For example, a record might contain the name, the email address, and the phone number of a single customer. Other tools refer to a record as a "row" or an "item."
* A table holds one or more records that contain the same categories of information. For example, a table might contain the names, the email addresses, and the phone numbers of 50 customers.

In your app, you'll use [formulas](working-with-formulas.md) to create, update, and manipulate records and tables. You'll probably read and write data to an external [data source](working-with-data-sources.md), which is an extended table. In addition, you might create one or more internal tables, which are called [collections](working-with-data-sources.md#collections).

You can build a variety of formulas that take the name of a table as an argument, just as a formula in Excel takes one or more cell references as arguments. Some formulas in Power Apps return a table that reflects the other arguments that you specify. For example, you might create a formula:

* to update a record in a table by specifying that table as one of multiple arguments for the **[Patch](functions/function-patch.md)** function
* to add, remove, and rename columns in a table by specifying that table as an argument for the **[AddColumns](functions/function-table-shaping.md)**, **[DropColumns](functions/function-table-shaping.md)**, or **[RenameColumns](functions/function-table-shaping.md)** function. None of those functions modifies the original table. Instead, the function returns another table based on the other arguments that you specify.

## Elements of a table
![Table elements.](media/working-with-tables/elements-of-a-table.png)

### Records
Each record contains at least one category of information for a person, a place, or a thing. The example above shows a record for each product (**Chocolate**, **Bread**, and **Water**) and a column for each category of information (**Price**, **Quantity on Hand**, and **Quantity on Order**).

In a formula, you can refer to a record by itself, outside of a table's context, by using curly braces. For example, this record **{ Name: "Strawberries", Price: 7.99 }** isn't associated with a table. Note that field names, such as **Name** and **Price** in that example, aren't enclosed in double quotation marks.

### Fields
A field is an individual piece of information in a record. You can visualize this sort of field as a value in a column for a particular record.

Just as with a control, you refer to a field of a record by using the **.** [operator](functions/operators.md) on the record.  For example, **First(Products).Name** returns the **Name** field for the first record in the **Products** table.

A field can contain another record or table, as the example for the **[GroupBy](functions/function-groupby.md)** function shows. You can nest as many levels of records and tables as you want.

### Columns
A column refers to the same field for one or more records in a table. In the above example, each product has a price field, and that price is in the same column for all products.  The above table has four columns, shown horizontally across the top:

* **Name**
* **Price**
* **Quantity on Hand**
* **Quantity on Order**

The column's name reflects the fields in that column.

All values within a column are of the same data type. In the above example, the "Quantity on Hand" column always contains a number and can't contain a string, such as "12 units," for one record.  The value of any field may also be *blank*.  

You may have referred to columns as "fields" in other tools.

> [!NOTE]
> For data sources such as SharePoint, Excel, or Power BI tiles that contain column names with spaces, Power Apps will replace the spaces with **"\_x0020\_"**. For example, **"Column Name"** in SharePoint, Excel, or Power BI tile will appear as **"Column_x0020_Name"** in Power Apps when displayed in the data layout or used in a formula.

### Table
A table comprises one or more records, each with multiple fields that have consistent names across the records.

Any table that's stored in a data source or a collection has a name, which you use to refer to the table and pass it to functions that take tables as arguments.  Tables can also be the result of a function or a formula.

As in the following example, you can express a table in a formula by using the **[Table](functions/function-table.md)** function with a set of records, which you express in curly braces:

`Table( { Value: "Strawberry" }, { Value: "Vanilla" } )`

You can also define a single-column table with square brackets.  An equivalent way to write the above:

`[ "Strawberry", "Vanilla" ]`

## Table formulas
In Excel and Power Apps, you use formulas to manipulate numbers and strings of text in similar ways:

* In Excel, type a value, such as **42**, in cell **A1**, and then type a formula, such as **A1+2**, in another cell to show the value of **44**.
* In Power Apps, set the **[Default](controls/properties-core.md)** property of **Slider1** to **42**, and set the **[Text](controls/properties-core.md)** property of a label to **Slider1.Value + 2** to show the value of **44**.

In both cases, the calculated value changes automatically if you change the values of the arguments (for example, the number in cell **A1** or the value of **Slider1**).

Similarly, you can use formulas to access and manipulate data in tables and records. You can use names of tables as arguments in some formulas, such as **Min(Catalog, Price)** to show the lowest value in the **Price** column of the **Catalog** table. Other formulas provide whole tables as return values, such as **RenameColumns(Catalog, "Price", "Cost")**, which returns all the records from the **Catalog** table but changes the name of the **Price** column to **Cost**.

Just as with numbers, formulas that involve tables and records are automatically recalculated as the underlying table or record changes. If the cost of a product in the **Catalog** table is lowered below the previous minimum, the return value of the **[Min](functions/function-aggregates.md)** formula will automatically change to match it.

Let's walk through some simple examples.

1. Create a blank app for a phone, and add a vertical **[Gallery](controls/control-gallery.md)** control that contains other controls.

    By default, the screen shows placeholder text from a table named **CustomGallerySample**. The **[Items](controls/properties-core.md)** property of the screen's **[Gallery](controls/control-gallery.md)** control is automatically set to that table.

    ![Gallery.](media/working-with-tables/gallery-items.png)

    > [!NOTE]
    > Some controls have been rearranged and enlarged for illustration purposes.

2. Instead of setting the **[Items](controls/properties-core.md)** property to the name of a table, set it to a formula that includes the name of the table as an argument, as in this example:

    `Sort(CustomGallerySample, SampleHeading, Descending)`

    This formula incorporates the **[Sort](functions/function-sort.md)** function, which takes the name of a table as its first argument and the name of a column in that table as its second argument. The function also supports an optional third argument, which stipulates that you want to sort the data in descending order.

    ![Sort for gallery.](media/working-with-tables/gallery-items-sort.png)

3. Set the **[Items](controls/properties-core.md)** property to a formula that takes the formula from the previous step as an argument and returns a table, as in this example:

    `FirstN(Sort(CustomGallerySample, SampleHeading, Descending), 2)`

    In this formula, you use the **[FirstN](functions/function-first-last.md)** function to show a particular number of records in a table. You use the **[Sort](functions/function-sort.md)** function as the first argument to **[FirstN](functions/function-first-last.md)** and a number (in this case, **2**) as the second argument, which specifies how many records to show.

    The entire formula returns a table that contains the first two records of the **CustomGallerySample** table, sorted by the **SampleHeading** column in descending order.

    ![FirstN for gallery.](media/working-with-tables/gallery-items-sort-firstn.png)

## Table functions and control properties

Consider the **Lower** function. If the variable **welcome** contains the text string **"Hello, World"**, the formula **Lower( welcome )** returns **"hello, world"**.  This function doesn't, in any way, change the value in that variable. **Lower** is a pure function in that it only processes input and produces output. That's all; it has no side effects. All functions in Excel and most functions in Power Apps are pure functions, which allow the workbook or the app to be recalculated automatically.

Power Apps offers a set of functions that operate on tables in the same manner. These functions take tables as input and filter, sort, transform, reduce, and summarize entire tables of data. In fact, **Lower** and many other functions that typically take a single value can also take a single-column table as input.

* **[Sort](functions/function-sort.md)**, **[Filter](functions/function-filter-lookup.md)** - Sorts and filters records.
* **[FirstN](functions/function-first-last.md)**, **[LastN](functions/function-first-last.md)** - Returns the first N or last N records of the table.
* **[Abs](functions/function-numericals.md)**, **[Sqrt](functions/function-numericals.md)**, **[Round](functions/function-round.md)**, **[RoundUp](functions/function-round.md)**, **[RoundDown](functions/function-round.md)** - Arithmetic operations on each record of a single-column table, resulting in a single-column table of results.
* **[Left](functions/function-left-mid-right.md)**, **[Mid](functions/function-left-mid-right.md)**, **[Right](functions/function-left-mid-right.md)**, **[Replace](functions/function-replace-substitute.md)**, **[Substitute](functions/function-replace-substitute.md)**, **[Trim](functions/function-trim.md)**, **[Lower](functions/function-lower-upper-proper.md)**, **[Upper](functions/function-lower-upper-proper.md)**, **[Proper](functions/function-lower-upper-proper.md)** - String manipulations on each record of a single-column table, resulting in a single-column table of strings.
* **[Len](functions/function-len.md)** - For a column of strings, returns a single-column table that contains the length of each string.
* **[Concatenate](functions/function-concatenate.md)** - Concatenates multiple columns of strings, resulting in a single-column table of strings.
* **[AddColumns](functions/function-table-shaping.md)**, **[DropColumns](functions/function-table-shaping.md)**, **[RenameColumns](functions/function-table-shaping.md)**, **[ShowColumns](functions/function-table-shaping.md)** - Column manipulation of the table, resulting in a new table with different columns.
* **[Distinct](functions/function-distinct.md)** - Removes duplicates records.
* **[Shuffle](functions/function-shuffle.md)** - Shuffles records into a random order.
* **[HashTags](functions/function-hashtags.md)** - Searches for hashtags in a string.
* **[Errors](functions/function-errors.md)** - Provides error information when you work with a data source.

Many of these functions take a single-column table as their input. If an entire table has only one column, you can specify it by name. If a table has multiple columns, you can specify one of those columns by using *Table.Column* syntax. For example, **Products.Name** returns the single-column table of only **Name** values from the **Products** table.

You can completely reshape a table however you want by using the **[AddColumns](functions/function-table-shaping.md)**, **[RenameColumns](functions/function-table-shaping.md)**, **[ShowColumns](functions/function-table-shaping.md)**, or **[DropColumns](functions/function-table-shaping.md)** function. Again, these functions change only their output, not their source.

Properties of controls can also be tables:

* **Items** - Applies to galleries, list boxes, and combo boxes. This property defines the table that the gallery or the list shows.
* **SelectedItems** - Applies to list boxes and combo boxes. This property defines the table of items that the user has selected if **SelectMultiple** is enabled.

## Behavioral formulas

Other functions are specifically designed to modify data and have side effects. Because these functions aren't pure, you must build them carefully, and they can't participate in automatically recalculating values in the app. You can use these functions only within [behavioral formulas](working-with-formulas-in-depth.md).

* **[Collect](functions/function-clear-collect-clearcollect.md)**, **[Clear](functions/function-clear-collect-clearcollect.md)**, **[ClearCollect](functions/function-clear-collect-clearcollect.md)** - Creates collections, clears them, and adds data to them.
* **[Patch](functions/function-patch.md)** - Modifies one or more fields in a record.
* **[Update](functions/function-update-updateif.md)**, **[UpdateIf](functions/function-update-updateif.md)** - Updates records that match one or more criteria that you specify.
* **[Remove](functions/function-remove-removeif.md)**, **[RemoveIf](functions/function-remove-removeif.md)** - Deletes records that match one or more criteria that you specify.

## Record formulas

You can also build a formula that calculates data for an individual record, takes an individual record as an argument, and provides an individual record as a return value. Returning to our gallery example above, let's use the **Gallery1.Selected** property to display information from whatever record the user selects in that gallery.

1. Add a [**Button**](controls/control-button.md), and set its **[OnSelect](controls/properties-core.md)** property to this formula:<br>
    **Collect( SelectedRecord, Gallery1.Selected )**

2. While holding down the Alt key, select the button.

3. In the **File** menu, select **Collections.**

    ![SelectedRecord collection.](media/working-with-tables/selected-collection.png)

This formula returns a record that includes not only the data from the record that's currently selected in the gallery but also each control in that gallery. For example, the record contains both a **SampleText** column, which matches the **SampleText** column in the original table, and a **Subtitle1** column, which represents the label that shows the data from that column. Select the table icon in the **Subtitle1** column to drill into that data.

> [!NOTE]
> The **Subtitle1** column might be named **Subtitle2** or similar if you've added elements other than those that this topic specifies.

Now that you have the selected record, you can extract individual fields from it with the **.** operator.

1. Add a **[Label](controls/control-text-box.md)** control, and then move it under the gallery and the button.

1. Set the label's **[Text](controls/properties-core.md)** property to this expression:<br>
    **"Selected: " & Gallery1.Selected.SampleHeading**

    ![Text property with updated label.](media/working-with-tables/gallery-selected.png)

You've taken the **Selected** property, which is a record, and extracted the **SampleHeading** property from it.

You can also use a record as a general-purpose container for related named values.

* If you build a formula around the **[UpdateContext](functions/function-updatecontext.md)** and **[Navigate](functions/function-navigate.md)** functions, use a record to gather the [context variables](working-with-variables.md#use-a-context-variable) that you want to update.
* Use the **[Updates](controls/control-form-detail.md)** property on an **[Edit form](controls/control-form-detail.md)** control to gather the changes that have been made by the user in a form.
* Use the **[Patch](functions/function-patch.md)** function to update a data source but also to merge records.

In these cases, the record was never a part of a table.

## Record functions and control properties
Functions that return records:

* **[FirstN](functions/function-first-last.md)**, **[LastN](functions/function-first-last.md)** - Returns the first or last record or records of the table.
* **[Lookup](functions/function-filter-lookup.md)** - Returns the first record from a table that matches one or more criteria.
* **[Patch](functions/function-patch.md)** - Updates a data source or merges records.
* **[Defaults](functions/function-defaults.md)** - Returns the default values for a data source.

Properties that return records:

* **Selected** - Applies to galleries and list boxes. Returns the currently selected record.
* **Updates** - Applies to galleries.  Pulls together all the changes that a user makes in a data-entry form.
* **[Update](functions/function-update-updateif.md)** - Applies to input controls such as text-input controls and sliders. Sets up individual properties for the gallery to pull together.

## Record scope

Some functions operate by evaluating a formula across all the records of a table individually. The formula's result is used in various ways:

* **AddColumns** - Formula provides the value of the added field.
* **Average**, **Max**, **Min**, **Sum**, **StdevP**, **VarP** - Formula provides the value to aggregate.
* **Filter**, **Lookup** - Formula determines if the record should be included in the output.
* **Concat** - Formula determines the strings to concatenate together.
* **Distinct** - Formula returns a value, used to identify duplicate records.
* **ForAll** - Formula can return any value, potentially with side effects.
* **Sort** - Formula provides the value to sort the records on.
* **With** - Formula can return any value, potentially with side effects.

Inside these formulas, you can reference the fields of the record being processed. Each of these functions creates a "record scope" in which the formula is evaluated, where the fields of the record are available as top-level identifiers. You can also reference control properties and other values from throughout your app.

For example, take a table of **Products**:

![Products example.](media/working-with-tables/requested.png)

To create this example table in your app, insert a button, set its **OnSelect** property to this formula, and then select the button (click it while you hold down the Alt key in Power Apps Studio):

```powerapps-dot
Set( Products,
    Table(
        { Product: "Widget",    'Quantity Requested': 6,  'Quantity Available': 3 },
        { Product: "Gadget",    'Quantity Requested': 10, 'Quantity Available': 20 },
        { Product: "Gizmo",     'Quantity Requested': 4,  'Quantity Available': 11 },
        { Product: "Apparatus", 'Quantity Requested': 7,  'Quantity Available': 6 }
    )
)
```

To determine whether any of any of these products had more requested than is available:

`Filter( Products, 'Quantity Requested' > 'Quantity Available' )`

The first argument to **Filter** is the table of records to operate on, and the second argument is a formula.  **Filter** creates a record scope for evaluating this formula in which the fields of each record are available, in this case **Product**, **Quantity Requested**, and **Quantity Available**.  The result of the comparison determines if each record should be included in the result of the function:

![Filtered table.](media/working-with-tables/needed.png)

Adding to this example, we can calculate how much of each product to order:

```powerapps-dot
AddColumns( 
    Filter( Products, 'Quantity Requested' > 'Quantity Available' ), 
    "Quantity To Order", 'Quantity Requested' - 'Quantity Available'
)
```

Here we are adding a calculated column to the result. **AddColumns** has its own record scope that it uses to calculate the difference between what has been requested and what is available.

![Added columns.](media/working-with-tables/toorder.png)

Finally, we can reduce the result table to just the columns that we want:

```powerapps-dot
ShowColumns(
    AddColumns(
        Filter( Products, 'Quantity Requested' > 'Quantity Available' ),
        "Quantity To Order", 'Quantity Requested' - 'Quantity Available'
    ),
    "Product",
    "Quantity To Order"
)
```

![Updated table.](media/working-with-tables/toorderonly.png)

Note that in the above, we used double quotes (") in some places and single quotes (') in other places.  Single quotes are required when referencing the value of an object, such as a field or table, in which the name of the object contains a space.  Double quotes are used when we are not referencing the value of an object but instead talking about it, especially in situations in which the object does not yet exist, as in the case of **AddColumns**.

## Disambiguation

Field names added with the record scope override the same names from elsewhere in the app.  When this happens, you can still access values from outside the record scope with the [**@** disambiguation](functions/operators.md) operator:

* To access values from nested record scopes, use the **@** operator with the name of the table being operated upon using this pattern:<br>_Table_**[@**_FieldName_**]**
* To access global values, such as data sources, collections, and context variables, use the pattern **[@**_ObjectName_**]** (without a table designation).

If the table being operated upon is an expression, such as **Filter(** _Table_**,** ... **)**, then the disambiguation operator cannot be used.  Only the innermost record scope can access fields from this table expression, by not using the disambiguation operator.

For example, imagine having a collection **X**:

![Collection X.](media/working-with-tables/X.png)

You can create this collection with **ClearCollect( X, \[1, 2\] )**.

And another collection **Y**:

![Collection Y.](media/working-with-tables/Y.png)

You can create this collection with **ClearCollect( Y, ["A", "B"] )**.

In addition, define a context variable named **Value** with this formula: **UpdateContext( {Value: "!"} )**

Let's put it all together. In this context, the following formula:

```powerapps-dot
Ungroup(
    ForAll( X,
        ForAll( Y,
            Y[@Value] & Text( X[@Value] ) & [@Value]
        )
    ),
    "Value"
)
```

produces this table:

![XY table.](media/working-with-tables/XY.png)

What is going on here?  The outermost **ForAll** function defines a record scope for **X**, allowing access to the **Value** field of each record as it is processed.  It can be accessed by simply using the word **Value** or by using **X[@Value]**.

The innermost **ForAll** function defines another record scope for **Y**.  Since this table also has a **Value** field defined, using **Value** here refers to the field in **Y**'s record and no longer the one from **X**.  Here, to access **X**'s **Value** field, we must use the longer version with the disambiguation operator.

Since **Y** is the innermost record scope, accessing fields of this table do not require disambiguation, allowing us to use this formula with the same result:

```powerapps-dot
Ungroup(
    ForAll( X,
        ForAll( Y,
            Value & Text( X[@Value] ) & [@Value]
        )
    ),
    "Value"
)
```

All the **ForAll** record scopes override the global scope. The **Value** context variable we defined isn't available by name without the disambiguation operator. To access this value, use **[@Value]**.

**Ungroup** flattens the result because nested **ForAll** functions result in a nested result table.

## Single-column tables

To operate on a single column from a table, use the **ShowColumns** function as in this example:

```powerapps-dot
ShowColumns( Products, "Product" )
```

This formula produces this single-column table:

![Single column table.](media/working-with-tables/single-column.png)

For a shorter alternative, specify *Table.Column*, which extracts the single-column table of just *Column* from *Table*. For example, this formula produces exactly the same result as using **ShowColumns**.

```powerapps-dot
Products.Product
```

## Inline records

You express records by using curly braces that contain named field values.  For example, you can express the first record in the table at the start of this topic by using this formula:

`{ Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quantity on Order': 10 }`

You can also embed formulas within other formulas, as this example shows:

`{ Name: First(Products).Name, Price: First(Products).Price * 1.095 }`

You can nest records by nesting curly braces, as this example shows:

`{ 'Quantity': { 'OnHand': ThisItem.QuantOnHand, 'OnOrder': ThisItem.QuantOnOrder } }`

Enclose each column name that contains a special character, such as a space or a colon, in single quotes.  To use a single quote within a column name, double it.

Note that the value in the **Price** column doesn't include a currency symbol, such as a dollar sign. That formatting will be applied when the value is displayed.  

## Inline tables
You can create a table by using the **[Table](functions/function-table.md)** function and a set of records. You can express the table at the start of this topic by using this formula:

```powerapps-dot
Table( 
	{ Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quantity on Order': 10 },
	{ Name: "Bread", Price: 4.95, 'Quantity on Hand': 34, 'Quantity on Order': 0 },
	{ Name: "Water", Price: 4.95, 'Quantity on Hand': 10, 'Quantity on Order': 0 } 
)
```

You can also nest tables:

```powerapps-dot
Table( 
	{ Name: "Chocolate", 
	  'Quantity History': Table( { Quarter: "Q1", OnHand: 10, OnOrder: 10 },
	                             { Quarter: "Q2", OnHand: 18, OnOrder: 0 } ) 
	}
)
```

## Inline value tables
You can create single-column tables by specifying values in square brackets. The resulting table has a single column, named **Value**.

For example, `[ 1, 2, 3, 4 ]` is equivalent to `Table( { Value: 1 }, { Value: 2 }, { Value: 3 }, { Value: 4 } )` and returns this table:

![Inline table.](media/working-with-tables/inline-table.png)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]