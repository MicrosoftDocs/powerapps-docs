---
title: "How to: Analyze data requests and responses"
description: "Learn how to filter network traces in browser dev tools to analyze code app data requests and responses with Power Apps code apps."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 02/02/2026
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Analyze data requests and responses

This article explains how to review code app data requests and responses in browser dev tools.

Browser developer tools (DevTools) are built-in tools in modern web browsers that let you inspect network traffic, view console logs, debug JavaScript, and examine HTML/CSS. You can open DevTools by pressing <kbd>F12</kbd> or <kbd>Ctrl+Shift+I</kbd>, or by right-clicking a page element and choosing **Inspect** (on macOS use <kbd>Command+Option+I</kbd>). For detailed guidance, review the browser documentation:

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [Microsoft Edge DevTools](/microsoft-edge/devtools-guide-chromium/)
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

:::image type="content" source="media/code-app_browser-dev-tools-data-requests.png" alt-text="Image shows using the apihub.net string to filter requests for connectors using dev tools with the Edge browser":::
