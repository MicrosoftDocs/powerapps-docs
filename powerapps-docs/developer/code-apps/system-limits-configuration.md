---
title: "Code Apps System Configuration"
description: "Learn about Power Apps code apps system configuration, including publicly hosted app assets and options to hide the header for all users or specific URLs."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 09/15/2026
ms.reviewer: jdaly
ms.topic: article
ai-usage: ai-assisted
contributors:
 - JimDaly
---

# Power Apps code apps system configuration

This article explains how Power Apps code apps host compiled app assets and how to control header visibility.

## Publicly hosted code app assets

When you publish a code app to Power Platform by using [`pa app push`](reference/cli.md#pa-app-push), you host the compiled app assets on a publicly accessible endpoint. This endpoint doesn't currently support IP-based access restrictions. Because code apps authenticate with Microsoft Entra ID, use [Conditional Access](/entra/identity/conditional-access/policy-block-by-location#create-a-conditional-access-policy) to control access by location or IP. Don't store sensitive user or organizational data in the app. Store this kind of data in a data source so the content is retrieved after end-users playing the app go through authentication and authorization checks.

## Hide the Power Apps header when playing an app

There are two ways to hide the header for all users of the app or for a specific app URL.

| Method | Description |
| --- | --- |
| [Configure the app setting to hide the header](#configure-the-app-setting-to-hide-the-header) | Use the Power Platform CLI to hide the header for all app users. |
| [Add a query string parameter to hide the header](#add-a-query-string-parameter-to-hide-the-header) | Add a parameter to hide the header for a specific app URL. |

### Configure the app setting to hide the header

Use [`pa app set-setting`](reference/cli.md#pa-app-set-setting) to hide the header by default. Run the command from the initialized code app project:

```console
pa app set-setting --show-header false
```

The command adds the setting to `power.config.json`. To review the current app settings, run:

```console
pa app get-settings
```

Publish the app to apply the setting:

```console
pa app push
```

To show the header again, set `--show-header` to `true`, and then publish the app.

### Add a query string parameter to hide the header

To hide the header for a specific app URL without changing the app setting, append the `hideNavBar=true` query string parameter when you share the URL.

**Header is visible:**

```text
https://apps.powerapps.com/play/e/{environment-id}/a/{app-id}
```

**Header is hidden:**

```text
https://apps.powerapps.com/play/e/{environment-id}/a/{app-id}?hideNavBar=true
```

If the URL already contains a query string parameter, append `&hideNavBar=true` instead.
