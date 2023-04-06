---
title: How to update forms and views from the table | Microsoft Docs
description: Add columns to forms and views through the table designer.
author: yueshu
manager:
ms.topic: how-to
ms.date: 04/05/2023
ms.subservice: dataverse-maker
ms.author: yueshu
search.audienceType:
  - maker
search.app:
  - PowerApps
  - D365CE
---

You can create columns directly from the table hub or table designer, which will then be added to your forms and views. In this walkthrough, we will show you how to simply add the columns you created to forms and views of this table without manually doing so through the form or view designer.

# Update through table hub and table designer

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2. In the left navigation pane, select **Tables**, then select the table that you wish to update from the table list. In the table hub and table designer, you can now see an **Update forms and views** option that allows you to directly add columns to selected forms and views from this table:

   :::image type="content" source="media/update-forms-and-views-table-hub.png" alt-text="Update forms and views option in table hub.":::

   :::image type="content" source="media/update-forms-and-views-table-designer.png" alt-text="Update forms and views option in table designer.":::

3. Select **Update forms and views** to configure what columns to be added to what forms and views:

| Property               | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Add these columns**  | <li>Selected columns in this dropdown will be added to the selected forms and views. </li><li>Available option: only columns currently shown in the table preview will be available to select.</li><li> Default option: both new columns that are just created and existing columns that are just added to the table will be preselected here. </li>                                                                      |
| **To these forms**     | <li> Columns selected in **Add these columns** will be added to selected forms here. If a certain column has already been added to this form before, it won’t be added again as a duplicate. </li><li> Available option: all Main, Quick Create, and Quick View forms from this table. </li><li> Default option: all Main forms from this table.</li>                                                                     |
| **And to these views** | <li> Columns selected in **Add these columns** will be added to selected views here. If a certain column has already been added to this view before, it won’t be added again as a duplicate. </li><li> Available option: all Public, Advanced Find, Associated, Quick Find, and Lookup views from this table. </li><li> Default option: all Public, Advanced Find, Associated, and Quick Find views from this table.</li> |

4. Once you’re done with the configuration, simply select **Update**, and after a moment, the columns you selected will be added to the forms and views you selected.

