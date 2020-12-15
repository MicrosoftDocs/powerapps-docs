---
title: Advanced monitoring concepts related to Monitor. | Microsoft Docs
description: Learn about advanced monitoring concepts related to Monitor.
author: hasharaf
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/19/2020
ms.author: hasharaf
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Advanced monitoring concepts

In this article, you'll learn about how to download, upload trace files in Monitor, events supported by Monitor, and unsupported scenarios.

## Download and upload trace files

You can download the events that are shown in the table for offline analysis.
Events can be downloaded in a .json or a .csv format, and can be shared with
others. The .csv files can only be downloaded. But if you export the events
in .json format, you can them back into the monitor tool for analysis. You can
also attach a trace file to support service requests helping speed-up the
solution to your problem.

![Download trace files](media/monitor/download.png "Download trace files")

Select **Upload** to load a .json trace file to Monitor. The upload option will remove any events currently displayed in the Monitor table, and replace the details with the events contained in the trace file.

![Upload trace files](media/monitor/upload.png "Upload trace files")

## Supported Events

Monitor supports several events for canvas apps and model-driven apps. Here are some examples of the supported event categories and types:

| Canvas apps | Model-driven apps |
| - | - |
| <ul> <li> Data connectors </li> <li> Network events (error status codes highlighted) </li> <li> Screen load metrics </li> <li> Cross-screen dependency warning </li> <li> User actions such as *Navigate*, *Select*, *SetProperty* </li> <li> Custom Trace() </li> <li> Delegated versus non-delegated queries </li> <li> Verbose switch (internal telemetry) </li> <li> Delegation </li> <li> Function </li> <li> Network </li> <li> Parsing </li> <li> Performance </li> <li> Scenario </li> <li> ScreenLoad </li> <li> Telemetry </li> <li> UserAction </li> <li> Verbose </li> </ul> | <ul> <li>	Form events, such as load and save  </li> <li> Network </li> <li> Page navigations</li> <li> command executions </li> </ul> |

## Unsupported scenarios for Monitor

The following scenarios aren't supported when using Monitor:

|Description  |App type  |
|---------|---------|
|Monitor connected to apps running on a mobile device (native players).     |  Canvas    |
|Monitor connected to canvas app embedded in a model-driven app or custom page.     |  Canvas       |
|Monitor connected to SharePoint custom form app.     | Canvas        |
|Monitor connected to Teams embedded app. As an alternative, play the app in a web player for diagnostics purposes.     | Canvas        |
|Monitor isn't supported on Internet Explorer version 11.     |  Canvas and model-driven       |

### See also

- [Monitor canvas apps using Monitor](monitor-canvasapps.md)
- [Monitor model-driven apps using Monitor](monitor-modelapps.md)
