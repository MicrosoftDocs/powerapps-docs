<properties
	pageTitle="PowerApps: Collect, Clear, and ClearCollect functions"
	description="Reference information for the Collect, Clear, and ClearCollect functions in PowerApps, including syntax and examples"
	services="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/01/2015"
   ms.author="gregli"/>

# Collect, Clear, and ClearCollect functions in PowerApps #

Creates and clears [collections](working-with-data-sources.md) and adds records to any [data source](working-with-data-sources.md).

## Description ##

### Collect ###

The **Collect** function adds records to a data source.  The items to be added can be:

- A single value: The value is placed in the **Value** property of a new record.  All other properties are left blank.

- A [record](working-with-tables.md): Each named property is placed in the corresponding property of a new record.  All other properties are left blank.
  
- A [table](working-with-tables.md): Each record of the table is added as a separate record of the data source as described above.  The table is not added as a nested table to a record.  To accomplish this, wrap the table in a record first. 

When used with a [collection](working-with-data-sources.md#collections), additional columns will be created as needed.  The columns for other data sources are fixed by the data source and new columns cannot be added.  

If the data source does not already exist, a new [collection](working-with-data-sources.md#collections) is created.

Collections are sometimes used to hold global variables or make a temporary copy of a data source.  PowerApps are based on formulas that automatically recalculate as the user interacts with an app.  Collections do not enjoy this benefit and their use can make your app harder to create and understand.  Before using a collection in this manner, review [working with variables](file-name.md).

You can also use the **[Patch](function-patch.md)** function to create records in a data source.

**Collect** returns the modified data source as a table.  **Collect** can only be used in a behavior formula.

### Clear ###

The **Clear** function deletes all the records of a collection.  The columns of the collection will remain.

Note that **Clear** only operates on collections and not other data sources.  You can use **[RemoveIf](function-remove-removeif.md)( *DataSource*, true )** for this purpose.  Use caution as this will remove all records from the data source's storage and can affect other users. 

You can use the **[Remove](function-remove.md)** function to selectively remove records.

**Clear** has no return value.  It can only be used in a [behavior](file-name.md) formula.

### ClearCollect ###

The **ClearCollect** function deletes all the records from a collection and then adds a different set of records to the same collection.  With a single function, **ClearCollect** offers the combination of **Clear** and then **Collect**.

**ClearCollect** returns the modified collection as a table.  **ClearCollect** can only be used in a behavior formula.

## Syntax ##

**Collect**( *DataSource*, *Item*, ... )

- *DataSource* – Required. The data source that you want to add data to.  If it does not already exist, a new collection is created.

- *Item(s)* - Required.  One or more items to add to the data source. 
 
**Clear**( *Collection* )

- *Collection* – Required. The collection that you want to clear.

**ClearCollect**( *Collection*, *Item*, ... )

- *Collection* – Required. The collection that you want to clear and then add data to.

- *Item(s)* - Required.  One or more items to add to the data source.  

## Examples ##

### Clearing and adding records to a data source ###

In these examples, you'll erase and add to a collection that's named **IceCream**. The ID column contains a property that the data source automatically generates.  The data source begins with these contents:

| ID (auto generated) | Flavor    | Quantity |
|-----|-----------|----------|
| 1   | Chocolate | 100      |
| 2   | Vanilla   | 200      |

We use the **ClearCollect** function to clear and then add records to **IceCream**:

| Formula | Description  | Result              |
|---------|--------------|---------------------|
| **ClearCollect( IceCream, {&nbsp;Flavor:&nbsp;"Strawberry",&nbsp;Quantity:&nbsp;300&nbsp;} )**| This formula clears all data from the **IceCream** data source and then adds a record that includes a quantity of strawberry ice cream. | The value of the changed data source as a [table](working-with-tables.md) (see below).<br><br>The data source will also be modified. |

After the above formula has been evaluated, the **IceCream** data source contains:

| ID (auto generated) | Flavor    | Quantity |
|-----|-----------|----------|
| 3   | Strawberry | 300      |

We then add another record to **IceCream** with a **Collect** function:

| Formula | Description  | Result              |
|---------|--------------|---------------------|
| **Collect( IceCream, {&nbsp;Flavor:&nbsp;"Pistachio",&nbsp;Quantity:&nbsp;40&nbsp;}, {&nbsp;Flavor:&nbsp;"Orange",&nbsp;Quantity:&nbsp;200&nbsp;}  ) **| This formula adds a record to the **IceCream** data source that includes a quantity of pistachio ice cream. | The value of the changed data source as a table (see below).<br><br>The data source will also be modified. |

After the above formula has been evaluated, the **IceCream** data source contains:

| ID (auto generated) | Flavor    | Quantity |
|-----|-----------|----------|
| 3   | Strawberry | 300      |
| 4   | Pistachio | 40 |
| 5   | Orange | 200 |


### Step by step ###

1. Add a button, and set its **OnSelect** property to this function:<br>**Collect(Products, &quot;Europa&quot;, &quot;Ganymede&quot;, &quot;Callisto&quot;)**

	This function creates a collection that's named **Products** that contains a row for each of three product names.

1. Press F5, click the button, and then press the Esc key to return to the design workspace.

1. (optional) To display a preview of the collection that you created, click **Collections**  on the **Content** tab.
