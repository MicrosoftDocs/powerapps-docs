---
title: Use Monitor to troubleshoot page behavior in model-driven apps with Power Apps
description: Monitor can help you debug and diagnose problems with custom pages. Discover how to troubleshoot page behavior in model-driven apps using the Monitor tool.
ms.custom: ""
ms.date: 10/18/2024
ms.reviewer: "matp"
ms.subservice: mda-maker
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "troubleshooting"
author: "aorth"
ms.author: "mspilde"
tags: 
search.audienceType: 
  - maker
---
# Use Monitor to troubleshoot page behavior in model-driven apps

Monitor can help you debug and diagnose problems, which help you build faster, more reliable model-driven apps. Monitor provides a deep view into how an app runs by providing a log of all activities in your app as it runs.

  > [!IMPORTANT]
  > Monitor must be run on the model-driven app and not directly on a custom page.

## Start a Monitor session

There are two ways to open a Monitor session.

- [From Power Apps](#from-power-apps)
- [From a model-driven app](#from-a-model-driven-app)

### From Power Apps

1. Sign in to [Power Apps](https://make.powerapps.com/), select **Apps**.
1. Select **...** next to the model-driven app or on the global command bar, and then select **Monitor**.

   :::image type="content" source="media/create-monitor-session.png" alt-text="Sample model-driven app":::

1. On the Monitor page, select **Play model-driven** app on the command bar.
1. When prompted, select **Join**.
1. The app loads in a new browser tab with a message indicating the monitoring session. Switch back to the Monitor tab to view activity.
   :::image type="content" source="media/monitored-app-session.png" alt-text="Monitored app session with message This app is currently connected to a monitor session." lightbox="media/monitored-app-session.png":::

### From a model-driven app

1. Play your model-driven app.
2. Add `&monitor=true` to the end of the URL in your web browser, and then refresh the page.
3. Select **Monitor** on the command bar.

    > ![Location of Monitor button in global command bar](https://user-images.githubusercontent.com/69216748/146047014-b9428da5-138a-4ccf-b74c-b45a0a0685b9.png)

## Filter monitored activity

When you filter on a model-driven app custom page-related events in Monitor, you can get information about related tables, tables, controls, and components, such as on a custom page, in Monitor as your app runs.

:::image type="content" source="media/add-component-to-model-app/monitor-app-with-custom-page.png" alt-text="Monitoring a model-driven app that has a custom page using the canvas app gallery control" lightbox="media/add-component-to-model-app/monitor-app-with-custom-page.png":::

For example, to filter on the custom page that uses the `Gallery1` control, select the **Control** column header > **Filter by**, enter *Gallery1*, and then select **Apply**.

For more information about model-driven app monitoring, go to [Debug a model-driven app with Monitor](../monitor-modelapps.md)

## Close a Monitor session

To close the monitoring session, close the browser tab where the monitored model-driven app is playing.

## Next steps

[Use Monitor to troubleshoot model-driven app form behavior](monitor-form-checker.md)
