---
title: "Migration Guide v1.0.1"
description: "This is the migration guide for v.1.0.1 of the Power Apps SDK."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 1/20/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:

---

# Power Apps SDK v1.0.1 Migration Guide

This guide applies to apps built using SDK 0.3.21 or earlier.

## Breaking changes

The initialize API has been fully removed in SDK 1.0.1. Apps must no longer import or call `initialize`. You can now make data calls, retrieve context, and interact with the platform directly without waiting on SDK initialization.

**Required action**

- Remove all imports of `initialize` ((e.g., `import { initialize } from '@microsoft/...'`)
- Remove any logic that waits on SDK initialization events
- Remove related state flags (e.g., isInitialized)

## Key changes

**New setConfig API**

A new setConfig API is available from `@microsoft/apps-powerapps/app`. This allows apps to opt in to optional behaviors and observability features.

Supported config options include:

**Logger**: Supply a logger with a `logMetric` function. This logMetric function will be used to log session and network metrics to the telemetry or monitoring service of your choice. See [How to set up Azure Application Insights](/how-to/set-up-azure-app-insights) for more information.






