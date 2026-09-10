---
title: Troubleshoot issues in the native mobile app (preview)
description: Troubleshoot Native mobile issues fast. Resolve "plugin source was not found" errors, invalid QR server URLs, and unrecognized slash commands with proven fixes.
author: shwetamurkute
ms.author: ruchidixit
ms.reviewer: smurkute
ms.date: 09/07/2026
ms.topic: troubleshooting-problem-resolution
---

# Troubleshoot issues in the native mobile app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]


This article helps you troubleshoot common issues in Power Apps native mobile apps.

## Installation
| Problem | Resolution |
|----------|----------|
|The plugin doesn't appear or won't install| - Confirm that your coding agent supports agent plugins. <br> - In VS Code, search Extensions for `@agentPlugins mobile-app`, then install the mobile-app plugin. <br> - Restart or reload VS Code after installation. <br> - If the plugin is still unavailable, ask your administrator whether organizational policies block agent plugins.|
|VS Code reports that the plugin source wasn't found|- Close VS Code. <br> - Delete the cached plugin folder under `%USERPROFILE%\.vscode\agent-plugins\github.com\microsoft\power-platform-skills/tree/main/plugins/mobile-apps`. <br> - Reopen VS Code and search Extensions for `@agentPlugins mobile-app` to reinstall it, published by Microsoft.
|`node` or `npm` isn't found, or `/create-mobile-app` fails at prerequisite checks| - Install latest version of Node.js and npm. Learn more in [Prerequisites](overview.md#prerequisites) <br> - Restart your terminal and coding agent. <br> - Confirm the installation with `node --version` and `npm --version`.

## Connection
| Problem | Resolution |
|----------|----------|
|Offline data is missing| Check the following items in order: <br> - `IsAvailableOffline` and `ChangeTrackingEnabled` are set (run `/enable-tables-offline`). <br> - The profile is published. <br> - The user is assigned. <br> - The table is in scope. <br> - The column is included in `selectedColumns`. <br> - The relationship is traversed. <br> - The initial sync completed. <br> - Schema changes are reconciled after `/add-dataverse`.
|Invalid server URL when scanning|- Scan the dev server QR code from your terminal to load the bundle. <br> - Sign in. <br> - Navigate inside the loaded app to your scanner screen and scan the business code there. <br> - Make sure the phone and the authoring device are on the same network.
|Sign-in fails or uses the wrong account|- Retry the connection and choose the correct organizational account. <br> - If your host offers connection options, select browser sign-in or provide the account email as a login hint.

## App authoring
| Problem | Resolution |
|----------|----------|
|The agent doesn't recognize a command|Some hosts namespace plugin commands. Try `/mobile-app:create-mobile-app` instead of `/create-mobile-app`. Run `/help` to see the command list that your installed version actually exposes.|
|Controls, connectors, or data sources are missing|- Confirm that the plugin is connected to the intended app and environment. <br> - Add the required connectors and data sources, then ask your agent to list them again. <br> - Check whether organizational data policies restrict what's available.|
|Generation stopped partway through|Re-run the same command from the same folder. The agent reads `memory-bank.md` and resumes from where it stopped rather than starting over.|