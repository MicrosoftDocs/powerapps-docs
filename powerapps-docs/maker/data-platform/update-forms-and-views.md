---
title: Update forms and views using table designer | Microsoft Docs
description: Learn how to update your forms and views without manually editing them in the form and view designer.
author: travshu77
manager:
ms.topic: how-to
ms.date: 08/25/2023
ms.subservice: dataverse-maker
ms.author: yueshu
ms.reviewer: matp
search.audienceType:
  - maker
search.app:
  - PowerApps
  - D365CE
---

# Update forms and views using table designer

Create columns directly in the table hub or table designer, which will then be added to your forms and views. In this walkthrough, you'll learn how to simply add the columns you created to forms and views of this table without manually doing so in the form or view designer.

## Using table hub and table designer

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2. In the left navigation pane, select **Tables**, and then select the table that you want to update from the table list. In the table hub and table designer, there's an **Update forms and views** option that allows you to directly add columns to selected forms and views in this table.

   :::image type="content" source="media/update-forms-and-views-table-hub.png" alt-text="Update forms and views option in table hub.":::

   :::image type="content" source="media/update-forms-and-views-table-designer.png" alt-text="Update forms and views option in table designer.":::

3. Select **Update forms and views** to configure what columns should be added to certain forms and views:

    | Property               | Description                                                                                                                                                                             | Available option                                                                     | Default option                                                                                |
    | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
    | **Add these columns**  | Selected columns in this dropdown list will be added to the selected forms and views.                                                                                                        | Only columns currently shown in the table preview.                                   | Both new columns that are recently created and existing columns that are recently added to the table. |
    | **To these forms**     | Columns selected in **Add these columns** will be added to selected forms. If a certain column has already been added to this form before, it won’t be added again as a duplicate. | All main, quick create, and quick view forms from this table.                        | All Main forms from this table.                                                               |
    | **And to these views** | Columns selected in **Add these columns** will be added to selected views. If a certain column has already been added to this view before, it won’t be added again as a duplicate. | All public, advanced find, associated, quick find, and lookup views from this table. | All public, advanced find, associated, and quick find views from this table.                  |

4. Once you’re done with the configuration, select **Update**. The columns you selected are added to the forms and views you selected.

## Using inline table designer in modern app designer

You might be working on a table in the modern app designer as you’re building an app. In this case, you can also update your forms and views directly using the inline table designer in the modern app designer:

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. On the left navigation pane, select **Apps**, select the app you want, and then select **Edit**.

1. In the left navigation pane within the modern app designer, select **Data**, then **… > Edit table** to edit your table using the inline table designer.

1. The **Update forms and views** option is displayed in the inline table designer:

   :::image type="content" source="media/update-forms-and-views-inline-table-designer.png" alt-text="Update forms and views option in inline table designer.":::

    Follow the same steps in 3 and 4 as in the table hub and table designer to update your forms and views. You can also add the columns you want to your table. When you’re finished with the update, select **Update and close** at the bottom right of the inline table designer. The columns are added to the forms and views preselected for you, and the inline table designer is closed.

   :::image type="content" source="media/update-forms-and-views-update-and-close-button.png" alt-text="Update and close button in inline table designer.":::

## See also

[Create a custom table](data-platform-create-entity.md)
