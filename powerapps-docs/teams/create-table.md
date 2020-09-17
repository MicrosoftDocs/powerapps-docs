---
title: Create a table in Teams | Microsoft Docs
description: Explains how to create a Project Oakdale table.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/16/2020
ms.author: nhelgren
ms.reviewer: matp
---

# Create tables in Microsoft Teams

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

In Teams, data is defined by *tables*, which are the same as *[entities](/powerapps/maker/common-data-service/entity-overview)* in Common Data Service. To create a table, you must be a member of a team.

## Types of tables

Whereas Common Data Service has two types of entities that can be created (a standard entity with ownership defined and an activity entity), you can only create standard tables in Project Oakdale.

You define the type of table by selecting **More settings** when you create a table.

There are four different types of table ownership. When you create a table, the only options are **user**, **team owned**, or **organization-owned**, but you should be aware that other tables have different ownership types. More information: [Types of entities in Common Data Service](../maker/common-data-service/types-of-entities.md)

## Create a table

1. Sign in to Teams, and then select the link for **Power Apps**.
   > [!div class="mx-imgBorder"] 
   > ![Sign in to Power Apps](media/create-table1.png "Sign in to Power Apps")

2. Select the **Build** tab, and then select **See all**.
   > [!div class="mx-imgBorder"] 
   > ![The Build tab](media/create-table2.png "The Build tab")

3. Select **Tables** on the left pane, and then select **New table** on the command bar.
    > [!div class="mx-imgBorder"] 
    > ![New table menu option](media/create-table3.png "New table menu option")

4. In the **New table** pane, enter the following information. Required columns are designated with an asterisk (*) next to the column label.
    - **Display name**: The name of the table to be displayed. For example, **Product**.
    - **Plural display name**: The name used to reflect multiples of what the table contains. For example, **Products**.
    - **Name**: A unique internal name for the table. Unlike the display name, after it's saved this value can't be changed.
       > [!NOTE]
       > Each Project Oakdale environment is assigned a prefix when it's created, such as **cr628**. The name for every table and column you create will be prefixed with this value. This value can't be changed.
    - **More settings**: This area provides additional settings that are available. More information: [Create a custom entity](../maker/common-data-service/data-platform-create-entity.md).
    > [!div class="mx-imgBorder"] 
    > ![Column details](media/create-table4.png "Column details")

5. Select **Done**.

### See also

[Edit or delete a table](edit-delete-table.md)
