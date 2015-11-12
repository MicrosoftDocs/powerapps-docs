<properties
	pageTitle="PowerApps: Remove and RemoveIf functions"
	description="Reference information for the Remove and RemoveIf functions in PowerApps, including syntax and examples"
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
   ms.date="10/21/2015"
   ms.author="gregli"/>

# Remove and RemoveIf functions in PowerApps #

Removes [records](working-with-tables.md) from a [data source](working-with-data-sources.md).

## Description ##

### Remove function ###

Use the **Remove** function to remove specific records from a data source.  Records are matched based on their [primary key](working-with-data-sources.md) and other columns are ignored.

For [collections](working-with-data-sources.md) that do not have a primary key, the entire record must match.  You can use the **All** argument to remove all copies of a record, otherwise only one copy of the record is removed. 

### RemoveIf function ###

Use the **RemoveIf** function to remove records based on a set of conditions.  The conditions can be any PowerApps formula that results in a **true** or **false** and can reference columns of the data source by name.  Conditions are evaluated individually for each record, and if all result in **true**, the record is removed.

**Remove** and **RemoveIf** return the modified data source as a table.  Both functions can only be used in [behavior](file-name.md) formulas. 

You can also use the **[Clear](function-clear.md)** function to remove all of the records in a data source.

## Syntax ##

**Remove**( *DataSource*, *Record1* [, *Record2*, ... ] [, **All** ] )

- *DataSource* – Required. The data source that contains the records that you want to remove.

- *Record(s)* – Required. The records to remove.

- **All** – Optional. In a collection, the same record may appear more than once.  You can add the **All** argument on the end to remove all copies of the record.

**Remove**( *DataSource*, *Table* [, **All** ] )

- *DataSource* – Required. The data source that contains the records that you want to remove.

- *Table* – Required. A table of records to remove. 

- **All** – Optional. In a collection, the same record may appear more than once.  You can add the **All** argument to remove all copies of the record.

**RemoveIf**( *DataSource*, *Condition* [, ... ] )

- *DataSource* – Required. The data source that contains the records that you want to remove.

- *Condition(s)* – Required. A formula that evaluates to **true** for records to remove.  You can use column names from the *DataSource* in the formula.  If multiple *Conditions* are provided, all must evaluate to **true** for the records to be removed.

## Examples ##

#### Remove records from a data source ###

In these examples, you'll modify or create a record in a data source that's named **IceCream**. The ID column contains a primary key that the data source generates.  The data source begins with the data in this table:

| ID (automatically generated<br>primary key) | Flavor    | Quantity |
|-----|-----------|----------|
| 1   | Chocolate | 100      |
| 2   | Vanilla   | 200      |
| 3   | Strawberry | 300 |

| Formula | Description | Result |
|---------|-------------|--------|
| **Remove(&nbsp;IceCream,<br>{&nbsp;ID:&nbsp;1,&nbsp;Flavor:&nbsp;"Chcocolate",&nbsp;Quantity:100&nbsp;} )** | Removes a record from the data source based on the primary key.  Other columns are ignored. |<table><tr><th>ID</th><th>Flavor</th><th>Quantity</th></tr><tr><td>2</td><td>Vanilla</td><td>200</td></tr><tr><td>3</td><td>Strawberry</td><td>300</td></tr></table><br>The **IceCream** data source has been modified. |
| **Remove(&nbsp;IceCream,<br>{&nbsp;ID:&nbsp;1,&nbsp;Flavor:&nbsp;"Chcocolate",&nbsp;Quantity:100&nbsp;}, {&nbsp;ID:&nbsp;3,&nbsp;Flavor:&nbsp;"Strawberry",&nbsp;Quantity:300&nbsp;} )** | Removes two records from the data source based on the primary key.  Other columns are ignored. |<table><tr><th>ID</th><th>Flavor</th><th>Quantity</th></tr><tr><td>2</td><td>Vanilla</td><td>200</td></tr></table><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, Quantity > 150 )** | Removes records that have a **Quantity** that is greater than 150. |<table><tr><th>ID</th><th>Flavor</th><th>Quantity</th></tr><tr><td>1</td><td>Chocolate</td><td>100</td></tr></table><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, Quantity&bnsp;>&nbsp;150, Left(&nbsp;Flavor,&nbsp;1&nbsp;) = "S" )** | Removes records that have a **Quantity** that is greater than 150 and **Flavor** starts with an "S". |<table><tr><th>ID</th><th>Flavor</th><th>Quantity</th></tr><tr><td>1</td><td>Chocolate</td><td>100</td></tr><tr><td>2</td><td>Vanilla</td><td>200</td></tr></table><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, true )** | Removes all records from the data source. |<table><tr><th>ID</th><th>Flavor</th><th>Quantity</th></tr></table><br>The **IceCream** data source has been modified. |

### Step by step ###

<ol><li>Import or create a collection named **Inventory**, and show it in a gallery as [Show data in a gallery](show-images-text-gallery-sort-filter.md) describes.</li><br><li>In the gallery, set the **OnSelect** property of the image to this expression:<br>**Remove(Inventory, ThisItem)**</li><br><li>Press F5, and then click an image in the gallery.<br>The item is removed from the gallery and the collection.</li></ol>