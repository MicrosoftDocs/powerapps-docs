---
title: DataSourceInfo function in Power Apps
description: Reference information including syntax and examples for the DataSourceInfo function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 03/12/2021
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
# DataSourceInfo function in Power Apps
Provides information about a [data source](../working-with-data-sources.md).

## Overview
Data sources can provide a wealth of information to optimize the user experience.

You can use [column](../working-with-tables.md#columns)-level information to validate user input and provide immediate feedback to the user before using the **[Patch](function-patch.md)** function. The **[Validate](function-validate.md)** function uses this same information.

You can use information at the data-source level, for example, to disable or hide **Edit** and **New** buttons for users who don't have permissions to edit and create [records](../working-with-tables.md#records).

Data sources vary in how much information they provide, including not providing any at all.  [Collections](../working-with-data-sources.md#collections) provide no information. If a piece of information isn't provided, a default is used, or *blank* is returned.

## Description
### Column information
You can use **DataSourceInfo** to obtain information about a particular column of a data source:  

| Information Argument | Result Type | Description |
| --- | --- | --- |
| **DataSourceInfo.DisplayName** |String |Display name for the column. If no display name is defined, returns the column name. |
| **DataSourceInfo.MaxLength** |Number |Maximum number of characters that the column can hold. Applies only to columns that contain strings. If a maximum isn't set, returns *blank*. |
| **DataSourceInfo.MaxValue** |Number |Maximum numeric value that a column can hold. Applies only to columns that contain numbers. If a maximum isn't set, returns *blank*. |
| **DataSourceInfo.MinValue** |Number |Minimum numeric value that a column can hold. Applies only to columns that contain numbers. If a minimum isn't set, returns *blank*. |
| **DataSourceInfo.Required** |Boolean |Is a value required for this column? If not set by the data source, returns **false**. |

The third argument is the name of a column as a string.  For example, column **Phone** in collection **People** would be passed as **"Phone"** including the double quotes.

### Data-source information
You can also use **DataSourceInfo** to obtain information about a data source as a whole:  

| Information Argument | Result Type | Description |
| --- | --- | --- |
| **DataSourceInfo.AllowedValues** |Boolean |What types of permissions can users be granted for this data source? If not set by the data source, returns *blank*. |
| **DataSourceInfo.CreatePermission** |Boolean |Does the current user have permission to create records in this data source? If not set by the data source, returns **true**. |
| **DataSourceInfo.DeletePermission** |Boolean |Does the current user have permission to delete records in this data source? If not set by the data source, returns **true**. |
| **DataSourceInfo.EditPermission** |Boolean |Does the current user have permission to edit records in this data source? If not set by the data source, returns **true**. |
| **DataSourceInfo.ReadPermission** |Boolean |Does the current user have permission to read records in this data source? If not set by the data source, returns **true**. |

> [!NOTE]
> **DataSourceInfo** returns *true* if it cannot determine whether the current user has the requested permission.  Permissions will be checked again by the server when the actual operation is carried out and an error is displayed if it was not allowed.

## Syntax
**DataSourceInfo**( *DataSource*, *Information*, *ColumnName* )

* *DataSource* – Required. The data source to use.
* *Information* – Required. The type of information that you want to retrieve.
* *ColumnName* – Optional. For column-level information, the column name as a string. Column **Phone** would be passed as **"Phone"**, including the double quotes. For information at the data-source level, the *ColumnName* argument can't be used.
  
    > [!NOTE]
  > For SharePoint and Excel data sources that contain column names with spaces, specify each space as **"\_x0020\_"**. For example, specify **"Column Name"** as **"Column_x0020_Name"**.

## Examples
The examples in this section use this data source, named **IceCream**:

![Icecream example.](media/function-datasourceinfo/icecream.png "Icecream example")

The data source has also provided this information:

* The display name for **Quantity** is "Quantity on Hand".
* The maximum length of **Flavor** is 30 characters.
* The **Flavor** column must contain a value. The **Quantity** column isn't required.
* The minimum **Quantity** is 0.
* The maximum **Quantity** is 100.
* The current user can read and edit the records of the **IceCream** data source but can't create or delete records.

| Formula | Description | Result |
| --- | --- | --- |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.DisplayName,&nbsp;"Quantity"&nbsp;)** |Returns the display name for the **Quantity** column of the **IceCream** data source. |"Quantity on Hand" |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.MaxLength,&nbsp;"Flavor"&nbsp;)** |Returns the maximum length of the string for the **Flavor** column of the **IceCream** data source. |30 |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.Required,&nbsp;"Flavor"&nbsp;)** |Is the **Flavor** column of the **IceCream** data source required? |**true** |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.Required,&nbsp;"Quantity"&nbsp;)** |Is the **Quantity** column of the **IceCream** data source required? |**false** |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.MaxValue,&nbsp;"Quantity"&nbsp;)** |Returns the maximum numeric value for the **Quantity** column of the **IceCream** data source. |100 |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.MinValue,&nbsp;"Quantity"&nbsp;)** |Returns the minimum numeric value for the **Quantity** column of the **IceCream** data source. |0 |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.ReadPermission)** |Can the current user read records in the **IceCream** data source? |**true** |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.EditPermission)** |Can the current user edit records in the **IceCream** data source? |**true** |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.CreatePermission)** |Can the current user create records in the **IceCream** data source? |**false** |
| **DataSourceInfo(&nbsp;IceCream, DataSourceInfo.DeletePermission)** |Can the current user delete records in the **IceCream** data source? |**false** |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
