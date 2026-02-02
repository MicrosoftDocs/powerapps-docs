---
title: "Power Apps SDK v1.0 Migration Guide"
description: "This is the migration guide for v1.0 of the Power Apps SDK."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 02/02/2026
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# Power Apps SDK v1.0 Migration Guide

As code apps approach general availability, we're improving the SDK and releasing version 1.0. These improvements include breaking changes from SDK version 0.3.21.

## Initialization isn't required

The SDK version 1.0 and later remove the `initialize` function. Apps must no longer import or call `initialize`. You can now make data calls, retrieve context, and interact with the platform directly without waiting on SDK initialization.

### Changes required

Review and apply the following changes to migrate existing code apps from SDK v0.3.21 to v1.0.

#### Remove imports of `initialize` function

Remove code like the following import statement, which is typically found at the top of your file.

```typescript
import { initialize } from '@microsoft/power-apps
```

#### Remove logic that waits on SDK initialization events

Remove code like the following example that invokes the `initialize` function and sets initialization state flags.

```typescript
useEffect(() => {
// Define an async function to initialize the Power Apps SDK
const init = async () => {
      try {
            await initialize(); // Wait for SDK initialization
            setIsInitialized(true); // Mark the app as ready for data operations
      } catch (err) {
            setError('Failed to initialize Power Apps SDK'); // Handle initialization errors
            setLoading(false); // Stop any loading indicators
      }
};

init(); // Call the initialization function when the component mounts
}, []);

useEffect(() => {
// Prevent data operations until the SDK is fully initialized
if (!isInitialized) return;

// Place your data reading logic here
}, []);
```

#### Remove initialization state flags

Remove code that checks initialization state flags, such as `isInitialized`, before using SDK methods.

## New `setConfig` API

A new `setConfig` API is available from [@microsoft/power-apps](https://www.npmjs.com/package/@microsoft/power-apps)/app. By using this API, apps can opt in to optional behaviors and observability features.

Supported config options include:

**Logger**: Supply a logger with a `logMetric` function. This `logMetric` function logs session and network metrics to the telemetry or monitoring service of your choice. For more information, see [How to: Set up Azure App Insights for your code app](set-up-azure-app-insights.md).
