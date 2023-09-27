---
title: Frequently asked questions and known issues about grids and views
description: Frequently asked questions and known issues about grids and views in Power Apps.
author: sericks
ms.component: pa-user
ms.topic: conceptual
ms.date: 03/09/2022
ms.subservice: end-user
ms.author: sericks
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# FAQs and known issues about grids and views

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

## How many levels of related table columns can I add to a view using the column editor?

You can add one level of related table columns using the column editor ([**Edit columns**](grid-filters-advanced.md#select-columns-in-the-column-editor)) on a grid page.

## How many levels of related table columns can I add to nested conditions in a view using the filter editor?

You can add up to 10 levels of related table conditions using the filter editor ([**Edit filters**](grid-filters-advanced.md#select-filter-conditions-in-the-filter-editor)) on a grid page.

## Known issues

- If you change the default display format for number, currency, time, or date and then filter data on a grid, the filter won't show your selected display format. The filters are still displayed in the system default format. In some cases, filtering might not work at all.

  To fix the issue, set the display format for number, currency, time, and date back to the default setting.

  1. In the upper-right corner, select the gear icon ![Gear icon.](media/selection-rule-gear-button.png), and then select **Personalization Settings**.

  2. On the **Formats** tab, change the number, currency, time, and date value back to the default setting.

    :::image type="content" source="./media/default-format.png" alt-text="A screenshot of the Personal Options page, showing the default format settings.":::

  We're working to correct this issue. Check here for updates.

- The advanced filter option on the Queues table doesn't work and displays this error message: *We are unable to display the filter conditions for this view.*

- Public views that include **Contains data** or **Does not contain data** filters don't appear in the list of saved views in legacy advanced find.

- When you open the **Edit filters** panel on certain Activity tables, you will see a condition filtering tables that are not valid for Unified Client. These conditions may not be a part of the FetchXML of the view.

- When you choose the **Search for rows in a table using advanced filters** option or the **Advanced find** button ![Advanced find button.](media/advanced_filter_icon.png "Advanced find button") when working in a  **Dynamics 365 - Custom** app with a [modern, advanced find experience](/power-platform/admin/settings-features) enabled, you might see a loading spinner appear indefinitely.

## See also

[Explore data in a view on a grid page](grid-filters.md)  
[Create and manage personal views on a grid page](grid-filters-advanced.md)  
[Advanced find](advanced-find.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
