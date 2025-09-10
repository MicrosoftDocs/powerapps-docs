---
title: "Power Apps code apps system limits and configuration (Preview)"
description: "Power Apps code apps system limits and configuration"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---

# System configuration (Preview)

This article contains information on the configuration for Power Apps code apps.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Hosted app code

When a code app is published to Power Platform (e.g. when using pac code push) app code is hosted on a publicly accessible endpoint. Sensitive user or organizational data should not be stored in the app and they should be stored in a data source so the content is retrieved after end-users playing the app go through authentication and authorization checks. 

## Hide the Power Apps header when playing an app

You can hide the header that appears when playing an app adding `hideNavBar=true` as a query string parameter. In practice, append this to the app link before sharing the app link.

**Before**

`https://apps.powerapps.com/play/e/{environment id}/a/{app id}`

**After**

`https://apps.powerapps.com/play/e/{environment id}/a/{app id}?hideNavBar=true`


