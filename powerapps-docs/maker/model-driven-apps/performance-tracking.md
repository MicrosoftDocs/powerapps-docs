---
title: Performance tracking in model-driven apps | Microsoft Docs
description: Learn how tperformance is tracked in model-driven apps
documentationcenter: ''
author: JesseParsons
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
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

# Performance tracking in model-driven apps

Model-driven apps use a custom performance tracking library to measure user actions.  The measurements can be tracked by makers using the [Monitor tool](https://powerapps.microsoft.com/en-us/blog/monitor-now-supports-model-driven-apps/).

## Page KPI's
The performance tracking library creates KPI's (key performance indicators) for each user action.  User actions include:
- Page navigations (e.g. edit forms, grids, dashboards)
- Command executions