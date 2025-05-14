---
title: Advanced Live monitor concepts
description: Learn about advanced monitoring concepts related to Live monitor.
author: mattgon

ms.subservice: troubleshoot
ms.topic: concept-article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 11/14/2022
ms.author: austinj
search.audienceType: 
  - maker
contributors:
  - mduelae
  - mattgon
  - maustinjones
---

# Advanced monitoring concepts

In this article, you'll learn about downloading and uploading trace files in Live monitor, events supported by Live monitor, and scenarios that Live monitor doesn't support.

## Download and upload trace files

You can download the events listed in [Supported events](#supported-events) for offline analysis.
Events can be downloaded in .json or .csv format, and you can share them with
others. The .csv files can only be downloaded, not uploaded, but if you download the events
in .json format, you can upload them later into Live monitor for analysis. You can
also attach a trace file to support service requests, which can help speed up getting the solution to your problem.

![Download trace files.](media/monitor/download.png "Download trace files")

Select **Upload** to load a .json trace file to Live monitor. This option removes any events currently displayed in the Live monitor table and replaces the details with events contained in the trace file.

![Upload trace files.](media/monitor/upload.png "Upload trace files")

## Supported events

Live monitor supports several events for canvas apps and model-driven apps. The following table includes examples of the supported event categories and types.

| Canvas apps | Model-driven apps |
| - | - |
| <ul> <li> Data connectors </li> <li> Network events (error status codes highlighted) </li> <li> Screen load metrics </li> <li> Cross-screen dependency warning </li> <li> User actions such as *Navigate*, *Select*, and *SetProperty* </li> <li> Custom Trace() </li> <li> Delegated versus non-delegated queries </li> <li> Verbose switch (internal telemetry) </li> <li> Delegation </li> <li> Function </li> <li> Network </li> <li> Parsing </li> <li> Performance </li> <li> Scenario </li> <li> ScreenLoad </li> <li> Telemetry </li> <li> UserAction </li> <li> Verbose </li> </ul> | <ul> <li>	Form events, such as load and save  </li> <li> Network </li> <li> Page navigation</li> <li>Command executions </li> </ul> |

## Unsupported scenarios for Live monitor

Live monitor doesn't support the scenarios in the following table.

|Description  |App type  |
|---------|---------|
|Live monitor connected to a canvas app embedded in a model-driven app or custom page.     |  Canvas       |
|Live monitor connected to a SharePoint custom form app.     | Canvas        |
|Live monitor connected to a Microsoft Teams embedded app. As an alternative, you can play the app in a web player for diagnostics purposes.     | Canvas        |

### See also

[Debugging canvas apps with MonLive monitor](monitor-canvasapps.md)  
[Debugging model-driven apps with Live monitor](monitor-modelapps.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
