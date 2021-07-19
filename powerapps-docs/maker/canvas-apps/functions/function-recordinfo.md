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

Use **RecordInfo** to obtain information about a particular record of a data source:

| Information Argument | Result Type | Description |
| --- | --- | --- |
| **DataSourceInfo.RemovePermission** |Boolean |Does the current user have permission to remove this record from the data source? |
| **DataSourceInfo.ModifyPermission** |Boolean |Does the current user have permission to modify this record in the data source? |
| **DataSourceInfo.ReadPermission** |Boolean |Does the current user have permission to read this record from the data source? |

**RecordInfo** takes into account permissions at the data source level.  For example, if the user has permission at the record level to modify a record, but the user does not have permissions at the table level, then it will return *false* for **ModifyPermission**.

**RecordInfo** returns *blank* if it cannot determine whether the current user has the requested permission.  Permissions will be checked again by the server when the actual operation is carried out and an error is displayed if it was not allowed.

Calling **RecordInfo** on records of tables that are not from a data source will return an error.  This includes records of collections and tables in variables.  Records from a data source can be placed into a variables or collection and then **RecordInfo** can be used. 

## Syntax
**RecordInfo**( *Record*, *Information* )

* *Record* – Required. The record to test.
* *Information* – Required. The desired information for the record.

## Examples
These examples use the Accounts table in Dataverse.

```powerapps-dot
RecordInfo( First(Accounts), RecordInfo.EditPermission )
```
Checks the edit permission for the first record in the Accounts data source.  If the user has permission to edit this record, and to modify the Accounts data source in general, then **RecordInfo** will return *true*.  

```powerapps-dot
With( { MyRecord: First(Accounts) }, 
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
RecordInfo( First(MyCollection), RecordInfo.RemovePermission )
```
Creates the `MyCollection` collection and tests the first record to determine if it can be removed.  Since the record's origin is a collection and not a data source, **RecordInfo** will return an error.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
