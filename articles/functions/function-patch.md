<properties
	pageTitle="PowerApps: Patch function"
	description="Reference information for the Patch function in PowerApps, including syntax and examples"
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

# Patch function in PowerApps #

Modifies or creates a [record](file-name.md) in a [data source](file-name.md), or merges records outside of a data source.

## Overview ##

In a data source, you can use the **Patch** function to modify the value of a [column](file-name.md) in a record without affecting the other columns in that record. In contrast, you can use the **[Update](function-update.md)** function to modify a record, but you must specify a value for each column of that record.

You can also create a record in a data source by combining **Patch** with the **[Defaults](function-defaults.md)** function. As a result, you can build a single [screen](file-name.md) in which users can either modify or create a record. You can also create a record by using the **[Collect](function-collect.md)** function.

Even if you're not updating a data source, you can use **Patch** to merge two or more records.

## Description ##

### Modify or create a record in a data source ###

To use this function with a data source, specify it first, and then do either of the following:

- Specify the name of the data source's [primary-key](file-name.md) column and the value in that column for the record that you want to modify.

- Use the **[Defaults]** function to create a record that contains the default values for the data source that you specified.

Then specify one or more change records, which contain the name of at least one column in the data source and a value for that column. The value in each column of a change record takes priority over the value in the same column of the record that you're modifying/creating or of the previous change record.

The [return value](file-name.md) of **Patch** contains the value of each column as specified in the record that's closest to the end of the [argument list](file-name.md). If you created a record, the return value might also include a primary key that the was generated automatically from the data source.

**Note**: When you try to update a data source, problems such as these might occur:
- You might try to update a record at the same time as someone else.
- The data might not pass validation that the data source requires.
- You might not have permission to update that data source.

Use the **[Errors](function-errors.md)** function to test for and examine these types of issues, as [Working with Data Sources](file-name.md) describes.

### Merge records outside of a data source ###

Specify two or more records that you want to merge. If the same column appears in more than one record, the return value contains the value in the record that's closest to the end of the argument list.

**Patch** returns the merged record without any [side effects](file-name.md).

## Syntax ##

#### Modify or create a record in a data source ####

**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord1* [, *ChangeRecord2*, … ])

- *DataSource* – Required. The data source that contains the record that you want to modify or create.

- *BaseRecord* – Required. A record that contains the name of at least one column in the data source and a value for that column. If you want to modify a record, include the name of the primary-key column and the value in that column for the record that you want to modify. Otherwise, **Patch** creates a record that contains any columns and values that you specify in this argument. For example, you can use **Defaults** to create a record that contains the default values for the data source.

- *ChangeRecord1* – Required.  A record that contains the name of at least one column in the data source and a value for that column. If any column names match a column name in the *BaseRecord*, the value of that column in this argument takes priority.

- *ChangeRecord2*, ... – Optional. If you specify multiple change records that contain the same column, the return value contains the value in the record that's closest to the end of the argument list.

#### Merge records ####

**Patch**( *Record1*, *Record2*, … )

- *Record(s)* - Required.  At least two records that you want to merge. The return value contains every column in any record. If you specify multiple records that contain the same column, the return value contains the value in the record that's closest to the end of the argument list.

## Examples ##

#### Modify or create a record (in a data source) ###

In these examples, you'll modify or create a record in a data source that's named **IceCream**. The data source contains the data in this table, and the ID column contains a primary key that the data source generates:

| ID  | Flavor    | Quantity |
|-----|-----------|----------|
| 1   | Chocolate | 100      |
| 2   | Vanilla   | 200      |

| Formula | Description | Result |
|---------|-------------|--------|
| **Patch(&nbsp;IceCream,<br>{&nbsp;ID:&nbsp;1&nbsp;}, {&nbsp;Quantity:&nbsp;400&nbsp;} )** | Modifies a record in the **IceCream** data source:<ul><li> The **ID** column of the record to modify contains the value of **1**. (The Chocolate record has that ID.)</li><li>The value in the **Quantity** column changes to **400**. | {&nbsp;ID:&nbsp;1, Flavor:&nbsp;"Chocolate", Quantity:&nbsp;400 } |
| **Patch( IceCream, Defaults(&nbsp;IceCream ), {&nbsp;Flavor:&nbsp;“Strawberry”&nbsp;}&nbsp;)** | Creates a record in the **IceCream** data source:<ul><li>The ID column contains a value that the data source generates automatically (3).</li><li>The Quantity column contains the default value (0) for that column in the **IceCream** data source, as the **Defaults** function specifies.<li>The **Flavor** column contains the value of **Strawberry**.</li> | { ID:&nbsp;3, Flavor:&nbsp;“Strawberry”, Quantity:&nbsp;0&nbsp;} |

#### Merge records (outside of a data source) ####

| Formula | Description | Result |
|---------|-------------|--------|
|**Patch(&nbsp;{&nbsp;Name:&nbsp;"James",&nbsp;Score:&nbsp;90&nbsp;}, {&nbsp;Name:&nbsp;"Jim",&nbsp;Passed:&nbsp;true&nbsp;} )** | Merges two records outside of a data source:<br><ul><li>The values in the **Name** column of each record don't match. The result contains the value (**Jim**) in the record that's closer to the end of the argument list instead of the value (**James**) in the record that's closer to the start.</li><li>The first record contains a column (**Score**) that doesn't exist in the second record. The result contains that column with its value (**90**).</li><li>The second record contains a column (**Passed**) that doesn't exist in the first record. The result contains that column with its value (**true**). | {&nbsp;Name:&nbsp;"Jim", Score:&nbsp;90, Passed:&nbsp;true&nbsp;} |
