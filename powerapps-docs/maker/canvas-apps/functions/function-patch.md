---
title: Patch function | Microsoft Docs
description: Reference information, including syntax and examples, for the Patch function in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/21/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Patch function in PowerApps
Modifies or creates one or more [records](../working-with-tables.md#records) in a [data source](../working-with-data-sources.md), or merges records outside of a data source.

Use the **Patch** function to modify records in complex situations, such as when you perform updates that require no user interaction or use forms that span multiple screens.

In less complex situations, you can use the **Edit form** control to update records in a data source more easily. When you add an **Edit form** control, you provide users with a form to fill in and then save the changes to a data source. For more information, see [Understand data forms](../working-with-forms.md).

## Overview
Use the **Patch** function to modify one or more records of a data source.  The values of specific [fields](../working-with-tables.md#elements-of-a-table) are modified without affecting other properties. For example, this formula changes the phone number for a customer named Contoso:

`Patch( Customers, First( Filter( Customers, Name = "Contoso" ) ), { Phone: “1-212-555-1234” } )`

Use **Patch** with the **[Defaults](function-defaults.md)** function to create records. Use this behavior to build a [single screen](../working-with-data-sources.md) for both creating and editing records. For example, this formula creates a record for a customer named Contoso:

`Patch( Customers, Defaults( Customer ), { Name: “Contoso” } )`

Even if you're not working with a data source, you can use **Patch** to merge two or more records. For example, this formula merges two records into one that identifies both the phone number and the location for Contoso:

`Patch( { Name: "Contoso", Phone: “1-212-555-1234” }, { Name: "Contoso", Location: “Midtown”  } )`

## Description
### Modify or create a record in a data source
To use this function with a data source, specify the data source, and then specify a base record:

* To modify a record, the base record needs to have come from a data source.  The base record may have come through a gallery's **[Items](../controls/properties-core.md)** property, been placed in a [context variable](../working-with-variables.md#create-a-context-variable), or come through some other path. But you should be able to trace the base record back to the data source.  This is important as the record will include additional information to help find the record again for modification.  
* To create a record, use the **[Defaults](function-defaults.md)** function to create a base record with default values.  

Then specify one or more change records, each of which contains new property values that override property values in the base record. Change records are processed in order from the beginning of the argument list to the end, with later property values overriding earlier ones.

The return value of **Patch** is the record that you modified or created.  If you created a record, the return value may include properties that the data source generated automatically.

When you update a data source, one or more issues may arise. Use the **[Errors](function-errors.md)** function to identify and examine issues, as [Working with Data Sources](../working-with-data-sources.md) describes.

Related functions include the **[Update](function-update-updateif.md)** function, which you can use to replace an entire record, and the **[Collect](function-clear-collect-clearcollect.md)** function, which you can use to create a record.  You can use the **[UpdateIf](function-update-updateif.md)** function to modify specific properties of multiple records based on a condition.

### Modify or create a set of records in a data source
**Patch** can also be used to create or modify multiple records with a single call.

Instead of passing a single base record, a table of base records can be provided in the second argument.  Change records are provided in a table as well, corresponding one-for-one with the base records.  The number of records in each change table must be the same as the number of records in the base table.

When using **Patch** in this manner, the return value is also a table with each record corresponding one-for-one with the base and change records.

### Merge records outside of a data source
Specify two or more records that you want to merge. Records are processed in order from the beginning of the argument list to the end, with later property values overriding earlier ones.

**Patch** returns the merged record and doesn't modify its arguments or records in any data sources.

## Syntax
#### Modify or create a record in a data source
**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord1* [, *ChangeRecord2*, … ])

* *DataSource* – Required. The data source that contains the record that you want to modify or will contain the record that you want to create.
* *BaseRecord* – Required. The record to modify or create.  If the record came from a data source, the record is found and modified. If the result of **[Defaults](function-defaults.md)** is used, a record is created.
* *ChangeRecord(s)* – Required.  One or more records that contain properties to modify in the *BaseRecord*.  Change records are processed in order from the beginning of the argument list to the end, with later property values overriding earlier ones.

#### Modify or create a set of records in a data source
**Patch**( *DataSource*, *BaseRecordsTable*, *ChageRecordTable1* [, *ChangeRecordTable2*, … ] )

* *DataSource* – Required. The data source that contains the records that you want to modify or will contain the records that you want to create.
* *BaseRecordTable* – Required. A table of records to modify or create.  If the record came from a data source, the record is found and modified. If the result of **[Defaults](function-defaults.md)** is used, a record is created.
* *ChangeRecordTable(s)* – Required.  One or more tables of records that contain properties to modify for each record of the *BaseRecordTable*.  Change records are processed in order from the beginning of the argument list to the end, with later property values overriding earlier ones.

#### Merge records
**Patch**( *Record1*, *Record2* [, …] )

* *Record(s)* - Required.  At least two records that you want to merge. Records are processed in order from the beginning of the argument list to the end, with later property values overriding earlier ones.

## Examples
#### Modify or create a record (in a data source)
In these examples, you'll modify or create a record in a data source, named **IceCream**, that contains the data in this [table](../working-with-tables.md) and automatically generates the values in the **ID** [column](../working-with-tables.md#columns):

![](media/function-patch/icecream.png)

| Formula | Description | Result |
| --- | --- | --- |
| **Patch(&nbsp;IceCream,<br>First( Filter( IceCream, Flavor = "Chocolate" ) ), {&nbsp;Quantity:&nbsp;400&nbsp;} )** |Modifies a record in the **IceCream** data source:<ul><li> The **ID** column of the record to modify contains the value of **1**. (The **Chocolate** record has that ID.)</li><li>The value in the **Quantity** column changes to **400**. |{&nbsp;ID:&nbsp;1, Flavor:&nbsp;"Chocolate", Quantity:&nbsp;400 }<br><br>The **Chocolate** entry in the **IceCream** data source has been modified. |
| **Patch( IceCream, Defaults(&nbsp;IceCream ), {&nbsp;Flavor:&nbsp;“Strawberry”&nbsp;}&nbsp;)** |Creates a record in the **IceCream** data source:<ul><li>The **ID** column contains the value **3**, which the data source generates automatically.</li><li>The **Quantity** column contains **0**, which is the default value for that column in the **IceCream** data source, as the **[Defaults](function-defaults.md)** function specifies.<li>The **Flavor** column contains the value of **Strawberry**.</li> |{ ID:&nbsp;3, Flavor:&nbsp;“Strawberry”, Quantity:&nbsp;0&nbsp;}<br><br>The **Strawberry** entry in the **IceCream** data source has been created. |

After the previous formulas have been evaluated, the data source ends with these values:

![](media/function-patch/icecream-after.png)

#### Merge records (outside of a data source)

| Formula | Description | Result |
| --- | --- | --- |
| **Patch(&nbsp;{&nbsp;Name:&nbsp;"James",&nbsp;Score:&nbsp;90&nbsp;}, {&nbsp;Name:&nbsp;"Jim",&nbsp;Passed:&nbsp;true&nbsp;} )** |Merges two records outside of a data source:<br><ul><li>The values in the **Name** column of each record don't match. The result contains the value (**Jim**) in the record that's closer to the end of the argument list instead of the value (**James**) in the record that's closer to the start.</li><li>The first record contains a column (**Score**) that doesn't exist in the second record. The result contains that column with its value (**90**).</li><li>The second record contains a column (**Passed**) that doesn't exist in the first record. The result contains that column with its value (**true**). |{&nbsp;Name:&nbsp;"Jim", Score:&nbsp;90, Passed:&nbsp;true&nbsp;} |

