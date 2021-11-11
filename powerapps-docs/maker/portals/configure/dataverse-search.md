---
title: Dataverse Search in portals
description: "Learn how global search works in a portal."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 11/11/2021
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# Walk-through: Configuring Dataverse Search (Preview)

## Overview

[Dataverse Search](https://docs.microsoft.com/en-us/powerapps/user/relevance-search-benefits) delivers fast and comprehensive search results sorted by relevance. Same Search service used in Modal Driven Apps and other Power Platform services built on Dataverse. Lucene .Net powered Search will co-exist for certain time and eventually Dataverse powered search will replace it. To enable Dataverse search add site setting Search/EnableDataverseSearch and set to true. Either false or without this setting will enable the Lucene .Net

## Steps to configure search for Dataverse powered Search

To configure Dataverse search

1.  [Enable Dataverse](#step-1-enable-dataverse-search) Search for environment in Power Platform Admin Center

2.  Set Portal to use Dataverse Search for first time by [adding site setting](#step-2-add-or-update-search-site-settings) Enable Dataverse Search setting

3.  [Create Portal Search view](#step-3-create-or-verify-the-portal-search-view) for each additional table with the required filters and columns that needs to be searchable.

4.  [Configure table permissions](#step-3-create-table-permissions) for each additional table with a Web Role to have at least read privilege. Skip this step if you already have the read permissions configured for each table.

5.  [Create a record details page](#step-4-add-record-details-webpage) for each table to show the details of the selected record from the search results page. Skip this step if you already have created separate results record details page for each table.

6.  [Create a site marker](#step-5-add-a-site-marker-for-record-details-webpage) named &lt;entitylogicalname&gt;\_SearchResultPage for each table with the associated record details page.

Note:

-   This walkthrough explains how to enable search for the **Order Products** table in the sample database **Northwind**, available with Microsoft Dataverse. For more information about sample databases, see [Install Northwind Traders database and apps](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/northwind-install).

-   You can follow the walkthrough with a table of your choice by replacing the *nwind\_products* table name with your table's logical name.

## Step 1: Enable Dataverse Search

1.  In the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select an environment.

2.  Select **Settings** &gt; **Product** &gt; **Features**.

3.  Under **Search**, set **Dataverse search** to **On**.

4.  Select **Save**.

![Graphical user interface  text  application  Teams Description automatically generated](media/image1.png)

## Step 2: Add or update search site settings

1.  Sign in to [Power Apps](https://make.powerapps.com).

2.  Ensure that you're in the appropriate environment where your portal exists.

3.  Select **Apps** in the left navigation pane, and locate the **Portal Management** model-driven app.  

4.  Select to open the **Portal Management** app, and then go to **Site Settings** in the left navigation pane.

![Portal Management ](media/image2.png)

5.  Create or Update setting, **Search/EnableDataverseSearch**, and set its value to **true**.

6.  Create or update the **Search/EnableAdditionalEntities** setting, and set its value to **true**..

7.  Create or update the **search/filters** setting, and add the value **Products:nwind\_products**.

## Step 3: Create or verify the Portal Search view

Note

The following steps require the [Northwind Traders solution](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/northwind-install) to be installed. If you want to use another table, use the appropriate solution or use the Default solution.

1.  Go to [Power Apps](https://make.powerapps.com), and select **Solutions** from the left navigation pane.

2.  Select **Northwind Traders**.

![Select solution ](media/image3.png)

3.  Search for the **Order Product** table.

![Order Product table ](media/image4.png)

4.  Select the **Order Product** table, and then select **Views**.

![Order Product   Views ](media/image5.png)

5.  Ensure that you see **Portal Search** in the views list.

![Portal Search view ](media/image6.png)

If the Portal Search view doesn't already exist, select **Add view**, enter the name as **Portal Search**, and then select **Create**.

![Add a view ](media/image7.png)

![Add the Portal Search view ](media/image8.png)

6.  Ensure appropriate columns are added to the view for search.

![Add columns ](media/image9.png)

7.  If you edited the view, be sure to select **Save**, and then **Publish** before you continue.

![Save and publish ](media/image10.png)

## Step 3: Create table permissions

1.  Sign in to [Power Apps](https://make.powerapps.com).

2.  Select **Apps** in the left navigation pane, and then select to open the **Portal Management** model-driven app.  

3.  Select **Table Permissions** in the left navigation pane.

4.  Select **New**.

![New Table Permission record ](media/image11.png)

5.  Enter the name as **Northwind Products Read All**, and then select the appropriate **Access Type** and the **Read** privilege.

For this example, the **Global** access type is provided to the **nwind\_products** table.

![Access Type and Read permissions ](media/image12.png)

6.  Select **Save & Close**.

7.  Select and open **Northwind Products Read All**.

8.  Scroll down to the **Web Roles** section, and then select **Add Existing Web Role**.

![Add an existing web role ](media/image13.png)

9.  Search for **Authenticated Users**, and then select **Add**:

![Add authenticated users ](media/image14.png)

## Step 4: Add record details webpage

1.  Go to [Power Apps](https://make.powerapps.com), and select **Apps** in the left navigation pane.

2.  Select **More Commands** (…) for the portal, and then select **Edit** to open the portal in Power Apps Studio.

3.  Select **New Page** from the menu in the upper-left corner, and then select the **Blank** layout for the page.

![Graphical user interface  application Description automatically generated](media/image15.png)

4.  Enter the webpage name as **Order Products**.

5.  Select **Components** in the left navigation pane, and then add a **Form** component to this webpage.

![Graphical user interface  application  Word Description automatically generated](media/image16.png)

6.  Select the **Use existing** or **Create New** option on the right side of your workspace, choose the **View Products** form for the **nwind\_products** table, and then set **Mode** to **ReadOnly**.

## Step 5: Add a site marker for record details webpage

1.  Sign in to [Power Apps](https://make.powerapps.com).

2.  Select **Apps** in the left navigation pane, and select to open the **Portal Management** model-driven app.  

3.  Select **Site Marker** from the left navigation pane.

4.  Select **New**, and then create a new site marker by using the following details:

    - **Name:** **nwind\_products\_SearchResultPage**

    - **Page:** **Order Products**

![New site marker ](media/image17.png)

## Step 7: Verify global search functionality

1.  Browse to the portal with a user that has *Authenticated* **Web Role** assigned.

2.  Go to the search toolbar or the search page, and search for a known record.

For example, use the search keyword **Northwind Clam Chowder** to get the results associated with the **nwind\_products** table.

![Search results ](media/image18.png)

## 

## Limitation

-   Boosting relevance, searching, or filtering results by Dataverse column name configured in **Search/Query** SiteSettings are not supported.

- **fileter** parameter in **searchindex** liquid will not work

Ex: {% searchindex query: 'support', filter: ' +statecode:0'%} This will not filter matching search results that doesn't have 'statecode:0'.

-   Although **Portal Search** view can have any Operator in filter, only below list of Operators are applied to query the search results and others are ignored

Equals

Does not equal

Is greater than

Is greater than or equal to

Is less than

Is than or equal to

-   Related fields defined in **Portal Search** view as a **filter column** or **view column** are not supported by Dataverse search and hence ignored.

-   Attachment content and objects in file data type are not searched

### See also

- [Use faceted search](improve-portal-search-faceted-search.md)
- [File attachment search](search-file-attachment.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]