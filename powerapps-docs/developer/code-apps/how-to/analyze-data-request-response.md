---
title: "How to: Analyze data requests and responses (preview)"
description: "Learn how to filter network traces in browser dev tools to analyze code app data requests and responses with PowerApps code apps."
ms.author: alaug
author: alaug
ms.date: 09/17/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Analyze data requests and responses (preview)

This article explains how to review code app data requests and responses in browser dev tools.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

Browser developer tools (DevTools) are built-in tools in modern web browsers that let you inspect network traffic, view console logs, debug JavaScript, and examine HTML/CSS. You can open DevTools by pressing F12 or Ctrl+Shift+I, or by right-clicking a page element and choosing "Inspect" (on macOS use Command+Option+I). For detailed guidance see the browser documentation:

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [Microsoft Edge DevTools](https://learn.microsoft.com/microsoft-edge/devtools-guide-chromium/)
- [Firefox DevTools](https://developer.mozilla.org/docs/Tools)

## Prerequisites

You have a code app that connects to data as described in these articles:

- [How to connect to data](connect-to-data.md)
- [How to connect to Azure SQL](connect-to-azure-sql.md)

## View data requests in browser dev tools

You can filter data requests using these strings:

|Data source  |Filter string  |
|---------|---------|
|Connectors|`apihub.net`|
|Dataverse|`dynamics.com`|

This screenshot shows how to filter requests to connectors using dev tools in Edge using the `apihub.net` filter.

:::image type="content" source="media/code_app_browser_dev_tools_to_see_data_requests.png" alt-text="Image shows using the apihub.net string to filter requests for connectors using dev tools with the Edge browser":::
