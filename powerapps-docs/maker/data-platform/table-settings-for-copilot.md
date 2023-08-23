---
title: Configure tables to use Copilot
description: Learn what properties are required to configure a table in Dataverse so that the table data can be used with Copilot.
author: mspilde
ms.author: mspilde
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 08/07/2023
---
# Configure tables to use Copilot (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

When users ask questions about the data available in an app, Copilot uses backend natural language questions and answer capabilities that rely on the table to be enabled for searching across the data. The table configuration must also include the columns that your end-users will like to ask questions about the data in order to get responses back from Copilot in Power Apps.

This article describes the steps to enable a table and select the columns, which determine the data that will be included with Copilot responses.

> [!IMPORTANT]
> This is a preview feature.
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Enable indexing

The **Track changes** and **Appear in search results** table options must be enabled. Note that these are the default settings for most standard tables, but aren't enabled by default for custom tables.

To verify these options, select **Properties** from the table designer in make.powerappps.com, and then check whether both **Track changes** and **Appear in search results** options are selected. If not, from the properties pane select both, and then **Save** your changes. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)

:::image type="content" source="media/table-settings-for-copilot.png" alt-text="Table properties to enable to work with Copilot in Power Apps":::

## Configure columns

To configure your columns for Copilot, open the table, and then select **Views** from the table hub. In the list of views open the default quick find view for the table. By default, the default quick find view for a table has the name **Quick Find Active *table name***, where *table name* is the name of the table. In this example, the contact table is opened and the default quick find view for the table is the **Quick Find Active Contacts** view. When users ask questions from an app, Copilot includes the data from the columns configured following the steps below that's in the contact table rows.

:::image type="content" source="media/column-settings-for-copilot.png" alt-text="Column settings for use with Copilot in Power Apps":::

There are two actions that you need to take:

1. The first is to set the list of columns that you want to have indexed. To do this, add columns to the list in the **Find by** options in the table configuration. Select **Edit find table columns** to add columns not already in the list. Remove a column by selecting **X** next to the column.
1. After setting the columns for searching, you then set those columns so they are used to return data. It's necessary to define the columns that are returned to your end-users in the Copilot experience when a user asks an open ended question that would return all columns. You do this by adding the column to the view. Since there's limited data that can go into a Copilot answer, it's important to ensure the question has high quality so as to receive an accurate answer.
   - To add a column to the view, select **View column**, and then select the column you want. Repeat this step until you have all the columns you want.
   - To remove a column, select the column heading, and then select **Remove**.
 :::image type="content" source="media/column-settings-for-copilot2.png" alt-text="Set columns used to return answers from Copilot":::

After making your edits be sure to **Save and publish** your changes. Depending on the size of the data in the table it might take between fifteen minutes and a full day before all data will be available for questions.

> [!NOTE]
> There's a limit of 1k columns per database that can be used to find data (indexed). Be aware that you may exceed that limit across all your tables.

## Related content

[Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md) <br />
[Add Copilot control to a canvas app (preview)](../canvas-apps/add-ai-copilot.md)

