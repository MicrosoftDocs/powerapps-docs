---
title: "System configuration (preview)"
description: "Power Apps code apps system configuration"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---

# System configuration (preview)

This article contains information on the configuration for Power Apps code apps.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Hosted app code

When a code app is published to Power Platform using [pac code push](/power-platform/developer/cli/reference/code#pac-code-push), the code is hosted on a publicly accessible endpoint. Sensitive user or organizational data shouldn't be stored in the app. Store this kind of data in a data source so the content is retrieved after end-users playing the app go through authentication and authorization checks.

## Hide the Power Apps header when playing an app

To hide the header that appears when you play the app, append a `hideNavBar=true` query string parameter to the url of an app when you share it.

**Before**: Header is visible

`https://apps.powerapps.com/play/e/{environment id}/a/{app id}`

**After**: Header is hidden

`https://apps.powerapps.com/play/e/{environment id}/a/{app id}?hideNavBar=true`
