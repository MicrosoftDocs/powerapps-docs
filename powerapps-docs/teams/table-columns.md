---
title: Work with Project Oakdale table columns | Microsoft Docs
description: Explains how to create and use Project Oakdale table columns.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---

# Work with table columns

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

With the exception of the Customer field, all field types in Common Data Service are available in Project Oakdale as *columns*. This article covers the content you'll need for working with table columns in Project Oakdale.

Notice that the currency feature will always use the default currency for the country that was selected during Project Oakdale environment creation. This can't be changed, and additional transaction currencies or exchange rates can't be added. However, you can upgrade from Project Oakdale to Common Data Service for full currency functionality.

For more information about the columns available, see these Common Data Service articles:

- [Fields overview](../maker/common-data-service/fields-overview.md)
- [Create and edit global option sets overview](../maker/common-data-service/create-edit-global-option-sets.md)
- [Autonumber fields](../maker/common-data-service/autonumber-fields.md)
- [Set managed properties for fields](../maker/common-data-service/set-managed-properties-for-field.md)
- [Behavior and format of the Date and Time field](../maker/common-data-service/behavior-format-date-time-field.md)

## Create a column

1. On the **Build** tab, select **See all**, and then expand **Tables**. 
2. Select the table you want to add a column to, and then select **Add column** on the command bar.
    > [!div class="mx-imgBorder"] 
    > ![Create a table column](media/create-table-column.png "Create a table column")

The rest of the process to add and manage columns is the same as in Common Data Service, which is documented in these articles:
- [Create and edit fields for Common Data Service using Power Apps portal](../maker/common-data-service/create-edit-field-portal.md)
- [Manage custom fields in an entity](../maker/common-data-service/data-platform-manage-fields.md)

## Choice columns

In Project Oakdale, choices can only be created as a column within a table. Creating choices is otherwise the same as creating an option set in Common Data Service. More information: [Create an Option set](../maker/common-data-service/custom-picklists.md)

## Calculated and rollup columns

The calculated columns and rollup columns that are available in Project Oakdale are equivalent to what's available in Common Data Service. More information: [Define calculated fields to automate manual calculations](../maker/common-data-service/define-calculated-fields.md) and [Define rollup fields that aggregate values](../maker/common-data-service/define-rollup-fields.md)

### See also

[Create a table](create-table.md)