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

By using **Patch**, you can modify the value in a [column](file-name.md) of a record in a data source without affecting the other columns of that record. In contrast, you can use the **[Update](function-update.md)** function to modify a record, but you must specify data for each column of that record.

You can also create a record in a data source by combining **Patch** with the **[Defaults](function-defaults.md)** function. For example, you can use this combination to build a single [screen](file-name) in which users can either modify or create a record. As an alternative, you can create a record by using the **[Collect](function-collect.md)** function.

If you use **Patch** to merge records outside of a data source, you specify two or more records to merge.
- If you specify a record that contains a column that no other records contain, the result contains that column with its original value.
- If you specify more than one record with the same column and the values don't match, the result contains the value in the record that's closest to the end of the [argument list](file-name.md).

**Note**: When you try to update a data source, problems such as these might occur:
- You might try to update a record at the same time as someone else.
- The data might not pass validation that the data source requires.
- You might not have permission to update that data source.

Use the **[Errors](function-errors.md)** function to test for and examine these types of issues, as [Working with Data Sources](file-name.md) describes.

## Description ##

### Modify a record in a data source ###

In the first argument, specify the data source that contains the record that you want to modify.

In the second argument, specify the [primary key](file-name.md) of the record that you want to modify.

In each subsequent argument, specify a column that you want to modify and the value that you want it to contain. If you specify the same column more than once, the result will contain the value that's closest to the end of the argument list.

**Patch** [returns](file-name.md) the modified record.

### Create a record in a data source ###

In the first argument, specify the data source in which you want to create a record.

In the second argument, use the **Defaults** function to create a record that contains the default values for the data source.

In each subsequent argument, specify any column or columns that you want to contain non-default values. If you specify the same column more than once, the result will contain the value that's closest to the end of the argument list.

**Patch** returns the new record, which might include a primary key that the data source generated automatically.

### Merge records outside of a data source ###

In each argument, specify a record that you want to merge. If the same column appears in more than one record, the result contains the value in the record that's closest to the end of the argument list.

**Patch** returns the merged record without any [side effects](file-name.md).

## Syntax ##

#### Modify a record in a data source ####

**Patch**( *DataSource*, *PrimaryKey*, *ChangeRecord1* [, *ChangeRecord2*, … ])

- *DataSource* – Required. The data source that contains the record that you want to modify.

- *PrimaryKey* – Required. The primary key of the record that you want to modify.

- *ChangeRecord1* – Required.  A change record to apply to the record that you want to modify.

- *ChangeRecord2*, ... – Optional. If you specify multiple change records that contain the same column, the result contains the value in the record that's closest to the end of the argument list.

#### Create a record in a data source ####

**Patch**( *DataSource*, **Defaults**(*DataSource*), *ChangeRecord1* [, *ChangeRecord2*, … ])

- *DataSource* – Optional. The data source in which to modify or create a record.

- *ChangeRecord1* – Required.  A change record to apply to the record that you want to create.

- *ChangeRecord2*, ... – Optional. If you specify multiple change records that contain the same column, the result contains the value in the record that's closest to the end of the argument list.

#### Merge records ####

**Patch**( *Record1*, *Record2*, … )

- *Record(s)* - Required.  At least two records that you want to merge. If you specify multiple records that contain the same column, the result contains the value in the record that's closest to the end of the argument list.

## Examples ##

#### Modify or create a record (in a data source) ###

In these examples, you'll modify or create a record in a data source that's named **IceCream**. The data source contains this data, and the ID column contains a primary key that the data source generates:

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
| **Patch(&nbsp;{&nbsp;Name:&nbsp;"James",&nbsp;Score:&nbsp;90&nbsp;}, {&nbsp;Name:&nbsp;"Jim",&nbsp;Passed:&nbsp;true&nbsp;} )** | Merges two records outside of a data source:<br><ul><li>The values in the **Name** column of each record don't match. The result contains the value in the second record (**Jim**) instead of the value in the first record (**James**).</li><li>The first record contains a column (**Score**) that doesn't exist in the second record. The result contains that column with its value (**90**).</li><li>The second record contains a column (**Passed**) that doesn't exist in the second record. The result contains that column with its value (**true**). | {&nbsp;Name:&nbsp;"Jim", Score:&nbsp;90, Passed:&nbsp;true&nbsp;} |
