---
title: "Work with pages in model-driven apps | MicrosoftDocs"
description: Learn how to create, edit, and remove pages in model-driven apps.
ms.custom: ""
ms.date: 08/17/2022
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: get-started
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.author: "emcoope"
ms.reviewer: "matp"
search.audienceType: 
  - maker
---
# Work with model-driven app pages

App designer pages are containers for one or more tables or dashboards. You can choose whether to have the page appear in the app navigation (site map) or not.

## Create a page

To create a page follow these steps:
1. Select **New page** in the app designer.
1. Select the page type, and then select **Next**:  
   - **Table based view and form**: Display records of a standard or custom table in a full-page list view. Creating a data view page also adds an associated form page for viewing and editing data on a selected record. More information: [Tables in Dataverse](../data-platform/entity-overview.md)
   - **Dashboard**: Display charts and tables from multiple entities to visualize data on a single page. Select one or more system, interactive, or Power BI dashboards. More information: [Create or edit model-driven app dashboards](create-edit-dashboards.md)
   - **Custom**: Design and build a page that's based on a canvas app. More information: [Overview of custom pages for model-driven apps](model-app-page-overview.md)
1. If you don't want your page to appear in the app's site map, clear the **Show in navigation** option.
  :::image type="content" source="media/add-table-view-and-form-pages.png" alt-text="Add table view and form pages":::
1. Select the components you want.
1. Select **Add**.

## Work with tables on a page

Create and edit tables directly from the app designer.

### Create a table for a page

1. In the model-driven app designer, select **Add page**, select **Table based view and form** as the page type, and then select **Next**.
1. Select **Create new table**. If your table is already created select it from the list.
1. If you selected **Create a new table**: 
   - Enter the table a name in the **Display name** field.
   - Optionally, specify the table **Record ownership** from the **Advanced options** area.
   :::image type="content" source="media/create-table-app-designer.png" alt-text="Create a table for a page in app designer":::
1. Select **Create**.

### Edit a table for a page

From the **Pages** area in app designer, select **...** to the right of the table name, and then select **Edit**.
:::image type="content" source="media/edit-table-app-designer.png" alt-text="Edit a table for a page in app designer":::

The table designer opens for you to make changes to the table.
:::image type="content" source="media/table-designer-app-designer.png" alt-text="Table designer for edit a table in app designer":::

To delete the table, **Close** the table hub, select **...** to the right of the table name, and then select **Remove**.

## Remove a page

To remove a page complete the following steps:

1. Select a page.
1. In the ellipses (**...**) select **Remove** *'Pagename'*.

## Next steps

[Create and customize a model-driven app form](create-and-edit-a-model-driven-form.md)

[Create or edit model-driven app dashboards](create-edit-dashboards.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)
