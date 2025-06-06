---
title: Debugging canvas apps with Live monitor
description: Learn about debugging canvas apps by using Live monitor.
author: mattgon

ms.subservice: troubleshoot
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 11/14/2024
ms.author: austinj
search.audienceType: 
  - maker
contributors:
  - mduelae
  - mattgon
  - maustinjones
---

# Debugging canvas apps with Live monitor

Live monitor is available by default for all canvas apps. Using Live monitor, you can trace events as they occur in a canvas app during the authoring experience in Power Apps Studio, or you can use Monitor to debug the published version of a canvas app. More information: [Live monitor overview](monitor-overview.md)

## Get started with Live monitor in canvas apps
<!--markdownlint-disable MD036-->
**To open Monitor when authoring an app**

1. Sign in to [Power Apps](https://make.powerapps.com/).

1. Create a [new app](canvas-apps/get-started-test-drive.md), or [edit an existing app](canvas-apps/edit-app.md).

1. On the left pane, select **Advanced tools**.

1. Select **Open live monitor**.


This action opens Live monitor in a new browser tab and connects it to your existing Power Apps Studio session.


A notification appears at the top to show the current monitoring session as a *Studio session*.

> [!TIP]
> Live monitor has no impact on your app. You can use Live monitor with any app in
a test environment or in production.

<a name="open-monitor-for-published-app"></a>
## Open Live monitor for a published app

You can also use Live monitor to debug the published app in the web player.

**To open Live monitor for a published app**

1. Sign in to [Power Apps](https://make.powerapps.com/).

1. On the left pane, select **Apps**.

1. Select an app from the list.

1. Select the drop-down menu next to **Details** and then select, **Live monitor**. 

1. Select **Play published app**.

    ![Play published app.](media/monitor/play-published-app.png "Play published app")

This action opens the published app in a new browser tab and connects it to your current Live monitor session. You'll immediately see events in Live monitor when the app is loaded in the web player, and as you interact with the published app.

Live monitor also displays a notification that the monitoring session that's currently open is for the published version of the app.

![Published app session.](media/monitor/published-app-session.png "Published app session")

### For apps running on Power Apps mobile (preview)

Follow the above steps, but select **Copy monitor link** instead of **Play published app**. Use the copied link on your device to open a monitored session for the published app. Make sure the link is opened using [Power Apps mobile](../mobile/run-powerapps-on-mobile.md), not a browser.

> [!NOTE]
> **Copy monitor link** is available in https://make.preview.powerapps.com

![Copy monitor link.](media/monitor-copy-link.png "Copy monitor link")

### Setting: Debug published app

If you want to view the source expressions in Live Monitor for the published app, you need to turn on the setting to publish the expressions with the app. This setting is similar to generating a debug file in traditional development. Publishing source expressions with your app is optional. Even when this setting is off, you'll be able to see the events happening in your app, but you won't be able to map these events to specific expressions or formulas.

To enable this setting, go to **File** > **Settings**, and then turn on **Debug published app**.

> [!NOTE]
> Enabling this setting has a detrimental impact on the performance of your app for all your users. To minimize the impact, disable this setting as soon as you no longer need to view source expressions when debugging your published app.

![Debug published app.](media/monitor/debug-published-app.png "Debug published app")

### View events in Live monitor

To view events from your app, play the app in Power Apps Studio. Live monitor will then
display the table of events as they're occurring, along with specific details.

![View events as they occur.](media/monitor/monitor-events-occurring.png "View events as they occur")

## Example: Using Live monitor with canvas apps

In this example, you'll use the Northwind Sample Data app included with
the [Northwind sample solution](canvas-apps/northwind-install.md).

The *Northwind sample solution* is a canvas app that loads sample data into Microsoft Dataverse. You can also create a new app or use an existing app instead.

### Background

Consider the scenario where an app has been deployed, and the initial version of the app experiences performance degradation. The app also intermittently generates errors with no clear pattern. Loading data in the app succeeds most of the time, but fails sometimes.

When you check Live monitor, you see data operations as expected. However, you also see several responses that have HTTP status code 429, indicating that there have been too many requests in a specific timeframe.

When you select such an event, you see the error as "Rate limit exceeded. Try again in XX seconds."

![Example scenario - error 429.](media/monitor/error-429.png "Example scenario - error 429")

### **Analysis**

The problem needs further analysis to understand why requests are getting
throttled. In Live monitor, you see that for each **createRow** call, there are
several **getRows** requests from the **ProgressCount.Text** property, each to a different entity. These entities aren't the entities the app is creating rows for. The **ProgressCount.Text** formula is seen in Live monitor, as shown in the following image.

![Error 429 - Formula.](media/monitor/error-429-formula.png "Error 429 - Formula")

For each record added, the formula is evaluated again and **CountRows** is
called on several entities. This behavior results in **getRows** in the log,
because **CountRows** isn't delegated for Dataverse. For each single
request to add a record, you're potentially making 12 additional requests to
count the rows in each entity.

These extra requests intermittently cause errors because the Dataverse platform is throttling the requests to the service. This also explains the overall performance problem.

## Next steps

[Collaborative debugging with Live monitor](monitor-collaborative-debugging.md)

### See also

[Advanced monitoring](monitor-advanced.md)  
[Debugging model-driven apps with Monitor](monitor-modelapps.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
