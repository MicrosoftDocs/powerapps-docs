---
title: Monitor your canvas apps performance (preview)
description: Get valuable insights and recommendations for your canvas app using Monitor.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 11/18/2024
ms.subservice: canvas-maker
ms.author: kaagar
search.audienceType: 
  - maker
contributors:
  - mduelae
  - damialajogun
---
#  Get insights and recommendations for your canvas app with Monitor (preview)

Monitor in Power Apps provides insights and recommendations to improve app performance. It equips makers with detailed information on their app's performance and provides actionable steps for improvement.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

To view your apps performance the TBD the following settings must be turn on in Power Platform Admin Center. 

- TBD add link to admin topics
- TBD add link to admin topics

## Open and pin Monitor

1. Sign in to [Power Apps](https://make.powerapps.com).
1. On the left navigation, select **Apps**.
1. On the commandbar, select **Monitor**.
1. Select **...** next to **Monitor** and select **Pin**.


## Use Monitor 

On the **Monitor** page, there are metric cards at the top of the page which highlight the top 3 underperforming apps for each metric. If all apps are performing well on a specific metric, then no apps will be listed in that card

| Metrics | Definition | Notes|
| ------------- | ------------- | -------------|
| App open success rate  | This measures the proportion of app launch attempts that resulted in end-users accessing the app successfully   | This metric is calculated once every 24 hours|
| Time to interact  | This measures end-user wait times to access the first screen of an app. This does not include time users wait to see all data that is to be presented on the first screen, e.g. filling in rows of a gallery  | This metric is calculated once every 24 hours. The metric is measured using percentiles. The 75th percentile is reported|
| Time to full load  | This measures end-user wait times to see all data displayed on the first screen of an app. In the app launch lifecycle, this metric is after Time to interact.  | This metric is calculated once every 24 hours. The metric is measured using percentiles. The 75th percentile is reported.|

To view Monitor details of a specific app, click on the app name in the grid. This will open a side panel with additional data for each metric, including a data chart for the last 30 days.


To view recommendations for an app, click on the app’s name to open the side panel. On the chart, you will see a callout with a recommended action for improving the metric.
Note: Recommendations are only available in Managed Environments. Please contact your admin to enable Managed Environments for access to recommendations.
