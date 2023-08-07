---
title: Configure tables to use with Copilot
description: Learn what properties are required to configure a table in Dataverse so that the table data can be used with Copilot.
author: mspilde
ms.author: mspilde
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 08/07/2023
---
# Configure tables to use with Copilot

When users ask questions about the data available in an app, Copilot uses backend natural language questions and answer capabilities that rely on the table to be enabled for searching across the data. The table configuration must also include the columns that your end-users will like to ask questions about the data in order to get responses back from Copilot in Power Apps.

Here are steps to enable your table and configure your data.

## Enable indexing

**Track changes** and **Appear in search results** options must be enabled. Since these are the default settings for most standard tables, these properties might already be enabled.

To verify, select **Properties** from the table designer in make.powerappps.com, and then check to see if both options are selected. If not, select both in the properties pane, and then **Save** your changes. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)

:::image type="content" source="media/table-settings-for-copilot.png" alt-text="Table properties to enable to work with Copilot in Power Apps":::

## Configure columns

To configure your columns, open the table, and then select **Views** from the table hub. In the list of views select the default quick find view for your table.  In the image below we are using the Contact table default quick-find view.

:::image type="content" source="media/column-settings-for-copilot.png" alt-text="Column settings for use with Copilot in Power Apps":::

There are two actions that you need to take.  The first is to set the list of columns that you would like to use in your index. To do this, add columns to the list in the **Find By** options in the table configuration.  This is the high-lighted section on the right.

> [!NOTE]
> There's a limit of 1k columns per database that can be used to find data (indexed). Be aware that you may exceed that limit across all your tables.

After setting the columns for searching, you then set the columns that are used to return data. It's necessary to define the columns that are returned to your end-users in the Copilot experience when a user asks an open ended question that would return all columns. Since there's limited data that can go into a Copilot answer, it's important to ensure the question has high quality to receive an accurate answer. This is highlighted in the middle of the image below.

:::image type="content" source="media/column-settings-for-copilot2.png" alt-text="Set columns used to return answers from Copilot":::

After making your edits be sure to save and publish your changes. Depending on the size of the data in the table it might take between fifteen minutes and a full day before all data will be available for questions.

## Related content

[Add Copilot control to a canvas app (preview)](../canvas-apps/add-ai-copilot.md)
