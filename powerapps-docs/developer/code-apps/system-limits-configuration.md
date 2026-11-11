---
title: "Configure Code Apps Hosting, Header, and Access Text"
description: "Learn about Power Apps code apps system configuration, including publicly hosted app assets, header visibility, and custom request-access text."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 11/10/2026
ms.reviewer: jdaly
ms.topic: article
ai-usage: ai-assisted
contributors:
 - JimDaly
---

# Power Apps code apps system configuration

This article explains how Power Apps code apps host compiled app assets, how to control header visibility, and how to customize the text shown when a user doesn't have access to an app.

## Publicly hosted code app assets

When you publish a code app to Power Platform by using [`pa app push`](reference/cli.md#pa-app-push), you host the compiled app assets on a publicly accessible endpoint. This endpoint doesn't currently support IP-based access restrictions. Because code apps authenticate with Microsoft Entra ID, use [Conditional Access](/entra/identity/conditional-access/policy-block-by-location#create-a-conditional-access-policy) to control access by location or IP. Don't store sensitive user or organizational data in the app. Store this kind of data in a data source so the content is retrieved after end-users playing the app go through authentication and authorization checks.

## Hide the Power Apps header when playing an app

There are two ways to hide the header for all users of the app or for a specific app URL.

| Method | Description |
| --- | --- |
| [Configure the app setting to hide the header](#configure-the-app-setting-to-hide-the-header) | Use the Power Apps CLI to hide the header for all app users. |
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

To configure the header interactively, run [`pa app set-setting`](reference/cli.md#pa-app-set-setting) without setting flags and select `show-header`. At **Show the app header bar?**, select **Yes** to show the header or **No** to hide it.

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

## Customize the request-access text

Customize the title and message that appear when a user doesn't have access to your code app. Use the message to explain how to request access, such as contacting an administrator.

> [!IMPORTANT]
> Custom text doesn't grant access or change app permissions. To grant access, share the app with the user by using [`pa app share`](reference/cli.md#pa-app-share).

Run the following command from an initialized code app project that contains a `power.config.json` file:

```console
pa app set-setting --customize-request-access true --request-access-title "Request access" --request-access-message "Contact your administrator to request access."
```

To configure the text interactively, run [`pa app set-setting`](reference/cli.md#pa-app-set-setting) without setting flags and select `customize-request-access`. Choose whether to enable customization. When you enable it, enter the title and message at the prompts. When you disable it, the command skips the content prompts and preserves the saved title and message.

Review the local settings, and then publish the app to apply your changes:

```console
pa app get-settings
pa app push
```

Use [`pa app get-settings --json`](reference/cli.md#pa-app-get-settings) to read the settings as JSON.

To disable customization, run the following commands. Disabling customization preserves the saved title and message for later use.

```console
pa app set-setting --customize-request-access false
pa app push
```

### App settings in power.config.json

The CLI stores header visibility and request-access customization in the `appSettings` object in `power.config.json`. For example, the following configuration hides the header and enables custom request-access text:

```json
{
  "appSettings": {
    "showHeader": false,
    "customizeRequestAccess": {
      "enabled": true,
      "title": "Request access",
      "messageBody": "Contact your administrator to request access."
    }
  }
}
```

Both settings are optional. Use [`pa app set-setting`](reference/cli.md#pa-app-set-setting) to update them.

| Property | Requirements and default behavior |
| --- | --- |
| `showHeader` | A Boolean value. If omitted, the header is shown. |
| `customizeRequestAccess.enabled` | A Boolean value. If omitted, customization is disabled. |
| `customizeRequestAccess.title` | Required when customization is enabled. Must be nonblank and no more than 100 characters. Optional when disabled, but any provided value must meet the same requirements. |
| `customizeRequestAccess.messageBody` | Required when customization is enabled. Must be nonblank and no more than 1,000 characters. Optional when disabled, but any provided value must meet the same requirements. |

[`pa app set-setting`](reference/cli.md#pa-app-set-setting) updates only the fields you specify and preserves omitted fields and unrelated settings. It validates the merged settings before saving. You can replace invalid saved field values by supplying valid values, but malformed settings containers or a result that still contains invalid values are rejected. [`pa app push`](reference/cli.md#pa-app-push) also validates settings before publishing.
