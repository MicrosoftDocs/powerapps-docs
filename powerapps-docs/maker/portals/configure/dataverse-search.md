---
title: Dataverse Search in portals
description: "Learn how Dataverse search works in a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 11/16/2021
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# Configure Dataverse search in portals (preview)

[This article is pre-release documentation and is subject to change.]

## Overview

[Dataverse search](../../../user/relevance-search-benefits.md) delivers fast and comprehensive search results sorted by relevance in portals. This is the same search service used in model-driven apps and other Power Platform services built on Microsoft Dataverse. The [Lucene.NET](search.md) powered search will coexist for certain time and will eventually be replaced by Dataverse search. To enable Dataverse search, add the [site setting](configure-site-settings.md) `Search/EnableDataverseSearch` and set to **true**. Either false or without this setting will instead enable the [Lucene.NET](search.md) search.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)]

This walk through explains how to enable search for the **Order Products** table in the **Northwind** sample database, available with Dataverse. For more information about sample databases, see [Install Northwind Traders database and apps](../../canvas-apps/northwind-install.md).

You can follow the walk through with a table of your choice by replacing the *nwind\_products* table name with your table's logical name.

## Step 1: Enable Dataverse Search

1. In the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select an environment.

1. Select **Settings** &gt; **Product** &gt; **Features**.

1. Under **Search**, set **Dataverse search** to **On**.

1. Select **Save**.

    :::image type="content" source="media/dataverse-search/enable-dataverse-search.png" alt-text="Power Platform admin center enabling Dataverse search":::

## Step 2: Add or update search site settings

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Ensure that you're in the appropriate environment where your portal exists.

1. Select **Apps** in the left navigation pane, and locate the **Portal Management** model-driven app.

    :::image type="content" source="media/dataverse-search/portal-management-app.png" alt-text="Launching Portal Management app.":::  

1. Select to open the **Portal Management** app, and then go to **Site Settings** in the left navigation pane.

1. Create or update the **Search/EnableDataverseSearch** site setting, and set its value to **true**.

1. Create or update the **Search/EnableAdditionalEntities** site setting, and set its value to **true**.

1. Create or update the **search/filters** site setting, and add the value **Products:nwind\_products**.

## Step 3: Create or verify the Portal Search view

> [!Note]
> The following steps require the [Northwind Traders solution](../../canvas-apps/northwind-install.md) to be installed. If you want to use another table, use the appropriate solution or use the **Default solution**.

1. Go to [Power Apps](https://make.powerapps.com), and select **Solutions** from the left navigation pane.

1. Select **Northwind Traders**.

    :::image type="content" source="media/dataverse-search/select-solution.png" alt-text="Selecting the Northwind Traders solution.":::

1. Search for the **Order Product** table.

    :::image type="content" source="media/dataverse-search/select-table.png" alt-text="Select order product table.":::

1. Select the **Order Product** table, and then select **Views**.

    :::image type="content" source="media/dataverse-search/table-view.png" alt-text="Selecting table views.":::

1. Ensure that you see **Portal Search** in the views list.

    :::image type="content" source="media/dataverse-search/portal-search-view.png" alt-text="Portal search view in list of views.":::

1. If the Portal Search view doesn't already exist:
    - Select **Add view**
    - Enter the name as **Portal Search**
    - Select **Create**

    :::image type="content" source="media/dataverse-search/add-search-view.png" alt-text="Adding a new portal search view.":::

    :::image type="content" source="media/dataverse-search/create-portal-search.png" alt-text="Creating portal search view.":::

1. Ensure appropriate columns are added to the view for search.

    :::image type="content" source="media/dataverse-search/add-columns.png" alt-text="Add columns to portal search view.":::

1. If you edited the view, be sure to select **Save**, and then **Publish** before you continue.

    :::image type="content" source="media/dataverse-search/publish-view.png" alt-text="Save and publish view.":::

## Step 3: Create table permissions

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** in the left navigation pane, and then select to open the **Portal Management** model-driven app.  

1. Select **Table Permissions** in the left navigation pane.

1. Select **New**.

    :::image type="content" source="media/dataverse-search/table-permission.png" alt-text="Creating a new table permission.":::

1. Enter the name as **Northwind Products Read All**, and then select the appropriate **Access Type** and the **Read** privilege.

    For this example, the **Global** access type is provided to the **nwind\_products** table.

    :::image type="content" source="media/dataverse-search/global-read-permission.png" alt-text="Configuring global read permission.":::

1. Select **Save & Close**.

1. Select and open **Northwind Products Read All**.

1. Scroll down to the **Web Roles** section, and then select **Add Existing Web Role**.

    :::image type="content" source="media/dataverse-search/add-existing-webrole.png" alt-text="Adding existing webrole to table permission.":::

1. Search for **Authenticated Users**, and then select **Add**:

    :::image type="content" source="media/dataverse-search/authenticated-users.png" alt-text="Add authenticated users.":::

## Step 4: Add record details webpage

1. Go to [Power Apps](https://make.powerapps.com), and select **Apps** in the left navigation pane.

1. Select **More Commands** (…) for the portal, and then select **Edit** to open the portal in the [Power Apps portals Studio](../portal-designer-anatomy.md).

1. Select **New Page** from the menu in the upper-left corner, and then select the **Blank** layout for the page.

    :::image type="content" source="media/dataverse-search/blank-layout.png" alt-text="Select blank-layout template.":::

1. Enter the webpage name as **Order Products**.

1. Select **Components** in the left navigation pane, and then add a **Form** component to this webpage.

    :::image type="content" source="media/dataverse-search/add-form-component.png" alt-text="Add form component to web page.":::

1. Select the **Use existing** or **Create New** option on the right side of your workspace, choose the **View Products** form for the **nwind\_products** table, and then set **Mode** to **ReadOnly**.

## Step 5: Add a site marker for the record details webpage

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** in the left navigation pane, and select to open the **Portal Management** model-driven app.  

1. Select **Site Marker** from the left navigation pane.

1. Select **New**, and then create a new site marker by using the following details:

    - Enter **nwind\_products\_SearchResultPage** for the **Name**.
    - Select **Order Products** for the **Page**.

    :::image type="content" source="media/dataverse-search/search-results-page.png" alt-text="Create search results site marker.":::

## Step 6: Verify Dataverse search functionality

1. Browse to the portal with a user that has *Authenticated* **Web Role** assigned.

1. Go to the search toolbar or the search page, and search for a known record.

    For example; use the search term **Northwind Clam Chowder** to get the results associated with the **nwind\_products** table.

    :::image type="content" source="media/dataverse-search/search-results.png" alt-text="Search results on web page.":::

## Limitations

- Boosting relevance, searching, or filtering results by Dataverse column name configured in **Search/Query** site setting is not supported.

- The **filter** parameter in the **searchindex** Liquid object will not filter search results.

    For example: `{% searchindex query: 'support', filter: ' +statecode:0'%}` will not filter matching search results that don't have `statecode:0`.

- Although **Portal Search** view can have any operator in filter, only the below list of operators is applied to query the search results:

    - equals
    - does not equal
    - is greater than
    - is greater than or equal to
    - is less than
    - is than or equal to

- Related fields defined in **Portal Search** view as a **filter column** or **view column** aren't supported by Dataverse search and will be ignored.

- Attachment content and objects in file data type are not searched.

### See also

- [Use faceted search](improve-portal-search-faceted-search.md)
- [File attachment search](search-file-attachment.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]