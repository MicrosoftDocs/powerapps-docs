---
title: "System configuration"
description: "Power Apps code apps system configuration"
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 06/22/2026
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---

# System configuration

This article provides information on the configuration for Power Apps code apps.

## Hosted app code

When you publish a code app to Power Platform by using [pac code push](/power-platform/developer/cli/reference/code#pac-code-push), the compiled app assets are hosted on a publicly accessible endpoint. This endpoint doesn't currently support IP-based access restrictions. Because code apps authenticate with Microsoft Entra ID, use [Conditional Access](/entra/identity/conditional-access/policy-block-by-location#create-a-conditional-access-policy) to control access by location or IP. Don't store sensitive user or organizational data in the app. Store this kind of data in a data source so the content is retrieved after end-users playing the app go through authentication and authorization checks.

## Hide the Power Apps header when playing an app

To hide the header that appears when you play the app, append a `hideNavBar=true` query string parameter to the URL of an app when you share it.

**Before**: Header is visible

`https://apps.powerapps.com/play/e/{environment id}/a/{app id}`

**After**: Header is hidden

`https://apps.powerapps.com/play/e/{environment id}/a/{app id}?hideNavBar=true`
