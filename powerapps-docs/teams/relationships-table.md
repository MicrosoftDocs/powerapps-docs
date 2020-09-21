---
title: Table relationships in Project Oakdale | Microsoft Docs
description: Explains how to create and use table relationships in in Project Oakdale.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/22/2020
ms.author: nhelgren
ms.reviewer: matp
---

# Work with table relationships

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Table relationships define the ways that table records can be associated with records from other tables or the same table. There are three types of table relationships. Project Oakdale allows for the creation of the same relationship types as Common Data Service does:

- **One-to-many relationships**. In this type of relationship, each row in table A can match more than one row in table B, but each row in table B can match only one row in table A. For example, a class of students have a single classroom.

- **Many-to-one relationships**. In this type of relationship, each row in table B can match more than one row in table A, but each row in table A can match only one row in table B. For example, one single teacher teaches many classes.

- **Many-to-many relationships**. In this type of relationship, each row in table A can match more than one row in table B, and vice versa. For example, students attend many classes, and each class can have multiple students.

More information: [Entity relationships](../maker/common-data-service/create-edit-entity-relationships.md)

## Create a table relationship

To add a lookup relation to a table, create a relation on the **Relationships** tab and specify the table with which you want to create a relationship.

1. In the **Power Apps** section of Microsoft Teams, select the table to create a relationship. This can be done by opening the table and selecting the **Relationships** tab.

   > [!div class="mx-imgBorder"] 
   > ![Relationships tab](media/create-relate-table.png "Relationships tab") 

   Or, on the left pane, expand **Tables**, expand the table you want, and then select **Relationships**. <br />

 <!--   > [!div class="mx-imgBorder"] 
    > ![Create a relationship from the left pane](media/create-relate-table2.png "Create a relationship from the left pane") -->

2. When the relationships page is open, select **Add relationship**, and then select the type of relationship you want to create (for example, **Many-to-one**).

   > [!div class="mx-imgBorder"] 
   > ![Add a relationship](media/create-relate-table3.png "Add a relationship")

More information: [Create a relationship between entities](../maker/common-data-service/data-platform-entity-lookup.md) 

> [!NOTE]
> When defining columns of type lookup within a table, a many-to-one relationship is created automatically.

## Edit a table relationship

Editing relationships in Project Oakdale works the same as Common Data Service except that you can't manage collaboration functions, such as allowing feedback or enabling SharePoint document management. More information: [Relationship actions](/maker/common-data-service/create-edit-entity-relationships.md#actions)

## Delete a table relationship

While viewing table relationships, select the table relationship you want to delete, and then do one of the following:

- Select **Delete relationship** on the command bar.

   <img src="media/delete-table-relationship1.png" alt="Delete table relationship from command bar" height="300" width="350">

- Select **…** next to the relationship, and then select **Delete relationship**.
   > [!div class="mx-imgBorder"] 
   > ![Delete table relationship in context](media/delete-table-relationship2.png "Delete table relationship in context") 

### See also

[Work with table columns](table-columns.md)
