<properties
	pageTitle="PowerApps: Clear, Collect, and ClearCollect functions"
	description="Reference information for the Clear, Collect, and ClearCollect functions in PowerApps, including syntax and examples"
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

# Clear, Collect, and ClearCollect functions in PowerApps #

Clears and/or adds to a [data source](working-with-data-sources.md).

## Description ##

### Clear ###

The **Clear** function clears all data from a data source.

You can use the **[Remove](function-remove.md)** function to selectively remove records.

**Clear** has no return value.  **Clear** can only be used in a [behavior](file-name.md) formula.

TODO: Clear for data source safety.

### Collect ###

The **Collect** function adds data to a data source.

Collect will create one or more new records in the data source.  The items to be added can be:

- A single value: The value is placed in the **Value** property of a new record.  All other properties are left blank.

- A [record](working-with-tables.md): Each named property is placed in the corresponding property of a new record.  All other properties are left blank.
  
- A [table](working-with-tables.md): Each record of the table is added as a separate record to the data source as described above.  The table is not added as whole to a record, to accomplish this wrap the table in a record first. 

When used with a [collection](working-with-data-sources.md#collections), additional columns will be created as needed.  This cannot be done for other data sources where the columns are set by the data storage.

If the data source does not already exist, a new [collection](working-with-data-sources.md#collections) is created.

You can also use the **[Patch](function-patch.md)** function to create records.

**Collect** returns the modified data source as a table.  **Collect** can only be used in a behavior formula.

### ClearCollect ###  

The **ClearCollect** function clears all data from a data source and then adds a different set of data to the same data source.  With a single function, **ClearCollect** offers the equivalent of **Clear** and then **Collect**.

**ClearCollect** returns the modified data source as a table.  **ClearCollect** can only be used in a behavior formula.

## Syntax ##

**Clear**( *DataSource* )

- *DataSource* – Required. The data source that you want to clear.

**Collect**( *DataSource*, *Item*, ... )

- *DataSource* – Required. The data source that you want to add data to.

- *Item(s)* - Required.  One or more items to add to the data source. 

**ClearCollect**( *DataSource*, *Item*, ... )

- *DataSource* – Required. The data source that you want to clear and then add data to.

- *Item(s)* - Required.  One or more items to add to the data source.  

## Examples ##

### Clearing and adding records to a data source ###

In these examples, you'll erase and add to a data source that's named **IceCream**. The ID column contains a primary key that the data source generates.  The data source begins with these contents:

| ID (automatically generated<br>primary key) | Flavor    | Quantity |
|-----|-----------|----------|
| 1   | Chocolate | 100      |
| 2   | Vanilla   | 200      |

We use the **ClearCollect** function to clear and then add records to **IceCream**:

| Formula | Description  | Result              |
|---------|--------------|---------------------|
| **ClearCollect( IceCream, {&nbsp;Flavor:&nbsp;"Strawberry",&nbsp;Quantity:&nbsp;300&nbsp;} ) **| This formula clears all data from the **IceCream** data source and then adds a record that includes a quantity of strawberry ice cream. | The value of the changed data source as a [table](working-with-tables.md) (see below).<br><br>The data source will also be modified. |

After the above formula has been evaluated, the **IceCream** data source contains:

| ID (automatically generated<br>primary key) | Flavor    | Quantity |
|-----|-----------|----------|
| 3   | Strawberry | 300      |

We then add another record to **IceCream** with a **Collect** function:

| Formula | Description  | Result              |
|---------|--------------|---------------------|
| **Collect( IceCream, {&nbsp;Flavor:&nbsp;"Pistachio",&nbsp;Quantity:&nbsp;40&nbsp;}, {&nbsp;Flavor:&nbsp;"Orange",&nbsp;Quantity:&nbsp;200&nbsp;}  ) **| This formula adds a record to the **IceCream** data source that includes a quantity of pistachio ice cream. | The value of the changed data source as a table (see below).<br><br>The data source will also be modified. |

After the above formula has been evaluated, the **IceCream** data source contains:

| ID (automatically generated<br>primary key) | Flavor    | Quantity |
|-----|-----------|----------|
| 3   | Strawberry | 300      |
| 4   | Pistachio | 40 |
| 5   | Orange | 200 |


### Step by step ###

<ol><li>Add a button, and set its **OnSelect** property to this function:<br>**Collect(Products, &quot;Europa&quot;, &quot;Ganymede&quot;, &quot;Callisto&quot;)**<br><br>This function creates a collection that's named **Products** and that contains a row for each of three product names.</li><br><li>Press F5, click the button, and then press Esc to return to the design workspace.</li><br><li>(optional) To display a preview of the collection that you created, click **Collections**  on the **Content** tab.</li></ol>
