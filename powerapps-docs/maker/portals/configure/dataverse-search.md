---
title: Dataverse search in portals
description: "Learn how Dataverse search works in a portal."
author: nageshbhat-msft

ms.topic: conceptual
ms.collection: get-started
ms.date: 04/20/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - nageshbhat-msft
    - ProfessorKendrick
---

# Configure Dataverse search in portals


[!INCLUDE[cc-pages-banner](../../../includes/cc-pages-banner.md)]

## Overview

[Dataverse search](../../../user/relevance-search-benefits.md) delivers fast and comprehensive search results sorted by relevance in portals. Dataverse search is the same search service used in model-driven apps and other Microsoft Power Platform services built on Microsoft Dataverse. To enable Dataverse search, add the [site setting](configure-site-settings.md) **Search/EnableDataverseSearch** and set it to **true**. If this setting is set to **false** or doesn't exist at all, [Lucene.NET](search.md) search will be enabled instead.

This walkthrough explains how to enable search for the **Order Products** table in the Northwind Traders sample database, which is available with Dataverse. For more information about sample databases, go to [Install Northwind Traders database and apps](../../canvas-apps/northwind-install.md).

You can follow the walkthrough with a table of your choice by replacing **nwind\_products** with the logical name of your table.

## Step 1: Enable Dataverse search

1. In the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select an environment.

1. Select **Settings** &gt; **Product** &gt; **Features**.

1. Under **Search**, set **Dataverse search** to **On**.

1. Select **Save**.

    :::image type="content" source="media/dataverse-search/enable-dataverse-search.png" alt-text="Power Platform admin center enabling Dataverse search":::

## Step 2: Add or update search site settings

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Ensure that you're in the appropriate environment where your portal exists.

1. On the left pane, select **Apps**, and locate the **Portal Management** model-driven app.

    :::image type="content" source="media/dataverse-search/portal-management-app.png" alt-text="Opening Portal Management.":::  

1. Select **Portal Management**, and then select **Site Settings** on the left pane.

1. Create or update the **Search/EnableDataverseSearch** site setting, and set its value to **true**.

1. Create or update the **Search/EnableAdditionalEntities** site setting, and set its value to **true**.

1. Create or update the **search/filters** site setting, and add the value **Products:nwind\_products**.

## Step 3: Create or verify the Portal Search view

> [!Note]
> The following steps require the [Northwind Traders solution](../../canvas-apps/northwind-install.md) to be installed. If you want to use another table, use the appropriate solution or use the **Default solution**.

1. Go to [Power Apps](https://make.powerapps.com), and select **Solutions** on the left pane.

1. Select **Northwind Traders**.

    :::image type="content" source="media/dataverse-search/select-solution.png" alt-text="Selecting the Northwind Traders solution.":::

1. Search for the **Order Product** table.

    :::image type="content" source="media/dataverse-search/select-table.png" alt-text="Select order product table.":::

1. Select the **Order Product** table, and then select **Views**.

    :::image type="content" source="media/dataverse-search/table-view.png" alt-text="Selecting table views.":::

1. Ensure that you see **Portal Search** in the views list.

    :::image type="content" source="media/dataverse-search/portal-search-view.png" alt-text="Portal search view in list of views.":::

    If the Portal Search view doesn't already exist, do the following:

    1. Select **Add view**

       :::image type="content" source="media/dataverse-search/add-search-view.png" alt-text="Adding a new portal search view.":::

    1. Enter the name as **Portal Search**, and then select **Create**.
 
       :::image type="content" source="media/dataverse-search/create-portal-search.png" alt-text="Creating portal search view.":::

1. Ensure that the view includes the appropriate columns that you want to use for search. Add additional columns if required.

    :::image type="content" source="media/dataverse-search/add-columns.png" alt-text="Screenshot showing the portal search view with Product Name, Product Code, and List Price columns. As well as option to add columns.":::

1. If you edited the view, be sure to select **Save**, and then select **Publish** before you continue.

    :::image type="content" source="media/dataverse-search/publish-view.png" alt-text="Save and publish the view.":::

## Step 3: Create table permissions

1. Sign in to [Power Apps](https://make.powerapps.com).

1. On the left pane, select **Apps**, and then select **Portal Management**.  

1. On the left pane, select **Table Permissions**.

1. Select **New**.

    :::image type="content" source="media/dataverse-search/table-permission.png" alt-text="Creating a new table permission.":::

1. Enter the name as **Northwind Products Read All**, and then select the appropriate **Access Type** and the **Read** privilege.

    For this example, the **Global** access type is provided to the **nwind\_products** table.

    :::image type="content" source="media/dataverse-search/global-read-permission.png" alt-text="Configuring global read permission.":::

    > [!NOTE]
    > The **Global** access type will provide access to all records of the **nwind\_products** table to related contacts of the associated web role (**Authenticated Users** web role will apply to all logged in portal users). Consider your data security requirements and choose other access types to restrict access to data. Please refer to [Configure security using table permissions](entity-permissions-studio.md) for more details.

1. Select **Save & Close**.

1. Select and open **Northwind Products Read All**.

1. Scroll down to the **Web Roles** section, and then select **Add Existing Web Role**.

    :::image type="content" source="media/dataverse-search/add-existing-webrole.png" alt-text="Adding an existing web role to table permissions.":::

1. Search for **Authenticated Users**, and then select **Add**:

    :::image type="content" source="media/dataverse-search/authenticated-users.png" alt-text="Add authenticated users.":::

## Step 4: Add a record details webpage

1. Go to [Power Apps](https://make.powerapps.com), and select **Apps** on the left pane.

1. Select **More Commands** (…) for the portal, and then select **Edit** to open the portal in [Power Apps portals Studio](../portal-designer-anatomy.md).

1. From the menu in the upper-left corner, select **New Page**, and then select the **Blank** layout for the page.

    :::image type="content" source="media/dataverse-search/blank-layout.png" alt-text="Select the blank layout template.":::

1. Enter the webpage name as **Order Products**.

1. On the left pane, select **Components**, and then select **Form**.

    :::image type="content" source="media/dataverse-search/add-form-component.png" alt-text="Add a form component to the webpage.":::

1. On the right side of your workspace, select **Use existing** or **Create New**, choose the **View Products** form for the **nwind\_products** table, and then set **Mode** to **ReadOnly**.

## Step 5: Add a site marker for the record details webpage

1. Sign in to [Power Apps](https://make.powerapps.com).

1. On the left pane, select **Apps**, and then select **Portal Management**.  

1. On the left pane, select **Site Marker**.

1. Select **New**, and then create a new site marker by doing the following:

   1. For **Name**, enter **nwind\_products\_SearchResultPage**.

   1. For **Page**, select **Order Products**.

   :::image type="content" source="media/dataverse-search/search-results-page.png" alt-text="Create a search results site marker.":::

## Step 6: Verify Dataverse search functionality

1. Browse to the portal with a user account that has the Authenticated web role assigned.

1. Go to the search toolbar or the search page, and search for a known record.

    For example, use the search term **Northwind Clam Chowder** to get the results associated with the **nwind\_products** table.

    :::image type="content" source="media/dataverse-search/search-results.png" alt-text="Search results on the webpage.":::

## Limitations

- It isn't possible to boost relevance, search, or filter results by a Dataverse column name that has been configured in the **Search/Query** site setting.

- The **filter** parameter in the **searchindex** Liquid object won't filter search results.

    For example: `{% searchindex query: 'support', filter: ' +statecode:0'%}` won't filter any matching search results that don't include `statecode:0`.

- Although the Portal Search view can have any operator in a filter, only the following list of operators is applied to query search results:

  - Equals
  - Does not equal
  - Is greater than
  - Is greater than or equal to
  - Is less than
  - Is less than or equal to

- Related fields defined in the Portal Search view as a filter column or view column aren't supported by Dataverse search and will be ignored.

- The content of attachments and objects specified in a file type column aren't searched.

## Known issues

- If you switch the site setting **Search/EnableDataverseSearch** from **true** to **false** to disable Dataverse search and re-enable Lucene.NET search, you'll need to go to the [Power Apps portals admin center](../admin/admin-overview.md) and choose **Actions** > **Restart** to restart the portal. If you miss this step, you'll see an error page when you attempt to [rebuild the search index](search.md#rebuild-full-search-index) and users won't see any search results.  

- When searching for a keyword, you might continuously encounter the message "There was a problem performing the search. Try again." To fix this, restart the portal by opening the Power Apps portals admin center and choosing **Actions** > **Restart**.

### See also

[Use faceted search](improve-portal-search-faceted-search.md)  
[File attachment search](search-file-attachment.md)  

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
