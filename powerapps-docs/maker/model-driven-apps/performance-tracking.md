---
title: Performance tracking in model-driven apps | Microsoft Docs
description: Learn how performance is tracked in model-driven apps
documentationcenter: ''
author: JesseParsons
ms.reviewer: matp
ms.service: powerapps
ms.topic: conceptual
ms.component: model
ms.date: 03/04/2020
ms.author: jeparson
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Tracking performance in model-driven apps

Model-driven apps use a custom performance tracking library to measure user actions. The measurements can be tracked by makers using the [Monitor tool](https://powerapps.microsoft.com/en-us/blog/monitor-now-supports-model-driven-apps/).

## Page KPI's
The performance tracking library creates key performance indicators (KPI's) for each user action. User actions include:
- Page navigations, such as edit forms, grids, and dashboards. 
- Command executions. 
