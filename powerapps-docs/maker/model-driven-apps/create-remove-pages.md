---
title: "Work with pages in model-driven apps"
description: Learn how to create, edit, and remove pages in model-driven apps.
ms.date: 07/10/2025
ms.topic: get-started
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.author: "emcoope"
ms.reviewer: "matp"
ms.subservice: mda-maker
search.audienceType: 
  - maker
---
# Work with model-driven app pages

App designer pages are containers for tables, dashboards, custom pages, or web resources. Pages determine your app's assets and navigation. You can choose whether to have the page appear in the app navigation (site map) or not.

:::image type="content" source="media/pages-in-model-driven-app.png" alt-text="Pages in a model-driven app" lightbox="media/pages-in-model-driven-app.png":::

## Create a page

To create a page, follow these steps:

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Apps**, and then **Edit** the app you want.
1. In the app designer on the **Pages** tab, select **New**.
1. Select the page type, and then select **Next**:  
   - **Dataverse table**: Display records of a standard or custom table in a full-page list view. Creating a data view page also adds an associated form page for viewing and editing data on a selected record. More information: [Tables in Dataverse](../data-platform/entity-overview.md)
   - **Dashboard**: Display charts and tables from multiple entities to visualize data on a single page. Select one or more system, interactive, or Power BI dashboards. More information: [Create or edit model-driven app dashboards](create-edit-dashboards.md)
   - **Custom page**: Design and build a page that's based on a canvas app. More information: [Overview of custom pages for model-driven apps](model-app-page-overview.md)
   - **Web resource**: Select a web resource from a list of web resources. More information: [Create or edit model-driven app web resources to extend an app](create-edit-web-resources.md)
   - **Navigation link**: Enter a direct link to a web resource. [Create or edit model-driven app web resources to extend an app](create-edit-web-resources.md)
   - **Describe a page**. Use natural language to create a generative page that's generated using AI. More information: [Describe a page using natural language (preview)](generative-pages.md)
1. If you don't want your page to appear in the app's site map, clear the **Show in navigation** option.
  :::image type="content" source="media/add-table-view-and-form-pages.png" alt-text="Add a table to a page":::
1. Select **Add**.

## Work with tables on a page

Create and edit tables directly from the app designer.

### Create a table for a page

1. In the model-driven app designer, select **Add page**, select **Dataverse table** as the page type.
1. Select **Create new tables**. Otherwise, if your table is already created select it from the list.
1. If you selected **Create a new tables**: 
   - Select the option you want to create a table and follow the instructions on your screen.
   - More information: [Create new tables](../data-platform/create-edit-entities-portal.md#create-new-tables)

### Edit a table for a page

From the **Pages** tab in app designer, select **...** to the right of the table name, and then select **Edit table**.
:::image type="content" source="media/edit-table-app-designer.png" alt-text="Edit a table for a page in app designer":::

The table designer opens for you to make changes to the table.
:::image type="content" source="media/table-designer-app-designer.png" alt-text="Table designer for edit a table in app designer":::

To delete the table, **Close** the table hub, select **...** to the right of the table name, and then select **Remove**.

### Edit a table view

To edit a view for a table that's added to your app in a page, complete these steps:

1. In the model-driven app designer, select a page that is based on a table.
1. On the command bar, select **Edit view**.

The view designer is displayed where you can edit the table view. More information: [Edit public views from a table](create-or-edit-model-driven-app-view.md#edit-public-views-from-a-table)

## Remove a page

To remove a page, complete these steps:

1. In the model-driven app designer, select a page.
1. Select the ellipses (**...**), and then select **Remove from navigation**.

## Next steps

[Create and customize a model-driven app form](create-and-edit-a-model-driven-form.md)

[Create or edit model-driven app dashboards](create-edit-dashboards.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)
