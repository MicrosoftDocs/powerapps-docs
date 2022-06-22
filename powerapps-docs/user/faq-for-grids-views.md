---
title: Frequently asked questions and known issues about grids and views
description: Frequently asked questions and known issues about grids and views in Power Apps.
author: mduelae
manager: kvivek
ms.component: pa-user
ms.topic: conceptual
ms.date: 03/09/2022
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
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

## See also

[Explore data in a view on a grid page](grid-filters.md)  
[Create and manage personal views on a grid page](grid-filters-advanced.md)  
[Advanced find](advanced-find.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
