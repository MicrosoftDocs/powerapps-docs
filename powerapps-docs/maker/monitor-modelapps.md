---
title: Diagnose model-driven app issues with Monitor for Power Apps | Microsoft Docs
description: Learn how to diagnose model-driven app issues using Monitor
author: hasharaf
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.reviewer: Mattp123
ms.date: 11/16/2020
ms.author: hasharaf
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Debug a model-driven app with Monitor

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

Monitor can help you debug and diagnose problems and help you build faster, more reliable apps. Monitor provides a deep view into how an app runs by providing a log of all activities in your app as the app runs.

This feature gives you a better understanding of how the formulas contained in your app work so you can improve performance and identify any errors or problems.

For more information about when you should monitor an app, see [Monitor overview](monitor-overview.md). To run Monitor with a canvas app, see [Debugging canvas apps with Monitor](monitor-canvasapps.md).

## Use Monitor to diagnose a model-driven app

1. Sign into Power Apps, and then select **Apps** from the left navigation pane.
1. Select the model-driven app that you want to monitor, and then select **Monitor** on the command bar.
1. In the web page that opens, select **Play model-driven app** to open your app.

   :::image type="content" source="media/monitor-play-app.png" alt-text="Play model-driven app command":::
   > [!NOTE]
   > Alternatively, you can run a model-driven app and add “&monitor=true” to the end of the URL in the browser. Then, select **Monitor** on the command bar to start a monitoring session in a new tab.

1. After the app is opened from Monitor, you’ll see a **Join monitor debug session?** dialog box. This lets you know that any data from the app will be sent to the Monitor owner. Select **Join**. Events begin to flow to the Monitor-driven app session screen as they occur in the app.

   :::image type="content" source="media/monitor-model-session.png" alt-text="Monitor session with events displayed":::

1. Select an event to display additional information in the right pane. 

   :::image type="content" source="media/monitor-right-pane.png" alt-text="More information displayed in the right pane":::

## Events monitored

Page navigations, command executions, form saves, and other major actions will send key performance indicators and network events to Monitor.

### FullLoad

FullLoad signifies the complete load of a page navigation, such as an edit form load. This event waits for certain network requests to complete and all rendering to finish, so the form can be ready before FullLoad completes.

   :::image type="content" source="media/monitor-fullload.png" alt-text="Fullload event":::

Select a FullLoad event to display the **Details** tab.

   :::image type="content" source="media/monitor-fullload-details.png" alt-text="Fulload event details":::

The FullLoad event captures many statistics about the page load.  You can see the task edit form loaded in 506 ms, and selecting the row reveals information in the property pane. You can see details on customScriptTime (time spend execute custom JavaScript), loadType (0 = first time loading page type, 1 = first time loading entity, 2  = first time loading record, 3 = exact record has been visited), and FormId (form identifier for further diagnosis).  Expanding **Attribution** gives a breakdown of custom JS execution time by type, publisher, solution, version, web resource, and method.  This can help identify bottlenecks in form load time.

### Network

The **Network** events reveal details about each request made from the app.

:::image type="content" source="media/monitor-network.png" alt-text="Network event":::

Select a Network event to display the **Details** tab.

:::image type="content" source="media/monitor-network-details.png" alt-text="Network event details":::

### See also
[Use Monitor to troubleshoot model-driven app form behavior](model-driven-apps/monitor-form-checker.md)