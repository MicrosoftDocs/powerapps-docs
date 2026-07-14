---
title: Testing and monitoring in Power Apps
description: Master testing and monitoring in Power Apps. Use tools like Monitor and App Checker to troubleshoot, enhance performance, and improve app accessibility.
#customer intent: As a Power Apps maker, I want to use Power Apps tools so that I can diagnose and troubleshoot performance issues in my app.
ms.date: 02/27/2026
ms.topic: best-practice
author: robstand
ms.author: rachaudh
ms.reviewer: jhaskett-msft
---

# Monitoring and testing

Testing and monitoring help you build reliable, high-performance Power Apps. Use the following Power Apps built-in tools to debug and diagnose performance issues, identify formula errors, and ensure your app is accessible to all users.

## Monitor

Power Apps Monitor is a debugging tool that monitors a stream of events from a user's sessions to diagnose and troubleshoot problems related to performance.

You can use the tool from Power Apps Studio or to monitor published apps during runtime. To access monitor for a published app, go to the app, and select **Details** and then **Monitor**.

:::image type="content" source="media/image33.png" alt-text="Screenshot of Power Apps with the context menu open, showing Monitor in the menu.":::

The Monitor tool returns important information, such as:

- Nature of the operation, such as `Select`, `Load Screen`, `Navigate`, and `GetRows`.

- Result and Result info, which indicate whether the call is Success, Failure, or Warning. Result info includes information such as the number of rows returned, runtime errors like 404 or 429, and more.

- Duration, which is the amount of time taken to complete a given request.

- Data source and control information.

:::image type="content" source="media/image34.png" alt-text="Screenshot of Monitor results showing the columns described." lightbox="media/image34.png":::

On selecting an item in the grid, you can get more information, such as an overview of the event, the formula related to the selected event, and the HTTP request sent and response received. By default, the formula is only available during authoring, not for published apps. To show the formula for published apps, you need to enable an option in the app settings. Go to **File**, then **Settings**, and turn on **Debug published app**.

:::image type="content" source="media/image35.png" alt-text="Screenshot of the Settings dialog with the Debug published app option enabled.":::

This image shows the JSON details of an item selected in the event grid:

:::image type="content" source="media/image36.png" alt-text="Screenshot showing the JSON details of an item selected in the event grid." lightbox="media/image36.png":::

Learn more in [Use Monitor to get insights and recommendations for your app](../../maker/common/monitor-app-performance.md).

## App checker

App checker provides a streamlined method for identifying formula issues and addressing accessibility concerns within your app. You access it through the App checker icon in the Power Apps Studio toolbar.

The tool presents a comprehensive list of formula-related issues and actionable recommendations. Its purpose extends beyond error detection, as it also contributes to improving debugging efficiency, optimizing performance, and ensuring alignment with best practices.

:::image type="content" source="../../maker/canvas-apps/media/studio/pa-studio-app-checker.png" alt-text="Screenshot of Power Apps Studio highlighting the App checker icon and the App checker panel listing formula issues and accessibility recommendations.":::

Learn more about [App checker](/power-apps/maker/canvas-apps/power-apps-studio#app-checker).

## Accessibility checker

The Accessibility checker functions in a manner similar to the formula errors checker. It scrutinizes your app for potential accessibility problems and presents them in a comprehensive list. The Accessibility checker offers guidance such as on enabling keyboard and screen reader support within apps.

When you select an item from the Accessibility checker list, the relevant property opens for addressing the identified issue. Selecting the right chevron reveals detailed information along with a link to resources that provide insights into creating accessible apps.

:::image type="content" source="../../maker/canvas-apps/media/accessibility-checker/accessibility-checker-pane.png" alt-text="Screenshot of Accessibility checker pane in Power Apps showing a list of detected accessibility issues and guidance links.":::

Learn more about the [Accessibility checker in Power Apps](/power-apps/maker/canvas-apps/accessibility-checker).
