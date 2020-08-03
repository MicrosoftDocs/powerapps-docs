---
title: Work with Dataflex table columns | Microsoft Docs
description: Explains how to create and use Dataflex table columns.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---

# Work with table columns

With the exception of the Customer field, all field types in Microsoft Dataflex Pro are available in Microsoft Dataflex as *columns*. This article covers the content you will need for working with table columns in Dataflex.

Notice that, the currency feature will always use the default currency for the country that was selected during Dataflex environment creation. This can’t be changed, and additional transaction currencies or exchange rates can’t be added. However, users can upgrade from Dataflex to Dataflex Pro. After upgrading, the full currency functionality will be available. 

For more information about the columns available, see these Dataflex Pro articles: 
- [Fields overview](../maker/common-data-service/fields-overview.md)
- [Create and edit global option sets overview](../maker/common-data-service/create-edit-global-option-sets.md)
- [Autonumber fields](../maker/common-data-service/autonumber-fields.md)
- [Set managed properties for fields](../maker/common-data-service/set-managed-properties-for-field.md)
- [Behavior and format of the Date and Time field](../maker/common-data-service/behavior-format-date-time-field.md)

## Create a column
1. On the **Build** tab, and then select **Tables**. 
2. Open the table you want to add a column to, and then select **Add column**.
    ![Create a table column](media/create-table-column.png)

The rest of the process to add and manage columns is the same as in Dataflex Pro, which is documented in these articles.
- [Create and edit fields for Common Data Service using Power Apps portal](../maker/common-data-service/create-edit-field-portal.md)
- [Manage custom fields in an entity](../maker/common-data-service/data-platform-manage-fields.md)

## Choice columns
In Dataflex, choices can only be created as a column within a table. Creation of choices is otherwise the same as creating an option set in Dataflex Pro. More information: [Create an Option set](../maker/common-data-service/custom-picklists.md)

## Calculated and Rollup Columns
Calculated columns and rollup columns available in Dataflex are equivalent to what is available in Dataflex Pro. More information: [Define calculated fields to automate manual calculations](../maker/common-data-service/define-calculated-fields.md) and [Define rollup fields that aggregate values](../maker/common-data-service/define-rollup-fields.md).


### See also
[Create a table](create-table.md)