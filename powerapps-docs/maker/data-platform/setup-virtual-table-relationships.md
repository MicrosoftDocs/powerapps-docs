---
title: Setting up relationships with virtual tables with Power Apps
description: Learn how to define relationships when using virtual tables.
author: NHelgren
ms.author: nhelgren
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 01/04/2023
ms.custom: template-concept
---
# Setting up a virtual table relationship

Virtual tables are  enabled for relationships. You can set up 1:N, N:1, and custom multi-table (polymorphic) relationships. Relationships can be established between:

- Local tables in Dataverse and virtual tables.
- Virtual tables and other virtual tables from the same provider, for example SQL->SQL.

For instance, you can't set up a relationship between a virtual table created using the OData virtual table provider and a virtual table created using the virtual connector provider.

## Defining relationships in virtual tables

Virtual tables created using the virtual connector provider automatically creates all the columns that are represented in the external source table. This will also include columns on which relationships are defined. However, the relationship definition won't be automatically created. You'll have to define this relationship in Dataverse manually.

The following example creates an N:1 relationship between a virtual table (**Service Request**) and a native table (**Account**). The column used to set up the relationship is **AccountId**. This column is the primary key in the account table and is a foreign key in the service request table.

A representation of the **Service Request** virtual table is shown below. You'll notice that the **AccountId** column, which is the column used for relationship in the external source, is of type **Multiple Line of Text**. You need to have this column represented as a **Lookup** type to create a relationship.

:::image type="content" source="media/ve-create-columns.png" alt-text="Create columns in virtual table":::

1. Go to **Advanced settings > Settings > Customization** and choose **Customize the System**.
1. In the left navigation pane, expand the **Entities** view and browse to the **Service Request** virtual table definition.
1. Select the **Fields** view, select the **AccountId** column, and then select **Delete**.
1. Choose **Delete** to confirm the deletion of this column.
1. To create the relationship, select the **N:1 Relationship** within the **Service Request** table.
1. Select **New Many-to-1 Relationship**.
1. Enter the following details to create the relationship between the **Service Request** virtual table and the **Account** table.
   1. In the **Relationship Definition** section – set the **Primary Entity** column value to **Account**.
   1. Optionally, if you want to edit the name of the relationship, you can do so in the **Name** column.
   1. In the **Lookup Field** section, set the **Display Name** to **Account.**
   1. The **Name** column automatically populates with the lookup column name.
   1. Set the **External Name** value to **AccountId** (matching the column name in your source table).
1. **Save**, and then close the relationship.

      :::image type="content" source="media/ve-create-relationship.png" alt-text="Create relationship":::

1. Refer to the columns for the **Service Request** virtual table, and you'll notice that the **AccountId** column is a **Lookup** type. This column can now
be added to forms and views to see all associated accounts for each of the service request record.

   :::image type="content" source="media/ve-custom-table-columns.png" alt-text="Custom table columns":::

1. With the relationship established you can now create a new service request and pick accounts to associate them to.

   :::image type="content" source="media/ve-new-custom-table.png" alt-text="New custom table":::

  > [!NOTE]
  > You will have to edit the forms and views for this table to include the lookup column and other required columns prior to operation on the virtual table.

## Tip

- The **Primary Key** column should be included in the create form if you didn't set up the column to increment during the design of the underlying source table automatically. You'll have to enter a valid value in the primary key column for an insert operation to succeed.

## Next steps

[Create virtual tables using the virtual connector provider (preview)](create-virtual-tables-using-connectors.md)
