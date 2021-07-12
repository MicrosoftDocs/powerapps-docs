---
title: "Create Many-to-many table relationships in Microsoft Dataverse using Power Apps portal | MicrosoftDocs"
description: "Learn how to create many-to-may relationships"
ms.custom: ""
ms.date: 06/10/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create Many-to-many table relationships in Microsoft Dataverse using Power Apps portal

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

The [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) provides an easy way to create and edit Many-to-many table relationships for Dataverse.

The portal enables configuring the most common options, but certain options can only be set using solution explorer. More information: 
- [Create N:N (many-to-many) table relationships](create-edit-nn-relationships.md)
- [Create N:N (many-to-many) table relationships in Dataverse using solution explorer](create-edit-nn-relationships-solution-explorer.md)

## View Many-to-many table relationships

1. From the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select either **Model-driven** or **Canvas** design mode.
2. Select **Data** > **Tables** and select the table that has the relationships you want to view.
3. With the **Relationships** tab selected, you can select the following views: 

 |View|Description|
 |--|--|
 |**All**| Shows all the relationships for the table|
 |**Custom**|Shows only custom relationships for the table|
 |**Default**|Shows only the standard relationships for the table|

![Account table relationships.](media/view-account-relationships-portal.png)

Many-to-many relationships will have a **Relationship type** of **Many-to-many**.

> [!NOTE]
> The table you view may have no **Many-to-many** relationships.

## Create relationships

While [viewing table relationships](#view-many-to-many-table-relationships), in the command bar, select **Add relationship** and choose **Many-to-many**.

![Select type of relationship.](media/add-relationship-menu-portal.png)

In the **Many-to-many** panel, choose the table you want related to the current table.

> [!div class="mx-imgBorder"] 
> ![Many-to-many panel with account table selected.](media/many-to-many-panel-1.png)

Select **More Options** to view the **Relationship Name** and **Relationship table name** columns.

> [!div class="mx-imgBorder"] 
> ![Many-to-many panel with More Options selected.](media/many-to-many-panel-2.png)

The values for these columns are generated for you based on the tables chosen.

> [!NOTE]
> If you create more than one **Many-to-many** relationship with the same two tables, you will need to edit the generated **Relationship Name** and **Relationship table name** columns so that they will be unique.

Select **OK** to close the **Many-to-many** panel. The relationship will be created when you save changes to the table. 

Once saved, there's nothing that can be changed using [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). To edit properties of the relationship for model-driven apps use [solution explorer](create-edit-nn-relationships-solution-explorer.md).

## Create a many-to-many relationship with the same table (self-referential relationship)

There may be times when you need to create a many-to-many relationship that references the same table. For example, account records may have multiple parent account records. However, if the self-referential relationship doesn’t have custom labels configured, distinguishing the two related record types that appear in the app won’t be apparent to users. This is because the related records appear twice in the app by using the same table name.
To create a self-referential relationship, use custom labels.
1. Create a new custom table. In this example, the table is named *Custom table*.
2. Open the classic solution explorer, open the custom table, and in the **N:N Relationships** section create a new **Many-to-Many Relationship**.
3. Complete the relationship definition as follows. Make sure to add custom labels to both the current and the other table’s relationship:

   **Current table** section
   - **Display option**: **Use Custom Label**
   - **Custom Label**: *Primary Custom Table Relationship*

   **Other table** section
   - **Entity Name**: *Custom table*
   - **Display Option**: **Use Custom Label**
   - **Custom Label**: *Secondary Custom Table Relationship*
   :::image type="content" source="media/self-referencing-table-example.png" alt-text="Self-referential table relationship configuration.":::
4. Save the relationship, and then publish the customization.

Because the related record types use the custom labels defined for the self-referential relationship instead of the table name, users running the app can distinguish between the two related record types that exist.

:::image type="content" source="media/related-record-labels.png" alt-text="App with related records using relationship custom labels.":::

## Delete relationships

While [viewing table relationships](#view-many-to-many-table-relationships), select the relationship you want to delete.

![Delete table relationship.](media/delete-entity-relationship-portal.png)

You can use the **Delete relationship** command from the command bar or from the row context menu when you select the ellipses (**...**).

Deleting the Many-to-Many relationship will delete the relationship table created. All data connecting tables using the relationship will be lost.

### See also

[Create N:N (many-to-many) table relationships](create-edit-nn-relationships.md)<br />
[Create N:N (many-to-many) table relationships in Dataverse using solution explorer](create-edit-nn-relationships-solution-explorer.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]