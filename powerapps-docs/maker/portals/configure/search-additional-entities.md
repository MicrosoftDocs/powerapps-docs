---
title: "Global search for additional entities in Power Apps portal | MicrosoftDocs"
description: "Learn how global search works for additional entities in a portal."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/28/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# Walkthrough: Configuring additional entities for global search  

## Overview

You can enable additional entities for search functionality. Configuring search for additional entities requires additional actions, which are described in this article.

Following considerations apply when configuring additional entities for global search:

- Ensure that the [site setting](#site-setting-for-additional-entities) for search for additional entities is enabled.
- Configure a [search results page](#results-page-for-additional-entities) to display search results.
- Ensure an **Entity Permission** is created that provides Read privilege, and appropriate scope for the records to show in search results.
- Associate the entity permission with required **Web Roles**.
- Entity permissions must be associated with the **Anonymous Web Role** if you want to allow anonymous search for an entity.
- Create a view named **Portal Search** for any additional entity you want to enable search for. More information: [Searchable fields in global search](search.md#fields-searchable-in-global-search)

The explicit configuration explained above ensures that no records will accidentally be made available via global search.

### Site setting for additional entities

The site setting **Search/EnableAdditionalEntities** is required when configuring additional entities for search.

> [!IMPORTANT]
> **Search/EnableAdditionalEntities** is explicitly for enabling search for additional entities. The main search site setting **Search/Enabled** must be set to **true** when using search functionality.

You can also configure other related site settings similar to the search configuration for default entities. For example, you can use the **Search/Filters** setting to configure additional entities and add a drop-down filter option to the global search. More information: [Site setting](search.md#related-site-settings)

### Results page for additional entities

The search result page is configured via a **Site Marker** named ```<entitylogicalname>_SearchResultPage```.

For example, if your entity logical name is *nwind_products*, the site marker will be ```nwind_products_SearchResultPage```. The value of the site marker is the page that you want to open when that search result is selected. By default, a record ID is passed in the *id* querystring parameter to the search results page.

Ensure that your search results page has an entity form, or has logic written to show the search result details.

## Walkthrough - configure search for additional entities with sample database

The following walkthrough explains how to enable search for the **Order Products** entity in the sample database **Northwind**, available with Common Data Service.

For more information about sample databases, see [Install Northwind Traders database and apps](../../canvas-apps/northwind-install.md).

> [!TIP]
> You can follow the walkthrough with an entity of your choice by replacing the *nwind_products* entity name with your entity's logical name.

## Step 1: Add or update search site settings

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Ensure that you're in the appropriate environment where your portal exists.

1. Select **Apps** in the left navigation pane, and locate the **Portal Management** model-driven app.  

    ![Portal Management](media/search-additional-entities/portal-management.png "Portal Management")

    >[!NOTE]
    > The Portal Management app might be named **Dynamics 365 Portals** if you're in an environment where Dynamics 365 applications are installed.

1. Select to open the **Portal Management** app, and then go to **Site Settings** in the left navigation pane.

1. Create a new setting, **Search/EnableAdditionalEntities**, and set its value to **true**.

    ![Site setting for EnableAdditionalEntities](media/search-additional-entities/enableadditionalentitiessearch-sitesetting.png "Site setting for EnableAdditionalEntities")

1. Create or update the **search/filters** setting, and add the value **Products:nwind_products**.

    ![Search/filters site setting](media/search-additional-entities/search-filters.png "Search/filters site setting")

## Step 2: Create or verify the Portal Search view

> [!NOTE]
> The following steps require the [Northwind Traders solution](../../canvas-apps/northwind-install.md) to be installed. If you want to use another entity, use the appropriate solution or use the Default solution.

1. Go to [Power Apps](https://make.powerapps.com), and select **Solutions** from the left navigation pane.

1. Select **Northwind Traders**.

    ![Select solution](media/search-additional-entities/select-solution.png "Select solution")

1. Search for the **Order Product** entity.

    ![Order Product entity](media/search-additional-entities/order-product.png "Order Product entity")

1. Select the **Order Product** entity, and then select **Views**.

    ![Views](media/search-additional-entities/views.png "Views")

1. Ensure that you see **Portal Search** in the views list.

    ![Portal Search view](media/search-additional-entities/portal-search.png "Portal Search view")

    If the Portal Search view doesn't already exist, select **Add view**, enter the name as **Portal Search**, and then select **Create**.

    ![Add a view](media/search-additional-entities/add-view.png "Add a view")

    ![Add the Portal Search view](media/search-additional-entities/portal-search-view.png "Add the Portal Search view")

1. Ensure appropriate columns are added to the view for search.

    ![Add columns](media/search-additional-entities/add-columns.png "Add columns")

1. If you edited the view, be sure to select **Save**, and then **Publish** before you continue.

    ![Save and publish](media/search-additional-entities/save-publish.png "Save and publish the view")

## Step 3: Create entity permissions

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** in the left navigation pane, and then select to open the **Portal Management** model-driven app.  

1. Select **Entity Permissions** in the left navigation pane.

1. Select **New**.

    ![New Entity Permission record](media/search-additional-entities/new-entity-permission.png "[New Entity Permission record")

1. Enter the name as **Northwind Products Read All**, and then select the appropriate **Scope** and the **Read** privilege.

    For this example, the **Global** scope is provided to the **nwind_products** entity.

    ![Scope and Read permissions](media/search-additional-entities/scope-read.png "Scope and Read permissions")

1. Select **Save & Close**.

1. Select and open **Northwind Products Read All**.

1. Scroll down to the **Web Roles** section, and then select **Add Existing Web Role**.

    ![Add an existing web role](media/search-additional-entities/add-existing-web-role.png "Add an existing web role")

1. Search for **Authenticated Users**, and then select **Add**:

    ![Add authenticated users](media/search-additional-entities/add-authenticated-users.png "Add authenticated users")

## Step 4: Add a webpage

1. Go to [Power Apps](https://make.powerapps.com), and select **Apps** in the left navigation pane.

1. Select **More Commands** (…) for the portal, and then select **Edit** to open the portal in Power Apps Studio.

1. Select **New Page** from the menu in the upper-left corner, and then select the **Blank** layout for the page.

    ![New page](media/search-additional-entities/new-page.png "New page")

1. Enter the webpage name as **Order Products**. This page will be configured as the search results page.

1. Select **Components** in the left navigation pane, and then add a **Form** component to this webpage.

    ![Add a form component](media/search-additional-entities/form-component.png "Add a form component")

1. Select the **Use existing** option on the right side of your workspace, choose the **View Products** form for the **nwind_products** entity, and then set **Mode** to **ReadOnly**.

    ![Set the mode](media/search-additional-entities/mode.png "Set the mode")

## Step 5: Add a site marker for the search results details page

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** in the left navigation pane, and select to open the **Portal Management** model-driven app.  

1. Select **Site Marker** from the left navigation pane.

1. Select **New**, and then create a new site marker by using the following details:

    - **Name:** **nwind_products_SearchResultPage**
    - **Page:** **Order Products**
    
    ![New site marker](media/search-additional-entities/new-site-marker.png "New site marker")

## Step 6: Rebuild the search index

1. Browse your portal by using a user account that has the Administrator web role assigned.

1. Append the URL in the address bar with **/_services/about**, and then select **Enter**.

   ![_services_about page](media/search-additional-entities/services-about.png "_services_about page")

1. Select [Clear cache](https://docs.microsoft.com/powerapps/maker/portals/admin/clear-server-side-cache).

1. After clearing the cache, select [Rebuild search index](search.md#rebuild-full-search-index).

## Step 7: Verify that global search works with the custom entity

1. Browse to the portal with a user that has *Authenticated* **Web Role** assigned.

1. Go to the search toolbar or the search page, and search for a known record.

   For example, use the search keyword **Northwind Clam Chowder** to display results associated with the **nwind_products** entity.

   ![Search results](media/search-additional-entities/search-results.png "Search results")

## Next steps

[Remove an entity from global search](search.md#remove-an-entity-from-global-search)

### See also

[Search related site settings](search.md#related-site-settings)