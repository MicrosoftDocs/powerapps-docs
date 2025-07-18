---
title: Visualize data in a view with Copilot (preview)
description: Learn how to visualize your data in a view using Copilot in Power Apps.
ms.date: 01/24/2025
ms.update-cycle: 180-days
ms.topic: how-to
ms.subservice: end-user
author: sriharibs-msft
ms.author: srihas
reviewer: shwetamurkute
ms.reviewer: smurkute
ms.component: pa-user
ms.collection: 
    - bap-ai-copilot 
search.audienceType: 
  - enduser
---

# Visualize data in a view with Copilot (preview)

[!INCLUDE [file-name](~/../shared-content/shared/preview-includes/preview-banner.md)]

Copilot enables you to visualize the data in the view in the form of a chart to help you understand trends, patterns and relations in your data easily. The visualization is interactive, based on the visible columns in the view, and can be personalized to support further data exploration.

## Prerequisites

- Copilot assistance is available for all model-driven apps on the web where the [modern, refreshed look](modern-fluent-design.md) is turned on.
- Your administrator must enable [Allow AI to generate charts to visualize the data in a view](/power-platform/admin/settings-features#natural-language-grid-and-view-search-preview) setting in Power Platform admin center.

[!INCLUDE [file-name](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

## Visualize data in a view

To use this Copilot visualization, your administrator must enable it. For more information on how to enable Copilot visualization, see [Manage feature settings](/power-platform/admin/settings-features).

When you navigate to a grid page, you can see the **Visualize** option on top of the page.

:::image type="content" source="media/visualize-data/visualize-data-button.png" alt-text="Screenshot that shows Visualize button on the page." lightbox="media/visualize-data/visualize-data-button.png":::

When you select **Visualize**, the chart pane opens next to the grid, complementing the table of rows. If the table has system or personal charts, the default chart for the table is shown. If the table doesn't have charts, Copilot generates a visualization for the view based on the visible columns and filters. The visualization is a chart that aggregates the data in the view.

:::image type="content" source="media/visualize-data/visualize-data-chart.png" alt-text="Screenshot showing data visualization in the form of a chart on the page." lightbox="media/visualize-data/visualize-data-chart.png":::

:::image type="content" source="media/visualize-data/visualize-data-chart-highlighted.png" alt-text="Screenshot showing highlighted chart to visualize the data on the page." lightbox="media/visualize-data/visualize-data-chart-highlighted.png":::

If Copilot generates a visualization for the view, you can edit the chart by changing the chart type, the columns that are visualized, or both. If you add or remove columns from the view, Copilot regenerates the chart based on the updated set of columns for the visualization. If you add or remove filters, Copilot refreshes the chart without changing the visualization. The asterisk (*) next to the chart name shows that the chart isn't saved yet.

:::image type="content" source="media/visualize-data/visualize-data-chart-top.png" alt-text="Screenshot showing three dots in the data visualization chart.":::

Select the three dots in the top-right corner of the chart pane, and then select **Save As** to save the chart.

:::image type="content" source="media/visualize-data/visualize-data-chart-top-options.png" alt-text="Screenshot showing options after clicking three dots in the data visualization chart.":::

Copilot automatically populates the chart name and description, but you can edit them to suit your needs. Select **Save** to save the chart.
You access the saved chart using the chart switcher in the chart pane. The **Visualize** icon next to the chart name indicates that it is an AI-generated chart, helping you distinguish it from other charts.

:::image type="content" source="media/visualize-data/visualize-data-chart-dropdown.png" alt-text="Screenshot showing dropdown with personal charts options.":::

To manage a personal chart, select the chart in the chart switcher, then select the three dots in the top-right corner of the chart pane. Select an option to delete, assign, or share the chart with others in your organization.

:::image type="content" source="media/visualize-data/visualize-data-options.png" alt-text="Screenshot showing detailed options after clicking in three dots.":::

Hover over the charts to examine data points or select chart elements to drill into the data. The grid filters rows automatically to match the selected area of the chart. Selecting the same area of the chart again toggles the selection and removes the filter.

> [!Note]
> Charts created with the legacy chart designer use the same styling as AI-generated charts. To learn how to turn off the styling update for charts created with the legacy chart designer, see [Manage feature settings](/power-platform/admin/settings-features).

## Visualize data in a view with natural language

You use natural language prompts in the Copilot bar on the grid page to visualize data in the view. Here are example prompts to help you understand the types of requests supported.

- *Visualize data as a bar chart.*  
- *Customers by location. Use the prompt [table name] by [column] generically depending on the table you're visualizing.*  
- *Trend of orders created during this fiscal year.*
- *Visualize average revenue per month as a column chart.*
- *Visualize high-priority cases as a chart.*  
- *Visualize data as a bubble chart.*  

:::image type="content" source="media/visualize-data/visualize-natural-language.png" alt-text="Screenshot showing natural language prompt for data visualization.":::

## Chart pane

:::image type="content" source="media/visualize-data/visualize-chart-pane.png" alt-text="Screenshot showing chart pane options in detail.":::

1. **Chart title**: AI-generated title for the chart based on the data and columns visualized.
1. **Chart switcher**: Lets you select and manage saved charts. Use it to switch between different charts, including AI-generated and personal charts, for the current view.
1. **Create new chart with AI**: AI-generated chart for the visualization that Copilot chose for this view.
1. **Commands to manage saved chart**: The **Commands to manage saved chart** appear as three dots in the top-right corner of the chart pane. They provide options to perform actions on saved charts.
1. **Expand**: Select **Expand** to expand the chart to full screen for a better view of the chart area.
1. **Close**: Select **Close** to close the chart pane.
1. **Chart selector**: List of eleven supported chart types – Pie, Donut, Bar, Column, Clustered Bar, Stacked Bar, Clustered Column, Stacked Column, Line, Histogram and Bubble chart.
1. **Edit chart columns**: This option allows you to customize the chart by selecting which columns from the view are visualized.
1. **Copy**: Select **Copy** to copy the chart as a PNG file to the clipboard.
1. **Feedback**: Select **Thumbs up** or **Thumbs Down** to provide feedback about the feature.

To provide feedback about the feature, select the thumbs up or down button on the chart pane, and provide detailed comments to help improve the feature.

## Related information

[Manage feature settings](/power-platform/admin/settings-features)  
[Responsible AI FAQ about Copilot visualizations on a view](/power-apps/maker/common/faq-visualize-view)   
