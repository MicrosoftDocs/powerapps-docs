---
title: Manage Telemetry Settings for the Power Apps CLI
description: Learn how to manage Power Apps CLI telemetry settings, view the current status, control data collection, and configure console output for debugging.
ms.author: pakempar
author: pavankm
ms.date: 08/13/2026
ms.topic: how-to
---

# Manage telemetry settings for the Power Apps CLI

This article explains how to manage Power Apps CLI telemetry settings so you can view the current status, enable or disable collection, and configure console output for debugging or support.

## Why enable telemetry?

When telemetry is enabled, the CLI can collect:

| Telemetry data | Description |
| --- | --- |
| Activity events | High-level actions, such as running commands or completing scenarios. |
| Error events | Failures and exceptions, including error names and messages. |
| Scenario timing | Start and stop events for key operations and their elapsed time. |
| Environment context | Non-personally identifiable metadata about the environment and region. |
| Tenant identifier | The current tenant ID when the CLI is authenticated. |

> [!NOTE]
> Telemetry failures never block CLI operations.

## Manage telemetry with CLI commands

Use the following commands to manage telemetry:

| Command | Description |
| --- | --- |
| [`pa telemetry enable`](../reference/cli.md#pa-telemetry-enable) | Enable telemetry collection. |
| [`pa telemetry disable`](../reference/cli.md#pa-telemetry-disable) | Disable telemetry collection. |
| [`pa telemetry status`](../reference/cli.md#pa-telemetry-status) | Display the current telemetry settings. |

For example:

```bash
pa telemetry disable
pa telemetry status
```

These settings persist across CLI runs.

## Configure console output

The CLI stores user-configurable settings in `userSettings.json` in the `.powerapps-cli` configuration directory.

# [Windows](#tab/windows)

The `.powerapps-cli` folder is located in the location designated by the `USERPROFILE` environment variable.

You can create the file manually or use the following PowerShell script:

```powershell
$settingsPath = Join-Path $env:USERPROFILE ".powerapps-cli\userSettings.json"
$settingsDir = Split-Path $settingsPath
if (-not (Test-Path $settingsDir)) { New-Item -ItemType Directory -Path $settingsDir -Force }
$settings = @{
    enabled = $true
    consoleOnly = $false
    outputToConsole = $false
}
$settings | ConvertTo-Json | Set-Content $settingsPath
```

# [Linux or Mac](#tab/linuxormac)

The `.powerapps-cli` folder is located in the location designated by the `HOME` environment variable.

You can create the file manually or use the following script:

```bash
mkdir -p "$HOME/.powerapps-cli" && cat > "$HOME/.powerapps-cli/userSettings.json" <<'EOF'
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": false
}
EOF
```

---

The file supports the following properties:

```json
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": false
}
```

| Property | Description |
| --- | --- |
| `enabled` | Indicates whether remote telemetry is enabled. |
| `consoleOnly` | Writes telemetry only to the console and doesn't send it remotely. |
| `outputToConsole` | Mirrors remotely sent telemetry events to the console. |

### Telemetry enabled, remote only (default)

If the file doesn't exist, remote telemetry is enabled and telemetry isn't written to the console.

```json
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": false
}
```

### Telemetry fully disabled

```json
{
  "enabled": false,
  "consoleOnly": false,
  "outputToConsole": false
}
```

Set `outputToConsole` to `true` if you still want to see events.

### Telemetry enabled, remote, and console

The system sends events remotely and prints them locally.


```json
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": true
}
```

### Console-only telemetry (no remote send)

To write telemetry to the console without sending it remotely, use:

```json
{
  "enabled": false,
  "consoleOnly": true,
  "outputToConsole": false
}
```

- `enabled` is effectively ignored for remote sending.
- `outputToConsole` isn't required because console logging is implied.

## Pipe telemetry to a file

When console output is enabled, you can redirect output from a command such as [`pa app add data-source`](../reference/cli.md#pa-app-add-data-source) to a file for debugging or support.

### Windows Command Prompt

```cmd
pa app add data-source ... > telemetry.log 2>&1
```

### PowerShell (Windows, macOS, Linux)

```powershell
pa app add data-source ... | Out-File -FilePath telemetry.log -Encoding utf8
```

## Related information

- [Power Apps CLI command reference](../reference/cli.md)
