---
title: Monitor your apps performance
description: Get valuable insights and recommendations for your app using Monitor.
author: dalajogun
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 8/12/2025
ms.subservice: canvas-maker
ms.author: damialajogun
search.audienceType: 
  - maker
contributors:
  - mduelae
  - damialajogun
---
#  Use Monitor to get insights and recommendations for your app

Monitor in Power Apps offers insights and recommendations to enhance app performance. It provides makers with detailed information on their app's performance and actionable steps to improve their apps.


## Prerequisites

To use this feature, your administrator must enable certain analytics and monitoring settings in the Power Platform Admin Center. More information: [Monitoring experiences for makers](/power-platform/admin/monitoring/monitoring-overview#monitoring-experiences-for-makers)

## Open and pin Monitor

1. Sign in to [Power Apps](https://make.powerapps.com).
1. On the left navigation, select **Apps**.
1. On the command bar, select **Monitor**.
1. On the left navigation pane, select the :::image type="content" source="../canvas-apps/media/intro-maker-portal/pin-button.png" alt-text="Pin button next to Monitor"::: pin button next to **Monitor**.


## Use Monitor 

The **Monitor** page displays metric cards at the top, highlighting the top three underperforming apps for each metric. If all apps perform well on a specific metric, then no apps are listed in the card. Use the tabs underneath the cards to switch between viewing your model-driven and canvas apps. 

:::image type="content" source="media/monitor-apps/power-apps-monitor.png" alt-text="Monitor main screen showing app metrics":::

| Metric | Definition | Available for Canvas apps | Available for Model-driven apps |
| ------------- | ------------- |------------- | ------------- |
| **App open success rate**  | Indicates the percentage of app launch attempts that successfully allowed end-users to access the app. This metric is calculated once every 24 hours.| Yes | Yes |
| **Time to interact**  | Measures the time end-users wait to access the first screen of an app. It doesn't include the time users wait to see all data presented on the first screen, such as filling in rows of a gallery. This metric is calculated every 24 hours and is measured using percentiles, with the 75th percentile being reported. | Yes | No |
| **Time to full load**  | Measures the time end-users wait to see all data displayed on the first screen of an app. In the app launch lifecycle, this metric follows the **Time to interact** phase. This metric is calculated every 24 hours and is measured using percentiles, with the 75th percentile being reported.| Yes | No |
| **Row summary dwell time** | The time (in seconds) that end users spend on the expanded AI row summary of a main form. | No | Yes |


### View metrics and recommendations for an app

  When you select an app on the  **Monitor** page a side pane opens and display more data for each metric, including a data chart for the last 30 days.

1. On **Monitor** page, select an app.

1. To view recommendations for an app, select the app’s name to open the side panel. The chart shows a callout with a recommended action for improving the metric.

    :::image type="content" source="media/monitor-apps/monitor-side-pane.png" alt-text="App metrics and recommendations":::

  > [!IMPORTANT]
  > Recommendations are only available in Managed Environments. Please contact your admin to enable Managed Environments for access to recommendations.
