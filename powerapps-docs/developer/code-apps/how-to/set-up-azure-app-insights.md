---
title: "How to: Set up Azure App Insights for your code app (preview)"
description: "Learn how to set up Azure App Insights for your code app"
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 1/20/2026
ms.reviewer: jdaly
ms.topic: how-to
---
# How to: Set up Azure App Insights for your code app (preview)

Azure Application Insights is a telemetry and monitoring service that helps you collect and analyze detailed telemetry from your applications. When you integrate it with Power Apps code apps, you can capture metrics such as session load performance and network request summaries. This integration gives you deeper visibility into how your app behaves in real‑world conditions. For more information, see the [Application Insights OpenTelemetry observability overview](/azure/azure-monitor/app/app-insights-overview).

> [!NOTE]
> This article shows **one example** of how to initialize and configure telemetry for your app. You can follow the same pattern to integrate any monitoring tool, not just Application Insights.
> Azure Application Insights complements [Power Platform Monitor](/power-platform/admin/monitoring/monitor-power-apps) by providing granular logs and custom events. However, it only captures telemetry after the app successfully loads. Startup failures - including problems caused by blocked files or failed initialization - don't appear here and only show up in Monitor.

## Prerequisites

- An Azure subscription.
- An Application Insights resource created in the Azure portal. 
- The connection string or instrumentation key from your App Insights resource. 

## Steps 

1. **Create an Application Insights resource**

- Sign in to the [Azure portal](https://ms.portal.azure.com/#home).
- Go to **Application Insights** and create a new resource.
- Copy the **Connection String** or **Instrumentation Key** from the resource overview.

1. **Install Application Insights SDK**

Add the npm package to your code app project:

```
npm install @microsoft/applicationinsights-web 
```

3. **Initialize Application Insights**

Add the logic to initialize Application Insights:

```typescript 

import { ApplicationInsights } from '@microsoft/applicationinsights-web'; 
 
const initializeAppInsights = () => { 
  const appInsights = new ApplicationInsights({ 
    config: { 
      connectionString: 'InstrumentationKey=<YOUR_KEY>;IngestionEndpoint=<YOUR_ENDPOINT>' 
    } 
  }); 
  appInsights.loadAppInsights(); 
  appInsights.trackPageView(); // Optional: Tracks page view 
  return appInsights; 
}; 

```

>[!NOTE] 
> Environment variables aren't yet supported for code apps. To manage per‑environment instrumentation keys, store values in Dataverse (for example, a settings table) or use [getContext()](/retrieve-context) to detect the environment and select the appropriate connection string from app constants.

1. **Configure the logger**

Provide a logger so the platform can forward session and network metrics to your monitoring system. The platform calls `logMetric` function with metrics like `sessionLoadSummary` and `networkLoadSummary`. You should only call this once. 

```typescript 
import { setConfig } from '@microsoft/power-apps/app' 
import type { IConfig } from '@microsoft/power-apps/app' 

setConfig({ 
  logger: {   
    logMetric: (value: Metric) => {   
      appInsights.trackEvent(   
        {   
          name: value.type, 
        }, 
          value.data   
      );   
    }   
  } 
}); 
```

**Additional guidance**

- **`logMetric` type**: Define it as `(value: Metric) => void` for clarity.
 
- **Logger interface**: 

```typescript 
interface ILogger { 
  logMetric?: (value: Metric) => void; 
} 
```

You can import it from: 

```typescript 
import type { ILogger } from '@microsoft/power-apps/telemetry' 
```

> [!NOTE] 
> This is just an example. You must implement `logMetric` so that metrics are sent to your monitoring tool of choice, not necessarily App Insights. The platform simply delivers metric payloads. Your implementation determines how they are handled.

1. **View logs in Azure portal** 

- Open your Application Insights resource. 
- Go to **Monitoring > Logs**. 
- Query the `customEvents` table to see session summaries and network requests.

The SDK currently provides two built‑in metric types:

```typescript 
type SessionLoadSummaryMetricData = { 
  successfulAppLaunch: boolean; 
  appLoadResult: 'optimal' | 'other'; 
  appLoadNonOptimalReason: 'interactionRequired' | 'throttled' | 'screenNavigatedAway' | 'other'; 
  timeToAppInteractive: number; 
} 

type NetworkRequestMetricData = { 
  url: string; 
  method:  string; 
  duration: number; 
  statusCode: number; 
  responseSize: number; 
} 
```

1. **(Optional) Log custom events**

You can log additional telemetry (beyond default metrics) by calling your monitoring tool's own APIs at the desired points in your app. For more advanced scenarios, refer to the official [Application Insights documentation](/azure/azure-monitor/app/app-insights-overview) for guidance. Note that you should avoid logging sensitive or unnecessary data and always follow your organization's compliance guidelines. 

## Sample queries 

To help you get started with analyzing your telemetry data, the following sample queries use Azure Application Insights Analytics (Kusto Query Language).

### App open performance 

This query shows app open performance metrics by day. Use this query to evaluate performance trends over time or after making changes. Use the 75th percentile of the `timeToAppInteractive` field to avoid noise caused by outliers. 

``` 
customEvents 
| where name == "sessionLoadSummary" 
| extend cd = parse_json(customDimensions) 
| extend cm = parse_json(customMeasurements)  
| extend timeToAppInteractive = todouble(cm["timeToAppInteractive"]) 
| extend successfulAppLaunch = tobool(cd.successfulAppLaunch) 
| where successfulAppLaunch == true 
| summarize percentile(timeToAppInteractive, 75)  
by bin(timestamp, 1d)  
| render timechart 
 ```

### Network request performance by URL 

This query analyzes custom `networkRequest` events in Application Insights. It extracts the URL and duration from the telemetry. It then summarizes daily counts and 75th percentile response times per URL. It visualizes the results as a time-series chart. 

``` 
customEvents 
| where name == "networkRequest" 
| extend cd = parse_json(customDimensions) 
| extend url = tostring(cd.url) 
| extend cm = parse_json(customMeasurements) 
| extend duration = todouble(cm.duration) 
| summarize  
count(), percentile(duration, 75) by url, bin(timestamp, 1d) 
| render timechart 
```


 


