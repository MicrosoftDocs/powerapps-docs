---
title: Delete or edit a table | Microsoft Docs
description: Explains how to delete or edit a table.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/03/2020
ms.author: nhelgren
ms.reviewer: matp
---

# Edit or delete a table

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

With Project Oakdale, you can perform the following types of operations on a table:

- Create table columns.
- Delete a table.
- Create, edit, and delete table relationships. More information: [Work with table relationships](relationships-table.md)

## Edit a table

In Microsoft Teams, you can edit four table properties:

- **Display name**: The name you want to display for the table.
- **Plural display name**: The plural of the table name, when needed for display.
- **Description**: A brief description of the purpose of the table.
- **Quick create settings**: This enables quick creation of records for client apps that support this feature.

> [!NOTE]
> - You can also edit a table using the visual editor. More information: [Create your first table](create-first-app.md#create-your-first-table)
> - Each Project Oakdale environment is assigned a prefix when it's created creation, such as **cr1a3**. The name for every table and column you create will be prefixed with this value. This value can't be changed.

1. On the left pane, expand **Tables**.
2. Open the table you want to edit, and then select **Settings** on the command bar to display the **Edit** table dialog box.  
    > [!div class="mx-imgBorder"] 
    > ![Edit table](media/edit-table1.png "Edit table")
    For more information about these settings, see [Create an entity](../maker/common-data-service/data-platform-create-entity.md#create-an-entity).
4. Make the changes you want, and then select **Done**.

## Delete a table

Anyone who's a member of the team can delete tables that aren't part of a managed solution.

In the **Tables** list, select **…** next to the table you want to delete, and then select **Delete table**. Alternatively, while viewing a table, select **Delete table** on the command bar.
<!-- >> [!div class="mx-imgBorder"] 
> ![Delete table](media/delete-table.png "Delete table")  -->

### See also

[Work with table relationships](relationships-table.md)