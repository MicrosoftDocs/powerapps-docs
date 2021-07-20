---
title: RecordInfo function in Power Apps
description: Reference information including syntax and examples for the RecordInfo function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 07/18/2021
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# RecordInfo function in Power Apps
Provides information about a [record](../working-with-tables#elements-of-a-table) of a [data source](../working-with-data-sources.md).

Use **RecordInfo** to obtain information about a particular record of a data source, such as Dataverse, SharePoint, or SQL Server.  The data source must be tabular and compatible with the [**Remove**](function-remove-removeif.md) and [**Patch**](function-patch.md) functions.  The information available:

| Information argument | Description |
| --- | --- |
| **RecordInfo.DeletePermission** | Does the current user have permission to remove this record from the data source? |
| **RecordInfo.EditPermission** | Does the current user have permission to modify this record in the data source? |
| **RecordInfo.ReadPermission** | Does the current user have permission to read this record from the data source? |

**RecordInfo** returns a Boolean, *blank*, or an error:

| Return value | Description |
| --- | --- |
| *true* | The user has the permission. |
| *false* | The user does not have the permission. |
| *blank* | The function could not determine if the user has the permission.  The operation can still be attempted as permissions will be checked by the data source and an error displayed if it was not allowed. If the record is *blank* then **RecordInfo** **will also return *blank*. |  
| *error* | The function was called on a record that did not originate from a data source.  This includes records of collections and tables in variables.  Records from a data source can be placed into a variables or collection and then **RecordInfo** can be used. |

**RecordInfo** takes into account permissions at the data source level.  For example, if the user has permission at the record level to modify a record, but the user does not have permissions at the table level, then it will return *false* for **ModifyPermission**.

## Syntax
**RecordInfo**( *Record*, *Information* )

* *Record* – Required. The record to test.
* *Information* – Required. The desired information for the record.

## Examples

```powerapps-dot
RecordInfo( First(Accounts), RecordInfo.EditPermission )
```
Checks the edit permission for the first record in the `Accounts` data source, which could be in Dataverse, SharePoint, SQL Server, or another tabular data source.  If the user has permission to edit this record, and to modify the `Accounts` data source in general, then **RecordInfo** will return *true*.  

```powerapps-dot
With( { MyRecord: First( Accounts ) }, 
      RecordInfo( MyRecord, RecordInfo.EditPermission ) )
```
Captures a record using the [**With**](function-with.md) function and then passes this value to the RecordInfo function.  The result will be the same as the last example.

```powerapps-dot
Collect( MyAccounts, FirstN( Accounts, 10 ) );
RecordInfo( First( MyAccounts ), RecordInfo.EditPermission ) )
```
Captures the first 10 records from the `Accounts` data source into the `MyAccounts` collection.  Since the records originated from a data source, they can be used with the **RecordInfo** function.  The result will be the same as the last example.

```powerapps-dot
Collect( MyCollection, [ 1, 2, 3 ] );
RecordInfo( First(MyCollection), RecordInfo.DeletePermission )
```
Creates the `MyCollection` collection and tests the first record to determine if it can be removed.  Since the record's origin is a collection and not a data source, **RecordInfo** will return an error.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
