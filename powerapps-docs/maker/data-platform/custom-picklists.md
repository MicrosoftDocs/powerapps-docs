---
title: Create a choice| Microsoft Docs
description: Step-by-step instructions for how to create a choice.
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: how-to
ms.date: 03/21/2018
ms.subservice: dataverse-maker
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create a choice

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Choices allow you to include drop down lists of fixed values to a user within your app to ensure data consistency, sometimes referred to as picklists or choice columns in other applications. Similar to tables, there are both standard choices, and the ability to create custom Choices to use within your app.

Choices can be created in two ways, either from the **Choices** list within the portal or directly within a table while creating a column. For more information on how to create a table, see [Create a table](data-platform-create-entity.md).

## Creating a Choice while adding a column

1. On [powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), expand the **Data** section and click or tap **Tables** in the left navigation pane.

    ![table Details.](./media/data-platform-cds-create-entity/entitylist.png "table List")

2. Click or tap an existing table, or [Create a new table](data-platform-create-entity.md)

3. Add a new column to your table by clicking **Add column**.

4. In the new column panel, enter the **Display name** for your column, **Name** will be automatically populated and is used as the unique name for your column. The **Display name** is used when presenting this column to your users, the **Name** is used when building your app, in expressions and formulas.

5. Click the **Data type** drop down and select **Choice** or **Multi Select Choice**.

    > [!div class="mx-imgBorder"] 
    > ![New choice column.](./media/data-platform-cds-create-entity/newfieldpanel.png "New Column Panel")

6. Click the **Choice** drop down and select **New Choice**

    > [!NOTE]
    > If an existing choice  could be used for your table, you can select it from this list without creating a new one.

    ![Choice List.](./media/data-platform-cds-newoptionset/fieldpanel-1.png "Choice list")

7. A new panel will open to create the choice, the **Display name** and **Name** will default from the name of the column but can be changed if needed. Click **Add new item** to start creating your list of options. Repeat this step until all your items are created.

    > [!div class="mx-imgBorder"] 
    > ![New choice.](./media/data-platform-cds-newoptionset/field-optionsetpanel.png "New choice")

8. Once you've entered your items, click **Save** to create your choice.

    > [!div class="mx-imgBorder"] 
    > ![Save choice.](./media/data-platform-cds-newoptionset/field-optionsetpanel-values.png "Save choirce")

9. Click **Done** to close the column panel, and then **Save Table** to save your table to Microsoft Dataverse.

    > [!NOTE]
    > You can select one of your items as the **Default** for this column, and it will be selected by default when users are creating new rows in your table.

    > [!div class="mx-imgBorder"] 
    > ![New Field.](./media/data-platform-cds-newoptionset/fieldpanel-2.png "New Column Panel")

## Creating n Choice from the Choice list

1. On [powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), expand the **Data** section and click or tap **Choices** in the left navigation pane.

    > [!div class="mx-imgBorder"] 
    > ![Choice list.](./media/data-platform-cds-newoptionset/optionsetlist.png "Choice List")

2. Click **New Choice**

3. A new panel will open to create the choice, enter the **Display name** and **Name**. Click **Add new item** to start creating your list of options. Repeat this step until all your items are created.

    > [!div class="mx-imgBorder"] 
    > ![Choice Create.](./media/data-platform-cds-newoptionset/optionset-create.png "Choice Create")

4. Once you've entered your items, click **Save** to create your choice.

    > [!div class="mx-imgBorder"] 
    > ![Save a new choice.](./media/data-platform-cds-newoptionset/optionset-create-values.png "Save a new choice")

5. You can now use this choice  by creating new column on a table.

## Global and local choices

By default, Choices are created as Global Choices which allows them to be reused across multiple tables. Under the **View more** option when creating a new Choice you can chose to make a Choice **Local**. This option is only available when creating a new Choice while adding a column, and not through the **Choices** list. Local choices can only be used by the table and column they are created against, and cannot be reused on other tables. This approach is only recommended for advanced users that a specific need for a local choice .

> [!IMPORTANT]
> Once a choice  is created as local or global, this cannot be changed.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]